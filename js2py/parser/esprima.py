from __future__ import unicode_literals
from espdata import *
from std_node import *

# len -> leng
# id -> d
# type -> typ
# str -> st
true = True
false = False
null = None

class EspParser:
    def __init__(self, source):
        source += ' ; ' # so that we dont have to care about index error in scanners anymore :)
        self.source = unicode(source)
        self.strict = None
        self.sourceType = None
        self.index = 0
        self.lineNumber = 1
        self.lineStart = 0
        self.hasLineTerminator = None
        self.lastIndex = None
        self.lastLineNumber = None
        self.lastLineStart = None
        self.startIndex = None
        self.startLineNumber = None
        self.startLineStart = None
        self.scanning = None
        self.length = len(source)
        self.lookahead = None
        self.state = None
        self.extra = {'tokens':[]}
        self.isBindingElement = None
        self.isAssignmentTarget = None
        self.firstCoverInitializedNameError = None

    def parse(self, source):
        self.source = source
        self.index = 0
        self.lineNumber = 0
        self.lineStart = 0
        self.length = len(source)
        self.skipComment()

    # 7.4 Comments

    def skipSingleLineComment(self, offset):
        start = self.index - offset;
        while self.index < self.length:
            ch = self.source[self.index];
            self.index += 1
            if isLineTerminator(ch):
                if (ord(ch) == 13 and ord(self.source[self.index]) == 10):
                    self.index += 1
                self.lineNumber += 1
                self.hasLineTerminator = True
                self.lineStart = self.index
                return

    def skipMultiLineComment(self):
        while self.index < self.length:
            ch = ord(self.source[self.index])
            if isLineTerminator(ch):
                if (ch == 0x0D and ord(self.source[self.index+1]) == 0x0A):
                    self.index += 1
                self.lineNumber += 1
                self.index += 1
                self.hasLineTerminator = True
                self.lineStart = self.index
            elif ch == 0x2A:
                # Block comment ends with '*/'.
                if ord(self.source[self.index+1]) == 0x2F:
                    self.index += 2
                    return
                self.index += 1
            else:
                self.index += 1
        self.tolerateUnexpectedToken()

    def skipComment(self):
        self.hasLineTerminator = False
        start = (self.index==0)
        while self.index < self.length:
            ch = ord(self.source[self.index])
            if isWhiteSpace(ch):
                self.index += 1
            elif isLineTerminator(ch):
                self.hasLineTerminator = True
                self.index += 1
                if (ch == 0x0D and ord(self.source[self.index]) == 0x0A):
                    self.index += 1
                self.lineNumber += 1
                self.lineStart = self.index
                start = True
            elif (ch == 0x2F): # U+002F is '/'
                ch = ord(self.source[self.index+1])
                if (ch == 0x2F):
                    self.index += 2
                    self.skipSingleLineComment(2)
                    start = True
                elif (ch == 0x2A):  # U+002A is '*'
                    self.index += 2
                    self.skipMultiLineComment()
                else:
                    break
            elif (start and ch == 0x2D): # U+002D is '-'
                # U+003E is '>'
                if (ord(self.source[self.index+1]) == 0x2D) and (ord(self.source[self.index+2]) == 0x3E):
                    # '-->' is a single-line comment
                    self.index += 3
                    self.skipSingleLineComment(3)
                else:
                    break
            elif (ch == 0x3C): # U+003C is '<'
                if self.source[self.index+1: self.index+4]=='!--':
                    # <!--
                    self.index += 4
                    self.skipSingleLineComment(4)
                else:
                    break
            else:
                break

    def scanHexEscape(self, prefix):
        code = 0
        leng = 4 if (prefix == 'u') else 2
        for i in xrange(leng):
            if self.index < self.length and isHexDigit(self.source[self.index]):
                ch = self.source[self.index]
                self.index += 1
                code = code * 16 + HEX_CONV[ch]
            else:
                return ''
        return unichr(code)

    def scanUnicodeCodePointEscape(self):
        ch = self.source[self.index]
        code = 0
        # At least, one hex digit is required.
        if ch == '}':
            self.throwUnexpectedToken()
        while (self.index < self.length):
            ch = self.source[self.index]
            self.index += 1
            if not isHexDigit(ch):
                break
            code = code * 16 + HEX_CONV[ch]
        if code > 0x10FFFF or ch != '}':
            self.throwUnexpectedToken()
        # UTF-16 Encoding
        if (code <= 0xFFFF):
            return unichr(code)
        cu1 = ((code - 0x10000) >> 10) + 0xD800;
        cu2 = ((code - 0x10000) & 1023) + 0xDC00;
        return unichr(cu1)+unichr(cu2)

    def ccode(self, offset=0):
        return ord(self.source[self.index+offset])

    def substr(self, le, offset=0):
        return self.source[self.index+offset:self.index+offset+le]

    def getEscapedIdentifier(self):
        d = self.source[self.index]
        ch = ord(d)
        self.index += 1
        # '\u' (U+005C, U+0075) denotes an escaped character.
        if (ch == 0x5C):
            if (ord(self.source[self.index]) != 0x75):
                self.throwUnexpectedToken()
            self.index += 1
            ch = self.scanHexEscape('u')
            if not ch or ch == '\\' or not isIdentifierStart(ch[0]):
                self.throwUnexpectedToken()
            d = ch
        while (self.index < self.length):
            ch = self.ccode()
            if not isIdentifierPart(ch):
                break
            self.index += 1
            d += unichr(ch)

            # '\u' (U+005C, U+0075) denotes an escaped character.
            if (ch == 0x5C):
                d = d[0: len(d)-1]
                if (self.ccode() != 0x75):
                    self.throwUnexpectedToken()
                self.index += 1
                ch = self.scanHexEscape('u');
                if (not ch or ch == '\\' or not isIdentifierPart(ch[0])):
                    self.throwUnexpectedToken()
                d += ch
        return d

    def getIdentifier(self):
        start = self.index
        self.index += 1
        while (self.index < self.length):
            ch = self.ccode()
            if (ch == 0x5C):
                # Blackslash (U+005C) marks Unicode escape sequence.
                self.index = start
                return self.getEscapedIdentifier()
            if (isIdentifierPart(ch)):
                self.index += 1
            else:
                break
        return self.source[start: self.index]

    def scanIdentifier(self):
        start = self.index

        # Backslash (U+005C) starts an escaped character.
        d = self.getEscapedIdentifier() if (self.ccode() == 0x5C) else self.getIdentifier()

        # There is no keyword or literal with only one character.
        # Thus, it must be an identifier.
        if (len(d)==1):
            type = Token.Identifier
        elif (isKeyword(d)):
            type = Token.Keyword
        elif (d == 'null'):
            type = Token.NullLiteral
        elif (i == 'true' or d == 'false'):
            type = Token.BooleanLiteral
        else:
            type = Token.Identifier;
        return {
            'type': type,
            'value': d,
            'lineNumber': self.lineNumber,
            'lineStart': self.lineStart,
            'start': start,
            'end': self.index
        }

    # 7.7 Punctuators

    def scanPunctuator(self):
        token = {
            'type': Token.Punctuator,
            'value': '',
            'lineNumber': self.lineNumber,
            'lineStart': self.lineStart,
            'start': self.index,
            'end': self.index
        }
        # Check for most common single-character punctuators.
        st = self.source[self.index]
        if st == '{':
            self.state.curlyStack.push('{')
            self.index += 1
        elif st == '}':
            self.index += 1
            self.state.curlyStack.pop()
        elif st in  {'.', '(', ')', ';', ',', '[', ']', ':', '?', '~'}:
            self.index += 1
        else:
            # 4-character punctuator.
            st = self.substr(4)
            if (st == '>>>='):
                self.index += 4
            else:
                # 3-character punctuators.
                st = st[0:3]
                if st in {'===', '!==', '>>>', '<<=', '>>='}:
                    self.index += 3
                else:
                    # 2-character punctuators.
                    st = st[0:2]
                    if st in {'&&','||','==','!=','+=','-=','*=' ,'/=' ,'++' , '--' , '<<', '>>', '&=', '|=', '^=', '%=', '<=', '>=', '=>'}:
                        self.index += 2
                    else:
                        # 1-character punctuators.
                        st = self.source[self.index]
                        if st in {'<', '>', '=', '!', '+', '-', '*', '%', '&', '|', '^', '/'}:
                            self.index += 1
        if self.index == token['start']:
            self.throwUnexpectedToken()
        token['end'] = self.index;
        token['value'] = st
        return token


    # 7.8.3 Numeric Literals

    def scanHexLiteral(self, start):
        number = ''
        while (self.index < self.length):
            if (not isHexDigit(self.source[self.index])):
                break
            number += self.source[self.index]
            self.index += 1
        if not number:
            self.throwUnexpectedToken()
        if isIdentifierStart(self.ccode()):
            self.throwUnexpectedToken()
        return {
            'type': Token.NumericLiteral,
            'value': int(number, 16),
            'lineNumber': self.lineNumber,
            'lineStart': self.lineStart,
            'start': start,
            'end': self.index}

    def scanBinaryLiteral(self, start):
        number = ''
        while (self.index < self.length):
            ch = self.source[self.index]
            if (ch != '0' and ch != '1'):
                break
            number += self.source[self.index]
            self.index += 1

        if not number:
            # only 0b or 0B
            self.throwUnexpectedToken()
        if (self.index < self.length):
            ch = self.source[self.index]
             # istanbul ignore else
            if (isIdentifierStart(ch) or isDecimalDigit(ch)):
                self.throwUnexpectedToken();
        return {
            'type': Token.NumericLiteral,
            'value': int(number, 2),
            'lineNumber': self.lineNumber,
            'lineStart': self.lineStart,
            'start': start,
            'end': self.index}


    def scanOctalLiteral(self, prefix, start):
        if isOctalDigit(prefix):
            octal = True
            number = '0' + self.source[self.index]
            self.index += 1
        else:
            octal = False
            self.index += 1
            number = ''
        while (self.index < self.length):
            if (not isOctalDigit(self.source[self.index])):
                break
            number += self.source[self.index]
            self.index += 1
        if (not octal and not number):
            # only 0o or 0O
            self.throwUnexpectedToken()
        if (isIdentifierStart(self.ccode()) or isDecimalDigit(self.ccode())):
            self.throwUnexpectedToken()
        return {
            'type': Token.NumericLiteral,
            'value': int(number, 8),
            'lineNumber': self.lineNumber,
            'lineStart': self.lineStart,
            'start': start,
            'end': self.index}

    def octalToDecimal(self, ch):
        # \0 is not octal escape sequence
        octal = (ch != '0')
        code = int(ch, 8)

        if (self.index < self.length and isOctalDigit(self.source[self.index])):
            octal = True
            code = code * 8 + int(self.source[self.index], 8)
            self.index += 1

            # 3 digits are only allowed when string starts
            # with 0, 1, 2, 3
            if (ch in '0123' and self.index < self.length and isOctalDigit(self.source[self.index])):
                code = code * 8 + int((self.source[self.index]), 8)
                self.index += 1
        return {
            'code': code,
            'octal': octal}


    def isImplicitOctalLiteral(self):
        # Implicit octal, unless there is a non-octal digit.
        # (Annex B.1.1 on Numeric Literals)
        for i in xrange(self.index + 1, self.length):
            ch = self.source[i];
            if (ch == '8' or ch == '9'):
                return False;
            if (not isOctalDigit(ch)):
                return True
        return True

    def scanNumericLiteral(self):
        ch = self.source[self.index]
        assert isDecimalDigit(ch) or (ch == '.'), 'Numeric literal must start with a decimal digit or a decimal point'
        start = self.index
        number = ''
        if ch != '.':
            number = self.source[self.index]
            self.index += 1
            ch = self.source[self.index]
            # Hex number starts with '0x'.
            # Octal number starts with '0'.
            # Octal number in ES6 starts with '0o'.
            # Binary number in ES6 starts with '0b'.
            if (number == '0'):
                if (ch == 'x' or ch == 'X'):
                    self.index += 1
                    return self.scanHexLiteral(start);
                if (ch == 'b' or ch == 'B'):
                    self.index += 1
                    return self.scanBinaryLiteral(start)
                if (ch == 'o' or ch == 'O'):
                    return self.scanOctalLiteral(ch, start)
                if (isOctalDigit(ch)):
                    if (self.isImplicitOctalLiteral()):
                        return self.scanOctalLiteral(ch, start);
            while (isDecimalDigit(self.ccode())):
                number += self.source[self.index]
                self.index += 1
            ch = self.source[self.index];
        if (ch == '.'):
            number += self.source[self.index]
            self.index += 1
            while (isDecimalDigit(self.source[self.index])):
                number += self.source[self.index]
                self.index += 1
            ch = self.source[self.index]
        if (ch == 'e' or ch == 'E'):
            number += self.source[self.index]
            self.index += 1
            ch = self.source[self.index]
            if (ch == '+' or ch == '-'):
                number += self.source[self.index]
                self.index += 1
            if (isDecimalDigit(self.source[self.index])):
                while (isDecimalDigit(self.source[self.index])):
                    number += self.source[self.index]
                    self.index += 1
            else:
                self.throwUnexpectedToken()
        if (isIdentifierStart(self.source[self.index])):
            self.throwUnexpectedToken();
        return {
            'type': Token.NumericLiteral,
            'value': float(number),
            'lineNumber': self.lineNumber,
            'lineStart': self.lineStart,
            'start': start,
            'end': self.index}

    # 7.8.4 String Literals

    def scanStringLiteral(self):
        st = ''
        octal = False

        quote = self.source[self.index]
        assert quote == '\''or quote == '"', 'String literal must starts with a quote'
        start = self.index;
        self.index += 1

        while (self.index < self.length):
            ch = self.source[self.index]
            self.index += 1
            if (ch == quote):
                quote = ''
                break
            elif (ch == '\\'):
                ch = self.source[self.index]
                self.index += 1
                if (not isLineTerminator(ch)):
                    if ch in 'ux':
                        if (self.source[self.index] == '{'):
                            self.index += 1
                            st += self.scanUnicodeCodePointEscape()
                        else:
                            unescaped = self.scanHexEscape(ch)
                            if (not unescaped):
                                self.throwUnexpectedToken() # with throw I don't know whats the difference
                            st += unescaped
                    elif ch=='n':
                        st += '\n';
                    elif ch=='r':
                        st += '\r';
                    elif ch=='t':
                        st += '\t';
                    elif ch=='b':
                        st += '\b';
                    elif ch=='f':
                        st += '\f';
                    elif ch=='v':
                        st += '\x0B'
                    elif st in '89':
                        self.throwUnexpectedToken() # again with throw....
                    else:
                        if isOctalDigit(ch):
                            octToDec = self.octalToDecimal(ch)
                            octal = octToDec['octal'] or octal
                            st += unichr(octToDec.code)
                        else:
                            st += ch
                else:
                    self.lineNumber += 1
                    if (ch == '\r' and self.source[self.index] == '\n'):
                        self.index += 1
                    self.lineStart = self.index
            elif isLineTerminator(ch):
                break
            else:
                st += ch;
        if (quote != ''):
            self.throwUnexpectedToken()
        return {
            'type': Token.StringLiteral,
            'value': st,
            'octal': octal,
            'lineNumber': self.lineNumber,
            'lineStart': self.startLineStart,
            'start': start,
            'end': self.index}

    def scanTemplate(self):
        cooked = ''
        terminated = False
        tail = False
        start = self.index
        head = (self.source[self.index]=='`')
        rawOffset = 2

        self.index += 1

        while (self.index < self.length):
            ch = self.source[self.index]
            self.index += 1
            if (ch == '`'):
                rawOffset = 1;
                tail = True
                terminated = True
                break
            elif (ch == '$'):
                if (self.source[self.index] == '{'):
                    self.state.curlyStack.push('${')
                    self.index += 1
                    terminated = True
                    break;
                cooked += ch
            elif (ch == '\\'):
                ch = self.source[self.index]
                self.index += 1
                if (not isLineTerminator(ch)):
                    if ch=='n':
                        cooked += '\n'
                    elif ch=='r':
                        cooked += '\r'
                    elif ch=='t':
                        cooked += '\t'
                    elif ch in 'ux':
                        if (self.source[self.index] == '{'):
                            self.index += 1
                            cooked += self.scanUnicodeCodePointEscape()
                        else:
                            restore = self.index
                            unescaped = self.scanHexEscape(ch)
                            if (unescaped):
                                cooked += unescaped
                            else:
                                self.index = restore
                                cooked += ch
                    elif ch=='b':
                        cooked += '\b'
                    elif ch=='f':
                        cooked += '\f'
                    elif ch=='v':
                        cooked += '\v'
                    else:
                        if (ch == '0'):
                            if isDecimalDigit(self.ccode()):
                                # Illegal: \01 \02 and so on
                                self.throwError(Messages.TemplateOctalLiteral)
                            cooked += '\0'
                        elif (isOctalDigit(ch)):
                            # Illegal: \1 \2
                            self.throwError(Messages.TemplateOctalLiteral)
                        else:
                            cooked += ch
                else:
                    self.lineNumber += 1
                    if (ch == '\r' and self.source[self.index] == '\n'):
                        self.index += 1
                    self.lineStart = self.index
            elif (isLineTerminator(ch)):
                self.lineNumber += 1
                if (ch == '\r' and self.source[self.index] =='\n'):
                    self.index += 1
                self.lineStart = self.index
                cooked += '\n'
            else:
                cooked += ch;
        if (not terminated):
            self.throwUnexpectedToken()

        if (not head):
            self.state.curlyStack.pop();

        return {
            'type': Token.Template,
            'value': {
                'cooked': cooked,
                'raw': self.source[start + 1, self.index - rawOffset]},
            'head': head,
            'tail': tail,
            'lineNumber': self.lineNumber,
            'lineStart': self.lineStart,
            'start': start,
            'end': self.index}

    def testRegExp(self, pattern, flags):
        #todo: you should return python regexp object
        return (pattern, flags)

    def scanRegExpBody(self):
        ch = self.source[self.index]
        assert ch == '/', 'Regular expression literal must start with a slash'
        st = ch
        self.index += 1

        classMarker = False
        terminated = False
        while (self.index < self.length):
            ch = self.source[self.index]
            self.index += 1
            st += ch
            if (ch == '\\'):
                ch = self.source[self.index]
                self.index += 1
                # ECMA-262 7.8.5
                if (isLineTerminator(ch)):
                    self.throwUnexpectedToken(None, Messages.UnterminatedRegExp)
                st += ch
            elif (isLineTerminator(ch)):
                self.throwUnexpectedToken(None, Messages.UnterminatedRegExp)
            elif (classMarker):
                if (ch == ']'):
                    classMarker = False
            else:
                if (ch == '/'):
                    terminated = True
                    break
                elif (ch == '['):
                    classMarker = True;
        if (not terminated):
            self.throwUnexpectedToken(None, Messages.UnterminatedRegExp)

        # Exclude leading and trailing slash.
        body = st[1:-1]
        return {
            'value': body,
            'literal': st}

    def scanRegExpFlags(self):
        st = ''
        flags = ''
        while (self.index < self.length):
            ch = self.source[self.index]
            if (not isIdentifierPart(ch)):
                break
            self.index += 1
            if (ch == '\\' and self.index < self.length):
                ch = self.source[self.index]
                if (ch == 'u'):
                    self.index += 1
                    restore = self.index
                    ch = self.scanHexEscape('u')
                    if (ch):
                        flags += ch
                        st += '\\u'
                        while restore < self.index:
                            st += self.source[restore]
                            restore += 1
                    else:
                        self.index = restore
                        flags += 'u'
                        st += '\\u'
                    self.tolerateUnexpectedToken()
                else:
                    st += '\\'
                    self.tolerateUnexpectedToken()
            else:
                flags += ch
                st += ch
        return {
            'value': flags,
            'literal': st}

    def scanRegExp(self):
        self.scanning = True
        self.lookahead = None
        self.skipComment()
        start = self.index

        body = self.scanRegExpBody()
        flags = self.scanRegExpFlags()
        value = self.testRegExp(body['value'], flags['value'])
        scanning = False
        return {
            'literal': body['literal'] + flags['literal'],
            'value': value,
            'regex': {
                'pattern': body['value'],
                'flags': flags['value']
            },
            'start': start,
            'end': self.index}

    def collectRegex(self):
        self.skipComment();
        return self.scanRegExp()

    def isIdentifierName(self, token):
        return token[type] in {1,3,4,5}

    #def advanceSlash(self): ???

    def advance(self):
        if (self.index >= self.length):
            return {
                'type': Token.EOF,
                'lineNumber': self.lineNumber,
                'lineStart': self.lineStart,
                'start': self.index,
                'end': self.index}
        ch = self.ccode()

        if isIdentifierStart(ch):
            token = self.scanIdentifier()
            if (self.strict and isStrictModeReservedWord(token['value'])):
                token['type'] = Token.Keyword
            return token
        # Very common: ( and ) and ;
        if (ch == 0x28 or ch == 0x29 or ch == 0x3B):
            return self.scanPunctuator()

        # String literal starts with single quote (U+0027) or double quote (U+0022).
        if (ch == 0x27 or ch == 0x22):
            return self.scanStringLiteral()

        # Dot (.) U+002E can also start a floating-point number, hence the need
        # to check the next character.
        if (ch == 0x2E):
            if (isDecimalDigit(self.ccode(1))):
                return self.scanNumericLiteral()
            return self.scanPunctuator();

        if (isDecimalDigit(ch)):
            return self.scanNumericLiteral()

        # Slash (/) U+002F can also start a regex.
        #if (extra.tokenize && ch === 0x2F) {
        #    return advanceSlash();

        # Template literals start with ` (U+0060) for template head
        # or } (U+007D) for template middle or template tail.
        if (ch == 0x60 or (ch == 0x7D and self.state.curlyStack[self.state.curlyStack.length - 1] == '${')):
            return self.scanTemplate()
        return self.scanPunctuator();

    #def collectToken(self):
    #    loc = {
    #        'start': {
    #            'line': self.lineNumber,
    #            'column': self.index - self.lineStart}}
    #
    #    token = self.advance()
    #
    #    loc['end'] = {
    #        'line': self.lineNumber,
    #        'column': self.index - self.lineStart}
    #    if (token['type'] != Token.EOF):
    #        value = self.source[token['start']: token['end']]
    #        entry = {
    #            'type': TokenName[token['type']],
    #            'value': value,
    #            'range': [token['start'], token['end']],
    #            'loc': loc}
    #        if (token.get('regex')):
    #            entry['regex'] = {
    #                'pattern': token['regex']['pattern'],
    #                'flags': token['regex']['flags']}
    #        self.extra['tokens'].append(entry)
    #    return token;


    def lex(self):
        self.scanning = True

        self.lastIndex = self.index
        self.lastLineNumber = self.lineNumber
        self.lastLineStart = self.lineStart

        self.skipComment()

        token = self.lookahead

        self.startIndex = self.index
        self.startLineNumber = self.lineNumber
        self.startLineStart = self.lineStart

        self.lookahead =  self.advance()
        self.scanning = False
        return token

    def peek(self):
        self.scanning = True

        self.skipComment()

        self.lastIndex = self.index
        self.lastLineNumber = self.lineNumber
        self.lastLineStart = self.lineStart

        self.startIndex = self.index
        self.startLineNumber = self.lineNumber
        self.startLineStart = self.lineStart

        self.lookahead = self.advance()
        self.scanning = False


    def createError(self, line, pos, description):
        error = JsSyntaxError('Line ' + line + ': ' + description);
        error.index = pos
        error.lineNumber = line
        error.column = pos - (self.lineStart if self.scanning else self.lastLineStart) + 1
        error.description = description
        return error

    # Throw an exception

    def throwError(self, messageFormat, *args):
        msg = messageFormat # todo replace appriopriate fields with args
        print 'TODO ERROR MSG:   ', msg, args
        raise self.createError(self.lastLineNumber, self.lastIndex, msg);

    def tolerateError(self, messageFormat, *args):
        return self.throwError(self, messageFormat, *args)

    # Throw an exception because of the token.

    def unexpectedTokenError(self, token={}, message=''):
        msg = message or Messages.UnexpectedToken
        if (token):
            typ = token['type']
            if (not message):
                if typ == Token.EOF: msg = Messages.UnexpectedEOS
                elif (typ == Token.Identifier): msg = Messages.UnexpectedIdentifier
                elif (typ == Token.NumericLiteral): msg = Messages.UnexpectedNumber
                elif (typ == Token.StringLiteral): msg = Messages.UnexpectedString
                elif (typ == Token.Template): msg = Messages.UnexpectedTemplate
                else: msg = Messages.UnexpectedToken;
                if (typ == Token.Keyword):
                    if (isFutureReservedWord(token['value'])):
                        msg = Messages.UnexpectedReserved
                    elif (self.strict and isStrictModeReservedWord(token['value'])):
                        msg = Messages.StrictReservedWord
            value = token['value']['raw'] if (typ == Token.Template)  else token['value']
        else:
            value = 'ILLEGAL'
        msg = msg.replace('%0', value)

        return (self.createError(token['lineNumber'], token['start'], msg) if (token and token.get('lineNumber')) else
               self.createError(self.lineNumber if self.scanning else self.lastLineNumber, self.index if self.scanning else self.lastIndex, msg))


    def throwUnexpectedToken(self, token={}, message=''):
        raise self.unexpectedTokenError(token, message)

    def tolerateUnexpectedToken(self, token={}, message=''):
        self.throwUnexpectedToken(token, message)

    # Expect the next token to match the specified punctuator.
    # If not, an exception will be thrown.

    def expect(self, value):
        token = self.lex()
        if (token['type'] != Token.Punctuator or token['value'] != value):
            self.throwUnexpectedToken(token)


    #/**
    # * @name expectCommaSeparator
    # * @description Quietly expect a comma when in tolerant mode, otherwise delegates
    # * to <code>expect(value)</code>
    # * @since 2.0
    # */
    def expectCommaSeparator(self):
        self.expect(',')

    # Expect the next token to match the specified keyword.
    # If not, an exception will be thrown.

    def expectKeyword(self, keyword):
        token = self.lex();
        if (token['type'] != Token.Keyword or token['value'] != keyword):
            self.throwUnexpectedToken(token)


    # Return true if the next token matches the specified punctuator.

    def match(self, value):
        return self.lookahead['type'] == Token.Punctuator and self.lookahead['value'] == value

    # Return true if the next token matches the specified keyword

    def matchKeyword(self, keyword):
        return self.lookahead['type'] == Token.Keyword and self.lookahead['value'] == keyword

    # Return true if the next token matches the specified contextual keyword
    # (where an identifier is sometimes a keyword depending on the context)

    def matchContextualKeyword(self, keyword):
        return self.lookahead.type == Token.Identifier and self.lookahead['value'] == keyword

    # Return true if the next token is an assignment operator

    def matchAssign(self):
        if (self.lookahead.type != Token.Punctuator):
            return False;
        op = self.lookahead['value']
        return op in {'=','*=', '/=','%=', '+=', '-=', '<<=', '>>=', '>>>=', '&=' , '^=' , '|='}

    def consumeSemicolon(self):
        # Catch the very common case first: immediately a semicolon (U+003B).
        if (self.source[self.startIndex] == ';' or self.match(';')):
            self.lex()
            return

        if (self.hasLineTerminator):
            return

        # TODO: FIXME(ikarienator): this is seemingly an issue in the previous location info convention.
        self.lastIndex = self.startIndex
        self.lastLineNumber = self.startLineNumber
        self.lastLineStart = self.startLineStart

        if (self.lookahead['type'] != Token.EOF and not self.match('}')):
            self.throwUnexpectedToken(self.lookahead)

    # // Cover grammar support.
    # //
    # // When an assignment expression position starts with an left parenthesis, the determination of the type
    # // of the syntax is to be deferred arbitrarily long until the end of the parentheses pair (plus a lookahead)
    # // or the first comma. This situation also defers the determination of all the expressions nested in the pair.
    # //
    # // There are three productions that can be parsed in a parentheses pair that needs to be determined
    # // after the outermost pair is closed. They are:
    # //
    # //   1. AssignmentExpression
    # //   2. BindingElements
    # //   3. AssignmentTargets
    # //
    # // In order to avoid exponential backtracking, we use two flags to denote if the production can be
    # // binding element or assignment target.
    # //
    # // The three productions have the relationship:
    # //
    # //   BindingElements <= AssignmentTargets <= AssignmentExpression
    # //
    # // with a single exception that CoverInitializedName when used directly in an Expression, generates
    # // an early error. Therefore, we need the third state, firstCoverInitializedNameError, to track the
    # // first usage of CoverInitializedName and report it when we reached the end of the parentheses pair.
    # //
    # // isolateCoverGrammar function runs the given parser function with a new cover grammar context, and it does not
    # // effect the current flags. This means the production the parser parses is only used as an expression. Therefore
    # // the CoverInitializedName check is conducted.
    # //
    # // inheritCoverGrammar function runs the given parse function with a new cover grammar context, and it propagates
    # // the flags outside of the parser. This means the production the parser parses is used as a part of a potential
    # // pattern. The CoverInitializedName check is deferred.

    def isolateCoverGrammar(self, parser):
        oldIsBindingElement = self.isBindingElement
        oldIsAssignmentTarget = self.isAssignmentTarget
        oldFirstCoverInitializedNameError = self.firstCoverInitializedNameError
        self.isBindingElement = true
        self.isAssignmentTarget = true
        self.firstCoverInitializedNameError = null
        result = parser()
        if (self.firstCoverInitializedNameError != null):
            self.throwUnexpectedToken(self.firstCoverInitializedNameError)
        self.isBindingElement = oldIsBindingElement
        self.isAssignmentTarget = oldIsAssignmentTarget
        self.firstCoverInitializedNameError = oldFirstCoverInitializedNameError
        return result

    def inheritCoverGrammar(self, parser):
        oldIsBindingElement = self.isBindingElement
        oldIsAssignmentTarget = self.isAssignmentTarget
        oldFirstCoverInitializedNameError = self.firstCoverInitializedNameError
        self.isBindingElement = true
        self.isAssignmentTarget = true
        self.firstCoverInitializedNameError = null
        result = parser()
        self.isBindingElement = self.isBindingElement and oldIsBindingElement
        self.isAssignmentTarget = self.isAssignmentTarget and oldIsAssignmentTarget
        self.firstCoverInitializedNameError = oldFirstCoverInitializedNameError or self.firstCoverInitializedNameError
        return result


    def parseArrayPattern(self):
        node = Node()
        elements = []
        self.expect('[');
        while (not self.match(']')):
            if (self.match(',')):
                self.lex()
                elements.append(null)
            else:
                if (self.match('...')):
                    restNode = Node()
                    self.lex()
                    rest = self.parseVariableIdentifier()
                    elements.append(restNode.finishRestElement(rest))
                    break
                else:
                    elements.append(self.parsePatternWithDefault())
                if (not self.match(']')):
                    self.expect(',')
        self.expect(']')
        return node.finishArrayPattern(elements)

    def parsePropertyPattern(self):
        node = Node()
        computed = self.match('[')
        if (self.lookahead.type == Token.Identifier):
            key = self.parseVariableIdentifier()
            if (self.match('=')):
                self.lex();
                init = self.parseAssignmentExpression()
                return node.finishProperty(
                    'init', key, false, WrappingNode(key).finishAssignmentPattern(key, init), false, false)
            elif (not self.match(':')):
                return node.finishProperty('init', key, false, key, false, true)
        else:
            key = self.parseObjectPropertyKey()
        self.expect(':')
        init = self.parsePatternWithDefault()
        return node.finishProperty('init', key, computed, init, false, false)

    def parseObjectPattern(self):
        node = Node()
        properties = []
        self.expect('{')
        while (not self.match('}')):
            properties.append(self.parsePropertyPattern())
            if (not self.match('}')):
                self.expect(',')
        self.lex()
        return node.finishObjectPattern(properties)

    def parsePattern(self):
        if (self.lookahead.type == Token.Identifier):
            return self.parseVariableIdentifier()
        elif (self.match('[')):
            return self.parseArrayPattern()
        elif (self.match('{')):
            return self.parseObjectPattern()
        self.throwUnexpectedToken(self.lookahead)

    def parsePatternWithDefault(self):
        startToken = self.lookahead

        pattern = self.parsePattern()
        if (self.match('=')):
            self.lex()
            right = self.isolateCoverGrammar(self.parseAssignmentExpression)
            pattern = WrappingNode(startToken).finishAssignmentPattern(pattern, right)
        return pattern

    # 11.1.4 Array Initialiser

    def parseArrayInitialiser(self):
        elements = []
        node = Node()

        self.expect('[')

        while (not self.match(']')):
            if (self.match(',')):
                self.lex()
                elements.append(null)
            elif (self.match('...')):
                restSpread = Node()
                self.lex()
                restSpread.finishSpreadElement(self.inheritCoverGrammar(self.parseAssignmentExpression))
                if (not self.match(']')):
                    self.isAssignmentTarget = self.isBindingElement = false
                    self.expect(',')
                elements.append(restSpread)
            else:
                elements.append(self.inheritCoverGrammar(self.parseAssignmentExpression))
                if (not self.match(']')):
                    self.expect(',')
        self.lex();

        return node.finishArrayExpression(elements)

    # 11.1.5 Object Initialiser

    def parsePropertyFunction(self, node, paramInfo):

        self.isAssignmentTarget = self.isBindingElement = false;

        previousStrict = self.strict;
        body = self.isolateCoverGrammar(self.parseFunctionSourceElements);

        if (self.strict and paramInfo.firstRestricted):
            self.tolerateUnexpectedToken(paramInfo.firstRestricted, paramInfo.message)
        if (self.strict and paramInfo.stricted):
            self.tolerateUnexpectedToken(paramInfo.stricted, paramInfo.message);

        self.strict = previousStrict;
        return node.finishFunctionExpression(null, paramInfo.params, paramInfo.defaults, body)

    def parsePropertyMethodFunction(self):
        node = Node();

        params = self.parseParams();
        method = self.parsePropertyFunction(node, params);
        return method;

    def parseObjectPropertyKey(self):
        node = Node()

        token = self.lex();

        # // Note: This function is called only from parseObjectProperty(), where
        # // EOF and Punctuator tokens are already filtered out.

        typ = token['type']

        if typ in [Token.StringLiteral, Token.NumericLiteral]:
            if self.strict and token['octal']:
                self.tolerateUnexpectedToken(token, Messages.StrictOctalLiteral);
            return node.finishLiteral(token);
        elif typ in  {Token.Identifier, Token.BooleanLiteral, Token.NullLiteral, Token.Keyword}:
            return node.finishIdentifier(token.value);
        elif typ==Token.Punctuator:
            if (token['value'] == '['):
                expr = self.isolateCoverGrammar(self.parseAssignmentExpression)
                self.expect(']')
                return expr
        self.throwUnexpectedToken(token)

    def lookaheadPropertyName(self):
        typ = self.lookahead['type']
        if typ in  {Token.Identifier, Token.StringLiteral, Token.BooleanLiteral, Token.NullLiteral, Token.NumericLiteral, Token.Keyword}:
            return true
        if typ == Token.Punctuator:
            return self.lookahead.value == '['
        return false

    # // This function is to try to parse a MethodDefinition as defined in 14.3. But in the case of object literals,
    # // it might be called at a position where there is in fact a short hand identifier pattern or a data property.
    # // This can only be determined after we consumed up to the left parentheses.
    # //
    # // In order to avoid back tracking, it returns `null` if the position is not a MethodDefinition and the caller
    # // is responsible to visit other options.
    def tryParseMethodDefinition(self, token, key, computed, node):
        if (token['type'] == Token.Identifier):
            # check for `get` and `set`;

            if (token['value'] == 'get' and self.lookaheadPropertyName()):
                computed = self.match('[');
                key = self.parseObjectPropertyKey()
                methodNode =  Node()
                self.expect('(')
                self.expect(')')
                value = self.parsePropertyFunction(methodNode, {
                    'params': [],
                    'defaults': [],
                    'stricted': null,
                    'firstRestricted': null,
                    'message': null
                })
                return node.finishProperty('get', key, computed, value, false, false)
            elif (token['value'] == 'set' and self.lookaheadPropertyName()):
                computed = self.match('[')
                key = self.parseObjectPropertyKey()
                methodNode =  Node()
                self.expect('(')

                options = {
                    'params': [],
                    'defaultCount': 0,
                    'defaults': [],
                    'firstRestricted': null,
                    'paramSet': {}
                }
                if (self.match(')')):
                    self.tolerateUnexpectedToken(self.lookahead);
                else:
                    self.parseParam(options);
                    if (options['defaultCount'] == 0):
                        options['defaults'] = []
                self.expect(')')

                value = self.parsePropertyFunction(methodNode, options);
                return node.finishProperty('set', key, computed, value, false, false);
        if (self.match('(')):
            value = self.parsePropertyMethodFunction();
            return node.finishProperty('init', key, computed, value, true, false)
        return null;

    def checkProto(self, key, computed, hasProto):
        if (computed == false and (key['type'] == Syntax.Identifier and key.name == '__proto__' or
            key['type'] == Syntax.Literal and key.value == '__proto__')):
            if (hasProto.value):
                self.tolerateError(Messages.DuplicateProtoProperty);
            else:
                hasProto.value = true;

    def parseObjectProperty(self, hasProto):
        token = self.lookahead
        node = Node()

        computed = self.match('[');
        key = self.parseObjectPropertyKey();
        maybeMethod = self.tryParseMethodDefinition(token, key, computed, node)

        if (maybeMethod):
            self.checkProto(maybeMethod.key, maybeMethod.computed, hasProto);
            return maybeMethod;

        #// init property or short hand property.
        self.checkProto(key, computed, hasProto);

        if (self.match(':')):
            self.lex();
            value = self.inheritCoverGrammar(self.parseAssignmentExpression)
            return node.finishProperty('init', key, computed, value, false, false)

        if (token['type'] == Token.Identifier):
            if (self.match('=')):
                self.firstCoverInitializedNameError = self.lookahead;
                self.lex();
                value = self.isolateCoverGrammar(self.parseAssignmentExpression);
                return node.finishProperty('init', key, computed,
                    WrappingNode(token).finishAssignmentPattern(key, value), false, true)
            return node.finishProperty('init', key, computed, key, false, true)
        self.throwUnexpectedToken(self.lookahead)

    def parseObjectInitialiser(self):
        properties = []
        hasProto = {'value': false}
        node = Node();

        self.expect('{');

        while (not self.match('}')):
            properties.append(self.parseObjectProperty(hasProto));

            if (not self.match('}')):
                self.expectCommaSeparator()
        self.expect('}');
        return node.finishObjectExpression(properties)

    def reinterpretExpressionAsPattern(self, expr):
        typ = (expr['type'])
        if typ in {Syntax.Identifier, Syntax.MemberExpression, Syntax.RestElement, Syntax.AssignmentPattern}:
            pass
        elif typ == Syntax.SpreadElement:
            expr['type'] = Syntax.RestElement
            self.reinterpretExpressionAsPattern(expr.argument)
        elif typ == Syntax.ArrayExpression:
            expr['type'] = Syntax.ArrayPattern
            for i in xrange(len(expr['elements'])):
                if (expr['elements'][i] != null):
                    self.reinterpretExpressionAsPattern(expr['elements'][i])
        elif typ == Syntax.ObjectExpression:
            expr['type'] = Syntax.ObjectPattern
            for i in xrange(len(expr['properties'])):
                self.reinterpretExpressionAsPattern(expr['properties'][i]['value']);
        elif Syntax.AssignmentExpression:
            expr['type'] = Syntax.AssignmentPattern;
            self.reinterpretExpressionAsPattern(expr['left'])
        else:
            #// Allow other node type for tolerant parsing.
            return

    def parseTemplateElement(self, option):

        if (self.lookahead['type'] != Token.Template or (option['head'] and not self.lookahead['head'])):
            self.throwUnexpectedToken()

        node = Node();
        token = self.lex();

        return node.finishTemplateElement({ 'raw': token['value']['raw'], 'cooked': token['value']['cooked'] }, token['tail'])

    def parseTemplateLiteral(self):
        node = Node()

        quasi = self.parseTemplateElement({ 'head': true })
        quasis = [quasi]
        expressions = []

        while (not quasi['tail']):
            expressions.append(self.parseExpression());
            quasi = self.parseTemplateElement({ 'head': false });
            quasis.append(quasi)
        return node.finishTemplateLiteral(quasis, expressions)

    # 11.1.6 The Grouping Operator

    def parseGroupExpression(self):
        self.expect('(');

        if (self.match(')')):
            self.lex();
            if (not self.match('=>')):
                self.expect('=>')
            return {
                'type': PlaceHolders.ArrowParameterPlaceHolder,
                'params': []}

        startToken = self.lookahead
        if (self.match('...')):
            expr = self.parseRestElement();
            self.expect(')');
            if (not self.match('=>')):
                self.expect('=>')
            return {
                'type': PlaceHolders.ArrowParameterPlaceHolder,
                'params': [expr]}

        self.isBindingElement = true;
        expr = self.inheritCoverGrammar(self.parseAssignmentExpression);

        if (self.match(',')):
            self.isAssignmentTarget = false;
            expressions = [expr]

            while (self.startIndex < self.length):
                if (not self.match(',')):
                    break
                self.lex();

                if (self.match('...')):
                    if (not self.isBindingElement):
                        self.throwUnexpectedToken(self.lookahead)
                    expressions.append(self.parseRestElement())
                    self.expect(')');
                    if (not self.match('=>')):
                        self.expect('=>');
                    self.isBindingElement = false
                    for i in xrange(len(expressions)):
                        self.reinterpretExpressionAsPattern(expressions[i])
                    return {
                        'type': PlaceHolders.ArrowParameterPlaceHolder,
                        'params': expressions}
                expressions.append(self.inheritCoverGrammar(self.parseAssignmentExpression))
            expr = WrappingNode(startToken).finishSequenceExpression(expressions);
        self.expect(')')

        if (self.match('=>')):
            if (not self.isBindingElement):
                self.throwUnexpectedToken(self.lookahead);
            if (expr['type'] == Syntax.SequenceExpression):
                for i in xrange(len(expr.expressions)):
                    self.reinterpretExpressionAsPattern(expr['expressions'][i])
            else:
                self.reinterpretExpressionAsPattern(expr);
            expr = {
                'type': PlaceHolders.ArrowParameterPlaceHolder,
                'params': expr['expressions'] if expr['type'] == Syntax.SequenceExpression  else [expr]}
        self.isBindingElement = false
        return expr

    # 11.1 Primary Expressions

    def parsePrimaryExpression(self):
        if (self.match('(')):
            self.isBindingElement = false;
            return self.inheritCoverGrammar(self.parseGroupExpression)
        if (self.match('[')):
            return self.inheritCoverGrammar(self.parseArrayInitialiser)

        if (self.match('{')):
            return self.inheritCoverGrammar(self.parseObjectInitialiser)

        typ = self.lookahead['type']
        node =  Node();

        if (typ == Token.Identifier):
            expr = node.finishIdentifier(self.lex().value);
        elif (typ == Token.StringLiteral or typ == Token.NumericLiteral):
            self.isAssignmentTarget = self.isBindingElement = false
            if (self.strict and self.lookahead.octal):
                self.tolerateUnexpectedToken(self.lookahead, Messages.StrictOctalLiteral)
            expr = node.finishLiteral(self.lex())
        elif (typ == Token.Keyword):
            self.isAssignmentTarget = self.isBindingElement = false
            if (self.matchKeyword('function')):
                return self.parseFunctionExpression()
            if (self.matchKeyword('this')):
                self.lex()
                return node.finishThisExpression()
            if (self.matchKeyword('class')):
                return self.parseClassExpression()
            self.throwUnexpectedToken(self.lex())
        elif (typ == Token.BooleanLiteral):
            isAssignmentTarget = self.isBindingElement = false
            token = self.lex();
            token['value'] = (token.value == 'true')
            expr = node.finishLiteral(token)
        elif (typ == Token.NullLiteral):
            self.isAssignmentTarget = self.isBindingElement = false
            token = self.lex()
            token['value'] = null;
            expr = node.finishLiteral(token)
        elif (self.match('/') or self.match('/=')):
            self.isAssignmentTarget = self.isBindingElement = false;
            self.index = self.startIndex;
            token = self.scanRegExp();   # hehe, here you are!
            self.lex();
            expr = node.finishLiteral(token);
        elif (typ == Token.Template):
            expr = self.parseTemplateLiteral()
        else:
            self.throwUnexpectedToken(self.lex());
        return expr;

    # 11.2 Left-Hand-Side Expressions

    def parseArguments(self):
        args = [];

        self.expect('(');
        if (not self.match(')')):
            while (self.startIndex < self.length):
                args.append(self.isolateCoverGrammar(self.parseAssignmentExpression))
                if (self.match(')')):
                    break
                self.expectCommaSeparator()
        self.expect(')')
        return args;

    def parseNonComputedProperty(self):
        node =  Node()

        token = self.lex();

        if (not self.isIdentifierName(token)):
            self.throwUnexpectedToken(token)
        return node.finishIdentifier(token['value'])

    def parseNonComputedMember(self):
        self.expect('.')
        return self.parseNonComputedProperty();

    def parseComputedMember(self):
        self.expect('[')

        expr = self.isolateCoverGrammar(self.parseExpression)
        self.expect(']')

        return expr

    def parseNewExpression(self):
        node = Node()
        self.expectKeyword('new')
        callee = self.isolateCoverGrammar(self.parseLeftHandSideExpression)
        args = self.parseArguments() if self.match('(') else []

        self.isAssignmentTarget = self.isBindingElement = false

        return node.finishNewExpression(callee, args)

    def parseLeftHandSideExpressionAllowCall(self):
        previousAllowIn = self.state['allowIn']

        startToken = self.lookahead;
        self.state['allowIn'] = true;

        if (self.matchKeyword('super') and self.state['inFunctionBody']):
            expr = Node();
            self.lex();
            expr = expr.finishSuper()
            if (not self.match('(') and not self.match('.') and not self.match('[')):
                self.throwUnexpectedToken(self.lookahead);
        else:
            expr = self.inheritCoverGrammar(self.parseNewExpression if self.matchKeyword('new') else self.parsePrimaryExpression)
        while True:
            if (self.match('.')):
                self.isBindingElement = false;
                self.isAssignmentTarget = true;
                property = self.parseNonComputedMember();
                expr = WrappingNode(startToken).finishMemberExpression('.', expr, property)
            elif (self.match('(')):
                self.isBindingElement = false;
                self.isAssignmentTarget = false;
                args = self.parseArguments();
                expr = WrappingNode(startToken).finishCallExpression(expr, args)
            elif (self.match('[')):
                self.isBindingElement = false;
                self.isAssignmentTarget = true;
                property = self.parseComputedMember();
                expr = WrappingNode(startToken).finishMemberExpression('[', expr, property)
            elif (self.lookahead.type == Token.Template and self.lookahead['head']):
                quasi = self.parseTemplateLiteral()
                expr = WrappingNode(startToken).finishTaggedTemplateExpression(expr, quasi)
            else:
                break
        self.state['allowIn'] = previousAllowIn

        return expr

    def parseLeftHandSideExpression(self):
        assert self.state['allowIn'], 'callee of new expression always allow in keyword.'

        startToken = self.lookahead

        if (self.matchKeyword('super') and self.state['inFunctionBody']):
            expr = Node();
            self.lex();
            expr = expr.finishSuper();
            if (not self.match('[') and not self.match('.')):
                self.throwUnexpectedToken(self.lookahead)
        else:
            expr = self.inheritCoverGrammar(self.parseNewExpression if self.matchKeyword('new') else self.parsePrimaryExpression);

        while True:
            if (self.match('[')):
                self.isBindingElement = false;
                self.isAssignmentTarget = true;
                property = self.parseComputedMember();
                expr = WrappingNode(startToken).finishMemberExpression('[', expr, property)
            elif (self.match('.')):
                self.isBindingElement = false;
                self.isAssignmentTarget = true;
                property = self.parseNonComputedMember();
                expr = WrappingNode(startToken).finishMemberExpression('.', expr, property);
            elif (self.lookahead['type'] == Token.Template and self.lookahead['head']):
                quasi = self.parseTemplateLiteral();
                expr = WrappingNode(startToken).finishTaggedTemplateExpression(expr, quasi)
            else:
                break
        return expr

    # 11.3 Postfix Expressions

    def parsePostfixExpression(self):
        startToken = self.lookahead

        expr = self.inheritCoverGrammar(self.parseLeftHandSideExpressionAllowCall)

        if (not self.hasLineTerminator and self.lookahead.type == Token.Punctuator):
            if (self.match('++') or self.match('--')):
                # 11.3.1, 11.3.2
                if (self.strict and expr.type == Syntax.Identifier and isRestrictedWord(expr.name)):
                    self.tolerateError(Messages.StrictLHSPostfix)
                if (not self.isAssignmentTarget):
                    self.tolerateError(Messages.InvalidLHSInAssignment);
                self.isAssignmentTarget = self.isBindingElement = false;

                token = self.lex();
                expr = WrappingNode(startToken).finishPostfixExpression(token['value'], expr);
        return expr;

    # 11.4 Unary Operators

    def parseUnaryExpression(self):

        if (self.lookahead.type != Token.Punctuator and self.lookahead.type != Token.Keyword):
            expr = self.parsePostfixExpression();
        elif (self.match('++') or self.match('--')):
            startToken = self.lookahead;
            token = self.lex();
            expr = self.inheritCoverGrammar(self.parseUnaryExpression);
            # 11.4.4, 11.4.5
            if (self.strict and expr.type == Syntax.Identifier and isRestrictedWord(expr.name)):
                self.tolerateError(Messages.StrictLHSPrefix)
            if (not self.isAssignmentTarget):
                self.tolerateError(Messages.InvalidLHSInAssignment)
            expr = WrappingNode(startToken).finishUnaryExpression(token['value'], expr)
            self.isAssignmentTarget = self.isBindingElement = false
        elif (self.match('+') or self.match('-') or  self.match('~') or self.match('!')):
            startToken = self.lookahead;
            token = self.lex();
            expr = self.inheritCoverGrammar(self.parseUnaryExpression);
            expr =  WrappingNode(startToken).finishUnaryExpression(token['value'], expr)
            self.isAssignmentTarget = self.isBindingElement = false;
        elif (self.matchKeyword('delete') or self.matchKeyword('void') or self.matchKeyword('typeof')):
            startToken = self.lookahead;
            token = self.lex();
            expr = self.inheritCoverGrammar(self.parseUnaryExpression);
            expr = WrappingNode(startToken).finishUnaryExpression(token['value'], expr);
            if (self.strict and expr.operator == 'delete' and expr.argument.type == Syntax.Identifier):
                self.tolerateError(Messages.StrictDelete)
            self.isAssignmentTarget = self.isBindingElement = false;
        else:
            expr = self.parsePostfixExpression()
        return expr

    def binaryPrecedence(self, token, allowIn):
        prec = 0;
        typ = token['type']
        if (typ != Token.Punctuator and typ != Token.Keyword):
            return 0;
        val = token['value']
        if val == 'in' and not allowIn:
            return 0
        return PRECEDENCE.get(val, 0)

    # 11.5 Multiplicative Operators
    # 11.6 Additive Operators
    # 11.7 Bitwise Shift Operators
    # 11.8 Relational Operators
    # 11.9 Equality Operators
    # 11.10 Binary Bitwise Operators
    # 11.11 Binary Logical Operators

    def parseBinaryExpression(self):

        marker = self.lookahead;
        left = self.inheritCoverGrammar(self.parseUnaryExpression);

        token = self.lookahead;
        prec = self.binaryPrecedence(token, self.state['allowIn']);
        if (prec == 0):
            return left
        self.isAssignmentTarget = self.isBindingElement = false;
        token['prec'] = prec
        self.lex()

        markers = [marker, self.lookahead];
        right = self.isolateCoverGrammar(self.parseUnaryExpression);

        stack = [left, token, right];

        while True:
            prec = self.binaryPrecedence(self.lookahead, self.state['allowIn'])
            if not prec > 0:
                break
            # Reduce: make a binary expression from the three topmost entries.
            while ((len(stack) > 2) and (prec <= stack[len(stack) - 2]['prec'])):
                right = stack.pop();
                operator = stack.pop()['value']
                left = stack.pop()
                markers.pop()
                expr = WrappingNode(markers[len(markers) - 1]).finishBinaryExpression(operator, left, right)
                stack.append(expr)

            # Shift
            token = self.lex();
            token['prec'] = prec;
            stack.append(token);
            markers.append(self.lookahead);
            expr = self.isolateCoverGrammar(self.parseUnaryExpression);
            stack.append(expr);

        # Final reduce to clean-up the stack.
        i = len(stack) - 1;
        expr = stack[i]
        markers.pop()
        while (i > 1):
            expr =  WrappingNode(markers.pop()).finishBinaryExpression(stack[i - 1]['value'], stack[i - 2], expr);
            i -= 2
        return expr


    # 11.12 Conditional Operator

    def parseConditionalExpression(self):

        startToken = self.lookahead

        expr = self.inheritCoverGrammar(self.parseBinaryExpression);
        if (self.match('?')):
            self.lex()
            previousAllowIn = self.state['allowIn']
            self.state['allowIn'] = true;
            consequent = self.isolateCoverGrammar(self.parseAssignmentExpression);
            self.state['allowIn'] = previousAllowIn;
            self.expect(':');
            alternate = self.isolateCoverGrammar(self.parseAssignmentExpression)

            expr = WrappingNode(startToken).finishConditionalExpression(expr, consequent, alternate);
            self.isAssignmentTarget = self.isBindingElement = false;
        return expr

    # [ES6] 14.2 Arrow Function

    def parseConciseBody(self):
        if (self.match('{')):
            return self.parseFunctionSourceElements()
        return self.isolateCoverGrammar(self.parseAssignmentExpression)

    def checkPatternParam(self, options, param):
        typ = param.type
        if typ == Syntax.Identifier:
            self.validateParam(options, param, param.name);
        elif typ == Syntax.RestElement:
            self.checkPatternParam(options, param.argument)
        elif typ == Syntax.AssignmentPattern:
            self.checkPatternParam(options, param.left)
        elif typ == Syntax.ArrayPattern:
            for i in xrange(len(param.elements)):
                if (param.elements[i] != null):
                    self.checkPatternParam(options, param.elements[i]);
        else:
            assert typ == Syntax.ObjectPattern, 'Invalid type'
            for i in xrange(len(param.properties)):
                self.checkPatternParam(options, param.properties[i].value);

    def reinterpretAsCoverFormalsList(self, expr):
        defaults = [];
        defaultCount = 0;
        params = [expr];

        typ = expr.type
        if typ == Syntax.Identifier:
            pass
        elif typ == PlaceHolders.ArrowParameterPlaceHolder:
            params = expr.params
        else:
            return null
        options = {
            'paramSet': {}}
        le = len(params)
        for i in xrange(le):
            param = params[i]
            if param.type == Syntax.AssignmentPattern:
                params[i] = param.left;
                defaults.append(param.right);
                defaultCount += 1
                self.checkPatternParam(options, param.left);
            else:
                self.checkPatternParam(options, param);
                params[i] = param;
                defaults.append(null);
        if (options['message'] == Messages.StrictParamDupe):
            token = options['stricted'] if self.strict else options['firstRestricted']
            self.throwUnexpectedToken(token, options['message']);
        if (defaultCount == 0):
            defaults = []
        return {
            'params': params,
            'defaults': defaults,
            'stricted': options['stricted'],
            'firstRestricted': options['firstRestricted'],
            'message': options['message']}

    def parseArrowFunctionExpression(self, options, node):
        if (self.hasLineTerminator):
            self.tolerateUnexpectedToken(self.lookahead)
        self.expect('=>')
        previousStrict = self.strict;

        body = self.parseConciseBody();

        if (self.strict and options.firstRestricted):
            self.throwUnexpectedToken(options.firstRestricted, options.message);
        if (self.strict and options.stricted):
            self.tolerateUnexpectedToken(options.stricted, options.message);

        self.strict = previousStrict

        return node.finishArrowFunctionExpression(options.params, options.defaults, body, body.type != Syntax.BlockStatement)

    # 11.13 Assignment Operators

    def parseAssignmentExpression(self):
        startToken = self.lookahead;
        token = self.lookahead;

        expr = self.parseConditionalExpression();

        if (expr.type == PlaceHolders.ArrowParameterPlaceHolder or self.match('=>')):
            self.isAssignmentTarget = self.isBindingElement = false;
            lis = self.reinterpretAsCoverFormalsList(expr)

            if (lis):
                self.firstCoverInitializedNameError = null;
                return self.parseArrowFunctionExpression(lis, WrappingNode(startToken))
            return expr

        if (self.matchAssign()):
            if (not self.isAssignmentTarget):
                self.tolerateError(Messages.InvalidLHSInAssignment)
            # 11.13.1

            if (self.strict and expr.type == Syntax.Identifier and self.isRestrictedWord(expr.name)):
                self.tolerateUnexpectedToken(token, Messages.StrictLHSAssignment);
            if (not self.match('=')):
                self.isAssignmentTarget = self.isBindingElement = false;
            else:
                self.reinterpretExpressionAsPattern(expr)
            token = self.lex();
            right = self.isolateCoverGrammar(self.parseAssignmentExpression)
            expr =  WrappingNode(startToken).finishAssignmentExpression(token['value'], expr, right);
            self.firstCoverInitializedNameError = null
        return expr


    # 11.14 Comma Operator

    def parseExpression(self):
        startToken = self.lookahead
        expr = self.isolateCoverGrammar(self.parseAssignmentExpression)

        if (self.match(',')):
            expressions = [expr];

            while (self.startIndex < self.length):
                if (not self.match(',')):
                    break
                self.lex();
                expressions.append(self.isolateCoverGrammar(self.parseAssignmentExpression))
            expr = WrappingNode(startToken).finishSequenceExpression(expressions);
        return expr
    // 12.1 Block

    function parseStatementListItem() {
        if (lookahead.type === Token.Keyword) {
            switch (lookahead.value) {
            case 'export':
                if (sourceType !== 'module') {
                    tolerateUnexpectedToken(lookahead, Messages.IllegalExportDeclaration);
                }
                return parseExportDeclaration();
            case 'import':
                if (sourceType !== 'module') {
                    tolerateUnexpectedToken(lookahead, Messages.IllegalImportDeclaration);
                }
                return parseImportDeclaration();
            case 'const':
            case 'let':
                return parseLexicalDeclaration({inFor: false});
            case 'function':
                return parseFunctionDeclaration(new Node());
            case 'class':
                return parseClassDeclaration();
            }
        }

        return parseStatement();
    }

    function parseStatementList() {
        var list = [];
        while (startIndex < length) {
            if (match('}')) {
                break;
            }
            list.push(parseStatementListItem());
        }

        return list;
    }

    function parseBlock() {
        var block, node = new Node();

        expect('{');

        block = parseStatementList();

        expect('}');

        return node.finishBlockStatement(block);
    }

    // 12.2 Variable Statement

    function parseVariableIdentifier() {
        var token, node = new Node();

        token = lex();

        if (token.type !== Token.Identifier) {
            if (strict && token.type === Token.Keyword && isStrictModeReservedWord(token.value)) {
                tolerateUnexpectedToken(token, Messages.StrictReservedWord);
            } else {
                throwUnexpectedToken(token);
            }
        }

        return node.finishIdentifier(token.value);
    }

    function parseVariableDeclaration() {
        var init = null, id, node = new Node();

        id = parsePattern();

        // 12.2.1
        if (strict && isRestrictedWord(id.name)) {
            tolerateError(Messages.StrictVarName);
        }

        if (match('=')) {
            lex();
            init = isolateCoverGrammar(parseAssignmentExpression);
        } else if (id.type !== Syntax.Identifier) {
            expect('=');
        }

        return node.finishVariableDeclarator(id, init);
    }

    function parseVariableDeclarationList() {
        var list = [];

        do {
            list.push(parseVariableDeclaration());
            if (!match(',')) {
                break;
            }
            lex();
        } while (startIndex < length);

        return list;
    }

    function parseVariableStatement(node) {
        var declarations;

        expectKeyword('var');

        declarations = parseVariableDeclarationList();

        consumeSemicolon();

        return node.finishVariableDeclaration(declarations);
    }

    function parseLexicalBinding(kind, options) {
        var init = null, id, node = new Node();

        id = parsePattern();

        // 12.2.1
        if (strict && id.type === Syntax.Identifier && isRestrictedWord(id.name)) {
            tolerateError(Messages.StrictVarName);
        }

        if (kind === 'const') {
            if (!matchKeyword('in')) {
                expect('=');
                init = isolateCoverGrammar(parseAssignmentExpression);
            }
        } else if ((!options.inFor && id.type !== Syntax.Identifier) || match('=')) {
            expect('=');
            init = isolateCoverGrammar(parseAssignmentExpression);
        }

        return node.finishVariableDeclarator(id, init);
    }

    function parseBindingList(kind, options) {
        var list = [];

        do {
            list.push(parseLexicalBinding(kind, options));
            if (!match(',')) {
                break;
            }
            lex();
        } while (startIndex < length);

        return list;
    }

    function parseLexicalDeclaration(options) {
        var kind, declarations, node = new Node();

        kind = lex().value;
        assert(kind === 'let' || kind === 'const', 'Lexical declaration must be either let or const');

        declarations = parseBindingList(kind, options);

        consumeSemicolon();

        return node.finishLexicalDeclaration(declarations, kind);
    }

    function parseRestElement() {
        var param, node = new Node();

        lex();

        if (match('{')) {
            throwError(Messages.ObjectPatternAsRestParameter);
        }

        param = parseVariableIdentifier();

        if (match('=')) {
            throwError(Messages.DefaultRestParameter);
        }

        if (!match(')')) {
            throwError(Messages.ParameterAfterRestParameter);
        }

        return node.finishRestElement(param);
    }

    // 12.3 Empty Statement

    function parseEmptyStatement(node) {
        expect(';');
        return node.finishEmptyStatement();
    }

    // 12.4 Expression Statement

    function parseExpressionStatement(node) {
        var expr = parseExpression();
        consumeSemicolon();
        return node.finishExpressionStatement(expr);
    }

    // 12.5 If statement

    function parseIfStatement(node) {
        var test, consequent, alternate;

        expectKeyword('if');

        expect('(');

        test = parseExpression();

        expect(')');

        consequent = parseStatement();

        if (matchKeyword('else')) {
            lex();
            alternate = parseStatement();
        } else {
            alternate = null;
        }

        return node.finishIfStatement(test, consequent, alternate);
    }

    // 12.6 Iteration Statements

    function parseDoWhileStatement(node) {
        var body, test, oldInIteration;

        expectKeyword('do');

        oldInIteration = state.inIteration;
        state.inIteration = true;

        body = parseStatement();

        state.inIteration = oldInIteration;

        expectKeyword('while');

        expect('(');

        test = parseExpression();

        expect(')');

        if (match(';')) {
            lex();
        }

        return node.finishDoWhileStatement(body, test);
    }

    function parseWhileStatement(node) {
        var test, body, oldInIteration;

        expectKeyword('while');

        expect('(');

        test = parseExpression();

        expect(')');

        oldInIteration = state.inIteration;
        state.inIteration = true;

        body = parseStatement();

        state.inIteration = oldInIteration;

        return node.finishWhileStatement(test, body);
    }

    function parseForStatement(node) {
        var init, initSeq, initStartToken, test, update, left, right, kind, declarations,
            body, oldInIteration, previousAllowIn = state.allowIn;

        init = test = update = null;

        expectKeyword('for');

        expect('(');

        if (match(';')) {
            lex();
        } else {
            if (matchKeyword('var')) {
                init = new Node();
                lex();

                state.allowIn = false;
                init = init.finishVariableDeclaration(parseVariableDeclarationList());
                state.allowIn = previousAllowIn;

                if (init.declarations.length === 1 && matchKeyword('in')) {
                    lex();
                    left = init;
                    right = parseExpression();
                    init = null;
                } else {
                    expect(';');
                }
            } else if (matchKeyword('const') || matchKeyword('let')) {
                init = new Node();
                kind = lex().value;

                state.allowIn = false;
                declarations = parseBindingList(kind, {inFor: true});
                state.allowIn = previousAllowIn;

                if (declarations.length === 1 && declarations[0].init === null && matchKeyword('in')) {
                    init = init.finishLexicalDeclaration(declarations, kind);
                    lex();
                    left = init;
                    right = parseExpression();
                    init = null;
                } else {
                    consumeSemicolon();
                    init = init.finishLexicalDeclaration(declarations, kind);
                }
            } else {
                initStartToken = lookahead;
                state.allowIn = false;
                init = inheritCoverGrammar(parseAssignmentExpression);
                state.allowIn = previousAllowIn;

                if (matchKeyword('in')) {
                    if (!isAssignmentTarget) {
                        tolerateError(Messages.InvalidLHSInForIn);
                    }

                    lex();
                    reinterpretExpressionAsPattern(init);
                    left = init;
                    right = parseExpression();
                    init = null;
                } else {
                    if (match(',')) {
                        initSeq = [init];
                        while (match(',')) {
                            lex();
                            initSeq.push(isolateCoverGrammar(parseAssignmentExpression));
                        }
                        init = new WrappingNode(initStartToken).finishSequenceExpression(initSeq);
                    }
                    expect(';');
                }
            }
        }

        if (typeof left === 'undefined') {

            if (!match(';')) {
                test = parseExpression();
            }
            expect(';');

            if (!match(')')) {
                update = parseExpression();
            }
        }

        expect(')');

        oldInIteration = state.inIteration;
        state.inIteration = true;

        body = isolateCoverGrammar(parseStatement);

        state.inIteration = oldInIteration;

        return (typeof left === 'undefined') ?
                node.finishForStatement(init, test, update, body) :
                node.finishForInStatement(left, right, body);
    }

    // 12.7 The continue statement

    function parseContinueStatement(node) {
        var label = null, key;

        expectKeyword('continue');

        // Optimize the most common form: 'continue;'.
        if (source.charCodeAt(startIndex) === 0x3B) {
            lex();

            if (!state.inIteration) {
                throwError(Messages.IllegalContinue);
            }

            return node.finishContinueStatement(null);
        }

        if (hasLineTerminator) {
            if (!state.inIteration) {
                throwError(Messages.IllegalContinue);
            }

            return node.finishContinueStatement(null);
        }

        if (lookahead.type === Token.Identifier) {
            label = parseVariableIdentifier();

            key = '$' + label.name;
            if (!Object.prototype.hasOwnProperty.call(state.labelSet, key)) {
                throwError(Messages.UnknownLabel, label.name);
            }
        }

        consumeSemicolon();

        if (label === null && !state.inIteration) {
            throwError(Messages.IllegalContinue);
        }

        return node.finishContinueStatement(label);
    }

    // 12.8 The break statement

    function parseBreakStatement(node) {
        var label = null, key;

        expectKeyword('break');

        // Catch the very common case first: immediately a semicolon (U+003B).
        if (source.charCodeAt(lastIndex) === 0x3B) {
            lex();

            if (!(state.inIteration || state.inSwitch)) {
                throwError(Messages.IllegalBreak);
            }

            return node.finishBreakStatement(null);
        }

        if (hasLineTerminator) {
            if (!(state.inIteration || state.inSwitch)) {
                throwError(Messages.IllegalBreak);
            }

            return node.finishBreakStatement(null);
        }

        if (lookahead.type === Token.Identifier) {
            label = parseVariableIdentifier();

            key = '$' + label.name;
            if (!Object.prototype.hasOwnProperty.call(state.labelSet, key)) {
                throwError(Messages.UnknownLabel, label.name);
            }
        }

        consumeSemicolon();

        if (label === null && !(state.inIteration || state.inSwitch)) {
            throwError(Messages.IllegalBreak);
        }

        return node.finishBreakStatement(label);
    }

    // 12.9 The return statement

    function parseReturnStatement(node) {
        var argument = null;

        expectKeyword('return');

        if (!state.inFunctionBody) {
            tolerateError(Messages.IllegalReturn);
        }

        // 'return' followed by a space and an identifier is very common.
        if (source.charCodeAt(lastIndex) === 0x20) {
            if (isIdentifierStart(source.charCodeAt(lastIndex + 1))) {
                argument = parseExpression();
                consumeSemicolon();
                return node.finishReturnStatement(argument);
            }
        }

        if (hasLineTerminator) {
            // HACK
            return node.finishReturnStatement(null);
        }

        if (!match(';')) {
            if (!match('}') && lookahead.type !== Token.EOF) {
                argument = parseExpression();
            }
        }

        consumeSemicolon();

        return node.finishReturnStatement(argument);
    }

    // 12.10 The with statement

    function parseWithStatement(node) {
        var object, body;

        if (strict) {
            tolerateError(Messages.StrictModeWith);
        }

        expectKeyword('with');

        expect('(');

        object = parseExpression();

        expect(')');

        body = parseStatement();

        return node.finishWithStatement(object, body);
    }

    // 12.10 The swith statement

    function parseSwitchCase() {
        var test, consequent = [], statement, node = new Node();

        if (matchKeyword('default')) {
            lex();
            test = null;
        } else {
            expectKeyword('case');
            test = parseExpression();
        }
        expect(':');

        while (startIndex < length) {
            if (match('}') || matchKeyword('default') || matchKeyword('case')) {
                break;
            }
            statement = parseStatementListItem();
            consequent.push(statement);
        }

        return node.finishSwitchCase(test, consequent);
    }

    function parseSwitchStatement(node) {
        var discriminant, cases, clause, oldInSwitch, defaultFound;

        expectKeyword('switch');

        expect('(');

        discriminant = parseExpression();

        expect(')');

        expect('{');

        cases = [];

        if (match('}')) {
            lex();
            return node.finishSwitchStatement(discriminant, cases);
        }

        oldInSwitch = state.inSwitch;
        state.inSwitch = true;
        defaultFound = false;

        while (startIndex < length) {
            if (match('}')) {
                break;
            }
            clause = parseSwitchCase();
            if (clause.test === null) {
                if (defaultFound) {
                    throwError(Messages.MultipleDefaultsInSwitch);
                }
                defaultFound = true;
            }
            cases.push(clause);
        }

        state.inSwitch = oldInSwitch;

        expect('}');

        return node.finishSwitchStatement(discriminant, cases);
    }

    // 12.13 The throw statement

    function parseThrowStatement(node) {
        var argument;

        expectKeyword('throw');

        if (hasLineTerminator) {
            throwError(Messages.NewlineAfterThrow);
        }

        argument = parseExpression();

        consumeSemicolon();

        return node.finishThrowStatement(argument);
    }

    // 12.14 The try statement

    function parseCatchClause() {
        var param, body, node = new Node();

        expectKeyword('catch');

        expect('(');
        if (match(')')) {
            throwUnexpectedToken(lookahead);
        }

        param = parsePattern();

        // 12.14.1
        if (strict && isRestrictedWord(param.name)) {
            tolerateError(Messages.StrictCatchVariable);
        }

        expect(')');
        body = parseBlock();
        return node.finishCatchClause(param, body);
    }

    function parseTryStatement(node) {
        var block, handler = null, finalizer = null;

        expectKeyword('try');

        block = parseBlock();

        if (matchKeyword('catch')) {
            handler = parseCatchClause();
        }

        if (matchKeyword('finally')) {
            lex();
            finalizer = parseBlock();
        }

        if (!handler && !finalizer) {
            throwError(Messages.NoCatchOrFinally);
        }

        return node.finishTryStatement(block, handler, finalizer);
    }

    // 12.15 The debugger statement

    function parseDebuggerStatement(node) {
        expectKeyword('debugger');

        consumeSemicolon();

        return node.finishDebuggerStatement();
    }

    // 12 Statements

    function parseStatement() {
        var type = lookahead.type,
            expr,
            labeledBody,
            key,
            node;

        if (type === Token.EOF) {
            throwUnexpectedToken(lookahead);
        }

        if (type === Token.Punctuator && lookahead.value === '{') {
            return parseBlock();
        }
        isAssignmentTarget = isBindingElement = true;
        node = new Node();

        if (type === Token.Punctuator) {
            switch (lookahead.value) {
            case ';':
                return parseEmptyStatement(node);
            case '(':
                return parseExpressionStatement(node);
            default:
                break;
            }
        } else if (type === Token.Keyword) {
            switch (lookahead.value) {
            case 'break':
                return parseBreakStatement(node);
            case 'continue':
                return parseContinueStatement(node);
            case 'debugger':
                return parseDebuggerStatement(node);
            case 'do':
                return parseDoWhileStatement(node);
            case 'for':
                return parseForStatement(node);
            case 'function':
                return parseFunctionDeclaration(node);
            case 'if':
                return parseIfStatement(node);
            case 'return':
                return parseReturnStatement(node);
            case 'switch':
                return parseSwitchStatement(node);
            case 'throw':
                return parseThrowStatement(node);
            case 'try':
                return parseTryStatement(node);
            case 'var':
                return parseVariableStatement(node);
            case 'while':
                return parseWhileStatement(node);
            case 'with':
                return parseWithStatement(node);
            default:
                break;
            }
        }

        expr = parseExpression();

        // 12.12 Labelled Statements
        if ((expr.type === Syntax.Identifier) && match(':')) {
            lex();

            key = '$' + expr.name;
            if (Object.prototype.hasOwnProperty.call(state.labelSet, key)) {
                throwError(Messages.Redeclaration, 'Label', expr.name);
            }

            state.labelSet[key] = true;
            labeledBody = parseStatement();
            delete state.labelSet[key];
            return node.finishLabeledStatement(expr, labeledBody);
        }

        consumeSemicolon();

        return node.finishExpressionStatement(expr);
    }

    // 13 Function Definition

    function parseFunctionSourceElements() {
        var statement, body = [], token, directive, firstRestricted,
            oldLabelSet, oldInIteration, oldInSwitch, oldInFunctionBody, oldParenthesisCount,
            node = new Node();

        expect('{');

        while (startIndex < length) {
            if (lookahead.type !== Token.StringLiteral) {
                break;
            }
            token = lookahead;

            statement = parseStatementListItem();
            body.push(statement);
            if (statement.expression.type !== Syntax.Literal) {
                // this is not directive
                break;
            }
            directive = source.slice(token.start + 1, token.end - 1);
            if (directive === 'use strict') {
                strict = true;
                if (firstRestricted) {
                    tolerateUnexpectedToken(firstRestricted, Messages.StrictOctalLiteral);
                }
            } else {
                if (!firstRestricted && token.octal) {
                    firstRestricted = token;
                }
            }
        }

        oldLabelSet = state.labelSet;
        oldInIteration = state.inIteration;
        oldInSwitch = state.inSwitch;
        oldInFunctionBody = state.inFunctionBody;
        oldParenthesisCount = state.parenthesizedCount;

        state.labelSet = {};
        state.inIteration = false;
        state.inSwitch = false;
        state.inFunctionBody = true;
        state.parenthesizedCount = 0;

        while (startIndex < length) {
            if (match('}')) {
                break;
            }
            body.push(parseStatementListItem());
        }

        expect('}');

        state.labelSet = oldLabelSet;
        state.inIteration = oldInIteration;
        state.inSwitch = oldInSwitch;
        state.inFunctionBody = oldInFunctionBody;
        state.parenthesizedCount = oldParenthesisCount;

        return node.finishBlockStatement(body);
    }

    function validateParam(options, param, name) {
        var key = '$' + name;
        if (strict) {
            if (isRestrictedWord(name)) {
                options.stricted = param;
                options.message = Messages.StrictParamName;
            }
            if (Object.prototype.hasOwnProperty.call(options.paramSet, key)) {
                options.stricted = param;
                options.message = Messages.StrictParamDupe;
            }
        } else if (!options.firstRestricted) {
            if (isRestrictedWord(name)) {
                options.firstRestricted = param;
                options.message = Messages.StrictParamName;
            } else if (isStrictModeReservedWord(name)) {
                options.firstRestricted = param;
                options.message = Messages.StrictReservedWord;
            } else if (Object.prototype.hasOwnProperty.call(options.paramSet, key)) {
                options.firstRestricted = param;
                options.message = Messages.StrictParamDupe;
            }
        }
        options.paramSet[key] = true;
    }

    function parseParam(options) {
        var token, param, def;

        token = lookahead;
        if (token.value === '...') {
            param = parseRestElement();
            validateParam(options, param.argument, param.argument.name);
            options.params.push(param);
            options.defaults.push(null);
            return false;
        }

        param = parsePatternWithDefault();
        validateParam(options, token, token.value);

        if (param.type === Syntax.AssignmentPattern) {
            def = param.right;
            param = param.left;
            ++options.defaultCount;
        }

        options.params.push(param);
        options.defaults.push(def);

        return !match(')');
    }

    function parseParams(firstRestricted) {
        var options;

        options = {
            params: [],
            defaultCount: 0,
            defaults: [],
            firstRestricted: firstRestricted
        };

        expect('(');

        if (!match(')')) {
            options.paramSet = {};
            while (startIndex < length) {
                if (!parseParam(options)) {
                    break;
                }
                expect(',');
            }
        }

        expect(')');

        if (options.defaultCount === 0) {
            options.defaults = [];
        }

        return {
            params: options.params,
            defaults: options.defaults,
            stricted: options.stricted,
            firstRestricted: options.firstRestricted,
            message: options.message
        };
    }

    function parseFunctionDeclaration(node, identifierIsOptional) {
        var id = null, params = [], defaults = [], body, token, stricted, tmp, firstRestricted, message, previousStrict;

        expectKeyword('function');
        if (!identifierIsOptional || !match('(')) {
            token = lookahead;
            id = parseVariableIdentifier();
            if (strict) {
                if (isRestrictedWord(token.value)) {
                    tolerateUnexpectedToken(token, Messages.StrictFunctionName);
                }
            } else {
                if (isRestrictedWord(token.value)) {
                    firstRestricted = token;
                    message = Messages.StrictFunctionName;
                } else if (isStrictModeReservedWord(token.value)) {
                    firstRestricted = token;
                    message = Messages.StrictReservedWord;
                }
            }
        }

        tmp = parseParams(firstRestricted);
        params = tmp.params;
        defaults = tmp.defaults;
        stricted = tmp.stricted;
        firstRestricted = tmp.firstRestricted;
        if (tmp.message) {
            message = tmp.message;
        }

        previousStrict = strict;
        body = parseFunctionSourceElements();
        if (strict && firstRestricted) {
            throwUnexpectedToken(firstRestricted, message);
        }
        if (strict && stricted) {
            tolerateUnexpectedToken(stricted, message);
        }
        strict = previousStrict;

        return node.finishFunctionDeclaration(id, params, defaults, body);
    }

    function parseFunctionExpression() {
        var token, id = null, stricted, firstRestricted, message, tmp,
            params = [], defaults = [], body, previousStrict, node = new Node();

        expectKeyword('function');

        if (!match('(')) {
            token = lookahead;
            id = parseVariableIdentifier();
            if (strict) {
                if (isRestrictedWord(token.value)) {
                    tolerateUnexpectedToken(token, Messages.StrictFunctionName);
                }
            } else {
                if (isRestrictedWord(token.value)) {
                    firstRestricted = token;
                    message = Messages.StrictFunctionName;
                } else if (isStrictModeReservedWord(token.value)) {
                    firstRestricted = token;
                    message = Messages.StrictReservedWord;
                }
            }
        }

        tmp = parseParams(firstRestricted);
        params = tmp.params;
        defaults = tmp.defaults;
        stricted = tmp.stricted;
        firstRestricted = tmp.firstRestricted;
        if (tmp.message) {
            message = tmp.message;
        }

        previousStrict = strict;
        body = parseFunctionSourceElements();
        if (strict && firstRestricted) {
            throwUnexpectedToken(firstRestricted, message);
        }
        if (strict && stricted) {
            tolerateUnexpectedToken(stricted, message);
        }
        strict = previousStrict;

        return node.finishFunctionExpression(id, params, defaults, body);
    }


    function parseClassBody() {
        var classBody, token, isStatic, hasConstructor = false, body, method, computed, key;

        classBody = new Node();

        expect('{');
        body = [];
        while (!match('}')) {
            if (match(';')) {
                lex();
            } else {
                method = new Node();
                token = lookahead;
                isStatic = false;
                computed = match('[');
                key = parseObjectPropertyKey();
                if (key.name === 'static' && lookaheadPropertyName()) {
                    token = lookahead;
                    isStatic = true;
                    computed = match('[');
                    key = parseObjectPropertyKey();
                }
                method = tryParseMethodDefinition(token, key, computed, method);
                if (method) {
                    method['static'] = isStatic;
                    if (method.kind === 'init') {
                        method.kind = 'method';
                    }
                    if (!isStatic) {
                        if (!method.computed && (method.key.name || method.key.value.toString()) === 'constructor') {
                            if (method.kind !== 'method' || !method.method || method.value.generator) {
                                throwUnexpectedToken(token, Messages.ConstructorSpecialMethod);
                            }
                            if (hasConstructor) {
                                throwUnexpectedToken(token, Messages.DuplicateConstructor);
                            } else {
                                hasConstructor = true;
                            }
                            method.kind = 'constructor';
                        }
                    } else {
                        if (!method.computed && (method.key.name || method.key.value.toString()) === 'prototype') {
                            throwUnexpectedToken(token, Messages.StaticPrototype);
                        }
                    }
                    method.type = Syntax.MethodDefinition;
                    delete method.method;
                    delete method.shorthand;
                    body.push(method);
                } else {
                    throwUnexpectedToken(lookahead);
                }
            }
        }
        lex();
        return classBody.finishClassBody(body);
    }

    function parseClassDeclaration(identifierIsOptional) {
        var id = null, superClass = null, classNode = new Node(), classBody, previousStrict = strict;
        strict = true;

        expectKeyword('class');

        if (!identifierIsOptional || lookahead.type === Token.Identifier) {
            id = parseVariableIdentifier();
        }

        if (matchKeyword('extends')) {
            lex();
            superClass = isolateCoverGrammar(parseLeftHandSideExpressionAllowCall);
        }
        classBody = parseClassBody();
        strict = previousStrict;

        return classNode.finishClassDeclaration(id, superClass, classBody);
    }

    function parseClassExpression() {
        var id = null, superClass = null, classNode = new Node(), classBody, previousStrict = strict;
        strict = true;

        expectKeyword('class');

        if (lookahead.type === Token.Identifier) {
            id = parseVariableIdentifier();
        }

        if (matchKeyword('extends')) {
            lex();
            superClass = isolateCoverGrammar(parseLeftHandSideExpressionAllowCall);
        }
        classBody = parseClassBody();
        strict = previousStrict;

        return classNode.finishClassExpression(id, superClass, classBody);


a = EspParser('"kk\\nnkkkm"')
a.parseExpression()
