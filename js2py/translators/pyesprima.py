""" Usage:

tree = esprima.parse('var a = 10')

You can convert tree to python dict if you want:

tree.to_dict()
"""

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:var.registers([])
@Js
def PyJs_anonymous_0_(exports, this, arguments, var=var):
    var = Scope({u'this':this, u'exports':exports, u'arguments':arguments}, var)
    var.registers([u'isKeyword', u'isolateCoverGrammar', u'consumeSemicolon', u'parseLeftHandSideExpression', u'throwUnexpectedToken', u'parsePatternWithDefault', u'parseExpressionStatement', u'advanceSlash', u'lastLineStart', u'tolerateUnexpectedToken', u'WrappingSourceLocation', u'source', u'parseThrowStatement', u'addComment', u'parseSwitchStatement', u'match', u'parseEmptyStatement', u'validateParam', u'exports', u'parseConditionalExpression', u'parseStatementListItem', u'parseClassDeclaration', u'Messages', u'isAssignmentTarget', u'parseVariableDeclaration', u'Token', u'reinterpretExpressionAsPattern', u'Position', u'isWhiteSpace', u'parseWhileStatement', u'scanIdentifier', u'parseTemplateLiteral', u'parseTemplateElement', u'parseGroupExpression', u'scanHexLiteral', u'parseBreakStatement', u'scanBinaryLiteral', u'firstCoverInitializedNameError', u'expectCommaSeparator', u'parseParams', u'getEscapedIdentifier', u'SourceLocation', u'parsePrimaryExpression', u'FnExprTokens', u'scanning', u'scanRegExpFlags', u'parseImportDeclaration', u'parseVariableDeclarationList', u'parseFunctionExpression', u'parseReturnStatement', u'recordError', u'parseExportAllDeclaration', u'collectRegex', u'expect', u'skipMultiLineComment', u'scanNumericLiteral', u'index', u'isIdentifierStart', u'parsePropertyMethodFunction', u'parseProgram', u'isImplicitOctalLiteral', u'state', u'isOctalDigit', u'isDecimalDigit', u'parseClassExpression', u'parseObjectProperty', u'parseCatchClause', u'peek', u'parseArguments', u'testRegExp', u'octalToDecimal', u'parseExportDeclaration', u'parseStatement', u'lastLineNumber', u'isLineTerminator', u'parseStatementList', u'parseModuleSpecifier', u'lex', u'parseFunctionSourceElements', u'isIdentifierName', u'advance', u'inheritCoverGrammar', u'isBindingElement', u'TokenName', u'parseArrayInitialiser', u'reinterpretAsCoverFormalsList', u'length', u'parseObjectInitialiser', u'isFutureReservedWord', u'parseImportNamespaceSpecifier', u'parseUnaryExpression', u'parseAssignmentExpression', u'Regex', u'parseLexicalBinding', u'tolerateError', u'parseBinaryExpression', u'startLineNumber', u'extra', u'scanStringLiteral', u'parseNamedImports', u'unexpectedTokenError', u'parseNonComputedProperty', u'startIndex', u'startLineStart', u'parseParam', u'parseNewExpression', u'scanRegExpBody', u'Node', u'collectToken', u'parseWithStatement', u'parseDebuggerStatement', u'parseObjectPattern', u'parseImportSpecifier', u'skipComment', u'parseVariableStatement', u'strict', u'lookaheadPropertyName', u'tokenize', u'parseVariableIdentifier', u'parseExpression', u'parseObjectPropertyKey', u'parseArrayPattern', u'expectKeyword', u'assert', u'lineNumber', u'parseConciseBody', u'createError', u'parseLeftHandSideExpressionAllowCall', u'hasLineTerminator', u'parseExportNamedDeclaration', u'parseBlock', u'Syntax', u'parseExportSpecifier', u'skipSingleLineComment', u'parseDoWhileStatement', u'scanHexEscape', u'isHexDigit', u'matchContextualKeyword', u'isStrictModeReservedWord', u'binaryPrecedence', u'parse', u'matchAssign', u'WrappingNode', u'getIdentifier', u'isRestrictedWord', u'parseSwitchCase', u'parsePropertyPattern', u'parseIfStatement', u'parseFunctionDeclaration', u'parsePostfixExpression', u'parseNonComputedMember', u'parseExportDefaultDeclaration', u'lastIndex', u'parseRestElement', u'parseScriptBody', u'parseBindingList', u'scanTemplate', u'PlaceHolders', u'parseLexicalDeclaration', u'checkProto', u'checkPatternParam', u'parsePropertyFunction', u'sourceType', u'scanPunctuator', u'parseArrowFunctionExpression', u'throwError', u'scanUnicodeCodePointEscape', u'scanOctalLiteral', u'scanRegExp', u'parseImportDefaultSpecifier', u'parsePattern', u'lineStart', u'parseForStatement', u'isIdentifierPart', u'matchKeyword', u'lookahead', u'parseTryStatement', u'parseComputedMember', u'parseContinueStatement', u'tryParseMethodDefinition', u'parseClassBody', u'filterTokenLocation'])
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
    def PyJsHoisted_parsePatternWithDefault_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'startToken', u'right', u'pattern'])
        var.put(u'startToken', var.get(u'lookahead'))
        var.put(u'pattern', var.get(u'parsePattern')())
        if var.get(u'match')(Js(u'=')):
            var.get(u'lex')()
            var.put(u'right', var.get(u'isolateCoverGrammar')(var.get(u'parseAssignmentExpression')))
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
        PyJs_Object_43_ = Js({u'line':var.get(u'startToken').get(u'lineNumber'),u'column':(var.get(u'startToken').get(u'start')-var.get(u'startToken').get(u'lineStart'))})
        var.get(u"this").put(u'start', PyJs_Object_43_)
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
        var.put(u'index',var.get(u'index')+Js(1))
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').get((var.put(u'index',var.get(u'index')+Js(1))-Js(1))))
            if PyJsStrictEq(var.get(u'ch'),var.get(u'quote')):
                var.put(u'quote', Js(u''))
                break
            else:
                if PyJsStrictEq(var.get(u'ch'),Js(u'\\')):
                    var.put(u'ch', var.get(u'source').get((var.put(u'index',var.get(u'index')+Js(1))-Js(1))))
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
                                    var.put(u'index',var.get(u'index')+Js(1))
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
                                PyJsTempException = JsToPyException(var.get(u'throwUnexpectedToken')())
                                raise PyJsTempException
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
                        var.put(u'lineNumber',var.get(u'lineNumber')+Js(1))
                        if (PyJsStrictEq(var.get(u'ch'),Js(u'\r')) and PyJsStrictEq(var.get(u'source').get(var.get(u'index')),Js(u'\n'))):
                            var.put(u'index',var.get(u'index')+Js(1))
                        var.put(u'lineStart', var.get(u'index'))
                else:
                    if var.get(u'isLineTerminator')(var.get(u'ch').callprop(u'charCodeAt', Js(0.0))):
                        break
                    else:
                        var.put(u'str', var.get(u'ch'), u'+')
        if PyJsStrictNeq(var.get(u'quote'),Js(u'')):
            var.get(u'throwUnexpectedToken')()
        PyJs_Object_23_ = Js({u'type':var.get(u'Token').get(u'StringLiteral'),u'value':var.get(u'str'),u'octal':var.get(u'octal'),u'lineNumber':var.get(u'startLineNumber'),u'lineStart':var.get(u'startLineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
        return PyJs_Object_23_
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
        PyJs_Object_8_ = Js({u'type':var.get(u'type'),u'value':var.get(u'value')})
        var.put(u'comment', PyJs_Object_8_)
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
                            var.get(u'options').put(u'firstRestricted', var.get(u'param'))
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
                    if PyJsStrictNeq(var.get(u'sourceType'),Js(u'module')):
                        var.get(u'tolerateUnexpectedToken')(var.get(u'lookahead'), var.get(u'Messages').get(u'IllegalExportDeclaration'))
                    return var.get(u'parseExportDeclaration')()
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'import')):
                    SWITCHED = True
                    if PyJsStrictNeq(var.get(u'sourceType'),Js(u'module')):
                        var.get(u'tolerateUnexpectedToken')(var.get(u'lookahead'), var.get(u'Messages').get(u'IllegalImportDeclaration'))
                    return var.get(u'parseImportDeclaration')()
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'const')):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'let')):
                    SWITCHED = True
                    PyJs_Object_125_ = Js({u'inFor':Js(False)})
                    return var.get(u'parseLexicalDeclaration')(PyJs_Object_125_)
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
    def PyJsHoisted_parseVariableDeclaration_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'init', u'id'])
        var.put(u'init', var.get(u"null"))
        var.put(u'node', var.get(u'Node').create())
        var.put(u'id', var.get(u'parsePattern')())
        if (var.get(u'strict') and var.get(u'isRestrictedWord')(var.get(u'id').get(u'name'))):
            var.get(u'tolerateError')(var.get(u'Messages').get(u'StrictVarName'))
        if var.get(u'match')(Js(u'=')):
            var.get(u'lex')()
            var.put(u'init', var.get(u'isolateCoverGrammar')(var.get(u'parseAssignmentExpression')))
        else:
            if PyJsStrictNeq(var.get(u'id').get(u'type'),var.get(u'Syntax').get(u'Identifier')):
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
                    if PyJsStrictNeq(var.get(u'expr').get(u'elements').get(var.get(u'i')),var.get(u"null")):
                        var.get(u'reinterpretExpressionAsPattern')(var.get(u'expr').get(u'elements').get(var.get(u'i')))
                    (var.put(u'i',var.get(u'i')+Js(1))-Js(1))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Syntax').get(u'ObjectExpression')):
                SWITCHED = True
                var.get(u'expr').put(u'type', var.get(u'Syntax').get(u'ObjectPattern'))
                #for JS loop
                var.put(u'i', Js(0.0))
                while (var.get(u'i')<var.get(u'expr').get(u'properties').get(u'length')):
                    var.get(u'reinterpretExpressionAsPattern')(var.get(u'expr').get(u'properties').get(var.get(u'i')).get(u'value'))
                    (var.put(u'i',var.get(u'i')+Js(1))-Js(1))
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
        return (((((PyJsStrictEq(var.get(u'ch'),Js(32)) or PyJsStrictEq(var.get(u'ch'),Js(9))) or PyJsStrictEq(var.get(u'ch'),Js(11))) or PyJsStrictEq(var.get(u'ch'),Js(12))) or PyJsStrictEq(var.get(u'ch'),Js(160))) or ((var.get(u'ch')>=Js(5760)) and (Js([Js(5760), Js(6158), Js(8192), Js(8193), Js(8194), Js(8195), Js(8196), Js(8197), Js(8198), Js(8199), Js(8200), Js(8201), Js(8202), Js(8239), Js(8287), Js(12288), Js(65279)]).callprop(u'indexOf', var.get(u'ch'))>=Js(0.0))))
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
        PyJs_Object_116_ = Js({u'head':var.get(u'true')})
        var.put(u'quasi', var.get(u'parseTemplateElement')(PyJs_Object_116_))
        var.put(u'quasis', Js([var.get(u'quasi')]))
        var.put(u'expressions', Js([]))
        while var.get(u'quasi').get(u'tail').neg():
            var.get(u'expressions').callprop(u'push', var.get(u'parseExpression')())
            PyJs_Object_117_ = Js({u'head':Js(False)})
            var.put(u'quasi', var.get(u'parseTemplateElement')(PyJs_Object_117_))
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
        PyJs_Object_115_ = Js({u'raw':var.get(u'token').get(u'value').get(u'raw'),u'cooked':var.get(u'token').get(u'value').get(u'cooked')})
        return var.get(u'node').callprop(u'finishTemplateElement', PyJs_Object_115_, var.get(u'token').get(u'tail'))
    PyJsHoisted_parseTemplateElement_.func_name = u'parseTemplateElement'
    var.put(u'parseTemplateElement', PyJsHoisted_parseTemplateElement_)
    @Js
    def PyJsHoisted_parseGroupExpression_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'i', u'expr', u'expressions', u'startToken'])
        pass
        var.get(u'expect')(Js(u'('))
        if var.get(u'match')(Js(u')')):
            var.get(u'lex')()
            if var.get(u'match')(Js(u'=>')).neg():
                var.get(u'expect')(Js(u'=>'))
            PyJs_Object_118_ = Js({u'type':var.get(u'PlaceHolders').get(u'ArrowParameterPlaceHolder'),u'params':Js([])})
            return PyJs_Object_118_
        var.put(u'startToken', var.get(u'lookahead'))
        if var.get(u'match')(Js(u'...')):
            var.put(u'expr', var.get(u'parseRestElement')())
            var.get(u'expect')(Js(u')'))
            if var.get(u'match')(Js(u'=>')).neg():
                var.get(u'expect')(Js(u'=>'))
            PyJs_Object_119_ = Js({u'type':var.get(u'PlaceHolders').get(u'ArrowParameterPlaceHolder'),u'params':Js([var.get(u'expr')])})
            return PyJs_Object_119_
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
                    var.get(u'expressions').callprop(u'push', var.get(u'parseRestElement')())
                    var.get(u'expect')(Js(u')'))
                    if var.get(u'match')(Js(u'=>')).neg():
                        var.get(u'expect')(Js(u'=>'))
                    var.put(u'isBindingElement', Js(False))
                    #for JS loop
                    var.put(u'i', Js(0.0))
                    while (var.get(u'i')<var.get(u'expressions').get(u'length')):
                        var.get(u'reinterpretExpressionAsPattern')(var.get(u'expressions').get(var.get(u'i')))
                        (var.put(u'i',var.get(u'i')+Js(1))-Js(1))
                    PyJs_Object_120_ = Js({u'type':var.get(u'PlaceHolders').get(u'ArrowParameterPlaceHolder'),u'params':var.get(u'expressions')})
                    return PyJs_Object_120_
                var.get(u'expressions').callprop(u'push', var.get(u'inheritCoverGrammar')(var.get(u'parseAssignmentExpression')))
            var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishSequenceExpression', var.get(u'expressions')))
        var.get(u'expect')(Js(u')'))
        if var.get(u'match')(Js(u'=>')):
            if var.get(u'isBindingElement').neg():
                var.get(u'throwUnexpectedToken')(var.get(u'lookahead'))
            if PyJsStrictEq(var.get(u'expr').get(u'type'),var.get(u'Syntax').get(u'SequenceExpression')):
                #for JS loop
                var.put(u'i', Js(0.0))
                while (var.get(u'i')<var.get(u'expr').get(u'expressions').get(u'length')):
                    var.get(u'reinterpretExpressionAsPattern')(var.get(u'expr').get(u'expressions').get(var.get(u'i')))
                    (var.put(u'i',var.get(u'i')+Js(1))-Js(1))
            else:
                var.get(u'reinterpretExpressionAsPattern')(var.get(u'expr'))
            PyJs_Object_121_ = Js({u'type':var.get(u'PlaceHolders').get(u'ArrowParameterPlaceHolder'),u'params':(var.get(u'expr').get(u'expressions') if PyJsStrictEq(var.get(u'expr').get(u'type'),var.get(u'Syntax').get(u'SequenceExpression')) else Js([var.get(u'expr')]))})
            var.put(u'expr', PyJs_Object_121_)
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
            var.put(u'number', var.get(u'source').get((var.put(u'index',var.get(u'index')+Js(1))-Js(1))), u'+')
        if PyJsStrictEq(var.get(u'number').get(u'length'),Js(0.0)):
            var.get(u'throwUnexpectedToken')()
        if var.get(u'isIdentifierStart')(var.get(u'source').callprop(u'charCodeAt', var.get(u'index'))):
            var.get(u'throwUnexpectedToken')()
        PyJs_Object_19_ = Js({u'type':var.get(u'Token').get(u'NumericLiteral'),u'value':var.get(u'parseInt')((Js(u'0x')+var.get(u'number')), Js(16.0)),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
        return PyJs_Object_19_
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
            var.put(u'number', var.get(u'source').get((var.put(u'index',var.get(u'index')+Js(1))-Js(1))), u'+')
        if PyJsStrictEq(var.get(u'number').get(u'length'),Js(0.0)):
            var.get(u'throwUnexpectedToken')()
        if (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').callprop(u'charCodeAt', var.get(u'index')))
            if (var.get(u'isIdentifierStart')(var.get(u'ch')) or var.get(u'isDecimalDigit')(var.get(u'ch'))):
                var.get(u'throwUnexpectedToken')()
        PyJs_Object_20_ = Js({u'type':var.get(u'Token').get(u'NumericLiteral'),u'value':var.get(u'parseInt')(var.get(u'number'), Js(2.0)),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
        return PyJs_Object_20_
    PyJsHoisted_scanBinaryLiteral_.func_name = u'scanBinaryLiteral'
    var.put(u'scanBinaryLiteral', PyJsHoisted_scanBinaryLiteral_)
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
        PyJs_Object_128_ = Js({u'params':Js([]),u'defaultCount':Js(0.0),u'defaults':Js([]),u'firstRestricted':var.get(u'firstRestricted')})
        var.put(u'options', PyJs_Object_128_)
        var.get(u'expect')(Js(u'('))
        if var.get(u'match')(Js(u')')).neg():
            PyJs_Object_129_ = Js({})
            var.get(u'options').put(u'paramSet', PyJs_Object_129_)
            while (var.get(u'startIndex')<var.get(u'length')):
                if var.get(u'parseParam')(var.get(u'options')).neg():
                    break
                var.get(u'expect')(Js(u','))
        var.get(u'expect')(Js(u')'))
        if PyJsStrictEq(var.get(u'options').get(u'defaultCount'),Js(0.0)):
            var.get(u'options').put(u'defaults', Js([]))
        PyJs_Object_130_ = Js({u'params':var.get(u'options').get(u'params'),u'defaults':var.get(u'options').get(u'defaults'),u'stricted':var.get(u'options').get(u'stricted'),u'firstRestricted':var.get(u'options').get(u'firstRestricted'),u'message':var.get(u'options').get(u'message')})
        return PyJs_Object_130_
    PyJsHoisted_parseParams_.func_name = u'parseParams'
    var.put(u'parseParams', PyJsHoisted_parseParams_)
    @Js
    def PyJsHoisted_getEscapedIdentifier_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'ch', u'id'])
        pass
        var.put(u'ch', var.get(u'source').callprop(u'charCodeAt', (var.put(u'index',var.get(u'index')+Js(1))-Js(1))))
        var.put(u'id', var.get(u'String').callprop(u'fromCharCode', var.get(u'ch')))
        if PyJsStrictEq(var.get(u'ch'),Js(92)):
            if PyJsStrictNeq(var.get(u'source').callprop(u'charCodeAt', var.get(u'index')),Js(117)):
                var.get(u'throwUnexpectedToken')()
            var.put(u'index',var.get(u'index')+Js(1))
            var.put(u'ch', var.get(u'scanHexEscape')(Js(u'u')))
            if ((var.get(u'ch').neg() or PyJsStrictEq(var.get(u'ch'),Js(u'\\'))) or var.get(u'isIdentifierStart')(var.get(u'ch').callprop(u'charCodeAt', Js(0.0))).neg()):
                var.get(u'throwUnexpectedToken')()
            var.put(u'id', var.get(u'ch'))
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').callprop(u'charCodeAt', var.get(u'index')))
            if var.get(u'isIdentifierPart')(var.get(u'ch')).neg():
                break
            var.put(u'index',var.get(u'index')+Js(1))
            var.put(u'id', var.get(u'String').callprop(u'fromCharCode', var.get(u'ch')), u'+')
            if PyJsStrictEq(var.get(u'ch'),Js(92)):
                var.put(u'id', var.get(u'id').callprop(u'substr', Js(0.0), (var.get(u'id').get(u'length')-Js(1.0))))
                if PyJsStrictNeq(var.get(u'source').callprop(u'charCodeAt', var.get(u'index')),Js(117)):
                    var.get(u'throwUnexpectedToken')()
                var.put(u'index',var.get(u'index')+Js(1))
                var.put(u'ch', var.get(u'scanHexEscape')(Js(u'u')))
                if ((var.get(u'ch').neg() or PyJsStrictEq(var.get(u'ch'),Js(u'\\'))) or var.get(u'isIdentifierPart')(var.get(u'ch').callprop(u'charCodeAt', Js(0.0))).neg()):
                    var.get(u'throwUnexpectedToken')()
                var.put(u'id', var.get(u'ch'), u'+')
        return var.get(u'id')
    PyJsHoisted_getEscapedIdentifier_.func_name = u'getEscapedIdentifier'
    var.put(u'getEscapedIdentifier', PyJsHoisted_getEscapedIdentifier_)
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
            return var.get(u'inheritCoverGrammar')(var.get(u'parseArrayInitialiser'))
        if var.get(u'match')(Js(u'{')):
            return var.get(u'inheritCoverGrammar')(var.get(u'parseObjectInitialiser'))
        var.put(u'type', var.get(u'lookahead').get(u'type'))
        var.put(u'node', var.get(u'Node').create())
        if PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'Identifier')):
            var.put(u'expr', var.get(u'node').callprop(u'finishIdentifier', var.get(u'lex')().get(u'value')))
        else:
            if (PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'StringLiteral')) or PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'NumericLiteral'))):
                var.put(u'isAssignmentTarget', var.put(u'isBindingElement', Js(False)))
                if (var.get(u'strict') and var.get(u'lookahead').get(u'octal')):
                    var.get(u'tolerateUnexpectedToken')(var.get(u'lookahead'), var.get(u'Messages').get(u'StrictOctalLiteral'))
                var.put(u'expr', var.get(u'node').callprop(u'finishLiteral', var.get(u'lex')()))
            else:
                if PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'Keyword')):
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
            var.put(u'index',var.get(u'index')+Js(1))
            if (PyJsStrictEq(var.get(u'ch'),Js(u'\\')) and (var.get(u'index')<var.get(u'length'))):
                var.put(u'ch', var.get(u'source').get(var.get(u'index')))
                if PyJsStrictEq(var.get(u'ch'),Js(u'u')):
                    var.put(u'index',var.get(u'index')+Js(1))
                    var.put(u'restore', var.get(u'index'))
                    var.put(u'ch', var.get(u'scanHexEscape')(Js(u'u')))
                    if var.get(u'ch'):
                        var.put(u'flags', var.get(u'ch'), u'+')
                        #for JS loop
                        var.put(u'str', Js(u'\\u'), u'+')
                        while (var.get(u'restore')<var.get(u'index')):
                            var.put(u'str', var.get(u'source').get(var.get(u'restore')), u'+')
                            var.put(u'restore',var.get(u'restore')+Js(1))
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
        PyJs_Object_28_ = Js({u'value':var.get(u'flags'),u'literal':var.get(u'str')})
        return PyJs_Object_28_
    PyJsHoisted_scanRegExpFlags_.func_name = u'scanRegExpFlags'
    var.put(u'scanRegExpFlags', PyJsHoisted_scanRegExpFlags_)
    @Js
    def PyJsHoisted_parseImportDeclaration_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'specifiers', u'src'])
        var.put(u'node', var.get(u'Node').create())
        if var.get(u'state').get(u'inFunctionBody'):
            var.get(u'throwError')(var.get(u'Messages').get(u'IllegalImportDeclaration'))
        var.get(u'expectKeyword')(Js(u'import'))
        var.put(u'specifiers', Js([]))
        if PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'StringLiteral')):
            var.put(u'src', var.get(u'parseModuleSpecifier')())
            var.get(u'consumeSemicolon')()
            return var.get(u'node').callprop(u'finishImportDeclaration', var.get(u'specifiers'), var.get(u'src'))
        if (var.get(u'matchKeyword')(Js(u'default')).neg() and var.get(u'isIdentifierName')(var.get(u'lookahead'))):
            var.get(u'specifiers').callprop(u'push', var.get(u'parseImportDefaultSpecifier')())
            if var.get(u'match')(Js(u',')):
                var.get(u'lex')()
        if var.get(u'match')(Js(u'*')):
            var.get(u'specifiers').callprop(u'push', var.get(u'parseImportNamespaceSpecifier')())
        else:
            if var.get(u'match')(Js(u'{')):
                var.put(u'specifiers', var.get(u'specifiers').callprop(u'concat', var.get(u'parseNamedImports')()))
        if var.get(u'matchContextualKeyword')(Js(u'from')).neg():
            var.get(u'throwError')((var.get(u'Messages').get(u'UnexpectedToken') if var.get(u'lookahead').get(u'value') else var.get(u'Messages').get(u'MissingFromClause')), var.get(u'lookahead').get(u'value'))
        var.get(u'lex')()
        var.put(u'src', var.get(u'parseModuleSpecifier')())
        var.get(u'consumeSemicolon')()
        return var.get(u'node').callprop(u'finishImportDeclaration', var.get(u'specifiers'), var.get(u'src'))
    PyJsHoisted_parseImportDeclaration_.func_name = u'parseImportDeclaration'
    var.put(u'parseImportDeclaration', PyJsHoisted_parseImportDeclaration_)
    @Js
    def PyJsHoisted_parseVariableDeclarationList_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'list'])
        var.put(u'list', Js([]))
        while 1:
            var.get(u'list').callprop(u'push', var.get(u'parseVariableDeclaration')())
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
        var.registers([u'tmp', u'body', u'previousStrict', u'node', u'stricted', u'id', u'token', u'params', u'defaults', u'firstRestricted', u'message'])
        var.put(u'id', var.get(u"null"))
        var.put(u'params', Js([]))
        var.put(u'defaults', Js([]))
        var.put(u'node', var.get(u'Node').create())
        var.get(u'expectKeyword')(Js(u'function'))
        if var.get(u'match')(Js(u'(')).neg():
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
        return var.get(u'node').callprop(u'finishFunctionExpression', var.get(u'id'), var.get(u'params'), var.get(u'defaults'), var.get(u'body'))
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
            var.put(u'existing', var.get(u'extra').get(u'errors').get(var.get(u'e')))
            if (PyJsStrictEq(var.get(u'existing').get(u'index'),var.get(u'error').get(u'index')) and PyJsStrictEq(var.get(u'existing').get(u'message'),var.get(u'error').get(u'message'))):
                return var.get('undefined')
            (var.put(u'e',var.get(u'e')+Js(1))-Js(1))
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
        PyJs_Object_34_ = Js({u'line':var.get(u'lineNumber'),u'column':(var.get(u'index')-var.get(u'lineStart'))})
        PyJs_Object_33_ = Js({u'start':PyJs_Object_34_})
        var.put(u'loc', PyJs_Object_33_)
        var.put(u'regex', var.get(u'scanRegExp')())
        PyJs_Object_35_ = Js({u'line':var.get(u'lineNumber'),u'column':(var.get(u'index')-var.get(u'lineStart'))})
        var.get(u'loc').put(u'end', PyJs_Object_35_)
        if var.get(u'extra').get(u'tokenize').neg():
            if (var.get(u'extra').get(u'tokens').get(u'length')>Js(0.0)):
                var.put(u'token', var.get(u'extra').get(u'tokens').get((var.get(u'extra').get(u'tokens').get(u'length')-Js(1.0))))
                if (PyJsStrictEq(var.get(u'token').get(u'range').get(u'0'),var.get(u'pos')) and PyJsStrictEq(var.get(u'token').get(u'type'),Js(u'Punctuator'))):
                    if (PyJsStrictEq(var.get(u'token').get(u'value'),Js(u'/')) or PyJsStrictEq(var.get(u'token').get(u'value'),Js(u'/='))):
                        var.get(u'extra').get(u'tokens').callprop(u'pop')
            PyJs_Object_36_ = Js({u'type':Js(u'RegularExpression'),u'value':var.get(u'regex').get(u'literal'),u'regex':var.get(u'regex').get(u'regex'),u'range':Js([var.get(u'pos'), var.get(u'index')]),u'loc':var.get(u'loc')})
            var.get(u'extra').get(u'tokens').callprop(u'push', PyJs_Object_36_)
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
            PyJs_Object_14_ = Js({u'line':var.get(u'lineNumber'),u'column':((var.get(u'index')-var.get(u'lineStart'))-Js(2.0))})
            PyJs_Object_13_ = Js({u'start':PyJs_Object_14_})
            var.put(u'loc', PyJs_Object_13_)
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').callprop(u'charCodeAt', var.get(u'index')))
            if var.get(u'isLineTerminator')(var.get(u'ch')):
                if (PyJsStrictEq(var.get(u'ch'),Js(13)) and PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt', (var.get(u'index')+Js(1.0))),Js(10))):
                    var.put(u'index',var.get(u'index')+Js(1))
                var.put(u'hasLineTerminator', var.get(u'true'))
                var.put(u'lineNumber',var.get(u'lineNumber')+Js(1))
                var.put(u'index',var.get(u'index')+Js(1))
                var.put(u'lineStart', var.get(u'index'))
            else:
                if PyJsStrictEq(var.get(u'ch'),Js(42)):
                    if PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt', (var.get(u'index')+Js(1.0))),Js(47)):
                        var.put(u'index',var.get(u'index')+Js(1))
                        var.put(u'index',var.get(u'index')+Js(1))
                        if var.get(u'extra').get(u'comments'):
                            var.put(u'comment', var.get(u'source').callprop(u'slice', (var.get(u'start')+Js(2.0)), (var.get(u'index')-Js(2.0))))
                            PyJs_Object_15_ = Js({u'line':var.get(u'lineNumber'),u'column':(var.get(u'index')-var.get(u'lineStart'))})
                            var.get(u'loc').put(u'end', PyJs_Object_15_)
                            var.get(u'addComment')(Js(u'Block'), var.get(u'comment'), var.get(u'start'), var.get(u'index'), var.get(u'loc'))
                        return var.get('undefined')
                    var.put(u'index',var.get(u'index')+Js(1))
                else:
                    var.put(u'index',var.get(u'index')+Js(1))
        if var.get(u'extra').get(u'comments'):
            PyJs_Object_16_ = Js({u'line':var.get(u'lineNumber'),u'column':(var.get(u'index')-var.get(u'lineStart'))})
            var.get(u'loc').put(u'end', PyJs_Object_16_)
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
            var.put(u'number', var.get(u'source').get((var.put(u'index',var.get(u'index')+Js(1))-Js(1))))
            var.put(u'ch', var.get(u'source').get(var.get(u'index')))
            if PyJsStrictEq(var.get(u'number'),Js(u'0')):
                if (PyJsStrictEq(var.get(u'ch'),Js(u'x')) or PyJsStrictEq(var.get(u'ch'),Js(u'X'))):
                    var.put(u'index',var.get(u'index')+Js(1))
                    return var.get(u'scanHexLiteral')(var.get(u'start'))
                if (PyJsStrictEq(var.get(u'ch'),Js(u'b')) or PyJsStrictEq(var.get(u'ch'),Js(u'B'))):
                    var.put(u'index',var.get(u'index')+Js(1))
                    return var.get(u'scanBinaryLiteral')(var.get(u'start'))
                if (PyJsStrictEq(var.get(u'ch'),Js(u'o')) or PyJsStrictEq(var.get(u'ch'),Js(u'O'))):
                    return var.get(u'scanOctalLiteral')(var.get(u'ch'), var.get(u'start'))
                if var.get(u'isOctalDigit')(var.get(u'ch')):
                    if var.get(u'isImplicitOctalLiteral')():
                        return var.get(u'scanOctalLiteral')(var.get(u'ch'), var.get(u'start'))
            while var.get(u'isDecimalDigit')(var.get(u'source').callprop(u'charCodeAt', var.get(u'index'))):
                var.put(u'number', var.get(u'source').get((var.put(u'index',var.get(u'index')+Js(1))-Js(1))), u'+')
            var.put(u'ch', var.get(u'source').get(var.get(u'index')))
        if PyJsStrictEq(var.get(u'ch'),Js(u'.')):
            var.put(u'number', var.get(u'source').get((var.put(u'index',var.get(u'index')+Js(1))-Js(1))), u'+')
            while var.get(u'isDecimalDigit')(var.get(u'source').callprop(u'charCodeAt', var.get(u'index'))):
                var.put(u'number', var.get(u'source').get((var.put(u'index',var.get(u'index')+Js(1))-Js(1))), u'+')
            var.put(u'ch', var.get(u'source').get(var.get(u'index')))
        if (PyJsStrictEq(var.get(u'ch'),Js(u'e')) or PyJsStrictEq(var.get(u'ch'),Js(u'E'))):
            var.put(u'number', var.get(u'source').get((var.put(u'index',var.get(u'index')+Js(1))-Js(1))), u'+')
            var.put(u'ch', var.get(u'source').get(var.get(u'index')))
            if (PyJsStrictEq(var.get(u'ch'),Js(u'+')) or PyJsStrictEq(var.get(u'ch'),Js(u'-'))):
                var.put(u'number', var.get(u'source').get((var.put(u'index',var.get(u'index')+Js(1))-Js(1))), u'+')
            if var.get(u'isDecimalDigit')(var.get(u'source').callprop(u'charCodeAt', var.get(u'index'))):
                while var.get(u'isDecimalDigit')(var.get(u'source').callprop(u'charCodeAt', var.get(u'index'))):
                    var.put(u'number', var.get(u'source').get((var.put(u'index',var.get(u'index')+Js(1))-Js(1))), u'+')
            else:
                var.get(u'throwUnexpectedToken')()
        if var.get(u'isIdentifierStart')(var.get(u'source').callprop(u'charCodeAt', var.get(u'index'))):
            var.get(u'throwUnexpectedToken')()
        PyJs_Object_22_ = Js({u'type':var.get(u'Token').get(u'NumericLiteral'),u'value':var.get(u'parseFloat')(var.get(u'number')),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
        return PyJs_Object_22_
    PyJsHoisted_scanNumericLiteral_.func_name = u'scanNumericLiteral'
    var.put(u'scanNumericLiteral', PyJsHoisted_scanNumericLiteral_)
    @Js
    def PyJsHoisted_isIdentifierStart_(ch, this, arguments, var=var):
        var = Scope({u'this':this, u'ch':ch, u'arguments':arguments}, var)
        var.registers([u'ch'])
        return (((((PyJsStrictEq(var.get(u'ch'),Js(36)) or PyJsStrictEq(var.get(u'ch'),Js(95))) or ((var.get(u'ch')>=Js(65)) and (var.get(u'ch')<=Js(90)))) or ((var.get(u'ch')>=Js(97)) and (var.get(u'ch')<=Js(122)))) or PyJsStrictEq(var.get(u'ch'),Js(92))) or ((var.get(u'ch')>=Js(128)) and var.get(u'Regex').get(u'NonAsciiIdentifierStart').callprop(u'test', var.get(u'String').callprop(u'fromCharCode', var.get(u'ch')))))
    PyJsHoisted_isIdentifierStart_.func_name = u'isIdentifierStart'
    var.put(u'isIdentifierStart', PyJsHoisted_isIdentifierStart_)
    @Js
    def PyJsHoisted_parsePropertyMethodFunction_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'params', u'method'])
        var.put(u'node', var.get(u'Node').create())
        var.put(u'params', var.get(u'parseParams')())
        var.put(u'method', var.get(u'parsePropertyFunction')(var.get(u'node'), var.get(u'params')))
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
        return var.get(u'node').callprop(u'finishProgram', var.get(u'body'))
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
            var.put(u'ch', var.get(u'source').get(var.get(u'i')))
            if (PyJsStrictEq(var.get(u'ch'),Js(u'8')) or PyJsStrictEq(var.get(u'ch'),Js(u'9'))):
                return Js(False)
            if var.get(u'isOctalDigit')(var.get(u'ch')).neg():
                return var.get(u'true')
            var.put(u'i',var.get(u'i')+Js(1))
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
        var.registers([u'node', u'hasProto', u'computed', u'value', u'token', u'maybeMethod', u'key'])
        var.put(u'token', var.get(u'lookahead'))
        var.put(u'node', var.get(u'Node').create())
        var.put(u'computed', var.get(u'match')(Js(u'[')))
        var.put(u'key', var.get(u'parseObjectPropertyKey')())
        var.put(u'maybeMethod', var.get(u'tryParseMethodDefinition')(var.get(u'token'), var.get(u'key'), var.get(u'computed'), var.get(u'node')))
        if var.get(u'maybeMethod'):
            var.get(u'checkProto')(var.get(u'maybeMethod').get(u'key'), var.get(u'maybeMethod').get(u'computed'), var.get(u'hasProto'))
            return var.get(u'maybeMethod')
        var.get(u'checkProto')(var.get(u'key'), var.get(u'computed'), var.get(u'hasProto'))
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
        var.registers([u'body', u'node', u'param'])
        var.put(u'node', var.get(u'Node').create())
        var.get(u'expectKeyword')(Js(u'catch'))
        var.get(u'expect')(Js(u'('))
        if var.get(u'match')(Js(u')')):
            var.get(u'throwUnexpectedToken')(var.get(u'lookahead'))
        var.put(u'param', var.get(u'parsePattern')())
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
        var.registers([u'args'])
        var.put(u'args', Js([]))
        var.get(u'expect')(Js(u'('))
        if var.get(u'match')(Js(u')')).neg():
            while (var.get(u'startIndex')<var.get(u'length')):
                var.get(u'args').callprop(u'push', var.get(u'isolateCoverGrammar')(var.get(u'parseAssignmentExpression')))
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
        var.registers([u'tmp', u'pattern', u'flags'])
        var.put(u'tmp', var.get(u'pattern'))
        if (var.get(u'flags').callprop(u'indexOf', Js(u'u'))>=Js(0.0)):
            @Js
            def PyJs_anonymous_26_(PyJsArg_2430_, PyJsArg_2431_, this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments, u'$0':PyJsArg_2430_, u'$1':PyJsArg_2431_}, var)
                var.registers([u'$0', u'$1'])
                if (var.get(u'parseInt')(var.get(u'$1'), Js(16.0))<=Js(1114111)):
                    return Js(u'x')
                var.get(u'throwUnexpectedToken')(var.get(u"null"), var.get(u'Messages').get(u'InvalidRegExp'))
            PyJs_anonymous_26_.func_name = u'anonymous'
            var.put(u'tmp', var.get(u'tmp').callprop(u'replace', JsRegExp(u'/\\\\u\\{([0-9a-fA-F]+)\\}/g'), PyJs_anonymous_26_).callprop(u'replace', JsRegExp(u'/\\\\u([a-fA-F0-9]{4})|[\\uD800-\\uDBFF][\\uDC00-\\uDFFF]/g'), Js(u'x')))
        try:
            var.get(u'RegExp')(var.get(u'tmp'))
        except PyJsException as PyJsTempException:
            PyJsHolder_65_51610080 = var.own.get(u'e')
            var.force_own_put(u'e', PyExceptionToJs(PyJsTempException))
            try:
                var.get(u'throwUnexpectedToken')(var.get(u"null"), var.get(u'Messages').get(u'InvalidRegExp'))
            finally:
                if PyJsHolder_65_51610080 is not None:
                    var.own[u'e'] = PyJsHolder_65_51610080
                else:
                    del var.own[u'e']
                del PyJsHolder_65_51610080
        try:
            return var.get(u'RegExp').create(var.get(u'pattern'), var.get(u'flags'))
        except PyJsException as PyJsTempException:
            PyJsHolder_657863657074696f6e_30067606 = var.own.get(u'exception')
            var.force_own_put(u'exception', PyExceptionToJs(PyJsTempException))
            try:
                return var.get(u"null")
            finally:
                if PyJsHolder_657863657074696f6e_30067606 is not None:
                    var.own[u'exception'] = PyJsHolder_657863657074696f6e_30067606
                else:
                    del var.own[u'exception']
                del PyJsHolder_657863657074696f6e_30067606
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
            var.put(u'code', ((var.get(u'code')*Js(8.0))+Js(u'01234567').callprop(u'indexOf', var.get(u'source').get((var.put(u'index',var.get(u'index')+Js(1))-Js(1))))))
            if (((Js(u'0123').callprop(u'indexOf', var.get(u'ch'))>=Js(0.0)) and (var.get(u'index')<var.get(u'length'))) and var.get(u'isOctalDigit')(var.get(u'source').get(var.get(u'index')))):
                var.put(u'code', ((var.get(u'code')*Js(8.0))+Js(u'01234567').callprop(u'indexOf', var.get(u'source').get((var.put(u'index',var.get(u'index')+Js(1))-Js(1))))))
        PyJs_Object_7_ = Js({u'code':var.get(u'code'),u'octal':var.get(u'octal')})
        return PyJs_Object_7_
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
    def PyJsHoisted_parseObjectInitialiser_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'hasProto', u'properties'])
        var.put(u'properties', Js([]))
        PyJs_Object_114_ = Js({u'value':Js(False)})
        var.put(u'hasProto', PyJs_Object_114_)
        var.put(u'node', var.get(u'Node').create())
        var.get(u'expect')(Js(u'{'))
        while var.get(u'match')(Js(u'}')).neg():
            var.get(u'properties').callprop(u'push', var.get(u'parseObjectProperty')(var.get(u'hasProto')))
            if var.get(u'match')(Js(u'}')).neg():
                var.get(u'expectCommaSeparator')()
        var.get(u'expect')(Js(u'}'))
        return var.get(u'node').callprop(u'finishObjectExpression', var.get(u'properties'))
    PyJsHoisted_parseObjectInitialiser_.func_name = u'parseObjectInitialiser'
    var.put(u'parseObjectInitialiser', PyJsHoisted_parseObjectInitialiser_)
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
        if var.get(u'match')(Js(u'}')).neg():
            while 1:
                var.get(u'specifiers').callprop(u'push', var.get(u'parseImportSpecifier')())
                if not (var.get(u'match')(Js(u',')) and var.get(u'lex')()):
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
        PyJs_Object_127_ = Js({})
        var.get(u'state').put(u'labelSet', PyJs_Object_127_)
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
        var.registers([u'token', u'ch'])
        pass
        if (var.get(u'index')>=var.get(u'length')):
            PyJs_Object_37_ = Js({u'type':var.get(u'Token').get(u'EOF'),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'index'),u'end':var.get(u'index')})
            return PyJs_Object_37_
        var.put(u'ch', var.get(u'source').callprop(u'charCodeAt', var.get(u'index')))
        if var.get(u'isIdentifierStart')(var.get(u'ch')):
            var.put(u'token', var.get(u'scanIdentifier')())
            if (var.get(u'strict') and var.get(u'isStrictModeReservedWord')(var.get(u'token').get(u'value'))):
                var.get(u'token').put(u'type', var.get(u'Token').get(u'Keyword'))
            return var.get(u'token')
        if ((PyJsStrictEq(var.get(u'ch'),Js(40)) or PyJsStrictEq(var.get(u'ch'),Js(41))) or PyJsStrictEq(var.get(u'ch'),Js(59))):
            return var.get(u'scanPunctuator')()
        if (PyJsStrictEq(var.get(u'ch'),Js(39)) or PyJsStrictEq(var.get(u'ch'),Js(34))):
            return var.get(u'scanStringLiteral')()
        if PyJsStrictEq(var.get(u'ch'),Js(46)):
            if var.get(u'isDecimalDigit')(var.get(u'source').callprop(u'charCodeAt', (var.get(u'index')+Js(1.0)))):
                return var.get(u'scanNumericLiteral')()
            return var.get(u'scanPunctuator')()
        if var.get(u'isDecimalDigit')(var.get(u'ch')):
            return var.get(u'scanNumericLiteral')()
        if (var.get(u'extra').get(u'tokenize') and PyJsStrictEq(var.get(u'ch'),Js(47))):
            return var.get(u'advanceSlash')()
        if (PyJsStrictEq(var.get(u'ch'),Js(96)) or (PyJsStrictEq(var.get(u'ch'),Js(125)) and PyJsStrictEq(var.get(u'state').get(u'curlyStack').get((var.get(u'state').get(u'curlyStack').get(u'length')-Js(1.0))),Js(u'${')))):
            return var.get(u'scanTemplate')()
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
    def PyJsHoisted_parseArrayInitialiser_(this, arguments, var=var):
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
    PyJsHoisted_parseArrayInitialiser_.func_name = u'parseArrayInitialiser'
    var.put(u'parseArrayInitialiser', PyJsHoisted_parseArrayInitialiser_)
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
        PyJs_Object_123_ = Js({})
        PyJs_Object_122_ = Js({u'paramSet':PyJs_Object_123_})
        var.put(u'options', PyJs_Object_122_)
        #for JS loop
        PyJsComma(var.put(u'i', Js(0.0)),var.put(u'len', var.get(u'params').get(u'length')))
        while (var.get(u'i')<var.get(u'len')):
            var.put(u'param', var.get(u'params').get(var.get(u'i')))
            while 1:
                SWITCHED = False
                CONDITION = (var.get(u'param').get(u'type'))
                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'Syntax').get(u'AssignmentPattern')):
                    SWITCHED = True
                    var.get(u'params').put(var.get(u'i'), var.get(u'param').get(u'left'))
                    var.get(u'defaults').callprop(u'push', var.get(u'param').get(u'right'))
                    var.put(u'defaultCount',var.get(u'defaultCount')+Js(1))
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
            var.put(u'i', Js(1.0), u'+')
        if PyJsStrictEq(var.get(u'options').get(u'message'),var.get(u'Messages').get(u'StrictParamDupe')):
            var.put(u'token', (var.get(u'options').get(u'stricted') if var.get(u'strict') else var.get(u'options').get(u'firstRestricted')))
            var.get(u'throwUnexpectedToken')(var.get(u'token'), var.get(u'options').get(u'message'))
        if PyJsStrictEq(var.get(u'defaultCount'),Js(0.0)):
            var.put(u'defaults', Js([]))
        PyJs_Object_124_ = Js({u'params':var.get(u'params'),u'defaults':var.get(u'defaults'),u'stricted':var.get(u'options').get(u'stricted'),u'firstRestricted':var.get(u'options').get(u'firstRestricted'),u'message':var.get(u'options').get(u'message')})
        return PyJs_Object_124_
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
            if ((var.get(u'strict') and PyJsStrictEq(var.get(u'expr').get(u'type'),var.get(u'Syntax').get(u'Identifier'))) and var.get(u'isRestrictedWord')(var.get(u'expr').get(u'name'))):
                var.get(u'tolerateUnexpectedToken')(var.get(u'token'), var.get(u'Messages').get(u'StrictLHSAssignment'))
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
        var.registers([u'node', u'init', u'id', u'kind', u'options'])
        var.put(u'init', var.get(u"null"))
        var.put(u'node', var.get(u'Node').create())
        var.put(u'id', var.get(u'parsePattern')())
        if ((var.get(u'strict') and PyJsStrictEq(var.get(u'id').get(u'type'),var.get(u'Syntax').get(u'Identifier'))) and var.get(u'isRestrictedWord')(var.get(u'id').get(u'name'))):
            var.get(u'tolerateError')(var.get(u'Messages').get(u'StrictVarName'))
        if PyJsStrictEq(var.get(u'kind'),Js(u'const')):
            if var.get(u'matchKeyword')(Js(u'in')).neg():
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
        def PyJs_anonymous_110_(whole, idx, this, arguments, var=var):
            var = Scope({u'this':this, u'whole':whole, u'arguments':arguments, u'idx':idx}, var)
            var.registers([u'whole', u'idx'])
            var.get(u'assert')((var.get(u'idx')<var.get(u'args').get(u'length')), Js(u'Message reference must be in range'))
            return var.get(u'args').get(var.get(u'idx'))
        PyJs_anonymous_110_.func_name = u'anonymous'
        var.put(u'msg', var.get(u'messageFormat').callprop(u'replace', JsRegExp(u'/%(\\d)/g'), PyJs_anonymous_110_))
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
        var.put(u'id', (var.get(u'getEscapedIdentifier')() if PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt', var.get(u'index')),Js(92)) else var.get(u'getIdentifier')()))
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
        PyJs_Object_17_ = Js({u'type':var.get(u'type'),u'value':var.get(u'id'),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
        return PyJs_Object_17_
    PyJsHoisted_scanIdentifier_.func_name = u'scanIdentifier'
    var.put(u'scanIdentifier', PyJsHoisted_scanIdentifier_)
    @Js
    def PyJsHoisted_unexpectedTokenError_(token, message, this, arguments, var=var):
        var = Scope({u'this':this, u'token':token, u'message':message, u'arguments':arguments}, var)
        var.registers([u'msg', u'token', u'message', u'value'])
        var.put(u'msg', (var.get(u'message') or var.get(u'Messages').get(u'UnexpectedToken')))
        if var.get(u'token'):
            if var.get(u'message').neg():
                var.put(u'msg', (var.get(u'Messages').get(u'UnexpectedEOS') if PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'EOF')) else (var.get(u'Messages').get(u'UnexpectedIdentifier') if PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Identifier')) else (var.get(u'Messages').get(u'UnexpectedNumber') if PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'NumericLiteral')) else (var.get(u'Messages').get(u'UnexpectedString') if PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'StringLiteral')) else (var.get(u'Messages').get(u'UnexpectedTemplate') if PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Template')) else var.get(u'Messages').get(u'UnexpectedToken')))))))
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
        return (var.get(u'createError')(var.get(u'token').get(u'lineNumber'), var.get(u'token').get(u'start'), var.get(u'msg')) if (var.get(u'token') and PyJsStrictEq(var.get(u'token').get(u'lineNumber').typeof(),Js(u'number'))) else var.get(u'createError')((var.get(u'lineNumber') if var.get(u'scanning') else var.get(u'lastLineNumber')), (var.get(u'index') if var.get(u'scanning') else var.get(u'lastIndex')), var.get(u'msg')))
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
        var.registers([u'token', u'def', u'param', u'options'])
        pass
        var.put(u'token', var.get(u'lookahead'))
        if PyJsStrictEq(var.get(u'token').get(u'value'),Js(u'...')):
            var.put(u'param', var.get(u'parseRestElement')())
            var.get(u'validateParam')(var.get(u'options'), var.get(u'param').get(u'argument'), var.get(u'param').get(u'argument').get(u'name'))
            var.get(u'options').get(u'params').callprop(u'push', var.get(u'param'))
            var.get(u'options').get(u'defaults').callprop(u'push', var.get(u"null"))
            return Js(False)
        var.put(u'param', var.get(u'parsePatternWithDefault')())
        var.get(u'validateParam')(var.get(u'options'), var.get(u'token'), var.get(u'token').get(u'value'))
        if PyJsStrictEq(var.get(u'param').get(u'type'),var.get(u'Syntax').get(u'AssignmentPattern')):
            var.put(u'def', var.get(u'param').get(u'right'))
            var.put(u'param', var.get(u'param').get(u'left'))
            var.get(u'options').put(u'defaultCount',var.get(u'options').get(u'defaultCount')+Js(1))
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
        var.put(u'str', var.get(u'source').get((var.put(u'index',var.get(u'index')+Js(1))-Js(1))))
        var.put(u'classMarker', Js(False))
        var.put(u'terminated', Js(False))
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').get((var.put(u'index',var.get(u'index')+Js(1))-Js(1))))
            var.put(u'str', var.get(u'ch'), u'+')
            if PyJsStrictEq(var.get(u'ch'),Js(u'\\')):
                var.put(u'ch', var.get(u'source').get((var.put(u'index',var.get(u'index')+Js(1))-Js(1))))
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
        PyJs_Object_27_ = Js({u'value':var.get(u'body'),u'literal':var.get(u'str')})
        return PyJs_Object_27_
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
        PyJs_Object_39_ = Js({u'line':var.get(u'lineNumber'),u'column':(var.get(u'index')-var.get(u'lineStart'))})
        PyJs_Object_38_ = Js({u'start':PyJs_Object_39_})
        var.put(u'loc', PyJs_Object_38_)
        var.put(u'token', var.get(u'advance')())
        PyJs_Object_40_ = Js({u'line':var.get(u'lineNumber'),u'column':(var.get(u'index')-var.get(u'lineStart'))})
        var.get(u'loc').put(u'end', PyJs_Object_40_)
        if PyJsStrictNeq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'EOF')):
            var.put(u'value', var.get(u'source').callprop(u'slice', var.get(u'token').get(u'start'), var.get(u'token').get(u'end')))
            PyJs_Object_41_ = Js({u'type':var.get(u'TokenName').get(var.get(u'token').get(u'type')),u'value':var.get(u'value'),u'range':Js([var.get(u'token').get(u'start'), var.get(u'token').get(u'end')]),u'loc':var.get(u'loc')})
            var.put(u'entry', PyJs_Object_41_)
            if var.get(u'token').get(u'regex'):
                PyJs_Object_42_ = Js({u'pattern':var.get(u'token').get(u'regex').get(u'pattern'),u'flags':var.get(u'token').get(u'regex').get(u'flags')})
                var.get(u'entry').put(u'regex', PyJs_Object_42_)
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
    def PyJsHoisted_parseObjectPattern_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'properties'])
        var.put(u'node', var.get(u'Node').create())
        var.put(u'properties', Js([]))
        var.get(u'expect')(Js(u'{'))
        while var.get(u'match')(Js(u'}')).neg():
            var.get(u'properties').callprop(u'push', var.get(u'parsePropertyPattern')())
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
                var.put(u'index',var.get(u'index')+Js(1))
            else:
                if var.get(u'isLineTerminator')(var.get(u'ch')):
                    var.put(u'hasLineTerminator', var.get(u'true'))
                    var.put(u'index',var.get(u'index')+Js(1))
                    if (PyJsStrictEq(var.get(u'ch'),Js(13)) and PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt', var.get(u'index')),Js(10))):
                        var.put(u'index',var.get(u'index')+Js(1))
                    var.put(u'lineNumber',var.get(u'lineNumber')+Js(1))
                    var.put(u'lineStart', var.get(u'index'))
                    var.put(u'start', var.get(u'true'))
                else:
                    if PyJsStrictEq(var.get(u'ch'),Js(47)):
                        var.put(u'ch', var.get(u'source').callprop(u'charCodeAt', (var.get(u'index')+Js(1.0))))
                        if PyJsStrictEq(var.get(u'ch'),Js(47)):
                            var.put(u'index',var.get(u'index')+Js(1))
                            var.put(u'index',var.get(u'index')+Js(1))
                            var.get(u'skipSingleLineComment')(Js(2.0))
                            var.put(u'start', var.get(u'true'))
                        else:
                            if PyJsStrictEq(var.get(u'ch'),Js(42)):
                                var.put(u'index',var.get(u'index')+Js(1))
                                var.put(u'index',var.get(u'index')+Js(1))
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
                                    var.put(u'index',var.get(u'index')+Js(1))
                                    var.put(u'index',var.get(u'index')+Js(1))
                                    var.put(u'index',var.get(u'index')+Js(1))
                                    var.put(u'index',var.get(u'index')+Js(1))
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
        var.put(u'declarations', var.get(u'parseVariableDeclarationList')())
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
        PyJs_Object_134_ = Js({})
        PyJs_Object_133_ = Js({u'allowIn':var.get(u'true'),u'labelSet':PyJs_Object_134_,u'inFunctionBody':Js(False),u'inIteration':Js(False),u'inSwitch':Js(False),u'lastCommentStart':(-Js(1.0)),u'curlyStack':Js([])})
        var.put(u'state', PyJs_Object_133_)
        PyJs_Object_135_ = Js({})
        var.put(u'extra', PyJs_Object_135_)
        PyJs_Object_136_ = Js({})
        var.put(u'options', (var.get(u'options') or PyJs_Object_136_))
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
                    PyJsHolder_6c65784572726f72_11098557 = var.own.get(u'lexError')
                    var.force_own_put(u'lexError', PyExceptionToJs(PyJsTempException))
                    try:
                        if var.get(u'extra').get(u'errors'):
                            var.get(u'recordError')(var.get(u'lexError'))
                            break
                        else:
                            PyJsTempException = JsToPyException(var.get(u'lexError'))
                            raise PyJsTempException
                    finally:
                        if PyJsHolder_6c65784572726f72_11098557 is not None:
                            var.own[u'lexError'] = PyJsHolder_6c65784572726f72_11098557
                        else:
                            del var.own[u'lexError']
                        del PyJsHolder_6c65784572726f72_11098557
            var.get(u'filterTokenLocation')()
            var.put(u'tokens', var.get(u'extra').get(u'tokens'))
            if PyJsStrictNeq(var.get(u'extra').get(u'comments').typeof(),Js(u'undefined')):
                var.get(u'tokens').put(u'comments', var.get(u'extra').get(u'comments'))
            if PyJsStrictNeq(var.get(u'extra').get(u'errors').typeof(),Js(u'undefined')):
                var.get(u'tokens').put(u'errors', var.get(u'extra').get(u'errors'))
        except PyJsException as PyJsTempException:
            PyJsHolder_65_11489438 = var.own.get(u'e')
            var.force_own_put(u'e', PyExceptionToJs(PyJsTempException))
            try:
                PyJsTempException = JsToPyException(var.get(u'e'))
                raise PyJsTempException
            finally:
                if PyJsHolder_65_11489438 is not None:
                    var.own[u'e'] = PyJsHolder_65_11489438
                else:
                    del var.own[u'e']
                del PyJsHolder_65_11489438
        finally:
            PyJs_Object_137_ = Js({})
            var.put(u'extra', PyJs_Object_137_)
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
    def PyJsHoisted_parseArrayPattern_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'elements', u'restNode', u'rest'])
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
                    var.put(u'rest', var.get(u'parseVariableIdentifier')())
                    var.get(u'elements').callprop(u'push', var.get(u'restNode').callprop(u'finishRestElement', var.get(u'rest')))
                    break
                else:
                    var.get(u'elements').callprop(u'push', var.get(u'parsePatternWithDefault')())
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
        var.registers([u'line', u'description', u'pos', u'error'])
        var.put(u'error', var.get(u'Error').create((((Js(u'Line ')+var.get(u'line'))+Js(u': '))+var.get(u'description'))))
        var.get(u'error').put(u'index', var.get(u'pos'))
        var.get(u'error').put(u'lineNumber', var.get(u'line'))
        var.get(u'error').put(u'column', ((var.get(u'pos')-(var.get(u'lineStart') if var.get(u'scanning') else var.get(u'lastLineStart')))+Js(1.0)))
        var.get(u'error').put(u'description', var.get(u'description'))
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
        if var.get(u'match')(Js(u'}')).neg():
            while 1:
                var.put(u'isExportFromIdentifier', (var.get(u'isExportFromIdentifier') or var.get(u'matchKeyword')(Js(u'default'))))
                var.get(u'specifiers').callprop(u'push', var.get(u'parseExportSpecifier')())
                if not (var.get(u'match')(Js(u',')) and var.get(u'lex')()):
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
        PyJs_Object_10_ = Js({u'line':var.get(u'lineNumber'),u'column':((var.get(u'index')-var.get(u'lineStart'))-var.get(u'offset'))})
        PyJs_Object_9_ = Js({u'start':PyJs_Object_10_})
        var.put(u'loc', PyJs_Object_9_)
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').callprop(u'charCodeAt', var.get(u'index')))
            var.put(u'index',var.get(u'index')+Js(1))
            if var.get(u'isLineTerminator')(var.get(u'ch')):
                var.put(u'hasLineTerminator', var.get(u'true'))
                if var.get(u'extra').get(u'comments'):
                    var.put(u'comment', var.get(u'source').callprop(u'slice', (var.get(u'start')+var.get(u'offset')), (var.get(u'index')-Js(1.0))))
                    PyJs_Object_11_ = Js({u'line':var.get(u'lineNumber'),u'column':((var.get(u'index')-var.get(u'lineStart'))-Js(1.0))})
                    var.get(u'loc').put(u'end', PyJs_Object_11_)
                    var.get(u'addComment')(Js(u'Line'), var.get(u'comment'), var.get(u'start'), (var.get(u'index')-Js(1.0)), var.get(u'loc'))
                if (PyJsStrictEq(var.get(u'ch'),Js(13.0)) and PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt', var.get(u'index')),Js(10.0))):
                    var.put(u'index',var.get(u'index')+Js(1))
                var.put(u'lineNumber',var.get(u'lineNumber')+Js(1))
                var.put(u'lineStart', var.get(u'index'))
                return var.get('undefined')
        if var.get(u'extra').get(u'comments'):
            var.put(u'comment', var.get(u'source').callprop(u'slice', (var.get(u'start')+var.get(u'offset')), var.get(u'index')))
            PyJs_Object_12_ = Js({u'line':var.get(u'lineNumber'),u'column':(var.get(u'index')-var.get(u'lineStart'))})
            var.get(u'loc').put(u'end', PyJs_Object_12_)
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
    def PyJsHoisted_scanHexEscape_(prefix, this, arguments, var=var):
        var = Scope({u'this':this, u'prefix':prefix, u'arguments':arguments}, var)
        var.registers([u'i', u'prefix', u'ch', u'len', u'code'])
        var.put(u'code', Js(0.0))
        var.put(u'len', (Js(4.0) if PyJsStrictEq(var.get(u'prefix'),Js(u'u')) else Js(2.0)))
        #for JS loop
        var.put(u'i', Js(0.0))
        while (var.get(u'i')<var.get(u'len')):
            if ((var.get(u'index')<var.get(u'length')) and var.get(u'isHexDigit')(var.get(u'source').get(var.get(u'index')))):
                var.put(u'ch', var.get(u'source').get((var.put(u'index',var.get(u'index')+Js(1))-Js(1))))
                var.put(u'code', ((var.get(u'code')*Js(16.0))+Js(u'0123456789abcdef').callprop(u'indexOf', var.get(u'ch').callprop(u'toLowerCase'))))
            else:
                return Js(u'')
            var.put(u'i',var.get(u'i')+Js(1))
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
        PyJs_Object_139_ = Js({})
        PyJs_Object_138_ = Js({u'allowIn':var.get(u'true'),u'labelSet':PyJs_Object_139_,u'inFunctionBody':Js(False),u'inIteration':Js(False),u'inSwitch':Js(False),u'lastCommentStart':(-Js(1.0)),u'curlyStack':Js([])})
        var.put(u'state', PyJs_Object_138_)
        var.put(u'sourceType', Js(u'script'))
        var.put(u'strict', Js(False))
        PyJs_Object_140_ = Js({})
        var.put(u'extra', PyJs_Object_140_)
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
                var.put(u'sourceType', var.get(u'options').get(u'sourceType'))
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
            PyJsHolder_65_98464870 = var.own.get(u'e')
            var.force_own_put(u'e', PyExceptionToJs(PyJsTempException))
            try:
                PyJsTempException = JsToPyException(var.get(u'e'))
                raise PyJsTempException
            finally:
                if PyJsHolder_65_98464870 is not None:
                    var.own[u'e'] = PyJsHolder_65_98464870
                else:
                    del var.own[u'e']
                del PyJsHolder_65_98464870
        finally:
            PyJs_Object_141_ = Js({})
            var.put(u'extra', PyJs_Object_141_)
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
        return (((((((((((PyJsStrictEq(var.get(u'op'),Js(u'=')) or PyJsStrictEq(var.get(u'op'),Js(u'*='))) or PyJsStrictEq(var.get(u'op'),Js(u'/='))) or PyJsStrictEq(var.get(u'op'),Js(u'%='))) or PyJsStrictEq(var.get(u'op'),Js(u'+='))) or PyJsStrictEq(var.get(u'op'),Js(u'-='))) or PyJsStrictEq(var.get(u'op'),Js(u'<<='))) or PyJsStrictEq(var.get(u'op'),Js(u'>>='))) or PyJsStrictEq(var.get(u'op'),Js(u'>>>='))) or PyJsStrictEq(var.get(u'op'),Js(u'&='))) or PyJsStrictEq(var.get(u'op'),Js(u'^='))) or PyJsStrictEq(var.get(u'op'),Js(u'|=')))
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
    def PyJsHoisted_getIdentifier_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'start', u'ch'])
        pass
        var.put(u'start', (var.put(u'index',var.get(u'index')+Js(1))-Js(1)))
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').callprop(u'charCodeAt', var.get(u'index')))
            if PyJsStrictEq(var.get(u'ch'),Js(92)):
                var.put(u'index', var.get(u'start'))
                return var.get(u'getEscapedIdentifier')()
            if var.get(u'isIdentifierPart')(var.get(u'ch')):
                var.put(u'index',var.get(u'index')+Js(1))
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
    def PyJsHoisted_parsePropertyPattern_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'init', u'computed', u'key'])
        var.put(u'node', var.get(u'Node').create())
        var.put(u'computed', var.get(u'match')(Js(u'[')))
        if PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Identifier')):
            var.put(u'key', var.get(u'parseVariableIdentifier')())
            if var.get(u'match')(Js(u'=')):
                var.get(u'lex')()
                var.put(u'init', var.get(u'parseAssignmentExpression')())
                return var.get(u'node').callprop(u'finishProperty', Js(u'init'), var.get(u'key'), Js(False), var.get(u'WrappingNode').create(var.get(u'key')).callprop(u'finishAssignmentPattern', var.get(u'key'), var.get(u'init')), Js(False), Js(False))
            else:
                if var.get(u'match')(Js(u':')).neg():
                    return var.get(u'node').callprop(u'finishProperty', Js(u'init'), var.get(u'key'), Js(False), var.get(u'key'), Js(False), var.get(u'true'))
        else:
            var.put(u'key', var.get(u'parseObjectPropertyKey')())
        var.get(u'expect')(Js(u':'))
        var.put(u'init', var.get(u'parsePatternWithDefault')())
        return var.get(u'node').callprop(u'finishProperty', Js(u'init'), var.get(u'key'), var.get(u'computed'), var.get(u'init'), Js(False), Js(False))
    PyJsHoisted_parsePropertyPattern_.func_name = u'parsePropertyPattern'
    var.put(u'parsePropertyPattern', PyJsHoisted_parsePropertyPattern_)
    @Js
    def PyJsHoisted_parseFunctionDeclaration_(node, identifierIsOptional, this, arguments, var=var):
        var = Scope({u'node':node, u'identifierIsOptional':identifierIsOptional, u'this':this, u'arguments':arguments}, var)
        var.registers([u'body', u'tmp', u'previousStrict', u'node', u'identifierIsOptional', u'message', u'stricted', u'token', u'params', u'defaults', u'firstRestricted', u'id'])
        var.put(u'id', var.get(u"null"))
        var.put(u'params', Js([]))
        var.put(u'defaults', Js([]))
        var.get(u'expectKeyword')(Js(u'function'))
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
        return var.get(u'node').callprop(u'finishFunctionDeclaration', var.get(u'id'), var.get(u'params'), var.get(u'defaults'), var.get(u'body'))
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
            var.put(u'expression', var.get(u'parseObjectInitialiser')())
        else:
            if var.get(u'match')(Js(u'[')):
                var.put(u'expression', var.get(u'parseArrayInitialiser')())
            else:
                var.put(u'expression', var.get(u'parseAssignmentExpression')())
        var.get(u'consumeSemicolon')()
        return var.get(u'node').callprop(u'finishExportDefaultDeclaration', var.get(u'expression'))
    PyJsHoisted_parseExportDefaultDeclaration_.func_name = u'parseExportDefaultDeclaration'
    var.put(u'parseExportDefaultDeclaration', PyJsHoisted_parseExportDefaultDeclaration_)
    @Js
    def PyJsHoisted_parseRestElement_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'param'])
        var.put(u'node', var.get(u'Node').create())
        var.get(u'lex')()
        if var.get(u'match')(Js(u'{')):
            var.get(u'throwError')(var.get(u'Messages').get(u'ObjectPatternAsRestParameter'))
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
        var.put(u'index',var.get(u'index')+Js(1))
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').get((var.put(u'index',var.get(u'index')+Js(1))-Js(1))))
            if PyJsStrictEq(var.get(u'ch'),Js(u'`')):
                var.put(u'rawOffset', Js(1.0))
                var.put(u'tail', var.get(u'true'))
                var.put(u'terminated', var.get(u'true'))
                break
            else:
                if PyJsStrictEq(var.get(u'ch'),Js(u'$')):
                    if PyJsStrictEq(var.get(u'source').get(var.get(u'index')),Js(u'{')):
                        var.get(u'state').get(u'curlyStack').callprop(u'push', Js(u'${'))
                        var.put(u'index',var.get(u'index')+Js(1))
                        var.put(u'terminated', var.get(u'true'))
                        break
                    var.put(u'cooked', var.get(u'ch'), u'+')
                else:
                    if PyJsStrictEq(var.get(u'ch'),Js(u'\\')):
                        var.put(u'ch', var.get(u'source').get((var.put(u'index',var.get(u'index')+Js(1))-Js(1))))
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
                                        var.put(u'index',var.get(u'index')+Js(1))
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
                            var.put(u'lineNumber',var.get(u'lineNumber')+Js(1))
                            if (PyJsStrictEq(var.get(u'ch'),Js(u'\r')) and PyJsStrictEq(var.get(u'source').get(var.get(u'index')),Js(u'\n'))):
                                var.put(u'index',var.get(u'index')+Js(1))
                            var.put(u'lineStart', var.get(u'index'))
                    else:
                        if var.get(u'isLineTerminator')(var.get(u'ch').callprop(u'charCodeAt', Js(0.0))):
                            var.put(u'lineNumber',var.get(u'lineNumber')+Js(1))
                            if (PyJsStrictEq(var.get(u'ch'),Js(u'\r')) and PyJsStrictEq(var.get(u'source').get(var.get(u'index')),Js(u'\n'))):
                                var.put(u'index',var.get(u'index')+Js(1))
                            var.put(u'lineStart', var.get(u'index'))
                            var.put(u'cooked', Js(u'\n'), u'+')
                        else:
                            var.put(u'cooked', var.get(u'ch'), u'+')
        if var.get(u'terminated').neg():
            var.get(u'throwUnexpectedToken')()
        if var.get(u'head').neg():
            var.get(u'state').get(u'curlyStack').callprop(u'pop')
        PyJs_Object_25_ = Js({u'cooked':var.get(u'cooked'),u'raw':var.get(u'source').callprop(u'slice', (var.get(u'start')+Js(1.0)), (var.get(u'index')-var.get(u'rawOffset')))})
        PyJs_Object_24_ = Js({u'type':var.get(u'Token').get(u'Template'),u'value':PyJs_Object_25_,u'head':var.get(u'head'),u'tail':var.get(u'tail'),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
        return PyJs_Object_24_
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
    def PyJsHoisted_checkProto_(key, computed, hasProto, this, arguments, var=var):
        var = Scope({u'this':this, u'hasProto':hasProto, u'computed':computed, u'key':key, u'arguments':arguments}, var)
        var.registers([u'hasProto', u'computed', u'key'])
        if (PyJsStrictEq(var.get(u'computed'),Js(False)) and ((PyJsStrictEq(var.get(u'key').get(u'type'),var.get(u'Syntax').get(u'Identifier')) and PyJsStrictEq(var.get(u'key').get(u'name'),Js(u'__proto__'))) or (PyJsStrictEq(var.get(u'key').get(u'type'),var.get(u'Syntax').get(u'Literal')) and PyJsStrictEq(var.get(u'key').get(u'value'),Js(u'__proto__'))))):
            if var.get(u'hasProto').get(u'value'):
                var.get(u'tolerateError')(var.get(u'Messages').get(u'DuplicateProtoProperty'))
            else:
                var.get(u'hasProto').put(u'value', var.get(u'true'))
    PyJsHoisted_checkProto_.func_name = u'checkProto'
    var.put(u'checkProto', PyJsHoisted_checkProto_)
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
                    if PyJsStrictNeq(var.get(u'param').get(u'elements').get(var.get(u'i')),var.get(u"null")):
                        var.get(u'checkPatternParam')(var.get(u'options'), var.get(u'param').get(u'elements').get(var.get(u'i')))
                    (var.put(u'i',var.get(u'i')+Js(1))-Js(1))
                break
            if True:
                SWITCHED = True
                var.get(u'assert')(PyJsStrictEq(var.get(u'param').get(u'type'),var.get(u'Syntax').get(u'ObjectPattern')), Js(u'Invalid type'))
                #for JS loop
                var.put(u'i', Js(0.0))
                while (var.get(u'i')<var.get(u'param').get(u'properties').get(u'length')):
                    var.get(u'checkPatternParam')(var.get(u'options'), var.get(u'param').get(u'properties').get(var.get(u'i')).get(u'value'))
                    (var.put(u'i',var.get(u'i')+Js(1))-Js(1))
                break
            SWITCHED = True
            break
    PyJsHoisted_checkPatternParam_.func_name = u'checkPatternParam'
    var.put(u'checkPatternParam', PyJsHoisted_checkPatternParam_)
    @Js
    def PyJsHoisted_parsePropertyFunction_(node, paramInfo, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'paramInfo':paramInfo, u'arguments':arguments}, var)
        var.registers([u'body', u'node', u'previousStrict', u'paramInfo'])
        pass
        var.put(u'isAssignmentTarget', var.put(u'isBindingElement', Js(False)))
        var.put(u'previousStrict', var.get(u'strict'))
        var.put(u'body', var.get(u'isolateCoverGrammar')(var.get(u'parseFunctionSourceElements')))
        if (var.get(u'strict') and var.get(u'paramInfo').get(u'firstRestricted')):
            var.get(u'tolerateUnexpectedToken')(var.get(u'paramInfo').get(u'firstRestricted'), var.get(u'paramInfo').get(u'message'))
        if (var.get(u'strict') and var.get(u'paramInfo').get(u'stricted')):
            var.get(u'tolerateUnexpectedToken')(var.get(u'paramInfo').get(u'stricted'), var.get(u'paramInfo').get(u'message'))
        var.put(u'strict', var.get(u'previousStrict'))
        return var.get(u'node').callprop(u'finishFunctionExpression', var.get(u"null"), var.get(u'paramInfo').get(u'params'), var.get(u'paramInfo').get(u'defaults'), var.get(u'body'))
    PyJsHoisted_parsePropertyFunction_.func_name = u'parsePropertyFunction'
    var.put(u'parsePropertyFunction', PyJsHoisted_parsePropertyFunction_)
    @Js
    def PyJsHoisted_scanPunctuator_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'token', u'str'])
        pass
        PyJs_Object_18_ = Js({u'type':var.get(u'Token').get(u'Punctuator'),u'value':Js(u''),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'index'),u'end':var.get(u'index')})
        var.put(u'token', PyJs_Object_18_)
        var.put(u'str', var.get(u'source').get(var.get(u'index')))
        while 1:
            SWITCHED = False
            CONDITION = (var.get(u'str'))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'(')):
                SWITCHED = True
                if var.get(u'extra').get(u'tokenize'):
                    var.get(u'extra').put(u'openParenToken', var.get(u'extra').get(u'tokens').get(u'length'))
                var.put(u'index',var.get(u'index')+Js(1))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'{')):
                SWITCHED = True
                if var.get(u'extra').get(u'tokenize'):
                    var.get(u'extra').put(u'openCurlyToken', var.get(u'extra').get(u'tokens').get(u'length'))
                var.get(u'state').get(u'curlyStack').callprop(u'push', Js(u'{'))
                var.put(u'index',var.get(u'index')+Js(1))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'.')):
                SWITCHED = True
                var.put(u'index',var.get(u'index')+Js(1))
                if (PyJsStrictEq(var.get(u'source').get(var.get(u'index')),Js(u'.')) and PyJsStrictEq(var.get(u'source').get((var.get(u'index')+Js(1.0))),Js(u'.'))):
                    var.put(u'index', Js(2.0), u'+')
                    var.put(u'str', Js(u'...'))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'}')):
                SWITCHED = True
                var.put(u'index',var.get(u'index')+Js(1))
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
                var.put(u'index',var.get(u'index')+Js(1))
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
                        if ((((((((((((((((((PyJsStrictEq(var.get(u'str'),Js(u'&&')) or PyJsStrictEq(var.get(u'str'),Js(u'||'))) or PyJsStrictEq(var.get(u'str'),Js(u'=='))) or PyJsStrictEq(var.get(u'str'),Js(u'!='))) or PyJsStrictEq(var.get(u'str'),Js(u'+='))) or PyJsStrictEq(var.get(u'str'),Js(u'-='))) or PyJsStrictEq(var.get(u'str'),Js(u'*='))) or PyJsStrictEq(var.get(u'str'),Js(u'/='))) or PyJsStrictEq(var.get(u'str'),Js(u'++'))) or PyJsStrictEq(var.get(u'str'),Js(u'--'))) or PyJsStrictEq(var.get(u'str'),Js(u'<<'))) or PyJsStrictEq(var.get(u'str'),Js(u'>>'))) or PyJsStrictEq(var.get(u'str'),Js(u'&='))) or PyJsStrictEq(var.get(u'str'),Js(u'|='))) or PyJsStrictEq(var.get(u'str'),Js(u'^='))) or PyJsStrictEq(var.get(u'str'),Js(u'%='))) or PyJsStrictEq(var.get(u'str'),Js(u'<='))) or PyJsStrictEq(var.get(u'str'),Js(u'>='))) or PyJsStrictEq(var.get(u'str'),Js(u'=>'))):
                            var.put(u'index', Js(2.0), u'+')
                        else:
                            var.put(u'str', var.get(u'source').get(var.get(u'index')))
                            if (Js(u'<>=!+-*%&|^/').callprop(u'indexOf', var.get(u'str'))>=Js(0.0)):
                                var.put(u'index',var.get(u'index')+Js(1))
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
        var.registers([u'body', u'node', u'previousStrict', u'options'])
        pass
        if var.get(u'hasLineTerminator'):
            var.get(u'tolerateUnexpectedToken')(var.get(u'lookahead'))
        var.get(u'expect')(Js(u'=>'))
        var.put(u'previousStrict', var.get(u'strict'))
        var.put(u'body', var.get(u'parseConciseBody')())
        if (var.get(u'strict') and var.get(u'options').get(u'firstRestricted')):
            var.get(u'throwUnexpectedToken')(var.get(u'options').get(u'firstRestricted'), var.get(u'options').get(u'message'))
        if (var.get(u'strict') and var.get(u'options').get(u'stricted')):
            var.get(u'tolerateUnexpectedToken')(var.get(u'options').get(u'stricted'), var.get(u'options').get(u'message'))
        var.put(u'strict', var.get(u'previousStrict'))
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
        def PyJs_anonymous_109_(whole, idx, this, arguments, var=var):
            var = Scope({u'this':this, u'whole':whole, u'arguments':arguments, u'idx':idx}, var)
            var.registers([u'whole', u'idx'])
            var.get(u'assert')((var.get(u'idx')<var.get(u'args').get(u'length')), Js(u'Message reference must be in range'))
            return var.get(u'args').get(var.get(u'idx'))
        PyJs_anonymous_109_.func_name = u'anonymous'
        var.put(u'msg', var.get(u'messageFormat').callprop(u'replace', JsRegExp(u'/%(\\d)/g'), PyJs_anonymous_109_))
        PyJsTempException = JsToPyException(var.get(u'createError')(var.get(u'lastLineNumber'), var.get(u'lastIndex'), var.get(u'msg')))
        raise PyJsTempException
    PyJsHoisted_throwError_.func_name = u'throwError'
    var.put(u'throwError', PyJsHoisted_throwError_)
    @Js
    def PyJsHoisted_scanUnicodeCodePointEscape_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'code', u'ch', u'cu2', u'cu1'])
        pass
        var.put(u'ch', var.get(u'source').get(var.get(u'index')))
        var.put(u'code', Js(0.0))
        if PyJsStrictEq(var.get(u'ch'),Js(u'}')):
            var.get(u'throwUnexpectedToken')()
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').get((var.put(u'index',var.get(u'index')+Js(1))-Js(1))))
            if var.get(u'isHexDigit')(var.get(u'ch')).neg():
                break
            var.put(u'code', ((var.get(u'code')*Js(16.0))+Js(u'0123456789abcdef').callprop(u'indexOf', var.get(u'ch').callprop(u'toLowerCase'))))
        if ((var.get(u'code')>Js(1114111)) or PyJsStrictNeq(var.get(u'ch'),Js(u'}'))):
            var.get(u'throwUnexpectedToken')()
        if (var.get(u'code')<=Js(65535)):
            return var.get(u'String').callprop(u'fromCharCode', var.get(u'code'))
        var.put(u'cu1', (((var.get(u'code')-Js(65536))>>Js(10.0))+Js(55296)))
        var.put(u'cu2', (((var.get(u'code')-Js(65536))&Js(1023.0))+Js(56320)))
        return var.get(u'String').callprop(u'fromCharCode', var.get(u'cu1'), var.get(u'cu2'))
    PyJsHoisted_scanUnicodeCodePointEscape_.func_name = u'scanUnicodeCodePointEscape'
    var.put(u'scanUnicodeCodePointEscape', PyJsHoisted_scanUnicodeCodePointEscape_)
    @Js
    def PyJsHoisted_scanOctalLiteral_(prefix, start, this, arguments, var=var):
        var = Scope({u'this':this, u'start':start, u'prefix':prefix, u'arguments':arguments}, var)
        var.registers([u'octal', u'start', u'prefix', u'number'])
        pass
        if var.get(u'isOctalDigit')(var.get(u'prefix')):
            var.put(u'octal', var.get(u'true'))
            var.put(u'number', (Js(u'0')+var.get(u'source').get((var.put(u'index',var.get(u'index')+Js(1))-Js(1)))))
        else:
            var.put(u'octal', Js(False))
            var.put(u'index',var.get(u'index')+Js(1))
            var.put(u'number', Js(u''))
        while (var.get(u'index')<var.get(u'length')):
            if var.get(u'isOctalDigit')(var.get(u'source').get(var.get(u'index'))).neg():
                break
            var.put(u'number', var.get(u'source').get((var.put(u'index',var.get(u'index')+Js(1))-Js(1))), u'+')
        if (var.get(u'octal').neg() and PyJsStrictEq(var.get(u'number').get(u'length'),Js(0.0))):
            var.get(u'throwUnexpectedToken')()
        if (var.get(u'isIdentifierStart')(var.get(u'source').callprop(u'charCodeAt', var.get(u'index'))) or var.get(u'isDecimalDigit')(var.get(u'source').callprop(u'charCodeAt', var.get(u'index')))):
            var.get(u'throwUnexpectedToken')()
        PyJs_Object_21_ = Js({u'type':var.get(u'Token').get(u'NumericLiteral'),u'value':var.get(u'parseInt')(var.get(u'number'), Js(8.0)),u'octal':var.get(u'octal'),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
        return PyJs_Object_21_
    PyJsHoisted_scanOctalLiteral_.func_name = u'scanOctalLiteral'
    var.put(u'scanOctalLiteral', PyJsHoisted_scanOctalLiteral_)
    @Js
    def PyJsHoisted_scanRegExp_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'body', u'start', u'flags', u'value'])
        var.put(u'scanning', var.get(u'true'))
        pass
        var.put(u'lookahead', var.get(u"null"))
        var.get(u'skipComment')()
        var.put(u'start', var.get(u'index'))
        var.put(u'body', var.get(u'scanRegExpBody')())
        var.put(u'flags', var.get(u'scanRegExpFlags')())
        var.put(u'value', var.get(u'testRegExp')(var.get(u'body').get(u'value'), var.get(u'flags').get(u'value')))
        var.put(u'scanning', Js(False))
        if var.get(u'extra').get(u'tokenize'):
            PyJs_Object_30_ = Js({u'pattern':var.get(u'body').get(u'value'),u'flags':var.get(u'flags').get(u'value')})
            PyJs_Object_29_ = Js({u'type':var.get(u'Token').get(u'RegularExpression'),u'value':var.get(u'value'),u'regex':PyJs_Object_30_,u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
            return PyJs_Object_29_
        PyJs_Object_32_ = Js({u'pattern':var.get(u'body').get(u'value'),u'flags':var.get(u'flags').get(u'value')})
        PyJs_Object_31_ = Js({u'literal':(var.get(u'body').get(u'literal')+var.get(u'flags').get(u'literal')),u'value':var.get(u'value'),u'regex':PyJs_Object_32_,u'start':var.get(u'start'),u'end':var.get(u'index')})
        return PyJs_Object_31_
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
    def PyJsHoisted_parsePattern_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        if PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Identifier')):
            return var.get(u'parseVariableIdentifier')()
        else:
            if var.get(u'match')(Js(u'[')):
                return var.get(u'parseArrayPattern')()
            else:
                if var.get(u'match')(Js(u'{')):
                    return var.get(u'parseObjectPattern')()
        var.get(u'throwUnexpectedToken')(var.get(u'lookahead'))
    PyJsHoisted_parsePattern_.func_name = u'parsePattern'
    var.put(u'parsePattern', PyJsHoisted_parsePattern_)
    @Js
    def PyJsHoisted_parseVariableIdentifier_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'token'])
        var.put(u'node', var.get(u'Node').create())
        var.put(u'token', var.get(u'lex')())
        if PyJsStrictNeq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Identifier')):
            if ((var.get(u'strict') and PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Keyword'))) and var.get(u'isStrictModeReservedWord')(var.get(u'token').get(u'value'))):
                var.get(u'tolerateUnexpectedToken')(var.get(u'token'), var.get(u'Messages').get(u'StrictReservedWord'))
            else:
                var.get(u'throwUnexpectedToken')(var.get(u'token'))
        return var.get(u'node').callprop(u'finishIdentifier', var.get(u'token').get(u'value'))
    PyJsHoisted_parseVariableIdentifier_.func_name = u'parseVariableIdentifier'
    var.put(u'parseVariableIdentifier', PyJsHoisted_parseVariableIdentifier_)
    @Js
    def PyJsHoisted_parseForStatement_(node, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'arguments':arguments}, var)
        var.registers([u'body', u'oldInIteration', u'kind', u'right', u'node', u'previousAllowIn', u'declarations', u'update', u'init', u'initSeq', u'test', u'initStartToken', u'left'])
        var.put(u'previousAllowIn', var.get(u'state').get(u'allowIn'))
        var.put(u'init', var.put(u'test', var.put(u'update', var.get(u"null"))))
        var.get(u'expectKeyword')(Js(u'for'))
        var.get(u'expect')(Js(u'('))
        if var.get(u'match')(Js(u';')):
            var.get(u'lex')()
        else:
            if var.get(u'matchKeyword')(Js(u'var')):
                var.put(u'init', var.get(u'Node').create())
                var.get(u'lex')()
                var.get(u'state').put(u'allowIn', Js(False))
                var.put(u'init', var.get(u'init').callprop(u'finishVariableDeclaration', var.get(u'parseVariableDeclarationList')()))
                var.get(u'state').put(u'allowIn', var.get(u'previousAllowIn'))
                if (PyJsStrictEq(var.get(u'init').get(u'declarations').get(u'length'),Js(1.0)) and var.get(u'matchKeyword')(Js(u'in'))):
                    var.get(u'lex')()
                    var.put(u'left', var.get(u'init'))
                    var.put(u'right', var.get(u'parseExpression')())
                    var.put(u'init', var.get(u"null"))
                else:
                    var.get(u'expect')(Js(u';'))
            else:
                if (var.get(u'matchKeyword')(Js(u'const')) or var.get(u'matchKeyword')(Js(u'let'))):
                    var.put(u'init', var.get(u'Node').create())
                    var.put(u'kind', var.get(u'lex')().get(u'value'))
                    var.get(u'state').put(u'allowIn', Js(False))
                    PyJs_Object_126_ = Js({u'inFor':var.get(u'true')})
                    var.put(u'declarations', var.get(u'parseBindingList')(var.get(u'kind'), PyJs_Object_126_))
                    var.get(u'state').put(u'allowIn', var.get(u'previousAllowIn'))
                    if ((PyJsStrictEq(var.get(u'declarations').get(u'length'),Js(1.0)) and PyJsStrictEq(var.get(u'declarations').get(u'0').get(u'init'),var.get(u"null"))) and var.get(u'matchKeyword')(Js(u'in'))):
                        var.put(u'init', var.get(u'init').callprop(u'finishLexicalDeclaration', var.get(u'declarations'), var.get(u'kind')))
                        var.get(u'lex')()
                        var.put(u'left', var.get(u'init'))
                        var.put(u'right', var.get(u'parseExpression')())
                        var.put(u'init', var.get(u"null"))
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
        return (var.get(u'node').callprop(u'finishForStatement', var.get(u'init'), var.get(u'test'), var.get(u'update'), var.get(u'body')) if PyJsStrictEq(var.get(u'left',throw=False).typeof(),Js(u'undefined')) else var.get(u'node').callprop(u'finishForInStatement', var.get(u'left'), var.get(u'right'), var.get(u'body')))
    PyJsHoisted_parseForStatement_.func_name = u'parseForStatement'
    var.put(u'parseForStatement', PyJsHoisted_parseForStatement_)
    @Js
    def PyJsHoisted_isIdentifierPart_(ch, this, arguments, var=var):
        var = Scope({u'this':this, u'ch':ch, u'arguments':arguments}, var)
        var.registers([u'ch'])
        return ((((((PyJsStrictEq(var.get(u'ch'),Js(36)) or PyJsStrictEq(var.get(u'ch'),Js(95))) or ((var.get(u'ch')>=Js(65)) and (var.get(u'ch')<=Js(90)))) or ((var.get(u'ch')>=Js(97)) and (var.get(u'ch')<=Js(122)))) or ((var.get(u'ch')>=Js(48)) and (var.get(u'ch')<=Js(57)))) or PyJsStrictEq(var.get(u'ch'),Js(92))) or ((var.get(u'ch')>=Js(128)) and var.get(u'Regex').get(u'NonAsciiIdentifierPart').callprop(u'test', var.get(u'String').callprop(u'fromCharCode', var.get(u'ch')))))
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
        var.registers([u'node', u'computed', u'value', u'token', u'key', u'methodNode', u'options'])
        pass
        if PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Identifier')):
            if (PyJsStrictEq(var.get(u'token').get(u'value'),Js(u'get')) and var.get(u'lookaheadPropertyName')()):
                var.put(u'computed', var.get(u'match')(Js(u'[')))
                var.put(u'key', var.get(u'parseObjectPropertyKey')())
                var.put(u'methodNode', var.get(u'Node').create())
                var.get(u'expect')(Js(u'('))
                var.get(u'expect')(Js(u')'))
                PyJs_Object_111_ = Js({u'params':Js([]),u'defaults':Js([]),u'stricted':var.get(u"null"),u'firstRestricted':var.get(u"null"),u'message':var.get(u"null")})
                var.put(u'value', var.get(u'parsePropertyFunction')(var.get(u'methodNode'), PyJs_Object_111_))
                return var.get(u'node').callprop(u'finishProperty', Js(u'get'), var.get(u'key'), var.get(u'computed'), var.get(u'value'), Js(False), Js(False))
            else:
                if (PyJsStrictEq(var.get(u'token').get(u'value'),Js(u'set')) and var.get(u'lookaheadPropertyName')()):
                    var.put(u'computed', var.get(u'match')(Js(u'[')))
                    var.put(u'key', var.get(u'parseObjectPropertyKey')())
                    var.put(u'methodNode', var.get(u'Node').create())
                    var.get(u'expect')(Js(u'('))
                    PyJs_Object_113_ = Js({})
                    PyJs_Object_112_ = Js({u'params':Js([]),u'defaultCount':Js(0.0),u'defaults':Js([]),u'firstRestricted':var.get(u"null"),u'paramSet':PyJs_Object_113_})
                    var.put(u'options', PyJs_Object_112_)
                    if var.get(u'match')(Js(u')')):
                        var.get(u'tolerateUnexpectedToken')(var.get(u'lookahead'))
                    else:
                        var.get(u'parseParam')(var.get(u'options'))
                        if PyJsStrictEq(var.get(u'options').get(u'defaultCount'),Js(0.0)):
                            var.get(u'options').put(u'defaults', Js([]))
                    var.get(u'expect')(Js(u')'))
                    var.put(u'value', var.get(u'parsePropertyFunction')(var.get(u'methodNode'), var.get(u'options')))
                    return var.get(u'node').callprop(u'finishProperty', Js(u'set'), var.get(u'key'), var.get(u'computed'), var.get(u'value'), Js(False), Js(False))
        if var.get(u'match')(Js(u'(')):
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
                var.put(u'key', var.get(u'parseObjectPropertyKey')())
                if (PyJsStrictEq(var.get(u'key').get(u'name'),Js(u'static')) and var.get(u'lookaheadPropertyName')()):
                    var.put(u'token', var.get(u'lookahead'))
                    var.put(u'isStatic', var.get(u'true'))
                    var.put(u'computed', var.get(u'match')(Js(u'[')))
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
            var.put(u'entry', var.get(u'extra').get(u'tokens').get(var.get(u'i')))
            PyJs_Object_131_ = Js({u'type':var.get(u'entry').get(u'type'),u'value':var.get(u'entry').get(u'value')})
            var.put(u'token', PyJs_Object_131_)
            if var.get(u'entry').get(u'regex'):
                PyJs_Object_132_ = Js({u'pattern':var.get(u'entry').get(u'regex').get(u'pattern'),u'flags':var.get(u'entry').get(u'regex').get(u'flags')})
                var.get(u'token').put(u'regex', PyJs_Object_132_)
            if var.get(u'extra').get(u'range'):
                var.get(u'token').put(u'range', var.get(u'entry').get(u'range'))
            if var.get(u'extra').get(u'loc'):
                var.get(u'token').put(u'loc', var.get(u'entry').get(u'loc'))
            var.get(u'tokens').callprop(u'push', var.get(u'token'))
            var.put(u'i',var.get(u'i')+Js(1))
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
    var.put(u'FnExprTokens', Js([Js(u'('), Js(u'{'), Js(u'['), Js(u'in'), Js(u'typeof'), Js(u'instanceof'), Js(u'new'), Js(u'return'), Js(u'case'), Js(u'delete'), Js(u'throw'), Js(u'void'), Js(u'='), Js(u'+='), Js(u'-='), Js(u'*='), Js(u'/='), Js(u'%='), Js(u'<<='), Js(u'>>='), Js(u'>>>='), Js(u'&='), Js(u'|='), Js(u'^='), Js(u','), Js(u'+'), Js(u'-'), Js(u'*'), Js(u'/'), Js(u'%'), Js(u'++'), Js(u'--'), Js(u'<<'), Js(u'>>'), Js(u'>>>'), Js(u'&'), Js(u'|'), Js(u'^'), Js(u'!'), Js(u'~'), Js(u'&&'), Js(u'||'), Js(u'?'), Js(u':'), Js(u'==='), Js(u'=='), Js(u'>='), Js(u'<='), Js(u'<'), Js(u'>'), Js(u'!='), Js(u'!==')]))
    PyJs_Object_3_ = Js({u'AssignmentExpression':Js(u'AssignmentExpression'),u'AssignmentPattern':Js(u'AssignmentPattern'),u'ArrayExpression':Js(u'ArrayExpression'),u'ArrayPattern':Js(u'ArrayPattern'),u'ArrowFunctionExpression':Js(u'ArrowFunctionExpression'),u'BlockStatement':Js(u'BlockStatement'),u'BinaryExpression':Js(u'BinaryExpression'),u'BreakStatement':Js(u'BreakStatement'),u'CallExpression':Js(u'CallExpression'),u'CatchClause':Js(u'CatchClause'),u'ClassBody':Js(u'ClassBody'),u'ClassDeclaration':Js(u'ClassDeclaration'),u'ClassExpression':Js(u'ClassExpression'),u'ConditionalExpression':Js(u'ConditionalExpression'),u'ContinueStatement':Js(u'ContinueStatement'),u'DoWhileStatement':Js(u'DoWhileStatement'),u'DebuggerStatement':Js(u'DebuggerStatement'),u'EmptyStatement':Js(u'EmptyStatement'),u'ExportAllDeclaration':Js(u'ExportAllDeclaration'),u'ExportDefaultDeclaration':Js(u'ExportDefaultDeclaration'),u'ExportNamedDeclaration':Js(u'ExportNamedDeclaration'),u'ExportSpecifier':Js(u'ExportSpecifier'),u'ExpressionStatement':Js(u'ExpressionStatement'),u'ForStatement':Js(u'ForStatement'),u'ForInStatement':Js(u'ForInStatement'),u'FunctionDeclaration':Js(u'FunctionDeclaration'),u'FunctionExpression':Js(u'FunctionExpression'),u'Identifier':Js(u'Identifier'),u'IfStatement':Js(u'IfStatement'),u'ImportDeclaration':Js(u'ImportDeclaration'),u'ImportDefaultSpecifier':Js(u'ImportDefaultSpecifier'),u'ImportNamespaceSpecifier':Js(u'ImportNamespaceSpecifier'),u'ImportSpecifier':Js(u'ImportSpecifier'),u'Literal':Js(u'Literal'),u'LabeledStatement':Js(u'LabeledStatement'),u'LogicalExpression':Js(u'LogicalExpression'),u'MemberExpression':Js(u'MemberExpression'),u'MethodDefinition':Js(u'MethodDefinition'),u'NewExpression':Js(u'NewExpression'),u'ObjectExpression':Js(u'ObjectExpression'),u'ObjectPattern':Js(u'ObjectPattern'),u'Program':Js(u'Program'),u'Property':Js(u'Property'),u'RestElement':Js(u'RestElement'),u'ReturnStatement':Js(u'ReturnStatement'),u'SequenceExpression':Js(u'SequenceExpression'),u'SpreadElement':Js(u'SpreadElement'),u'Super':Js(u'Super'),u'SwitchCase':Js(u'SwitchCase'),u'SwitchStatement':Js(u'SwitchStatement'),u'TaggedTemplateExpression':Js(u'TaggedTemplateExpression'),u'TemplateElement':Js(u'TemplateElement'),u'TemplateLiteral':Js(u'TemplateLiteral'),u'ThisExpression':Js(u'ThisExpression'),u'ThrowStatement':Js(u'ThrowStatement'),u'TryStatement':Js(u'TryStatement'),u'UnaryExpression':Js(u'UnaryExpression'),u'UpdateExpression':Js(u'UpdateExpression'),u'VariableDeclaration':Js(u'VariableDeclaration'),u'VariableDeclarator':Js(u'VariableDeclarator'),u'WhileStatement':Js(u'WhileStatement'),u'WithStatement':Js(u'WithStatement')})
    var.put(u'Syntax', PyJs_Object_3_)
    PyJs_Object_4_ = Js({u'ArrowParameterPlaceHolder':Js(u'ArrowParameterPlaceHolder')})
    var.put(u'PlaceHolders', PyJs_Object_4_)
    PyJs_Object_5_ = Js({u'UnexpectedToken':Js(u'Unexpected token %0'),u'UnexpectedNumber':Js(u'Unexpected number'),u'UnexpectedString':Js(u'Unexpected string'),u'UnexpectedIdentifier':Js(u'Unexpected identifier'),u'UnexpectedReserved':Js(u'Unexpected reserved word'),u'UnexpectedTemplate':Js(u'Unexpected quasi %0'),u'UnexpectedEOS':Js(u'Unexpected end of input'),u'NewlineAfterThrow':Js(u'Illegal newline after throw'),u'InvalidRegExp':Js(u'Invalid regular expression'),u'UnterminatedRegExp':Js(u'Invalid regular expression: missing /'),u'InvalidLHSInAssignment':Js(u'Invalid left-hand side in assignment'),u'InvalidLHSInForIn':Js(u'Invalid left-hand side in for-in'),u'MultipleDefaultsInSwitch':Js(u'More than one default clause in switch statement'),u'NoCatchOrFinally':Js(u'Missing catch or finally after try'),u'UnknownLabel':Js(u"Undefined label '%0'"),u'Redeclaration':Js(u"%0 '%1' has already been declared"),u'IllegalContinue':Js(u'Illegal continue statement'),u'IllegalBreak':Js(u'Illegal break statement'),u'IllegalReturn':Js(u'Illegal return statement'),u'StrictModeWith':Js(u'Strict mode code may not include a with statement'),u'StrictCatchVariable':Js(u'Catch variable may not be eval or arguments in strict mode'),u'StrictVarName':Js(u'Variable name may not be eval or arguments in strict mode'),u'StrictParamName':Js(u'Parameter name eval or arguments is not allowed in strict mode'),u'StrictParamDupe':Js(u'Strict mode function may not have duplicate parameter names'),u'StrictFunctionName':Js(u'Function name may not be eval or arguments in strict mode'),u'StrictOctalLiteral':Js(u'Octal literals are not allowed in strict mode.'),u'StrictDelete':Js(u'Delete of an unqualified identifier in strict mode.'),u'StrictLHSAssignment':Js(u'Assignment to eval or arguments is not allowed in strict mode'),u'StrictLHSPostfix':Js(u'Postfix increment/decrement may not have eval or arguments operand in strict mode'),u'StrictLHSPrefix':Js(u'Prefix increment/decrement may not have eval or arguments operand in strict mode'),u'StrictReservedWord':Js(u'Use of future reserved word in strict mode'),u'TemplateOctalLiteral':Js(u'Octal literals are not allowed in template strings.'),u'ParameterAfterRestParameter':Js(u'Rest parameter must be last formal parameter'),u'DefaultRestParameter':Js(u'Unexpected token ='),u'ObjectPatternAsRestParameter':Js(u'Unexpected token {'),u'DuplicateProtoProperty':Js(u'Duplicate __proto__ fields are not allowed in object literals'),u'ConstructorSpecialMethod':Js(u'Class constructor may not be an accessor'),u'DuplicateConstructor':Js(u'A class may only have one constructor'),u'StaticPrototype':Js(u'Classes may not have static property named prototype'),u'MissingFromClause':Js(u'Unexpected token'),u'NoAsAfterImportNamespace':Js(u'Unexpected token'),u'InvalidModuleSpecifier':Js(u'Unexpected token'),u'IllegalImportDeclaration':Js(u'Unexpected token'),u'IllegalExportDeclaration':Js(u'Unexpected token')})
    var.put(u'Messages', PyJs_Object_5_)
    PyJs_Object_6_ = Js({u'NonAsciiIdentifierStart':var.get(u'RegExp').create(Js(u'[\xaa\xb5\xba\xc0-\xd6\xd8-\xf6\xf8-\u02c1\u02c6-\u02d1\u02e0-\u02e4\u02ec\u02ee\u0370-\u0374\u0376\u0377\u037a-\u037d\u037f\u0386\u0388-\u038a\u038c\u038e-\u03a1\u03a3-\u03f5\u03f7-\u0481\u048a-\u052f\u0531-\u0556\u0559\u0561-\u0587\u05d0-\u05ea\u05f0-\u05f2\u0620-\u064a\u066e\u066f\u0671-\u06d3\u06d5\u06e5\u06e6\u06ee\u06ef\u06fa-\u06fc\u06ff\u0710\u0712-\u072f\u074d-\u07a5\u07b1\u07ca-\u07ea\u07f4\u07f5\u07fa\u0800-\u0815\u081a\u0824\u0828\u0840-\u0858\u08a0-\u08b2\u0904-\u0939\u093d\u0950\u0958-\u0961\u0971-\u0980\u0985-\u098c\u098f\u0990\u0993-\u09a8\u09aa-\u09b0\u09b2\u09b6-\u09b9\u09bd\u09ce\u09dc\u09dd\u09df-\u09e1\u09f0\u09f1\u0a05-\u0a0a\u0a0f\u0a10\u0a13-\u0a28\u0a2a-\u0a30\u0a32\u0a33\u0a35\u0a36\u0a38\u0a39\u0a59-\u0a5c\u0a5e\u0a72-\u0a74\u0a85-\u0a8d\u0a8f-\u0a91\u0a93-\u0aa8\u0aaa-\u0ab0\u0ab2\u0ab3\u0ab5-\u0ab9\u0abd\u0ad0\u0ae0\u0ae1\u0b05-\u0b0c\u0b0f\u0b10\u0b13-\u0b28\u0b2a-\u0b30\u0b32\u0b33\u0b35-\u0b39\u0b3d\u0b5c\u0b5d\u0b5f-\u0b61\u0b71\u0b83\u0b85-\u0b8a\u0b8e-\u0b90\u0b92-\u0b95\u0b99\u0b9a\u0b9c\u0b9e\u0b9f\u0ba3\u0ba4\u0ba8-\u0baa\u0bae-\u0bb9\u0bd0\u0c05-\u0c0c\u0c0e-\u0c10\u0c12-\u0c28\u0c2a-\u0c39\u0c3d\u0c58\u0c59\u0c60\u0c61\u0c85-\u0c8c\u0c8e-\u0c90\u0c92-\u0ca8\u0caa-\u0cb3\u0cb5-\u0cb9\u0cbd\u0cde\u0ce0\u0ce1\u0cf1\u0cf2\u0d05-\u0d0c\u0d0e-\u0d10\u0d12-\u0d3a\u0d3d\u0d4e\u0d60\u0d61\u0d7a-\u0d7f\u0d85-\u0d96\u0d9a-\u0db1\u0db3-\u0dbb\u0dbd\u0dc0-\u0dc6\u0e01-\u0e30\u0e32\u0e33\u0e40-\u0e46\u0e81\u0e82\u0e84\u0e87\u0e88\u0e8a\u0e8d\u0e94-\u0e97\u0e99-\u0e9f\u0ea1-\u0ea3\u0ea5\u0ea7\u0eaa\u0eab\u0ead-\u0eb0\u0eb2\u0eb3\u0ebd\u0ec0-\u0ec4\u0ec6\u0edc-\u0edf\u0f00\u0f40-\u0f47\u0f49-\u0f6c\u0f88-\u0f8c\u1000-\u102a\u103f\u1050-\u1055\u105a-\u105d\u1061\u1065\u1066\u106e-\u1070\u1075-\u1081\u108e\u10a0-\u10c5\u10c7\u10cd\u10d0-\u10fa\u10fc-\u1248\u124a-\u124d\u1250-\u1256\u1258\u125a-\u125d\u1260-\u1288\u128a-\u128d\u1290-\u12b0\u12b2-\u12b5\u12b8-\u12be\u12c0\u12c2-\u12c5\u12c8-\u12d6\u12d8-\u1310\u1312-\u1315\u1318-\u135a\u1380-\u138f\u13a0-\u13f4\u1401-\u166c\u166f-\u167f\u1681-\u169a\u16a0-\u16ea\u16ee-\u16f8\u1700-\u170c\u170e-\u1711\u1720-\u1731\u1740-\u1751\u1760-\u176c\u176e-\u1770\u1780-\u17b3\u17d7\u17dc\u1820-\u1877\u1880-\u18a8\u18aa\u18b0-\u18f5\u1900-\u191e\u1950-\u196d\u1970-\u1974\u1980-\u19ab\u19c1-\u19c7\u1a00-\u1a16\u1a20-\u1a54\u1aa7\u1b05-\u1b33\u1b45-\u1b4b\u1b83-\u1ba0\u1bae\u1baf\u1bba-\u1be5\u1c00-\u1c23\u1c4d-\u1c4f\u1c5a-\u1c7d\u1ce9-\u1cec\u1cee-\u1cf1\u1cf5\u1cf6\u1d00-\u1dbf\u1e00-\u1f15\u1f18-\u1f1d\u1f20-\u1f45\u1f48-\u1f4d\u1f50-\u1f57\u1f59\u1f5b\u1f5d\u1f5f-\u1f7d\u1f80-\u1fb4\u1fb6-\u1fbc\u1fbe\u1fc2-\u1fc4\u1fc6-\u1fcc\u1fd0-\u1fd3\u1fd6-\u1fdb\u1fe0-\u1fec\u1ff2-\u1ff4\u1ff6-\u1ffc\u2071\u207f\u2090-\u209c\u2102\u2107\u210a-\u2113\u2115\u2119-\u211d\u2124\u2126\u2128\u212a-\u212d\u212f-\u2139\u213c-\u213f\u2145-\u2149\u214e\u2160-\u2188\u2c00-\u2c2e\u2c30-\u2c5e\u2c60-\u2ce4\u2ceb-\u2cee\u2cf2\u2cf3\u2d00-\u2d25\u2d27\u2d2d\u2d30-\u2d67\u2d6f\u2d80-\u2d96\u2da0-\u2da6\u2da8-\u2dae\u2db0-\u2db6\u2db8-\u2dbe\u2dc0-\u2dc6\u2dc8-\u2dce\u2dd0-\u2dd6\u2dd8-\u2dde\u2e2f\u3005-\u3007\u3021-\u3029\u3031-\u3035\u3038-\u303c\u3041-\u3096\u309d-\u309f\u30a1-\u30fa\u30fc-\u30ff\u3105-\u312d\u3131-\u318e\u31a0-\u31ba\u31f0-\u31ff\u3400-\u4db5\u4e00-\u9fcc\ua000-\ua48c\ua4d0-\ua4fd\ua500-\ua60c\ua610-\ua61f\ua62a\ua62b\ua640-\ua66e\ua67f-\ua69d\ua6a0-\ua6ef\ua717-\ua71f\ua722-\ua788\ua78b-\ua78e\ua790-\ua7ad\ua7b0\ua7b1\ua7f7-\ua801\ua803-\ua805\ua807-\ua80a\ua80c-\ua822\ua840-\ua873\ua882-\ua8b3\ua8f2-\ua8f7\ua8fb\ua90a-\ua925\ua930-\ua946\ua960-\ua97c\ua984-\ua9b2\ua9cf\ua9e0-\ua9e4\ua9e6-\ua9ef\ua9fa-\ua9fe\uaa00-\uaa28\uaa40-\uaa42\uaa44-\uaa4b\uaa60-\uaa76\uaa7a\uaa7e-\uaaaf\uaab1\uaab5\uaab6\uaab9-\uaabd\uaac0\uaac2\uaadb-\uaadd\uaae0-\uaaea\uaaf2-\uaaf4\uab01-\uab06\uab09-\uab0e\uab11-\uab16\uab20-\uab26\uab28-\uab2e\uab30-\uab5a\uab5c-\uab5f\uab64\uab65\uabc0-\uabe2\uac00-\ud7a3\ud7b0-\ud7c6\ud7cb-\ud7fb\uf900-\ufa6d\ufa70-\ufad9\ufb00-\ufb06\ufb13-\ufb17\ufb1d\ufb1f-\ufb28\ufb2a-\ufb36\ufb38-\ufb3c\ufb3e\ufb40\ufb41\ufb43\ufb44\ufb46-\ufbb1\ufbd3-\ufd3d\ufd50-\ufd8f\ufd92-\ufdc7\ufdf0-\ufdfb\ufe70-\ufe74\ufe76-\ufefc\uff21-\uff3a\uff41-\uff5a\uff66-\uffbe\uffc2-\uffc7\uffca-\uffcf\uffd2-\uffd7\uffda-\uffdc]')),u'NonAsciiIdentifierPart':var.get(u'RegExp').create(Js(u'[\xaa\xb5\xba\xc0-\xd6\xd8-\xf6\xf8-\u02c1\u02c6-\u02d1\u02e0-\u02e4\u02ec\u02ee\u0300-\u0374\u0376\u0377\u037a-\u037d\u037f\u0386\u0388-\u038a\u038c\u038e-\u03a1\u03a3-\u03f5\u03f7-\u0481\u0483-\u0487\u048a-\u052f\u0531-\u0556\u0559\u0561-\u0587\u0591-\u05bd\u05bf\u05c1\u05c2\u05c4\u05c5\u05c7\u05d0-\u05ea\u05f0-\u05f2\u0610-\u061a\u0620-\u0669\u066e-\u06d3\u06d5-\u06dc\u06df-\u06e8\u06ea-\u06fc\u06ff\u0710-\u074a\u074d-\u07b1\u07c0-\u07f5\u07fa\u0800-\u082d\u0840-\u085b\u08a0-\u08b2\u08e4-\u0963\u0966-\u096f\u0971-\u0983\u0985-\u098c\u098f\u0990\u0993-\u09a8\u09aa-\u09b0\u09b2\u09b6-\u09b9\u09bc-\u09c4\u09c7\u09c8\u09cb-\u09ce\u09d7\u09dc\u09dd\u09df-\u09e3\u09e6-\u09f1\u0a01-\u0a03\u0a05-\u0a0a\u0a0f\u0a10\u0a13-\u0a28\u0a2a-\u0a30\u0a32\u0a33\u0a35\u0a36\u0a38\u0a39\u0a3c\u0a3e-\u0a42\u0a47\u0a48\u0a4b-\u0a4d\u0a51\u0a59-\u0a5c\u0a5e\u0a66-\u0a75\u0a81-\u0a83\u0a85-\u0a8d\u0a8f-\u0a91\u0a93-\u0aa8\u0aaa-\u0ab0\u0ab2\u0ab3\u0ab5-\u0ab9\u0abc-\u0ac5\u0ac7-\u0ac9\u0acb-\u0acd\u0ad0\u0ae0-\u0ae3\u0ae6-\u0aef\u0b01-\u0b03\u0b05-\u0b0c\u0b0f\u0b10\u0b13-\u0b28\u0b2a-\u0b30\u0b32\u0b33\u0b35-\u0b39\u0b3c-\u0b44\u0b47\u0b48\u0b4b-\u0b4d\u0b56\u0b57\u0b5c\u0b5d\u0b5f-\u0b63\u0b66-\u0b6f\u0b71\u0b82\u0b83\u0b85-\u0b8a\u0b8e-\u0b90\u0b92-\u0b95\u0b99\u0b9a\u0b9c\u0b9e\u0b9f\u0ba3\u0ba4\u0ba8-\u0baa\u0bae-\u0bb9\u0bbe-\u0bc2\u0bc6-\u0bc8\u0bca-\u0bcd\u0bd0\u0bd7\u0be6-\u0bef\u0c00-\u0c03\u0c05-\u0c0c\u0c0e-\u0c10\u0c12-\u0c28\u0c2a-\u0c39\u0c3d-\u0c44\u0c46-\u0c48\u0c4a-\u0c4d\u0c55\u0c56\u0c58\u0c59\u0c60-\u0c63\u0c66-\u0c6f\u0c81-\u0c83\u0c85-\u0c8c\u0c8e-\u0c90\u0c92-\u0ca8\u0caa-\u0cb3\u0cb5-\u0cb9\u0cbc-\u0cc4\u0cc6-\u0cc8\u0cca-\u0ccd\u0cd5\u0cd6\u0cde\u0ce0-\u0ce3\u0ce6-\u0cef\u0cf1\u0cf2\u0d01-\u0d03\u0d05-\u0d0c\u0d0e-\u0d10\u0d12-\u0d3a\u0d3d-\u0d44\u0d46-\u0d48\u0d4a-\u0d4e\u0d57\u0d60-\u0d63\u0d66-\u0d6f\u0d7a-\u0d7f\u0d82\u0d83\u0d85-\u0d96\u0d9a-\u0db1\u0db3-\u0dbb\u0dbd\u0dc0-\u0dc6\u0dca\u0dcf-\u0dd4\u0dd6\u0dd8-\u0ddf\u0de6-\u0def\u0df2\u0df3\u0e01-\u0e3a\u0e40-\u0e4e\u0e50-\u0e59\u0e81\u0e82\u0e84\u0e87\u0e88\u0e8a\u0e8d\u0e94-\u0e97\u0e99-\u0e9f\u0ea1-\u0ea3\u0ea5\u0ea7\u0eaa\u0eab\u0ead-\u0eb9\u0ebb-\u0ebd\u0ec0-\u0ec4\u0ec6\u0ec8-\u0ecd\u0ed0-\u0ed9\u0edc-\u0edf\u0f00\u0f18\u0f19\u0f20-\u0f29\u0f35\u0f37\u0f39\u0f3e-\u0f47\u0f49-\u0f6c\u0f71-\u0f84\u0f86-\u0f97\u0f99-\u0fbc\u0fc6\u1000-\u1049\u1050-\u109d\u10a0-\u10c5\u10c7\u10cd\u10d0-\u10fa\u10fc-\u1248\u124a-\u124d\u1250-\u1256\u1258\u125a-\u125d\u1260-\u1288\u128a-\u128d\u1290-\u12b0\u12b2-\u12b5\u12b8-\u12be\u12c0\u12c2-\u12c5\u12c8-\u12d6\u12d8-\u1310\u1312-\u1315\u1318-\u135a\u135d-\u135f\u1380-\u138f\u13a0-\u13f4\u1401-\u166c\u166f-\u167f\u1681-\u169a\u16a0-\u16ea\u16ee-\u16f8\u1700-\u170c\u170e-\u1714\u1720-\u1734\u1740-\u1753\u1760-\u176c\u176e-\u1770\u1772\u1773\u1780-\u17d3\u17d7\u17dc\u17dd\u17e0-\u17e9\u180b-\u180d\u1810-\u1819\u1820-\u1877\u1880-\u18aa\u18b0-\u18f5\u1900-\u191e\u1920-\u192b\u1930-\u193b\u1946-\u196d\u1970-\u1974\u1980-\u19ab\u19b0-\u19c9\u19d0-\u19d9\u1a00-\u1a1b\u1a20-\u1a5e\u1a60-\u1a7c\u1a7f-\u1a89\u1a90-\u1a99\u1aa7\u1ab0-\u1abd\u1b00-\u1b4b\u1b50-\u1b59\u1b6b-\u1b73\u1b80-\u1bf3\u1c00-\u1c37\u1c40-\u1c49\u1c4d-\u1c7d\u1cd0-\u1cd2\u1cd4-\u1cf6\u1cf8\u1cf9\u1d00-\u1df5\u1dfc-\u1f15\u1f18-\u1f1d\u1f20-\u1f45\u1f48-\u1f4d\u1f50-\u1f57\u1f59\u1f5b\u1f5d\u1f5f-\u1f7d\u1f80-\u1fb4\u1fb6-\u1fbc\u1fbe\u1fc2-\u1fc4\u1fc6-\u1fcc\u1fd0-\u1fd3\u1fd6-\u1fdb\u1fe0-\u1fec\u1ff2-\u1ff4\u1ff6-\u1ffc\u200c\u200d\u203f\u2040\u2054\u2071\u207f\u2090-\u209c\u20d0-\u20dc\u20e1\u20e5-\u20f0\u2102\u2107\u210a-\u2113\u2115\u2119-\u211d\u2124\u2126\u2128\u212a-\u212d\u212f-\u2139\u213c-\u213f\u2145-\u2149\u214e\u2160-\u2188\u2c00-\u2c2e\u2c30-\u2c5e\u2c60-\u2ce4\u2ceb-\u2cf3\u2d00-\u2d25\u2d27\u2d2d\u2d30-\u2d67\u2d6f\u2d7f-\u2d96\u2da0-\u2da6\u2da8-\u2dae\u2db0-\u2db6\u2db8-\u2dbe\u2dc0-\u2dc6\u2dc8-\u2dce\u2dd0-\u2dd6\u2dd8-\u2dde\u2de0-\u2dff\u2e2f\u3005-\u3007\u3021-\u302f\u3031-\u3035\u3038-\u303c\u3041-\u3096\u3099\u309a\u309d-\u309f\u30a1-\u30fa\u30fc-\u30ff\u3105-\u312d\u3131-\u318e\u31a0-\u31ba\u31f0-\u31ff\u3400-\u4db5\u4e00-\u9fcc\ua000-\ua48c\ua4d0-\ua4fd\ua500-\ua60c\ua610-\ua62b\ua640-\ua66f\ua674-\ua67d\ua67f-\ua69d\ua69f-\ua6f1\ua717-\ua71f\ua722-\ua788\ua78b-\ua78e\ua790-\ua7ad\ua7b0\ua7b1\ua7f7-\ua827\ua840-\ua873\ua880-\ua8c4\ua8d0-\ua8d9\ua8e0-\ua8f7\ua8fb\ua900-\ua92d\ua930-\ua953\ua960-\ua97c\ua980-\ua9c0\ua9cf-\ua9d9\ua9e0-\ua9fe\uaa00-\uaa36\uaa40-\uaa4d\uaa50-\uaa59\uaa60-\uaa76\uaa7a-\uaac2\uaadb-\uaadd\uaae0-\uaaef\uaaf2-\uaaf6\uab01-\uab06\uab09-\uab0e\uab11-\uab16\uab20-\uab26\uab28-\uab2e\uab30-\uab5a\uab5c-\uab5f\uab64\uab65\uabc0-\uabea\uabec\uabed\uabf0-\uabf9\uac00-\ud7a3\ud7b0-\ud7c6\ud7cb-\ud7fb\uf900-\ufa6d\ufa70-\ufad9\ufb00-\ufb06\ufb13-\ufb17\ufb1d-\ufb28\ufb2a-\ufb36\ufb38-\ufb3c\ufb3e\ufb40\ufb41\ufb43\ufb44\ufb46-\ufbb1\ufbd3-\ufd3d\ufd50-\ufd8f\ufd92-\ufdc7\ufdf0-\ufdfb\ufe00-\ufe0f\ufe20-\ufe2d\ufe33\ufe34\ufe4d-\ufe4f\ufe70-\ufe74\ufe76-\ufefc\uff10-\uff19\uff21-\uff3a\uff3f\uff41-\uff5a\uff66-\uffbe\uffc2-\uffc7\uffca-\uffcf\uffd2-\uffd7\uffda-\uffdc]'))})
    var.put(u'Regex', PyJs_Object_6_)
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
    def PyJs_anonymous_45_(this, arguments, var=var):
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
                var.put(u'comment', var.get(u'extra').get(u'trailingComments').get(var.get(u'i')))
                if (var.get(u'comment').get(u'range').get(u'0')>=var.get(u"this").get(u'range').get(u'1')):
                    var.get(u'trailingComments').callprop(u'unshift', var.get(u'comment'))
                    var.get(u'extra').get(u'trailingComments').callprop(u'splice', var.get(u'i'), Js(1.0))
                var.put(u'i',var.get(u'i')-Js(1))
            var.get(u'extra').put(u'trailingComments', Js([]))
        else:
            if ((var.get(u'last') and var.get(u'last').get(u'trailingComments')) and (var.get(u'last').get(u'trailingComments').get(u'0').get(u'range').get(u'0')>=var.get(u"this").get(u'range').get(u'1'))):
                var.put(u'trailingComments', var.get(u'last').get(u'trailingComments'))
                var.get(u'last').delete(u'trailingComments')
        if var.get(u'last'):
            while (var.get(u'last') and (var.get(u'last').get(u'range').get(u'0')>=var.get(u"this").get(u'range').get(u'0'))):
                var.put(u'lastChild', var.get(u'last'))
                var.put(u'last', var.get(u'bottomRight').callprop(u'pop'))
        if var.get(u'lastChild'):
            if (var.get(u'lastChild').get(u'leadingComments') and (var.get(u'lastChild').get(u'leadingComments').get((var.get(u'lastChild').get(u'leadingComments').get(u'length')-Js(1.0))).get(u'range').get(u'1')<=var.get(u"this").get(u'range').get(u'0'))):
                var.get(u"this").put(u'leadingComments', var.get(u'lastChild').get(u'leadingComments'))
                var.get(u'lastChild').put(u'leadingComments', var.get(u'undefined'))
        else:
            if (var.get(u'extra').get(u'leadingComments').get(u'length')>Js(0.0)):
                var.put(u'leadingComments', Js([]))
                #for JS loop
                var.put(u'i', (var.get(u'extra').get(u'leadingComments').get(u'length')-Js(1.0)))
                while (var.get(u'i')>=Js(0.0)):
                    var.put(u'comment', var.get(u'extra').get(u'leadingComments').get(var.get(u'i')))
                    if (var.get(u'comment').get(u'range').get(u'1')<=var.get(u"this").get(u'range').get(u'0')):
                        var.get(u'leadingComments').callprop(u'unshift', var.get(u'comment'))
                        var.get(u'extra').get(u'leadingComments').callprop(u'splice', var.get(u'i'), Js(1.0))
                    var.put(u'i',var.get(u'i')-Js(1))
        if (var.get(u'leadingComments') and (var.get(u'leadingComments').get(u'length')>Js(0.0))):
            var.get(u"this").put(u'leadingComments', var.get(u'leadingComments'))
        if (var.get(u'trailingComments') and (var.get(u'trailingComments').get(u'length')>Js(0.0))):
            var.get(u"this").put(u'trailingComments', var.get(u'trailingComments'))
        var.get(u'bottomRight').callprop(u'push', var.get(u"this"))
    PyJs_anonymous_45_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_46_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        if var.get(u'extra').get(u'range'):
            var.get(u"this").get(u'range').put(u'1', var.get(u'lastIndex'))
        if var.get(u'extra').get(u'loc'):
            PyJs_Object_47_ = Js({u'line':var.get(u'lastLineNumber'),u'column':(var.get(u'lastIndex')-var.get(u'lastLineStart'))})
            var.get(u"this").get(u'loc').put(u'end', PyJs_Object_47_)
            if var.get(u'extra').get(u'source'):
                var.get(u"this").get(u'loc').put(u'source', var.get(u'extra').get(u'source'))
        if var.get(u'extra').get(u'attachComment'):
            var.get(u"this").callprop(u'processComment')
    PyJs_anonymous_46_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_48_(elements, this, arguments, var=var):
        var = Scope({u'this':this, u'elements':elements, u'arguments':arguments}, var)
        var.registers([u'elements'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ArrayExpression'))
        var.get(u"this").put(u'elements', var.get(u'elements'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_48_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_49_(elements, this, arguments, var=var):
        var = Scope({u'this':this, u'elements':elements, u'arguments':arguments}, var)
        var.registers([u'elements'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ArrayPattern'))
        var.get(u"this").put(u'elements', var.get(u'elements'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_49_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_50_(params, defaults, body, expression, this, arguments, var=var):
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
    PyJs_anonymous_50_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_51_(operator, left, right, this, arguments, var=var):
        var = Scope({u'operator':operator, u'this':this, u'right':right, u'arguments':arguments, u'left':left}, var)
        var.registers([u'operator', u'right', u'left'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'AssignmentExpression'))
        var.get(u"this").put(u'operator', var.get(u'operator'))
        var.get(u"this").put(u'left', var.get(u'left'))
        var.get(u"this").put(u'right', var.get(u'right'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_51_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_52_(left, right, this, arguments, var=var):
        var = Scope({u'this':this, u'right':right, u'arguments':arguments, u'left':left}, var)
        var.registers([u'right', u'left'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'AssignmentPattern'))
        var.get(u"this").put(u'left', var.get(u'left'))
        var.get(u"this").put(u'right', var.get(u'right'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_52_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_53_(operator, left, right, this, arguments, var=var):
        var = Scope({u'operator':operator, u'this':this, u'right':right, u'arguments':arguments, u'left':left}, var)
        var.registers([u'operator', u'right', u'left'])
        var.get(u"this").put(u'type', (var.get(u'Syntax').get(u'LogicalExpression') if (PyJsStrictEq(var.get(u'operator'),Js(u'||')) or PyJsStrictEq(var.get(u'operator'),Js(u'&&'))) else var.get(u'Syntax').get(u'BinaryExpression')))
        var.get(u"this").put(u'operator', var.get(u'operator'))
        var.get(u"this").put(u'left', var.get(u'left'))
        var.get(u"this").put(u'right', var.get(u'right'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_53_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_54_(body, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'arguments':arguments}, var)
        var.registers([u'body'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'BlockStatement'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_54_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_55_(label, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'label':label}, var)
        var.registers([u'label'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'BreakStatement'))
        var.get(u"this").put(u'label', var.get(u'label'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_55_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_56_(callee, args, this, arguments, var=var):
        var = Scope({u'this':this, u'args':args, u'callee':callee, u'arguments':arguments}, var)
        var.registers([u'args', u'callee'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'CallExpression'))
        var.get(u"this").put(u'callee', var.get(u'callee'))
        var.get(u"this").put(u'arguments', var.get(u'args'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_56_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_57_(param, body, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'arguments':arguments, u'param':param}, var)
        var.registers([u'body', u'param'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'CatchClause'))
        var.get(u"this").put(u'param', var.get(u'param'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_57_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_58_(body, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'arguments':arguments}, var)
        var.registers([u'body'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ClassBody'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_58_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_59_(id, superClass, body, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'id':id, u'arguments':arguments, u'superClass':superClass}, var)
        var.registers([u'body', u'id', u'superClass'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ClassDeclaration'))
        var.get(u"this").put(u'id', var.get(u'id'))
        var.get(u"this").put(u'superClass', var.get(u'superClass'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_59_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_60_(id, superClass, body, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'id':id, u'arguments':arguments, u'superClass':superClass}, var)
        var.registers([u'body', u'id', u'superClass'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ClassExpression'))
        var.get(u"this").put(u'id', var.get(u'id'))
        var.get(u"this").put(u'superClass', var.get(u'superClass'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_60_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_61_(test, consequent, alternate, this, arguments, var=var):
        var = Scope({u'test':test, u'this':this, u'alternate':alternate, u'arguments':arguments, u'consequent':consequent}, var)
        var.registers([u'test', u'alternate', u'consequent'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ConditionalExpression'))
        var.get(u"this").put(u'test', var.get(u'test'))
        var.get(u"this").put(u'consequent', var.get(u'consequent'))
        var.get(u"this").put(u'alternate', var.get(u'alternate'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_61_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_62_(label, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'label':label}, var)
        var.registers([u'label'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ContinueStatement'))
        var.get(u"this").put(u'label', var.get(u'label'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_62_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_63_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'DebuggerStatement'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_63_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_64_(body, test, this, arguments, var=var):
        var = Scope({u'body':body, u'test':test, u'this':this, u'arguments':arguments}, var)
        var.registers([u'body', u'test'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'DoWhileStatement'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").put(u'test', var.get(u'test'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_64_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_65_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'EmptyStatement'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_65_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_66_(expression, this, arguments, var=var):
        var = Scope({u'this':this, u'expression':expression, u'arguments':arguments}, var)
        var.registers([u'expression'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ExpressionStatement'))
        var.get(u"this").put(u'expression', var.get(u'expression'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_66_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_67_(init, test, update, body, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'init':init, u'arguments':arguments, u'test':test, u'update':update}, var)
        var.registers([u'test', u'body', u'init', u'update'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ForStatement'))
        var.get(u"this").put(u'init', var.get(u'init'))
        var.get(u"this").put(u'test', var.get(u'test'))
        var.get(u"this").put(u'update', var.get(u'update'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_67_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_68_(left, right, body, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'right':right, u'arguments':arguments, u'left':left}, var)
        var.registers([u'body', u'right', u'left'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ForInStatement'))
        var.get(u"this").put(u'left', var.get(u'left'))
        var.get(u"this").put(u'right', var.get(u'right'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").put(u'each', Js(False))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_68_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_69_(id, params, defaults, body, this, arguments, var=var):
        var = Scope({u'body':body, u'params':params, u'arguments':arguments, u'defaults':defaults, u'this':this, u'id':id}, var)
        var.registers([u'body', u'params', u'id', u'defaults'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'FunctionDeclaration'))
        var.get(u"this").put(u'id', var.get(u'id'))
        var.get(u"this").put(u'params', var.get(u'params'))
        var.get(u"this").put(u'defaults', var.get(u'defaults'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").put(u'generator', Js(False))
        var.get(u"this").put(u'expression', Js(False))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_69_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_70_(id, params, defaults, body, this, arguments, var=var):
        var = Scope({u'body':body, u'params':params, u'arguments':arguments, u'defaults':defaults, u'this':this, u'id':id}, var)
        var.registers([u'body', u'params', u'id', u'defaults'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'FunctionExpression'))
        var.get(u"this").put(u'id', var.get(u'id'))
        var.get(u"this").put(u'params', var.get(u'params'))
        var.get(u"this").put(u'defaults', var.get(u'defaults'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").put(u'generator', Js(False))
        var.get(u"this").put(u'expression', Js(False))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_70_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_71_(name, this, arguments, var=var):
        var = Scope({u'this':this, u'name':name, u'arguments':arguments}, var)
        var.registers([u'name'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'Identifier'))
        var.get(u"this").put(u'name', var.get(u'name'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_71_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_72_(test, consequent, alternate, this, arguments, var=var):
        var = Scope({u'test':test, u'this':this, u'alternate':alternate, u'arguments':arguments, u'consequent':consequent}, var)
        var.registers([u'test', u'alternate', u'consequent'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'IfStatement'))
        var.get(u"this").put(u'test', var.get(u'test'))
        var.get(u"this").put(u'consequent', var.get(u'consequent'))
        var.get(u"this").put(u'alternate', var.get(u'alternate'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_72_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_73_(label, body, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'arguments':arguments, u'label':label}, var)
        var.registers([u'body', u'label'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'LabeledStatement'))
        var.get(u"this").put(u'label', var.get(u'label'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_73_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_74_(token, this, arguments, var=var):
        var = Scope({u'this':this, u'token':token, u'arguments':arguments}, var)
        var.registers([u'token'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'Literal'))
        var.get(u"this").put(u'value', var.get(u'token').get(u'value'))
        var.get(u"this").put(u'raw', var.get(u'source').callprop(u'slice', var.get(u'token').get(u'start'), var.get(u'token').get(u'end')))
        if var.get(u'token').get(u'regex'):
            var.get(u"this").put(u'regex', var.get(u'token').get(u'regex'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_74_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_75_(accessor, object, property, this, arguments, var=var):
        var = Scope({u'this':this, u'property':property, u'object':object, u'accessor':accessor, u'arguments':arguments}, var)
        var.registers([u'property', u'object', u'accessor'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'MemberExpression'))
        var.get(u"this").put(u'computed', PyJsStrictEq(var.get(u'accessor'),Js(u'[')))
        var.get(u"this").put(u'object', var.get(u'object'))
        var.get(u"this").put(u'property', var.get(u'property'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_75_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_76_(callee, args, this, arguments, var=var):
        var = Scope({u'this':this, u'args':args, u'callee':callee, u'arguments':arguments}, var)
        var.registers([u'args', u'callee'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'NewExpression'))
        var.get(u"this").put(u'callee', var.get(u'callee'))
        var.get(u"this").put(u'arguments', var.get(u'args'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_76_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_77_(properties, this, arguments, var=var):
        var = Scope({u'this':this, u'properties':properties, u'arguments':arguments}, var)
        var.registers([u'properties'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ObjectExpression'))
        var.get(u"this").put(u'properties', var.get(u'properties'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_77_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_78_(properties, this, arguments, var=var):
        var = Scope({u'this':this, u'properties':properties, u'arguments':arguments}, var)
        var.registers([u'properties'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ObjectPattern'))
        var.get(u"this").put(u'properties', var.get(u'properties'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_78_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_79_(operator, argument, this, arguments, var=var):
        var = Scope({u'operator':operator, u'this':this, u'argument':argument, u'arguments':arguments}, var)
        var.registers([u'operator', u'argument'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'UpdateExpression'))
        var.get(u"this").put(u'operator', var.get(u'operator'))
        var.get(u"this").put(u'argument', var.get(u'argument'))
        var.get(u"this").put(u'prefix', Js(False))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_79_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_80_(body, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'arguments':arguments}, var)
        var.registers([u'body'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'Program'))
        var.get(u"this").put(u'body', var.get(u'body'))
        if PyJsStrictEq(var.get(u'sourceType'),Js(u'module')):
            var.get(u"this").put(u'sourceType', var.get(u'sourceType'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_80_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_81_(kind, key, computed, value, method, shorthand, this, arguments, var=var):
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
    PyJs_anonymous_81_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_82_(argument, this, arguments, var=var):
        var = Scope({u'this':this, u'argument':argument, u'arguments':arguments}, var)
        var.registers([u'argument'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'RestElement'))
        var.get(u"this").put(u'argument', var.get(u'argument'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_82_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_83_(argument, this, arguments, var=var):
        var = Scope({u'this':this, u'argument':argument, u'arguments':arguments}, var)
        var.registers([u'argument'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ReturnStatement'))
        var.get(u"this").put(u'argument', var.get(u'argument'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_83_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_84_(expressions, this, arguments, var=var):
        var = Scope({u'this':this, u'expressions':expressions, u'arguments':arguments}, var)
        var.registers([u'expressions'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'SequenceExpression'))
        var.get(u"this").put(u'expressions', var.get(u'expressions'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_84_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_85_(argument, this, arguments, var=var):
        var = Scope({u'this':this, u'argument':argument, u'arguments':arguments}, var)
        var.registers([u'argument'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'SpreadElement'))
        var.get(u"this").put(u'argument', var.get(u'argument'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_85_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_86_(test, consequent, this, arguments, var=var):
        var = Scope({u'test':test, u'this':this, u'arguments':arguments, u'consequent':consequent}, var)
        var.registers([u'test', u'consequent'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'SwitchCase'))
        var.get(u"this").put(u'test', var.get(u'test'))
        var.get(u"this").put(u'consequent', var.get(u'consequent'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_86_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_87_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'Super'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_87_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_88_(discriminant, cases, this, arguments, var=var):
        var = Scope({u'this':this, u'cases':cases, u'arguments':arguments, u'discriminant':discriminant}, var)
        var.registers([u'cases', u'discriminant'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'SwitchStatement'))
        var.get(u"this").put(u'discriminant', var.get(u'discriminant'))
        var.get(u"this").put(u'cases', var.get(u'cases'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_88_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_89_(tag, quasi, this, arguments, var=var):
        var = Scope({u'this':this, u'quasi':quasi, u'tag':tag, u'arguments':arguments}, var)
        var.registers([u'quasi', u'tag'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'TaggedTemplateExpression'))
        var.get(u"this").put(u'tag', var.get(u'tag'))
        var.get(u"this").put(u'quasi', var.get(u'quasi'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_89_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_90_(value, tail, this, arguments, var=var):
        var = Scope({u'this':this, u'tail':tail, u'arguments':arguments, u'value':value}, var)
        var.registers([u'tail', u'value'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'TemplateElement'))
        var.get(u"this").put(u'value', var.get(u'value'))
        var.get(u"this").put(u'tail', var.get(u'tail'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_90_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_91_(quasis, expressions, this, arguments, var=var):
        var = Scope({u'quasis':quasis, u'this':this, u'expressions':expressions, u'arguments':arguments}, var)
        var.registers([u'quasis', u'expressions'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'TemplateLiteral'))
        var.get(u"this").put(u'quasis', var.get(u'quasis'))
        var.get(u"this").put(u'expressions', var.get(u'expressions'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_91_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_92_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ThisExpression'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_92_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_93_(argument, this, arguments, var=var):
        var = Scope({u'this':this, u'argument':argument, u'arguments':arguments}, var)
        var.registers([u'argument'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ThrowStatement'))
        var.get(u"this").put(u'argument', var.get(u'argument'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_93_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_94_(block, handler, finalizer, this, arguments, var=var):
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
    PyJs_anonymous_94_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_95_(operator, argument, this, arguments, var=var):
        var = Scope({u'operator':operator, u'this':this, u'argument':argument, u'arguments':arguments}, var)
        var.registers([u'operator', u'argument'])
        var.get(u"this").put(u'type', (var.get(u'Syntax').get(u'UpdateExpression') if (PyJsStrictEq(var.get(u'operator'),Js(u'++')) or PyJsStrictEq(var.get(u'operator'),Js(u'--'))) else var.get(u'Syntax').get(u'UnaryExpression')))
        var.get(u"this").put(u'operator', var.get(u'operator'))
        var.get(u"this").put(u'argument', var.get(u'argument'))
        var.get(u"this").put(u'prefix', var.get(u'true'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_95_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_96_(declarations, this, arguments, var=var):
        var = Scope({u'this':this, u'declarations':declarations, u'arguments':arguments}, var)
        var.registers([u'declarations'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'VariableDeclaration'))
        var.get(u"this").put(u'declarations', var.get(u'declarations'))
        var.get(u"this").put(u'kind', Js(u'var'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_96_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_97_(declarations, kind, this, arguments, var=var):
        var = Scope({u'this':this, u'kind':kind, u'declarations':declarations, u'arguments':arguments}, var)
        var.registers([u'kind', u'declarations'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'VariableDeclaration'))
        var.get(u"this").put(u'declarations', var.get(u'declarations'))
        var.get(u"this").put(u'kind', var.get(u'kind'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_97_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_98_(id, init, this, arguments, var=var):
        var = Scope({u'this':this, u'init':init, u'id':id, u'arguments':arguments}, var)
        var.registers([u'init', u'id'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'VariableDeclarator'))
        var.get(u"this").put(u'id', var.get(u'id'))
        var.get(u"this").put(u'init', var.get(u'init'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_98_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_99_(test, body, this, arguments, var=var):
        var = Scope({u'test':test, u'body':body, u'this':this, u'arguments':arguments}, var)
        var.registers([u'test', u'body'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'WhileStatement'))
        var.get(u"this").put(u'test', var.get(u'test'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_99_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_100_(object, body, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'object':object, u'arguments':arguments}, var)
        var.registers([u'body', u'object'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'WithStatement'))
        var.get(u"this").put(u'object', var.get(u'object'))
        var.get(u"this").put(u'body', var.get(u'body'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_100_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_101_(local, exported, this, arguments, var=var):
        var = Scope({u'this':this, u'local':local, u'exported':exported, u'arguments':arguments}, var)
        var.registers([u'local', u'exported'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ExportSpecifier'))
        var.get(u"this").put(u'exported', (var.get(u'exported') or var.get(u'local')))
        var.get(u"this").put(u'local', var.get(u'local'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_101_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_102_(local, this, arguments, var=var):
        var = Scope({u'this':this, u'local':local, u'arguments':arguments}, var)
        var.registers([u'local'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ImportDefaultSpecifier'))
        var.get(u"this").put(u'local', var.get(u'local'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_102_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_103_(local, this, arguments, var=var):
        var = Scope({u'this':this, u'local':local, u'arguments':arguments}, var)
        var.registers([u'local'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ImportNamespaceSpecifier'))
        var.get(u"this").put(u'local', var.get(u'local'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_103_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_104_(declaration, specifiers, src, this, arguments, var=var):
        var = Scope({u'this':this, u'specifiers':specifiers, u'src':src, u'arguments':arguments, u'declaration':declaration}, var)
        var.registers([u'specifiers', u'src', u'declaration'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ExportNamedDeclaration'))
        var.get(u"this").put(u'declaration', var.get(u'declaration'))
        var.get(u"this").put(u'specifiers', var.get(u'specifiers'))
        var.get(u"this").put(u'source', var.get(u'src'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_104_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_105_(declaration, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'declaration':declaration}, var)
        var.registers([u'declaration'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ExportDefaultDeclaration'))
        var.get(u"this").put(u'declaration', var.get(u'declaration'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_105_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_106_(src, this, arguments, var=var):
        var = Scope({u'this':this, u'src':src, u'arguments':arguments}, var)
        var.registers([u'src'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ExportAllDeclaration'))
        var.get(u"this").put(u'source', var.get(u'src'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_106_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_107_(local, imported, this, arguments, var=var):
        var = Scope({u'this':this, u'imported':imported, u'local':local, u'arguments':arguments}, var)
        var.registers([u'imported', u'local'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ImportSpecifier'))
        var.get(u"this").put(u'local', (var.get(u'local') or var.get(u'imported')))
        var.get(u"this").put(u'imported', var.get(u'imported'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_107_.func_name = u'anonymous'
    @Js
    def PyJs_anonymous_108_(specifiers, src, this, arguments, var=var):
        var = Scope({u'this':this, u'specifiers':specifiers, u'arguments':arguments, u'src':src}, var)
        var.registers([u'specifiers', u'src'])
        var.get(u"this").put(u'type', var.get(u'Syntax').get(u'ImportDeclaration'))
        var.get(u"this").put(u'specifiers', var.get(u'specifiers'))
        var.get(u"this").put(u'source', var.get(u'src'))
        var.get(u"this").callprop(u'finish')
        return var.get(u"this")
    PyJs_anonymous_108_.func_name = u'anonymous'
    PyJs_Object_44_ = Js({u'processComment':PyJs_anonymous_45_,u'finish':PyJs_anonymous_46_,u'finishArrayExpression':PyJs_anonymous_48_,u'finishArrayPattern':PyJs_anonymous_49_,u'finishArrowFunctionExpression':PyJs_anonymous_50_,u'finishAssignmentExpression':PyJs_anonymous_51_,u'finishAssignmentPattern':PyJs_anonymous_52_,u'finishBinaryExpression':PyJs_anonymous_53_,u'finishBlockStatement':PyJs_anonymous_54_,u'finishBreakStatement':PyJs_anonymous_55_,u'finishCallExpression':PyJs_anonymous_56_,u'finishCatchClause':PyJs_anonymous_57_,u'finishClassBody':PyJs_anonymous_58_,u'finishClassDeclaration':PyJs_anonymous_59_,u'finishClassExpression':PyJs_anonymous_60_,u'finishConditionalExpression':PyJs_anonymous_61_,u'finishContinueStatement':PyJs_anonymous_62_,u'finishDebuggerStatement':PyJs_anonymous_63_,u'finishDoWhileStatement':PyJs_anonymous_64_,u'finishEmptyStatement':PyJs_anonymous_65_,u'finishExpressionStatement':PyJs_anonymous_66_,u'finishForStatement':PyJs_anonymous_67_,u'finishForInStatement':PyJs_anonymous_68_,u'finishFunctionDeclaration':PyJs_anonymous_69_,u'finishFunctionExpression':PyJs_anonymous_70_,u'finishIdentifier':PyJs_anonymous_71_,u'finishIfStatement':PyJs_anonymous_72_,u'finishLabeledStatement':PyJs_anonymous_73_,u'finishLiteral':PyJs_anonymous_74_,u'finishMemberExpression':PyJs_anonymous_75_,u'finishNewExpression':PyJs_anonymous_76_,u'finishObjectExpression':PyJs_anonymous_77_,u'finishObjectPattern':PyJs_anonymous_78_,u'finishPostfixExpression':PyJs_anonymous_79_,u'finishProgram':PyJs_anonymous_80_,u'finishProperty':PyJs_anonymous_81_,u'finishRestElement':PyJs_anonymous_82_,u'finishReturnStatement':PyJs_anonymous_83_,u'finishSequenceExpression':PyJs_anonymous_84_,u'finishSpreadElement':PyJs_anonymous_85_,u'finishSwitchCase':PyJs_anonymous_86_,u'finishSuper':PyJs_anonymous_87_,u'finishSwitchStatement':PyJs_anonymous_88_,u'finishTaggedTemplateExpression':PyJs_anonymous_89_,u'finishTemplateElement':PyJs_anonymous_90_,u'finishTemplateLiteral':PyJs_anonymous_91_,u'finishThisExpression':PyJs_anonymous_92_,u'finishThrowStatement':PyJs_anonymous_93_,u'finishTryStatement':PyJs_anonymous_94_,u'finishUnaryExpression':PyJs_anonymous_95_,u'finishVariableDeclaration':PyJs_anonymous_96_,u'finishLexicalDeclaration':PyJs_anonymous_97_,u'finishVariableDeclarator':PyJs_anonymous_98_,u'finishWhileStatement':PyJs_anonymous_99_,u'finishWithStatement':PyJs_anonymous_100_,u'finishExportSpecifier':PyJs_anonymous_101_,u'finishImportDefaultSpecifier':PyJs_anonymous_102_,u'finishImportNamespaceSpecifier':PyJs_anonymous_103_,u'finishExportNamedDeclaration':PyJs_anonymous_104_,u'finishExportDefaultDeclaration':PyJs_anonymous_105_,u'finishExportAllDeclaration':PyJs_anonymous_106_,u'finishImportSpecifier':PyJs_anonymous_107_,u'finishImportDeclaration':PyJs_anonymous_108_})
    var.get(u'WrappingNode').put(u'prototype', var.get(u'Node').put(u'prototype', PyJs_Object_44_))
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
    var.get(u'exports').put(u'version', Js(u'2.2.0'))
    var.get(u'exports').put(u'tokenize', var.get(u'tokenize'))
    var.get(u'exports').put(u'parse', var.get(u'parse'))
    @Js
    def PyJs_anonymous_142_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'name', u'types'])
        PyJs_Object_143_ = Js({})
        var.put(u'types', PyJs_Object_143_)
        if PyJsStrictEq(var.get(u'Object').get(u'create').typeof(),Js(u'function')):
            var.put(u'types', var.get(u'Object').callprop(u'create', var.get(u"null")))
        for PyJsTemp in var.get(u'Syntax'):
            var.put(u'name', PyJsTemp)
            if var.get(u'Syntax').callprop(u'hasOwnProperty', var.get(u'name')):
                var.get(u'types').put(var.get(u'name'), var.get(u'Syntax').get(var.get(u'name')))
        if PyJsStrictEq(var.get(u'Object').get(u'freeze').typeof(),Js(u'function')):
            var.get(u'Object').callprop(u'freeze', var.get(u'types'))
        return var.get(u'types')
    PyJs_anonymous_142_.func_name = u'anonymous'
    var.get(u'exports').put(u'Syntax', PyJs_anonymous_142_())
PyJs_anonymous_0_.func_name = u'anonymous'
@Js
def PyJs_anonymous_144_(root, factory, this, arguments, var=var):
    var = Scope({u'this':this, u'root':root, u'factory':factory, u'arguments':arguments}, var)
    var.registers([u'root', u'factory'])
    Js(u'use strict')
    if (PyJsStrictEq(var.get(u'define',throw=False).typeof(),Js(u'function')) and var.get(u'define').get(u'amd')):
        var.get(u'define')(Js([Js(u'exports')]), var.get(u'factory'))
    else:
        if PyJsStrictNeq(var.get(u'exports',throw=False).typeof(),Js(u'undefined')):
            var.get(u'factory')(var.get(u'exports'))
        else:
            PyJs_Object_145_ = Js({})
            var.get(u'factory')(var.get(u'root').put(u'esprima', PyJs_Object_145_))
PyJs_anonymous_144_.func_name = u'anonymous'
PyJs_anonymous_144_(var.get(u"this"), PyJs_anonymous_0_)
pass



esprima = var.get('esprima').to_python()
