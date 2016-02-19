# The MIT License
#
# Copyright 2014, 2015 Piotr Dabkowski
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the 'Software'),
# to deal in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so, subject
# to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
#  OR THE USE OR OTHER DEALINGS IN THE SOFTWARE

"""
SUPPORTS WHOLE ECMA SCRIPT 6 !!!
Usage:

tree = esprima.parse('var a = 10')   # Of course supports also options just like normal esprima!

You can convert tree to python dict if you want:

tree.to_dict()
"""
from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([])
@Js
def PyJs_anonymous_0_(exports, this, arguments, var=var):
    var = Scope({u'this':this, u'exports':exports, u'arguments':arguments}, var)
    var.registers([u'isKeyword', u'isolateCoverGrammar', u'consumeSemicolon', u'parseLeftHandSideExpression', u'throwUnexpectedToken', u'parsePatternWithDefault', u'parseExpressionStatement', u'advanceSlash', u'lastLineStart', u'tolerateUnexpectedToken', u'WrappingSourceLocation', u'source', u'parseThrowStatement', u'addComment', u'parseSwitchStatement', u'match', u'parseEmptyStatement', u'validateParam', u'exports', u'parseConditionalExpression', u'parseStatementListItem', u'parseClassDeclaration', u'Messages', u'isAssignmentTarget', u'parseVariableDeclaration', u'Token', u'reinterpretExpressionAsPattern', u'getComplexIdentifier', u'Position', u'isWhiteSpace', u'parseWhileStatement', u'parseTemplateLiteral', u'parseTemplateElement', u'parseGroupExpression', u'scanHexLiteral', u'parseBreakStatement', u'scanBinaryLiteral', u'firstCoverInitializedNameError', u'expectCommaSeparator', u'parseParams', u'SourceLocation', u'parsePrimaryExpression', u'FnExprTokens', u'scanning', u'scanRegExpFlags', u'parseImportDeclaration', u'parseVariableDeclarationList', u'parseFunctionExpression', u'parseReturnStatement', u'recordError', u'parseExportAllDeclaration', u'collectRegex', u'expect', u'skipMultiLineComment', u'scanNumericLiteral', u'parseYieldExpression', u'index', u'isIdentifierStart', u'parsePropertyMethodFunction', u'parseProgram', u'isImplicitOctalLiteral', u'state', u'isOctalDigit', u'parseArrayInitializer', u'isDecimalDigit', u'parseClassExpression', u'parseObjectProperty', u'parseCatchClause', u'peek', u'parseArguments', u'testRegExp', u'octalToDecimal', u'parseExportDeclaration', u'parseStatement', u'lastLineNumber', u'isLineTerminator', u'parseStatementList', u'parseModuleSpecifier', u'lex', u'parseFunctionSourceElements', u'isIdentifierName', u'advance', u'inheritCoverGrammar', u'isBindingElement', u'TokenName', u'reinterpretAsCoverFormalsList', u'length', u'isFutureReservedWord', u'parseImportNamespaceSpecifier', u'parseUnaryExpression', u'parseAssignmentExpression', u'Regex', u'parseLexicalBinding', u'tolerateError', u'parseBinaryExpression', u'startLineNumber', u'extra', u'scanIdentifier', u'parseNamedImports', u'unexpectedTokenError', u'parseNonComputedProperty', u'startIndex', u'startLineStart', u'parseParam', u'parseNewExpression', u'scanRegExpBody', u'Node', u'collectToken', u'parseWithStatement', u'parseDebuggerStatement', u'parseObjectPattern', u'parseImportSpecifier', u'skipComment', u'parseVariableStatement', u'strict', u'lookaheadPropertyName', u'tokenize', u'parseVariableIdentifier', u'parseExpression', u'constructError', u'scanStringLiteral', u'parseObjectPropertyKey', u'parseArrayPattern', u'expectKeyword', u'assert', u'lineNumber', u'parseConciseBody', u'createError', u'parseLeftHandSideExpressionAllowCall', u'hasLineTerminator', u'fromCodePoint', u'parseExportNamedDeclaration', u'parseBlock', u'Syntax', u'parseExportSpecifier', u'skipSingleLineComment', u'parseDoWhileStatement', u'codePointAt', u'scanHexEscape', u'isHexDigit', u'matchContextualKeyword', u'isStrictModeReservedWord', u'binaryPrecedence', u'parse', u'matchAssign', u'WrappingNode', u'parseObjectInitializer', u'getIdentifier', u'isRestrictedWord', u'parseSwitchCase', u'parsePropertyPattern', u'parseIfStatement', u'parseFunctionDeclaration', u'parsePostfixExpression', u'parseNonComputedMember', u'parseExportDefaultDeclaration', u'lastIndex', u'parseRestElement', u'parseScriptBody', u'parseBindingList', u'scanTemplate', u'PlaceHolders', u'parseLexicalDeclaration', u'checkPatternParam', u'parsePropertyFunction', u'scanPunctuator', u'parseArrowFunctionExpression', u'throwError', u'scanUnicodeCodePointEscape', u'scanOctalLiteral', u'scanRegExp', u'parseImportDefaultSpecifier', u'parsePattern', u'lineStart', u'parseForStatement', u'isIdentifierPart', u'matchKeyword', u'lookahead', u'parseTryStatement', u'parseComputedMember', u'parseContinueStatement', u'tryParseMethodDefinition', u'parseClassBody', u'filterTokenLocation'])
    @Js
    def PyJsHoisted_consumeSemicolon_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        if (PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt', var.get(u'startIndex')),Js(59)) or var.get(u'match')(Js(u';'))):
            var.get(u'lex')()
            return var.get('undefined')
        if var.get(u'hasLineTerminator'):
            return var.get('undefined')
        var.put(u'lastIndex', var.get(u'startIndex'))
        var.put(u'lastLineNumber', var.get(u'startLineNumber'))
        var.put(u'lastLineStart', var.get(u'startLineStart'))
        if (PyJsStrictNeq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'EOF')) and var.get(u'match')(Js(u'}')).neg()):
            var.get(u'throwUnexpectedToken')(var.get(u'lookahead'))
    PyJsHoisted_consumeSemicolon_.func_name = u'consumeSemicolon'
    var.put(u'consumeSemicolon', PyJsHoisted_consumeSemicolon_)
    @Js
    def PyJsHoisted_isolateCoverGrammar_(parser, this, arguments, var=var):
        var = Scope({u'this':this, u'parser':parser, u'arguments':arguments}, var)
        var.registers([u'oldFirstCoverInitializedNameError', u'parser', u'oldIsBindingElement', u'oldIsAssignmentTarget', u'result'])
        var.put(u'oldIsBindingElement', var.get(u'isBindingElement'))
        var.put(u'oldIsAssignmentTarget', var.get(u'isAssignmentTarget'))
        var.put(u'oldFirstCoverInitializedNameError', var.get(u'firstCoverInitializedNameError'))
        var.put(u'isBindingElement', var.get(u'true'))
        var.put(u'isAssignmentTarget', var.get(u'true'))
        var.put(u'firstCoverInitializedNameError', var.get(u"null"))
        var.put(u'result', var.get(u'parser')())
        if PyJsStrictNeq(var.get(u'firstCoverInitializedNameError'),var.get(u"null")):
            var.get(u'throwUnexpectedToken')(var.get(u'firstCoverInitializedNameError'))
        var.put(u'isBindingElement', var.get(u'oldIsBindingElement'))
        var.put(u'isAssignmentTarget', var.get(u'oldIsAssignmentTarget'))
        var.put(u'firstCoverInitializedNameError', var.get(u'oldFirstCoverInitializedNameError'))
        return var.get(u'result')
    PyJsHoisted_isolateCoverGrammar_.func_name = u'isolateCoverGrammar'
    var.put(u'isolateCoverGrammar', PyJsHoisted_isolateCoverGrammar_)
    @Js
    def PyJsHoisted_parseLeftHandSideExpression_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'expr', u'quasi', u'property', u'startToken'])
        pass
        var.get(u'assert')(var.get(u'state').get(u'allowIn'), Js(u'callee of new expression always allow in keyword.'))
        var.put(u'startToken', var.get(u'lookahead'))
        if (var.get(u'matchKeyword')(Js(u'super')) and var.get(u'state').get(u'inFunctionBody')):
            var.put(u'expr', var.get(u'Node').create())
            var.get(u'lex')()
            var.put(u'expr', var.get(u'expr').callprop(u'finishSuper'))
            if (var.get(u'match')(Js(u'[')).neg() and var.get(u'match')(Js(u'.')).neg()):
                var.get(u'throwUnexpectedToken')(var.get(u'lookahead'))
        else:
            var.put(u'expr', var.get(u'inheritCoverGrammar')((var.get(u'parseNewExpression') if var.get(u'matchKeyword')(Js(u'new')) else var.get(u'parsePrimaryExpression'))))
        #for JS loop

        while 1:
            if var.get(u'match')(Js(u'[')):
                var.put(u'isBindingElement', Js(False))
                var.put(u'isAssignmentTarget', var.get(u'true'))
                var.put(u'property', var.get(u'parseComputedMember')())
                var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishMemberExpression', Js(u'['), var.get(u'expr'), var.get(u'property')))
            else:
                if var.get(u'match')(Js(u'.')):
                    var.put(u'isBindingElement', Js(False))
                    var.put(u'isAssignmentTarget', var.get(u'true'))
                    var.put(u'property', var.get(u'parseNonComputedMember')())
                    var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishMemberExpression', Js(u'.'), var.get(u'expr'), var.get(u'property')))
                else:
                    if (PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Template')) and var.get(u'lookahead').get(u'head')):
                        var.put(u'quasi', var.get(u'parseTemplateLiteral')())
                        var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishTaggedTemplateExpression', var.get(u'expr'), var.get(u'quasi')))
                    else:
                        break

        return var.get(u'expr')
    PyJsHoisted_parseLeftHandSideExpression_.func_name = u'parseLeftHandSideExpression'
    var.put(u'parseLeftHandSideExpression', PyJsHoisted_parseLeftHandSideExpression_)
    @Js
    def PyJsHoisted_throwUnexpectedToken_(token, message, this, arguments, var=var):
        var = Scope({u'this':this, u'token':token, u'message':message, u'arguments':arguments}, var)
        var.registers([u'token', u'message'])
        PyJsTempException = JsToPyException(var.get(u'unexpectedTokenError')(var.get(u'token'), var.get(u'message')))
        raise PyJsTempException
    PyJsHoisted_throwUnexpectedToken_.func_name = u'throwUnexpectedToken'
    var.put(u'throwUnexpectedToken', PyJsHoisted_throwUnexpectedToken_)
    @Js
    def PyJsHoisted_parsePatternWithDefault_(params, kind, this, arguments, var=var):
        var = Scope({u'this':this, u'kind':kind, u'params':params, u'arguments':arguments}, var)
        var.registers([u'kind', u'right', u'startToken', u'params', u'previousAllowYield', u'pattern'])
        var.put(u'startToken', var.get(u'lookahead'))
        var.put(u'pattern', var.get(u'parsePattern')(var.get(u'params'), var.get(u'kind')))
        if var.get(u'match')(Js(u'=')):
            var.get(u'lex')()
            var.put(u'previousAllowYield', var.get(u'state').get(u'allowYield'))
            var.get(u'state').put(u'allowYield', var.get(u'true'))
            var.put(u'right', var.get(u'isolateCoverGrammar')(var.get(u'parseAssignmentExpression')))
            var.get(u'state').put(u'allowYield', var.get(u'previousAllowYield'))
            var.put(u'pattern', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishAssignmentPattern', var.get(u'pattern'), var.get(u'right')))
        return var.get(u'pattern')
    PyJsHoisted_parsePatternWithDefault_.func_name = u'parsePatternWithDefault'
    var.put(u'parsePatternWithDefault', PyJsHoisted_parsePatternWithDefault_)
    @Js
    def PyJsHoisted_parseExpressionStatement_(node, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'expr'])
        var.put(u'expr', var.get(u'parseExpression')())
        var.get(u'consumeSemicolon')()
        return var.get(u'node').callprop(u'finishExpressionStatement', var.get(u'expr'))
    PyJsHoisted_parseExpressionStatement_.func_name = u'parseExpressionStatement'
    var.put(u'parseExpressionStatement', PyJsHoisted_parseExpressionStatement_)
    @Js
    def PyJsHoisted_advanceSlash_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'checkToken', u'prevToken'])
        pass
        var.put(u'prevToken', var.get(u'extra').get(u'tokens').get((var.get(u'extra').get(u'tokens').get(u'length')-Js(1.0))))
        if var.get(u'prevToken').neg():
            return var.get(u'collectRegex')()
        if PyJsStrictEq(var.get(u'prevToken').get(u'type'),Js(u'Punctuator')):
            if PyJsStrictEq(var.get(u'prevToken').get(u'value'),Js(u']')):
                return var.get(u'scanPunctuator')()
            if PyJsStrictEq(var.get(u'prevToken').get(u'value'),Js(u')')):
                var.put(u'checkToken', var.get(u'extra').get(u'tokens').get((var.get(u'extra').get(u'openParenToken')-Js(1.0))))
                if ((var.get(u'checkToken') and PyJsStrictEq(var.get(u'checkToken').get(u'type'),Js(u'Keyword'))) and (((PyJsStrictEq(var.get(u'checkToken').get(u'value'),Js(u'if')) or PyJsStrictEq(var.get(u'checkToken').get(u'value'),Js(u'while'))) or PyJsStrictEq(var.get(u'checkToken').get(u'value'),Js(u'for'))) or PyJsStrictEq(var.get(u'checkToken').get(u'value'),Js(u'with')))):
                    return var.get(u'collectRegex')()
                return var.get(u'scanPunctuator')()
            if PyJsStrictEq(var.get(u'prevToken').get(u'value'),Js(u'}')):
                if (var.get(u'extra').get(u'tokens').get((var.get(u'extra').get(u'openCurlyToken')-Js(3.0))) and PyJsStrictEq(var.get(u'extra').get(u'tokens').get((var.get(u'extra').get(u'openCurlyToken')-Js(3.0))).get(u'type'),Js(u'Keyword'))):
                    var.put(u'checkToken', var.get(u'extra').get(u'tokens').get((var.get(u'extra').get(u'openCurlyToken')-Js(4.0))))
                    if var.get(u'checkToken').neg():
                        return var.get(u'scanPunctuator')()
                else:
                    if (var.get(u'extra').get(u'tokens').get((var.get(u'extra').get(u'openCurlyToken')-Js(4.0))) and PyJsStrictEq(var.get(u'extra').get(u'tokens').get((var.get(u'extra').get(u'openCurlyToken')-Js(4.0))).get(u'type'),Js(u'Keyword'))):
                        var.put(u'checkToken', var.get(u'extra').get(u'tokens').get((var.get(u'extra').get(u'openCurlyToken')-Js(5.0))))
                        if var.get(u'checkToken').neg():
                            return var.get(u'collectRegex')()
                    else:
                        return var.get(u'scanPunctuator')()
                if (var.get(u'FnExprTokens').callprop(u'indexOf', var.get(u'checkToken').get(u'value'))>=Js(0.0)):
                    return var.get(u'scanPunctuator')()
                return var.get(u'collectRegex')()
            return var.get(u'collectRegex')()
        if (PyJsStrictEq(var.get(u'prevToken').get(u'type'),Js(u'Keyword')) and PyJsStrictNeq(var.get(u'prevToken').get(u'value'),Js(u'this'))):
            return var.get(u'collectRegex')()
        return var.get(u'scanPunctuator')()
    PyJsHoisted_advanceSlash_.func_name = u'advanceSlash'
    var.put(u'advanceSlash', PyJsHoisted_advanceSlash_)
    @Js
    def PyJsHoisted_parseIfStatement_(node, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'arguments':arguments}, var)
        var.registers([u'test', u'node', u'alternate', u'consequent'])
        pass
        var.get(u'expectKeyword')(Js(u'if'))
        var.get(u'expect')(Js(u'('))
        var.put(u'test', var.get(u'parseExpression')())
        var.get(u'expect')(Js(u')'))
        var.put(u'consequent', var.get(u'parseStatement')())
        if var.get(u'matchKeyword')(Js(u'else')):
            var.get(u'lex')()
            var.put(u'alternate', var.get(u'parseStatement')())
        else:
            var.put(u'alternate', var.get(u"null"))
        return var.get(u'node').callprop(u'finishIfStatement', var.get(u'test'), var.get(u'consequent'), var.get(u'alternate'))
    PyJsHoisted_parseIfStatement_.func_name = u'parseIfStatement'
    var.put(u'parseIfStatement', PyJsHoisted_parseIfStatement_)
    @Js
    def PyJsHoisted_tolerateUnexpectedToken_(token, message, this, arguments, var=var):
        var = Scope({u'this':this, u'token':token, u'message':message, u'arguments':arguments}, var)
        var.registers([u'token', u'message', u'error'])
        var.put(u'error', var.get(u'unexpectedTokenError')(var.get(u'token'), var.get(u'message')))
        if var.get(u'extra').get(u'errors'):
            var.get(u'recordError')(var.get(u'error'))
        else:
            PyJsTempException = JsToPyException(var.get(u'error'))
            raise PyJsTempException
    PyJsHoisted_tolerateUnexpectedToken_.func_name = u'tolerateUnexpectedToken'
    var.put(u'tolerateUnexpectedToken', PyJsHoisted_tolerateUnexpectedToken_)
    @Js
    def PyJsHoisted_WrappingSourceLocation_(startToken, this, arguments, var=var):
        var = Scope({u'this':this, u'startToken':startToken, u'arguments':arguments}, var)
        var.registers([u'startToken'])
        PyJs_Object_48_ = Js({u'line':var.get(u'startToken').get(u'lineNumber'),u'column':(var.get(u'startToken').get(u'start')-var.get(u'startToken').get(u'lineStart'))})
        var.get(u"this").put(u'start', PyJs_Object_48_)
        var.get(u"this").put(u'end', var.get(u"null"))
    PyJsHoisted_WrappingSourceLocation_.func_name = u'WrappingSourceLocation'
    var.put(u'WrappingSourceLocation', PyJsHoisted_WrappingSourceLocation_)
    @Js
    def PyJsHoisted_scanStringLiteral_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'ch', u'octToDec', u'quote', u'start', u'str', u'unescaped', u'octal'])
        var.put(u'str', Js(u''))
        var.put(u'octal', Js(False))
        var.put(u'quote', var.get(u'source').get(var.get(u'index')))
        var.get(u'assert')((PyJsStrictEq(var.get(u'quote'),Js(u"'")) or PyJsStrictEq(var.get(u'quote'),Js(u'"'))), Js(u'String literal must starts with a quote'))
        var.put(u'start', var.get(u'index'))
        var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').get((var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1))))
            if PyJsStrictEq(var.get(u'ch'),var.get(u'quote')):
                var.put(u'quote', Js(u''))
                break
            else:
                if PyJsStrictEq(var.get(u'ch'),Js(u'\\')):
                    var.put(u'ch', var.get(u'source').get((var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1))))
                    if (var.get(u'ch').neg() or var.get(u'isLineTerminator')(var.get(u'ch').callprop(u'charCodeAt', Js(0.0))).neg()):
                        while 1:
                            SWITCHED = False
                            CONDITION = (var.get(u'ch'))
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'u')):
                                SWITCHED = True
                                pass
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'x')):
                                SWITCHED = True
                                if PyJsStrictEq(var.get(u'source').get(var.get(u'index')),Js(u'{')):
                                    var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                                    var.put(u'str', var.get(u'scanUnicodeCodePointEscape')(), u'+')
                                else:
                                    var.put(u'unescaped', var.get(u'scanHexEscape')(var.get(u'ch')))
                                    if var.get(u'unescaped').neg():
                                        PyJsTempException = JsToPyException(var.get(u'throwUnexpectedToken')())
                                        raise PyJsTempException
                                    var.put(u'str', var.get(u'unescaped'), u'+')
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'n')):
                                SWITCHED = True
                                var.put(u'str', Js(u'\n'), u'+')
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'r')):
                                SWITCHED = True
                                var.put(u'str', Js(u'\r'), u'+')
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(u't')):
                                SWITCHED = True
                                var.put(u'str', Js(u'\t'), u'+')
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'b')):
                                SWITCHED = True
                                var.put(u'str', Js(u'\x08'), u'+')
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'f')):
                                SWITCHED = True
                                var.put(u'str', Js(u'\x0c'), u'+')
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'v')):
                                SWITCHED = True
                                var.put(u'str', Js(u'\x0b'), u'+')
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'8')):
                                SWITCHED = True
                                pass
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'9')):
                                SWITCHED = True
                                var.put(u'str', var.get(u'ch'), u'+')
                                var.get(u'tolerateUnexpectedToken')()
                                break
                            if True:
                                SWITCHED = True
                                if var.get(u'isOctalDigit')(var.get(u'ch')):
                                    var.put(u'octToDec', var.get(u'octalToDecimal')(var.get(u'ch')))
                                    var.put(u'octal', (var.get(u'octToDec').get(u'octal') or var.get(u'octal')))
                                    var.put(u'str', var.get(u'String').callprop(u'fromCharCode', var.get(u'octToDec').get(u'code')), u'+')
                                else:
                                    var.put(u'str', var.get(u'ch'), u'+')
                                break
                            SWITCHED = True
                            break
                    else:
                        var.put(u'lineNumber',Js(var.get(u'lineNumber').to_number())+Js(1))
                        if (PyJsStrictEq(var.get(u'ch'),Js(u'\r')) and PyJsStrictEq(var.get(u'source').get(var.get(u'index')),Js(u'\n'))):
                            var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                        var.put(u'lineStart', var.get(u'index'))
                else:
                    if var.get(u'isLineTerminator')(var.get(u'ch').callprop(u'charCodeAt', Js(0.0))):
                        break
                    else:
                        var.put(u'str', var.get(u'ch'), u'+')
        if PyJsStrictNeq(var.get(u'quote'),Js(u'')):
            var.get(u'throwUnexpectedToken')()
        PyJs_Object_28_ = Js({u'type':var.get(u'Token').get(u'StringLiteral'),u'value':var.get(u'str'),u'octal':var.get(u'octal'),u'lineNumber':var.get(u'startLineNumber'),u'lineStart':var.get(u'startLineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
        return PyJs_Object_28_
    PyJsHoisted_scanStringLiteral_.func_name = u'scanStringLiteral'
    var.put(u'scanStringLiteral', PyJsHoisted_scanStringLiteral_)
    @Js
    def PyJsHoisted_parseThrowStatement_(node, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'argument'])
        pass
        var.get(u'expectKeyword')(Js(u'throw'))
        if var.get(u'hasLineTerminator'):
            var.get(u'throwError')(var.get(u'Messages').get(u'NewlineAfterThrow'))
        var.put(u'argument', var.get(u'parseExpression')())
        var.get(u'consumeSemicolon')()
        return var.get(u'node').callprop(u'finishThrowStatement', var.get(u'argument'))
    PyJsHoisted_parseThrowStatement_.func_name = u'parseThrowStatement'
    var.put(u'parseThrowStatement', PyJsHoisted_parseThrowStatement_)
    @Js
    def PyJsHoisted_addComment_(type, value, start, end, loc, this, arguments, var=var):
        var = Scope({u'start':start, u'end':end, u'arguments':arguments, u'loc':loc, u'this':this, u'type':type, u'value':value}, var)
        var.registers([u'comment', u'loc', u'end', u'value', u'start', u'type'])
        pass
        var.get(u'assert')(PyJsStrictEq(var.get(u'start',throw=False).typeof(),Js(u'number')), Js(u'Comment must have valid position'))
        var.get(u'state').put(u'lastCommentStart', var.get(u'start'))
        PyJs_Object_11_ = Js({u'type':var.get(u'type'),u'value':var.get(u'value')})
        var.put(u'comment', PyJs_Object_11_)
        if var.get(u'extra').get(u'range'):
            var.get(u'comment').put(u'range', Js([var.get(u'start'), var.get(u'end')]))
        if var.get(u'extra').get(u'loc'):
            var.get(u'comment').put(u'loc', var.get(u'loc'))
        var.get(u'extra').get(u'comments').callprop(u'push', var.get(u'comment'))
        if var.get(u'extra').get(u'attachComment'):
            var.get(u'extra').get(u'leadingComments').callprop(u'push', var.get(u'comment'))
            var.get(u'extra').get(u'trailingComments').callprop(u'push', var.get(u'comment'))
    PyJsHoisted_addComment_.func_name = u'addComment'
    var.put(u'addComment', PyJsHoisted_addComment_)
    @Js
    def PyJsHoisted_parseSwitchStatement_(node, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'discriminant', u'clause', u'defaultFound', u'oldInSwitch', u'cases'])
        pass
        var.get(u'expectKeyword')(Js(u'switch'))
        var.get(u'expect')(Js(u'('))
        var.put(u'discriminant', var.get(u'parseExpression')())
        var.get(u'expect')(Js(u')'))
        var.get(u'expect')(Js(u'{'))
        var.put(u'cases', Js([]))
        if var.get(u'match')(Js(u'}')):
            var.get(u'lex')()
            return var.get(u'node').callprop(u'finishSwitchStatement', var.get(u'discriminant'), var.get(u'cases'))
        var.put(u'oldInSwitch', var.get(u'state').get(u'inSwitch'))
        var.get(u'state').put(u'inSwitch', var.get(u'true'))
        var.put(u'defaultFound', Js(False))
        while (var.get(u'startIndex')<var.get(u'length')):
            if var.get(u'match')(Js(u'}')):
                break
            var.put(u'clause', var.get(u'parseSwitchCase')())
            if PyJsStrictEq(var.get(u'clause').get(u'test'),var.get(u"null")):
                if var.get(u'defaultFound'):
                    var.get(u'throwError')(var.get(u'Messages').get(u'MultipleDefaultsInSwitch'))
                var.put(u'defaultFound', var.get(u'true'))
            var.get(u'cases').callprop(u'push', var.get(u'clause'))
        var.get(u'state').put(u'inSwitch', var.get(u'oldInSwitch'))
        var.get(u'expect')(Js(u'}'))
        return var.get(u'node').callprop(u'finishSwitchStatement', var.get(u'discriminant'), var.get(u'cases'))
    PyJsHoisted_parseSwitchStatement_.func_name = u'parseSwitchStatement'
    var.put(u'parseSwitchStatement', PyJsHoisted_parseSwitchStatement_)
    @Js
    def PyJsHoisted_match_(value, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'value':value}, var)
        var.registers([u'value'])
        return (PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Punctuator')) and PyJsStrictEq(var.get(u'lookahead').get(u'value'),var.get(u'value')))
    PyJsHoisted_match_.func_name = u'match'
    var.put(u'match', PyJsHoisted_match_)
    @Js
    def PyJsHoisted_parseEmptyStatement_(node, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'arguments':arguments}, var)
        var.registers([u'node'])
        var.get(u'expect')(Js(u';'))
        return var.get(u'node').callprop(u'finishEmptyStatement')
    PyJsHoisted_parseEmptyStatement_.func_name = u'parseEmptyStatement'
    var.put(u'parseEmptyStatement', PyJsHoisted_parseEmptyStatement_)
    @Js
    def PyJsHoisted_validateParam_(options, param, name, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'options':options, u'param':param, u'name':name}, var)
        var.registers([u'param', u'options', u'key', u'name'])
        var.put(u'key', (Js(u'$')+var.get(u'name')))
        if var.get(u'strict'):
            if var.get(u'isRestrictedWord')(var.get(u'name')):
                var.get(u'options').put(u'stricted', var.get(u'param'))
                var.get(u'options').put(u'message', var.get(u'Messages').get(u'StrictParamName'))
            if var.get(u'Object').get(u'prototype').get(u'hasOwnProperty').callprop(u'call', var.get(u'options').get(u'paramSet'), var.get(u'key')):
                var.get(u'options').put(u'stricted', var.get(u'param'))
                var.get(u'options').put(u'message', var.get(u'Messages').get(u'StrictParamDupe'))
        else:
            if var.get(u'options').get(u'firstRestricted').neg():
                if var.get(u'isRestrictedWord')(var.get(u'name')):
                    var.get(u'options').put(u'firstRestricted', var.get(u'param'))
                    var.get(u'options').put(u'message', var.get(u'Messages').get(u'StrictParamName'))
                else:
                    if var.get(u'isStrictModeReservedWord')(var.get(u'name')):
                        var.get(u'options').put(u'firstRestricted', var.get(u'param'))
                        var.get(u'options').put(u'message', var.get(u'Messages').get(u'StrictReservedWord'))
                    else:
                        if var.get(u'Object').get(u'prototype').get(u'hasOwnProperty').callprop(u'call', var.get(u'options').get(u'paramSet'), var.get(u'key')):
                            var.get(u'options').put(u'stricted', var.get(u'param'))
                            var.get(u'options').put(u'message', var.get(u'Messages').get(u'StrictParamDupe'))
        var.get(u'options').get(u'paramSet').put(var.get(u'key'), var.get(u'true'))
    PyJsHoisted_validateParam_.func_name = u'validateParam'
    var.put(u'validateParam', PyJsHoisted_validateParam_)
    @Js
    def PyJsHoisted_parseConditionalExpression_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'previousAllowIn', u'expr', u'alternate', u'startToken', u'consequent'])
        pass
        var.put(u'startToken', var.get(u'lookahead'))
        var.put(u'expr', var.get(u'inheritCoverGrammar')(var.get(u'parseBinaryExpression')))
        if var.get(u'match')(Js(u'?')):
            var.get(u'lex')()
            var.put(u'previousAllowIn', var.get(u'state').get(u'allowIn'))
            var.get(u'state').put(u'allowIn', var.get(u'true'))
            var.put(u'consequent', var.get(u'isolateCoverGrammar')(var.get(u'parseAssignmentExpression')))
            var.get(u'state').put(u'allowIn', var.get(u'previousAllowIn'))
            var.get(u'expect')(Js(u':'))
            var.put(u'alternate', var.get(u'isolateCoverGrammar')(var.get(u'parseAssignmentExpression')))
            var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishConditionalExpression', var.get(u'expr'), var.get(u'consequent'), var.get(u'alternate')))
            var.put(u'isAssignmentTarget', var.put(u'isBindingElement', Js(False)))
        return var.get(u'expr')
    PyJsHoisted_parseConditionalExpression_.func_name = u'parseConditionalExpression'
    var.put(u'parseConditionalExpression', PyJsHoisted_parseConditionalExpression_)
    @Js
    def PyJsHoisted_parseStatementListItem_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        if PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Keyword')):
            while 1:
                SWITCHED = False
                CONDITION = (var.get(u'lookahead').get(u'value'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'export')):
                    SWITCHED = True
                    if PyJsStrictNeq(var.get(u'state').get(u'sourceType'),Js(u'module')):
                        var.get(u'tolerateUnexpectedToken')(var.get(u'lookahead'), var.get(u'Messages').get(u'IllegalExportDeclaration'))
                    return var.get(u'parseExportDeclaration')()
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'import')):
                    SWITCHED = True
                    if PyJsStrictNeq(var.get(u'state').get(u'sourceType'),Js(u'module')):
                        var.get(u'tolerateUnexpectedToken')(var.get(u'lookahead'), var.get(u'Messages').get(u'IllegalImportDeclaration'))
                    return var.get(u'parseImportDeclaration')()
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'const')):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'let')):
                    SWITCHED = True
                    PyJs_Object_138_ = Js({u'inFor':Js(False)})
                    return var.get(u'parseLexicalDeclaration')(PyJs_Object_138_)
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'function')):
                    SWITCHED = True
                    return var.get(u'parseFunctionDeclaration')(var.get(u'Node').create())
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'class')):
                    SWITCHED = True
                    return var.get(u'parseClassDeclaration')()
                SWITCHED = True
                break
        return var.get(u'parseStatement')()
    PyJsHoisted_parseStatementListItem_.func_name = u'parseStatementListItem'
    var.put(u'parseStatementListItem', PyJsHoisted_parseStatementListItem_)
    @Js
    def PyJsHoisted_parseClassDeclaration_(identifierIsOptional, this, arguments, var=var):
        var = Scope({u'this':this, u'identifierIsOptional':identifierIsOptional, u'arguments':arguments}, var)
        var.registers([u'identifierIsOptional', u'previousStrict', u'superClass', u'classNode', u'id', u'classBody'])
        var.put(u'id', var.get(u"null"))
        var.put(u'superClass', var.get(u"null"))
        var.put(u'classNode', var.get(u'Node').create())
        var.put(u'previousStrict', var.get(u'strict'))
        var.put(u'strict', var.get(u'true'))
        var.get(u'expectKeyword')(Js(u'class'))
        if (var.get(u'identifierIsOptional').neg() or PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Identifier'))):
            var.put(u'id', var.get(u'parseVariableIdentifier')())
        if var.get(u'matchKeyword')(Js(u'extends')):
            var.get(u'lex')()
            var.put(u'superClass', var.get(u'isolateCoverGrammar')(var.get(u'parseLeftHandSideExpressionAllowCall')))
        var.put(u'classBody', var.get(u'parseClassBody')())
        var.put(u'strict', var.get(u'previousStrict'))
        return var.get(u'classNode').callprop(u'finishClassDeclaration', var.get(u'id'), var.get(u'superClass'), var.get(u'classBody'))
    PyJsHoisted_parseClassDeclaration_.func_name = u'parseClassDeclaration'
    var.put(u'parseClassDeclaration', PyJsHoisted_parseClassDeclaration_)
    @Js
    def PyJsHoisted_parseVariableDeclaration_(options, this, arguments, var=var):
        var = Scope({u'this':this, u'options':options, u'arguments':arguments}, var)
        var.registers([u'node', u'init', u'params', u'id', u'options'])
        var.put(u'init', var.get(u"null"))
        var.put(u'node', var.get(u'Node').create())
        var.put(u'params', Js([]))
        var.put(u'id', var.get(u'parsePattern')(var.get(u'params'), Js(u'var')))
        if (var.get(u'strict') and var.get(u'isRestrictedWord')(var.get(u'id').get(u'name'))):
            var.get(u'tolerateError')(var.get(u'Messages').get(u'StrictVarName'))
        if var.get(u'match')(Js(u'=')):
            var.get(u'lex')()
            var.put(u'init', var.get(u'isolateCoverGrammar')(var.get(u'parseAssignmentExpression')))
        else:
            if (PyJsStrictNeq(var.get(u'id').get(u'type'),var.get(u'Syntax').get(u'Identifier')) and var.get(u'options').get(u'inFor').neg()):
                var.get(u'expect')(Js(u'='))
        return var.get(u'node').callprop(u'finishVariableDeclarator', var.get(u'id'), var.get(u'init'))
    PyJsHoisted_parseVariableDeclaration_.func_name = u'parseVariableDeclaration'
    var.put(u'parseVariableDeclaration', PyJsHoisted_parseVariableDeclaration_)
    @Js
    def PyJsHoisted_reinterpretExpressionAsPattern_(expr, this, arguments, var=var):
        var = Scope({u'this':this, u'expr':expr, u'arguments':arguments}, var)
        var.registers([u'i', u'expr'])
        pass
        while 1:
            SWITCHED = False
            CONDITION = (var.get(u'expr').get(u'type'))
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Syntax').get(u'Identifier')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Syntax').get(u'MemberExpression')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Syntax').get(u'RestElement')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Syntax').get(u'AssignmentPattern')):
                SWITCHED = True
                break
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Syntax').get(u'SpreadElement')):
                SWITCHED = True
                var.get(u'expr').put(u'type', var.get(u'Syntax').get(u'RestElement'))
                var.get(u'reinterpretExpressionAsPattern')(var.get(u'expr').get(u'argument'))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Syntax').get(u'ArrayExpression')):
                SWITCHED = True
                var.get(u'expr').put(u'type', var.get(u'Syntax').get(u'ArrayPattern'))
                #for JS loop
                var.put(u'i', Js(0.0))
                while (var.get(u'i')<var.get(u'expr').get(u'elements').get(u'length')):
                    try:
                        if PyJsStrictNeq(var.get(u'expr').get(u'elements').get(var.get(u'i')),var.get(u"null")):
                            var.get(u'reinterpretExpressionAsPattern')(var.get(u'expr').get(u'elements').get(var.get(u'i')))
                    finally:
                            (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Syntax').get(u'ObjectExpression')):
                SWITCHED = True
                var.get(u'expr').put(u'type', var.get(u'Syntax').get(u'ObjectPattern'))
                #for JS loop
                var.put(u'i', Js(0.0))
                while (var.get(u'i')<var.get(u'expr').get(u'properties').get(u'length')):
                    try:
                        var.get(u'reinterpretExpressionAsPattern')(var.get(u'expr').get(u'properties').get(var.get(u'i')).get(u'value'))
                    finally:
                            (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Syntax').get(u'AssignmentExpression')):
                SWITCHED = True
                var.get(u'expr').put(u'type', var.get(u'Syntax').get(u'AssignmentPattern'))
                var.get(u'reinterpretExpressionAsPattern')(var.get(u'expr').get(u'left'))
                break
            if True:
                SWITCHED = True
                break
            SWITCHED = True
            break
    PyJsHoisted_reinterpretExpressionAsPattern_.func_name = u'reinterpretExpressionAsPattern'
    var.put(u'reinterpretExpressionAsPattern', PyJsHoisted_reinterpretExpressionAsPattern_)
    @Js
    def PyJsHoisted_getComplexIdentifier_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'ch', u'cp', u'id'])
        pass
        var.put(u'cp', var.get(u'codePointAt')(var.get(u'index')))
        var.put(u'id', var.get(u'fromCodePoint')(var.get(u'cp')))
        var.put(u'index', var.get(u'id').get(u'length'), u'+')
        if PyJsStrictEq(var.get(u'cp'),Js(92)):
            if PyJsStrictNeq(var.get(u'source').callprop(u'charCodeAt', var.get(u'index')),Js(117)):
                var.get(u'throwUnexpectedToken')()
            var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
            if PyJsStrictEq(var.get(u'source').get(var.get(u'index')),Js(u'{')):
                var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                var.put(u'ch', var.get(u'scanUnicodeCodePointEscape')())
            else:
                var.put(u'ch', var.get(u'scanHexEscape')(Js(u'u')))
                var.put(u'cp', var.get(u'ch').callprop(u'charCodeAt', Js(0.0)))
                if ((var.get(u'ch').neg() or PyJsStrictEq(var.get(u'ch'),Js(u'\\'))) or var.get(u'isIdentifierStart')(var.get(u'cp')).neg()):
                    var.get(u'throwUnexpectedToken')()
            var.put(u'id', var.get(u'ch'))
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'cp', var.get(u'codePointAt')(var.get(u'index')))
            if var.get(u'isIdentifierPart')(var.get(u'cp')).neg():
                break
            var.put(u'ch', var.get(u'fromCodePoint')(var.get(u'cp')))
            var.put(u'id', var.get(u'ch'), u'+')
            var.put(u'index', var.get(u'ch').get(u'length'), u'+')
            if PyJsStrictEq(var.get(u'cp'),Js(92)):
                var.put(u'id', var.get(u'id').callprop(u'substr', Js(0.0), (var.get(u'id').get(u'length')-Js(1.0))))
                if PyJsStrictNeq(var.get(u'source').callprop(u'charCodeAt', var.get(u'index')),Js(117)):
                    var.get(u'throwUnexpectedToken')()
                var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                if PyJsStrictEq(var.get(u'source').get(var.get(u'index')),Js(u'{')):
                    var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                    var.put(u'ch', var.get(u'scanUnicodeCodePointEscape')())
                else:
                    var.put(u'ch', var.get(u'scanHexEscape')(Js(u'u')))
                    var.put(u'cp', var.get(u'ch').callprop(u'charCodeAt', Js(0.0)))
                    if ((var.get(u'ch').neg() or PyJsStrictEq(var.get(u'ch'),Js(u'\\'))) or var.get(u'isIdentifierPart')(var.get(u'cp')).neg()):
                        var.get(u'throwUnexpectedToken')()
                var.put(u'id', var.get(u'ch'), u'+')
        return var.get(u'id')
    PyJsHoisted_getComplexIdentifier_.func_name = u'getComplexIdentifier'
    var.put(u'getComplexIdentifier', PyJsHoisted_getComplexIdentifier_)
    @Js
    def PyJsHoisted_Position_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        var.get(u"this").put(u'line', var.get(u'startLineNumber'))
        var.get(u"this").put(u'column', (var.get(u'startIndex')-var.get(u'startLineStart')))
    PyJsHoisted_Position_.func_name = u'Position'
    var.put(u'Position', PyJsHoisted_Position_)
    @Js
    def PyJsHoisted_isWhiteSpace_(ch, this, arguments, var=var):
        var = Scope({u'this':this, u'ch':ch, u'arguments':arguments}, var)
        var.registers([u'ch'])
        def PyJs_LONG_9_(var=var):
            return (((((PyJsStrictEq(var.get(u'ch'),Js(32)) or PyJsStrictEq(var.get(u'ch'),Js(9))) or PyJsStrictEq(var.get(u'ch'),Js(11))) or PyJsStrictEq(var.get(u'ch'),Js(12))) or PyJsStrictEq(var.get(u'ch'),Js(160))) or ((var.get(u'ch')>=Js(5760)) and (Js([Js(5760), Js(6158), Js(8192), Js(8193), Js(8194), Js(8195), Js(8196), Js(8197), Js(8198), Js(8199), Js(8200), Js(8201), Js(8202), Js(8239), Js(8287), Js(12288), Js(65279)]).callprop(u'indexOf', var.get(u'ch'))>=Js(0.0))))
        return PyJs_LONG_9_()
    PyJsHoisted_isWhiteSpace_.func_name = u'isWhiteSpace'
    var.put(u'isWhiteSpace', PyJsHoisted_isWhiteSpace_)
    @Js
    def PyJsHoisted_parseWhileStatement_(node, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'arguments':arguments}, var)
        var.registers([u'test', u'body', u'node', u'oldInIteration'])
        pass
        var.get(u'expectKeyword')(Js(u'while'))
        var.get(u'expect')(Js(u'('))
        var.put(u'test', var.get(u'parseExpression')())
        var.get(u'expect')(Js(u')'))
        var.put(u'oldInIteration', var.get(u'state').get(u'inIteration'))
        var.get(u'state').put(u'inIteration', var.get(u'true'))
        var.put(u'body', var.get(u'parseStatement')())
        var.get(u'state').put(u'inIteration', var.get(u'oldInIteration'))
        return var.get(u'node').callprop(u'finishWhileStatement', var.get(u'test'), var.get(u'body'))
    PyJsHoisted_parseWhileStatement_.func_name = u'parseWhileStatement'
    var.put(u'parseWhileStatement', PyJsHoisted_parseWhileStatement_)
    @Js
    def PyJsHoisted_parseTemplateLiteral_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'quasis', u'node', u'quasi', u'expressions'])
        var.put(u'node', var.get(u'Node').create())
        PyJs_Object_128_ = Js({u'head':var.get(u'true')})
        var.put(u'quasi', var.get(u'parseTemplateElement')(PyJs_Object_128_))
        var.put(u'quasis', Js([var.get(u'quasi')]))
        var.put(u'expressions', Js([]))
        while var.get(u'quasi').get(u'tail').neg():
            var.get(u'expressions').callprop(u'push', var.get(u'parseExpression')())
            PyJs_Object_129_ = Js({u'head':Js(False)})
            var.put(u'quasi', var.get(u'parseTemplateElement')(PyJs_Object_129_))
            var.get(u'quasis').callprop(u'push', var.get(u'quasi'))
        return var.get(u'node').callprop(u'finishTemplateLiteral', var.get(u'quasis'), var.get(u'expressions'))
    PyJsHoisted_parseTemplateLiteral_.func_name = u'parseTemplateLiteral'
    var.put(u'parseTemplateLiteral', PyJsHoisted_parseTemplateLiteral_)
    @Js
    def PyJsHoisted_parseTemplateElement_(option, this, arguments, var=var):
        var = Scope({u'this':this, u'option':option, u'arguments':arguments}, var)
        var.registers([u'node', u'token', u'option'])
        pass
        if (PyJsStrictNeq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Template')) or (var.get(u'option').get(u'head') and var.get(u'lookahead').get(u'head').neg())):
            var.get(u'throwUnexpectedToken')()
        var.put(u'node', var.get(u'Node').create())
        var.put(u'token', var.get(u'lex')())
        PyJs_Object_127_ = Js({u'raw':var.get(u'token').get(u'value').get(u'raw'),u'cooked':var.get(u'token').get(u'value').get(u'cooked')})
        return var.get(u'node').callprop(u'finishTemplateElement', PyJs_Object_127_, var.get(u'token').get(u'tail'))
    PyJsHoisted_parseTemplateElement_.func_name = u'parseTemplateElement'
    var.put(u'parseTemplateElement', PyJsHoisted_parseTemplateElement_)
    @Js
    def PyJsHoisted_parseGroupExpression_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'i', u'expr', u'expressions', u'params', u'startToken'])
        var.put(u'params', Js([]))
        var.get(u'expect')(Js(u'('))
        if var.get(u'match')(Js(u')')):
            var.get(u'lex')()
            if var.get(u'match')(Js(u'=>')).neg():
                var.get(u'expect')(Js(u'=>'))
            PyJs_Object_130_ = Js({u'type':var.get(u'PlaceHolders').get(u'ArrowParameterPlaceHolder'),u'params':Js([]),u'rawParams':Js([])})
            return PyJs_Object_130_
        var.put(u'startToken', var.get(u'lookahead'))
        if var.get(u'match')(Js(u'...')):
            var.put(u'expr', var.get(u'parseRestElement')(var.get(u'params')))
            var.get(u'expect')(Js(u')'))
            if var.get(u'match')(Js(u'=>')).neg():
                var.get(u'expect')(Js(u'=>'))
            PyJs_Object_131_ = Js({u'type':var.get(u'PlaceHolders').get(u'ArrowParameterPlaceHolder'),u'params':Js([var.get(u'expr')])})
            return PyJs_Object_131_
        var.put(u'isBindingElement', var.get(u'true'))
        var.put(u'expr', var.get(u'inheritCoverGrammar')(var.get(u'parseAssignmentExpression')))
        if var.get(u'match')(Js(u',')):
            var.put(u'isAssignmentTarget', Js(False))
            var.put(u'expressions', Js([var.get(u'expr')]))
            while (var.get(u'startIndex')<var.get(u'length')):
                if var.get(u'match')(Js(u',')).neg():
                    break
                var.get(u'lex')()
                if var.get(u'match')(Js(u'...')):
                    if var.get(u'isBindingElement').neg():
                        var.get(u'throwUnexpectedToken')(var.get(u'lookahead'))
                    var.get(u'expressions').callprop(u'push', var.get(u'parseRestElement')(var.get(u'params')))
                    var.get(u'expect')(Js(u')'))
                    if var.get(u'match')(Js(u'=>')).neg():
                        var.get(u'expect')(Js(u'=>'))
                    var.put(u'isBindingElement', Js(False))
                    #for JS loop
                    var.put(u'i', Js(0.0))
                    while (var.get(u'i')<var.get(u'expressions').get(u'length')):
                        try:
                            var.get(u'reinterpretExpressionAsPattern')(var.get(u'expressions').get(var.get(u'i')))
                        finally:
                                (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
                    PyJs_Object_132_ = Js({u'type':var.get(u'PlaceHolders').get(u'ArrowParameterPlaceHolder'),u'params':var.get(u'expressions')})
                    return PyJs_Object_132_
                var.get(u'expressions').callprop(u'push', var.get(u'inheritCoverGrammar')(var.get(u'parseAssignmentExpression')))
            var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishSequenceExpression', var.get(u'expressions')))
        var.get(u'expect')(Js(u')'))
        if var.get(u'match')(Js(u'=>')):
            if (PyJsStrictEq(var.get(u'expr').get(u'type'),var.get(u'Syntax').get(u'Identifier')) and PyJsStrictEq(var.get(u'expr').get(u'name'),Js(u'yield'))):
                PyJs_Object_133_ = Js({u'type':var.get(u'PlaceHolders').get(u'ArrowParameterPlaceHolder'),u'params':Js([var.get(u'expr')])})
                return PyJs_Object_133_
            if var.get(u'isBindingElement').neg():
                var.get(u'throwUnexpectedToken')(var.get(u'lookahead'))
            if PyJsStrictEq(var.get(u'expr').get(u'type'),var.get(u'Syntax').get(u'SequenceExpression')):
                #for JS loop
                var.put(u'i', Js(0.0))
                while (var.get(u'i')<var.get(u'expr').get(u'expressions').get(u'length')):
                    try:
                        var.get(u'reinterpretExpressionAsPattern')(var.get(u'expr').get(u'expressions').get(var.get(u'i')))
                    finally:
                            (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
            else:
                var.get(u'reinterpretExpressionAsPattern')(var.get(u'expr'))
            PyJs_Object_134_ = Js({u'type':var.get(u'PlaceHolders').get(u'ArrowParameterPlaceHolder'),u'params':(var.get(u'expr').get(u'expressions') if PyJsStrictEq(var.get(u'expr').get(u'type'),var.get(u'Syntax').get(u'SequenceExpression')) else Js([var.get(u'expr')]))})
            var.put(u'expr', PyJs_Object_134_)
        var.put(u'isBindingElement', Js(False))
        return var.get(u'expr')
    PyJsHoisted_parseGroupExpression_.func_name = u'parseGroupExpression'
    var.put(u'parseGroupExpression', PyJsHoisted_parseGroupExpression_)
    @Js
    def PyJsHoisted_scanHexLiteral_(start, this, arguments, var=var):
        var = Scope({u'this':this, u'start':start, u'arguments':arguments}, var)
        var.registers([u'start', u'number'])
        var.put(u'number', Js(u''))
        while (var.get(u'index')<var.get(u'length')):
            if var.get(u'isHexDigit')(var.get(u'source').get(var.get(u'index'))).neg():
                break
            var.put(u'number', var.get(u'source').get((var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1))), u'+')
        if PyJsStrictEq(var.get(u'number').get(u'length'),Js(0.0)):
            var.get(u'throwUnexpectedToken')()
        if var.get(u'isIdentifierStart')(var.get(u'source').callprop(u'charCodeAt', var.get(u'index'))):
            var.get(u'throwUnexpectedToken')()
        PyJs_Object_24_ = Js({u'type':var.get(u'Token').get(u'NumericLiteral'),u'value':var.get(u'parseInt')((Js(u'0x')+var.get(u'number')), Js(16.0)),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
        return PyJs_Object_24_
    PyJsHoisted_scanHexLiteral_.func_name = u'scanHexLiteral'
    var.put(u'scanHexLiteral', PyJsHoisted_scanHexLiteral_)
    @Js
    def PyJsHoisted_parseBreakStatement_(node, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'key', u'label'])
        var.put(u'label', var.get(u"null"))
        var.get(u'expectKeyword')(Js(u'break'))
        if PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt', var.get(u'lastIndex')),Js(59)):
            var.get(u'lex')()
            if (var.get(u'state').get(u'inIteration') or var.get(u'state').get(u'inSwitch')).neg():
                var.get(u'throwError')(var.get(u'Messages').get(u'IllegalBreak'))
            return var.get(u'node').callprop(u'finishBreakStatement', var.get(u"null"))
        if var.get(u'hasLineTerminator'):
            if (var.get(u'state').get(u'inIteration') or var.get(u'state').get(u'inSwitch')).neg():
                var.get(u'throwError')(var.get(u'Messages').get(u'IllegalBreak'))
            return var.get(u'node').callprop(u'finishBreakStatement', var.get(u"null"))
        if PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Identifier')):
            var.put(u'label', var.get(u'parseVariableIdentifier')())
            var.put(u'key', (Js(u'$')+var.get(u'label').get(u'name')))
            if var.get(u'Object').get(u'prototype').get(u'hasOwnProperty').callprop(u'call', var.get(u'state').get(u'labelSet'), var.get(u'key')).neg():
                var.get(u'throwError')(var.get(u'Messages').get(u'UnknownLabel'), var.get(u'label').get(u'name'))
        var.get(u'consumeSemicolon')()
        if (PyJsStrictEq(var.get(u'label'),var.get(u"null")) and (var.get(u'state').get(u'inIteration') or var.get(u'state').get(u'inSwitch')).neg()):
            var.get(u'throwError')(var.get(u'Messages').get(u'IllegalBreak'))
        return var.get(u'node').callprop(u'finishBreakStatement', var.get(u'label'))
    PyJsHoisted_parseBreakStatement_.func_name = u'parseBreakStatement'
    var.put(u'parseBreakStatement', PyJsHoisted_parseBreakStatement_)
    @Js
    def PyJsHoisted_scanBinaryLiteral_(start, this, arguments, var=var):
        var = Scope({u'this':this, u'start':start, u'arguments':arguments}, var)
        var.registers([u'start', u'ch', u'number'])
        pass
        var.put(u'number', Js(u''))
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').get(var.get(u'index')))
            if (PyJsStrictNeq(var.get(u'ch'),Js(u'0')) and PyJsStrictNeq(var.get(u'ch'),Js(u'1'))):
                break
            var.put(u'number', var.get(u'source').get((var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1))), u'+')
        if PyJsStrictEq(var.get(u'number').get(u'length'),Js(0.0)):
            var.get(u'throwUnexpectedToken')()
        if (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').callprop(u'charCodeAt', var.get(u'index')))
            if (var.get(u'isIdentifierStart')(var.get(u'ch')) or var.get(u'isDecimalDigit')(var.get(u'ch'))):
                var.get(u'throwUnexpectedToken')()
        PyJs_Object_25_ = Js({u'type':var.get(u'Token').get(u'NumericLiteral'),u'value':var.get(u'parseInt')(var.get(u'number'), Js(2.0)),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
        return PyJs_Object_25_
    PyJsHoisted_scanBinaryLiteral_.func_name = u'scanBinaryLiteral'
    var.put(u'scanBinaryLiteral', PyJsHoisted_scanBinaryLiteral_)
    @Js
    def PyJsHoisted_parseYieldExpression_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'expr', u'previousAllowYield', u'argument', u'delegate'])
        pass
        var.put(u'argument', var.get(u"null"))
        var.put(u'expr', var.get(u'Node').create())
        var.get(u'expectKeyword')(Js(u'yield'))
        if var.get(u'hasLineTerminator').neg():
            var.put(u'previousAllowYield', var.get(u'state').get(u'allowYield'))
            var.get(u'state').put(u'allowYield', Js(False))
            var.put(u'delegate', var.get(u'match')(Js(u'*')))
            if var.get(u'delegate'):
                var.get(u'lex')()
                var.put(u'argument', var.get(u'parseAssignmentExpression')())
            else:
                if (((var.get(u'match')(Js(u';')).neg() and var.get(u'match')(Js(u'}')).neg()) and var.get(u'match')(Js(u')')).neg()) and PyJsStrictNeq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'EOF'))):
                    var.put(u'argument', var.get(u'parseAssignmentExpression')())
            var.get(u'state').put(u'allowYield', var.get(u'previousAllowYield'))
        return var.get(u'expr').callprop(u'finishYieldExpression', var.get(u'argument'), var.get(u'delegate'))
    PyJsHoisted_parseYieldExpression_.func_name = u'parseYieldExpression'
    var.put(u'parseYieldExpression', PyJsHoisted_parseYieldExpression_)
    @Js
    def PyJsHoisted_expectCommaSeparator_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'token'])
        pass
        if var.get(u'extra').get(u'errors'):
            var.put(u'token', var.get(u'lookahead'))
            if (PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Punctuator')) and PyJsStrictEq(var.get(u'token').get(u'value'),Js(u','))):
                var.get(u'lex')()
            else:
                if (PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Punctuator')) and PyJsStrictEq(var.get(u'token').get(u'value'),Js(u';'))):
                    var.get(u'lex')()
                    var.get(u'tolerateUnexpectedToken')(var.get(u'token'))
                else:
                    var.get(u'tolerateUnexpectedToken')(var.get(u'token'), var.get(u'Messages').get(u'UnexpectedToken'))
        else:
            var.get(u'expect')(Js(u','))
    PyJsHoisted_expectCommaSeparator_.func_name = u'expectCommaSeparator'
    var.put(u'expectCommaSeparator', PyJsHoisted_expectCommaSeparator_)
    @Js
    def PyJsHoisted_parseParams_(firstRestricted, this, arguments, var=var):
        var = Scope({u'this':this, u'firstRestricted':firstRestricted, u'arguments':arguments}, var)
        var.registers([u'firstRestricted', u'options'])
        pass
        PyJs_Object_146_ = Js({u'params':Js([]),u'defaultCount':Js(0.0),u'defaults':Js([]),u'firstRestricted':var.get(u'firstRestricted')})
        var.put(u'options', PyJs_Object_146_)
        var.get(u'expect')(Js(u'('))
        if var.get(u'match')(Js(u')')).neg():
            PyJs_Object_147_ = Js({})
            var.get(u'options').put(u'paramSet', PyJs_Object_147_)
            while (var.get(u'startIndex')<var.get(u'length')):
                if var.get(u'parseParam')(var.get(u'options')).neg():
                    break
                var.get(u'expect')(Js(u','))
        var.get(u'expect')(Js(u')'))
        if PyJsStrictEq(var.get(u'options').get(u'defaultCount'),Js(0.0)):
            var.get(u'options').put(u'defaults', Js([]))
        PyJs_Object_148_ = Js({u'params':var.get(u'options').get(u'params'),u'defaults':var.get(u'options').get(u'defaults'),u'stricted':var.get(u'options').get(u'stricted'),u'firstRestricted':var.get(u'options').get(u'firstRestricted'),u'message':var.get(u'options').get(u'message')})
        return PyJs_Object_148_
    PyJsHoisted_parseParams_.func_name = u'parseParams'
    var.put(u'parseParams', PyJsHoisted_parseParams_)
    @Js
    def PyJsHoisted_SourceLocation_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        var.get(u"this").put(u'start', var.get(u'Position').create())
        var.get(u"this").put(u'end', var.get(u"null"))
    PyJsHoisted_SourceLocation_.func_name = u'SourceLocation'
    var.put(u'SourceLocation', PyJsHoisted_SourceLocation_)
    @Js
    def PyJsHoisted_parsePrimaryExpression_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'expr', u'token', u'type'])
        pass
        if var.get(u'match')(Js(u'(')):
            var.put(u'isBindingElement', Js(False))
            return var.get(u'inheritCoverGrammar')(var.get(u'parseGroupExpression'))
        if var.get(u'match')(Js(u'[')):
            return var.get(u'inheritCoverGrammar')(var.get(u'parseArrayInitializer'))
        if var.get(u'match')(Js(u'{')):
            return var.get(u'inheritCoverGrammar')(var.get(u'parseObjectInitializer'))
        var.put(u'type', var.get(u'lookahead').get(u'type'))
        var.put(u'node', var.get(u'Node').create())
        if PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'Identifier')):
            if (PyJsStrictEq(var.get(u'state').get(u'sourceType'),Js(u'module')) and PyJsStrictEq(var.get(u'lookahead').get(u'value'),Js(u'await'))):
                var.get(u'tolerateUnexpectedToken')(var.get(u'lookahead'))
            var.put(u'expr', var.get(u'node').callprop(u'finishIdentifier', var.get(u'lex')().get(u'value')))
        else:
            if (PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'StringLiteral')) or PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'NumericLiteral'))):
                var.put(u'isAssignmentTarget', var.put(u'isBindingElement', Js(False)))
                if (var.get(u'strict') and var.get(u'lookahead').get(u'octal')):
                    var.get(u'tolerateUnexpectedToken')(var.get(u'lookahead'), var.get(u'Messages').get(u'StrictOctalLiteral'))
                var.put(u'expr', var.get(u'node').callprop(u'finishLiteral', var.get(u'lex')()))
            else:
                if PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'Keyword')):
                    if ((var.get(u'strict').neg() and var.get(u'state').get(u'allowYield')) and var.get(u'matchKeyword')(Js(u'yield'))):
                        return var.get(u'parseNonComputedProperty')()
                    var.put(u'isAssignmentTarget', var.put(u'isBindingElement', Js(False)))
                    if var.get(u'matchKeyword')(Js(u'function')):
                        return var.get(u'parseFunctionExpression')()
                    if var.get(u'matchKeyword')(Js(u'this')):
                        var.get(u'lex')()
                        return var.get(u'node').callprop(u'finishThisExpression')
                    if var.get(u'matchKeyword')(Js(u'class')):
                        return var.get(u'parseClassExpression')()
                    var.get(u'throwUnexpectedToken')(var.get(u'lex')())
                else:
                    if PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'BooleanLiteral')):
                        var.put(u'isAssignmentTarget', var.put(u'isBindingElement', Js(False)))
                        var.put(u'token', var.get(u'lex')())
                        var.get(u'token').put(u'value', PyJsStrictEq(var.get(u'token').get(u'value'),Js(u'true')))
                        var.put(u'expr', var.get(u'node').callprop(u'finishLiteral', var.get(u'token')))
                    else:
                        if PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'NullLiteral')):
                            var.put(u'isAssignmentTarget', var.put(u'isBindingElement', Js(False)))
                            var.put(u'token', var.get(u'lex')())
                            var.get(u'token').put(u'value', var.get(u"null"))
                            var.put(u'expr', var.get(u'node').callprop(u'finishLiteral', var.get(u'token')))
                        else:
                            if (var.get(u'match')(Js(u'/')) or var.get(u'match')(Js(u'/='))):
                                var.put(u'isAssignmentTarget', var.put(u'isBindingElement', Js(False)))
                                var.put(u'index', var.get(u'startIndex'))
                                if PyJsStrictNeq(var.get(u'extra').get(u'tokens').typeof(),Js(u'undefined')):
                                    var.put(u'token', var.get(u'collectRegex')())
                                else:
                                    var.put(u'token', var.get(u'scanRegExp')())
                                var.get(u'lex')()
                                var.put(u'expr', var.get(u'node').callprop(u'finishLiteral', var.get(u'token')))
                            else:
                                if PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'Template')):
                                    var.put(u'expr', var.get(u'parseTemplateLiteral')())
                                else:
                                    var.get(u'throwUnexpectedToken')(var.get(u'lex')())
        return var.get(u'expr')
    PyJsHoisted_parsePrimaryExpression_.func_name = u'parsePrimaryExpression'
    var.put(u'parsePrimaryExpression', PyJsHoisted_parsePrimaryExpression_)
    @Js
    def PyJsHoisted_scanRegExpFlags_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'restore', u'ch', u'flags', u'str'])
        pass
        var.put(u'str', Js(u''))
        var.put(u'flags', Js(u''))
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').get(var.get(u'index')))
            if var.get(u'isIdentifierPart')(var.get(u'ch').callprop(u'charCodeAt', Js(0.0))).neg():
                break
            var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
            if (PyJsStrictEq(var.get(u'ch'),Js(u'\\')) and (var.get(u'index')<var.get(u'length'))):
                var.put(u'ch', var.get(u'source').get(var.get(u'index')))
                if PyJsStrictEq(var.get(u'ch'),Js(u'u')):
                    var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                    var.put(u'restore', var.get(u'index'))
                    var.put(u'ch', var.get(u'scanHexEscape')(Js(u'u')))
                    if var.get(u'ch'):
                        var.put(u'flags', var.get(u'ch'), u'+')
                        #for JS loop
                        var.put(u'str', Js(u'\\u'), u'+')
                        while (var.get(u'restore')<var.get(u'index')):
                            try:
                                var.put(u'str', var.get(u'source').get(var.get(u'restore')), u'+')
                            finally:
                                    var.put(u'restore',Js(var.get(u'restore').to_number())+Js(1))
                    else:
                        var.put(u'index', var.get(u'restore'))
                        var.put(u'flags', Js(u'u'), u'+')
                        var.put(u'str', Js(u'\\u'), u'+')
                    var.get(u'tolerateUnexpectedToken')()
                else:
                    var.put(u'str', Js(u'\\'), u'+')
                    var.get(u'tolerateUnexpectedToken')()
            else:
                var.put(u'flags', var.get(u'ch'), u'+')
                var.put(u'str', var.get(u'ch'), u'+')
        PyJs_Object_33_ = Js({u'value':var.get(u'flags'),u'literal':var.get(u'str')})
        return PyJs_Object_33_
    PyJsHoisted_scanRegExpFlags_.func_name = u'scanRegExpFlags'
    var.put(u'scanRegExpFlags', PyJsHoisted_scanRegExpFlags_)
    @Js
    def PyJsHoisted_parseImportDeclaration_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'specifiers', u'src'])
        var.put(u'specifiers', Js([]))
        var.put(u'node', var.get(u'Node').create())
        if var.get(u'state').get(u'inFunctionBody'):
            var.get(u'throwError')(var.get(u'Messages').get(u'IllegalImportDeclaration'))
        var.get(u'expectKeyword')(Js(u'import'))
        if PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'StringLiteral')):
            var.put(u'src', var.get(u'parseModuleSpecifier')())
        else:
            if var.get(u'match')(Js(u'{')):
                var.put(u'specifiers', var.get(u'specifiers').callprop(u'concat', var.get(u'parseNamedImports')()))
            else:
                if var.get(u'match')(Js(u'*')):
                    var.get(u'specifiers').callprop(u'push', var.get(u'parseImportNamespaceSpecifier')())
                else:
                    if (var.get(u'isIdentifierName')(var.get(u'lookahead')) and var.get(u'matchKeyword')(Js(u'default')).neg()):
                        var.get(u'specifiers').callprop(u'push', var.get(u'parseImportDefaultSpecifier')())
                        if var.get(u'match')(Js(u',')):
                            var.get(u'lex')()
                            if var.get(u'match')(Js(u'*')):
                                var.get(u'specifiers').callprop(u'push', var.get(u'parseImportNamespaceSpecifier')())
                            else:
                                if var.get(u'match')(Js(u'{')):
                                    var.put(u'specifiers', var.get(u'specifiers').callprop(u'concat', var.get(u'parseNamedImports')()))
                                else:
                                    var.get(u'throwUnexpectedToken')(var.get(u'lookahead'))
                    else:
                        var.get(u'throwUnexpectedToken')(var.get(u'lex')())
            if var.get(u'matchContextualKeyword')(Js(u'from')).neg():
                var.get(u'throwError')((var.get(u'Messages').get(u'UnexpectedToken') if var.get(u'lookahead').get(u'value') else var.get(u'Messages').get(u'MissingFromClause')), var.get(u'lookahead').get(u'value'))
            var.get(u'lex')()
            var.put(u'src', var.get(u'parseModuleSpecifier')())
        var.get(u'consumeSemicolon')()
        return var.get(u'node').callprop(u'finishImportDeclaration', var.get(u'specifiers'), var.get(u'src'))
    PyJsHoisted_parseImportDeclaration_.func_name = u'parseImportDeclaration'
    var.put(u'parseImportDeclaration', PyJsHoisted_parseImportDeclaration_)
    @Js
    def PyJsHoisted_parseVariableDeclarationList_(options, this, arguments, var=var):
        var = Scope({u'this':this, u'options':options, u'arguments':arguments}, var)
        var.registers([u'list', u'options'])
        var.put(u'list', Js([]))
        while 1:
            PyJs_Object_139_ = Js({u'inFor':var.get(u'options').get(u'inFor')})
            var.get(u'list').callprop(u'push', var.get(u'parseVariableDeclaration')(PyJs_Object_139_))
            if var.get(u'match')(Js(u',')).neg():
                break
            var.get(u'lex')()
            if not (var.get(u'startIndex')<var.get(u'length')):
                break
        return var.get(u'list')
    PyJsHoisted_parseVariableDeclarationList_.func_name = u'parseVariableDeclarationList'
    var.put(u'parseVariableDeclarationList', PyJsHoisted_parseVariableDeclarationList_)
    @Js
    def PyJsHoisted_parseFunctionExpression_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'tmp', u'body', u'previousStrict', u'node', u'isGenerator', u'stricted', u'id', u'token', u'params', u'defaults', u'previousAllowYield', u'firstRestricted', u'message'])
        var.put(u'id', var.get(u"null"))
        var.put(u'params', Js([]))
        var.put(u'defaults', Js([]))
        var.put(u'node', var.get(u'Node').create())
        var.put(u'previousAllowYield', var.get(u'state').get(u'allowYield'))
        var.get(u'expectKeyword')(Js(u'function'))
        var.put(u'isGenerator', var.get(u'match')(Js(u'*')))
        if var.get(u'isGenerator'):
            var.get(u'lex')()
        var.get(u'state').put(u'allowYield', var.get(u'isGenerator').neg())
        if var.get(u'match')(Js(u'(')).neg():
            var.put(u'token', var.get(u'lookahead'))
            var.put(u'id', (var.get(u'parseNonComputedProperty')() if ((var.get(u'strict').neg() and var.get(u'isGenerator').neg()) and var.get(u'matchKeyword')(Js(u'yield'))) else var.get(u'parseVariableIdentifier')()))
            if var.get(u'strict'):
                if var.get(u'isRestrictedWord')(var.get(u'token').get(u'value')):
                    var.get(u'tolerateUnexpectedToken')(var.get(u'token'), var.get(u'Messages').get(u'StrictFunctionName'))
            else:
                if var.get(u'isRestrictedWord')(var.get(u'token').get(u'value')):
                    var.put(u'firstRestricted', var.get(u'token'))
                    var.put(u'message', var.get(u'Messages').get(u'StrictFunctionName'))
                else:
                    if var.get(u'isStrictModeReservedWord')(var.get(u'token').get(u'value')):
                        var.put(u'firstRestricted', var.get(u'token'))
                        var.put(u'message', var.get(u'Messages').get(u'StrictReservedWord'))
        var.put(u'tmp', var.get(u'parseParams')(var.get(u'firstRestricted')))
        var.put(u'params', var.get(u'tmp').get(u'params'))
        var.put(u'defaults', var.get(u'tmp').get(u'defaults'))
        var.put(u'stricted', var.get(u'tmp').get(u'stricted'))
        var.put(u'firstRestricted', var.get(u'tmp').get(u'firstRestricted'))
        if var.get(u'tmp').get(u'message'):
            var.put(u'message', var.get(u'tmp').get(u'message'))
        var.put(u'previousStrict', var.get(u'strict'))
        var.put(u'body', var.get(u'parseFunctionSourceElements')())
        if (var.get(u'strict') and var.get(u'firstRestricted')):
            var.get(u'throwUnexpectedToken')(var.get(u'firstRestricted'), var.get(u'message'))
        if (var.get(u'strict') and var.get(u'stricted')):
            var.get(u'tolerateUnexpectedToken')(var.get(u'stricted'), var.get(u'message'))
        var.put(u'strict', var.get(u'previousStrict'))
        var.get(u'state').put(u'allowYield', var.get(u'previousAllowYield'))
        return var.get(u'node').callprop(u'finishFunctionExpression', var.get(u'id'), var.get(u'params'), var.get(u'defaults'), var.get(u'body'), var.get(u'isGenerator'))
    PyJsHoisted_parseFunctionExpression_.func_name = u'parseFunctionExpression'
    var.put(u'parseFunctionExpression', PyJsHoisted_parseFunctionExpression_)
    @Js
    def PyJsHoisted_parseReturnStatement_(node, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'argument'])
        var.put(u'argument', var.get(u"null"))
        var.get(u'expectKeyword')(Js(u'return'))
        if var.get(u'state').get(u'inFunctionBody').neg():
            var.get(u'tolerateError')(var.get(u'Messages').get(u'IllegalReturn'))
        if PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt', var.get(u'lastIndex')),Js(32)):
            if var.get(u'isIdentifierStart')(var.get(u'source').callprop(u'charCodeAt', (var.get(u'lastIndex')+Js(1.0)))):
                var.put(u'argument', var.get(u'parseExpression')())
                var.get(u'consumeSemicolon')()
                return var.get(u'node').callprop(u'finishReturnStatement', var.get(u'argument'))
        if var.get(u'hasLineTerminator'):
            return var.get(u'node').callprop(u'finishReturnStatement', var.get(u"null"))
        if var.get(u'match')(Js(u';')).neg():
            if (var.get(u'match')(Js(u'}')).neg() and PyJsStrictNeq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'EOF'))):
                var.put(u'argument', var.get(u'parseExpression')())
        var.get(u'consumeSemicolon')()
        return var.get(u'node').callprop(u'finishReturnStatement', var.get(u'argument'))
    PyJsHoisted_parseReturnStatement_.func_name = u'parseReturnStatement'
    var.put(u'parseReturnStatement', PyJsHoisted_parseReturnStatement_)
    @Js
    def PyJsHoisted_recordError_(error, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'error':error}, var)
        var.registers([u'error', u'e', u'existing'])
        pass
        #for JS loop
        var.put(u'e', Js(0.0))
        while (var.get(u'e')<var.get(u'extra').get(u'errors').get(u'length')):
            try:
                var.put(u'existing', var.get(u'extra').get(u'errors').get(var.get(u'e')))
                if (PyJsStrictEq(var.get(u'existing').get(u'index'),var.get(u'error').get(u'index')) and PyJsStrictEq(var.get(u'existing').get(u'message'),var.get(u'error').get(u'message'))):
                    return var.get('undefined')
            finally:
                    (var.put(u'e',Js(var.get(u'e').to_number())+Js(1))-Js(1))
        var.get(u'extra').get(u'errors').callprop(u'push', var.get(u'error'))
    PyJsHoisted_recordError_.func_name = u'recordError'
    var.put(u'recordError', PyJsHoisted_recordError_)
    @Js
    def PyJsHoisted_parseExportAllDeclaration_(node, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'src'])
        pass
        var.get(u'expect')(Js(u'*'))
        if var.get(u'matchContextualKeyword')(Js(u'from')).neg():
            var.get(u'throwError')((var.get(u'Messages').get(u'UnexpectedToken') if var.get(u'lookahead').get(u'value') else var.get(u'Messages').get(u'MissingFromClause')), var.get(u'lookahead').get(u'value'))
        var.get(u'lex')()
        var.put(u'src', var.get(u'parseModuleSpecifier')())
        var.get(u'consumeSemicolon')()
        return var.get(u'node').callprop(u'finishExportAllDeclaration', var.get(u'src'))
    PyJsHoisted_parseExportAllDeclaration_.func_name = u'parseExportAllDeclaration'
    var.put(u'parseExportAllDeclaration', PyJsHoisted_parseExportAllDeclaration_)
    @Js
    def PyJsHoisted_collectRegex_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'regex', u'loc', u'token', u'pos'])
        pass
        var.get(u'skipComment')()
        var.put(u'pos', var.get(u'index'))
        PyJs_Object_39_ = Js({u'line':var.get(u'lineNumber'),u'column':(var.get(u'index')-var.get(u'lineStart'))})
        PyJs_Object_38_ = Js({u'start':PyJs_Object_39_})
        var.put(u'loc', PyJs_Object_38_)
        var.put(u'regex', var.get(u'scanRegExp')())
        PyJs_Object_40_ = Js({u'line':var.get(u'lineNumber'),u'column':(var.get(u'index')-var.get(u'lineStart'))})
        var.get(u'loc').put(u'end', PyJs_Object_40_)
        if var.get(u'extra').get(u'tokenize').neg():
            if (var.get(u'extra').get(u'tokens').get(u'length')>Js(0.0)):
                var.put(u'token', var.get(u'extra').get(u'tokens').get((var.get(u'extra').get(u'tokens').get(u'length')-Js(1.0))))
                if (PyJsStrictEq(var.get(u'token').get(u'range').get(u'0'),var.get(u'pos')) and PyJsStrictEq(var.get(u'token').get(u'type'),Js(u'Punctuator'))):
                    if (PyJsStrictEq(var.get(u'token').get(u'value'),Js(u'/')) or PyJsStrictEq(var.get(u'token').get(u'value'),Js(u'/='))):
                        var.get(u'extra').get(u'tokens').callprop(u'pop')
            PyJs_Object_41_ = Js({u'type':Js(u'RegularExpression'),u'value':var.get(u'regex').get(u'literal'),u'regex':var.get(u'regex').get(u'regex'),u'range':Js([var.get(u'pos'), var.get(u'index')]),u'loc':var.get(u'loc')})
            var.get(u'extra').get(u'tokens').callprop(u'push', PyJs_Object_41_)
        return var.get(u'regex')
    PyJsHoisted_collectRegex_.func_name = u'collectRegex'
    var.put(u'collectRegex', PyJsHoisted_collectRegex_)
    @Js
    def PyJsHoisted_expect_(value, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'value':value}, var)
        var.registers([u'token', u'value'])
        var.put(u'token', var.get(u'lex')())
        if (PyJsStrictNeq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Punctuator')) or PyJsStrictNeq(var.get(u'token').get(u'value'),var.get(u'value'))):
            var.get(u'throwUnexpectedToken')(var.get(u'token'))
    PyJsHoisted_expect_.func_name = u'expect'
    var.put(u'expect', PyJsHoisted_expect_)
    @Js
    def PyJsHoisted_skipMultiLineComment_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'comment', u'start', u'ch', u'loc'])
        pass
        if var.get(u'extra').get(u'comments'):
            var.put(u'start', (var.get(u'index')-Js(2.0)))
            PyJs_Object_17_ = Js({u'line':var.get(u'lineNumber'),u'column':((var.get(u'index')-var.get(u'lineStart'))-Js(2.0))})
            PyJs_Object_16_ = Js({u'start':PyJs_Object_17_})
            var.put(u'loc', PyJs_Object_16_)
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').callprop(u'charCodeAt', var.get(u'index')))
            if var.get(u'isLineTerminator')(var.get(u'ch')):
                if (PyJsStrictEq(var.get(u'ch'),Js(13)) and PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt', (var.get(u'index')+Js(1.0))),Js(10))):
                    var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                var.put(u'hasLineTerminator', var.get(u'true'))
                var.put(u'lineNumber',Js(var.get(u'lineNumber').to_number())+Js(1))
                var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                var.put(u'lineStart', var.get(u'index'))
            else:
                if PyJsStrictEq(var.get(u'ch'),Js(42)):
                    if PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt', (var.get(u'index')+Js(1.0))),Js(47)):
                        var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                        var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                        if var.get(u'extra').get(u'comments'):
                            var.put(u'comment', var.get(u'source').callprop(u'slice', (var.get(u'start')+Js(2.0)), (var.get(u'index')-Js(2.0))))
                            PyJs_Object_18_ = Js({u'line':var.get(u'lineNumber'),u'column':(var.get(u'index')-var.get(u'lineStart'))})
                            var.get(u'loc').put(u'end', PyJs_Object_18_)
                            var.get(u'addComment')(Js(u'Block'), var.get(u'comment'), var.get(u'start'), var.get(u'index'), var.get(u'loc'))
                        return var.get('undefined')
                    var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                else:
                    var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
        if var.get(u'extra').get(u'comments'):
            PyJs_Object_19_ = Js({u'line':var.get(u'lineNumber'),u'column':(var.get(u'index')-var.get(u'lineStart'))})
            var.get(u'loc').put(u'end', PyJs_Object_19_)
            var.put(u'comment', var.get(u'source').callprop(u'slice', (var.get(u'start')+Js(2.0)), var.get(u'index')))
            var.get(u'addComment')(Js(u'Block'), var.get(u'comment'), var.get(u'start'), var.get(u'index'), var.get(u'loc'))
        var.get(u'tolerateUnexpectedToken')()
    PyJsHoisted_skipMultiLineComment_.func_name = u'skipMultiLineComment'
    var.put(u'skipMultiLineComment', PyJsHoisted_skipMultiLineComment_)
    @Js
    def PyJsHoisted_scanNumericLiteral_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'start', u'ch', u'number'])
        pass
        var.put(u'ch', var.get(u'source').get(var.get(u'index')))
        var.get(u'assert')((var.get(u'isDecimalDigit')(var.get(u'ch').callprop(u'charCodeAt', Js(0.0))) or PyJsStrictEq(var.get(u'ch'),Js(u'.'))), Js(u'Numeric literal must start with a decimal digit or a decimal point'))
        var.put(u'start', var.get(u'index'))
        var.put(u'number', Js(u''))
        if PyJsStrictNeq(var.get(u'ch'),Js(u'.')):
            var.put(u'number', var.get(u'source').get((var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1))))
            var.put(u'ch', var.get(u'source').get(var.get(u'index')))
            if PyJsStrictEq(var.get(u'number'),Js(u'0')):
                if (PyJsStrictEq(var.get(u'ch'),Js(u'x')) or PyJsStrictEq(var.get(u'ch'),Js(u'X'))):
                    var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                    return var.get(u'scanHexLiteral')(var.get(u'start'))
                if (PyJsStrictEq(var.get(u'ch'),Js(u'b')) or PyJsStrictEq(var.get(u'ch'),Js(u'B'))):
                    var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                    return var.get(u'scanBinaryLiteral')(var.get(u'start'))
                if (PyJsStrictEq(var.get(u'ch'),Js(u'o')) or PyJsStrictEq(var.get(u'ch'),Js(u'O'))):
                    return var.get(u'scanOctalLiteral')(var.get(u'ch'), var.get(u'start'))
                if var.get(u'isOctalDigit')(var.get(u'ch')):
                    if var.get(u'isImplicitOctalLiteral')():
                        return var.get(u'scanOctalLiteral')(var.get(u'ch'), var.get(u'start'))
            while var.get(u'isDecimalDigit')(var.get(u'source').callprop(u'charCodeAt', var.get(u'index'))):
                var.put(u'number', var.get(u'source').get((var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1))), u'+')
            var.put(u'ch', var.get(u'source').get(var.get(u'index')))
        if PyJsStrictEq(var.get(u'ch'),Js(u'.')):
            var.put(u'number', var.get(u'source').get((var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1))), u'+')
            while var.get(u'isDecimalDigit')(var.get(u'source').callprop(u'charCodeAt', var.get(u'index'))):
                var.put(u'number', var.get(u'source').get((var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1))), u'+')
            var.put(u'ch', var.get(u'source').get(var.get(u'index')))
        if (PyJsStrictEq(var.get(u'ch'),Js(u'e')) or PyJsStrictEq(var.get(u'ch'),Js(u'E'))):
            var.put(u'number', var.get(u'source').get((var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1))), u'+')
            var.put(u'ch', var.get(u'source').get(var.get(u'index')))
            if (PyJsStrictEq(var.get(u'ch'),Js(u'+')) or PyJsStrictEq(var.get(u'ch'),Js(u'-'))):
                var.put(u'number', var.get(u'source').get((var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1))), u'+')
            if var.get(u'isDecimalDigit')(var.get(u'source').callprop(u'charCodeAt', var.get(u'index'))):
                while var.get(u'isDecimalDigit')(var.get(u'source').callprop(u'charCodeAt', var.get(u'index'))):
                    var.put(u'number', var.get(u'source').get((var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1))), u'+')
            else:
                var.get(u'throwUnexpectedToken')()
        if var.get(u'isIdentifierStart')(var.get(u'source').callprop(u'charCodeAt', var.get(u'index'))):
            var.get(u'throwUnexpectedToken')()
        PyJs_Object_27_ = Js({u'type':var.get(u'Token').get(u'NumericLiteral'),u'value':var.get(u'parseFloat')(var.get(u'number')),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
        return PyJs_Object_27_
    PyJsHoisted_scanNumericLiteral_.func_name = u'scanNumericLiteral'
    var.put(u'scanNumericLiteral', PyJsHoisted_scanNumericLiteral_)
    @Js
    def PyJsHoisted_isIdentifierStart_(ch, this, arguments, var=var):
        var = Scope({u'this':this, u'ch':ch, u'arguments':arguments}, var)
        var.registers([u'ch'])
        return (((((PyJsStrictEq(var.get(u'ch'),Js(36)) or PyJsStrictEq(var.get(u'ch'),Js(95))) or ((var.get(u'ch')>=Js(65)) and (var.get(u'ch')<=Js(90)))) or ((var.get(u'ch')>=Js(97)) and (var.get(u'ch')<=Js(122)))) or PyJsStrictEq(var.get(u'ch'),Js(92))) or ((var.get(u'ch')>=Js(128)) and var.get(u'Regex').get(u'NonAsciiIdentifierStart').callprop(u'test', var.get(u'fromCodePoint')(var.get(u'ch')))))
    PyJsHoisted_isIdentifierStart_.func_name = u'isIdentifierStart'
    var.put(u'isIdentifierStart', PyJsHoisted_isIdentifierStart_)
    @Js
    def PyJsHoisted_parsePropertyMethodFunction_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'params', u'method', u'previousAllowYield'])
        var.put(u'node', var.get(u'Node').create())
        var.put(u'previousAllowYield', var.get(u'state').get(u'allowYield'))
        var.get(u'state').put(u'allowYield', Js(False))
        var.put(u'params', var.get(u'parseParams')())
        var.get(u'state').put(u'allowYield', var.get(u'previousAllowYield'))
        var.get(u'state').put(u'allowYield', Js(False))
        var.put(u'method', var.get(u'parsePropertyFunction')(var.get(u'node'), var.get(u'params'), Js(False)))
        var.get(u'state').put(u'allowYield', var.get(u'previousAllowYield'))
        return var.get(u'method')
    PyJsHoisted_parsePropertyMethodFunction_.func_name = u'parsePropertyMethodFunction'
    var.put(u'parsePropertyMethodFunction', PyJsHoisted_parsePropertyMethodFunction_)
    @Js
    def PyJsHoisted_parseProgram_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'body', u'node'])
        pass
        var.get(u'peek')()
        var.put(u'node', var.get(u'Node').create())
        var.put(u'body', var.get(u'parseScriptBody')())
        return var.get(u'node').callprop(u'finishProgram', var.get(u'body'), var.get(u'state').get(u'sourceType'))
    PyJsHoisted_parseProgram_.func_name = u'parseProgram'
    var.put(u'parseProgram', PyJsHoisted_parseProgram_)
    @Js
    def PyJsHoisted_isImplicitOctalLiteral_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'i', u'ch'])
        pass
        #for JS loop
        var.put(u'i', (var.get(u'index')+Js(1.0)))
        while (var.get(u'i')<var.get(u'length')):
            try:
                var.put(u'ch', var.get(u'source').get(var.get(u'i')))
                if (PyJsStrictEq(var.get(u'ch'),Js(u'8')) or PyJsStrictEq(var.get(u'ch'),Js(u'9'))):
                    return Js(False)
                if var.get(u'isOctalDigit')(var.get(u'ch')).neg():
                    return var.get(u'true')
            finally:
                    var.put(u'i',Js(var.get(u'i').to_number())+Js(1))
        return var.get(u'true')
    PyJsHoisted_isImplicitOctalLiteral_.func_name = u'isImplicitOctalLiteral'
    var.put(u'isImplicitOctalLiteral', PyJsHoisted_isImplicitOctalLiteral_)
    @Js
    def PyJsHoisted_isOctalDigit_(ch, this, arguments, var=var):
        var = Scope({u'this':this, u'ch':ch, u'arguments':arguments}, var)
        var.registers([u'ch'])
        return (Js(u'01234567').callprop(u'indexOf', var.get(u'ch'))>=Js(0.0))
    PyJsHoisted_isOctalDigit_.func_name = u'isOctalDigit'
    var.put(u'isOctalDigit', PyJsHoisted_isOctalDigit_)
    @Js
    def PyJsHoisted_parseArrayInitializer_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'elements', u'restSpread'])
        var.put(u'elements', Js([]))
        var.put(u'node', var.get(u'Node').create())
        var.get(u'expect')(Js(u'['))
        while var.get(u'match')(Js(u']')).neg():
            if var.get(u'match')(Js(u',')):
                var.get(u'lex')()
                var.get(u'elements').callprop(u'push', var.get(u"null"))
            else:
                if var.get(u'match')(Js(u'...')):
                    var.put(u'restSpread', var.get(u'Node').create())
                    var.get(u'lex')()
                    var.get(u'restSpread').callprop(u'finishSpreadElement', var.get(u'inheritCoverGrammar')(var.get(u'parseAssignmentExpression')))
                    if var.get(u'match')(Js(u']')).neg():
                        var.put(u'isAssignmentTarget', var.put(u'isBindingElement', Js(False)))
                        var.get(u'expect')(Js(u','))
                    var.get(u'elements').callprop(u'push', var.get(u'restSpread'))
                else:
                    var.get(u'elements').callprop(u'push', var.get(u'inheritCoverGrammar')(var.get(u'parseAssignmentExpression')))
                    if var.get(u'match')(Js(u']')).neg():
                        var.get(u'expect')(Js(u','))
        var.get(u'lex')()
        return var.get(u'node').callprop(u'finishArrayExpression', var.get(u'elements'))
    PyJsHoisted_parseArrayInitializer_.func_name = u'parseArrayInitializer'
    var.put(u'parseArrayInitializer', PyJsHoisted_parseArrayInitializer_)
    @Js
    def PyJsHoisted_isDecimalDigit_(ch, this, arguments, var=var):
        var = Scope({u'this':this, u'ch':ch, u'arguments':arguments}, var)
        var.registers([u'ch'])
        return ((var.get(u'ch')>=Js(48)) and (var.get(u'ch')<=Js(57)))
    PyJsHoisted_isDecimalDigit_.func_name = u'isDecimalDigit'
    var.put(u'isDecimalDigit', PyJsHoisted_isDecimalDigit_)
    @Js
    def PyJsHoisted_parseClassExpression_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'classNode', u'previousStrict', u'classBody', u'id', u'superClass'])
        var.put(u'id', var.get(u"null"))
        var.put(u'superClass', var.get(u"null"))
        var.put(u'classNode', var.get(u'Node').create())
        var.put(u'previousStrict', var.get(u'strict'))
        var.put(u'strict', var.get(u'true'))
        var.get(u'expectKeyword')(Js(u'class'))
        if PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Identifier')):
            var.put(u'id', var.get(u'parseVariableIdentifier')())
        if var.get(u'matchKeyword')(Js(u'extends')):
            var.get(u'lex')()
            var.put(u'superClass', var.get(u'isolateCoverGrammar')(var.get(u'parseLeftHandSideExpressionAllowCall')))
        var.put(u'classBody', var.get(u'parseClassBody')())
        var.put(u'strict', var.get(u'previousStrict'))
        return var.get(u'classNode').callprop(u'finishClassExpression', var.get(u'id'), var.get(u'superClass'), var.get(u'classBody'))
    PyJsHoisted_parseClassExpression_.func_name = u'parseClassExpression'
    var.put(u'parseClassExpression', PyJsHoisted_parseClassExpression_)
    @Js
    def PyJsHoisted_parseObjectProperty_(hasProto, this, arguments, var=var):
        var = Scope({u'this':this, u'hasProto':hasProto, u'arguments':arguments}, var)
        var.registers([u'node', u'hasProto', u'computed', u'proto', u'value', u'token', u'maybeMethod', u'key'])
        var.put(u'token', var.get(u'lookahead'))
        var.put(u'node', var.get(u'Node').create())
        var.put(u'computed', var.get(u'match')(Js(u'[')))
        if var.get(u'match')(Js(u'*')):
            var.get(u'lex')()
        else:
            var.put(u'key', var.get(u'parseObjectPropertyKey')())
        var.put(u'maybeMethod', var.get(u'tryParseMethodDefinition')(var.get(u'token'), var.get(u'key'), var.get(u'computed'), var.get(u'node')))
        if var.get(u'maybeMethod'):
            return var.get(u'maybeMethod')
        if var.get(u'key').neg():
            var.get(u'throwUnexpectedToken')(var.get(u'lookahead'))
        if var.get(u'computed').neg():
            var.put(u'proto', ((PyJsStrictEq(var.get(u'key').get(u'type'),var.get(u'Syntax').get(u'Identifier')) and PyJsStrictEq(var.get(u'key').get(u'name'),Js(u'__proto__'))) or (PyJsStrictEq(var.get(u'key').get(u'type'),var.get(u'Syntax').get(u'Literal')) and PyJsStrictEq(var.get(u'key').get(u'value'),Js(u'__proto__')))))
            if (var.get(u'hasProto').get(u'value') and var.get(u'proto')):
                var.get(u'tolerateError')(var.get(u'Messages').get(u'DuplicateProtoProperty'))
            var.get(u'hasProto').put(u'value', var.get(u'proto'), u'|')
        if var.get(u'match')(Js(u':')):
            var.get(u'lex')()
            var.put(u'value', var.get(u'inheritCoverGrammar')(var.get(u'parseAssignmentExpression')))
            return var.get(u'node').callprop(u'finishProperty', Js(u'init'), var.get(u'key'), var.get(u'computed'), var.get(u'value'), Js(False), Js(False))
        if PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Identifier')):
            if var.get(u'match')(Js(u'=')):
                var.put(u'firstCoverInitializedNameError', var.get(u'lookahead'))
                var.get(u'lex')()
                var.put(u'value', var.get(u'isolateCoverGrammar')(var.get(u'parseAssignmentExpression')))
                return var.get(u'node').callprop(u'finishProperty', Js(u'init'), var.get(u'key'), var.get(u'computed'), var.get(u'WrappingNode').create(var.get(u'token')).callprop(u'finishAssignmentPattern', var.get(u'key'), var.get(u'value')), Js(False), var.get(u'true'))
            return var.get(u'node').callprop(u'finishProperty', Js(u'init'), var.get(u'key'), var.get(u'computed'), var.get(u'key'), Js(False), var.get(u'true'))
        var.get(u'throwUnexpectedToken')(var.get(u'lookahead'))
    PyJsHoisted_parseObjectProperty_.func_name = u'parseObjectProperty'
    var.put(u'parseObjectProperty', PyJsHoisted_parseObjectProperty_)
    @Js
    def PyJsHoisted_parseCatchClause_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'body', u'node', u'i', u'param', u'params', u'key', u'paramMap'])
        var.put(u'params', Js([]))
        PyJs_Object_144_ = Js({})
        var.put(u'paramMap', PyJs_Object_144_)
        var.put(u'node', var.get(u'Node').create())
        var.get(u'expectKeyword')(Js(u'catch'))
        var.get(u'expect')(Js(u'('))
        if var.get(u'match')(Js(u')')):
            var.get(u'throwUnexpectedToken')(var.get(u'lookahead'))
        var.put(u'param', var.get(u'parsePattern')(var.get(u'params')))
        #for JS loop
        var.put(u'i', Js(0.0))
        while (var.get(u'i')<var.get(u'params').get(u'length')):
            try:
                var.put(u'key', (Js(u'$')+var.get(u'params').get(var.get(u'i')).get(u'value')))
                if var.get(u'Object').get(u'prototype').get(u'hasOwnProperty').callprop(u'call', var.get(u'paramMap'), var.get(u'key')):
                    var.get(u'tolerateError')(var.get(u'Messages').get(u'DuplicateBinding'), var.get(u'params').get(var.get(u'i')).get(u'value'))
                var.get(u'paramMap').put(var.get(u'key'), var.get(u'true'))
            finally:
                    (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
        if (var.get(u'strict') and var.get(u'isRestrictedWord')(var.get(u'param').get(u'name'))):
            var.get(u'tolerateError')(var.get(u'Messages').get(u'StrictCatchVariable'))
        var.get(u'expect')(Js(u')'))
        var.put(u'body', var.get(u'parseBlock')())
        return var.get(u'node').callprop(u'finishCatchClause', var.get(u'param'), var.get(u'body'))
    PyJsHoisted_parseCatchClause_.func_name = u'parseCatchClause'
    var.put(u'parseCatchClause', PyJsHoisted_parseCatchClause_)
    @Js
    def PyJsHoisted_peek_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        var.put(u'scanning', var.get(u'true'))
        var.get(u'skipComment')()
        var.put(u'lastIndex', var.get(u'index'))
        var.put(u'lastLineNumber', var.get(u'lineNumber'))
        var.put(u'lastLineStart', var.get(u'lineStart'))
        var.put(u'startIndex', var.get(u'index'))
        var.put(u'startLineNumber', var.get(u'lineNumber'))
        var.put(u'startLineStart', var.get(u'lineStart'))
        var.put(u'lookahead', (var.get(u'collectToken')() if PyJsStrictNeq(var.get(u'extra').get(u'tokens').typeof(),Js(u'undefined')) else var.get(u'advance')()))
        var.put(u'scanning', Js(False))
    PyJsHoisted_peek_.func_name = u'peek'
    var.put(u'peek', PyJsHoisted_peek_)
    @Js
    def PyJsHoisted_parseArguments_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'expr', u'args'])
        var.put(u'args', Js([]))
        var.get(u'expect')(Js(u'('))
        if var.get(u'match')(Js(u')')).neg():
            while (var.get(u'startIndex')<var.get(u'length')):
                if var.get(u'match')(Js(u'...')):
                    var.put(u'expr', var.get(u'Node').create())
                    var.get(u'lex')()
                    var.get(u'expr').callprop(u'finishSpreadElement', var.get(u'isolateCoverGrammar')(var.get(u'parseAssignmentExpression')))
                else:
                    var.put(u'expr', var.get(u'isolateCoverGrammar')(var.get(u'parseAssignmentExpression')))
                var.get(u'args').callprop(u'push', var.get(u'expr'))
                if var.get(u'match')(Js(u')')):
                    break
                var.get(u'expectCommaSeparator')()
        var.get(u'expect')(Js(u')'))
        return var.get(u'args')
    PyJsHoisted_parseArguments_.func_name = u'parseArguments'
    var.put(u'parseArguments', PyJsHoisted_parseArguments_)
    @Js
    def PyJsHoisted_testRegExp_(pattern, flags, this, arguments, var=var):
        var = Scope({u'this':this, u'pattern':pattern, u'flags':flags, u'arguments':arguments}, var)
        var.registers([u'tmp', u'pattern', u'flags', u'astralSubstitute'])
        var.put(u'astralSubstitute', Js(u'\uffff'))
        var.put(u'tmp', var.get(u'pattern'))
        if (var.get(u'flags').callprop(u'indexOf', Js(u'u'))>=Js(0.0)):
            @Js
            def PyJs_anonymous_31_(PyJsArg_2430_, PyJsArg_2431_, PyJsArg_2432_, this, arguments, var=var):
                var = Scope({u'this':this, u'$2':PyJsArg_2432_, u'arguments':arguments, u'$0':PyJsArg_2430_, u'$1':PyJsArg_2431_}, var)
                var.registers([u'codePoint', u'$2', u'$0', u'$1'])
                var.put(u'codePoint', var.get(u'parseInt')((var.get(u'$1') or var.get(u'$2')), Js(16.0)))
                if (var.get(u'codePoint')>Js(1114111)):
                    var.get(u'throwUnexpectedToken')(var.get(u"null"), var.get(u'Messages').get(u'InvalidRegExp'))
                if (var.get(u'codePoint')<=Js(65535)):
                    return var.get(u'String').callprop(u'fromCharCode', var.get(u'codePoint'))
                return var.get(u'astralSubstitute')
            PyJs_anonymous_31_._set_name(u'anonymous')
            var.put(u'tmp', var.get(u'tmp').callprop(u'replace', JsRegExp(u'/\\\\u\\{([0-9a-fA-F]+)\\}|\\\\u([a-fA-F0-9]{4})/g'), PyJs_anonymous_31_).callprop(u'replace', JsRegExp(u'/[\\uD800-\\uDBFF][\\uDC00-\\uDFFF]/g'), var.get(u'astralSubstitute')))
        try:
            var.get(u'RegExp')(var.get(u'tmp'))
        except PyJsException as PyJsTempException:
            PyJsHolder_65_65374668 = var.own.get(u'e')
            var.force_own_put(u'e', PyExceptionToJs(PyJsTempException))
            try:
                var.get(u'throwUnexpectedToken')(var.get(u"null"), var.get(u'Messages').get(u'InvalidRegExp'))
            finally:
                if PyJsHolder_65_65374668 is not None:
                    var.own[u'e'] = PyJsHolder_65_65374668
                else:
                    del var.own[u'e']
                del PyJsHolder_65_65374668
        try:
            return var.get(u'RegExp').create(var.get(u'pattern'), var.get(u'flags'))
        except PyJsException as PyJsTempException:
            PyJsHolder_657863657074696f6e_9604751 = var.own.get(u'exception')
            var.force_own_put(u'exception', PyExceptionToJs(PyJsTempException))
            try:
                return var.get(u"null")
            finally:
                if PyJsHolder_657863657074696f6e_9604751 is not None:
                    var.own[u'exception'] = PyJsHolder_657863657074696f6e_9604751
                else:
                    del var.own[u'exception']
                del PyJsHolder_657863657074696f6e_9604751
    PyJsHoisted_testRegExp_.func_name = u'testRegExp'
    var.put(u'testRegExp', PyJsHoisted_testRegExp_)
    @Js
    def PyJsHoisted_octalToDecimal_(ch, this, arguments, var=var):
        var = Scope({u'this':this, u'ch':ch, u'arguments':arguments}, var)
        var.registers([u'octal', u'ch', u'code'])
        var.put(u'octal', PyJsStrictNeq(var.get(u'ch'),Js(u'0')))
        var.put(u'code', Js(u'01234567').callprop(u'indexOf', var.get(u'ch')))
        if ((var.get(u'index')<var.get(u'length')) and var.get(u'isOctalDigit')(var.get(u'source').get(var.get(u'index')))):
            var.put(u'octal', var.get(u'true'))
            var.put(u'code', ((var.get(u'code')*Js(8.0))+Js(u'01234567').callprop(u'indexOf', var.get(u'source').get((var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1))))))
            if (((Js(u'0123').callprop(u'indexOf', var.get(u'ch'))>=Js(0.0)) and (var.get(u'index')<var.get(u'length'))) and var.get(u'isOctalDigit')(var.get(u'source').get(var.get(u'index')))):
                var.put(u'code', ((var.get(u'code')*Js(8.0))+Js(u'01234567').callprop(u'indexOf', var.get(u'source').get((var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1))))))
        PyJs_Object_8_ = Js({u'code':var.get(u'code'),u'octal':var.get(u'octal')})
        return PyJs_Object_8_
    PyJsHoisted_octalToDecimal_.func_name = u'octalToDecimal'
    var.put(u'octalToDecimal', PyJsHoisted_octalToDecimal_)
    @Js
    def PyJsHoisted_parseExportDeclaration_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node'])
        var.put(u'node', var.get(u'Node').create())
        if var.get(u'state').get(u'inFunctionBody'):
            var.get(u'throwError')(var.get(u'Messages').get(u'IllegalExportDeclaration'))
        var.get(u'expectKeyword')(Js(u'export'))
        if var.get(u'matchKeyword')(Js(u'default')):
            return var.get(u'parseExportDefaultDeclaration')(var.get(u'node'))
        if var.get(u'match')(Js(u'*')):
            return var.get(u'parseExportAllDeclaration')(var.get(u'node'))
        return var.get(u'parseExportNamedDeclaration')(var.get(u'node'))
    PyJsHoisted_parseExportDeclaration_.func_name = u'parseExportDeclaration'
    var.put(u'parseExportDeclaration', PyJsHoisted_parseExportDeclaration_)
    @Js
    def PyJsHoisted_parseStatement_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'expr', u'type', u'key', u'labeledBody'])
        var.put(u'type', var.get(u'lookahead').get(u'type'))
        if PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'EOF')):
            var.get(u'throwUnexpectedToken')(var.get(u'lookahead'))
        if (PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'Punctuator')) and PyJsStrictEq(var.get(u'lookahead').get(u'value'),Js(u'{'))):
            return var.get(u'parseBlock')()
        var.put(u'isAssignmentTarget', var.put(u'isBindingElement', var.get(u'true')))
        var.put(u'node', var.get(u'Node').create())
        if PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'Punctuator')):
            while 1:
                SWITCHED = False
                CONDITION = (var.get(u'lookahead').get(u'value'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u';')):
                    SWITCHED = True
                    return var.get(u'parseEmptyStatement')(var.get(u'node'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'(')):
                    SWITCHED = True
                    return var.get(u'parseExpressionStatement')(var.get(u'node'))
                if True:
                    SWITCHED = True
                    break
                SWITCHED = True
                break
        else:
            if PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'Keyword')):
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get(u'lookahead').get(u'value'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(u'break')):
                        SWITCHED = True
                        return var.get(u'parseBreakStatement')(var.get(u'node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(u'continue')):
                        SWITCHED = True
                        return var.get(u'parseContinueStatement')(var.get(u'node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(u'debugger')):
                        SWITCHED = True
                        return var.get(u'parseDebuggerStatement')(var.get(u'node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(u'do')):
                        SWITCHED = True
                        return var.get(u'parseDoWhileStatement')(var.get(u'node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(u'for')):
                        SWITCHED = True
                        return var.get(u'parseForStatement')(var.get(u'node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(u'function')):
                        SWITCHED = True
                        return var.get(u'parseFunctionDeclaration')(var.get(u'node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(u'if')):
                        SWITCHED = True
                        return var.get(u'parseIfStatement')(var.get(u'node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(u'return')):
                        SWITCHED = True
                        return var.get(u'parseReturnStatement')(var.get(u'node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(u'switch')):
                        SWITCHED = True
                        return var.get(u'parseSwitchStatement')(var.get(u'node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(u'throw')):
                        SWITCHED = True
                        return var.get(u'parseThrowStatement')(var.get(u'node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(u'try')):
                        SWITCHED = True
                        return var.get(u'parseTryStatement')(var.get(u'node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(u'var')):
                        SWITCHED = True
                        return var.get(u'parseVariableStatement')(var.get(u'node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(u'while')):
                        SWITCHED = True
                        return var.get(u'parseWhileStatement')(var.get(u'node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(u'with')):
                        SWITCHED = True
                        return var.get(u'parseWithStatement')(var.get(u'node'))
                    if True:
                        SWITCHED = True
                        break
                    SWITCHED = True
                    break
        var.put(u'expr', var.get(u'parseExpression')())
        if (PyJsStrictEq(var.get(u'expr').get(u'type'),var.get(u'Syntax').get(u'Identifier')) and var.get(u'match')(Js(u':'))):
            var.get(u'lex')()
            var.put(u'key', (Js(u'$')+var.get(u'expr').get(u'name')))
            if var.get(u'Object').get(u'prototype').get(u'hasOwnProperty').callprop(u'call', var.get(u'state').get(u'labelSet'), var.get(u'key')):
                var.get(u'throwError')(var.get(u'Messages').get(u'Redeclaration'), Js(u'Label'), var.get(u'expr').get(u'name'))
            var.get(u'state').get(u'labelSet').put(var.get(u'key'), var.get(u'true'))
            var.put(u'labeledBody', var.get(u'parseStatement')())
            var.get(u'state').get(u'labelSet').delete(var.get(u'key'))
            return var.get(u'node').callprop(u'finishLabeledStatement', var.get(u'expr'), var.get(u'labeledBody'))
        var.get(u'consumeSemicolon')()
        return var.get(u'node').callprop(u'finishExpressionStatement', var.get(u'expr'))
    PyJsHoisted_parseStatement_.func_name = u'parseStatement'
    var.put(u'parseStatement', PyJsHoisted_parseStatement_)
    @Js
    def PyJsHoisted_isLineTerminator_(ch, this, arguments, var=var):
        var = Scope({u'this':this, u'ch':ch, u'arguments':arguments}, var)
        var.registers([u'ch'])
        return (((PyJsStrictEq(var.get(u'ch'),Js(10)) or PyJsStrictEq(var.get(u'ch'),Js(13))) or PyJsStrictEq(var.get(u'ch'),Js(8232))) or PyJsStrictEq(var.get(u'ch'),Js(8233)))
    PyJsHoisted_isLineTerminator_.func_name = u'isLineTerminator'
    var.put(u'isLineTerminator', PyJsHoisted_isLineTerminator_)
    @Js
    def PyJsHoisted_parseStatementList_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'list'])
        var.put(u'list', Js([]))
        while (var.get(u'startIndex')<var.get(u'length')):
            if var.get(u'match')(Js(u'}')):
                break
            var.get(u'list').callprop(u'push', var.get(u'parseStatementListItem')())
        return var.get(u'list')
    PyJsHoisted_parseStatementList_.func_name = u'parseStatementList'
    var.put(u'parseStatementList', PyJsHoisted_parseStatementList_)
    @Js
    def PyJsHoisted_parseNamedImports_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'specifiers'])
        var.put(u'specifiers', Js([]))
        var.get(u'expect')(Js(u'{'))
        while var.get(u'match')(Js(u'}')).neg():
            var.get(u'specifiers').callprop(u'push', var.get(u'parseImportSpecifier')())
            if var.get(u'match')(Js(u'}')).neg():
                var.get(u'expect')(Js(u','))
                if var.get(u'match')(Js(u'}')):
                    break
        var.get(u'expect')(Js(u'}'))
        return var.get(u'specifiers')
    PyJsHoisted_parseNamedImports_.func_name = u'parseNamedImports'
    var.put(u'parseNamedImports', PyJsHoisted_parseNamedImports_)
    @Js
    def PyJsHoisted_lex_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'token'])
        pass
        var.put(u'scanning', var.get(u'true'))
        var.put(u'lastIndex', var.get(u'index'))
        var.put(u'lastLineNumber', var.get(u'lineNumber'))
        var.put(u'lastLineStart', var.get(u'lineStart'))
        var.get(u'skipComment')()
        var.put(u'token', var.get(u'lookahead'))
        var.put(u'startIndex', var.get(u'index'))
        var.put(u'startLineNumber', var.get(u'lineNumber'))
        var.put(u'startLineStart', var.get(u'lineStart'))
        var.put(u'lookahead', (var.get(u'collectToken')() if PyJsStrictNeq(var.get(u'extra').get(u'tokens').typeof(),Js(u'undefined')) else var.get(u'advance')()))
        var.put(u'scanning', Js(False))
        return var.get(u'token')
    PyJsHoisted_lex_.func_name = u'lex'
    var.put(u'lex', PyJsHoisted_lex_)
    @Js
    def PyJsHoisted_parseFunctionSourceElements_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'body', u'oldInIteration', u'oldInFunctionBody', u'node', u'directive', u'oldInSwitch', u'oldLabelSet', u'token', u'statement', u'firstRestricted', u'oldParenthesisCount'])
        var.put(u'body', Js([]))
        var.put(u'node', var.get(u'Node').create())
        var.get(u'expect')(Js(u'{'))
        while (var.get(u'startIndex')<var.get(u'length')):
            if PyJsStrictNeq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'StringLiteral')):
                break
            var.put(u'token', var.get(u'lookahead'))
            var.put(u'statement', var.get(u'parseStatementListItem')())
            var.get(u'body').callprop(u'push', var.get(u'statement'))
            if PyJsStrictNeq(var.get(u'statement').get(u'expression').get(u'type'),var.get(u'Syntax').get(u'Literal')):
                break
            var.put(u'directive', var.get(u'source').callprop(u'slice', (var.get(u'token').get(u'start')+Js(1.0)), (var.get(u'token').get(u'end')-Js(1.0))))
            if PyJsStrictEq(var.get(u'directive'),Js(u'use strict')):
                var.put(u'strict', var.get(u'true'))
                if var.get(u'firstRestricted'):
                    var.get(u'tolerateUnexpectedToken')(var.get(u'firstRestricted'), var.get(u'Messages').get(u'StrictOctalLiteral'))
            else:
                if (var.get(u'firstRestricted').neg() and var.get(u'token').get(u'octal')):
                    var.put(u'firstRestricted', var.get(u'token'))
        var.put(u'oldLabelSet', var.get(u'state').get(u'labelSet'))
        var.put(u'oldInIteration', var.get(u'state').get(u'inIteration'))
        var.put(u'oldInSwitch', var.get(u'state').get(u'inSwitch'))
        var.put(u'oldInFunctionBody', var.get(u'state').get(u'inFunctionBody'))
        var.put(u'oldParenthesisCount', var.get(u'state').get(u'parenthesizedCount'))
        PyJs_Object_145_ = Js({})
        var.get(u'state').put(u'labelSet', PyJs_Object_145_)
        var.get(u'state').put(u'inIteration', Js(False))
        var.get(u'state').put(u'inSwitch', Js(False))
        var.get(u'state').put(u'inFunctionBody', var.get(u'true'))
        var.get(u'state').put(u'parenthesizedCount', Js(0.0))
        while (var.get(u'startIndex')<var.get(u'length')):
            if var.get(u'match')(Js(u'}')):
                break
            var.get(u'body').callprop(u'push', var.get(u'parseStatementListItem')())
        var.get(u'expect')(Js(u'}'))
        var.get(u'state').put(u'labelSet', var.get(u'oldLabelSet'))
        var.get(u'state').put(u'inIteration', var.get(u'oldInIteration'))
        var.get(u'state').put(u'inSwitch', var.get(u'oldInSwitch'))
        var.get(u'state').put(u'inFunctionBody', var.get(u'oldInFunctionBody'))
        var.get(u'state').put(u'parenthesizedCount', var.get(u'oldParenthesisCount'))
        return var.get(u'node').callprop(u'finishBlockStatement', var.get(u'body'))
    PyJsHoisted_parseFunctionSourceElements_.func_name = u'parseFunctionSourceElements'
    var.put(u'parseFunctionSourceElements', PyJsHoisted_parseFunctionSourceElements_)
    @Js
    def PyJsHoisted_isIdentifierName_(token, this, arguments, var=var):
        var = Scope({u'this':this, u'token':token, u'arguments':arguments}, var)
        var.registers([u'token'])
        return (((PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Identifier')) or PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Keyword'))) or PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'BooleanLiteral'))) or PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'NullLiteral')))
    PyJsHoisted_isIdentifierName_.func_name = u'isIdentifierName'
    var.put(u'isIdentifierName', PyJsHoisted_isIdentifierName_)
    @Js
    def PyJsHoisted_advance_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'token', u'cp'])
        pass
        if (var.get(u'index')>=var.get(u'length')):
            PyJs_Object_42_ = Js({u'type':var.get(u'Token').get(u'EOF'),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'index'),u'end':var.get(u'index')})
            return PyJs_Object_42_
        var.put(u'cp', var.get(u'source').callprop(u'charCodeAt', var.get(u'index')))
        if var.get(u'isIdentifierStart')(var.get(u'cp')):
            var.put(u'token', var.get(u'scanIdentifier')())
            if (var.get(u'strict') and var.get(u'isStrictModeReservedWord')(var.get(u'token').get(u'value'))):
                var.get(u'token').put(u'type', var.get(u'Token').get(u'Keyword'))
            return var.get(u'token')
        if ((PyJsStrictEq(var.get(u'cp'),Js(40)) or PyJsStrictEq(var.get(u'cp'),Js(41))) or PyJsStrictEq(var.get(u'cp'),Js(59))):
            return var.get(u'scanPunctuator')()
        if (PyJsStrictEq(var.get(u'cp'),Js(39)) or PyJsStrictEq(var.get(u'cp'),Js(34))):
            return var.get(u'scanStringLiteral')()
        if PyJsStrictEq(var.get(u'cp'),Js(46)):
            if var.get(u'isDecimalDigit')(var.get(u'source').callprop(u'charCodeAt', (var.get(u'index')+Js(1.0)))):
                return var.get(u'scanNumericLiteral')()
            return var.get(u'scanPunctuator')()
        if var.get(u'isDecimalDigit')(var.get(u'cp')):
            return var.get(u'scanNumericLiteral')()
        if (var.get(u'extra').get(u'tokenize') and PyJsStrictEq(var.get(u'cp'),Js(47))):
            return var.get(u'advanceSlash')()
        if (PyJsStrictEq(var.get(u'cp'),Js(96)) or (PyJsStrictEq(var.get(u'cp'),Js(125)) and PyJsStrictEq(var.get(u'state').get(u'curlyStack').get((var.get(u'state').get(u'curlyStack').get(u'length')-Js(1.0))),Js(u'${')))):
            return var.get(u'scanTemplate')()
        if ((var.get(u'cp')>=Js(55296)) and (var.get(u'cp')<Js(57343))):
            var.put(u'cp', var.get(u'codePointAt')(var.get(u'index')))
            if var.get(u'isIdentifierStart')(var.get(u'cp')):
                return var.get(u'scanIdentifier')()
        return var.get(u'scanPunctuator')()
    PyJsHoisted_advance_.func_name = u'advance'
    var.put(u'advance', PyJsHoisted_advance_)
    @Js
    def PyJsHoisted_inheritCoverGrammar_(parser, this, arguments, var=var):
        var = Scope({u'this':this, u'parser':parser, u'arguments':arguments}, var)
        var.registers([u'oldFirstCoverInitializedNameError', u'parser', u'oldIsBindingElement', u'oldIsAssignmentTarget', u'result'])
        var.put(u'oldIsBindingElement', var.get(u'isBindingElement'))
        var.put(u'oldIsAssignmentTarget', var.get(u'isAssignmentTarget'))
        var.put(u'oldFirstCoverInitializedNameError', var.get(u'firstCoverInitializedNameError'))
        var.put(u'isBindingElement', var.get(u'true'))
        var.put(u'isAssignmentTarget', var.get(u'true'))
        var.put(u'firstCoverInitializedNameError', var.get(u"null"))
        var.put(u'result', var.get(u'parser')())
        var.put(u'isBindingElement', (var.get(u'isBindingElement') and var.get(u'oldIsBindingElement')))
        var.put(u'isAssignmentTarget', (var.get(u'isAssignmentTarget') and var.get(u'oldIsAssignmentTarget')))
        var.put(u'firstCoverInitializedNameError', (var.get(u'oldFirstCoverInitializedNameError') or var.get(u'firstCoverInitializedNameError')))
        return var.get(u'result')
    PyJsHoisted_inheritCoverGrammar_.func_name = u'inheritCoverGrammar'
    var.put(u'inheritCoverGrammar', PyJsHoisted_inheritCoverGrammar_)
    @Js
    def PyJsHoisted_reinterpretAsCoverFormalsList_(expr, this, arguments, var=var):
        var = Scope({u'this':this, u'expr':expr, u'arguments':arguments}, var)
        var.registers([u'i', u'expr', u'param', u'token', u'params', u'len', u'defaults', u'defaultCount', u'options'])
        pass
        var.put(u'defaults', Js([]))
        var.put(u'defaultCount', Js(0.0))
        var.put(u'params', Js([var.get(u'expr')]))
        while 1:
            SWITCHED = False
            CONDITION = (var.get(u'expr').get(u'type'))
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Syntax').get(u'Identifier')):
                SWITCHED = True
                break
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'PlaceHolders').get(u'ArrowParameterPlaceHolder')):
                SWITCHED = True
                var.put(u'params', var.get(u'expr').get(u'params'))
                break
            if True:
                SWITCHED = True
                return var.get(u"null")
            SWITCHED = True
            break
        PyJs_Object_136_ = Js({})
        PyJs_Object_135_ = Js({u'paramSet':PyJs_Object_136_})
        var.put(u'options', PyJs_Object_135_)
        #for JS loop
        PyJsComma(var.put(u'i', Js(0.0)),var.put(u'len', var.get(u'params').get(u'length')))
        while (var.get(u'i')<var.get(u'len')):
            try:
                var.put(u'param', var.get(u'params').get(var.get(u'i')))
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get(u'param').get(u'type'))
                    if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Syntax').get(u'AssignmentPattern')):
                        SWITCHED = True
                        var.get(u'params').put(var.get(u'i'), var.get(u'param').get(u'left'))
                        if PyJsStrictEq(var.get(u'param').get(u'right').get(u'type'),var.get(u'Syntax').get(u'YieldExpression')):
                            if var.get(u'param').get(u'right').get(u'argument'):
                                var.get(u'throwUnexpectedToken')(var.get(u'lookahead'))
                            var.get(u'param').get(u'right').put(u'type', var.get(u'Syntax').get(u'Identifier'))
                            var.get(u'param').get(u'right').put(u'name', Js(u'yield'))
                            var.get(u'param').get(u'right').delete(u'argument')
                            var.get(u'param').get(u'right').delete(u'delegate')
                        var.get(u'defaults').callprop(u'push', var.get(u'param').get(u'right'))
                        var.put(u'defaultCount',Js(var.get(u'defaultCount').to_number())+Js(1))
                        var.get(u'checkPatternParam')(var.get(u'options'), var.get(u'param').get(u'left'))
                        break
                    if True:
                        SWITCHED = True
                        var.get(u'checkPatternParam')(var.get(u'options'), var.get(u'param'))
                        var.get(u'params').put(var.get(u'i'), var.get(u'param'))
                        var.get(u'defaults').callprop(u'push', var.get(u"null"))
                        break
                    SWITCHED = True
                    break
            finally:
                    var.put(u'i', Js(1.0), u'+')
        if (var.get(u'strict') or var.get(u'state').get(u'allowYield').neg()):
            #for JS loop
            PyJsComma(var.put(u'i', Js(0.0)),var.put(u'len', var.get(u'params').get(u'length')))
            while (var.get(u'i')<var.get(u'len')):
                try:
                    var.put(u'param', var.get(u'params').get(var.get(u'i')))
                    if PyJsStrictEq(var.get(u'param').get(u'type'),var.get(u'Syntax').get(u'YieldExpression')):
                        var.get(u'throwUnexpectedToken')(var.get(u'lookahead'))
                finally:
                        var.put(u'i', Js(1.0), u'+')
        if PyJsStrictEq(var.get(u'options').get(u'message'),var.get(u'Messages').get(u'StrictParamDupe')):
            var.put(u'token', (var.get(u'options').get(u'stricted') if var.get(u'strict') else var.get(u'options').get(u'firstRestricted')))
            var.get(u'throwUnexpectedToken')(var.get(u'token'), var.get(u'options').get(u'message'))
        if PyJsStrictEq(var.get(u'defaultCount'),Js(0.0)):
            var.put(u'defaults', Js([]))
        PyJs_Object_137_ = Js({u'params':var.get(u'params'),u'defaults':var.get(u'defaults'),u'stricted':var.get(u'options').get(u'stricted'),u'firstRestricted':var.get(u'options').get(u'firstRestricted'),u'message':var.get(u'options').get(u'message')})
        return PyJs_Object_137_
    PyJsHoisted_reinterpretAsCoverFormalsList_.func_name = u'reinterpretAsCoverFormalsList'
    var.put(u'reinterpretAsCoverFormalsList', PyJsHoisted_reinterpretAsCoverFormalsList_)
    @Js
    def PyJsHoisted_isFutureReservedWord_(id, this, arguments, var=var):
        var = Scope({u'this':this, u'id':id, u'arguments':arguments}, var)
        var.registers([u'id'])
        while 1:
            SWITCHED = False
            CONDITION = (var.get(u'id'))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'enum')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'export')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'import')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'super')):
                SWITCHED = True
                return var.get(u'true')
            if True:
                SWITCHED = True
                return Js(False)
            SWITCHED = True
            break
    PyJsHoisted_isFutureReservedWord_.func_name = u'isFutureReservedWord'
    var.put(u'isFutureReservedWord', PyJsHoisted_isFutureReservedWord_)
    @Js
    def PyJsHoisted_parseImportNamespaceSpecifier_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'local'])
        var.put(u'node', var.get(u'Node').create())
        var.get(u'expect')(Js(u'*'))
        if var.get(u'matchContextualKeyword')(Js(u'as')).neg():
            var.get(u'throwError')(var.get(u'Messages').get(u'NoAsAfterImportNamespace'))
        var.get(u'lex')()
        var.put(u'local', var.get(u'parseNonComputedProperty')())
        return var.get(u'node').callprop(u'finishImportNamespaceSpecifier', var.get(u'local'))
    PyJsHoisted_parseImportNamespaceSpecifier_.func_name = u'parseImportNamespaceSpecifier'
    var.put(u'parseImportNamespaceSpecifier', PyJsHoisted_parseImportNamespaceSpecifier_)
    @Js
    def PyJsHoisted_parseUnaryExpression_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'expr', u'token', u'startToken'])
        pass
        if (PyJsStrictNeq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Punctuator')) and PyJsStrictNeq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Keyword'))):
            var.put(u'expr', var.get(u'parsePostfixExpression')())
        else:
            if (var.get(u'match')(Js(u'++')) or var.get(u'match')(Js(u'--'))):
                var.put(u'startToken', var.get(u'lookahead'))
                var.put(u'token', var.get(u'lex')())
                var.put(u'expr', var.get(u'inheritCoverGrammar')(var.get(u'parseUnaryExpression')))
                if ((var.get(u'strict') and PyJsStrictEq(var.get(u'expr').get(u'type'),var.get(u'Syntax').get(u'Identifier'))) and var.get(u'isRestrictedWord')(var.get(u'expr').get(u'name'))):
                    var.get(u'tolerateError')(var.get(u'Messages').get(u'StrictLHSPrefix'))
                if var.get(u'isAssignmentTarget').neg():
                    var.get(u'tolerateError')(var.get(u'Messages').get(u'InvalidLHSInAssignment'))
                var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishUnaryExpression', var.get(u'token').get(u'value'), var.get(u'expr')))
                var.put(u'isAssignmentTarget', var.put(u'isBindingElement', Js(False)))
            else:
                if (((var.get(u'match')(Js(u'+')) or var.get(u'match')(Js(u'-'))) or var.get(u'match')(Js(u'~'))) or var.get(u'match')(Js(u'!'))):
                    var.put(u'startToken', var.get(u'lookahead'))
                    var.put(u'token', var.get(u'lex')())
                    var.put(u'expr', var.get(u'inheritCoverGrammar')(var.get(u'parseUnaryExpression')))
                    var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishUnaryExpression', var.get(u'token').get(u'value'), var.get(u'expr')))
                    var.put(u'isAssignmentTarget', var.put(u'isBindingElement', Js(False)))
                else:
                    if ((var.get(u'matchKeyword')(Js(u'delete')) or var.get(u'matchKeyword')(Js(u'void'))) or var.get(u'matchKeyword')(Js(u'typeof'))):
                        var.put(u'startToken', var.get(u'lookahead'))
                        var.put(u'token', var.get(u'lex')())
                        var.put(u'expr', var.get(u'inheritCoverGrammar')(var.get(u'parseUnaryExpression')))
                        var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishUnaryExpression', var.get(u'token').get(u'value'), var.get(u'expr')))
                        if ((var.get(u'strict') and PyJsStrictEq(var.get(u'expr').get(u'operator'),Js(u'delete'))) and PyJsStrictEq(var.get(u'expr').get(u'argument').get(u'type'),var.get(u'Syntax').get(u'Identifier'))):
                            var.get(u'tolerateError')(var.get(u'Messages').get(u'StrictDelete'))
                        var.put(u'isAssignmentTarget', var.put(u'isBindingElement', Js(False)))
                    else:
                        var.put(u'expr', var.get(u'parsePostfixExpression')())
        return var.get(u'expr')
    PyJsHoisted_parseUnaryExpression_.func_name = u'parseUnaryExpression'
    var.put(u'parseUnaryExpression', PyJsHoisted_parseUnaryExpression_)
    @Js
    def PyJsHoisted_parseAssignmentExpression_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'expr', u'token', u'right', u'list', u'startToken'])
        pass
        var.put(u'startToken', var.get(u'lookahead'))
        var.put(u'token', var.get(u'lookahead'))
        if (var.get(u'state').get(u'allowYield').neg() and var.get(u'matchKeyword')(Js(u'yield'))):
            return var.get(u'parseYieldExpression')()
        var.put(u'expr', var.get(u'parseConditionalExpression')())
        if (PyJsStrictEq(var.get(u'expr').get(u'type'),var.get(u'PlaceHolders').get(u'ArrowParameterPlaceHolder')) or var.get(u'match')(Js(u'=>'))):
            var.put(u'isAssignmentTarget', var.put(u'isBindingElement', Js(False)))
            var.put(u'list', var.get(u'reinterpretAsCoverFormalsList')(var.get(u'expr')))
            if var.get(u'list'):
                var.put(u'firstCoverInitializedNameError', var.get(u"null"))
                return var.get(u'parseArrowFunctionExpression')(var.get(u'list'), var.get(u'WrappingNode').create(var.get(u'startToken')))
            return var.get(u'expr')
        if var.get(u'matchAssign')():
            if var.get(u'isAssignmentTarget').neg():
                var.get(u'tolerateError')(var.get(u'Messages').get(u'InvalidLHSInAssignment'))
            if (var.get(u'strict') and PyJsStrictEq(var.get(u'expr').get(u'type'),var.get(u'Syntax').get(u'Identifier'))):
                if var.get(u'isRestrictedWord')(var.get(u'expr').get(u'name')):
                    var.get(u'tolerateUnexpectedToken')(var.get(u'token'), var.get(u'Messages').get(u'StrictLHSAssignment'))
                if var.get(u'isStrictModeReservedWord')(var.get(u'expr').get(u'name')):
                    var.get(u'tolerateUnexpectedToken')(var.get(u'token'), var.get(u'Messages').get(u'StrictReservedWord'))
            if var.get(u'match')(Js(u'=')).neg():
                var.put(u'isAssignmentTarget', var.put(u'isBindingElement', Js(False)))
            else:
                var.get(u'reinterpretExpressionAsPattern')(var.get(u'expr'))
            var.put(u'token', var.get(u'lex')())
            var.put(u'right', var.get(u'isolateCoverGrammar')(var.get(u'parseAssignmentExpression')))
            var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishAssignmentExpression', var.get(u'token').get(u'value'), var.get(u'expr'), var.get(u'right')))
            var.put(u'firstCoverInitializedNameError', var.get(u"null"))
        return var.get(u'expr')
    PyJsHoisted_parseAssignmentExpression_.func_name = u'parseAssignmentExpression'
    var.put(u'parseAssignmentExpression', PyJsHoisted_parseAssignmentExpression_)
    @Js
    def PyJsHoisted_isKeyword_(id, this, arguments, var=var):
        var = Scope({u'this':this, u'id':id, u'arguments':arguments}, var)
        var.registers([u'id'])
        while 1:
            SWITCHED = False
            CONDITION = (var.get(u'id').get(u'length'))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                SWITCHED = True
                return ((PyJsStrictEq(var.get(u'id'),Js(u'if')) or PyJsStrictEq(var.get(u'id'),Js(u'in'))) or PyJsStrictEq(var.get(u'id'),Js(u'do')))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                SWITCHED = True
                return ((((PyJsStrictEq(var.get(u'id'),Js(u'var')) or PyJsStrictEq(var.get(u'id'),Js(u'for'))) or PyJsStrictEq(var.get(u'id'),Js(u'new'))) or PyJsStrictEq(var.get(u'id'),Js(u'try'))) or PyJsStrictEq(var.get(u'id'),Js(u'let')))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                SWITCHED = True
                return (((((PyJsStrictEq(var.get(u'id'),Js(u'this')) or PyJsStrictEq(var.get(u'id'),Js(u'else'))) or PyJsStrictEq(var.get(u'id'),Js(u'case'))) or PyJsStrictEq(var.get(u'id'),Js(u'void'))) or PyJsStrictEq(var.get(u'id'),Js(u'with'))) or PyJsStrictEq(var.get(u'id'),Js(u'enum')))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                SWITCHED = True
                return (((((((PyJsStrictEq(var.get(u'id'),Js(u'while')) or PyJsStrictEq(var.get(u'id'),Js(u'break'))) or PyJsStrictEq(var.get(u'id'),Js(u'catch'))) or PyJsStrictEq(var.get(u'id'),Js(u'throw'))) or PyJsStrictEq(var.get(u'id'),Js(u'const'))) or PyJsStrictEq(var.get(u'id'),Js(u'yield'))) or PyJsStrictEq(var.get(u'id'),Js(u'class'))) or PyJsStrictEq(var.get(u'id'),Js(u'super')))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                SWITCHED = True
                return (((((PyJsStrictEq(var.get(u'id'),Js(u'return')) or PyJsStrictEq(var.get(u'id'),Js(u'typeof'))) or PyJsStrictEq(var.get(u'id'),Js(u'delete'))) or PyJsStrictEq(var.get(u'id'),Js(u'switch'))) or PyJsStrictEq(var.get(u'id'),Js(u'export'))) or PyJsStrictEq(var.get(u'id'),Js(u'import')))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
                SWITCHED = True
                return ((PyJsStrictEq(var.get(u'id'),Js(u'default')) or PyJsStrictEq(var.get(u'id'),Js(u'finally'))) or PyJsStrictEq(var.get(u'id'),Js(u'extends')))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(8.0)):
                SWITCHED = True
                return ((PyJsStrictEq(var.get(u'id'),Js(u'function')) or PyJsStrictEq(var.get(u'id'),Js(u'continue'))) or PyJsStrictEq(var.get(u'id'),Js(u'debugger')))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(10.0)):
                SWITCHED = True
                return PyJsStrictEq(var.get(u'id'),Js(u'instanceof'))
            if True:
                SWITCHED = True
                return Js(False)
            SWITCHED = True
            break
    PyJsHoisted_isKeyword_.func_name = u'isKeyword'
    var.put(u'isKeyword', PyJsHoisted_isKeyword_)
    @Js
    def PyJsHoisted_parseLexicalBinding_(kind, options, this, arguments, var=var):
        var = Scope({u'this':this, u'kind':kind, u'options':options, u'arguments':arguments}, var)
        var.registers([u'node', u'kind', u'options', u'init', u'params', u'id'])
        var.put(u'init', var.get(u"null"))
        var.put(u'node', var.get(u'Node').create())
        var.put(u'params', Js([]))
        var.put(u'id', var.get(u'parsePattern')(var.get(u'params'), var.get(u'kind')))
        if ((var.get(u'strict') and PyJsStrictEq(var.get(u'id').get(u'type'),var.get(u'Syntax').get(u'Identifier'))) and var.get(u'isRestrictedWord')(var.get(u'id').get(u'name'))):
            var.get(u'tolerateError')(var.get(u'Messages').get(u'StrictVarName'))
        if PyJsStrictEq(var.get(u'kind'),Js(u'const')):
            if (var.get(u'matchKeyword')(Js(u'in')).neg() and var.get(u'matchContextualKeyword')(Js(u'of')).neg()):
                var.get(u'expect')(Js(u'='))
                var.put(u'init', var.get(u'isolateCoverGrammar')(var.get(u'parseAssignmentExpression')))
        else:
            if ((var.get(u'options').get(u'inFor').neg() and PyJsStrictNeq(var.get(u'id').get(u'type'),var.get(u'Syntax').get(u'Identifier'))) or var.get(u'match')(Js(u'='))):
                var.get(u'expect')(Js(u'='))
                var.put(u'init', var.get(u'isolateCoverGrammar')(var.get(u'parseAssignmentExpression')))
        return var.get(u'node').callprop(u'finishVariableDeclarator', var.get(u'id'), var.get(u'init'))
    PyJsHoisted_parseLexicalBinding_.func_name = u'parseLexicalBinding'
    var.put(u'parseLexicalBinding', PyJsHoisted_parseLexicalBinding_)
    @Js
    def PyJsHoisted_tolerateError_(messageFormat, this, arguments, var=var):
        var = Scope({u'this':this, u'messageFormat':messageFormat, u'arguments':arguments}, var)
        var.registers([u'msg', u'args', u'messageFormat', u'error'])
        pass
        var.put(u'args', var.get(u'Array').get(u'prototype').get(u'slice').callprop(u'call', var.get(u'arguments'), Js(1.0)))
        @Js
        def PyJs_anonymous_119_(whole, idx, this, arguments, var=var):
            var = Scope({u'this':this, u'whole':whole, u'arguments':arguments, u'idx':idx}, var)
            var.registers([u'whole', u'idx'])
            var.get(u'assert')((var.get(u'idx')<var.get(u'args').get(u'length')), Js(u'Message reference must be in range'))
            return var.get(u'args').get(var.get(u'idx'))
        PyJs_anonymous_119_._set_name(u'anonymous')
        var.put(u'msg', var.get(u'messageFormat').callprop(u'replace', JsRegExp(u'/%(\\d)/g'), PyJs_anonymous_119_))
        var.put(u'error', var.get(u'createError')(var.get(u'lineNumber'), var.get(u'lastIndex'), var.get(u'msg')))
        if var.get(u'extra').get(u'errors'):
            var.get(u'recordError')(var.get(u'error'))
        else:
            PyJsTempException = JsToPyException(var.get(u'error'))
            raise PyJsTempException
    PyJsHoisted_tolerateError_.func_name = u'tolerateError'
    var.put(u'tolerateError', PyJsHoisted_tolerateError_)
    @Js
    def PyJsHoisted_parseBinaryExpression_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'right', u'i', u'expr', u'prec', u'operator', u'token', u'markers', u'marker', u'stack', u'left'])
        pass
        var.put(u'marker', var.get(u'lookahead'))
        var.put(u'left', var.get(u'inheritCoverGrammar')(var.get(u'parseUnaryExpression')))
        var.put(u'token', var.get(u'lookahead'))
        var.put(u'prec', var.get(u'binaryPrecedence')(var.get(u'token'), var.get(u'state').get(u'allowIn')))
        if PyJsStrictEq(var.get(u'prec'),Js(0.0)):
            return var.get(u'left')
        var.put(u'isAssignmentTarget', var.put(u'isBindingElement', Js(False)))
        var.get(u'token').put(u'prec', var.get(u'prec'))
        var.get(u'lex')()
        var.put(u'markers', Js([var.get(u'marker'), var.get(u'lookahead')]))
        var.put(u'right', var.get(u'isolateCoverGrammar')(var.get(u'parseUnaryExpression')))
        var.put(u'stack', Js([var.get(u'left'), var.get(u'token'), var.get(u'right')]))
        while (var.put(u'prec', var.get(u'binaryPrecedence')(var.get(u'lookahead'), var.get(u'state').get(u'allowIn')))>Js(0.0)):
            while ((var.get(u'stack').get(u'length')>Js(2.0)) and (var.get(u'prec')<=var.get(u'stack').get((var.get(u'stack').get(u'length')-Js(2.0))).get(u'prec'))):
                var.put(u'right', var.get(u'stack').callprop(u'pop'))
                var.put(u'operator', var.get(u'stack').callprop(u'pop').get(u'value'))
                var.put(u'left', var.get(u'stack').callprop(u'pop'))
                var.get(u'markers').callprop(u'pop')
                var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'markers').get((var.get(u'markers').get(u'length')-Js(1.0)))).callprop(u'finishBinaryExpression', var.get(u'operator'), var.get(u'left'), var.get(u'right')))
                var.get(u'stack').callprop(u'push', var.get(u'expr'))
            var.put(u'token', var.get(u'lex')())
            var.get(u'token').put(u'prec', var.get(u'prec'))
            var.get(u'stack').callprop(u'push', var.get(u'token'))
            var.get(u'markers').callprop(u'push', var.get(u'lookahead'))
            var.put(u'expr', var.get(u'isolateCoverGrammar')(var.get(u'parseUnaryExpression')))
            var.get(u'stack').callprop(u'push', var.get(u'expr'))
        var.put(u'i', (var.get(u'stack').get(u'length')-Js(1.0)))
        var.put(u'expr', var.get(u'stack').get(var.get(u'i')))
        var.get(u'markers').callprop(u'pop')
        while (var.get(u'i')>Js(1.0)):
            var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'markers').callprop(u'pop')).callprop(u'finishBinaryExpression', var.get(u'stack').get((var.get(u'i')-Js(1.0))).get(u'value'), var.get(u'stack').get((var.get(u'i')-Js(2.0))), var.get(u'expr')))
            var.put(u'i', Js(2.0), u'-')
        return var.get(u'expr')
    PyJsHoisted_parseBinaryExpression_.func_name = u'parseBinaryExpression'
    var.put(u'parseBinaryExpression', PyJsHoisted_parseBinaryExpression_)
    @Js
    def PyJsHoisted_scanIdentifier_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'start', u'type', u'id'])
        pass
        var.put(u'start', var.get(u'index'))
        var.put(u'id', (var.get(u'getComplexIdentifier')() if PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt', var.get(u'index')),Js(92)) else var.get(u'getIdentifier')()))
        if PyJsStrictEq(var.get(u'id').get(u'length'),Js(1.0)):
            var.put(u'type', var.get(u'Token').get(u'Identifier'))
        else:
            if var.get(u'isKeyword')(var.get(u'id')):
                var.put(u'type', var.get(u'Token').get(u'Keyword'))
            else:
                if PyJsStrictEq(var.get(u'id'),Js(u'null')):
                    var.put(u'type', var.get(u'Token').get(u'NullLiteral'))
                else:
                    if (PyJsStrictEq(var.get(u'id'),Js(u'true')) or PyJsStrictEq(var.get(u'id'),Js(u'false'))):
                        var.put(u'type', var.get(u'Token').get(u'BooleanLiteral'))
                    else:
                        var.put(u'type', var.get(u'Token').get(u'Identifier'))
        PyJs_Object_20_ = Js({u'type':var.get(u'type'),u'value':var.get(u'id'),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
        return PyJs_Object_20_
    PyJsHoisted_scanIdentifier_.func_name = u'scanIdentifier'
    var.put(u'scanIdentifier', PyJsHoisted_scanIdentifier_)
    @Js
    def PyJsHoisted_unexpectedTokenError_(token, message, this, arguments, var=var):
        var = Scope({u'this':this, u'token':token, u'message':message, u'arguments':arguments}, var)
        var.registers([u'msg', u'token', u'message', u'value'])
        var.put(u'msg', (var.get(u'message') or var.get(u'Messages').get(u'UnexpectedToken')))
        if var.get(u'token'):
            if var.get(u'message').neg():
                def PyJs_LONG_120_(var=var):
                    return (var.get(u'Messages').get(u'UnexpectedNumber') if PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'NumericLiteral')) else (var.get(u'Messages').get(u'UnexpectedString') if PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'StringLiteral')) else (var.get(u'Messages').get(u'UnexpectedTemplate') if PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Template')) else var.get(u'Messages').get(u'UnexpectedToken'))))
                var.put(u'msg', (var.get(u'Messages').get(u'UnexpectedEOS') if PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'EOF')) else (var.get(u'Messages').get(u'UnexpectedIdentifier') if PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Identifier')) else PyJs_LONG_120_())))
                if PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Keyword')):
                    if var.get(u'isFutureReservedWord')(var.get(u'token').get(u'value')):
                        var.put(u'msg', var.get(u'Messages').get(u'UnexpectedReserved'))
                    else:
                        if (var.get(u'strict') and var.get(u'isStrictModeReservedWord')(var.get(u'token').get(u'value'))):
                            var.put(u'msg', var.get(u'Messages').get(u'StrictReservedWord'))
            var.put(u'value', (var.get(u'token').get(u'value').get(u'raw') if PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Template')) else var.get(u'token').get(u'value')))
        else:
            var.put(u'value', Js(u'ILLEGAL'))
        var.put(u'msg', var.get(u'msg').callprop(u'replace', Js(u'%0'), var.get(u'value')))
        def PyJs_LONG_121_(var=var):
            return (var.get(u'createError')(var.get(u'token').get(u'lineNumber'), var.get(u'token').get(u'start'), var.get(u'msg')) if (var.get(u'token') and PyJsStrictEq(var.get(u'token').get(u'lineNumber').typeof(),Js(u'number'))) else var.get(u'createError')((var.get(u'lineNumber') if var.get(u'scanning') else var.get(u'lastLineNumber')), (var.get(u'index') if var.get(u'scanning') else var.get(u'lastIndex')), var.get(u'msg')))
        return PyJs_LONG_121_()
    PyJsHoisted_unexpectedTokenError_.func_name = u'unexpectedTokenError'
    var.put(u'unexpectedTokenError', PyJsHoisted_unexpectedTokenError_)
    @Js
    def PyJsHoisted_parseNonComputedProperty_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'token'])
        var.put(u'node', var.get(u'Node').create())
        var.put(u'token', var.get(u'lex')())
        if var.get(u'isIdentifierName')(var.get(u'token')).neg():
            var.get(u'throwUnexpectedToken')(var.get(u'token'))
        return var.get(u'node').callprop(u'finishIdentifier', var.get(u'token').get(u'value'))
    PyJsHoisted_parseNonComputedProperty_.func_name = u'parseNonComputedProperty'
    var.put(u'parseNonComputedProperty', PyJsHoisted_parseNonComputedProperty_)
    @Js
    def PyJsHoisted_parseModuleSpecifier_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node'])
        var.put(u'node', var.get(u'Node').create())
        if PyJsStrictNeq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'StringLiteral')):
            var.get(u'throwError')(var.get(u'Messages').get(u'InvalidModuleSpecifier'))
        return var.get(u'node').callprop(u'finishLiteral', var.get(u'lex')())
    PyJsHoisted_parseModuleSpecifier_.func_name = u'parseModuleSpecifier'
    var.put(u'parseModuleSpecifier', PyJsHoisted_parseModuleSpecifier_)
    @Js
    def PyJsHoisted_parseParam_(options, this, arguments, var=var):
        var = Scope({u'this':this, u'options':options, u'arguments':arguments}, var)
        var.registers([u'i', u'param', u'token', u'params', u'options', u'def'])
        var.put(u'params', Js([]))
        var.put(u'token', var.get(u'lookahead'))
        if PyJsStrictEq(var.get(u'token').get(u'value'),Js(u'...')):
            var.put(u'param', var.get(u'parseRestElement')(var.get(u'params')))
            var.get(u'validateParam')(var.get(u'options'), var.get(u'param').get(u'argument'), var.get(u'param').get(u'argument').get(u'name'))
            var.get(u'options').get(u'params').callprop(u'push', var.get(u'param'))
            var.get(u'options').get(u'defaults').callprop(u'push', var.get(u"null"))
            return Js(False)
        var.put(u'param', var.get(u'parsePatternWithDefault')(var.get(u'params')))
        #for JS loop
        var.put(u'i', Js(0.0))
        while (var.get(u'i')<var.get(u'params').get(u'length')):
            try:
                var.get(u'validateParam')(var.get(u'options'), var.get(u'params').get(var.get(u'i')), var.get(u'params').get(var.get(u'i')).get(u'value'))
            finally:
                    (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
        if PyJsStrictEq(var.get(u'param').get(u'type'),var.get(u'Syntax').get(u'AssignmentPattern')):
            var.put(u'def', var.get(u'param').get(u'right'))
            var.put(u'param', var.get(u'param').get(u'left'))
            var.get(u'options').put(u'defaultCount',Js(var.get(u'options').get(u'defaultCount').to_number())+Js(1))
        var.get(u'options').get(u'params').callprop(u'push', var.get(u'param'))
        var.get(u'options').get(u'defaults').callprop(u'push', var.get(u'def'))
        return var.get(u'match')(Js(u')')).neg()
    PyJsHoisted_parseParam_.func_name = u'parseParam'
    var.put(u'parseParam', PyJsHoisted_parseParam_)
    @Js
    def PyJsHoisted_parseNewExpression_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'args', u'callee'])
        var.put(u'node', var.get(u'Node').create())
        var.get(u'expectKeyword')(Js(u'new'))
        if var.get(u'match')(Js(u'.')):
            var.get(u'lex')()
            if (PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Identifier')) and PyJsStrictEq(var.get(u'lookahead').get(u'value'),Js(u'target'))):
                if var.get(u'state').get(u'inFunctionBody'):
                    var.get(u'lex')()
                    return var.get(u'node').callprop(u'finishMetaProperty', Js(u'new'), Js(u'target'))
            var.get(u'throwUnexpectedToken')(var.get(u'lookahead'))
        var.put(u'callee', var.get(u'isolateCoverGrammar')(var.get(u'parseLeftHandSideExpression')))
        var.put(u'args', (var.get(u'parseArguments')() if var.get(u'match')(Js(u'(')) else Js([])))
        var.put(u'isAssignmentTarget', var.put(u'isBindingElement', Js(False)))
        return var.get(u'node').callprop(u'finishNewExpression', var.get(u'callee'), var.get(u'args'))
    PyJsHoisted_parseNewExpression_.func_name = u'parseNewExpression'
    var.put(u'parseNewExpression', PyJsHoisted_parseNewExpression_)
    @Js
    def PyJsHoisted_scanRegExpBody_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'body', u'terminated', u'ch', u'classMarker', u'str'])
        pass
        var.put(u'ch', var.get(u'source').get(var.get(u'index')))
        var.get(u'assert')(PyJsStrictEq(var.get(u'ch'),Js(u'/')), Js(u'Regular expression literal must start with a slash'))
        var.put(u'str', var.get(u'source').get((var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1))))
        var.put(u'classMarker', Js(False))
        var.put(u'terminated', Js(False))
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').get((var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1))))
            var.put(u'str', var.get(u'ch'), u'+')
            if PyJsStrictEq(var.get(u'ch'),Js(u'\\')):
                var.put(u'ch', var.get(u'source').get((var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1))))
                if var.get(u'isLineTerminator')(var.get(u'ch').callprop(u'charCodeAt', Js(0.0))):
                    var.get(u'throwUnexpectedToken')(var.get(u"null"), var.get(u'Messages').get(u'UnterminatedRegExp'))
                var.put(u'str', var.get(u'ch'), u'+')
            else:
                if var.get(u'isLineTerminator')(var.get(u'ch').callprop(u'charCodeAt', Js(0.0))):
                    var.get(u'throwUnexpectedToken')(var.get(u"null"), var.get(u'Messages').get(u'UnterminatedRegExp'))
                else:
                    if var.get(u'classMarker'):
                        if PyJsStrictEq(var.get(u'ch'),Js(u']')):
                            var.put(u'classMarker', Js(False))
                    else:
                        if PyJsStrictEq(var.get(u'ch'),Js(u'/')):
                            var.put(u'terminated', var.get(u'true'))
                            break
                        else:
                            if PyJsStrictEq(var.get(u'ch'),Js(u'[')):
                                var.put(u'classMarker', var.get(u'true'))
        if var.get(u'terminated').neg():
            var.get(u'throwUnexpectedToken')(var.get(u"null"), var.get(u'Messages').get(u'UnterminatedRegExp'))
        var.put(u'body', var.get(u'str').callprop(u'substr', Js(1.0), (var.get(u'str').get(u'length')-Js(2.0))))
        PyJs_Object_32_ = Js({u'value':var.get(u'body'),u'literal':var.get(u'str')})
        return PyJs_Object_32_
    PyJsHoisted_scanRegExpBody_.func_name = u'scanRegExpBody'
    var.put(u'scanRegExpBody', PyJsHoisted_scanRegExpBody_)
    @Js
    def PyJsHoisted_Node_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        if var.get(u'extra').get(u'range'):
            var.get(u"this").put(u'range', Js([var.get(u'startIndex'), Js(0.0)]))
        if var.get(u'extra').get(u'loc'):
            var.get(u"this").put(u'loc', var.get(u'SourceLocation').create())
    PyJsHoisted_Node_.func_name = u'Node'
    var.put(u'Node', PyJsHoisted_Node_)
    @Js
    def PyJsHoisted_collectToken_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'loc', u'token', u'value', u'entry'])
        pass
        PyJs_Object_44_ = Js({u'line':var.get(u'lineNumber'),u'column':(var.get(u'index')-var.get(u'lineStart'))})
        PyJs_Object_43_ = Js({u'start':PyJs_Object_44_})
        var.put(u'loc', PyJs_Object_43_)
        var.put(u'token', var.get(u'advance')())
        PyJs_Object_45_ = Js({u'line':var.get(u'lineNumber'),u'column':(var.get(u'index')-var.get(u'lineStart'))})
        var.get(u'loc').put(u'end', PyJs_Object_45_)
        if PyJsStrictNeq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'EOF')):
            var.put(u'value', var.get(u'source').callprop(u'slice', var.get(u'token').get(u'start'), var.get(u'token').get(u'end')))
            PyJs_Object_46_ = Js({u'type':var.get(u'TokenName').get(var.get(u'token').get(u'type')),u'value':var.get(u'value'),u'range':Js([var.get(u'token').get(u'start'), var.get(u'token').get(u'end')]),u'loc':var.get(u'loc')})
            var.put(u'entry', PyJs_Object_46_)
            if var.get(u'token').get(u'regex'):
                PyJs_Object_47_ = Js({u'pattern':var.get(u'token').get(u'regex').get(u'pattern'),u'flags':var.get(u'token').get(u'regex').get(u'flags')})
                var.get(u'entry').put(u'regex', PyJs_Object_47_)
            var.get(u'extra').get(u'tokens').callprop(u'push', var.get(u'entry'))
        return var.get(u'token')
    PyJsHoisted_collectToken_.func_name = u'collectToken'
    var.put(u'collectToken', PyJsHoisted_collectToken_)
    @Js
    def PyJsHoisted_parseWithStatement_(node, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'arguments':arguments}, var)
        var.registers([u'body', u'node', u'object'])
        pass
        if var.get(u'strict'):
            var.get(u'tolerateError')(var.get(u'Messages').get(u'StrictModeWith'))
        var.get(u'expectKeyword')(Js(u'with'))
        var.get(u'expect')(Js(u'('))
        var.put(u'object', var.get(u'parseExpression')())
        var.get(u'expect')(Js(u')'))
        var.put(u'body', var.get(u'parseStatement')())
        return var.get(u'node').callprop(u'finishWithStatement', var.get(u'object'), var.get(u'body'))
    PyJsHoisted_parseWithStatement_.func_name = u'parseWithStatement'
    var.put(u'parseWithStatement', PyJsHoisted_parseWithStatement_)
    @Js
    def PyJsHoisted_parseObjectPattern_(params, kind, this, arguments, var=var):
        var = Scope({u'this':this, u'kind':kind, u'params':params, u'arguments':arguments}, var)
        var.registers([u'node', u'kind', u'params', u'properties'])
        var.put(u'node', var.get(u'Node').create())
        var.put(u'properties', Js([]))
        var.get(u'expect')(Js(u'{'))
        while var.get(u'match')(Js(u'}')).neg():
            var.get(u'properties').callprop(u'push', var.get(u'parsePropertyPattern')(var.get(u'params'), var.get(u'kind')))
            if var.get(u'match')(Js(u'}')).neg():
                var.get(u'expect')(Js(u','))
        var.get(u'lex')()
        return var.get(u'node').callprop(u'finishObjectPattern', var.get(u'properties'))
    PyJsHoisted_parseObjectPattern_.func_name = u'parseObjectPattern'
    var.put(u'parseObjectPattern', PyJsHoisted_parseObjectPattern_)
    @Js
    def PyJsHoisted_parseImportSpecifier_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'imported', u'local'])
        var.put(u'node', var.get(u'Node').create())
        var.put(u'imported', var.get(u'parseNonComputedProperty')())
        if var.get(u'matchContextualKeyword')(Js(u'as')):
            var.get(u'lex')()
            var.put(u'local', var.get(u'parseVariableIdentifier')())
        return var.get(u'node').callprop(u'finishImportSpecifier', var.get(u'local'), var.get(u'imported'))
    PyJsHoisted_parseImportSpecifier_.func_name = u'parseImportSpecifier'
    var.put(u'parseImportSpecifier', PyJsHoisted_parseImportSpecifier_)
    @Js
    def PyJsHoisted_skipComment_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'start', u'ch'])
        pass
        var.put(u'hasLineTerminator', Js(False))
        var.put(u'start', PyJsStrictEq(var.get(u'index'),Js(0.0)))
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').callprop(u'charCodeAt', var.get(u'index')))
            if var.get(u'isWhiteSpace')(var.get(u'ch')):
                var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
            else:
                if var.get(u'isLineTerminator')(var.get(u'ch')):
                    var.put(u'hasLineTerminator', var.get(u'true'))
                    var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                    if (PyJsStrictEq(var.get(u'ch'),Js(13)) and PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt', var.get(u'index')),Js(10))):
                        var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                    var.put(u'lineNumber',Js(var.get(u'lineNumber').to_number())+Js(1))
                    var.put(u'lineStart', var.get(u'index'))
                    var.put(u'start', var.get(u'true'))
                else:
                    if PyJsStrictEq(var.get(u'ch'),Js(47)):
                        var.put(u'ch', var.get(u'source').callprop(u'charCodeAt', (var.get(u'index')+Js(1.0))))
                        if PyJsStrictEq(var.get(u'ch'),Js(47)):
                            var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                            var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                            var.get(u'skipSingleLineComment')(Js(2.0))
                            var.put(u'start', var.get(u'true'))
                        else:
                            if PyJsStrictEq(var.get(u'ch'),Js(42)):
                                var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                                var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                                var.get(u'skipMultiLineComment')()
                            else:
                                break
                    else:
                        if (var.get(u'start') and PyJsStrictEq(var.get(u'ch'),Js(45))):
                            if (PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt', (var.get(u'index')+Js(1.0))),Js(45)) and PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt', (var.get(u'index')+Js(2.0))),Js(62))):
                                var.put(u'index', Js(3.0), u'+')
                                var.get(u'skipSingleLineComment')(Js(3.0))
                            else:
                                break
                        else:
                            if PyJsStrictEq(var.get(u'ch'),Js(60)):
                                if PyJsStrictEq(var.get(u'source').callprop(u'slice', (var.get(u'index')+Js(1.0)), (var.get(u'index')+Js(4.0))),Js(u'!--')):
                                    var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                                    var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                                    var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                                    var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                                    var.get(u'skipSingleLineComment')(Js(4.0))
                                else:
                                    break
                            else:
                                break
    PyJsHoisted_skipComment_.func_name = u'skipComment'
    var.put(u'skipComment', PyJsHoisted_skipComment_)
    @Js
    def PyJsHoisted_parseVariableStatement_(node, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'declarations'])
        pass
        var.get(u'expectKeyword')(Js(u'var'))
        PyJs_Object_140_ = Js({u'inFor':Js(False)})
        var.put(u'declarations', var.get(u'parseVariableDeclarationList')(PyJs_Object_140_))
        var.get(u'consumeSemicolon')()
        return var.get(u'node').callprop(u'finishVariableDeclaration', var.get(u'declarations'))
    PyJsHoisted_parseVariableStatement_.func_name = u'parseVariableStatement'
    var.put(u'parseVariableStatement', PyJsHoisted_parseVariableStatement_)
    @Js
    def PyJsHoisted_parseDebuggerStatement_(node, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'arguments':arguments}, var)
        var.registers([u'node'])
        var.get(u'expectKeyword')(Js(u'debugger'))
        var.get(u'consumeSemicolon')()
        return var.get(u'node').callprop(u'finishDebuggerStatement')
    PyJsHoisted_parseDebuggerStatement_.func_name = u'parseDebuggerStatement'
    var.put(u'parseDebuggerStatement', PyJsHoisted_parseDebuggerStatement_)
    @Js
    def PyJsHoisted_lookaheadPropertyName_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        while 1:
            SWITCHED = False
            CONDITION = (var.get(u'lookahead').get(u'type'))
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Token').get(u'Identifier')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Token').get(u'StringLiteral')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Token').get(u'BooleanLiteral')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Token').get(u'NullLiteral')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Token').get(u'NumericLiteral')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Token').get(u'Keyword')):
                SWITCHED = True
                return var.get(u'true')
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Token').get(u'Punctuator')):
                SWITCHED = True
                return PyJsStrictEq(var.get(u'lookahead').get(u'value'),Js(u'['))
            SWITCHED = True
            break
        return Js(False)
    PyJsHoisted_lookaheadPropertyName_.func_name = u'lookaheadPropertyName'
    var.put(u'lookaheadPropertyName', PyJsHoisted_lookaheadPropertyName_)
    @Js
    def PyJsHoisted_tokenize_(code, options, this, arguments, var=var):
        var = Scope({u'this':this, u'code':code, u'options':options, u'arguments':arguments}, var)
        var.registers([u'tokens', u'code', u'toString', u'options'])
        pass
        var.put(u'toString', var.get(u'String'))
        if (PyJsStrictNeq(var.get(u'code',throw=False).typeof(),Js(u'string')) and var.get(u'code').instanceof(var.get(u'String')).neg()):
            var.put(u'code', var.get(u'toString')(var.get(u'code')))
        var.put(u'source', var.get(u'code'))
        var.put(u'index', Js(0.0))
        var.put(u'lineNumber', (Js(1.0) if (var.get(u'source').get(u'length')>Js(0.0)) else Js(0.0)))
        var.put(u'lineStart', Js(0.0))
        var.put(u'startIndex', var.get(u'index'))
        var.put(u'startLineNumber', var.get(u'lineNumber'))
        var.put(u'startLineStart', var.get(u'lineStart'))
        var.put(u'length', var.get(u'source').get(u'length'))
        var.put(u'lookahead', var.get(u"null"))
        PyJs_Object_152_ = Js({})
        PyJs_Object_151_ = Js({u'allowIn':var.get(u'true'),u'allowYield':var.get(u'true'),u'labelSet':PyJs_Object_152_,u'inFunctionBody':Js(False),u'inIteration':Js(False),u'inSwitch':Js(False),u'lastCommentStart':(-Js(1.0)),u'curlyStack':Js([])})
        var.put(u'state', PyJs_Object_151_)
        PyJs_Object_153_ = Js({})
        var.put(u'extra', PyJs_Object_153_)
        PyJs_Object_154_ = Js({})
        var.put(u'options', (var.get(u'options') or PyJs_Object_154_))
        var.get(u'options').put(u'tokens', var.get(u'true'))
        var.get(u'extra').put(u'tokens', Js([]))
        var.get(u'extra').put(u'tokenize', var.get(u'true'))
        var.get(u'extra').put(u'openParenToken', (-Js(1.0)))
        var.get(u'extra').put(u'openCurlyToken', (-Js(1.0)))
        var.get(u'extra').put(u'range', (PyJsStrictEq(var.get(u'options').get(u'range').typeof(),Js(u'boolean')) and var.get(u'options').get(u'range')))
        var.get(u'extra').put(u'loc', (PyJsStrictEq(var.get(u'options').get(u'loc').typeof(),Js(u'boolean')) and var.get(u'options').get(u'loc')))
        if (PyJsStrictEq(var.get(u'options').get(u'comment').typeof(),Js(u'boolean')) and var.get(u'options').get(u'comment')):
            var.get(u'extra').put(u'comments', Js([]))
        if (PyJsStrictEq(var.get(u'options').get(u'tolerant').typeof(),Js(u'boolean')) and var.get(u'options').get(u'tolerant')):
            var.get(u'extra').put(u'errors', Js([]))
        try:
            var.get(u'peek')()
            if PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'EOF')):
                return var.get(u'extra').get(u'tokens')
            var.get(u'lex')()
            while PyJsStrictNeq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'EOF')):
                try:
                    var.get(u'lex')()
                except PyJsException as PyJsTempException:
                    PyJsHolder_6c65784572726f72_76841511 = var.own.get(u'lexError')
                    var.force_own_put(u'lexError', PyExceptionToJs(PyJsTempException))
                    try:
                        if var.get(u'extra').get(u'errors'):
                            var.get(u'recordError')(var.get(u'lexError'))
                            break
                        else:
                            PyJsTempException = JsToPyException(var.get(u'lexError'))
                            raise PyJsTempException
                    finally:
                        if PyJsHolder_6c65784572726f72_76841511 is not None:
                            var.own[u'lexError'] = PyJsHolder_6c65784572726f72_76841511
                        else:
                            del var.own[u'lexError']
                        del PyJsHolder_6c65784572726f72_76841511
            var.get(u'filterTokenLocation')()
            var.put(u'tokens', var.get(u'extra').get(u'tokens'))
            if PyJsStrictNeq(var.get(u'extra').get(u'comments').typeof(),Js(u'undefined')):
                var.get(u'tokens').put(u'comments', var.get(u'extra').get(u'comments'))
            if PyJsStrictNeq(var.get(u'extra').get(u'errors').typeof(),Js(u'undefined')):
                var.get(u'tokens').put(u'errors', var.get(u'extra').get(u'errors'))
        except PyJsException as PyJsTempException:
            PyJsHolder_65_58840235 = var.own.get(u'e')
            var.force_own_put(u'e', PyExceptionToJs(PyJsTempException))
            try:
                PyJsTempException = JsToPyException(var.get(u'e'))
                raise PyJsTempException
            finally:
                if PyJsHolder_65_58840235 is not None:
                    var.own[u'e'] = PyJsHolder_65_58840235
                else:
                    del var.own[u'e']
                del PyJsHolder_65_58840235
        finally:
            PyJs_Object_155_ = Js({})
            var.put(u'extra', PyJs_Object_155_)
        return var.get(u'tokens')
    PyJsHoisted_tokenize_.func_name = u'tokenize'
    var.put(u'tokenize', PyJsHoisted_tokenize_)
    @Js
    def PyJsHoisted_parseExpression_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'expr', u'expressions', u'startToken'])
        var.put(u'startToken', var.get(u'lookahead'))
        var.put(u'expr', var.get(u'isolateCoverGrammar')(var.get(u'parseAssignmentExpression')))
        if var.get(u'match')(Js(u',')):
            var.put(u'expressions', Js([var.get(u'expr')]))
            while (var.get(u'startIndex')<var.get(u'length')):
                if var.get(u'match')(Js(u',')).neg():
                    break
                var.get(u'lex')()
                var.get(u'expressions').callprop(u'push', var.get(u'isolateCoverGrammar')(var.get(u'parseAssignmentExpression')))
            var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishSequenceExpression', var.get(u'expressions')))
        return var.get(u'expr')
    PyJsHoisted_parseExpression_.func_name = u'parseExpression'
    var.put(u'parseExpression', PyJsHoisted_parseExpression_)
    @Js
    def PyJsHoisted_constructError_(msg, column, this, arguments, var=var):
        var = Scope({u'msg':msg, u'column':column, u'this':this, u'arguments':arguments}, var)
        var.registers([u'msg', u'column', u'error'])
        var.put(u'error', var.get(u'Error').create(var.get(u'msg')))
        try:
            PyJsTempException = JsToPyException(var.get(u'error'))
            raise PyJsTempException
        except PyJsException as PyJsTempException:
            PyJsHolder_62617365_41349638 = var.own.get(u'base')
            var.force_own_put(u'base', PyExceptionToJs(PyJsTempException))
            try:
                if (var.get(u'Object').get(u'create') and var.get(u'Object').get(u'defineProperty')):
                    var.put(u'error', var.get(u'Object').callprop(u'create', var.get(u'base')))
                    PyJs_Object_117_ = Js({u'value':var.get(u'column')})
                    var.get(u'Object').callprop(u'defineProperty', var.get(u'error'), Js(u'column'), PyJs_Object_117_)
            finally:
                if PyJsHolder_62617365_41349638 is not None:
                    var.own[u'base'] = PyJsHolder_62617365_41349638
                else:
                    del var.own[u'base']
                del PyJsHolder_62617365_41349638
        finally:
            return var.get(u'error')
    PyJsHoisted_constructError_.func_name = u'constructError'
    var.put(u'constructError', PyJsHoisted_constructError_)
    @Js
    def PyJsHoisted_parseObjectPropertyKey_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'expr', u'token'])
        var.put(u'node', var.get(u'Node').create())
        var.put(u'token', var.get(u'lex')())
        while 1:
            SWITCHED = False
            CONDITION = (var.get(u'token').get(u'type'))
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Token').get(u'StringLiteral')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Token').get(u'NumericLiteral')):
                SWITCHED = True
                if (var.get(u'strict') and var.get(u'token').get(u'octal')):
                    var.get(u'tolerateUnexpectedToken')(var.get(u'token'), var.get(u'Messages').get(u'StrictOctalLiteral'))
                return var.get(u'node').callprop(u'finishLiteral', var.get(u'token'))
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Token').get(u'Identifier')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Token').get(u'BooleanLiteral')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Token').get(u'NullLiteral')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Token').get(u'Keyword')):
                SWITCHED = True
                return var.get(u'node').callprop(u'finishIdentifier', var.get(u'token').get(u'value'))
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Token').get(u'Punctuator')):
                SWITCHED = True
                if PyJsStrictEq(var.get(u'token').get(u'value'),Js(u'[')):
                    var.put(u'expr', var.get(u'isolateCoverGrammar')(var.get(u'parseAssignmentExpression')))
                    var.get(u'expect')(Js(u']'))
                    return var.get(u'expr')
                break
            SWITCHED = True
            break
        var.get(u'throwUnexpectedToken')(var.get(u'token'))
    PyJsHoisted_parseObjectPropertyKey_.func_name = u'parseObjectPropertyKey'
    var.put(u'parseObjectPropertyKey', PyJsHoisted_parseObjectPropertyKey_)
    @Js
    def PyJsHoisted_parseArrayPattern_(params, kind, this, arguments, var=var):
        var = Scope({u'this':this, u'kind':kind, u'params':params, u'arguments':arguments}, var)
        var.registers([u'node', u'kind', u'elements', u'restNode', u'rest', u'params'])
        var.put(u'node', var.get(u'Node').create())
        var.put(u'elements', Js([]))
        var.get(u'expect')(Js(u'['))
        while var.get(u'match')(Js(u']')).neg():
            if var.get(u'match')(Js(u',')):
                var.get(u'lex')()
                var.get(u'elements').callprop(u'push', var.get(u"null"))
            else:
                if var.get(u'match')(Js(u'...')):
                    var.put(u'restNode', var.get(u'Node').create())
                    var.get(u'lex')()
                    var.get(u'params').callprop(u'push', var.get(u'lookahead'))
                    var.put(u'rest', var.get(u'parseVariableIdentifier')(var.get(u'params'), var.get(u'kind')))
                    var.get(u'elements').callprop(u'push', var.get(u'restNode').callprop(u'finishRestElement', var.get(u'rest')))
                    break
                else:
                    var.get(u'elements').callprop(u'push', var.get(u'parsePatternWithDefault')(var.get(u'params'), var.get(u'kind')))
                if var.get(u'match')(Js(u']')).neg():
                    var.get(u'expect')(Js(u','))
        var.get(u'expect')(Js(u']'))
        return var.get(u'node').callprop(u'finishArrayPattern', var.get(u'elements'))
    PyJsHoisted_parseArrayPattern_.func_name = u'parseArrayPattern'
    var.put(u'parseArrayPattern', PyJsHoisted_parseArrayPattern_)
    @Js
    def PyJsHoisted_expectKeyword_(keyword, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'keyword':keyword}, var)
        var.registers([u'token', u'keyword'])
        var.put(u'token', var.get(u'lex')())
        if (PyJsStrictNeq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Keyword')) or PyJsStrictNeq(var.get(u'token').get(u'value'),var.get(u'keyword'))):
            var.get(u'throwUnexpectedToken')(var.get(u'token'))
    PyJsHoisted_expectKeyword_.func_name = u'expectKeyword'
    var.put(u'expectKeyword', PyJsHoisted_expectKeyword_)
    @Js
    def PyJsHoisted_assert_(condition, message, this, arguments, var=var):
        var = Scope({u'this':this, u'message':message, u'arguments':arguments, u'condition':condition}, var)
        var.registers([u'message', u'condition'])
        if var.get(u'condition').neg():
            PyJsTempException = JsToPyException(var.get(u'Error').create((Js(u'ASSERT: ')+var.get(u'message'))))
            raise PyJsTempException
    PyJsHoisted_assert_.func_name = u'assert'
    var.put(u'assert', PyJsHoisted_assert_)
    @Js
    def PyJsHoisted_parseConciseBody_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        if var.get(u'match')(Js(u'{')):
            return var.get(u'parseFunctionSourceElements')()
        return var.get(u'isolateCoverGrammar')(var.get(u'parseAssignmentExpression'))
    PyJsHoisted_parseConciseBody_.func_name = u'parseConciseBody'
    var.put(u'parseConciseBody', PyJsHoisted_parseConciseBody_)
    @Js
    def PyJsHoisted_createError_(line, pos, description, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'line':line, u'pos':pos, u'description':description}, var)
        var.registers([u'description', u'column', u'pos', u'error', u'msg', u'line'])
        pass
        var.put(u'msg', (((Js(u'Line ')+var.get(u'line'))+Js(u': '))+var.get(u'description')))
        var.put(u'column', ((var.get(u'pos')-(var.get(u'lineStart') if var.get(u'scanning') else var.get(u'lastLineStart')))+Js(1.0)))
        var.put(u'error', var.get(u'constructError')(var.get(u'msg'), var.get(u'column')))
        var.get(u'error').put(u'lineNumber', var.get(u'line'))
        var.get(u'error').put(u'description', var.get(u'description'))
        var.get(u'error').put(u'index', var.get(u'pos'))
        return var.get(u'error')
    PyJsHoisted_createError_.func_name = u'createError'
    var.put(u'createError', PyJsHoisted_createError_)
    @Js
    def PyJsHoisted_parseLeftHandSideExpressionAllowCall_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'previousAllowIn', u'expr', u'args', u'quasi', u'startToken', u'property'])
        var.put(u'previousAllowIn', var.get(u'state').get(u'allowIn'))
        var.put(u'startToken', var.get(u'lookahead'))
        var.get(u'state').put(u'allowIn', var.get(u'true'))
        if (var.get(u'matchKeyword')(Js(u'super')) and var.get(u'state').get(u'inFunctionBody')):
            var.put(u'expr', var.get(u'Node').create())
            var.get(u'lex')()
            var.put(u'expr', var.get(u'expr').callprop(u'finishSuper'))
            if ((var.get(u'match')(Js(u'(')).neg() and var.get(u'match')(Js(u'.')).neg()) and var.get(u'match')(Js(u'[')).neg()):
                var.get(u'throwUnexpectedToken')(var.get(u'lookahead'))
        else:
            var.put(u'expr', var.get(u'inheritCoverGrammar')((var.get(u'parseNewExpression') if var.get(u'matchKeyword')(Js(u'new')) else var.get(u'parsePrimaryExpression'))))
        #for JS loop

        while 1:
            if var.get(u'match')(Js(u'.')):
                var.put(u'isBindingElement', Js(False))
                var.put(u'isAssignmentTarget', var.get(u'true'))
                var.put(u'property', var.get(u'parseNonComputedMember')())
                var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishMemberExpression', Js(u'.'), var.get(u'expr'), var.get(u'property')))
            else:
                if var.get(u'match')(Js(u'(')):
                    var.put(u'isBindingElement', Js(False))
                    var.put(u'isAssignmentTarget', Js(False))
                    var.put(u'args', var.get(u'parseArguments')())
                    var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishCallExpression', var.get(u'expr'), var.get(u'args')))
                else:
                    if var.get(u'match')(Js(u'[')):
                        var.put(u'isBindingElement', Js(False))
                        var.put(u'isAssignmentTarget', var.get(u'true'))
                        var.put(u'property', var.get(u'parseComputedMember')())
                        var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishMemberExpression', Js(u'['), var.get(u'expr'), var.get(u'property')))
                    else:
                        if (PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Template')) and var.get(u'lookahead').get(u'head')):
                            var.put(u'quasi', var.get(u'parseTemplateLiteral')())
                            var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishTaggedTemplateExpression', var.get(u'expr'), var.get(u'quasi')))
                        else:
                            break

        var.get(u'state').put(u'allowIn', var.get(u'previousAllowIn'))
        return var.get(u'expr')
    PyJsHoisted_parseLeftHandSideExpressionAllowCall_.func_name = u'parseLeftHandSideExpressionAllowCall'
    var.put(u'parseLeftHandSideExpressionAllowCall', PyJsHoisted_parseLeftHandSideExpressionAllowCall_)
    @Js
    def PyJsHoisted_fromCodePoint_(cp, this, arguments, var=var):
        var = Scope({u'this':this, u'cp':cp, u'arguments':arguments}, var)
        var.registers([u'cp'])
        return (var.get(u'String').callprop(u'fromCharCode', var.get(u'cp')) if (var.get(u'cp')<Js(65536)) else (var.get(u'String').callprop(u'fromCharCode', (Js(55296)+((var.get(u'cp')-Js(65536))>>Js(10.0))))+var.get(u'String').callprop(u'fromCharCode', (Js(56320)+((var.get(u'cp')-Js(65536))&Js(1023.0))))))
    PyJsHoisted_fromCodePoint_.func_name = u'fromCodePoint'
    var.put(u'fromCodePoint', PyJsHoisted_fromCodePoint_)
    @Js
    def PyJsHoisted_parseExportNamedDeclaration_(node, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'src', u'specifiers', u'isExportFromIdentifier', u'declaration'])
        var.put(u'declaration', var.get(u"null"))
        var.put(u'src', var.get(u"null"))
        var.put(u'specifiers', Js([]))
        if PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Keyword')):
            while 1:
                SWITCHED = False
                CONDITION = (var.get(u'lookahead').get(u'value'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'let')):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'const')):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'var')):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'class')):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'function')):
                    SWITCHED = True
                    var.put(u'declaration', var.get(u'parseStatementListItem')())
                    return var.get(u'node').callprop(u'finishExportNamedDeclaration', var.get(u'declaration'), var.get(u'specifiers'), var.get(u"null"))
                SWITCHED = True
                break
        var.get(u'expect')(Js(u'{'))
        while var.get(u'match')(Js(u'}')).neg():
            var.put(u'isExportFromIdentifier', (var.get(u'isExportFromIdentifier') or var.get(u'matchKeyword')(Js(u'default'))))
            var.get(u'specifiers').callprop(u'push', var.get(u'parseExportSpecifier')())
            if var.get(u'match')(Js(u'}')).neg():
                var.get(u'expect')(Js(u','))
                if var.get(u'match')(Js(u'}')):
                    break
        var.get(u'expect')(Js(u'}'))
        if var.get(u'matchContextualKeyword')(Js(u'from')):
            var.get(u'lex')()
            var.put(u'src', var.get(u'parseModuleSpecifier')())
            var.get(u'consumeSemicolon')()
        else:
            if var.get(u'isExportFromIdentifier'):
                var.get(u'throwError')((var.get(u'Messages').get(u'UnexpectedToken') if var.get(u'lookahead').get(u'value') else var.get(u'Messages').get(u'MissingFromClause')), var.get(u'lookahead').get(u'value'))
            else:
                var.get(u'consumeSemicolon')()
        return var.get(u'node').callprop(u'finishExportNamedDeclaration', var.get(u'declaration'), var.get(u'specifiers'), var.get(u'src'))
    PyJsHoisted_parseExportNamedDeclaration_.func_name = u'parseExportNamedDeclaration'
    var.put(u'parseExportNamedDeclaration', PyJsHoisted_parseExportNamedDeclaration_)
    @Js
    def PyJsHoisted_parseBlock_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'block'])
        var.put(u'node', var.get(u'Node').create())
        var.get(u'expect')(Js(u'{'))
        var.put(u'block', var.get(u'parseStatementList')())
        var.get(u'expect')(Js(u'}'))
        return var.get(u'node').callprop(u'finishBlockStatement', var.get(u'block'))
    PyJsHoisted_parseBlock_.func_name = u'parseBlock'
    var.put(u'parseBlock', PyJsHoisted_parseBlock_)
    @Js
    def PyJsHoisted_parseExportSpecifier_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'local', u'exported', u'def'])
        var.put(u'node', var.get(u'Node').create())
        if var.get(u'matchKeyword')(Js(u'default')):
            var.put(u'def', var.get(u'Node').create())
            var.get(u'lex')()
            var.put(u'local', var.get(u'def').callprop(u'finishIdentifier', Js(u'default')))
        else:
            var.put(u'local', var.get(u'parseVariableIdentifier')())
        if var.get(u'matchContextualKeyword')(Js(u'as')):
            var.get(u'lex')()
            var.put(u'exported', var.get(u'parseNonComputedProperty')())
        return var.get(u'node').callprop(u'finishExportSpecifier', var.get(u'local'), var.get(u'exported'))
    PyJsHoisted_parseExportSpecifier_.func_name = u'parseExportSpecifier'
    var.put(u'parseExportSpecifier', PyJsHoisted_parseExportSpecifier_)
    @Js
    def PyJsHoisted_skipSingleLineComment_(offset, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'offset':offset}, var)
        var.registers([u'comment', u'start', u'ch', u'offset', u'loc'])
        pass
        var.put(u'start', (var.get(u'index')-var.get(u'offset')))
        PyJs_Object_13_ = Js({u'line':var.get(u'lineNumber'),u'column':((var.get(u'index')-var.get(u'lineStart'))-var.get(u'offset'))})
        PyJs_Object_12_ = Js({u'start':PyJs_Object_13_})
        var.put(u'loc', PyJs_Object_12_)
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').callprop(u'charCodeAt', var.get(u'index')))
            var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
            if var.get(u'isLineTerminator')(var.get(u'ch')):
                var.put(u'hasLineTerminator', var.get(u'true'))
                if var.get(u'extra').get(u'comments'):
                    var.put(u'comment', var.get(u'source').callprop(u'slice', (var.get(u'start')+var.get(u'offset')), (var.get(u'index')-Js(1.0))))
                    PyJs_Object_14_ = Js({u'line':var.get(u'lineNumber'),u'column':((var.get(u'index')-var.get(u'lineStart'))-Js(1.0))})
                    var.get(u'loc').put(u'end', PyJs_Object_14_)
                    var.get(u'addComment')(Js(u'Line'), var.get(u'comment'), var.get(u'start'), (var.get(u'index')-Js(1.0)), var.get(u'loc'))
                if (PyJsStrictEq(var.get(u'ch'),Js(13.0)) and PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt', var.get(u'index')),Js(10.0))):
                    var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                var.put(u'lineNumber',Js(var.get(u'lineNumber').to_number())+Js(1))
                var.put(u'lineStart', var.get(u'index'))
                return var.get('undefined')
        if var.get(u'extra').get(u'comments'):
            var.put(u'comment', var.get(u'source').callprop(u'slice', (var.get(u'start')+var.get(u'offset')), var.get(u'index')))
            PyJs_Object_15_ = Js({u'line':var.get(u'lineNumber'),u'column':(var.get(u'index')-var.get(u'lineStart'))})
            var.get(u'loc').put(u'end', PyJs_Object_15_)
            var.get(u'addComment')(Js(u'Line'), var.get(u'comment'), var.get(u'start'), var.get(u'index'), var.get(u'loc'))
    PyJsHoisted_skipSingleLineComment_.func_name = u'skipSingleLineComment'
    var.put(u'skipSingleLineComment', PyJsHoisted_skipSingleLineComment_)
    @Js
    def PyJsHoisted_parseDoWhileStatement_(node, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'arguments':arguments}, var)
        var.registers([u'body', u'test', u'node', u'oldInIteration'])
        pass
        var.get(u'expectKeyword')(Js(u'do'))
        var.put(u'oldInIteration', var.get(u'state').get(u'inIteration'))
        var.get(u'state').put(u'inIteration', var.get(u'true'))
        var.put(u'body', var.get(u'parseStatement')())
        var.get(u'state').put(u'inIteration', var.get(u'oldInIteration'))
        var.get(u'expectKeyword')(Js(u'while'))
        var.get(u'expect')(Js(u'('))
        var.put(u'test', var.get(u'parseExpression')())
        var.get(u'expect')(Js(u')'))
        if var.get(u'match')(Js(u';')):
            var.get(u'lex')()
        return var.get(u'node').callprop(u'finishDoWhileStatement', var.get(u'body'), var.get(u'test'))
    PyJsHoisted_parseDoWhileStatement_.func_name = u'parseDoWhileStatement'
    var.put(u'parseDoWhileStatement', PyJsHoisted_parseDoWhileStatement_)
    @Js
    def PyJsHoisted_codePointAt_(i, this, arguments, var=var):
        var = Scope({u'i':i, u'this':this, u'arguments':arguments}, var)
        var.registers([u'i', u'second', u'cp', u'first'])
        pass
        var.put(u'cp', var.get(u'source').callprop(u'charCodeAt', var.get(u'i')))
        if ((var.get(u'cp')>=Js(55296)) and (var.get(u'cp')<=Js(56319))):
            var.put(u'second', var.get(u'source').callprop(u'charCodeAt', (var.get(u'i')+Js(1.0))))
            if ((var.get(u'second')>=Js(56320)) and (var.get(u'second')<=Js(57343))):
                var.put(u'first', var.get(u'cp'))
                var.put(u'cp', (((((var.get(u'first')-Js(55296))*Js(1024))+var.get(u'second'))-Js(56320))+Js(65536)))
        return var.get(u'cp')
    PyJsHoisted_codePointAt_.func_name = u'codePointAt'
    var.put(u'codePointAt', PyJsHoisted_codePointAt_)
    @Js
    def PyJsHoisted_scanHexEscape_(prefix, this, arguments, var=var):
        var = Scope({u'this':this, u'prefix':prefix, u'arguments':arguments}, var)
        var.registers([u'i', u'prefix', u'ch', u'len', u'code'])
        var.put(u'code', Js(0.0))
        var.put(u'len', (Js(4.0) if PyJsStrictEq(var.get(u'prefix'),Js(u'u')) else Js(2.0)))
        #for JS loop
        var.put(u'i', Js(0.0))
        while (var.get(u'i')<var.get(u'len')):
            try:
                if ((var.get(u'index')<var.get(u'length')) and var.get(u'isHexDigit')(var.get(u'source').get(var.get(u'index')))):
                    var.put(u'ch', var.get(u'source').get((var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1))))
                    var.put(u'code', ((var.get(u'code')*Js(16.0))+Js(u'0123456789abcdef').callprop(u'indexOf', var.get(u'ch').callprop(u'toLowerCase'))))
                else:
                    return Js(u'')
            finally:
                    var.put(u'i',Js(var.get(u'i').to_number())+Js(1))
        return var.get(u'String').callprop(u'fromCharCode', var.get(u'code'))
    PyJsHoisted_scanHexEscape_.func_name = u'scanHexEscape'
    var.put(u'scanHexEscape', PyJsHoisted_scanHexEscape_)
    @Js
    def PyJsHoisted_isHexDigit_(ch, this, arguments, var=var):
        var = Scope({u'this':this, u'ch':ch, u'arguments':arguments}, var)
        var.registers([u'ch'])
        return (Js(u'0123456789abcdefABCDEF').callprop(u'indexOf', var.get(u'ch'))>=Js(0.0))
    PyJsHoisted_isHexDigit_.func_name = u'isHexDigit'
    var.put(u'isHexDigit', PyJsHoisted_isHexDigit_)
    @Js
    def PyJsHoisted_matchContextualKeyword_(keyword, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'keyword':keyword}, var)
        var.registers([u'keyword'])
        return (PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Identifier')) and PyJsStrictEq(var.get(u'lookahead').get(u'value'),var.get(u'keyword')))
    PyJsHoisted_matchContextualKeyword_.func_name = u'matchContextualKeyword'
    var.put(u'matchContextualKeyword', PyJsHoisted_matchContextualKeyword_)
    @Js
    def PyJsHoisted_isStrictModeReservedWord_(id, this, arguments, var=var):
        var = Scope({u'this':this, u'id':id, u'arguments':arguments}, var)
        var.registers([u'id'])
        while 1:
            SWITCHED = False
            CONDITION = (var.get(u'id'))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'implements')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'interface')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'package')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'private')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'protected')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'public')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'static')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'yield')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'let')):
                SWITCHED = True
                return var.get(u'true')
            if True:
                SWITCHED = True
                return Js(False)
            SWITCHED = True
            break
    PyJsHoisted_isStrictModeReservedWord_.func_name = u'isStrictModeReservedWord'
    var.put(u'isStrictModeReservedWord', PyJsHoisted_isStrictModeReservedWord_)
    @Js
    def PyJsHoisted_binaryPrecedence_(token, allowIn, this, arguments, var=var):
        var = Scope({u'this':this, u'allowIn':allowIn, u'token':token, u'arguments':arguments}, var)
        var.registers([u'allowIn', u'token', u'prec'])
        var.put(u'prec', Js(0.0))
        if (PyJsStrictNeq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Punctuator')) and PyJsStrictNeq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Keyword'))):
            return Js(0.0)
        while 1:
            SWITCHED = False
            CONDITION = (var.get(u'token').get(u'value'))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'||')):
                SWITCHED = True
                var.put(u'prec', Js(1.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'&&')):
                SWITCHED = True
                var.put(u'prec', Js(2.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'|')):
                SWITCHED = True
                var.put(u'prec', Js(3.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'^')):
                SWITCHED = True
                var.put(u'prec', Js(4.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'&')):
                SWITCHED = True
                var.put(u'prec', Js(5.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'==')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'!=')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'===')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'!==')):
                SWITCHED = True
                var.put(u'prec', Js(6.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'<')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'>')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'<=')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'>=')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'instanceof')):
                SWITCHED = True
                var.put(u'prec', Js(7.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'in')):
                SWITCHED = True
                var.put(u'prec', (Js(7.0) if var.get(u'allowIn') else Js(0.0)))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'<<')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'>>')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'>>>')):
                SWITCHED = True
                var.put(u'prec', Js(8.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'+')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'-')):
                SWITCHED = True
                var.put(u'prec', Js(9.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'*')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'/')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'%')):
                SWITCHED = True
                var.put(u'prec', Js(11.0))
                break
            if True:
                SWITCHED = True
                break
            SWITCHED = True
            break
        return var.get(u'prec')
    PyJsHoisted_binaryPrecedence_.func_name = u'binaryPrecedence'
    var.put(u'binaryPrecedence', PyJsHoisted_binaryPrecedence_)
    @Js
    def PyJsHoisted_parse_(code, options, this, arguments, var=var):
        var = Scope({u'this':this, u'code':code, u'options':options, u'arguments':arguments}, var)
        var.registers([u'code', u'program', u'toString', u'options'])
        pass
        var.put(u'toString', var.get(u'String'))
        if (PyJsStrictNeq(var.get(u'code',throw=False).typeof(),Js(u'string')) and var.get(u'code').instanceof(var.get(u'String')).neg()):
            var.put(u'code', var.get(u'toString')(var.get(u'code')))
        var.put(u'source', var.get(u'code'))
        var.put(u'index', Js(0.0))
        var.put(u'lineNumber', (Js(1.0) if (var.get(u'source').get(u'length')>Js(0.0)) else Js(0.0)))
        var.put(u'lineStart', Js(0.0))
        var.put(u'startIndex', var.get(u'index'))
        var.put(u'startLineNumber', var.get(u'lineNumber'))
        var.put(u'startLineStart', var.get(u'lineStart'))
        var.put(u'length', var.get(u'source').get(u'length'))
        var.put(u'lookahead', var.get(u"null"))
        PyJs_Object_157_ = Js({})
        PyJs_Object_156_ = Js({u'allowIn':var.get(u'true'),u'allowYield':var.get(u'true'),u'labelSet':PyJs_Object_157_,u'inFunctionBody':Js(False),u'inIteration':Js(False),u'inSwitch':Js(False),u'lastCommentStart':(-Js(1.0)),u'curlyStack':Js([]),u'sourceType':Js(u'script')})
        var.put(u'state', PyJs_Object_156_)
        var.put(u'strict', Js(False))
        PyJs_Object_158_ = Js({})
        var.put(u'extra', PyJs_Object_158_)
        if PyJsStrictNeq(var.get(u'options',throw=False).typeof(),Js(u'undefined')):
            var.get(u'extra').put(u'range', (PyJsStrictEq(var.get(u'options').get(u'range').typeof(),Js(u'boolean')) and var.get(u'options').get(u'range')))
            var.get(u'extra').put(u'loc', (PyJsStrictEq(var.get(u'options').get(u'loc').typeof(),Js(u'boolean')) and var.get(u'options').get(u'loc')))
            var.get(u'extra').put(u'attachComment', (PyJsStrictEq(var.get(u'options').get(u'attachComment').typeof(),Js(u'boolean')) and var.get(u'options').get(u'attachComment')))
            if ((var.get(u'extra').get(u'loc') and PyJsStrictNeq(var.get(u'options').get(u'source'),var.get(u"null"))) and PyJsStrictNeq(var.get(u'options').get(u'source'),var.get(u'undefined'))):
                var.get(u'extra').put(u'source', var.get(u'toString')(var.get(u'options').get(u'source')))
            if (PyJsStrictEq(var.get(u'options').get(u'tokens').typeof(),Js(u'boolean')) and var.get(u'options').get(u'tokens')):
                var.get(u'extra').put(u'tokens', Js([]))
            if (PyJsStrictEq(var.get(u'options').get(u'comment').typeof(),Js(u'boolean')) and var.get(u'options').get(u'comment')):
                var.get(u'extra').put(u'comments', Js([]))
            if (PyJsStrictEq(var.get(u'options').get(u'tolerant').typeof(),Js(u'boolean')) and var.get(u'options').get(u'tolerant')):
                var.get(u'extra').put(u'errors', Js([]))
            if var.get(u'extra').get(u'attachComment'):
                var.get(u'extra').put(u'range', var.get(u'true'))
                var.get(u'extra').put(u'comments', Js([]))
                var.get(u'extra').put(u'bottomRightStack', Js([]))
                var.get(u'extra').put(u'trailingComments', Js([]))
                var.get(u'extra').put(u'leadingComments', Js([]))
            if PyJsStrictEq(var.get(u'options').get(u'sourceType'),Js(u'module')):
                var.get(u'state').put(u'sourceType', var.get(u'options').get(u'sourceType'))
                var.put(u'strict', var.get(u'true'))
        try:
            var.put(u'program', var.get(u'parseProgram')())
            if PyJsStrictNeq(var.get(u'extra').get(u'comments').typeof(),Js(u'undefined')):
                var.get(u'program').put(u'comments', var.get(u'extra').get(u'comments'))
            if PyJsStrictNeq(var.get(u'extra').get(u'tokens').typeof(),Js(u'undefined')):
                var.get(u'filterTokenLocation')()
                var.get(u'program').put(u'tokens', var.get(u'extra').get(u'tokens'))
            if PyJsStrictNeq(var.get(u'extra').get(u'errors').typeof(),Js(u'undefined')):
                var.get(u'program').put(u'errors', var.get(u'extra').get(u'errors'))
        except PyJsException as PyJsTempException:
            PyJsHolder_65_51248354 = var.own.get(u'e')
            var.force_own_put(u'e', PyExceptionToJs(PyJsTempException))
            try:
                PyJsTempException = JsToPyException(var.get(u'e'))
                raise PyJsTempException
            finally:
                if PyJsHolder_65_51248354 is not None:
                    var.own[u'e'] = PyJsHolder_65_51248354
                else:
                    del var.own[u'e']
                del PyJsHolder_65_51248354
        finally:
            PyJs_Object_159_ = Js({})
            var.put(u'extra', PyJs_Object_159_)
        return var.get(u'program')
    PyJsHoisted_parse_.func_name = u'parse'
    var.put(u'parse', PyJsHoisted_parse_)
    @Js
    def PyJsHoisted_matchAssign_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'op'])
        pass
        if PyJsStrictNeq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Punctuator')):
            return Js(False)
        var.put(u'op', var.get(u'lookahead').get(u'value'))
        def PyJs_LONG_122_(var=var):
            return (((((((((PyJsStrictEq(var.get(u'op'),Js(u'=')) or PyJsStrictEq(var.get(u'op'),Js(u'*='))) or PyJsStrictEq(var.get(u'op'),Js(u'/='))) or PyJsStrictEq(var.get(u'op'),Js(u'%='))) or PyJsStrictEq(var.get(u'op'),Js(u'+='))) or PyJsStrictEq(var.get(u'op'),Js(u'-='))) or PyJsStrictEq(var.get(u'op'),Js(u'<<='))) or PyJsStrictEq(var.get(u'op'),Js(u'>>='))) or PyJsStrictEq(var.get(u'op'),Js(u'>>>='))) or PyJsStrictEq(var.get(u'op'),Js(u'&=')))
        return ((PyJs_LONG_122_() or PyJsStrictEq(var.get(u'op'),Js(u'^='))) or PyJsStrictEq(var.get(u'op'),Js(u'|=')))
    PyJsHoisted_matchAssign_.func_name = u'matchAssign'
    var.put(u'matchAssign', PyJsHoisted_matchAssign_)
    @Js
    def PyJsHoisted_WrappingNode_(startToken, this, arguments, var=var):
        var = Scope({u'this':this, u'startToken':startToken, u'arguments':arguments}, var)
        var.registers([u'startToken'])
        if var.get(u'extra').get(u'range'):
            var.get(u"this").put(u'range', Js([var.get(u'startToken').get(u'start'), Js(0.0)]))
        if var.get(u'extra').get(u'loc'):
            var.get(u"this").put(u'loc', var.get(u'WrappingSourceLocation').create(var.get(u'startToken')))
    PyJsHoisted_WrappingNode_.func_name = u'WrappingNode'
    var.put(u'WrappingNode', PyJsHoisted_WrappingNode_)
    @Js
    def PyJsHoisted_parseObjectInitializer_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'hasProto', u'properties'])
        var.put(u'properties', Js([]))
        PyJs_Object_126_ = Js({u'value':Js(False)})
        var.put(u'hasProto', PyJs_Object_126_)
        var.put(u'node', var.get(u'Node').create())
        var.get(u'expect')(Js(u'{'))
        while var.get(u'match')(Js(u'}')).neg():
            var.get(u'properties').callprop(u'push', var.get(u'parseObjectProperty')(var.get(u'hasProto')))
            if var.get(u'match')(Js(u'}')).neg():
                var.get(u'expectCommaSeparator')()
        var.get(u'expect')(Js(u'}'))
        return var.get(u'node').callprop(u'finishObjectExpression', var.get(u'properties'))
    PyJsHoisted_parseObjectInitializer_.func_name = u'parseObjectInitializer'
    var.put(u'parseObjectInitializer', PyJsHoisted_parseObjectInitializer_)
    @Js
    def PyJsHoisted_getIdentifier_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'start', u'ch'])
        pass
        var.put(u'start', (var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1)))
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').callprop(u'charCodeAt', var.get(u'index')))
            if PyJsStrictEq(var.get(u'ch'),Js(92)):
                var.put(u'index', var.get(u'start'))
                return var.get(u'getComplexIdentifier')()
            else:
                if ((var.get(u'ch')>=Js(55296)) and (var.get(u'ch')<Js(57343))):
                    var.put(u'index', var.get(u'start'))
                    return var.get(u'getComplexIdentifier')()
            if var.get(u'isIdentifierPart')(var.get(u'ch')):
                var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
            else:
                break
        return var.get(u'source').callprop(u'slice', var.get(u'start'), var.get(u'index'))
    PyJsHoisted_getIdentifier_.func_name = u'getIdentifier'
    var.put(u'getIdentifier', PyJsHoisted_getIdentifier_)
    @Js
    def PyJsHoisted_isRestrictedWord_(id, this, arguments, var=var):
        var = Scope({u'this':this, u'id':id, u'arguments':arguments}, var)
        var.registers([u'id'])
        return (PyJsStrictEq(var.get(u'id'),Js(u'eval')) or PyJsStrictEq(var.get(u'id'),Js(u'arguments')))
    PyJsHoisted_isRestrictedWord_.func_name = u'isRestrictedWord'
    var.put(u'isRestrictedWord', PyJsHoisted_isRestrictedWord_)
    @Js
    def PyJsHoisted_parseSwitchCase_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'test', u'node', u'statement', u'consequent'])
        var.put(u'consequent', Js([]))
        var.put(u'node', var.get(u'Node').create())
        if var.get(u'matchKeyword')(Js(u'default')):
            var.get(u'lex')()
            var.put(u'test', var.get(u"null"))
        else:
            var.get(u'expectKeyword')(Js(u'case'))
            var.put(u'test', var.get(u'parseExpression')())
        var.get(u'expect')(Js(u':'))
        while (var.get(u'startIndex')<var.get(u'length')):
            if ((var.get(u'match')(Js(u'}')) or var.get(u'matchKeyword')(Js(u'default'))) or var.get(u'matchKeyword')(Js(u'case'))):
                break
            var.put(u'statement', var.get(u'parseStatementListItem')())
            var.get(u'consequent').callprop(u'push', var.get(u'statement'))
        return var.get(u'node').callprop(u'finishSwitchCase', var.get(u'test'), var.get(u'consequent'))
    PyJsHoisted_parseSwitchCase_.func_name = u'parseSwitchCase'
    var.put(u'parseSwitchCase', PyJsHoisted_parseSwitchCase_)
    @Js
    def PyJsHoisted_parsePropertyPattern_(params, kind, this, arguments, var=var):
        var = Scope({u'this':this, u'kind':kind, u'params':params, u'arguments':arguments}, var)
        var.registers([u'node', u'kind', u'computed', u'init', u'params', u'key', u'keyToken'])
        var.put(u'node', var.get(u'Node').create())
        var.put(u'computed', var.get(u'match')(Js(u'[')))
        if PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Identifier')):
            var.put(u'keyToken', var.get(u'lookahead'))
            var.put(u'key', var.get(u'parseVariableIdentifier')())
            if var.get(u'match')(Js(u'=')):
                var.get(u'params').callprop(u'push', var.get(u'keyToken'))
                var.get(u'lex')()
                var.put(u'init', var.get(u'parseAssignmentExpression')())
                return var.get(u'node').callprop(u'finishProperty', Js(u'init'), var.get(u'key'), Js(False), var.get(u'WrappingNode').create(var.get(u'keyToken')).callprop(u'finishAssignmentPattern', var.get(u'key'), var.get(u'init')), Js(False), Js(False))
            else:
                if var.get(u'match')(Js(u':')).neg():
                    var.get(u'params').callprop(u'push', var.get(u'keyToken'))
                    return var.get(u'node').callprop(u'finishProperty', Js(u'init'), var.get(u'key'), Js(False), var.get(u'key'), Js(False), var.get(u'true'))
        else:
            var.put(u'key', var.get(u'parseObjectPropertyKey')(var.get(u'params'), var.get(u'kind')))
        var.get(u'expect')(Js(u':'))
        var.put(u'init', var.get(u'parsePatternWithDefault')(var.get(u'params'), var.get(u'kind')))
        return var.get(u'node').callprop(u'finishProperty', Js(u'init'), var.get(u'key'), var.get(u'computed'), var.get(u'init'), Js(False), Js(False))
    PyJsHoisted_parsePropertyPattern_.func_name = u'parsePropertyPattern'
    var.put(u'parsePropertyPattern', PyJsHoisted_parsePropertyPattern_)
    @Js
    def PyJsHoisted_parseFunctionDeclaration_(node, identifierIsOptional, this, arguments, var=var):
        var = Scope({u'node':node, u'identifierIsOptional':identifierIsOptional, u'this':this, u'arguments':arguments}, var)
        var.registers([u'body', u'tmp', u'previousStrict', u'node', u'identifierIsOptional', u'isGenerator', u'message', u'stricted', u'token', u'params', u'defaults', u'previousAllowYield', u'firstRestricted', u'id'])
        var.put(u'id', var.get(u"null"))
        var.put(u'params', Js([]))
        var.put(u'defaults', Js([]))
        var.put(u'previousAllowYield', var.get(u'state').get(u'allowYield'))
        var.get(u'expectKeyword')(Js(u'function'))
        var.put(u'isGenerator', var.get(u'match')(Js(u'*')))
        if var.get(u'isGenerator'):
            var.get(u'lex')()
        if (var.get(u'identifierIsOptional').neg() or var.get(u'match')(Js(u'(')).neg()):
            var.put(u'token', var.get(u'lookahead'))
            var.put(u'id', var.get(u'parseVariableIdentifier')())
            if var.get(u'strict'):
                if var.get(u'isRestrictedWord')(var.get(u'token').get(u'value')):
                    var.get(u'tolerateUnexpectedToken')(var.get(u'token'), var.get(u'Messages').get(u'StrictFunctionName'))
            else:
                if var.get(u'isRestrictedWord')(var.get(u'token').get(u'value')):
                    var.put(u'firstRestricted', var.get(u'token'))
                    var.put(u'message', var.get(u'Messages').get(u'StrictFunctionName'))
                else:
                    if var.get(u'isStrictModeReservedWord')(var.get(u'token').get(u'value')):
                        var.put(u'firstRestricted', var.get(u'token'))
                        var.put(u'message', var.get(u'Messages').get(u'StrictReservedWord'))
        var.get(u'state').put(u'allowYield', var.get(u'isGenerator').neg())
        var.put(u'tmp', var.get(u'parseParams')(var.get(u'firstRestricted')))
        var.put(u'params', var.get(u'tmp').get(u'params'))
        var.put(u'defaults', var.get(u'tmp').get(u'defaults'))
        var.put(u'stricted', var.get(u'tmp').get(u'stricted'))
        var.put(u'firstRestricted', var.get(u'tmp').get(u'firstRestricted'))
        if var.get(u'tmp').get(u'message'):
            var.put(u'message', var.get(u'tmp').get(u'message'))
        var.put(u'previousStrict', var.get(u'strict'))
        var.put(u'body', var.get(u'parseFunctionSourceElements')())
        if (var.get(u'strict') and var.get(u'firstRestricted')):
            var.get(u'throwUnexpectedToken')(var.get(u'firstRestricted'), var.get(u'message'))
        if (var.get(u'strict') and var.get(u'stricted')):
            var.get(u'tolerateUnexpectedToken')(var.get(u'stricted'), var.get(u'message'))
        var.put(u'strict', var.get(u'previousStrict'))
        var.get(u'state').put(u'allowYield', var.get(u'previousAllowYield'))
        return var.get(u'node').callprop(u'finishFunctionDeclaration', var.get(u'id'), var.get(u'params'), var.get(u'defaults'), var.get(u'body'), var.get(u'isGenerator'))
    PyJsHoisted_parseFunctionDeclaration_.func_name = u'parseFunctionDeclaration'
    var.put(u'parseFunctionDeclaration', PyJsHoisted_parseFunctionDeclaration_)
    @Js
    def PyJsHoisted_parsePostfixExpression_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'expr', u'token', u'startToken'])
        var.put(u'startToken', var.get(u'lookahead'))
        var.put(u'expr', var.get(u'inheritCoverGrammar')(var.get(u'parseLeftHandSideExpressionAllowCall')))
        if (var.get(u'hasLineTerminator').neg() and PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Punctuator'))):
            if (var.get(u'match')(Js(u'++')) or var.get(u'match')(Js(u'--'))):
                if ((var.get(u'strict') and PyJsStrictEq(var.get(u'expr').get(u'type'),var.get(u'Syntax').get(u'Identifier'))) and var.get(u'isRestrictedWord')(var.get(u'expr').get(u'name'))):
                    var.get(u'tolerateError')(var.get(u'Messages').get(u'StrictLHSPostfix'))
                if var.get(u'isAssignmentTarget').neg():
                    var.get(u'tolerateError')(var.get(u'Messages').get(u'InvalidLHSInAssignment'))
                var.put(u'isAssignmentTarget', var.put(u'isBindingElement', Js(False)))
                var.put(u'token', var.get(u'lex')())
                var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishPostfixExpression', var.get(u'token').get(u'value'), var.get(u'expr')))
        return var.get(u'expr')
    PyJsHoisted_parsePostfixExpression_.func_name = u'parsePostfixExpression'
    var.put(u'parsePostfixExpression', PyJsHoisted_parsePostfixExpression_)
    @Js
    def PyJsHoisted_parseNonComputedMember_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        var.get(u'expect')(Js(u'.'))
        return var.get(u'parseNonComputedProperty')()
    PyJsHoisted_parseNonComputedMember_.func_name = u'parseNonComputedMember'
    var.put(u'parseNonComputedMember', PyJsHoisted_parseNonComputedMember_)
    @Js
    def PyJsHoisted_parseExportDefaultDeclaration_(node, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'expression', u'declaration'])
        var.put(u'declaration', var.get(u"null"))
        var.put(u'expression', var.get(u"null"))
        var.get(u'expectKeyword')(Js(u'default'))
        if var.get(u'matchKeyword')(Js(u'function')):
            var.put(u'declaration', var.get(u'parseFunctionDeclaration')(var.get(u'Node').create(), var.get(u'true')))
            return var.get(u'node').callprop(u'finishExportDefaultDeclaration', var.get(u'declaration'))
        if var.get(u'matchKeyword')(Js(u'class')):
            var.put(u'declaration', var.get(u'parseClassDeclaration')(var.get(u'true')))
            return var.get(u'node').callprop(u'finishExportDefaultDeclaration', var.get(u'declaration'))
        if var.get(u'matchContextualKeyword')(Js(u'from')):
            var.get(u'throwError')(var.get(u'Messages').get(u'UnexpectedToken'), var.get(u'lookahead').get(u'value'))
        if var.get(u'match')(Js(u'{')):
            var.put(u'expression', var.get(u'parseObjectInitializer')())
        else:
            if var.get(u'match')(Js(u'[')):
                var.put(u'expression', var.get(u'parseArrayInitializer')())
            else:
                var.put(u'expression', var.get(u'parseAssignmentExpression')())
        var.get(u'consumeSemicolon')()
        return var.get(u'node').callprop(u'finishExportDefaultDeclaration', var.get(u'expression'))
    PyJsHoisted_parseExportDefaultDeclaration_.func_name = u'parseExportDefaultDeclaration'
    var.put(u'parseExportDefaultDeclaration', PyJsHoisted_parseExportDefaultDeclaration_)
    @Js
    def PyJsHoisted_parseRestElement_(params, this, arguments, var=var):
        var = Scope({u'this':this, u'params':params, u'arguments':arguments}, var)
        var.registers([u'node', u'params', u'param'])
        var.put(u'node', var.get(u'Node').create())
        var.get(u'lex')()
        if var.get(u'match')(Js(u'{')):
            var.get(u'throwError')(var.get(u'Messages').get(u'ObjectPatternAsRestParameter'))
        var.get(u'params').callprop(u'push', var.get(u'lookahead'))
        var.put(u'param', var.get(u'parseVariableIdentifier')())
        if var.get(u'match')(Js(u'=')):
            var.get(u'throwError')(var.get(u'Messages').get(u'DefaultRestParameter'))
        if var.get(u'match')(Js(u')')).neg():
            var.get(u'throwError')(var.get(u'Messages').get(u'ParameterAfterRestParameter'))
        return var.get(u'node').callprop(u'finishRestElement', var.get(u'param'))
    PyJsHoisted_parseRestElement_.func_name = u'parseRestElement'
    var.put(u'parseRestElement', PyJsHoisted_parseRestElement_)
    @Js
    def PyJsHoisted_parseScriptBody_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'body', u'firstRestricted', u'token', u'directive', u'statement'])
        var.put(u'body', Js([]))
        while (var.get(u'startIndex')<var.get(u'length')):
            var.put(u'token', var.get(u'lookahead'))
            if PyJsStrictNeq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'StringLiteral')):
                break
            var.put(u'statement', var.get(u'parseStatementListItem')())
            var.get(u'body').callprop(u'push', var.get(u'statement'))
            if PyJsStrictNeq(var.get(u'statement').get(u'expression').get(u'type'),var.get(u'Syntax').get(u'Literal')):
                break
            var.put(u'directive', var.get(u'source').callprop(u'slice', (var.get(u'token').get(u'start')+Js(1.0)), (var.get(u'token').get(u'end')-Js(1.0))))
            if PyJsStrictEq(var.get(u'directive'),Js(u'use strict')):
                var.put(u'strict', var.get(u'true'))
                if var.get(u'firstRestricted'):
                    var.get(u'tolerateUnexpectedToken')(var.get(u'firstRestricted'), var.get(u'Messages').get(u'StrictOctalLiteral'))
            else:
                if (var.get(u'firstRestricted').neg() and var.get(u'token').get(u'octal')):
                    var.put(u'firstRestricted', var.get(u'token'))
        while (var.get(u'startIndex')<var.get(u'length')):
            var.put(u'statement', var.get(u'parseStatementListItem')())
            if PyJsStrictEq(var.get(u'statement',throw=False).typeof(),Js(u'undefined')):
                break
            var.get(u'body').callprop(u'push', var.get(u'statement'))
        return var.get(u'body')
    PyJsHoisted_parseScriptBody_.func_name = u'parseScriptBody'
    var.put(u'parseScriptBody', PyJsHoisted_parseScriptBody_)
    @Js
    def PyJsHoisted_parseBindingList_(kind, options, this, arguments, var=var):
        var = Scope({u'this':this, u'kind':kind, u'options':options, u'arguments':arguments}, var)
        var.registers([u'kind', u'list', u'options'])
        var.put(u'list', Js([]))
        while 1:
            var.get(u'list').callprop(u'push', var.get(u'parseLexicalBinding')(var.get(u'kind'), var.get(u'options')))
            if var.get(u'match')(Js(u',')).neg():
                break
            var.get(u'lex')()
            if not (var.get(u'startIndex')<var.get(u'length')):
                break
        return var.get(u'list')
    PyJsHoisted_parseBindingList_.func_name = u'parseBindingList'
    var.put(u'parseBindingList', PyJsHoisted_parseBindingList_)
    @Js
    def PyJsHoisted_scanTemplate_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'terminated', u'rawOffset', u'ch', u'start', u'unescaped', u'head', u'cooked', u'tail', u'restore'])
        var.put(u'cooked', Js(u''))
        var.put(u'terminated', Js(False))
        var.put(u'tail', Js(False))
        var.put(u'start', var.get(u'index'))
        var.put(u'head', PyJsStrictEq(var.get(u'source').get(var.get(u'index')),Js(u'`')))
        var.put(u'rawOffset', Js(2.0))
        var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').get((var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1))))
            if PyJsStrictEq(var.get(u'ch'),Js(u'`')):
                var.put(u'rawOffset', Js(1.0))
                var.put(u'tail', var.get(u'true'))
                var.put(u'terminated', var.get(u'true'))
                break
            else:
                if PyJsStrictEq(var.get(u'ch'),Js(u'$')):
                    if PyJsStrictEq(var.get(u'source').get(var.get(u'index')),Js(u'{')):
                        var.get(u'state').get(u'curlyStack').callprop(u'push', Js(u'${'))
                        var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                        var.put(u'terminated', var.get(u'true'))
                        break
                    var.put(u'cooked', var.get(u'ch'), u'+')
                else:
                    if PyJsStrictEq(var.get(u'ch'),Js(u'\\')):
                        var.put(u'ch', var.get(u'source').get((var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1))))
                        if var.get(u'isLineTerminator')(var.get(u'ch').callprop(u'charCodeAt', Js(0.0))).neg():
                            while 1:
                                SWITCHED = False
                                CONDITION = (var.get(u'ch'))
                                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'n')):
                                    SWITCHED = True
                                    var.put(u'cooked', Js(u'\n'), u'+')
                                    break
                                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'r')):
                                    SWITCHED = True
                                    var.put(u'cooked', Js(u'\r'), u'+')
                                    break
                                if SWITCHED or PyJsStrictEq(CONDITION, Js(u't')):
                                    SWITCHED = True
                                    var.put(u'cooked', Js(u'\t'), u'+')
                                    break
                                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'u')):
                                    SWITCHED = True
                                    pass
                                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'x')):
                                    SWITCHED = True
                                    if PyJsStrictEq(var.get(u'source').get(var.get(u'index')),Js(u'{')):
                                        var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                                        var.put(u'cooked', var.get(u'scanUnicodeCodePointEscape')(), u'+')
                                    else:
                                        var.put(u'restore', var.get(u'index'))
                                        var.put(u'unescaped', var.get(u'scanHexEscape')(var.get(u'ch')))
                                        if var.get(u'unescaped'):
                                            var.put(u'cooked', var.get(u'unescaped'), u'+')
                                        else:
                                            var.put(u'index', var.get(u'restore'))
                                            var.put(u'cooked', var.get(u'ch'), u'+')
                                    break
                                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'b')):
                                    SWITCHED = True
                                    var.put(u'cooked', Js(u'\x08'), u'+')
                                    break
                                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'f')):
                                    SWITCHED = True
                                    var.put(u'cooked', Js(u'\x0c'), u'+')
                                    break
                                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'v')):
                                    SWITCHED = True
                                    var.put(u'cooked', Js(u'\x0b'), u'+')
                                    break
                                if True:
                                    SWITCHED = True
                                    if PyJsStrictEq(var.get(u'ch'),Js(u'0')):
                                        if var.get(u'isDecimalDigit')(var.get(u'source').callprop(u'charCodeAt', var.get(u'index'))):
                                            var.get(u'throwError')(var.get(u'Messages').get(u'TemplateOctalLiteral'))
                                        var.put(u'cooked', Js(u'\x00'), u'+')
                                    else:
                                        if var.get(u'isOctalDigit')(var.get(u'ch')):
                                            var.get(u'throwError')(var.get(u'Messages').get(u'TemplateOctalLiteral'))
                                        else:
                                            var.put(u'cooked', var.get(u'ch'), u'+')
                                    break
                                SWITCHED = True
                                break
                        else:
                            var.put(u'lineNumber',Js(var.get(u'lineNumber').to_number())+Js(1))
                            if (PyJsStrictEq(var.get(u'ch'),Js(u'\r')) and PyJsStrictEq(var.get(u'source').get(var.get(u'index')),Js(u'\n'))):
                                var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                            var.put(u'lineStart', var.get(u'index'))
                    else:
                        if var.get(u'isLineTerminator')(var.get(u'ch').callprop(u'charCodeAt', Js(0.0))):
                            var.put(u'lineNumber',Js(var.get(u'lineNumber').to_number())+Js(1))
                            if (PyJsStrictEq(var.get(u'ch'),Js(u'\r')) and PyJsStrictEq(var.get(u'source').get(var.get(u'index')),Js(u'\n'))):
                                var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                            var.put(u'lineStart', var.get(u'index'))
                            var.put(u'cooked', Js(u'\n'), u'+')
                        else:
                            var.put(u'cooked', var.get(u'ch'), u'+')
        if var.get(u'terminated').neg():
            var.get(u'throwUnexpectedToken')()
        if var.get(u'head').neg():
            var.get(u'state').get(u'curlyStack').callprop(u'pop')
        PyJs_Object_30_ = Js({u'cooked':var.get(u'cooked'),u'raw':var.get(u'source').callprop(u'slice', (var.get(u'start')+Js(1.0)), (var.get(u'index')-var.get(u'rawOffset')))})
        PyJs_Object_29_ = Js({u'type':var.get(u'Token').get(u'Template'),u'value':PyJs_Object_30_,u'head':var.get(u'head'),u'tail':var.get(u'tail'),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
        return PyJs_Object_29_
    PyJsHoisted_scanTemplate_.func_name = u'scanTemplate'
    var.put(u'scanTemplate', PyJsHoisted_scanTemplate_)
    @Js
    def PyJsHoisted_parseLexicalDeclaration_(options, this, arguments, var=var):
        var = Scope({u'this':this, u'options':options, u'arguments':arguments}, var)
        var.registers([u'node', u'kind', u'declarations', u'options'])
        var.put(u'node', var.get(u'Node').create())
        var.put(u'kind', var.get(u'lex')().get(u'value'))
        var.get(u'assert')((PyJsStrictEq(var.get(u'kind'),Js(u'let')) or PyJsStrictEq(var.get(u'kind'),Js(u'const'))), Js(u'Lexical declaration must be either let or const'))
        var.put(u'declarations', var.get(u'parseBindingList')(var.get(u'kind'), var.get(u'options')))
        var.get(u'consumeSemicolon')()
        return var.get(u'node').callprop(u'finishLexicalDeclaration', var.get(u'declarations'), var.get(u'kind'))
    PyJsHoisted_parseLexicalDeclaration_.func_name = u'parseLexicalDeclaration'
    var.put(u'parseLexicalDeclaration', PyJsHoisted_parseLexicalDeclaration_)
    @Js
    def PyJsHoisted_checkPatternParam_(options, param, this, arguments, var=var):
        var = Scope({u'this':this, u'options':options, u'param':param, u'arguments':arguments}, var)
        var.registers([u'i', u'options', u'param'])
        pass
        while 1:
            SWITCHED = False
            CONDITION = (var.get(u'param').get(u'type'))
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Syntax').get(u'Identifier')):
                SWITCHED = True
                var.get(u'validateParam')(var.get(u'options'), var.get(u'param'), var.get(u'param').get(u'name'))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Syntax').get(u'RestElement')):
                SWITCHED = True
                var.get(u'checkPatternParam')(var.get(u'options'), var.get(u'param').get(u'argument'))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Syntax').get(u'AssignmentPattern')):
                SWITCHED = True
                var.get(u'checkPatternParam')(var.get(u'options'), var.get(u'param').get(u'left'))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Syntax').get(u'ArrayPattern')):
                SWITCHED = True
                #for JS loop
                var.put(u'i', Js(0.0))
                while (var.get(u'i')<var.get(u'param').get(u'elements').get(u'length')):
                    try:
                        if PyJsStrictNeq(var.get(u'param').get(u'elements').get(var.get(u'i')),var.get(u"null")):
                            var.get(u'checkPatternParam')(var.get(u'options'), var.get(u'param').get(u'elements').get(var.get(u'i')))
                    finally:
                            (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Syntax').get(u'YieldExpression')):
                SWITCHED = True
                break
            if True:
                SWITCHED = True
                var.get(u'assert')(PyJsStrictEq(var.get(u'param').get(u'type'),var.get(u'Syntax').get(u'ObjectPattern')), Js(u'Invalid type'))
                #for JS loop
                var.put(u'i', Js(0.0))
                while (var.get(u'i')<var.get(u'param').get(u'properties').get(u'length')):
                    try:
                        var.get(u'checkPatternParam')(var.get(u'options'), var.get(u'param').get(u'properties').get(var.get(u'i')).get(u'value'))
                    finally:
                            (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
                break
            SWITCHED = True
            break
    PyJsHoisted_checkPatternParam_.func_name = u'checkPatternParam'
    var.put(u'checkPatternParam', PyJsHoisted_checkPatternParam_)
    @Js
    def PyJsHoisted_parsePropertyFunction_(node, paramInfo, isGenerator, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'paramInfo':paramInfo, u'isGenerator':isGenerator, u'arguments':arguments}, var)
        var.registers([u'body', u'node', u'previousStrict', u'isGenerator', u'paramInfo'])
        pass
        var.put(u'isAssignmentTarget', var.put(u'isBindingElement', Js(False)))
        var.put(u'previousStrict', var.get(u'strict'))
        var.put(u'body', var.get(u'isolateCoverGrammar')(var.get(u'parseFunctionSourceElements')))
        if (var.get(u'strict') and var.get(u'paramInfo').get(u'firstRestricted')):
            var.get(u'tolerateUnexpectedToken')(var.get(u'paramInfo').get(u'firstRestricted'), var.get(u'paramInfo').get(u'message'))
        if (var.get(u'strict') and var.get(u'paramInfo').get(u'stricted')):
            var.get(u'tolerateUnexpectedToken')(var.get(u'paramInfo').get(u'stricted'), var.get(u'paramInfo').get(u'message'))
        var.put(u'strict', var.get(u'previousStrict'))
        return var.get(u'node').callprop(u'finishFunctionExpression', var.get(u"null"), var.get(u'paramInfo').get(u'params'), var.get(u'paramInfo').get(u'defaults'), var.get(u'body'), var.get(u'isGenerator'))
    PyJsHoisted_parsePropertyFunction_.func_name = u'parsePropertyFunction'
    var.put(u'parsePropertyFunction', PyJsHoisted_parsePropertyFunction_)
    @Js
    def PyJsHoisted_scanPunctuator_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'token', u'str'])
        pass
        PyJs_Object_21_ = Js({u'type':var.get(u'Token').get(u'Punctuator'),u'value':Js(u''),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'index'),u'end':var.get(u'index')})
        var.put(u'token', PyJs_Object_21_)
        var.put(u'str', var.get(u'source').get(var.get(u'index')))
        while 1:
            SWITCHED = False
            CONDITION = (var.get(u'str'))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'(')):
                SWITCHED = True
                if var.get(u'extra').get(u'tokenize'):
                    var.get(u'extra').put(u'openParenToken', var.get(u'extra').get(u'tokens').get(u'length'))
                var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'{')):
                SWITCHED = True
                if var.get(u'extra').get(u'tokenize'):
                    var.get(u'extra').put(u'openCurlyToken', var.get(u'extra').get(u'tokens').get(u'length'))
                var.get(u'state').get(u'curlyStack').callprop(u'push', Js(u'{'))
                var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'.')):
                SWITCHED = True
                var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                if (PyJsStrictEq(var.get(u'source').get(var.get(u'index')),Js(u'.')) and PyJsStrictEq(var.get(u'source').get((var.get(u'index')+Js(1.0))),Js(u'.'))):
                    var.put(u'index', Js(2.0), u'+')
                    var.put(u'str', Js(u'...'))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'}')):
                SWITCHED = True
                var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                var.get(u'state').get(u'curlyStack').callprop(u'pop')
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u')')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u';')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u',')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'[')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u']')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u':')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'?')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'~')):
                SWITCHED = True
                var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
                break
            if True:
                SWITCHED = True
                var.put(u'str', var.get(u'source').callprop(u'substr', var.get(u'index'), Js(4.0)))
                if PyJsStrictEq(var.get(u'str'),Js(u'>>>=')):
                    var.put(u'index', Js(4.0), u'+')
                else:
                    var.put(u'str', var.get(u'str').callprop(u'substr', Js(0.0), Js(3.0)))
                    if ((((PyJsStrictEq(var.get(u'str'),Js(u'===')) or PyJsStrictEq(var.get(u'str'),Js(u'!=='))) or PyJsStrictEq(var.get(u'str'),Js(u'>>>'))) or PyJsStrictEq(var.get(u'str'),Js(u'<<='))) or PyJsStrictEq(var.get(u'str'),Js(u'>>='))):
                        var.put(u'index', Js(3.0), u'+')
                    else:
                        var.put(u'str', var.get(u'str').callprop(u'substr', Js(0.0), Js(2.0)))
                        def PyJs_LONG_23_(var=var):
                            def PyJs_LONG_22_(var=var):
                                return (((((((((PyJsStrictEq(var.get(u'str'),Js(u'&&')) or PyJsStrictEq(var.get(u'str'),Js(u'||'))) or PyJsStrictEq(var.get(u'str'),Js(u'=='))) or PyJsStrictEq(var.get(u'str'),Js(u'!='))) or PyJsStrictEq(var.get(u'str'),Js(u'+='))) or PyJsStrictEq(var.get(u'str'),Js(u'-='))) or PyJsStrictEq(var.get(u'str'),Js(u'*='))) or PyJsStrictEq(var.get(u'str'),Js(u'/='))) or PyJsStrictEq(var.get(u'str'),Js(u'++'))) or PyJsStrictEq(var.get(u'str'),Js(u'--')))
                            return (((((((((PyJs_LONG_22_() or PyJsStrictEq(var.get(u'str'),Js(u'<<'))) or PyJsStrictEq(var.get(u'str'),Js(u'>>'))) or PyJsStrictEq(var.get(u'str'),Js(u'&='))) or PyJsStrictEq(var.get(u'str'),Js(u'|='))) or PyJsStrictEq(var.get(u'str'),Js(u'^='))) or PyJsStrictEq(var.get(u'str'),Js(u'%='))) or PyJsStrictEq(var.get(u'str'),Js(u'<='))) or PyJsStrictEq(var.get(u'str'),Js(u'>='))) or PyJsStrictEq(var.get(u'str'),Js(u'=>')))
                        if PyJs_LONG_23_():
                            var.put(u'index', Js(2.0), u'+')
                        else:
                            var.put(u'str', var.get(u'source').get(var.get(u'index')))
                            if (Js(u'<>=!+-*%&|^/').callprop(u'indexOf', var.get(u'str'))>=Js(0.0)):
                                var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
            SWITCHED = True
            break
        if PyJsStrictEq(var.get(u'index'),var.get(u'token').get(u'start')):
            var.get(u'throwUnexpectedToken')()
        var.get(u'token').put(u'end', var.get(u'index'))
        var.get(u'token').put(u'value', var.get(u'str'))
        return var.get(u'token')
    PyJsHoisted_scanPunctuator_.func_name = u'scanPunctuator'
    var.put(u'scanPunctuator', PyJsHoisted_scanPunctuator_)
    @Js
    def PyJsHoisted_parseArrowFunctionExpression_(options, node, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'options':options, u'arguments':arguments}, var)
        var.registers([u'body', u'node', u'previousStrict', u'options', u'previousAllowYield'])
        pass
        if var.get(u'hasLineTerminator'):
            var.get(u'tolerateUnexpectedToken')(var.get(u'lookahead'))
        var.get(u'expect')(Js(u'=>'))
        var.put(u'previousStrict', var.get(u'strict'))
        var.put(u'previousAllowYield', var.get(u'state').get(u'allowYield'))
        var.get(u'state').put(u'allowYield', var.get(u'true'))
        var.put(u'body', var.get(u'parseConciseBody')())
        if (var.get(u'strict') and var.get(u'options').get(u'firstRestricted')):
            var.get(u'throwUnexpectedToken')(var.get(u'options').get(u'firstRestricted'), var.get(u'options').get(u'message'))
        if (var.get(u'strict') and var.get(u'options').get(u'stricted')):
            var.get(u'tolerateUnexpectedToken')(var.get(u'options').get(u'stricted'), var.get(u'options').get(u'message'))
        var.put(u'strict', var.get(u'previousStrict'))
        var.get(u'state').put(u'allowYield', var.get(u'previousAllowYield'))
        return var.get(u'node').callprop(u'finishArrowFunctionExpression', var.get(u'options').get(u'params'), var.get(u'options').get(u'defaults'), var.get(u'body'), PyJsStrictNeq(var.get(u'body').get(u'type'),var.get(u'Syntax').get(u'BlockStatement')))
    PyJsHoisted_parseArrowFunctionExpression_.func_name = u'parseArrowFunctionExpression'
    var.put(u'parseArrowFunctionExpression', PyJsHoisted_parseArrowFunctionExpression_)
    @Js
    def PyJsHoisted_throwError_(messageFormat, this, arguments, var=var):
        var = Scope({u'this':this, u'messageFormat':messageFormat, u'arguments':arguments}, var)
        var.registers([u'msg', u'args', u'messageFormat'])
        pass
        var.put(u'args', var.get(u'Array').get(u'prototype').get(u'slice').callprop(u'call', var.get(u'arguments'), Js(1.0)))
        @Js
        def PyJs_anonymous_118_(whole, idx, this, arguments, var=var):
            var = Scope({u'this':this, u'whole':whole, u'arguments':arguments, u'idx':idx}, var)
            var.registers([u'whole', u'idx'])
            var.get(u'assert')((var.get(u'idx')<var.get(u'args').get(u'length')), Js(u'Message reference must be in range'))
            return var.get(u'args').get(var.get(u'idx'))
        PyJs_anonymous_118_._set_name(u'anonymous')
        var.put(u'msg', var.get(u'messageFormat').callprop(u'replace', JsRegExp(u'/%(\\d)/g'), PyJs_anonymous_118_))
        PyJsTempException = JsToPyException(var.get(u'createError')(var.get(u'lastLineNumber'), var.get(u'lastIndex'), var.get(u'msg')))
        raise PyJsTempException
    PyJsHoisted_throwError_.func_name = u'throwError'
    var.put(u'throwError', PyJsHoisted_throwError_)
    @Js
    def PyJsHoisted_scanUnicodeCodePointEscape_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'code', u'ch'])
        pass
        var.put(u'ch', var.get(u'source').get(var.get(u'index')))
        var.put(u'code', Js(0.0))
        if PyJsStrictEq(var.get(u'ch'),Js(u'}')):
            var.get(u'throwUnexpectedToken')()
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').get((var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1))))
            if var.get(u'isHexDigit')(var.get(u'ch')).neg():
                break
            var.put(u'code', ((var.get(u'code')*Js(16.0))+Js(u'0123456789abcdef').callprop(u'indexOf', var.get(u'ch').callprop(u'toLowerCase'))))
        if ((var.get(u'code')>Js(1114111)) or PyJsStrictNeq(var.get(u'ch'),Js(u'}'))):
            var.get(u'throwUnexpectedToken')()
        return var.get(u'fromCodePoint')(var.get(u'code'))
    PyJsHoisted_scanUnicodeCodePointEscape_.func_name = u'scanUnicodeCodePointEscape'
    var.put(u'scanUnicodeCodePointEscape', PyJsHoisted_scanUnicodeCodePointEscape_)
    @Js
    def PyJsHoisted_scanOctalLiteral_(prefix, start, this, arguments, var=var):
        var = Scope({u'this':this, u'start':start, u'prefix':prefix, u'arguments':arguments}, var)
        var.registers([u'octal', u'start', u'prefix', u'number'])
        pass
        if var.get(u'isOctalDigit')(var.get(u'prefix')):
            var.put(u'octal', var.get(u'true'))
            var.put(u'number', (Js(u'0')+var.get(u'source').get((var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1)))))
        else:
            var.put(u'octal', Js(False))
            var.put(u'index',Js(var.get(u'index').to_number())+Js(1))
            var.put(u'number', Js(u''))
        while (var.get(u'index')<var.get(u'length')):
            if var.get(u'isOctalDigit')(var.get(u'source').get(var.get(u'index'))).neg():
                break
            var.put(u'number', var.get(u'source').get((var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1))), u'+')
        if (var.get(u'octal').neg() and PyJsStrictEq(var.get(u'number').get(u'length'),Js(0.0))):
            var.get(u'throwUnexpectedToken')()
        if (var.get(u'isIdentifierStart')(var.get(u'source').callprop(u'charCodeAt', var.get(u'index'))) or var.get(u'isDecimalDigit')(var.get(u'source').callprop(u'charCodeAt', var.get(u'index')))):
            var.get(u'throwUnexpectedToken')()
        PyJs_Object_26_ = Js({u'type':var.get(u'Token').get(u'NumericLiteral'),u'value':var.get(u'parseInt')(var.get(u'number'), Js(8.0)),u'octal':var.get(u'octal'),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
        return PyJs_Object_26_
    PyJsHoisted_scanOctalLiteral_.func_name = u'scanOctalLiteral'
    var.put(u'scanOctalLiteral', PyJsHoisted_scanOctalLiteral_)
    @Js
    def PyJsHoisted_scanRegExp_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'body', u'start', u'flags', u'value'])
        pass
        var.put(u'scanning', var.get(u'true'))
        var.put(u'lookahead', var.get(u"null"))
        var.get(u'skipComment')()
        var.put(u'start', var.get(u'index'))
        var.put(u'body', var.get(u'scanRegExpBody')())
        var.put(u'flags', var.get(u'scanRegExpFlags')())
        var.put(u'value', var.get(u'testRegExp')(var.get(u'body').get(u'value'), var.get(u'flags').get(u'value')))
        var.put(u'scanning', Js(False))
        if var.get(u'extra').get(u'tokenize'):
            PyJs_Object_35_ = Js({u'pattern':var.get(u'body').get(u'value'),u'flags':var.get(u'flags').get(u'value')})
            PyJs_Object_34_ = Js({u'type':var.get(u'Token').get(u'RegularExpression'),u'value':var.get(u'value'),u'regex':PyJs_Object_35_,u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
            return PyJs_Object_34_
        PyJs_Object_37_ = Js({u'pattern':var.get(u'body').get(u'value'),u'flags':var.get(u'flags').get(u'value')})
        PyJs_Object_36_ = Js({u'literal':(var.get(u'body').get(u'literal')+var.get(u'flags').get(u'literal')),u'value':var.get(u'value'),u'regex':PyJs_Object_37_,u'start':var.get(u'start'),u'end':var.get(u'index')})
        return PyJs_Object_36_
    PyJsHoisted_scanRegExp_.func_name = u'scanRegExp'
    var.put(u'scanRegExp', PyJsHoisted_scanRegExp_)
    @Js
    def PyJsHoisted_parseImportDefaultSpecifier_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'local'])
        var.put(u'node', var.get(u'Node').create())
        var.put(u'local', var.get(u'parseNonComputedProperty')())
        return var.get(u'node').callprop(u'finishImportDefaultSpecifier', var.get(u'local'))
    PyJsHoisted_parseImportDefaultSpecifier_.func_name = u'parseImportDefaultSpecifier'
    var.put(u'parseImportDefaultSpecifier', PyJsHoisted_parseImportDefaultSpecifier_)
    @Js
    def PyJsHoisted_parsePattern_(params, kind, this, arguments, var=var):
        var = Scope({u'this':this, u'kind':kind, u'params':params, u'arguments':arguments}, var)
        var.registers([u'kind', u'params'])
        if var.get(u'match')(Js(u'[')):
            return var.get(u'parseArrayPattern')(var.get(u'params'), var.get(u'kind'))
        else:
            if var.get(u'match')(Js(u'{')):
                return var.get(u'parseObjectPattern')(var.get(u'params'), var.get(u'kind'))
        var.get(u'params').callprop(u'push', var.get(u'lookahead'))
        return var.get(u'parseVariableIdentifier')(var.get(u'kind'))
    PyJsHoisted_parsePattern_.func_name = u'parsePattern'
    var.put(u'parsePattern', PyJsHoisted_parsePattern_)
    @Js
    def PyJsHoisted_parseVariableIdentifier_(kind, this, arguments, var=var):
        var = Scope({u'this':this, u'kind':kind, u'arguments':arguments}, var)
        var.registers([u'node', u'token', u'kind'])
        var.put(u'node', var.get(u'Node').create())
        var.put(u'token', var.get(u'lex')())
        if (PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Keyword')) and PyJsStrictEq(var.get(u'token').get(u'value'),Js(u'yield'))):
            if var.get(u'strict'):
                var.get(u'tolerateUnexpectedToken')(var.get(u'token'), var.get(u'Messages').get(u'StrictReservedWord'))
            if var.get(u'state').get(u'allowYield').neg():
                var.get(u'throwUnexpectedToken')(var.get(u'token'))
        else:
            if PyJsStrictNeq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Identifier')):
                if ((var.get(u'strict') and PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Keyword'))) and var.get(u'isStrictModeReservedWord')(var.get(u'token').get(u'value'))):
                    var.get(u'tolerateUnexpectedToken')(var.get(u'token'), var.get(u'Messages').get(u'StrictReservedWord'))
                else:
                    if ((var.get(u'strict') or PyJsStrictNeq(var.get(u'token').get(u'value'),Js(u'let'))) or PyJsStrictNeq(var.get(u'kind'),Js(u'var'))):
                        var.get(u'throwUnexpectedToken')(var.get(u'token'))
            else:
                if ((PyJsStrictEq(var.get(u'state').get(u'sourceType'),Js(u'module')) and PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Identifier'))) and PyJsStrictEq(var.get(u'token').get(u'value'),Js(u'await'))):
                    var.get(u'tolerateUnexpectedToken')(var.get(u'token'))
        return var.get(u'node').callprop(u'finishIdentifier', var.get(u'token').get(u'value'))
    PyJsHoisted_parseVariableIdentifier_.func_name = u'parseVariableIdentifier'
    var.put(u'parseVariableIdentifier', PyJsHoisted_parseVariableIdentifier_)
    @Js
    def PyJsHoisted_parseForStatement_(node, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'arguments':arguments}, var)
        var.registers([u'body', u'oldInIteration', u'kind', u'right', u'node', u'previousAllowIn', u'declarations', u'update', u'init', u'initSeq', u'test', u'forIn', u'initStartToken', u'left'])
        var.put(u'previousAllowIn', var.get(u'state').get(u'allowIn'))
        var.put(u'init', var.put(u'test', var.put(u'update', var.get(u"null"))))
        var.put(u'forIn', var.get(u'true'))
        var.get(u'expectKeyword')(Js(u'for'))
        var.get(u'expect')(Js(u'('))
        if var.get(u'match')(Js(u';')):
            var.get(u'lex')()
        else:
            if var.get(u'matchKeyword')(Js(u'var')):
                var.put(u'init', var.get(u'Node').create())
                var.get(u'lex')()
                var.get(u'state').put(u'allowIn', Js(False))
                PyJs_Object_141_ = Js({u'inFor':var.get(u'true')})
                var.put(u'declarations', var.get(u'parseVariableDeclarationList')(PyJs_Object_141_))
                var.get(u'state').put(u'allowIn', var.get(u'previousAllowIn'))
                if (PyJsStrictEq(var.get(u'declarations').get(u'length'),Js(1.0)) and var.get(u'matchKeyword')(Js(u'in'))):
                    var.put(u'init', var.get(u'init').callprop(u'finishVariableDeclaration', var.get(u'declarations')))
                    var.get(u'lex')()
                    var.put(u'left', var.get(u'init'))
                    var.put(u'right', var.get(u'parseExpression')())
                    var.put(u'init', var.get(u"null"))
                else:
                    if ((PyJsStrictEq(var.get(u'declarations').get(u'length'),Js(1.0)) and PyJsStrictEq(var.get(u'declarations').get(u'0').get(u'init'),var.get(u"null"))) and var.get(u'matchContextualKeyword')(Js(u'of'))):
                        var.put(u'init', var.get(u'init').callprop(u'finishVariableDeclaration', var.get(u'declarations')))
                        var.get(u'lex')()
                        var.put(u'left', var.get(u'init'))
                        var.put(u'right', var.get(u'parseAssignmentExpression')())
                        var.put(u'init', var.get(u"null"))
                        var.put(u'forIn', Js(False))
                    else:
                        var.put(u'init', var.get(u'init').callprop(u'finishVariableDeclaration', var.get(u'declarations')))
                        var.get(u'expect')(Js(u';'))
            else:
                if (var.get(u'matchKeyword')(Js(u'const')) or var.get(u'matchKeyword')(Js(u'let'))):
                    var.put(u'init', var.get(u'Node').create())
                    var.put(u'kind', var.get(u'lex')().get(u'value'))
                    var.get(u'state').put(u'allowIn', Js(False))
                    PyJs_Object_142_ = Js({u'inFor':var.get(u'true')})
                    var.put(u'declarations', var.get(u'parseBindingList')(var.get(u'kind'), PyJs_Object_142_))
                    var.get(u'state').put(u'allowIn', var.get(u'previousAllowIn'))
                    if ((PyJsStrictEq(var.get(u'declarations').get(u'length'),Js(1.0)) and PyJsStrictEq(var.get(u'declarations').get(u'0').get(u'init'),var.get(u"null"))) and var.get(u'matchKeyword')(Js(u'in'))):
                        var.put(u'init', var.get(u'init').callprop(u'finishLexicalDeclaration', var.get(u'declarations'), var.get(u'kind')))
                        var.get(u'lex')()
                        var.put(u'left', var.get(u'init'))
                        var.put(u'right', var.get(u'parseExpression')())
                        var.put(u'init', var.get(u"null"))
                    else:
                        if ((PyJsStrictEq(var.get(u'declarations').get(u'length'),Js(1.0)) and PyJsStrictEq(var.get(u'declarations').get(u'0').get(u'init'),var.get(u"null"))) and var.get(u'matchContextualKeyword')(Js(u'of'))):
                            var.put(u'init', var.get(u'init').callprop(u'finishLexicalDeclaration', var.get(u'declarations'), var.get(u'kind')))
                            var.get(u'lex')()
                            var.put(u'left', var.get(u'init'))
                            var.put(u'right', var.get(u'parseAssignmentExpression')())
                            var.put(u'init', var.get(u"null"))
                            var.put(u'forIn', Js(False))
                        else:
                            var.get(u'consumeSemicolon')()
                            var.put(u'init', var.get(u'init').callprop(u'finishLexicalDeclaration', var.get(u'declarations'), var.get(u'kind')))
                else:
                    var.put(u'initStartToken', var.get(u'lookahead'))
                    var.get(u'state').put(u'allowIn', Js(False))
                    var.put(u'init', var.get(u'inheritCoverGrammar')(var.get(u'parseAssignmentExpression')))
                    var.get(u'state').put(u'allowIn', var.get(u'previousAllowIn'))
                    if var.get(u'matchKeyword')(Js(u'in')):
                        if var.get(u'isAssignmentTarget').neg():
                            var.get(u'tolerateError')(var.get(u'Messages').get(u'InvalidLHSInForIn'))
                        var.get(u'lex')()
                        var.get(u'reinterpretExpressionAsPattern')(var.get(u'init'))
                        var.put(u'left', var.get(u'init'))
                        var.put(u'right', var.get(u'parseExpression')())
                        var.put(u'init', var.get(u"null"))
                    else:
                        if var.get(u'matchContextualKeyword')(Js(u'of')):
                            if var.get(u'isAssignmentTarget').neg():
                                var.get(u'tolerateError')(var.get(u'Messages').get(u'InvalidLHSInForLoop'))
                            var.get(u'lex')()
                            var.get(u'reinterpretExpressionAsPattern')(var.get(u'init'))
                            var.put(u'left', var.get(u'init'))
                            var.put(u'right', var.get(u'parseAssignmentExpression')())
                            var.put(u'init', var.get(u"null"))
                            var.put(u'forIn', Js(False))
                        else:
                            if var.get(u'match')(Js(u',')):
                                var.put(u'initSeq', Js([var.get(u'init')]))
                                while var.get(u'match')(Js(u',')):
                                    var.get(u'lex')()
                                    var.get(u'initSeq').callprop(u'push', var.get(u'isolateCoverGrammar')(var.get(u'parseAssignmentExpression')))
                                var.put(u'init', var.get(u'WrappingNode').create(var.get(u'initStartToken')).callprop(u'finishSequenceExpression', var.get(u'initSeq')))
                            var.get(u'expect')(Js(u';'))
        if PyJsStrictEq(var.get(u'left',throw=False).typeof(),Js(u'undefined')):
            if var.get(u'match')(Js(u';')).neg():
                var.put(u'test', var.get(u'parseExpression')())
            var.get(u'expect')(Js(u';'))
            if var.get(u'match')(Js(u')')).neg():
                var.put(u'update', var.get(u'parseExpression')())
        var.get(u'expect')(Js(u')'))
        var.put(u'oldInIteration', var.get(u'state').get(u'inIteration'))
        var.get(u'state').put(u'inIteration', var.get(u'true'))
        var.put(u'body', var.get(u'isolateCoverGrammar')(var.get(u'parseStatement')))
        var.get(u'state').put(u'inIteration', var.get(u'oldInIteration'))
        def PyJs_LONG_143_(var=var):
            return (var.get(u'node').callprop(u'finishForStatement', var.get(u'init'), var.get(u'test'), var.get(u'update'), var.get(u'body')) if PyJsStrictEq(var.get(u'left',throw=False).typeof(),Js(u'undefined')) else (var.get(u'node').callprop(u'finishForInStatement', var.get(u'left'), var.get(u'right'), var.get(u'body')) if var.get(u'forIn') else var.get(u'node').callprop(u'finishForOfStatement', var.get(u'left'), var.get(u'right'), var.get(u'body'))))
        return PyJs_LONG_143_()
    PyJsHoisted_parseForStatement_.func_name = u'parseForStatement'
    var.put(u'parseForStatement', PyJsHoisted_parseForStatement_)
    @Js
    def PyJsHoisted_isIdentifierPart_(ch, this, arguments, var=var):
        var = Scope({u'this':this, u'ch':ch, u'arguments':arguments}, var)
        var.registers([u'ch'])
        def PyJs_LONG_10_(var=var):
            return ((((((PyJsStrictEq(var.get(u'ch'),Js(36)) or PyJsStrictEq(var.get(u'ch'),Js(95))) or ((var.get(u'ch')>=Js(65)) and (var.get(u'ch')<=Js(90)))) or ((var.get(u'ch')>=Js(97)) and (var.get(u'ch')<=Js(122)))) or ((var.get(u'ch')>=Js(48)) and (var.get(u'ch')<=Js(57)))) or PyJsStrictEq(var.get(u'ch'),Js(92))) or ((var.get(u'ch')>=Js(128)) and var.get(u'Regex').get(u'NonAsciiIdentifierPart').callprop(u'test', var.get(u'fromCodePoint')(var.get(u'ch')))))
        return PyJs_LONG_10_()
    PyJsHoisted_isIdentifierPart_.func_name = u'isIdentifierPart'
    var.put(u'isIdentifierPart', PyJsHoisted_isIdentifierPart_)
    @Js
    def PyJsHoisted_matchKeyword_(keyword, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'keyword':keyword}, var)
        var.registers([u'keyword'])
        return (PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Keyword')) and PyJsStrictEq(var.get(u'lookahead').get(u'value'),var.get(u'keyword')))
    PyJsHoisted_matchKeyword_.func_name = u'matchKeyword'
    var.put(u'matchKeyword', PyJsHoisted_matchKeyword_)
    @Js
    def PyJsHoisted_parseTryStatement_(node, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'finalizer', u'handler', u'block'])
        var.put(u'handler', var.get(u"null"))
        var.put(u'finalizer', var.get(u"null"))
        var.get(u'expectKeyword')(Js(u'try'))
        var.put(u'block', var.get(u'parseBlock')())
        if var.get(u'matchKeyword')(Js(u'catch')):
            var.put(u'handler', var.get(u'parseCatchClause')())
        if var.get(u'matchKeyword')(Js(u'finally')):
            var.get(u'lex')()
            var.put(u'finalizer', var.get(u'parseBlock')())
        if (var.get(u'handler').neg() and var.get(u'finalizer').neg()):
            var.get(u'throwError')(var.get(u'Messages').get(u'NoCatchOrFinally'))
        return var.get(u'node').callprop(u'finishTryStatement', var.get(u'block'), var.get(u'handler'), var.get(u'finalizer'))
    PyJsHoisted_parseTryStatement_.func_name = u'parseTryStatement'
    var.put(u'parseTryStatement', PyJsHoisted_parseTryStatement_)
    @Js
    def PyJsHoisted_parseComputedMember_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'expr'])
        pass
        var.get(u'expect')(Js(u'['))
        var.put(u'expr', var.get(u'isolateCoverGrammar')(var.get(u'parseExpression')))
        var.get(u'expect')(Js(u']'))
        return var.get(u'expr')
    PyJsHoisted_parseComputedMember_.func_name = u'parseComputedMember'
    var.put(u'parseComputedMember', PyJsHoisted_parseComputedMember_)
    @Js
    def PyJsHoisted_parseContinueStatement_(node, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'key', u'label'])
        var.put(u'label', var.get(u"null"))
        var.get(u'expectKeyword')(Js(u'continue'))
        if PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt', var.get(u'startIndex')),Js(59)):
            var.get(u'lex')()
            if var.get(u'state').get(u'inIteration').neg():
                var.get(u'throwError')(var.get(u'Messages').get(u'IllegalContinue'))
            return var.get(u'node').callprop(u'finishContinueStatement', var.get(u"null"))
        if var.get(u'hasLineTerminator'):
            if var.get(u'state').get(u'inIteration').neg():
                var.get(u'throwError')(var.get(u'Messages').get(u'IllegalContinue'))
            return var.get(u'node').callprop(u'finishContinueStatement', var.get(u"null"))
        if PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Identifier')):
            var.put(u'label', var.get(u'parseVariableIdentifier')())
            var.put(u'key', (Js(u'$')+var.get(u'label').get(u'name')))
            if var.get(u'Object').get(u'prototype').get(u'hasOwnProperty').callprop(u'call', var.get(u'state').get(u'labelSet'), var.get(u'key')).neg():
                var.get(u'throwError')(var.get(u'Messages').get(u'UnknownLabel'), var.get(u'label').get(u'name'))
        var.get(u'consumeSemicolon')()
        if (PyJsStrictEq(var.get(u'label'),var.get(u"null")) and var.get(u'state').get(u'inIteration').neg()):
            var.get(u'throwError')(var.get(u'Messages').get(u'IllegalContinue'))
        return var.get(u'node').callprop(u'finishContinueStatement', var.get(u'label'))
    PyJsHoisted_parseContinueStatement_.func_name = u'parseContinueStatement'
    var.put(u'parseContinueStatement', PyJsHoisted_parseContinueStatement_)
    @Js
    def PyJsHoisted_tryParseMethodDefinition_(token, key, computed, node, this, arguments, var=var):
        var = Scope({u'node':node, u'token':token, u'computed':computed, u'key':key, u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'computed', u'value', u'token', u'params', u'key', u'previousAllowYield', u'methodNode', u'options'])
        var.put(u'previousAllowYield', var.get(u'state').get(u'allowYield'))
        if PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Identifier')):
            if (PyJsStrictEq(var.get(u'token').get(u'value'),Js(u'get')) and var.get(u'lookaheadPropertyName')()):
                var.put(u'computed', var.get(u'match')(Js(u'[')))
                var.put(u'key', var.get(u'parseObjectPropertyKey')())
                var.put(u'methodNode', var.get(u'Node').create())
                var.get(u'expect')(Js(u'('))
                var.get(u'expect')(Js(u')'))
                var.get(u'state').put(u'allowYield', Js(False))
                PyJs_Object_123_ = Js({u'params':Js([]),u'defaults':Js([]),u'stricted':var.get(u"null"),u'firstRestricted':var.get(u"null"),u'message':var.get(u"null")})
                var.put(u'value', var.get(u'parsePropertyFunction')(var.get(u'methodNode'), PyJs_Object_123_, Js(False)))
                var.get(u'state').put(u'allowYield', var.get(u'previousAllowYield'))
                return var.get(u'node').callprop(u'finishProperty', Js(u'get'), var.get(u'key'), var.get(u'computed'), var.get(u'value'), Js(False), Js(False))
            else:
                if (PyJsStrictEq(var.get(u'token').get(u'value'),Js(u'set')) and var.get(u'lookaheadPropertyName')()):
                    var.put(u'computed', var.get(u'match')(Js(u'[')))
                    var.put(u'key', var.get(u'parseObjectPropertyKey')())
                    var.put(u'methodNode', var.get(u'Node').create())
                    var.get(u'expect')(Js(u'('))
                    PyJs_Object_125_ = Js({})
                    PyJs_Object_124_ = Js({u'params':Js([]),u'defaultCount':Js(0.0),u'defaults':Js([]),u'firstRestricted':var.get(u"null"),u'paramSet':PyJs_Object_125_})
                    var.put(u'options', PyJs_Object_124_)
                    if var.get(u'match')(Js(u')')):
                        var.get(u'tolerateUnexpectedToken')(var.get(u'lookahead'))
                    else:
                        var.get(u'state').put(u'allowYield', Js(False))
                        var.get(u'parseParam')(var.get(u'options'))
                        var.get(u'state').put(u'allowYield', var.get(u'previousAllowYield'))
                        if PyJsStrictEq(var.get(u'options').get(u'defaultCount'),Js(0.0)):
                            var.get(u'options').put(u'defaults', Js([]))
                    var.get(u'expect')(Js(u')'))
                    var.get(u'state').put(u'allowYield', Js(False))
                    var.put(u'value', var.get(u'parsePropertyFunction')(var.get(u'methodNode'), var.get(u'options'), Js(False)))
                    var.get(u'state').put(u'allowYield', var.get(u'previousAllowYield'))
                    return var.get(u'node').callprop(u'finishProperty', Js(u'set'), var.get(u'key'), var.get(u'computed'), var.get(u'value'), Js(False), Js(False))
        else:
            if ((PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Punctuator')) and PyJsStrictEq(var.get(u'token').get(u'value'),Js(u'*'))) and var.get(u'lookaheadPropertyName')()):
                var.put(u'computed', var.get(u'match')(Js(u'[')))
                var.put(u'key', var.get(u'parseObjectPropertyKey')())
                var.put(u'methodNode', var.get(u'Node').create())
                var.get(u'state').put(u'allowYield', var.get(u'true'))
                var.put(u'params', var.get(u'parseParams')())
                var.get(u'state').put(u'allowYield', var.get(u'previousAllowYield'))
                var.get(u'state').put(u'allowYield', Js(False))
                var.put(u'value', var.get(u'parsePropertyFunction')(var.get(u'methodNode'), var.get(u'params'), var.get(u'true')))
                var.get(u'state').put(u'allowYield', var.get(u'previousAllowYield'))
                return var.get(u'node').callprop(u'finishProperty', Js(u'init'), var.get(u'key'), var.get(u'computed'), var.get(u'value'), var.get(u'true'), Js(False))
        if (var.get(u'key') and var.get(u'match')(Js(u'('))):
            var.put(u'value', var.get(u'parsePropertyMethodFunction')())
            return var.get(u'node').callprop(u'finishProperty', Js(u'init'), var.get(u'key'), var.get(u'computed'), var.get(u'value'), var.get(u'true'), Js(False))
        return var.get(u"null")
    PyJsHoisted_tryParseMethodDefinition_.func_name = u'tryParseMethodDefinition'
    var.put(u'tryParseMethodDefinition', PyJsHoisted_tryParseMethodDefinition_)
    @Js
    def PyJsHoisted_parseClassBody_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'body', u'isStatic', u'computed', u'token', u'classBody', u'key', u'hasConstructor', u'method'])
        var.put(u'hasConstructor', Js(False))
        var.put(u'classBody', var.get(u'Node').create())
        var.get(u'expect')(Js(u'{'))
        var.put(u'body', Js([]))
        while var.get(u'match')(Js(u'}')).neg():
            if var.get(u'match')(Js(u';')):
                var.get(u'lex')()
            else:
                var.put(u'method', var.get(u'Node').create())
                var.put(u'token', var.get(u'lookahead'))
                var.put(u'isStatic', Js(False))
                var.put(u'computed', var.get(u'match')(Js(u'[')))
                if var.get(u'match')(Js(u'*')):
                    var.get(u'lex')()
                else:
                    var.put(u'key', var.get(u'parseObjectPropertyKey')())
                    if (PyJsStrictEq(var.get(u'key').get(u'name'),Js(u'static')) and (var.get(u'lookaheadPropertyName')() or var.get(u'match')(Js(u'*')))):
                        var.put(u'token', var.get(u'lookahead'))
                        var.put(u'isStatic', var.get(u'true'))
                        var.put(u'computed', var.get(u'match')(Js(u'[')))
                        if var.get(u'match')(Js(u'*')):
                            var.get(u'lex')()
                        else:
                            var.put(u'key', var.get(u'parseObjectPropertyKey')())
                var.put(u'method', var.get(u'tryParseMethodDefinition')(var.get(u'token'), var.get(u'key'), var.get(u'computed'), var.get(u'method')))
                if var.get(u'method'):
                    var.get(u'method').put(u'static', var.get(u'isStatic'))
                    if PyJsStrictEq(var.get(u'method').get(u'kind'),Js(u'init')):
                        var.get(u'method').put(u'kind', Js(u'method'))
                    if var.get(u'isStatic').neg():
                        if (var.get(u'method').get(u'computed').neg() and PyJsStrictEq((var.get(u'method').get(u'key').get(u'name') or var.get(u'method').get(u'key').get(u'value').callprop(u'toString')),Js(u'constructor'))):
                            if ((PyJsStrictNeq(var.get(u'method').get(u'kind'),Js(u'method')) or var.get(u'method').get(u'method').neg()) or var.get(u'method').get(u'value').get(u'generator')):
                                var.get(u'throwUnexpectedToken')(var.get(u'token'), var.get(u'Messages').get(u'ConstructorSpecialMethod'))
                            if var.get(u'hasConstructor'):
                                var.get(u'throwUnexpectedToken')(var.get(u'token'), var.get(u'Messages').get(u'DuplicateConstructor'))
                            else:
                                var.put(u'hasConstructor', var.get(u'true'))
                            var.get(u'method').put(u'kind', Js(u'constructor'))
                    else:
                        if (var.get(u'method').get(u'computed').neg() and PyJsStrictEq((var.get(u'method').get(u'key').get(u'name') or var.get(u'method').get(u'key').get(u'value').callprop(u'toString')),Js(u'prototype'))):
                            var.get(u'throwUnexpectedToken')(var.get(u'token'), var.get(u'Messages').get(u'StaticPrototype'))
                    var.get(u'method').put(u'type', var.get(u'Syntax').get(u'MethodDefinition'))
                    var.get(u'method').delete(u'method')
                    var.get(u'method').delete(u'shorthand')
                    var.get(u'body').callprop(u'push', var.get(u'method'))
                else:
                    var.get(u'throwUnexpectedToken')(var.get(u'lookahead'))
        var.get(u'lex')()
        return var.get(u'classBody').callprop(u'finishClassBody', var.get(u'body'))
    PyJsHoisted_parseClassBody_.func_name = u'parseClassBody'
    var.put(u'parseClassBody', PyJsHoisted_parseClassBody_)
    @Js
    def PyJsHoisted_filterTokenLocation_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'i', u'entry', u'token', u'tokens'])
        var.put(u'tokens', Js([]))
        #for JS loop
        var.put(u'i', Js(0.0))
        while (var.get(u'i')<var.get(u'extra').get(u'tokens').get(u'length')):
            try:
                var.put(u'entry', var.get(u'extra').get(u'tokens').get(var.get(u'i')))
                PyJs_Object_149_ = Js({u'type':var.get(u'entry').get(u'type'),u'value':var.get(u'entry').get(u'value')})
                var.put(u'token', PyJs_Object_149_)
                if var.get(u'entry').get(u'regex'):
                    PyJs_Object_150_ = Js({u'pattern':var.get(u'entry').get(u'regex').get(u'pattern'),u'flags':var.get(u'entry').get(u'regex').get(u'flags')})
                    var.get(u'token').put(u'regex', PyJs_Object_150_)
                if var.get(u'extra').get(u'range'):
                    var.get(u'token').put(u'range', var.get(u'entry').get(u'range'))
                if var.get(u'extra').get(u'loc'):
                    var.get(u'token').put(u'loc', var.get(u'entry').get(u'loc'))
                var.get(u'tokens').callprop(u'push', var.get(u'token'))
            finally:
                    var.put(u'i',Js(var.get(u'i').to_number())+Js(1))
        var.get(u'extra').put(u'tokens', var.get(u'tokens'))
    PyJsHoisted_filterTokenLocation_.func_name = u'filterTokenLocation'
    var.put(u'filterTokenLocation', PyJsHoisted_filterTokenLocation_)
    Js(u'use strict')
    pass
    PyJs_Object_1_ = Js({u'BooleanLiteral':Js(1.0),u'EOF':Js(2.0),u'Identifier':Js(3.0),u'Keyword':Js(4.0),u'NullLiteral':Js(5.0),u'NumericLiteral':Js(6.0),u'Punctuator':Js(7.0),u'StringLiteral':Js(8.0),u'RegularExpression':Js(9.0),u'Template':Js(10.0)})
    var.put(u'Token', PyJs_Object_1_)
    PyJs_Object_2_ = Js({})
    var.put(u'TokenName', PyJs_Object_2_)
    var.get(u'TokenName').put(var.get(u'Token').get(u'BooleanLiteral'), Js(u'Boolean'))
    var.get(u'TokenName').put(var.get(u'Token').get(u'EOF'), Js(u'<end>'))
    var.get(u'TokenName').put(var.get(u'Token').get(u'Identifier'), Js(u'Identifier'))
    var.get(u'TokenName').put(var.get(u'Token').get(u'Keyword'), Js(u'Keyword'))
    var.get(u'TokenName').put(var.get(u'Token').get(u'NullLiteral'), Js(u'Null'))
    var.get(u'TokenName').put(var.get(u'Token').get(u'NumericLiteral'), Js(u'Numeric'))
    var.get(u'TokenName').put(var.get(u'Token').get(u'Punctuator'), Js(u'Punctuator'))
    var.get(u'TokenName').put(var.get(u'Token').get(u'StringLiteral'), Js(u'String'))
    var.get(u'TokenName').put(var.get(u'Token').get(u'RegularExpression'), Js(u'RegularExpression'))
    var.get(u'TokenName').put(var.get(u'Token').get(u'Template'), Js(u'Template'))
    def PyJs_LONG_3_(var=var):
        return var.put(u'FnExprTokens', Js([Js(u'('), Js(u'{'), Js(u'['), Js(u'in'), Js(u'typeof'), Js(u'instanceof'), Js(u'new'), Js(u'return'), Js(u'case'), Js(u'delete'), Js(u'throw'), Js(u'void'), Js(u'='), Js(u'+='), Js(u'-='), Js(u'*='), Js(u'/='), Js(u'%='), Js(u'<<='), Js(u'>>='), Js(u'>>>='), Js(u'&='), Js(u'|='), Js(u'^='), Js(u','), Js(u'+'), Js(u'-'), Js(u'*'), Js(u'/'), Js(u'%'), Js(u'++'), Js(u'--'), Js(u'<<'), Js(u'>>'), Js(u'>>>'), Js(u'&'), Js(u'|'), Js(u'^'), Js(u'!'), Js(u'~'), Js(u'&&'), Js(u'||'), Js(u'?'), Js(u':'), Js(u'==='), Js(u'=='), Js(u'>='), Js(u'<='), Js(u'<'), Js(u'>'), Js(u'!='), Js(u'!==')]))
    PyJs_LONG_3_()
    PyJs_Object_4_ = Js({u'AssignmentExpression':Js(u'AssignmentExpression'),u'AssignmentPattern':Js(u'AssignmentPattern'),u'ArrayExpression':Js(u'ArrayExpression'),u'ArrayPattern':Js(u'ArrayPattern'),u'ArrowFunctionExpression':Js(u'ArrowFunctionExpression'),u'BlockStatement':Js(u'BlockStatement'),u'BinaryExpression':Js(u'BinaryExpression'),u'BreakStatement':Js(u'BreakStatement'),u'CallExpression':Js(u'CallExpression'),u'CatchClause':Js(u'CatchClause'),u'ClassBody':Js(u'ClassBody'),u'ClassDeclaration':Js(u'ClassDeclaration'),u'ClassExpression':Js(u'ClassExpression'),u'ConditionalExpression':Js(u'ConditionalExpression'),u'ContinueStatement':Js(u'ContinueStatement'),u'DoWhileStatement':Js(u'DoWhileStatement'),u'DebuggerStatement':Js(u'DebuggerStatement'),u'EmptyStatement':Js(u'EmptyStatement'),u'ExportAllDeclaration':Js(u'ExportAllDeclaration'),u'ExportDefaultDeclaration':Js(u'ExportDefaultDeclaration'),u'ExportNamedDeclaration':Js(u'ExportNamedDeclaration'),u'ExportSpecifier':Js(u'ExportSpecifier'),u'ExpressionStatement':Js(u'ExpressionStatement'),u'ForStatement':Js(u'ForStatement'),u'ForOfStatement':Js(u'ForOfStatement'),u'ForInStatement':Js(u'ForInStatement'),u'FunctionDeclaration':Js(u'FunctionDeclaration'),u'FunctionExpression':Js(u'FunctionExpression'),u'Identifier':Js(u'Identifier'),u'IfStatement':Js(u'IfStatement'),u'ImportDeclaration':Js(u'ImportDeclaration'),u'ImportDefaultSpecifier':Js(u'ImportDefaultSpecifier'),u'ImportNamespaceSpecifier':Js(u'ImportNamespaceSpecifier'),u'ImportSpecifier':Js(u'ImportSpecifier'),u'Literal':Js(u'Literal'),u'LabeledStatement':Js(u'LabeledStatement'),u'LogicalExpression':Js(u'LogicalExpression'),u'MemberExpression':Js(u'MemberExpression'),u'MetaProperty':Js(u'MetaProperty'),u'MethodDefinition':Js(u'MethodDefinition'),u'NewExpression':Js(u'NewExpression'),u'ObjectExpression':Js(u'ObjectExpression'),u'ObjectPattern':Js(u'ObjectPattern'),u'Program':Js(u'Program'),u'Property':Js(u'Property'),u'RestElement':Js(u'RestElement'),u'ReturnStatement':Js(u'ReturnStatement'),u'SequenceExpression':Js(u'SequenceExpression'),u'SpreadElement':Js(u'SpreadElement'),u'Super':Js(u'Super'),u'SwitchCase':Js(u'SwitchCase'),u'SwitchStatement':Js(u'SwitchStatement'),u'TaggedTemplateExpression':Js(u'TaggedTemplateExpression'),u'TemplateElement':Js(u'TemplateElement'),u'TemplateLiteral':Js(u'TemplateLiteral'),u'ThisExpression':Js(u'ThisExpression'),u'ThrowStatement':Js(u'ThrowStatement'),u'TryStatement':Js(u'TryStatement'),u'UnaryExpression':Js(u'UnaryExpression'),u'UpdateExpression':Js(u'UpdateExpression'),u'VariableDeclaration':Js(u'VariableDeclaration'),u'VariableDeclarator':Js(u'VariableDeclarator'),u'WhileStatement':Js(u'WhileStatement'),u'WithStatement':Js(u'WithStatement'),u'YieldExpression':Js(u'YieldExpression')})
    var.put(u'Syntax', PyJs_Object_4_)
    PyJs_Object_5_ = Js({u'ArrowParameterPlaceHolder':Js(u'ArrowParameterPlaceHolder')})
    var.put(u'PlaceHolders', PyJs_Object_5_)
    PyJs_Object_6_ = Js({u'UnexpectedToken':Js(u'Unexpected token %0'),u'UnexpectedNumber':Js(u'Unexpected number'),u'UnexpectedString':Js(u'Unexpected string'),u'UnexpectedIdentifier':Js(u'Unexpected identifier'),u'UnexpectedReserved':Js(u'Unexpected reserved word'),u'UnexpectedTemplate':Js(u'Unexpected quasi %0'),u'UnexpectedEOS':Js(u'Unexpected end of input'),u'NewlineAfterThrow':Js(u'Illegal newline after throw'),u'InvalidRegExp':Js(u'Invalid regular expression'),u'UnterminatedRegExp':Js(u'Invalid regular expression: missing /'),u'InvalidLHSInAssignment':Js(u'Invalid left-hand side in assignment'),u'InvalidLHSInForIn':Js(u'Invalid left-hand side in for-in'),u'InvalidLHSInForLoop':Js(u'Invalid left-hand side in for-loop'),u'MultipleDefaultsInSwitch':Js(u'More than one default clause in switch statement'),u'NoCatchOrFinally':Js(u'Missing catch or finally after try'),u'UnknownLabel':Js(u"Undefined label '%0'"),u'Redeclaration':Js(u"%0 '%1' has already been declared"),u'IllegalContinue':Js(u'Illegal continue statement'),u'IllegalBreak':Js(u'Illegal break statement'),u'IllegalReturn':Js(u'Illegal return statement'),u'StrictModeWith':Js(u'Strict mode code may not include a with statement'),u'StrictCatchVariable':Js(u'Catch variable may not be eval or arguments in strict mode'),u'StrictVarName':Js(u'Variable name may not be eval or arguments in strict mode'),u'StrictParamName':Js(u'Parameter name eval or arguments is not allowed in strict mode'),u'StrictParamDupe':Js(u'Strict mode function may not have duplicate parameter names'),u'StrictFunctionName':Js(u'Function name may not be eval or arguments in strict mode'),u'StrictOctalLiteral':Js(u'Octal literals are not allowed in strict mode.'),u'StrictDelete':Js(u'Delete of an unqualified identifier in strict mode.'),u'StrictLHSAssignment':Js(u'Assignment to eval or arguments is not allowed in strict mode'),u'StrictLHSPostfix':Js(u'Postfix increment/decrement may not have eval or arguments operand in strict mode'),u'StrictLHSPrefix':Js(u'Prefix increment/decrement may not have eval or arguments operand in strict mode'),u'StrictReservedWord':Js(u'Use of future reserved word in strict mode'),u'TemplateOctalLiteral':Js(u'Octal literals are not allowed in template strings.'),u'ParameterAfterRestParameter':Js(u'Rest parameter must be last formal parameter'),u'DefaultRestParameter':Js(u'Unexpected token ='),u'ObjectPatternAsRestParameter':Js(u'Unexpected token {'),u'DuplicateProtoProperty':Js(u'Duplicate __proto__ fields are not allowed in object literals'),u'ConstructorSpecialMethod':Js(u'Class constructor may not be an accessor'),u'DuplicateConstructor':Js(u'A class may only have one constructor'),u'StaticPrototype':Js(u'Classes may not have static property named prototype'),u'MissingFromClause':Js(u'Unexpected token'),u'NoAsAfterImportNamespace':Js(u'Unexpected token'),u'InvalidModuleSpecifier':Js(u'Unexpected token'),u'IllegalImportDeclaration':Js(u'Unexpected token'),u'IllegalExportDeclaration':Js(u'Unexpected token'),u'DuplicateBinding':Js(u'Duplicate binding %0')})
    var.put(u'Messages', PyJs_Object_6_)
    PyJs_Object_7_ = Js({u'NonAsciiIdentifierStart':JsRegExp(u'/[\\xAA\\xB5\\xBA\\xC0-\\xD6\\xD8-\\xF6\\xF8-\\u02C1\\u02C6-\\u02D1\\u02E0-\\u02E4\\u02EC\\u02EE\\u0370-\\u0374\\u0376\\u0377\\u037A-\\u037D\\u037F\\u0386\\u0388-\\u038A\\u038C\\u038E-\\u03A1\\u03A3-\\u03F5\\u03F7-\\u0481\\u048A-\\u052F\\u0531-\\u0556\\u0559\\u0561-\\u0587\\u05D0-\\u05EA\\u05F0-\\u05F2\\u0620-\\u064A\\u066E\\u066F\\u0671-\\u06D3\\u06D5\\u06E5\\u06E6\\u06EE\\u06EF\\u06FA-\\u06FC\\u06FF\\u0710\\u0712-\\u072F\\u074D-\\u07A5\\u07B1\\u07CA-\\u07EA\\u07F4\\u07F5\\u07FA\\u0800-\\u0815\\u081A\\u0824\\u0828\\u0840-\\u0858\\u08A0-\\u08B2\\u0904-\\u0939\\u093D\\u0950\\u0958-\\u0961\\u0971-\\u0980\\u0985-\\u098C\\u098F\\u0990\\u0993-\\u09A8\\u09AA-\\u09B0\\u09B2\\u09B6-\\u09B9\\u09BD\\u09CE\\u09DC\\u09DD\\u09DF-\\u09E1\\u09F0\\u09F1\\u0A05-\\u0A0A\\u0A0F\\u0A10\\u0A13-\\u0A28\\u0A2A-\\u0A30\\u0A32\\u0A33\\u0A35\\u0A36\\u0A38\\u0A39\\u0A59-\\u0A5C\\u0A5E\\u0A72-\\u0A74\\u0A85-\\u0A8D\\u0A8F-\\u0A91\\u0A93-\\u0AA8\\u0AAA-\\u0AB0\\u0AB2\\u0AB3\\u0AB5-\\u0AB9\\u0ABD\\u0AD0\\u0AE0\\u0AE1\\u0B05-\\u0B0C\\u0B0F\\u0B10\\u0B13-\\u0B28\\u0B2A-\\u0B30\\u0B32\\u0B33\\u0B35-\\u0B39\\u0B3D\\u0B5C\\u0B5D\\u0B5F-\\u0B61\\u0B71\\u0B83\\u0B85-\\u0B8A\\u0B8E-\\u0B90\\u0B92-\\u0B95\\u0B99\\u0B9A\\u0B9C\\u0B9E\\u0B9F\\u0BA3\\u0BA4\\u0BA8-\\u0BAA\\u0BAE-\\u0BB9\\u0BD0\\u0C05-\\u0C0C\\u0C0E-\\u0C10\\u0C12-\\u0C28\\u0C2A-\\u0C39\\u0C3D\\u0C58\\u0C59\\u0C60\\u0C61\\u0C85-\\u0C8C\\u0C8E-\\u0C90\\u0C92-\\u0CA8\\u0CAA-\\u0CB3\\u0CB5-\\u0CB9\\u0CBD\\u0CDE\\u0CE0\\u0CE1\\u0CF1\\u0CF2\\u0D05-\\u0D0C\\u0D0E-\\u0D10\\u0D12-\\u0D3A\\u0D3D\\u0D4E\\u0D60\\u0D61\\u0D7A-\\u0D7F\\u0D85-\\u0D96\\u0D9A-\\u0DB1\\u0DB3-\\u0DBB\\u0DBD\\u0DC0-\\u0DC6\\u0E01-\\u0E30\\u0E32\\u0E33\\u0E40-\\u0E46\\u0E81\\u0E82\\u0E84\\u0E87\\u0E88\\u0E8A\\u0E8D\\u0E94-\\u0E97\\u0E99-\\u0E9F\\u0EA1-\\u0EA3\\u0EA5\\u0EA7\\u0EAA\\u0EAB\\u0EAD-\\u0EB0\\u0EB2\\u0EB3\\u0EBD\\u0EC0-\\u0EC4\\u0EC6\\u0EDC-\\u0EDF\\u0F00\\u0F40-\\u0F47\\u0F49-\\u0F6C\\u0F88-\\u0F8C\\u1000-\\u102A\\u103F\\u1050-\\u1055\\u105A-\\u105D\\u1061\\u1065\\u1066\\u106E-\\u1070\\u1075-\\u1081\\u108E\\u10A0-\\u10C5\\u10C7\\u10CD\\u10D0-\\u10FA\\u10FC-\\u1248\\u124A-\\u124D\\u1250-\\u1256\\u1258\\u125A-\\u125D\\u1260-\\u1288\\u128A-\\u128D\\u1290-\\u12B0\\u12B2-\\u12B5\\u12B8-\\u12BE\\u12C0\\u12C2-\\u12C5\\u12C8-\\u12D6\\u12D8-\\u1310\\u1312-\\u1315\\u1318-\\u135A\\u1380-\\u138F\\u13A0-\\u13F4\\u1401-\\u166C\\u166F-\\u167F\\u1681-\\u169A\\u16A0-\\u16EA\\u16EE-\\u16F8\\u1700-\\u170C\\u170E-\\u1711\\u1720-\\u1731\\u1740-\\u1751\\u1760-\\u176C\\u176E-\\u1770\\u1780-\\u17B3\\u17D7\\u17DC\\u1820-\\u1877\\u1880-\\u18A8\\u18AA\\u18B0-\\u18F5\\u1900-\\u191E\\u1950-\\u196D\\u1970-\\u1974\\u1980-\\u19AB\\u19C1-\\u19C7\\u1A00-\\u1A16\\u1A20-\\u1A54\\u1AA7\\u1B05-\\u1B33\\u1B45-\\u1B4B\\u1B83-\\u1BA0\\u1BAE\\u1BAF\\u1BBA-\\u1BE5\\u1C00-\\u1C23\\u1C4D-\\u1C4F\\u1C5A-\\u1C7D\\u1CE9-\\u1CEC\\u1CEE-\\u1CF1\\u1CF5\\u1CF6\\u1D00-\\u1DBF\\u1E00-\\u1F15\\u1F18-\\u1F1D\\u1F20-\\u1F45\\u1F48-\\u1F4D\\u1F50-\\u1F57\\u1F59\\u1F5B\\u1F5D\\u1F5F-\\u1F7D\\u1F80-\\u1FB4\\u1FB6-\\u1FBC\\u1FBE\\u1FC2-\\u1FC4\\u1FC6-\\u1FCC\\u1FD0-\\u1FD3\\u1FD6-\\u1FDB\\u1FE0-\\u1FEC\\u1FF2-\\u1FF4\\u1FF6-\\u1FFC\\u2071\\u207F\\u2090-\\u209C\\u2102\\u2107\\u210A-\\u2113\\u2115\\u2118-\\u211D\\u2124\\u2126\\u2128\\u212A-\\u2139\\u213C-\\u213F\\u2145-\\u2149\\u214E\\u2160-\\u2188\\u2C00-\\u2C2E\\u2C30-\\u2C5E\\u2C60-\\u2CE4\\u2CEB-\\u2CEE\\u2CF2\\u2CF3\\u2D00-\\u2D25\\u2D27\\u2D2D\\u2D30-\\u2D67\\u2D6F\\u2D80-\\u2D96\\u2DA0-\\u2DA6\\u2DA8-\\u2DAE\\u2DB0-\\u2DB6\\u2DB8-\\u2DBE\\u2DC0-\\u2DC6\\u2DC8-\\u2DCE\\u2DD0-\\u2DD6\\u2DD8-\\u2DDE\\u3005-\\u3007\\u3021-\\u3029\\u3031-\\u3035\\u3038-\\u303C\\u3041-\\u3096\\u309B-\\u309F\\u30A1-\\u30FA\\u30FC-\\u30FF\\u3105-\\u312D\\u3131-\\u318E\\u31A0-\\u31BA\\u31F0-\\u31FF\\u3400-\\u4DB5\\u4E00-\\u9FCC\\uA000-\\uA48C\\uA4D0-\\uA4FD\\uA500-\\uA60C\\uA610-\\uA61F\\uA62A\\uA62B\\uA640-\\uA66E\\uA67F-\\uA69D\\uA6A0-\\uA6EF\\uA717-\\uA71F\\uA722-\\uA788\\uA78B-\\uA78E\\uA790-\\uA7AD\\uA7B0\\uA7B1\\uA7F7-\\uA801\\uA803-\\uA805\\uA807-\\uA80A\\uA80C-\\uA822\\uA840-\\uA873\\uA882-\\uA8B3\\uA8F2-\\uA8F7\\uA8FB\\uA90A-\\uA925\\uA930-\\uA946\\uA960-\\uA97C\\uA984-\\uA9B2\\uA9CF\\uA9E0-\\uA9E4\\uA9E6-\\uA9EF\\uA9FA-\\uA9FE\\uAA00-\\uAA28\\uAA40-\\uAA42\\uAA44-\\uAA4B\\uAA60-\\uAA76\\uAA7A\\uAA7E-\\uAAAF\\uAAB1\\uAAB5\\uAAB6\\uAAB9-\\uAABD\\uAAC0\\uAAC2\\uAADB-\\uAADD\\uAAE0-\\uAAEA\\uAAF2-\\uAAF4\\uAB01-\\uAB06\\uAB09-\\uAB0E\\uAB11-\\uAB16\\uAB20-\\uAB26\\uAB28-\\uAB2E\\uAB30-\\uAB5A\\uAB5C-\\uAB5F\\uAB64\\uAB65\\uABC0-\\uABE2\\uAC00-\\uD7A3\\uD7B0-\\uD7C6\\uD7CB-\\uD7FB\\uF900-\\uFA6D\\uFA70-\\uFAD9\\uFB00-\\uFB06\\uFB13-\\uFB17\\uFB1D\\uFB1F-\\uFB28\\uFB2A-\\uFB36\\uFB38-\\uFB3C\\uFB3E\\uFB40\\uFB41\\uFB43\\uFB44\\uFB46-\\uFBB1\\uFBD3-\\uFD3D\\uFD50-\\uFD8F\\uFD92-\\uFDC7\\uFDF0-\\uFDFB\\uFE70-\\uFE74\\uFE76-\\uFEFC\\uFF21-\\uFF3A\\uFF41-\\uFF5A\\uFF66-\\uFFBE\\uFFC2-\\uFFC7\\uFFCA-\\uFFCF\\uFFD2-\\uFFD7\\uFFDA-\\uFFDC]|\\uD800[\\uDC00-\\uDC0B\\uDC0D-\\uDC26\\uDC28-\\uDC3A\\uDC3C\\uDC3D\\uDC3F-\\uDC4D\\uDC50-\\uDC5D\\uDC80-\\uDCFA\\uDD40-\\uDD74\\uDE80-\\uDE9C\\uDEA0-\\uDED0\\uDF00-\\uDF1F\\uDF30-\\uDF4A\\uDF50-\\uDF75\\uDF80-\\uDF9D\\uDFA0-\\uDFC3\\uDFC8-\\uDFCF\\uDFD1-\\uDFD5]|\\uD801[\\uDC00-\\uDC9D\\uDD00-\\uDD27\\uDD30-\\uDD63\\uDE00-\\uDF36\\uDF40-\\uDF55\\uDF60-\\uDF67]|\\uD802[\\uDC00-\\uDC05\\uDC08\\uDC0A-\\uDC35\\uDC37\\uDC38\\uDC3C\\uDC3F-\\uDC55\\uDC60-\\uDC76\\uDC80-\\uDC9E\\uDD00-\\uDD15\\uDD20-\\uDD39\\uDD80-\\uDDB7\\uDDBE\\uDDBF\\uDE00\\uDE10-\\uDE13\\uDE15-\\uDE17\\uDE19-\\uDE33\\uDE60-\\uDE7C\\uDE80-\\uDE9C\\uDEC0-\\uDEC7\\uDEC9-\\uDEE4\\uDF00-\\uDF35\\uDF40-\\uDF55\\uDF60-\\uDF72\\uDF80-\\uDF91]|\\uD803[\\uDC00-\\uDC48]|\\uD804[\\uDC03-\\uDC37\\uDC83-\\uDCAF\\uDCD0-\\uDCE8\\uDD03-\\uDD26\\uDD50-\\uDD72\\uDD76\\uDD83-\\uDDB2\\uDDC1-\\uDDC4\\uDDDA\\uDE00-\\uDE11\\uDE13-\\uDE2B\\uDEB0-\\uDEDE\\uDF05-\\uDF0C\\uDF0F\\uDF10\\uDF13-\\uDF28\\uDF2A-\\uDF30\\uDF32\\uDF33\\uDF35-\\uDF39\\uDF3D\\uDF5D-\\uDF61]|\\uD805[\\uDC80-\\uDCAF\\uDCC4\\uDCC5\\uDCC7\\uDD80-\\uDDAE\\uDE00-\\uDE2F\\uDE44\\uDE80-\\uDEAA]|\\uD806[\\uDCA0-\\uDCDF\\uDCFF\\uDEC0-\\uDEF8]|\\uD808[\\uDC00-\\uDF98]|\\uD809[\\uDC00-\\uDC6E]|[\\uD80C\\uD840-\\uD868\\uD86A-\\uD86C][\\uDC00-\\uDFFF]|\\uD80D[\\uDC00-\\uDC2E]|\\uD81A[\\uDC00-\\uDE38\\uDE40-\\uDE5E\\uDED0-\\uDEED\\uDF00-\\uDF2F\\uDF40-\\uDF43\\uDF63-\\uDF77\\uDF7D-\\uDF8F]|\\uD81B[\\uDF00-\\uDF44\\uDF50\\uDF93-\\uDF9F]|\\uD82C[\\uDC00\\uDC01]|\\uD82F[\\uDC00-\\uDC6A\\uDC70-\\uDC7C\\uDC80-\\uDC88\\uDC90-\\uDC99]|\\uD835[\\uDC00-\\uDC54\\uDC56-\\uDC9C\\uDC9E\\uDC9F\\uDCA2\\uDCA5\\uDCA6\\uDCA9-\\uDCAC\\uDCAE-\\uDCB9\\uDCBB\\uDCBD-\\uDCC3\\uDCC5-\\uDD05\\uDD07-\\uDD0A\\uDD0D-\\uDD14\\uDD16-\\uDD1C\\uDD1E-\\uDD39\\uDD3B-\\uDD3E\\uDD40-\\uDD44\\uDD46\\uDD4A-\\uDD50\\uDD52-\\uDEA5\\uDEA8-\\uDEC0\\uDEC2-\\uDEDA\\uDEDC-\\uDEFA\\uDEFC-\\uDF14\\uDF16-\\uDF34\\uDF36-\\uDF4E\\uDF50-\\uDF6E\\uDF70-\\uDF88\\uDF8A-\\uDFA8\\uDFAA-\\uDFC2\\uDFC4-\\uDFCB]|\\uD83A[\\uDC00-\\uDCC4]|\\uD83B[\\uDE00-\\uDE03\\uDE05-\\uDE1F\\uDE21\\uDE22\\uDE24\\uDE27\\uDE29-\\uDE32\\uDE34-\\uDE37\\uDE39\\uDE3B\\uDE42\\uDE47\\uDE49\\uDE4B\\uDE4D-\\uDE4F\\uDE51\\uDE52\\uDE54\\uDE57\\uDE59\\uDE5B\\uDE5D\\uDE5F\\uDE61\\uDE62\\uDE64\\uDE67-\\uDE6A\\uDE6C-\\uDE72\\uDE74-\\uDE77\\uDE79-\\uDE7C\\uDE7E\\uDE80-\\uDE89\\uDE8B-\\uDE9B\\uDEA1-\\uDEA3\\uDEA5-\\uDEA9\\uDEAB-\\uDEBB]|\\uD869[\\uDC00-\\uDED6\\uDF00-\\uDFFF]|\\uD86D[\\uDC00-\\uDF34\\uDF40-\\uDFFF]|\\uD86E[\\uDC00-\\uDC1D]|\\uD87E[\\uDC00-\\uDE1D]/'),u'NonAsciiIdentifierPart':JsRegExp(u'/[\\xAA\\xB5\\xB7\\xBA\\xC0-\\xD6\\xD8-\\xF6\\xF8-\\u02C1\\u02C6-\\u02D1\\u02E0-\\u02E4\\u02EC\\u02EE\\u0300-\\u0374\\u0376\\u0377\\u037A-\\u037D\\u037F\\u0386-\\u038A\\u038C\\u038E-\\u03A1\\u03A3-\\u03F5\\u03F7-\\u0481\\u0483-\\u0487\\u048A-\\u052F\\u0531-\\u0556\\u0559\\u0561-\\u0587\\u0591-\\u05BD\\u05BF\\u05C1\\u05C2\\u05C4\\u05C5\\u05C7\\u05D0-\\u05EA\\u05F0-\\u05F2\\u0610-\\u061A\\u0620-\\u0669\\u066E-\\u06D3\\u06D5-\\u06DC\\u06DF-\\u06E8\\u06EA-\\u06FC\\u06FF\\u0710-\\u074A\\u074D-\\u07B1\\u07C0-\\u07F5\\u07FA\\u0800-\\u082D\\u0840-\\u085B\\u08A0-\\u08B2\\u08E4-\\u0963\\u0966-\\u096F\\u0971-\\u0983\\u0985-\\u098C\\u098F\\u0990\\u0993-\\u09A8\\u09AA-\\u09B0\\u09B2\\u09B6-\\u09B9\\u09BC-\\u09C4\\u09C7\\u09C8\\u09CB-\\u09CE\\u09D7\\u09DC\\u09DD\\u09DF-\\u09E3\\u09E6-\\u09F1\\u0A01-\\u0A03\\u0A05-\\u0A0A\\u0A0F\\u0A10\\u0A13-\\u0A28\\u0A2A-\\u0A30\\u0A32\\u0A33\\u0A35\\u0A36\\u0A38\\u0A39\\u0A3C\\u0A3E-\\u0A42\\u0A47\\u0A48\\u0A4B-\\u0A4D\\u0A51\\u0A59-\\u0A5C\\u0A5E\\u0A66-\\u0A75\\u0A81-\\u0A83\\u0A85-\\u0A8D\\u0A8F-\\u0A91\\u0A93-\\u0AA8\\u0AAA-\\u0AB0\\u0AB2\\u0AB3\\u0AB5-\\u0AB9\\u0ABC-\\u0AC5\\u0AC7-\\u0AC9\\u0ACB-\\u0ACD\\u0AD0\\u0AE0-\\u0AE3\\u0AE6-\\u0AEF\\u0B01-\\u0B03\\u0B05-\\u0B0C\\u0B0F\\u0B10\\u0B13-\\u0B28\\u0B2A-\\u0B30\\u0B32\\u0B33\\u0B35-\\u0B39\\u0B3C-\\u0B44\\u0B47\\u0B48\\u0B4B-\\u0B4D\\u0B56\\u0B57\\u0B5C\\u0B5D\\u0B5F-\\u0B63\\u0B66-\\u0B6F\\u0B71\\u0B82\\u0B83\\u0B85-\\u0B8A\\u0B8E-\\u0B90\\u0B92-\\u0B95\\u0B99\\u0B9A\\u0B9C\\u0B9E\\u0B9F\\u0BA3\\u0BA4\\u0BA8-\\u0BAA\\u0BAE-\\u0BB9\\u0BBE-\\u0BC2\\u0BC6-\\u0BC8\\u0BCA-\\u0BCD\\u0BD0\\u0BD7\\u0BE6-\\u0BEF\\u0C00-\\u0C03\\u0C05-\\u0C0C\\u0C0E-\\u0C10\\u0C12-\\u0C28\\u0C2A-\\u0C39\\u0C3D-\\u0C44\\u0C46-\\u0C48\\u0C4A-\\u0C4D\\u0C55\\u0C56\\u0C58\\u0C59\\u0C60-\\u0C63\\u0C66-\\u0C6F\\u0C81-\\u0C83\\u0C85-\\u0C8C\\u0C8E-\\u0C90\\u0C92-\\u0CA8\\u0CAA-\\u0CB3\\u0CB5-\\u0CB9\\u0CBC-\\u0CC4\\u0CC6-\\u0CC8\\u0CCA-\\u0CCD\\u0CD5\\u0CD6\\u0CDE\\u0CE0-\\u0CE3\\u0CE6-\\u0CEF\\u0CF1\\u0CF2\\u0D01-\\u0D03\\u0D05-\\u0D0C\\u0D0E-\\u0D10\\u0D12-\\u0D3A\\u0D3D-\\u0D44\\u0D46-\\u0D48\\u0D4A-\\u0D4E\\u0D57\\u0D60-\\u0D63\\u0D66-\\u0D6F\\u0D7A-\\u0D7F\\u0D82\\u0D83\\u0D85-\\u0D96\\u0D9A-\\u0DB1\\u0DB3-\\u0DBB\\u0DBD\\u0DC0-\\u0DC6\\u0DCA\\u0DCF-\\u0DD4\\u0DD6\\u0DD8-\\u0DDF\\u0DE6-\\u0DEF\\u0DF2\\u0DF3\\u0E01-\\u0E3A\\u0E40-\\u0E4E\\u0E50-\\u0E59\\u0E81\\u0E82\\u0E84\\u0E87\\u0E88\\u0E8A\\u0E8D\\u0E94-\\u0E97\\u0E99-\\u0E9F\\u0EA1-\\u0EA3\\u0EA5\\u0EA7\\u0EAA\\u0EAB\\u0EAD-\\u0EB9\\u0EBB-\\u0EBD\\u0EC0-\\u0EC4\\u0EC6\\u0EC8-\\u0ECD\\u0ED0-\\u0ED9\\u0EDC-\\u0EDF\\u0F00\\u0F18\\u0F19\\u0F20-\\u0F29\\u0F35\\u0F37\\u0F39\\u0F3E-\\u0F47\\u0F49-\\u0F6C\\u0F71-\\u0F84\\u0F86-\\u0F97\\u0F99-\\u0FBC\\u0FC6\\u1000-\\u1049\\u1050-\\u109D\\u10A0-\\u10C5\\u10C7\\u10CD\\u10D0-\\u10FA\\u10FC-\\u1248\\u124A-\\u124D\\u1250-\\u1256\\u1258\\u125A-\\u125D\\u1260-\\u1288\\u128A-\\u128D\\u1290-\\u12B0\\u12B2-\\u12B5\\u12B8-\\u12BE\\u12C0\\u12C2-\\u12C5\\u12C8-\\u12D6\\u12D8-\\u1310\\u1312-\\u1315\\u1318-\\u135A\\u135D-\\u135F\\u1369-\\u1371\\u1380-\\u138F\\u13A0-\\u13F4\\u1401-\\u166C\\u166F-\\u167F\\u1681-\\u169A\\u16A0-\\u16EA\\u16EE-\\u16F8\\u1700-\\u170C\\u170E-\\u1714\\u1720-\\u1734\\u1740-\\u1753\\u1760-\\u176C\\u176E-\\u1770\\u1772\\u1773\\u1780-\\u17D3\\u17D7\\u17DC\\u17DD\\u17E0-\\u17E9\\u180B-\\u180D\\u1810-\\u1819\\u1820-\\u1877\\u1880-\\u18AA\\u18B0-\\u18F5\\u1900-\\u191E\\u1920-\\u192B\\u1930-\\u193B\\u1946-\\u196D\\u1970-\\u1974\\u1980-\\u19AB\\u19B0-\\u19C9\\u19D0-\\u19DA\\u1A00-\\u1A1B\\u1A20-\\u1A5E\\u1A60-\\u1A7C\\u1A7F-\\u1A89\\u1A90-\\u1A99\\u1AA7\\u1AB0-\\u1ABD\\u1B00-\\u1B4B\\u1B50-\\u1B59\\u1B6B-\\u1B73\\u1B80-\\u1BF3\\u1C00-\\u1C37\\u1C40-\\u1C49\\u1C4D-\\u1C7D\\u1CD0-\\u1CD2\\u1CD4-\\u1CF6\\u1CF8\\u1CF9\\u1D00-\\u1DF5\\u1DFC-\\u1F15\\u1F18-\\u1F1D\\u1F20-\\u1F45\\u1F48-\\u1F4D\\u1F50-\\u1F57\\u1F59\\u1F5B\\u1F5D\\u1F5F-\\u1F7D\\u1F80-\\u1FB4\\u1FB6-\\u1FBC\\u1FBE\\u1FC2-\\u1FC4\\u1FC6-\\u1FCC\\u1FD0-\\u1FD3\\u1FD6-\\u1FDB\\u1FE0-\\u1FEC\\u1FF2-\\u1FF4\\u1FF6-\\u1FFC\\u200C\\u200D\\u203F\\u2040\\u2054\\u2071\\u207F\\u2090-\\u209C\\u20D0-\\u20DC\\u20E1\\u20E5-\\u20F0\\u2102\\u2107\\u210A-\\u2113\\u2115\\u2118-\\u211D\\u2124\\u2126\\u2128\\u212A-\\u2139\\u213C-\\u213F\\u2145-\\u2149\\u214E\\u2160-\\u2188\\u2C00-\\u2C2E\\u2C30-\\u2C5E\\u2C60-\\u2CE4\\u2CEB-\\u2CF3\\u2D00-\\u2D25\\u2D27\\u2D2D\\u2D30-\\u2D67\\u2D6F\\u2D7F-\\u2D96\\u2DA0-\\u2DA6\\u2DA8-\\u2DAE\\u2DB0-\\u2DB6\\u2DB8-\\u2DBE\\u2DC0-\\u2DC6\\u2DC8-\\u2DCE\\u2DD0-\\u2DD6\\u2DD8-\\u2DDE\\u2DE0-\\u2DFF\\u3005-\\u3007\\u3021-\\u302F\\u3031-\\u3035\\u3038-\\u303C\\u3041-\\u3096\\u3099-\\u309F\\u30A1-\\u30FA\\u30FC-\\u30FF\\u3105-\\u312D\\u3131-\\u318E\\u31A0-\\u31BA\\u31F0-\\u31FF\\u3400-\\u4DB5\\u4E00-\\u9FCC\\uA000-\\uA48C\\uA4D0-\\uA4FD\\uA500-\\uA60C\\uA610-\\uA62B\\uA640-\\uA66F\\uA674-\\uA67D\\uA67F-\\uA69D\\uA69F-\\uA6F1\\uA717-\\uA71F\\uA722-\\uA788\\uA78B-\\uA78E\\uA790-\\uA7AD\\uA7B0\\uA7B1\\uA7F7-\\uA827\\uA840-\\uA873\\uA880-\\uA8C4\\uA8D0-\\uA8D9\\uA8E0-\\uA8F7\\uA8FB\\uA900-\\uA92D\\uA930-\\uA953\\uA960-\\uA97C\\uA980-\\uA9C0\\uA9CF-\\uA9D9\\uA9E0-\\uA9FE\\uAA00-\\uAA36\\uAA40-\\uAA4D\\uAA50-\\uAA59\\uAA60-\\uAA76\\uAA7A-\\uAAC2\\uAADB-\\uAADD\\uAAE0-\\uAAEF\\uAAF2-\\uAAF6\\uAB01-\\uAB06\\uAB09-\\uAB0E\\uAB11-\\uAB16\\uAB20-\\uAB26\\uAB28-\\uAB2E\\uAB30-\\uAB5A\\uAB5C-\\uAB5F\\uAB64\\uAB65\\uABC0-\\uABEA\\uABEC\\uABED\\uABF0-\\uABF9\\uAC00-\\uD7A3\\uD7B0-\\uD7C6\\uD7CB-\\uD7FB\\uF900-\\uFA6D\\uFA70-\\uFAD9\\uFB00-\\uFB06\\uFB13-\\uFB17\\uFB1D-\\uFB28\\uFB2A-\\uFB36\\uFB38-\\uFB3C\\uFB3E\\uFB40\\uFB41\\uFB43\\uFB44\\uFB46-\\uFBB1\\uFBD3-\\uFD3D\\uFD50-\\uFD8F\\uFD92-\\uFDC7\\uFDF0-\\uFDFB\\uFE00-\\uFE0F\\uFE20-\\uFE2D\\uFE33\\uFE34\\uFE4D-\\uFE4F\\uFE70-\\uFE74\\uFE76-\\uFEFC\\uFF10-\\uFF19\\uFF21-\\uFF3A\\uFF3F\\uFF41-\\uFF5A\\uFF66-\\uFFBE\\uFFC2-\\uFFC7\\uFFCA-\\uFFCF\\uFFD2-\\uFFD7\\uFFDA-\\uFFDC]|\\uD800[\\uDC00-\\uDC0B\\uDC0D-\\uDC26\\uDC28-\\uDC3A\\uDC3C\\uDC3D\\uDC3F-\\uDC4D\\uDC50-\\uDC5D\\uDC80-\\uDCFA\\uDD40-\\uDD74\\uDDFD\\uDE80-\\uDE9C\\uDEA0-\\uDED0\\uDEE0\\uDF00-\\uDF1F\\uDF30-\\uDF4A\\uDF50-\\uDF7A\\uDF80-\\uDF9D\\uDFA0-\\uDFC3\\uDFC8-\\uDFCF\\uDFD1-\\uDFD5]|\\uD801[\\uDC00-\\uDC9D\\uDCA0-\\uDCA9\\uDD00-\\uDD27\\uDD30-\\uDD63\\uDE00-\\uDF36\\uDF40-\\uDF55\\uDF60-\\uDF67]|\\uD802[\\uDC00-\\uDC05\\uDC08\\uDC0A-\\uDC35\\uDC37\\uDC38\\uDC3C\\uDC3F-\\uDC55\\uDC60-\\uDC76\\uDC80-\\uDC9E\\uDD00-\\uDD15\\uDD20-\\uDD39\\uDD80-\\uDDB7\\uDDBE\\uDDBF\\uDE00-\\uDE03\\uDE05\\uDE06\\uDE0C-\\uDE13\\uDE15-\\uDE17\\uDE19-\\uDE33\\uDE38-\\uDE3A\\uDE3F\\uDE60-\\uDE7C\\uDE80-\\uDE9C\\uDEC0-\\uDEC7\\uDEC9-\\uDEE6\\uDF00-\\uDF35\\uDF40-\\uDF55\\uDF60-\\uDF72\\uDF80-\\uDF91]|\\uD803[\\uDC00-\\uDC48]|\\uD804[\\uDC00-\\uDC46\\uDC66-\\uDC6F\\uDC7F-\\uDCBA\\uDCD0-\\uDCE8\\uDCF0-\\uDCF9\\uDD00-\\uDD34\\uDD36-\\uDD3F\\uDD50-\\uDD73\\uDD76\\uDD80-\\uDDC4\\uDDD0-\\uDDDA\\uDE00-\\uDE11\\uDE13-\\uDE37\\uDEB0-\\uDEEA\\uDEF0-\\uDEF9\\uDF01-\\uDF03\\uDF05-\\uDF0C\\uDF0F\\uDF10\\uDF13-\\uDF28\\uDF2A-\\uDF30\\uDF32\\uDF33\\uDF35-\\uDF39\\uDF3C-\\uDF44\\uDF47\\uDF48\\uDF4B-\\uDF4D\\uDF57\\uDF5D-\\uDF63\\uDF66-\\uDF6C\\uDF70-\\uDF74]|\\uD805[\\uDC80-\\uDCC5\\uDCC7\\uDCD0-\\uDCD9\\uDD80-\\uDDB5\\uDDB8-\\uDDC0\\uDE00-\\uDE40\\uDE44\\uDE50-\\uDE59\\uDE80-\\uDEB7\\uDEC0-\\uDEC9]|\\uD806[\\uDCA0-\\uDCE9\\uDCFF\\uDEC0-\\uDEF8]|\\uD808[\\uDC00-\\uDF98]|\\uD809[\\uDC00-\\uDC6E]|[\\uD80C\\uD840-\\uD868\\uD86A-\\uD86C][\\uDC00-\\uDFFF]|\\uD80D[\\uDC00-\\uDC2E]|\\uD81A[\\uDC00-\\uDE38\\uDE40-\\uDE5E\\uDE60-\\uDE69\\uDED0-\\uDEED\\uDEF0-\\uDEF4\\uDF00-\\uDF36\\uDF40-\\uDF43\\uDF50-\\uDF59\\uDF63-\\uDF77\\uDF7D-\\uDF8F]|\\uD81B[\\uDF00-\\uDF44\\uDF50-\\uDF7E\\uDF8F-\\uDF9F]|\\uD82C[\\uDC00\\uDC01]|\\uD82F[\\uDC00-\\uDC6A\\uDC70-\\uDC7C\\uDC80-\\uDC88\\uDC90-\\uDC99\\uDC9D\\uDC9E]|\\uD834[\\uDD65-\\uDD69\\uDD6D-\\uDD72\\uDD7B-\\uDD82\\uDD85-\\uDD8B\\uDDAA-\\uDDAD\\uDE42-\\uDE44]|\\uD835[\\uDC00-\\uDC54\\uDC56-\\uDC9C\\uDC9E\\uDC9F\\uDCA2\\uDCA5\\uDCA6\\uDCA9-\\uDCAC\\uDCAE-\\uDCB9\\uDCBB\\uDCBD-\\uDCC3\\uDCC5-\\uDD05\\uDD07-\\uDD0A\\uDD0D-\\uDD14\\uDD16-\\uDD1C\\uDD1E-\\uDD39\\uDD3B-\\uDD3E\\uDD40-\\uDD44\\uDD46\\uDD4A-\\uDD50\\uDD52-\\uDEA5\\uDEA8-\\uDEC0\\uDEC2-\\uDEDA\\uDEDC-\\uDEFA\\uDEFC-\\uDF14\\uDF16-\\uDF34\\uDF36-\\uDF4E\\uDF50-\\uDF6E\\uDF70-\\uDF88\\uDF8A-\\uDFA8\\uDFAA-\\uDFC2\\uDFC4-\\uDFCB\\uDFCE-\\uDFFF]|\\uD83A[\\uDC00-\\uDCC4\\uDCD0-\\uDCD6]|\\uD83B[\\uDE00-\\uDE03\\uDE05-\\uDE1F\\uDE21\\uDE22\\uDE24\\uDE27\\uDE29-\\uDE32\\uDE34-\\uDE37\\uDE39\\uDE3B\\uDE42\\uDE47\\uDE49\\uDE4B\\uDE4D-\\uDE4F\\uDE51\\uDE52\\uDE54\\uDE57\\uDE59\\uDE5B\\uDE5D\\uDE5F\\uDE61\\uDE62\\uDE64\\uDE67-\\uDE6A\\uDE6C-\\uDE72\\uDE74-\\uDE77\\uDE79-\\uDE7C\\uDE7E\\uDE80-\\uDE89\\uDE8B-\\uDE9B\\uDEA1-\\uDEA3\\uDEA5-\\uDEA9\\uDEAB-\\uDEBB]|\\uD869[\\uDC00-\\uDED6\\uDF00-\\uDFFF]|\\uD86D[\\uDC00-\\uDF34\\uDF40-\\uDFFF]|\\uD86E[\\uDC00-\\uDC1D]|\\uD87E[\\uDC00-\\uDE1D]|\\uDB40[\\uDD00-\\uDDEF]/')})
    var.put(u'Regex', PyJs_Object_7_)
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    @Js
    def PyJs_anonymous_50_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'comment', u'leadingComments', u'last', u'bottomRight', u'i', u'trailingComments', u'lastChild'])
        var.put(u'bottomRight', var.get(u'extra').get(u'bottomRightStack'))
        var.put(u'last', var.get(u'bottomRight').get((var.get(u'bottomRight').get(u'length')-Js(1.0))))
        if PyJsStrictEq(var.get(u"this").get(u'type'),var.get(u'Syntax').get(u'Program')):
            if (var.get(u"this").get(u'body').get(u'length')>Js(0.0)):
                return var.get('undefined')
        if (var.get(u'extra').get(u'trailingComments').get(u'length')>Js(0.0)):
            var.put(u'trailingComments', Js([]))
            #for JS loop
            var.put(u'i', (var.get(u'extra').get(u'trailingComments').get(u'length')-Js(1.0)))
            while (var.get(u'i')>=Js(0.0)):
                try:
                    var.put(u'comment', var.get(u'extra').get(u'trailingComments').get(var.get(u'i')))
                    if (var.get(u'comment').get(u'range').get(u'0')>=var.get(u"this").get(u'range').get(u'1')):
                        var.get(u'trailingComments').callprop(u'unshift', var.get(u'comment'))
                        var.get(u'extra').get(u'trailingComments').callprop(u'splice', var.get(u'i'), Js(1.0))
                finally:
                        var.put(u'i',Js(var.get(u'i').to_number())-Js(1))
            var.get(u'extra').put(u'trailingComments', Js([]))
        else:
            if ((var.get(u'last') and var.get(u'last').get(u'trailingComments')) and (var.get(u'last').get(u'trailingComments').get(u'0').get(u'range').get(u'0')>=var.get(u"this").get(u'range').get(u'1'))):
                var.put(u'trailingComments', var.get(u'last').get(u'trailingComments'))
                var.get(u'last').delete(u'trailingComments')
        while (var.get(u'last') and (var.get(u'last').get(u'range').get(u'0')>=var.get(u"this").get(u'range').get(u'0'))):
            var.put(u'lastChild', var.get(u'bottomRight').callprop(u'pop'))
            var.put(u'last', var.get(u'bottomRight').get((var.get(u'bottomRight').get(u'length')-Js(1.0))))
        if var.get(u'lastChild'):
            if var.get(u'lastChild').get(u'leadingComments'):
                var.put(u'leadingComments', Js([]))
                #for JS loop
                var.put(u'i', (var.get(u'lastChild').get(u'leadingComments').get(u'length')-Js(1.0)))
                while (var.get(u'i')>=Js(0.0)):
                    try:
                        var.put(u'comment', var.get(u'lastChild').get(u'leadingComments').get(var.get(u'i')))
                        if (var.get(u'comment').get(u'range').get(u'1')<=var.get(u"this").get(u'range').get(u'0')):
                            var.get(u'leadingComments').callprop(u'unshift', var.get(u'comment'))
                            var.get(u'lastChild').get(u'leadingComments').callprop(u'splice', var.get(u'i'), Js(1.0))
                    finally:
                            var.put(u'i',Js(var.get(u'i').to_number())-Js(1))
                if var.get(u'lastChild').get(u'leadingComments').get(u'length').neg():
                    var.get(u'lastChild').put(u'leadingComments', var.get(u'undefined'))
        else:
            if (var.get(u'extra').get(u'leadingComments').get(u'length')>Js(0.0)):
                var.put(u'leadingComments', Js([]))
                #for JS loop
                var.put(u'i', (var.get(u'extra').get(u'leadingComments').get(u'length')-Js(1.0)))
                while (var.get(u'i')>=Js(0.0)):
                    try:
                        var.put(u'comment', var.get(u'extra').get(u'leadingComments').get(var.get(u'i')))
                        if (var.get(u'comment').get(u'range').get(u'1')<=var.get(u"this").get(u'range').get(u'0')):
                            var.get(u'leadingComments').callprop(u'unshift', var.get(u'comment'))
                            var.get(u'extra').get(u'leadingComments').callprop(u'splice', var.get(u'i'), Js(1.0))
                    finally:
                            var.put(u'i',Js(var.get(u'i').to_number())-Js(1))
        if (var.get(u'leadingComments') and (var.get(u'leadingComments').get(u'length')>Js(0.0))):
            var.get(u"this").put(u'leadingComments', var.get(u'leadingComments'))
        if (var.get(u'trailingComments') and (var.get(u'trailingComments').get(u'length')>Js(0.0))):
            var.get(u"this").put(u'trailingComments', var.get(u'trailingComments'))
        var.get(u'bottomRight').callprop(u'push', var.get(u"this"))
    PyJs_anonymous_50_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_51_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        if var.get(u'extra').get(u'range'):
            var.get(u"this").get(u'range').put(u'1', var.get(u'lastIndex'))
        if var.get(u'extra').get(u'loc'):
            PyJs_Object_52_ = Js({u'line':var.get(u'lastLineNumber'),u'column':(var.get(u'lastIndex')-var.get(u'lastLineStart'))})
            var.get(u"this").get(u'loc').put(u'end', PyJs_Object_52_)
            if var.get(u'extra').get(u'source'):
                var.get(u"this").get(u'loc').put(u'source', var.get(u'extra').get(u'source'))
        if var.get(u'extra').get(u'attachComment'):
            var.get(u"this").callprop(u'processComment')
    PyJs_anonymous_51_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_53_(elements, this, arguments, var=var):
        var = Scope({u'this':this, u'elements':elements, u'arguments':arguments}, var)
        var.registers([u'elements'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ArrayExpression'))
        var.get(u"this").put(u'elements', var.get(u'elements'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_53_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_54_(elements, this, arguments, var=var):
        var = Scope({u'this':this, u'elements':elements, u'arguments':arguments}, var)
        var.registers([u'elements'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ArrayPattern'))
        var.get(u"this").put(u'elements', var.get(u'elements'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_54_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_55_(params, defaults, body, expression, this, arguments, var=var):
        var = Scope({u'body':body, u'params':params, u'arguments':arguments, u'defaults':defaults, u'this':this, u'expression':expression}, var)
        var.registers([u'body', u'expression', u'params', u'defaults'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ArrowFunctionExpression'))
        var.get(u"this").put(u'id', var.get(u"null"))
        var.get(u"this").put(u'params', var.get(u'params'))
        var.get(u"this").put(u'defaults', var.get(u'defaults'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").put(u'generator', Js(False))
        var.get(u"this").put(u'expression', var.get(u'expression'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_55_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_56_(operator, left, right, this, arguments, var=var):
        var = Scope({u'operator':operator, u'this':this, u'right':right, u'arguments':arguments, u'left':left}, var)
        var.registers([u'operator', u'right', u'left'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'AssignmentExpression'))
        var.get(u"this").put(u'operator', var.get(u'operator'))
        var.get(u"this").put(u'left', var.get(u'left'))
        var.get(u"this").put(u'right', var.get(u'right'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_56_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_57_(left, right, this, arguments, var=var):
        var = Scope({u'this':this, u'right':right, u'arguments':arguments, u'left':left}, var)
        var.registers([u'right', u'left'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'AssignmentPattern'))
        var.get(u"this").put(u'left', var.get(u'left'))
        var.get(u"this").put(u'right', var.get(u'right'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_57_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_58_(operator, left, right, this, arguments, var=var):
        var = Scope({u'operator':operator, u'this':this, u'right':right, u'arguments':arguments, u'left':left}, var)
        var.registers([u'operator', u'right', u'left'])
        var.get(u"this").put(u'type', (var.get(u'Syntax').get(u'LogicalExpression') if (PyJsStrictEq(var.get(u'operator'),Js(u'||')) or PyJsStrictEq(var.get(u'operator'),Js(u'&&'))) else var.get(u'Syntax').get(u'BinaryExpression')))
        var.get(u"this").put(u'operator', var.get(u'operator'))
        var.get(u"this").put(u'left', var.get(u'left'))
        var.get(u"this").put(u'right', var.get(u'right'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_58_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_59_(body, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'arguments':arguments}, var)
        var.registers([u'body'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'BlockStatement'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_59_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_60_(label, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'label':label}, var)
        var.registers([u'label'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'BreakStatement'))
        var.get(u"this").put(u'label', var.get(u'label'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_60_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_61_(callee, args, this, arguments, var=var):
        var = Scope({u'this':this, u'args':args, u'callee':callee, u'arguments':arguments}, var)
        var.registers([u'args', u'callee'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'CallExpression'))
        var.get(u"this").put(u'callee', var.get(u'callee'))
        var.get(u"this").put(u'arguments', var.get(u'args'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_61_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_62_(param, body, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'arguments':arguments, u'param':param}, var)
        var.registers([u'body', u'param'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'CatchClause'))
        var.get(u"this").put(u'param', var.get(u'param'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_62_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_63_(body, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'arguments':arguments}, var)
        var.registers([u'body'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ClassBody'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_63_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_64_(id, superClass, body, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'id':id, u'arguments':arguments, u'superClass':superClass}, var)
        var.registers([u'body', u'id', u'superClass'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ClassDeclaration'))
        var.get(u"this").put(u'id', var.get(u'id'))
        var.get(u"this").put(u'superClass', var.get(u'superClass'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_64_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_65_(id, superClass, body, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'id':id, u'arguments':arguments, u'superClass':superClass}, var)
        var.registers([u'body', u'id', u'superClass'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ClassExpression'))
        var.get(u"this").put(u'id', var.get(u'id'))
        var.get(u"this").put(u'superClass', var.get(u'superClass'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_65_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_66_(test, consequent, alternate, this, arguments, var=var):
        var = Scope({u'test':test, u'this':this, u'alternate':alternate, u'arguments':arguments, u'consequent':consequent}, var)
        var.registers([u'test', u'alternate', u'consequent'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ConditionalExpression'))
        var.get(u"this").put(u'test', var.get(u'test'))
        var.get(u"this").put(u'consequent', var.get(u'consequent'))
        var.get(u"this").put(u'alternate', var.get(u'alternate'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_66_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_67_(label, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'label':label}, var)
        var.registers([u'label'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ContinueStatement'))
        var.get(u"this").put(u'label', var.get(u'label'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_67_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_68_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'DebuggerStatement'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_68_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_69_(body, test, this, arguments, var=var):
        var = Scope({u'body':body, u'test':test, u'this':this, u'arguments':arguments}, var)
        var.registers([u'body', u'test'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'DoWhileStatement'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").put(u'test', var.get(u'test'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_69_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_70_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'EmptyStatement'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_70_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_71_(expression, this, arguments, var=var):
        var = Scope({u'this':this, u'expression':expression, u'arguments':arguments}, var)
        var.registers([u'expression'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ExpressionStatement'))
        var.get(u"this").put(u'expression', var.get(u'expression'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_71_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_72_(init, test, update, body, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'init':init, u'arguments':arguments, u'test':test, u'update':update}, var)
        var.registers([u'test', u'body', u'init', u'update'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ForStatement'))
        var.get(u"this").put(u'init', var.get(u'init'))
        var.get(u"this").put(u'test', var.get(u'test'))
        var.get(u"this").put(u'update', var.get(u'update'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_72_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_73_(left, right, body, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'right':right, u'arguments':arguments, u'left':left}, var)
        var.registers([u'body', u'right', u'left'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ForOfStatement'))
        var.get(u"this").put(u'left', var.get(u'left'))
        var.get(u"this").put(u'right', var.get(u'right'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_73_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_74_(left, right, body, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'right':right, u'arguments':arguments, u'left':left}, var)
        var.registers([u'body', u'right', u'left'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ForInStatement'))
        var.get(u"this").put(u'left', var.get(u'left'))
        var.get(u"this").put(u'right', var.get(u'right'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").put(u'each', Js(False))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_74_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_75_(id, params, defaults, body, generator, this, arguments, var=var):
        var = Scope({u'body':body, u'params':params, u'defaults':defaults, u'generator':generator, u'this':this, u'id':id, u'arguments':arguments}, var)
        var.registers([u'body', u'generator', u'params', u'id', u'defaults'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'FunctionDeclaration'))
        var.get(u"this").put(u'id', var.get(u'id'))
        var.get(u"this").put(u'params', var.get(u'params'))
        var.get(u"this").put(u'defaults', var.get(u'defaults'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").put(u'generator', var.get(u'generator'))
        var.get(u"this").put(u'expression', Js(False))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_75_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_76_(id, params, defaults, body, generator, this, arguments, var=var):
        var = Scope({u'body':body, u'params':params, u'defaults':defaults, u'generator':generator, u'this':this, u'id':id, u'arguments':arguments}, var)
        var.registers([u'body', u'generator', u'params', u'id', u'defaults'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'FunctionExpression'))
        var.get(u"this").put(u'id', var.get(u'id'))
        var.get(u"this").put(u'params', var.get(u'params'))
        var.get(u"this").put(u'defaults', var.get(u'defaults'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").put(u'generator', var.get(u'generator'))
        var.get(u"this").put(u'expression', Js(False))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_76_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_77_(name, this, arguments, var=var):
        var = Scope({u'this':this, u'name':name, u'arguments':arguments}, var)
        var.registers([u'name'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'Identifier'))
        var.get(u"this").put(u'name', var.get(u'name'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_77_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_78_(test, consequent, alternate, this, arguments, var=var):
        var = Scope({u'test':test, u'this':this, u'alternate':alternate, u'arguments':arguments, u'consequent':consequent}, var)
        var.registers([u'test', u'alternate', u'consequent'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'IfStatement'))
        var.get(u"this").put(u'test', var.get(u'test'))
        var.get(u"this").put(u'consequent', var.get(u'consequent'))
        var.get(u"this").put(u'alternate', var.get(u'alternate'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_78_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_79_(label, body, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'arguments':arguments, u'label':label}, var)
        var.registers([u'body', u'label'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'LabeledStatement'))
        var.get(u"this").put(u'label', var.get(u'label'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_79_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_80_(token, this, arguments, var=var):
        var = Scope({u'this':this, u'token':token, u'arguments':arguments}, var)
        var.registers([u'token'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'Literal'))
        var.get(u"this").put(u'value', var.get(u'token').get(u'value'))
        var.get(u"this").put(u'raw', var.get(u'source').callprop(u'slice', var.get(u'token').get(u'start'), var.get(u'token').get(u'end')))
        if var.get(u'token').get(u'regex'):
            var.get(u"this").put(u'regex', var.get(u'token').get(u'regex'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_80_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_81_(accessor, object, property, this, arguments, var=var):
        var = Scope({u'this':this, u'property':property, u'object':object, u'accessor':accessor, u'arguments':arguments}, var)
        var.registers([u'property', u'object', u'accessor'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'MemberExpression'))
        var.get(u"this").put(u'computed', PyJsStrictEq(var.get(u'accessor'),Js(u'[')))
        var.get(u"this").put(u'object', var.get(u'object'))
        var.get(u"this").put(u'property', var.get(u'property'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_81_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_82_(meta, property, this, arguments, var=var):
        var = Scope({u'this':this, u'property':property, u'meta':meta, u'arguments':arguments}, var)
        var.registers([u'property', u'meta'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'MetaProperty'))
        var.get(u"this").put(u'meta', var.get(u'meta'))
        var.get(u"this").put(u'property', var.get(u'property'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_82_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_83_(callee, args, this, arguments, var=var):
        var = Scope({u'this':this, u'args':args, u'callee':callee, u'arguments':arguments}, var)
        var.registers([u'args', u'callee'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'NewExpression'))
        var.get(u"this").put(u'callee', var.get(u'callee'))
        var.get(u"this").put(u'arguments', var.get(u'args'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_83_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_84_(properties, this, arguments, var=var):
        var = Scope({u'this':this, u'properties':properties, u'arguments':arguments}, var)
        var.registers([u'properties'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ObjectExpression'))
        var.get(u"this").put(u'properties', var.get(u'properties'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_84_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_85_(properties, this, arguments, var=var):
        var = Scope({u'this':this, u'properties':properties, u'arguments':arguments}, var)
        var.registers([u'properties'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ObjectPattern'))
        var.get(u"this").put(u'properties', var.get(u'properties'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_85_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_86_(operator, argument, this, arguments, var=var):
        var = Scope({u'operator':operator, u'this':this, u'argument':argument, u'arguments':arguments}, var)
        var.registers([u'operator', u'argument'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'UpdateExpression'))
        var.get(u"this").put(u'operator', var.get(u'operator'))
        var.get(u"this").put(u'argument', var.get(u'argument'))
        var.get(u"this").put(u'prefix', Js(False))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_86_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_87_(body, sourceType, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'sourceType':sourceType, u'arguments':arguments}, var)
        var.registers([u'body', u'sourceType'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'Program'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").put(u'sourceType', var.get(u'sourceType'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_87_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_88_(kind, key, computed, value, method, shorthand, this, arguments, var=var):
        var = Scope({u'kind':kind, u'shorthand':shorthand, u'computed':computed, u'this':this, u'value':value, u'arguments':arguments, u'key':key, u'method':method}, var)
        var.registers([u'kind', u'shorthand', u'computed', u'value', u'key', u'method'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'Property'))
        var.get(u"this").put(u'key', var.get(u'key'))
        var.get(u"this").put(u'computed', var.get(u'computed'))
        var.get(u"this").put(u'value', var.get(u'value'))
        var.get(u"this").put(u'kind', var.get(u'kind'))
        var.get(u"this").put(u'method', var.get(u'method'))
        var.get(u"this").put(u'shorthand', var.get(u'shorthand'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_88_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_89_(argument, this, arguments, var=var):
        var = Scope({u'this':this, u'argument':argument, u'arguments':arguments}, var)
        var.registers([u'argument'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'RestElement'))
        var.get(u"this").put(u'argument', var.get(u'argument'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_89_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_90_(argument, this, arguments, var=var):
        var = Scope({u'this':this, u'argument':argument, u'arguments':arguments}, var)
        var.registers([u'argument'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ReturnStatement'))
        var.get(u"this").put(u'argument', var.get(u'argument'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_90_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_91_(expressions, this, arguments, var=var):
        var = Scope({u'this':this, u'expressions':expressions, u'arguments':arguments}, var)
        var.registers([u'expressions'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'SequenceExpression'))
        var.get(u"this").put(u'expressions', var.get(u'expressions'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_91_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_92_(argument, this, arguments, var=var):
        var = Scope({u'this':this, u'argument':argument, u'arguments':arguments}, var)
        var.registers([u'argument'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'SpreadElement'))
        var.get(u"this").put(u'argument', var.get(u'argument'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_92_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_93_(test, consequent, this, arguments, var=var):
        var = Scope({u'test':test, u'this':this, u'arguments':arguments, u'consequent':consequent}, var)
        var.registers([u'test', u'consequent'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'SwitchCase'))
        var.get(u"this").put(u'test', var.get(u'test'))
        var.get(u"this").put(u'consequent', var.get(u'consequent'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_93_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_94_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'Super'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_94_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_95_(discriminant, cases, this, arguments, var=var):
        var = Scope({u'this':this, u'cases':cases, u'arguments':arguments, u'discriminant':discriminant}, var)
        var.registers([u'cases', u'discriminant'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'SwitchStatement'))
        var.get(u"this").put(u'discriminant', var.get(u'discriminant'))
        var.get(u"this").put(u'cases', var.get(u'cases'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_95_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_96_(tag, quasi, this, arguments, var=var):
        var = Scope({u'this':this, u'quasi':quasi, u'tag':tag, u'arguments':arguments}, var)
        var.registers([u'quasi', u'tag'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'TaggedTemplateExpression'))
        var.get(u"this").put(u'tag', var.get(u'tag'))
        var.get(u"this").put(u'quasi', var.get(u'quasi'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_96_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_97_(value, tail, this, arguments, var=var):
        var = Scope({u'this':this, u'tail':tail, u'arguments':arguments, u'value':value}, var)
        var.registers([u'tail', u'value'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'TemplateElement'))
        var.get(u"this").put(u'value', var.get(u'value'))
        var.get(u"this").put(u'tail', var.get(u'tail'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_97_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_98_(quasis, expressions, this, arguments, var=var):
        var = Scope({u'quasis':quasis, u'this':this, u'expressions':expressions, u'arguments':arguments}, var)
        var.registers([u'quasis', u'expressions'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'TemplateLiteral'))
        var.get(u"this").put(u'quasis', var.get(u'quasis'))
        var.get(u"this").put(u'expressions', var.get(u'expressions'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_98_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_99_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ThisExpression'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_99_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_100_(argument, this, arguments, var=var):
        var = Scope({u'this':this, u'argument':argument, u'arguments':arguments}, var)
        var.registers([u'argument'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ThrowStatement'))
        var.get(u"this").put(u'argument', var.get(u'argument'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_100_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_101_(block, handler, finalizer, this, arguments, var=var):
        var = Scope({u'this':this, u'finalizer':finalizer, u'handler':handler, u'arguments':arguments, u'block':block}, var)
        var.registers([u'finalizer', u'handler', u'block'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'TryStatement'))
        var.get(u"this").put(u'block', var.get(u'block'))
        var.get(u"this").put(u'guardedHandlers', Js([]))
        var.get(u"this").put(u'handlers', (Js([var.get(u'handler')]) if var.get(u'handler') else Js([])))
        var.get(u"this").put(u'handler', var.get(u'handler'))
        var.get(u"this").put(u'finalizer', var.get(u'finalizer'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_101_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_102_(operator, argument, this, arguments, var=var):
        var = Scope({u'operator':operator, u'this':this, u'argument':argument, u'arguments':arguments}, var)
        var.registers([u'operator', u'argument'])
        var.get(u"this").put(u'type', (var.get(u'Syntax').get(u'UpdateExpression') if (PyJsStrictEq(var.get(u'operator'),Js(u'++')) or PyJsStrictEq(var.get(u'operator'),Js(u'--'))) else var.get(u'Syntax').get(u'UnaryExpression')))
        var.get(u"this").put(u'operator', var.get(u'operator'))
        var.get(u"this").put(u'argument', var.get(u'argument'))
        var.get(u"this").put(u'prefix', var.get(u'true'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_102_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_103_(declarations, this, arguments, var=var):
        var = Scope({u'this':this, u'declarations':declarations, u'arguments':arguments}, var)
        var.registers([u'declarations'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'VariableDeclaration'))
        var.get(u"this").put(u'declarations', var.get(u'declarations'))
        var.get(u"this").put(u'kind', Js(u'var'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_103_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_104_(declarations, kind, this, arguments, var=var):
        var = Scope({u'this':this, u'kind':kind, u'declarations':declarations, u'arguments':arguments}, var)
        var.registers([u'kind', u'declarations'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'VariableDeclaration'))
        var.get(u"this").put(u'declarations', var.get(u'declarations'))
        var.get(u"this").put(u'kind', var.get(u'kind'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_104_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_105_(id, init, this, arguments, var=var):
        var = Scope({u'this':this, u'init':init, u'id':id, u'arguments':arguments}, var)
        var.registers([u'init', u'id'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'VariableDeclarator'))
        var.get(u"this").put(u'id', var.get(u'id'))
        var.get(u"this").put(u'init', var.get(u'init'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_105_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_106_(test, body, this, arguments, var=var):
        var = Scope({u'test':test, u'body':body, u'this':this, u'arguments':arguments}, var)
        var.registers([u'test', u'body'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'WhileStatement'))
        var.get(u"this").put(u'test', var.get(u'test'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_106_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_107_(object, body, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'object':object, u'arguments':arguments}, var)
        var.registers([u'body', u'object'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'WithStatement'))
        var.get(u"this").put(u'object', var.get(u'object'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_107_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_108_(local, exported, this, arguments, var=var):
        var = Scope({u'this':this, u'local':local, u'exported':exported, u'arguments':arguments}, var)
        var.registers([u'local', u'exported'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ExportSpecifier'))
        var.get(u"this").put(u'exported', (var.get(u'exported') or var.get(u'local')))
        var.get(u"this").put(u'local', var.get(u'local'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_108_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_109_(local, this, arguments, var=var):
        var = Scope({u'this':this, u'local':local, u'arguments':arguments}, var)
        var.registers([u'local'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ImportDefaultSpecifier'))
        var.get(u"this").put(u'local', var.get(u'local'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_109_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_110_(local, this, arguments, var=var):
        var = Scope({u'this':this, u'local':local, u'arguments':arguments}, var)
        var.registers([u'local'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ImportNamespaceSpecifier'))
        var.get(u"this").put(u'local', var.get(u'local'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_110_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_111_(declaration, specifiers, src, this, arguments, var=var):
        var = Scope({u'this':this, u'specifiers':specifiers, u'src':src, u'arguments':arguments, u'declaration':declaration}, var)
        var.registers([u'specifiers', u'src', u'declaration'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ExportNamedDeclaration'))
        var.get(u"this").put(u'declaration', var.get(u'declaration'))
        var.get(u"this").put(u'specifiers', var.get(u'specifiers'))
        var.get(u"this").put(u'source', var.get(u'src'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_111_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_112_(declaration, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'declaration':declaration}, var)
        var.registers([u'declaration'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ExportDefaultDeclaration'))
        var.get(u"this").put(u'declaration', var.get(u'declaration'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_112_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_113_(src, this, arguments, var=var):
        var = Scope({u'this':this, u'src':src, u'arguments':arguments}, var)
        var.registers([u'src'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ExportAllDeclaration'))
        var.get(u"this").put(u'source', var.get(u'src'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_113_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_114_(local, imported, this, arguments, var=var):
        var = Scope({u'this':this, u'imported':imported, u'local':local, u'arguments':arguments}, var)
        var.registers([u'imported', u'local'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ImportSpecifier'))
        var.get(u"this").put(u'local', (var.get(u'local') or var.get(u'imported')))
        var.get(u"this").put(u'imported', var.get(u'imported'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_114_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_115_(specifiers, src, this, arguments, var=var):
        var = Scope({u'this':this, u'specifiers':specifiers, u'arguments':arguments, u'src':src}, var)
        var.registers([u'specifiers', u'src'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ImportDeclaration'))
        var.get(u"this").put(u'specifiers', var.get(u'specifiers'))
        var.get(u"this").put(u'source', var.get(u'src'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_115_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_116_(argument, delegate, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'argument':argument, u'delegate':delegate}, var)
        var.registers([u'argument', u'delegate'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'YieldExpression'))
        var.get(u"this").put(u'argument', var.get(u'argument'))
        var.get(u"this").put(u'delegate', var.get(u'delegate'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_116_._set_name(u'anonymous')
    PyJs_Object_49_ = Js({u'processComment':PyJs_anonymous_50_,u'finish':PyJs_anonymous_51_,u'finishArrayExpression':PyJs_anonymous_53_,u'finishArrayPattern':PyJs_anonymous_54_,u'finishArrowFunctionExpression':PyJs_anonymous_55_,u'finishAssignmentExpression':PyJs_anonymous_56_,u'finishAssignmentPattern':PyJs_anonymous_57_,u'finishBinaryExpression':PyJs_anonymous_58_,u'finishBlockStatement':PyJs_anonymous_59_,u'finishBreakStatement':PyJs_anonymous_60_,u'finishCallExpression':PyJs_anonymous_61_,u'finishCatchClause':PyJs_anonymous_62_,u'finishClassBody':PyJs_anonymous_63_,u'finishClassDeclaration':PyJs_anonymous_64_,u'finishClassExpression':PyJs_anonymous_65_,u'finishConditionalExpression':PyJs_anonymous_66_,u'finishContinueStatement':PyJs_anonymous_67_,u'finishDebuggerStatement':PyJs_anonymous_68_,u'finishDoWhileStatement':PyJs_anonymous_69_,u'finishEmptyStatement':PyJs_anonymous_70_,u'finishExpressionStatement':PyJs_anonymous_71_,u'finishForStatement':PyJs_anonymous_72_,u'finishForOfStatement':PyJs_anonymous_73_,u'finishForInStatement':PyJs_anonymous_74_,u'finishFunctionDeclaration':PyJs_anonymous_75_,u'finishFunctionExpression':PyJs_anonymous_76_,u'finishIdentifier':PyJs_anonymous_77_,u'finishIfStatement':PyJs_anonymous_78_,u'finishLabeledStatement':PyJs_anonymous_79_,u'finishLiteral':PyJs_anonymous_80_,u'finishMemberExpression':PyJs_anonymous_81_,u'finishMetaProperty':PyJs_anonymous_82_,u'finishNewExpression':PyJs_anonymous_83_,u'finishObjectExpression':PyJs_anonymous_84_,u'finishObjectPattern':PyJs_anonymous_85_,u'finishPostfixExpression':PyJs_anonymous_86_,u'finishProgram':PyJs_anonymous_87_,u'finishProperty':PyJs_anonymous_88_,u'finishRestElement':PyJs_anonymous_89_,u'finishReturnStatement':PyJs_anonymous_90_,u'finishSequenceExpression':PyJs_anonymous_91_,u'finishSpreadElement':PyJs_anonymous_92_,u'finishSwitchCase':PyJs_anonymous_93_,u'finishSuper':PyJs_anonymous_94_,u'finishSwitchStatement':PyJs_anonymous_95_,u'finishTaggedTemplateExpression':PyJs_anonymous_96_,u'finishTemplateElement':PyJs_anonymous_97_,u'finishTemplateLiteral':PyJs_anonymous_98_,u'finishThisExpression':PyJs_anonymous_99_,u'finishThrowStatement':PyJs_anonymous_100_,u'finishTryStatement':PyJs_anonymous_101_,u'finishUnaryExpression':PyJs_anonymous_102_,u'finishVariableDeclaration':PyJs_anonymous_103_,u'finishLexicalDeclaration':PyJs_anonymous_104_,u'finishVariableDeclarator':PyJs_anonymous_105_,u'finishWhileStatement':PyJs_anonymous_106_,u'finishWithStatement':PyJs_anonymous_107_,u'finishExportSpecifier':PyJs_anonymous_108_,u'finishImportDefaultSpecifier':PyJs_anonymous_109_,u'finishImportNamespaceSpecifier':PyJs_anonymous_110_,u'finishExportNamedDeclaration':PyJs_anonymous_111_,u'finishExportDefaultDeclaration':PyJs_anonymous_112_,u'finishExportAllDeclaration':PyJs_anonymous_113_,u'finishImportSpecifier':PyJs_anonymous_114_,u'finishImportDeclaration':PyJs_anonymous_115_,u'finishYieldExpression':PyJs_anonymous_116_})
    var.get(u'WrappingNode').put(u'prototype', var.get(u'Node').put(u'prototype', PyJs_Object_49_))
    var.get(u'exports').put(u'version', Js(u'2.6.0'))
    var.get(u'exports').put(u'tokenize', var.get(u'tokenize'))
    var.get(u'exports').put(u'parse', var.get(u'parse'))
    @Js
    def PyJs_anonymous_160_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'name', u'types'])
        PyJs_Object_161_ = Js({})
        var.put(u'types', PyJs_Object_161_)
        if PyJsStrictEq(var.get(u'Object').get(u'create').typeof(),Js(u'function')):
            var.put(u'types', var.get(u'Object').callprop(u'create', var.get(u"null")))
        for PyJsTemp in var.get(u'Syntax'):
            var.put(u'name', PyJsTemp)
            if var.get(u'Syntax').callprop(u'hasOwnProperty', var.get(u'name')):
                var.get(u'types').put(var.get(u'name'), var.get(u'Syntax').get(var.get(u'name')))
        if PyJsStrictEq(var.get(u'Object').get(u'freeze').typeof(),Js(u'function')):
            var.get(u'Object').callprop(u'freeze', var.get(u'types'))
        return var.get(u'types')
    PyJs_anonymous_160_._set_name(u'anonymous')
    var.get(u'exports').put(u'Syntax', PyJs_anonymous_160_())
PyJs_anonymous_0_._set_name(u'anonymous')
@Js
def PyJs_anonymous_162_(root, factory, this, arguments, var=var):
    var = Scope({u'this':this, u'root':root, u'factory':factory, u'arguments':arguments}, var)
    var.registers([u'root', u'factory'])
    Js(u'use strict')
    if (PyJsStrictEq(var.get(u'define',throw=False).typeof(),Js(u'function')) and var.get(u'define').get(u'amd')):
        var.get(u'define')(Js([Js(u'exports')]), var.get(u'factory'))
    else:
        if PyJsStrictNeq(var.get(u'exports',throw=False).typeof(),Js(u'undefined')):
            var.get(u'factory')(var.get(u'exports'))
        else:
            PyJs_Object_163_ = Js({})
            var.get(u'factory')(var.get(u'root').put(u'esprima', PyJs_Object_163_))
PyJs_anonymous_162_._set_name(u'anonymous')
PyJs_anonymous_162_(var.get(u"this"), PyJs_anonymous_0_)
pass


# Added manually
esprima = var.to_python().esprima # this will now behave exactly like JS esprima object

if __name__=='__main__':

    JSON = var.to_python().JSON
    print('version', esprima.version)

    print('parsing var odds = evens.map(v => v + 1);')
    tree = esprima.parse('var odds = evens.map(v => v + 1);')
    py_tree = tree.to_dict()

    print(JSON.stringify(py_tree, None, 4))

    another_tree = esprima.parse('export var answer = 42', {'sourceType': 'module' })
    print(JSON.stringify(another_tree, None, 4))



