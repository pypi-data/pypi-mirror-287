"""Core pragmas

    Provides the core assembler directives."""

# Copyright 2002-2024 Michael C. Martin and additional contributors.
# You may use, modify, and distribute this file under the MIT
# license: See README for details.

import Ophis.CmdLine
import Ophis.IR as IR
import Ophis.Frontend as FE
import Ophis.Errors as Err
import math
import os.path

basecharmap = "".join([chr(x) for x in range(256)])
currentcharmap = basecharmap


def reset():
    global currentcharmap, basecharmap
    FE.loadedfiles = {}
    currentcharmap = basecharmap


def pragmaOutfile(ppt, line, result):
    "Sets the output file if it hasn't already been set"
    filename = line.expect("STRING").value
    line.expect("EOL")
    if type(filename) == str and Ophis.CmdLine.outfile is None:
        Ophis.CmdLine.outfile = filename


def pragmaListfile(ppt, line, result):
    "Sets the listing file if it hasn't already been set"
    filename = line.expect("STRING").value
    line.expect("EOL")
    if type(filename) == str and Ophis.CmdLine.listfile is None:
        Ophis.CmdLine.listfile = filename


def pragmaInclude(ppt, line, result):
    "Includes a source file"
    filename = line.expect("STRING").value
    line.expect("EOL")
    if type(filename) == str:
        result.append(FE.parse_file(ppt, filename))


def pragmaRequire(ppt, line, result):
    "Includes a source file at most one time"
    filename = line.expect("STRING").value
    line.expect("EOL")
    if type(filename) == str:
        result.append(FE.parse_file(ppt, filename, True))


def pragmaIncbin(ppt, line, result):
    "Includes a binary file"
    filename = line.expect("STRING").value
    offset = IR.ConstantExpr(0)
    size = None
    if str(line.lookahead(0)) == ",":
        line.pop()
        offset = FE.parse_expr(line)
        if str(line.lookahead(0)) == ",":
            line.pop()
            size = FE.parse_expr(line)
    line.expect("EOL")
    if type(filename) == str:
        try:
            f = open(os.path.join(FE.context_directory, filename), "rb")
            if offset.hardcoded and (size is None or size.hardcoded):
                # We know how big it will be, we can just use the values.
                # First check to make sure they're sane
                if offset.value() < 0:
                    Err.log("Offset may not be negative")
                    f.close()
                    return
                f.seek(0, 2)  # Seek to end of file
                if offset.value() > f.tell():
                    Err.log("Offset runs past end of file")
                    f.close()
                    return
                if size is not None:
                    if size.value() < 0:
                        Err.log("Length may not be negative")
                        f.close()
                        return
                    if offset.value() + size.value() > f.tell():
                        Err.log(".incbin length too long")
                        f.close()
                        return
                if size is None:
                    size = IR.ConstantExpr(-1)
                f.seek(offset.value())
                bytes = f.read(size.value())
                bytes = [IR.ConstantExpr(x) for x in bytes]
                result.append(IR.Node(ppt, "Byte", *bytes))
            else:
                # offset or length could change based on label placement.
                # This seems like an unbelievably bad idea, but since we
                # don't have constant prop it will happen for any symbolic
                # alias. Don't use symbolic aliases when extracting tiny
                # pieces out of humongous files, I guess.
                bytes = f.read()
                bytes = [IR.ConstantExpr(x) for x in bytes]
                if size is None:
                    size = IR.SequenceExpr([IR.ConstantExpr(len(bytes)),
                                            "-",
                                            offset])
                result.append(IR.Node(ppt, "ByteRange", offset, size, *bytes))
            f.close()
        except IOError:
            Err.log("Could not read " + filename)
            return


def pragmaCharmap(ppt, line, result):
    "Modify the character map."
    global currentcharmap, basecharmap
    if str(line.lookahead(0)) == "EOL":
        currentcharmap = basecharmap
    else:
        bytes = readRawData(line)
        try:
            base = bytes[0].data
            newsubstr = "".join([chr(x.data) for x in bytes[1:]])
            currentcharmap = currentcharmap[:base] + newsubstr + \
                             currentcharmap[base + len(newsubstr):]
            if len(currentcharmap) != 256 or base < 0 or base > 255:
                Err.log("Charmap replacement out of range")
                currentcharmap = currentcharmap[:256]
        except ValueError:
            Err.log("Illegal character in .charmap directive")


def pragmaCharmapbin(ppt, line, result):
    "Load a new character map from a file"
    global currentcharmap
    filename = line.expect("STRING").value
    line.expect("EOL")
    if type(filename) == str:
        try:
            f = open(os.path.join(FE.context_directory, filename), "rb")
            bytes = f.read()
            f.close()
        except IOError:
            Err.log("Could not read " + filename)
            return
        if len(bytes) == 256:
            currentcharmap = bytes
        else:
            Err.log("Character map " + filename + " not 256 bytes long")


def pragmaOrg(ppt, line, result):
    "Relocates the PC with no output"
    newPC = FE.parse_expr(line)
    line.expect("EOL")
    result.append(IR.Node(ppt, "SetPC", newPC))


def pragmaAdvance(ppt, line, result):
    "Outputs filler until reaching the target PC"
    newPC = FE.parse_expr(line)
    if str(line.lookahead(0)) == ",":
        line.pop()
        fillexpr = FE.parse_expr(line)
    else:
        fillexpr = IR.ConstantExpr(0)
    line.expect("EOL")
    result.append(IR.Node(ppt, "Advance", newPC, fillexpr))


def pragmaCheckpc(ppt, line, result):
    "Enforces that the PC has not exceeded a certain point"
    target = FE.parse_expr(line)
    line.expect("EOL")
    result.append(IR.Node(ppt, "CheckPC", target))


def pragmaAlias(ppt, line, result):
    "Assigns an arbitrary label"
    lbl = line.expect("LABEL").value
    target = FE.parse_expr(line)
    result.append(IR.Node(ppt, "Label", lbl, target))


def pragmaSpace(ppt, line, result):
    "Reserves space in a data segment for a variable"
    lbl = line.expect("LABEL").value
    size = line.expect("NUM").value
    line.expect("EOL")
    result.append(IR.Node(ppt, "Label", lbl, IR.PCExpr()))
    result.append(IR.Node(ppt, "SetPC",
                          IR.SequenceExpr([IR.PCExpr(), "+",
                                           IR.ConstantExpr(size)])))


def pragmaText(ppt, line, result):
    "Switches to a text segment"
    next = line.expect("LABEL", "EOL")
    if next.type == "LABEL":
        line.expect("EOL")
        segment = next.value
    else:
        segment = "*text-default*"
    result.append(IR.Node(ppt, "TextSegment", segment))


def pragmaData(ppt, line, result):
    "Switches to a data segment (no output allowed)"
    next = line.expect("LABEL", "EOL")
    if next.type == "LABEL":
        line.expect("EOL")
        segment = next.value
    else:
        segment = "*data-default*"
    result.append(IR.Node(ppt, "DataSegment", segment))


def pragmaCbmfloat(ppt, line, result):
    "Parses a string into a CBM BASIC format floating point number"
    data = []
    while True:
        try:
            v_str = line.expect("STRING").value
            v = float(v_str)
            if v == 0.0:
                data.extend([0,0,0,0,0])
            else:
                if v < 0.0:
                    sign = 128
                    v = -v
                else:
                    sign = 0
                expt = math.floor(math.log(v, 2))
                if expt >= -128 and expt <= 126:
                    mantissa = v / (2**expt)
                    m1 = (mantissa - 1.0) * 128 + sign
                    m2 = m1 * 256
                    m3 = m2 * 256
                    m4 = m3 * 256
                    data.extend([int(x) % 256 for x in [expt+129,m1,m2,m3,m4]])
                else:
                    Err.log("Floating point constant out of range")
        except ValueError:
            Err.log("Expected: floating point")
        next = line.expect(',', 'EOL').type
        if next == 'EOL':
            break
    bytes = [IR.ConstantExpr(x) for x in data]
    result.append(IR.Node(ppt, "Byte", *bytes))


def readRawData(line):
    "Read raw data from a comma-separated list"
    if line.lookahead(0).type == "STRING":
        data = [IR.ConstantExpr(ord(x))
                for x in line.expect("STRING").value]
    else:
        data = [FE.parse_expr(line)]
    next = line.expect(',', 'EOL').type
    while next == ',':
        if line.lookahead(0).type == "STRING":
            data.extend([IR.ConstantExpr(ord(x))
                         for x in line.expect("STRING").value])
        else:
            data.append(FE.parse_expr(line))
        next = line.expect(',', 'EOL').type
    return data


def readData(line):
    "Read charmap-translated data from a comma-separated list"
    if line.lookahead(0).type == "STRING":
        data = [IR.ConstantExpr(ord(x))
                for x in line.expect("STRING").value.translate(currentcharmap)]
    else:
        data = [FE.parse_expr(line)]
    next = line.expect(',', 'EOL').type
    while next == ',':
        if line.lookahead(0).type == "STRING":
            data.extend([IR.ConstantExpr(ord(x))
                         for x in line.expect("STRING").value.translate(currentcharmap)])
        else:
            data.append(FE.parse_expr(line))
        next = line.expect(',', 'EOL').type
    return data


def pragmaByte(ppt, line, result):
    "Raw data, a byte at a time"
    bytes = readData(line)
    result.append(IR.Node(ppt, "Byte", *bytes))


def pragmaWord(ppt, line, result):
    "Raw data, a word at a time, little-endian"
    words = readData(line)
    result.append(IR.Node(ppt, "Word", *words))


def pragmaDword(ppt, line, result):
    "Raw data, a double-word at a time, little-endian"
    dwords = readData(line)
    result.append(IR.Node(ppt, "Dword", *dwords))


def pragmaWordbe(ppt, line, result):
    "Raw data, a word at a time, big-endian"
    words = readData(line)
    result.append(IR.Node(ppt, "WordBE", *words))


def pragmaDwordbe(ppt, line, result):
    "Raw data, a dword at a time, big-endian"
    dwords = readData(line)
    result.append(IR.Node(ppt, "DwordBE", *dwords))


def pragmaScope(ppt, line, result):
    "Create a new lexical scoping block"
    line.expect("EOL")
    result.append(IR.Node(ppt, "ScopeBegin"))


def pragmaScend(ppt, line, result):
    "End the innermost lexical scoping block"
    line.expect("EOL")
    result.append(IR.Node(ppt, "ScopeEnd"))


def pragmaMacro(ppt, line, result):
    "Begin a macro definition"
    lbl = line.expect("LABEL").value
    line.expect("EOL")
    result.append(IR.Node(ppt, "MacroBegin", lbl))


def pragmaMacend(ppt, line, result):
    "End a macro definition"
    line.expect("EOL")
    result.append(IR.Node(ppt, "MacroEnd"))


def pragmaInvoke(ppt, line, result):
    macro = line.expect("LABEL").value
    if line.lookahead(0).type == "EOL":
        args = []
    else:
        args = readRawData(line)
    result.append(IR.Node(ppt, "MacroInvoke", macro, *args))
