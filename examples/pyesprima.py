# By Piotr Dabkowski
# https://github.com/PiotrDabkowski/Js2Py
####################
"""
Translation of esprima (https://github.com/ariya/esprima/blob/master/esprima.js) to Python.

Note you will need js2py to use this module:
https://github.com/PiotrDabkowski/Js2Py

Usage:
parse('function a() {}')

Remember to access properties with [] 
esprima['tokenize'] is OK while esprima.tokenize will not work
"""

from js2py.pyjs import *
var = Scope( JS_BUILTINS )
set_global_object(var)
@Js
def PyJsLvalInline1_(root, factory, this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments, u'root':root, u'factory':factory}, var)
    Js(u'use strict')
    if (PyJsStrictEq(var.get(u'define',throw=False).typeof(),Js(u'function')) and var.get(u'define').get(u'amd')):
        PyJsLvalArray1_ = Js([Js(u'exports')])
        var.get(u'define')(PyJsLvalArray1_,var.get(u'factory'))
        pass
    elif PyJsStrictNeq(var.get(u'exports',throw=False).typeof(),Js(u'undefined')):
        var.get(u'factory')(var.get(u'exports'))
        pass
    else:
        PyJsLvalObject1_ = Js({})
        var.get(u'factory')((var.get(u'root').put(u'esprima', PyJsLvalObject1_)))
        pass
    pass
    pass
@Js
def PyJsLvalInline2_(exports, this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments, u'exports':exports}, var)
    var.registers([u'Token', u'TokenName', u'FnExprTokens', u'Syntax', u'PlaceHolders', u'PropertyKind', u'Messages', u'Regex', u'source', u'strict', u'index', u'lineNumber', u'lineStart', u'length', u'lookahead', u'state', u'extra', u'consumeSemicolon', u'parseForVariableDeclaration', u'parseLeftHandSideExpression', u'parseParams', u'parseExpressionStatement', u'advanceSlash', u'parseSourceElements', u'parseIfStatement', u'WrappingSourceLocation', u'scanStringLiteral', u'parseThrowStatement', u'addComment', u'parseSwitchStatement', u'match', u'parseEmptyStatement', u'parseConditionalExpression', u'parseVariableDeclaration', u'Position', u'isWhiteSpace', u'parseWhileStatement', u'validateParam', u'parseGroupExpression', u'scanHexLiteral', u'parseBreakStatement', u'getEscapedIdentifier', u'SourceLocation', u'parsePrimaryExpression', u'scanRegExpFlags', u'parseVariableDeclarationList', u'parseFunctionExpression', u'parseReturnStatement', u'parseUnaryExpression', u'collectRegex', u'expect', u'skipMultiLineComment', u'scanNumericLiteral', u'isIdentifierStart', u'expectTolerant', u'parseProgram', u'isOctalDigit', u'isDecimalDigit', u'parseObjectProperty', u'parseCatchClause', u'peek', u'parseArguments', u'testRegExp', u'parseStatement', u'parseObjectInitialiser', u'isLineTerminator', u'parseStatementList', u'lex', u'parseFunctionSourceElements', u'throwErrorTolerant', u'isIdentifierName', u'advance', u'throwUnexpected', u'parseArrayInitialiser', u'isFutureReservedWord', u'scanOctalLiteral', u'isKeyword', u'parseBinaryExpression', u'scanIdentifier', u'parseNonComputedProperty', u'parseParam', u'parseNewExpression', u'scanRegExpBody', u'Node', u'collectToken', u'parseWithStatement', u'reinterpretAsCoverFormalsList', u'skipComment', u'parseVariableStatement', u'parseDebuggerStatement', u'tokenize', u'parseExpression', u'parseObjectPropertyKey', u'expectKeyword', u'assert', u'parseConciseBody', u'parseLeftHandSideExpressionAllowCall', u'parseBlock', u'parseConstLetDeclaration', u'skipSingleLineComment', u'parseDoWhileStatement', u'parseSourceElement', u'scanHexEscape', u'isHexDigit', u'isStrictModeReservedWord', u'binaryPrecedence', u'parse', u'matchAssign', u'WrappingNode', u'getIdentifier', u'isRestrictedWord', u'parseSwitchCase', u'parseFunctionDeclaration', u'parsePostfixExpression', u'parseNonComputedMember', u'filterTokenLocation', u'peekLineTerminator', u'parsePropertyFunction', u'isLeftHandSide', u'scanPunctuator', u'parseArrowFunctionExpression', u'throwError', u'scanUnicodeCodePointEscape', u'parseAssignmentExpression', u'scanRegExp', u'parseVariableIdentifier', u'parseForStatement', u'isIdentifierPart', u'matchKeyword', u'parseTryStatement', u'parseComputedMember', u'parseContinueStatement'])
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'line'])
        pass
        if (PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt',var.get(u'index')),Js(0x3B)) or var.get(u'match')(Js(u';'))):
            var.get(u'lex')()
            return var.get('undefined')
            pass
        var.put(u'line', var.get(u'lineNumber'))
        var.get(u'skipComment')()
        if PyJsStrictNeq(var.get(u'lineNumber'),var.get(u'line')):
            return var.get('undefined')
            pass
        if (PyJsStrictNeq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'EOF')) and var.get(u'match')(Js(u'}')).neg()):
            var.get(u'throwUnexpected')(var.get(u'lookahead'))
            pass
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'consumeSemicolon'
    var.put(u'consumeSemicolon', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'token', u'declarations', u'node'])
        var.put(u'node', var.get(u'Node').create())
        var.put(u'token', var.get(u'lex')())
        var.put(u'declarations', var.get(u'parseVariableDeclarationList')())
        return var.get(u'node').callprop(u'finishVariableDeclaration',var.get(u'declarations'),var.get(u'token').get(u'value'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseForVariableDeclaration'
    var.put(u'parseForVariableDeclaration', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'expr', u'property', u'startToken'])
        pass
        var.get(u'assert')(var.get(u'state').get(u'allowIn'),Js(u'callee of new expression always allow in keyword.'))
        var.put(u'startToken', var.get(u'lookahead'))
        var.put(u'expr', (var.get(u'parseNewExpression')() if var.put(u'expr', var.get(u'matchKeyword')(Js(u'new'))) else var.get(u'parsePrimaryExpression')()))
        #for JS loop
        while 1:
            if var.get(u'match')(Js(u'[')):
                var.put(u'property', var.get(u'parseComputedMember')())
                var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishMemberExpression',Js(u'['),var.get(u'expr'),var.get(u'property')))
                pass
            elif var.get(u'match')(Js(u'.')):
                var.put(u'property', var.get(u'parseNonComputedMember')())
                var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishMemberExpression',Js(u'.'),var.get(u'expr'),var.get(u'property')))
                pass
            else:
                break
                pass
            pass
            
        return var.get(u'expr')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseLeftHandSideExpression'
    var.put(u'parseLeftHandSideExpression', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(firstRestricted, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'firstRestricted':firstRestricted}, var)
        var.registers([u'options'])
        pass
        PyJsLvalArray51_ = Js([None])
        PyJsLvalArray52_ = Js([None])
        PyJsLvalObject94_ = Js({u'params':PyJsLvalArray51_,u'defaultCount':Js(0),u'defaults':PyJsLvalArray52_,u'firstRestricted':var.get(u'firstRestricted')})
        var.put(u'options', PyJsLvalObject94_)
        var.get(u'expect')(Js(u'('))
        if var.get(u'match')(Js(u')')).neg():
            PyJsLvalObject95_ = Js({})
            var.get(u'options').put(u'paramSet', PyJsLvalObject95_)
            while (var.get(u'index')<var.get(u'length')):
                if var.get(u'parseParam')(var.get(u'options')).neg():
                    break
                    pass
                var.get(u'expect')(Js(u','))
                pass
            pass
        var.get(u'expect')(Js(u')'))
        if PyJsStrictEq(var.get(u'options').get(u'defaultCount'),Js(0)):
            PyJsLvalArray31_ = Js([None])
            var.get(u'options').put(u'defaults', PyJsLvalArray31_)
            pass
        PyJsLvalObject96_ = Js({u'params':var.get(u'options').get(u'params'),u'defaults':var.get(u'options').get(u'defaults'),u'stricted':var.get(u'options').get(u'stricted'),u'firstRestricted':var.get(u'options').get(u'firstRestricted'),u'message':var.get(u'options').get(u'message')})
        return PyJsLvalObject96_
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseParams'
    var.put(u'parseParams', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(node, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'node':node}, var)
        var.registers([u'expr'])
        var.put(u'expr', var.get(u'parseExpression')())
        var.get(u'consumeSemicolon')()
        return var.get(u'node').callprop(u'finishExpressionStatement',var.get(u'expr'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseExpressionStatement'
    var.put(u'parseExpressionStatement', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'prevToken', u'checkToken'])
        pass
        var.put(u'prevToken', var.get(u'extra').get(u'tokens').get((var.get(u'extra').get(u'tokens').get(u'length')-Js(1))))
        if var.get(u'prevToken').neg():
            return var.get(u'collectRegex')()
            pass
        if PyJsStrictEq(var.get(u'prevToken').get(u'type'),Js(u'Punctuator')):
            if PyJsStrictEq(var.get(u'prevToken').get(u'value'),Js(u']')):
                return var.get(u'scanPunctuator')()
                pass
            if PyJsStrictEq(var.get(u'prevToken').get(u'value'),Js(u')')):
                var.put(u'checkToken', var.get(u'extra').get(u'tokens').get((var.get(u'extra').get(u'openParenToken')-Js(1))))
                if ((var.get(u'checkToken') and PyJsStrictEq(var.get(u'checkToken').get(u'type'),Js(u'Keyword'))) and ((((PyJsStrictEq(var.get(u'checkToken').get(u'value'),Js(u'if')) or PyJsStrictEq(var.get(u'checkToken').get(u'value'),Js(u'while'))) or PyJsStrictEq(var.get(u'checkToken').get(u'value'),Js(u'for'))) or PyJsStrictEq(var.get(u'checkToken').get(u'value'),Js(u'with'))))):
                    return var.get(u'collectRegex')()
                    pass
                return var.get(u'scanPunctuator')()
                pass
            if PyJsStrictEq(var.get(u'prevToken').get(u'value'),Js(u'}')):
                if (var.get(u'extra').get(u'tokens').get((var.get(u'extra').get(u'openCurlyToken')-Js(3))) and PyJsStrictEq(var.get(u'extra').get(u'tokens').get((var.get(u'extra').get(u'openCurlyToken')-Js(3))).get(u'type'),Js(u'Keyword'))):
                    var.put(u'checkToken', var.get(u'extra').get(u'tokens').get((var.get(u'extra').get(u'openCurlyToken')-Js(4))))
                    if var.get(u'checkToken').neg():
                        return var.get(u'scanPunctuator')()
                        pass
                    pass
                elif (var.get(u'extra').get(u'tokens').get((var.get(u'extra').get(u'openCurlyToken')-Js(4))) and PyJsStrictEq(var.get(u'extra').get(u'tokens').get((var.get(u'extra').get(u'openCurlyToken')-Js(4))).get(u'type'),Js(u'Keyword'))):
                    var.put(u'checkToken', var.get(u'extra').get(u'tokens').get((var.get(u'extra').get(u'openCurlyToken')-Js(5))))
                    if var.get(u'checkToken').neg():
                        return var.get(u'collectRegex')()
                        pass
                    pass
                else:
                    return var.get(u'scanPunctuator')()
                    pass
                if (var.get(u'FnExprTokens').callprop(u'indexOf',var.get(u'checkToken').get(u'value'))>=Js(0)):
                    return var.get(u'scanPunctuator')()
                    pass
                return var.get(u'collectRegex')()
                pass
            return var.get(u'collectRegex')()
            pass
        if PyJsStrictEq(var.get(u'prevToken').get(u'type'),Js(u'Keyword')):
            return var.get(u'collectRegex')()
            pass
        return var.get(u'scanPunctuator')()
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'advanceSlash'
    var.put(u'advanceSlash', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'sourceElement', u'sourceElements', u'token', u'directive', u'firstRestricted'])
        PyJsLvalArray36_ = Js([None])
        var.put(u'sourceElements', PyJsLvalArray36_)
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'token', var.get(u'lookahead'))
            if PyJsStrictNeq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'StringLiteral')):
                break
                pass
            var.put(u'sourceElement', var.get(u'parseSourceElement')())
            var.get(u'sourceElements').callprop(u'push',var.get(u'sourceElement'))
            if PyJsStrictNeq(var.get(u'sourceElement').get(u'expression').get(u'type'),var.get(u'Syntax').get(u'Literal')):
                break
                pass
            var.put(u'directive', var.get(u'source').callprop(u'slice',(var.get(u'token').get(u'start')+Js(1)),(var.get(u'token').get(u'end')-Js(1))))
            if PyJsStrictEq(var.get(u'directive'),Js(u'use strict')):
                var.put(u'strict', var.get(u'true'))
                if var.get(u'firstRestricted'):
                    var.get(u'throwErrorTolerant')(var.get(u'firstRestricted'),var.get(u'Messages').get(u'StrictOctalLiteral'))
                    pass
                pass
            else:
                if (var.get(u'firstRestricted').neg() and var.get(u'token').get(u'octal')):
                    var.put(u'firstRestricted', var.get(u'token'))
                    pass
                pass
            pass
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'sourceElement', var.get(u'parseSourceElement')())
            if PyJsStrictEq(var.get(u'sourceElement',throw=False).typeof(),Js(u'undefined')):
                break
                pass
            var.get(u'sourceElements').callprop(u'push',var.get(u'sourceElement'))
            pass
        return var.get(u'sourceElements')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseSourceElements'
    var.put(u'parseSourceElements', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(node, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'node':node}, var)
        var.registers([u'test', u'consequent', u'alternate'])
        pass
        var.get(u'expectKeyword')(Js(u'if'))
        var.get(u'expect')(Js(u'('))
        var.put(u'test', var.get(u'parseExpression')())
        var.get(u'expect')(Js(u')'))
        var.put(u'consequent', var.get(u'parseStatement')())
        if var.get(u'matchKeyword')(Js(u'else')):
            var.get(u'lex')()
            var.put(u'alternate', var.get(u'parseStatement')())
            pass
        else:
            var.put(u'alternate', var.get(u'null'))
            pass
        return var.get(u'node').callprop(u'finishIfStatement',var.get(u'test'),var.get(u'consequent'),var.get(u'alternate'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseIfStatement'
    var.put(u'parseIfStatement', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(startToken, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'startToken':startToken}, var)
        if PyJsStrictEq(var.get(u'startToken').get(u'type'),var.get(u'Token').get(u'StringLiteral')):
            PyJsLvalObject60_ = Js({u'line':var.get(u'startToken').get(u'startLineNumber'),u'column':(var.get(u'startToken').get(u'start')-var.get(u'startToken').get(u'startLineStart'))})
            var.get(u'this').put(u'start', PyJsLvalObject60_)
            pass
        else:
            PyJsLvalObject61_ = Js({u'line':var.get(u'startToken').get(u'lineNumber'),u'column':(var.get(u'startToken').get(u'start')-var.get(u'startToken').get(u'lineStart'))})
            var.get(u'this').put(u'start', PyJsLvalObject61_)
            pass
        var.get(u'this').put(u'end', var.get(u'null'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'WrappingSourceLocation'
    var.put(u'WrappingSourceLocation', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'str', u'quote', u'start', u'ch', u'code', u'unescaped', u'restore', u'octal', u'startLineNumber', u'startLineStart'])
        var.put(u'str', Js(u''))
        var.put(u'octal', var.get(u'false'))
        var.put(u'startLineNumber', var.get(u'lineNumber'))
        var.put(u'startLineStart', var.get(u'lineStart'))
        var.put(u'quote', var.get(u'source').get(var.get(u'index')))
        var.get(u'assert')(((PyJsStrictEq(var.get(u'quote'),Js(u'\'')) or PyJsStrictEq(var.get(u'quote'),Js(u'"')))),Js(u'String literal must starts with a quote'))
        var.put(u'start', var.get(u'index'))
        var.get(u'index').PreInc()
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').get(var.get(u'index').PostInc()))
            if PyJsStrictEq(var.get(u'ch'),var.get(u'quote')):
                var.put(u'quote', Js(u''))
                break
                pass
            elif PyJsStrictEq(var.get(u'ch'),Js(u'\\')):
                var.put(u'ch', var.get(u'source').get(var.get(u'index').PostInc()))
                if (var.get(u'ch').neg() or var.get(u'isLineTerminator')(var.get(u'ch').callprop(u'charCodeAt',Js(0))).neg()):
                    while 1:
                        SWITCHED = False
                        CONDITION = ((var.get(u'ch')))
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(u'u')):
                            SWITCHED = True
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(u'x')):
                            if PyJsStrictEq(var.get(u'source').get(var.get(u'index')),Js(u'{')):
                                var.get(u'index').PreInc()
                                var.put(u'str', var.get(u'scanUnicodeCodePointEscape')(),u'+')
                                pass
                            else:
                                var.put(u'restore', var.get(u'index'))
                                var.put(u'unescaped', var.get(u'scanHexEscape')(var.get(u'ch')))
                                if var.get(u'unescaped'):
                                    var.put(u'str', var.get(u'unescaped'),u'+')
                                    pass
                                else:
                                    var.put(u'index', var.get(u'restore'))
                                    var.put(u'str', var.get(u'ch'),u'+')
                                    pass
                                pass
                            break
                            SWITCHED = True
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(u'n')):
                            var.put(u'str', Js(u'\n'),u'+')
                            break
                            SWITCHED = True
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(u'r')):
                            var.put(u'str', Js(u'\r'),u'+')
                            break
                            SWITCHED = True
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(u't')):
                            var.put(u'str', Js(u'\t'),u'+')
                            break
                            SWITCHED = True
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(u'b')):
                            var.put(u'str', Js(u'\b'),u'+')
                            break
                            SWITCHED = True
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(u'f')):
                            var.put(u'str', Js(u'\f'),u'+')
                            break
                            SWITCHED = True
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(u'v')):
                            var.put(u'str', Js(u'\x0B'),u'+')
                            break
                            SWITCHED = True
                        if True:
                            if var.get(u'isOctalDigit')(var.get(u'ch')):
                                var.put(u'code', Js(u'01234567').callprop(u'indexOf',var.get(u'ch')))
                                if PyJsStrictNeq(var.get(u'code'),Js(0)):
                                    var.put(u'octal', var.get(u'true'))
                                    pass
                                if ((var.get(u'index')<var.get(u'length')) and var.get(u'isOctalDigit')(var.get(u'source').get(var.get(u'index')))):
                                    var.put(u'octal', var.get(u'true'))
                                    var.put(u'code', ((var.get(u'code')*Js(8))+Js(u'01234567').callprop(u'indexOf',var.get(u'source').get(var.get(u'index').PostInc()))))
                                    if (((Js(u'0123').callprop(u'indexOf',var.get(u'ch'))>=Js(0)) and (var.get(u'index')<var.get(u'length'))) and var.get(u'isOctalDigit')(var.get(u'source').get(var.get(u'index')))):
                                        var.put(u'code', ((var.get(u'code')*Js(8))+Js(u'01234567').callprop(u'indexOf',var.get(u'source').get(var.get(u'index').PostInc()))))
                                        pass
                                    pass
                                var.put(u'str', var.get(u'String').callprop(u'fromCharCode',var.get(u'code')),u'+')
                                pass
                            else:
                                var.put(u'str', var.get(u'ch'),u'+')
                                pass
                            break
                            pass
                            SWITCHED = True
                        break
                    pass
                else:
                    var.get(u'lineNumber').PreInc()
                    if (PyJsStrictEq(var.get(u'ch'),Js(u'\r')) and PyJsStrictEq(var.get(u'source').get(var.get(u'index')),Js(u'\n'))):
                        var.get(u'index').PreInc()
                        pass
                    var.put(u'lineStart', var.get(u'index'))
                    pass
                pass
            elif var.get(u'isLineTerminator')(var.get(u'ch').callprop(u'charCodeAt',Js(0))):
                break
                pass
            else:
                var.put(u'str', var.get(u'ch'),u'+')
                pass
            pass
        if PyJsStrictNeq(var.get(u'quote'),Js(u'')):
            PyJsLvalObject41_ = Js({})
            var.get(u'throwError')(PyJsLvalObject41_,var.get(u'Messages').get(u'UnexpectedToken'),Js(u'ILLEGAL'))
            pass
        PyJsLvalObject42_ = Js({u'type':var.get(u'Token').get(u'StringLiteral'),u'value':var.get(u'str'),u'octal':var.get(u'octal'),u'startLineNumber':var.get(u'startLineNumber'),u'startLineStart':var.get(u'startLineStart'),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
        return PyJsLvalObject42_
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'scanStringLiteral'
    var.put(u'scanStringLiteral', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(node, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'node':node}, var)
        var.registers([u'argument'])
        pass
        var.get(u'expectKeyword')(Js(u'throw'))
        if var.get(u'peekLineTerminator')():
            PyJsLvalObject89_ = Js({})
            var.get(u'throwError')(PyJsLvalObject89_,var.get(u'Messages').get(u'NewlineAfterThrow'))
            pass
        var.put(u'argument', var.get(u'parseExpression')())
        var.get(u'consumeSemicolon')()
        return var.get(u'node').callprop(u'finishThrowStatement',var.get(u'argument'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseThrowStatement'
    var.put(u'parseThrowStatement', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(type, value, start, end, loc, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'type':type, u'value':value, u'start':start, u'end':end, u'loc':loc}, var)
        var.registers([u'comment'])
        pass
        var.get(u'assert')(PyJsStrictEq(var.get(u'start',throw=False).typeof(),Js(u'number')),Js(u'Comment must have valid position'))
        if (var.get(u'state').get(u'lastCommentStart')>=var.get(u'start')):
            return var.get('undefined')
            pass
        var.get(u'state').put(u'lastCommentStart', var.get(u'start'))
        PyJsLvalObject9_ = Js({u'type':var.get(u'type'),u'value':var.get(u'value')})
        var.put(u'comment', PyJsLvalObject9_)
        if var.get(u'extra').get(u'range'):
            PyJsLvalArray4_ = Js([var.get(u'start'),var.get(u'end')])
            var.get(u'comment').put(u'range', PyJsLvalArray4_)
            pass
        if var.get(u'extra').get(u'loc'):
            var.get(u'comment').put(u'loc', var.get(u'loc'))
            pass
        var.get(u'extra').get(u'comments').callprop(u'push',var.get(u'comment'))
        if var.get(u'extra').get(u'attachComment'):
            var.get(u'extra').get(u'leadingComments').callprop(u'push',var.get(u'comment'))
            var.get(u'extra').get(u'trailingComments').callprop(u'push',var.get(u'comment'))
            pass
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'addComment'
    var.put(u'addComment', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(node, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'node':node}, var)
        var.registers([u'discriminant', u'cases', u'clause', u'oldInSwitch', u'defaultFound'])
        pass
        var.get(u'expectKeyword')(Js(u'switch'))
        var.get(u'expect')(Js(u'('))
        var.put(u'discriminant', var.get(u'parseExpression')())
        var.get(u'expect')(Js(u')'))
        var.get(u'expect')(Js(u'{'))
        PyJsLvalArray27_ = Js([None])
        var.put(u'cases', PyJsLvalArray27_)
        if var.get(u'match')(Js(u'}')):
            var.get(u'lex')()
            return var.get(u'node').callprop(u'finishSwitchStatement',var.get(u'discriminant'),var.get(u'cases'))
            pass
        var.put(u'oldInSwitch', var.get(u'state').get(u'inSwitch'))
        var.get(u'state').put(u'inSwitch', var.get(u'true'))
        var.put(u'defaultFound', var.get(u'false'))
        while (var.get(u'index')<var.get(u'length')):
            if var.get(u'match')(Js(u'}')):
                break
                pass
            var.put(u'clause', var.get(u'parseSwitchCase')())
            if PyJsStrictEq(var.get(u'clause').get(u'test'),var.get(u'null')):
                if var.get(u'defaultFound'):
                    PyJsLvalObject88_ = Js({})
                    var.get(u'throwError')(PyJsLvalObject88_,var.get(u'Messages').get(u'MultipleDefaultsInSwitch'))
                    pass
                var.put(u'defaultFound', var.get(u'true'))
                pass
            var.get(u'cases').callprop(u'push',var.get(u'clause'))
            pass
        var.get(u'state').put(u'inSwitch', var.get(u'oldInSwitch'))
        var.get(u'expect')(Js(u'}'))
        return var.get(u'node').callprop(u'finishSwitchStatement',var.get(u'discriminant'),var.get(u'cases'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseSwitchStatement'
    var.put(u'parseSwitchStatement', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(value, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'value':value}, var)
        return (PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Punctuator')) and PyJsStrictEq(var.get(u'lookahead').get(u'value'),var.get(u'value')))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'match'
    var.put(u'match', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'node'])
        var.put(u'node', var.get(u'Node').create())
        var.get(u'expect')(Js(u';'))
        return var.get(u'node').callprop(u'finishEmptyStatement')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseEmptyStatement'
    var.put(u'parseEmptyStatement', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'expr', u'previousAllowIn', u'consequent', u'alternate', u'startToken'])
        pass
        var.put(u'startToken', var.get(u'lookahead'))
        var.put(u'expr', var.get(u'parseBinaryExpression')())
        if PyJsStrictEq(var.get(u'expr'),var.get(u'PlaceHolders').get(u'ArrowParameterPlaceHolder')):
            return var.get(u'expr')
            pass
        if var.get(u'match')(Js(u'?')):
            var.get(u'lex')()
            var.put(u'previousAllowIn', var.get(u'state').get(u'allowIn'))
            var.get(u'state').put(u'allowIn', var.get(u'true'))
            var.put(u'consequent', var.get(u'parseAssignmentExpression')())
            var.get(u'state').put(u'allowIn', var.get(u'previousAllowIn'))
            var.get(u'expect')(Js(u':'))
            var.put(u'alternate', var.get(u'parseAssignmentExpression')())
            var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishConditionalExpression',var.get(u'expr'),var.get(u'consequent'),var.get(u'alternate')))
            pass
        return var.get(u'expr')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseConditionalExpression'
    var.put(u'parseConditionalExpression', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(kind, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'kind':kind}, var)
        var.registers([u'init', u'id', u'node'])
        var.put(u'init', var.get(u'null'))
        var.put(u'node', var.get(u'Node').create())
        var.put(u'id', var.get(u'parseVariableIdentifier')())
        if (var.get(u'strict') and var.get(u'isRestrictedWord')(var.get(u'id').get(u'name'))):
            PyJsLvalObject76_ = Js({})
            var.get(u'throwErrorTolerant')(PyJsLvalObject76_,var.get(u'Messages').get(u'StrictVarName'))
            pass
        if PyJsStrictEq(var.get(u'kind'),Js(u'const')):
            var.get(u'expect')(Js(u'='))
            var.put(u'init', var.get(u'parseAssignmentExpression')())
            pass
        elif var.get(u'match')(Js(u'=')):
            var.get(u'lex')()
            var.put(u'init', var.get(u'parseAssignmentExpression')())
            pass
        return var.get(u'node').callprop(u'finishVariableDeclarator',var.get(u'id'),var.get(u'init'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseVariableDeclaration'
    var.put(u'parseVariableDeclaration', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.get(u'this').put(u'line', var.get(u'lineNumber'))
        var.get(u'this').put(u'column', (var.get(u'index')-var.get(u'lineStart')))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'Position'
    var.put(u'Position', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(ch, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'ch':ch}, var)
        PyJsLvalArray3_ = Js([Js(0x1680),Js(0x180E),Js(0x2000),Js(0x2001),Js(0x2002),Js(0x2003),Js(0x2004),Js(0x2005),Js(0x2006),Js(0x2007),Js(0x2008),Js(0x2009),Js(0x200A),Js(0x202F),Js(0x205F),Js(0x3000),Js(0xFEFF)])
        return ((((((PyJsStrictEq(var.get(u'ch'),Js(0x20))) or (PyJsStrictEq(var.get(u'ch'),Js(0x09)))) or (PyJsStrictEq(var.get(u'ch'),Js(0x0B)))) or (PyJsStrictEq(var.get(u'ch'),Js(0x0C)))) or (PyJsStrictEq(var.get(u'ch'),Js(0xA0)))) or (((var.get(u'ch')>=Js(0x1680)) and (PyJsLvalArray3_.callprop(u'indexOf',var.get(u'ch'))>=Js(0)))))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'isWhiteSpace'
    var.put(u'isWhiteSpace', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(node, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'node':node}, var)
        var.registers([u'test', u'body', u'oldInIteration'])
        pass
        var.get(u'expectKeyword')(Js(u'while'))
        var.get(u'expect')(Js(u'('))
        var.put(u'test', var.get(u'parseExpression')())
        var.get(u'expect')(Js(u')'))
        var.put(u'oldInIteration', var.get(u'state').get(u'inIteration'))
        var.get(u'state').put(u'inIteration', var.get(u'true'))
        var.put(u'body', var.get(u'parseStatement')())
        var.get(u'state').put(u'inIteration', var.get(u'oldInIteration'))
        return var.get(u'node').callprop(u'finishWhileStatement',var.get(u'test'),var.get(u'body'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseWhileStatement'
    var.put(u'parseWhileStatement', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(options, param, name, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'options':options, u'param':param, u'name':name}, var)
        var.registers([u'key'])
        var.put(u'key', (Js(u'$')+var.get(u'name')))
        if var.get(u'strict'):
            if var.get(u'isRestrictedWord')(var.get(u'name')):
                var.get(u'options').put(u'stricted', var.get(u'param'))
                var.get(u'options').put(u'message', var.get(u'Messages').get(u'StrictParamName'))
                pass
            if var.get(u'Object').get(u'prototype').get(u'hasOwnProperty').callprop(u'call',var.get(u'options').get(u'paramSet'),var.get(u'key')):
                var.get(u'options').put(u'stricted', var.get(u'param'))
                var.get(u'options').put(u'message', var.get(u'Messages').get(u'StrictParamDupe'))
                pass
            pass
        elif var.get(u'options').get(u'firstRestricted').neg():
            if var.get(u'isRestrictedWord')(var.get(u'name')):
                var.get(u'options').put(u'firstRestricted', var.get(u'param'))
                var.get(u'options').put(u'message', var.get(u'Messages').get(u'StrictParamName'))
                pass
            elif var.get(u'isStrictModeReservedWord')(var.get(u'name')):
                var.get(u'options').put(u'firstRestricted', var.get(u'param'))
                var.get(u'options').put(u'message', var.get(u'Messages').get(u'StrictReservedWord'))
                pass
            elif var.get(u'Object').get(u'prototype').get(u'hasOwnProperty').callprop(u'call',var.get(u'options').get(u'paramSet'),var.get(u'key')):
                var.get(u'options').put(u'firstRestricted', var.get(u'param'))
                var.get(u'options').put(u'message', var.get(u'Messages').get(u'StrictParamDupe'))
                pass
            pass
        var.get(u'options').get(u'paramSet').put(var.get(u'key'), var.get(u'true'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'validateParam'
    var.put(u'validateParam', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'expr'])
        pass
        var.get(u'expect')(Js(u'('))
        if var.get(u'match')(Js(u')')):
            var.get(u'lex')()
            return var.get(u'PlaceHolders').get(u'ArrowParameterPlaceHolder')
            pass
        var.get(u'state').get(u'parenthesisCount').PreInc()
        var.put(u'expr', var.get(u'parseExpression')())
        var.get(u'expect')(Js(u')'))
        return var.get(u'expr')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseGroupExpression'
    var.put(u'parseGroupExpression', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(start, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'start':start}, var)
        var.registers([u'number'])
        var.put(u'number', Js(u''))
        while (var.get(u'index')<var.get(u'length')):
            if var.get(u'isHexDigit')(var.get(u'source').get(var.get(u'index'))).neg():
                break
                pass
            var.put(u'number', var.get(u'source').get(var.get(u'index').PostInc()),u'+')
            pass
        if PyJsStrictEq(var.get(u'number').get(u'length'),Js(0)):
            PyJsLvalObject32_ = Js({})
            var.get(u'throwError')(PyJsLvalObject32_,var.get(u'Messages').get(u'UnexpectedToken'),Js(u'ILLEGAL'))
            pass
        if var.get(u'isIdentifierStart')(var.get(u'source').callprop(u'charCodeAt',var.get(u'index'))):
            PyJsLvalObject33_ = Js({})
            var.get(u'throwError')(PyJsLvalObject33_,var.get(u'Messages').get(u'UnexpectedToken'),Js(u'ILLEGAL'))
            pass
        PyJsLvalObject34_ = Js({u'type':var.get(u'Token').get(u'NumericLiteral'),u'value':var.get(u'parseInt')((Js(u'0x')+var.get(u'number')),Js(16)),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
        return PyJsLvalObject34_
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'scanHexLiteral'
    var.put(u'scanHexLiteral', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(node, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'node':node}, var)
        var.registers([u'label', u'key'])
        var.put(u'label', var.get(u'null'))
        var.get(u'expectKeyword')(Js(u'break'))
        if PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt',var.get(u'index')),Js(0x3B)):
            var.get(u'lex')()
            if ((var.get(u'state').get(u'inIteration') or var.get(u'state').get(u'inSwitch'))).neg():
                PyJsLvalObject82_ = Js({})
                var.get(u'throwError')(PyJsLvalObject82_,var.get(u'Messages').get(u'IllegalBreak'))
                pass
            return var.get(u'node').callprop(u'finishBreakStatement',var.get(u'null'))
            pass
        if var.get(u'peekLineTerminator')():
            if ((var.get(u'state').get(u'inIteration') or var.get(u'state').get(u'inSwitch'))).neg():
                PyJsLvalObject83_ = Js({})
                var.get(u'throwError')(PyJsLvalObject83_,var.get(u'Messages').get(u'IllegalBreak'))
                pass
            return var.get(u'node').callprop(u'finishBreakStatement',var.get(u'null'))
            pass
        if PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Identifier')):
            var.put(u'label', var.get(u'parseVariableIdentifier')())
            var.put(u'key', (Js(u'$')+var.get(u'label').get(u'name')))
            if var.get(u'Object').get(u'prototype').get(u'hasOwnProperty').callprop(u'call',var.get(u'state').get(u'labelSet'),var.get(u'key')).neg():
                PyJsLvalObject84_ = Js({})
                var.get(u'throwError')(PyJsLvalObject84_,var.get(u'Messages').get(u'UnknownLabel'),var.get(u'label').get(u'name'))
                pass
            pass
        var.get(u'consumeSemicolon')()
        if (PyJsStrictEq(var.get(u'label'),var.get(u'null')) and ((var.get(u'state').get(u'inIteration') or var.get(u'state').get(u'inSwitch'))).neg()):
            PyJsLvalObject85_ = Js({})
            var.get(u'throwError')(PyJsLvalObject85_,var.get(u'Messages').get(u'IllegalBreak'))
            pass
        return var.get(u'node').callprop(u'finishBreakStatement',var.get(u'label'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseBreakStatement'
    var.put(u'parseBreakStatement', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'ch', u'id'])
        pass
        var.put(u'ch', var.get(u'source').callprop(u'charCodeAt',var.get(u'index').PostInc()))
        var.put(u'id', var.get(u'String').callprop(u'fromCharCode',var.get(u'ch')))
        if PyJsStrictEq(var.get(u'ch'),Js(0x5C)):
            if PyJsStrictNeq(var.get(u'source').callprop(u'charCodeAt',var.get(u'index')),Js(0x75)):
                PyJsLvalObject19_ = Js({})
                var.get(u'throwError')(PyJsLvalObject19_,var.get(u'Messages').get(u'UnexpectedToken'),Js(u'ILLEGAL'))
                pass
            var.get(u'index').PreInc()
            var.put(u'ch', var.get(u'scanHexEscape')(Js(u'u')))
            if ((var.get(u'ch').neg() or PyJsStrictEq(var.get(u'ch'),Js(u'\\'))) or var.get(u'isIdentifierStart')(var.get(u'ch').callprop(u'charCodeAt',Js(0))).neg()):
                PyJsLvalObject20_ = Js({})
                var.get(u'throwError')(PyJsLvalObject20_,var.get(u'Messages').get(u'UnexpectedToken'),Js(u'ILLEGAL'))
                pass
            var.put(u'id', var.get(u'ch'))
            pass
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').callprop(u'charCodeAt',var.get(u'index')))
            if var.get(u'isIdentifierPart')(var.get(u'ch')).neg():
                break
                pass
            var.get(u'index').PreInc()
            var.put(u'id', var.get(u'String').callprop(u'fromCharCode',var.get(u'ch')),u'+')
            if PyJsStrictEq(var.get(u'ch'),Js(0x5C)):
                var.put(u'id', var.get(u'id').callprop(u'substr',Js(0),(var.get(u'id').get(u'length')-Js(1))))
                if PyJsStrictNeq(var.get(u'source').callprop(u'charCodeAt',var.get(u'index')),Js(0x75)):
                    PyJsLvalObject21_ = Js({})
                    var.get(u'throwError')(PyJsLvalObject21_,var.get(u'Messages').get(u'UnexpectedToken'),Js(u'ILLEGAL'))
                    pass
                var.get(u'index').PreInc()
                var.put(u'ch', var.get(u'scanHexEscape')(Js(u'u')))
                if ((var.get(u'ch').neg() or PyJsStrictEq(var.get(u'ch'),Js(u'\\'))) or var.get(u'isIdentifierPart')(var.get(u'ch').callprop(u'charCodeAt',Js(0))).neg()):
                    PyJsLvalObject22_ = Js({})
                    var.get(u'throwError')(PyJsLvalObject22_,var.get(u'Messages').get(u'UnexpectedToken'),Js(u'ILLEGAL'))
                    pass
                var.put(u'id', var.get(u'ch'),u'+')
                pass
            pass
        return var.get(u'id')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'getEscapedIdentifier'
    var.put(u'getEscapedIdentifier', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.get(u'this').put(u'start', var.get(u'Position').create())
        var.get(u'this').put(u'end', var.get(u'null'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'SourceLocation'
    var.put(u'SourceLocation', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'type', u'token', u'expr', u'node'])
        pass
        if var.get(u'match')(Js(u'(')):
            return var.get(u'parseGroupExpression')()
            pass
        if var.get(u'match')(Js(u'[')):
            return var.get(u'parseArrayInitialiser')()
            pass
        if var.get(u'match')(Js(u'{')):
            return var.get(u'parseObjectInitialiser')()
            pass
        var.put(u'type', var.get(u'lookahead').get(u'type'))
        var.put(u'node', var.get(u'Node').create())
        if PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'Identifier')):
            var.put(u'expr', var.get(u'node').callprop(u'finishIdentifier',var.get(u'lex')().get(u'value')))
            pass
        elif (PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'StringLiteral')) or PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'NumericLiteral'))):
            if (var.get(u'strict') and var.get(u'lookahead').get(u'octal')):
                var.get(u'throwErrorTolerant')(var.get(u'lookahead'),var.get(u'Messages').get(u'StrictOctalLiteral'))
                pass
            var.put(u'expr', var.get(u'node').callprop(u'finishLiteral',var.get(u'lex')()))
            pass
        elif PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'Keyword')):
            if var.get(u'matchKeyword')(Js(u'function')):
                return var.get(u'parseFunctionExpression')()
                pass
            if var.get(u'matchKeyword')(Js(u'this')):
                var.get(u'lex')()
                var.put(u'expr', var.get(u'node').callprop(u'finishThisExpression'))
                pass
            else:
                var.get(u'throwUnexpected')(var.get(u'lex')())
                pass
            pass
        elif PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'BooleanLiteral')):
            var.put(u'token', var.get(u'lex')())
            var.get(u'token').put(u'value', (PyJsStrictEq(var.get(u'token').get(u'value'),Js(u'true'))))
            var.put(u'expr', var.get(u'node').callprop(u'finishLiteral',var.get(u'token')))
            pass
        elif PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'NullLiteral')):
            var.put(u'token', var.get(u'lex')())
            var.get(u'token').put(u'value', var.get(u'null'))
            var.put(u'expr', var.get(u'node').callprop(u'finishLiteral',var.get(u'token')))
            pass
        elif (var.get(u'match')(Js(u'/')) or var.get(u'match')(Js(u'/='))):
            if PyJsStrictNeq(var.get(u'extra').get(u'tokens').typeof(),Js(u'undefined')):
                var.put(u'expr', var.get(u'node').callprop(u'finishLiteral',var.get(u'collectRegex')()))
                pass
            else:
                var.put(u'expr', var.get(u'node').callprop(u'finishLiteral',var.get(u'scanRegExp')()))
                pass
            var.get(u'peek')()
            pass
        else:
            var.get(u'throwUnexpected')(var.get(u'lex')())
            pass
        return var.get(u'expr')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parsePrimaryExpression'
    var.put(u'parsePrimaryExpression', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'ch', u'str', u'flags', u'restore'])
        pass
        var.put(u'str', Js(u''))
        var.put(u'flags', Js(u''))
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').get(var.get(u'index')))
            if var.get(u'isIdentifierPart')(var.get(u'ch').callprop(u'charCodeAt',Js(0))).neg():
                break
                pass
            var.get(u'index').PreInc()
            if (PyJsStrictEq(var.get(u'ch'),Js(u'\\')) and (var.get(u'index')<var.get(u'length'))):
                var.put(u'ch', var.get(u'source').get(var.get(u'index')))
                if PyJsStrictEq(var.get(u'ch'),Js(u'u')):
                    var.get(u'index').PreInc()
                    var.put(u'restore', var.get(u'index'))
                    var.put(u'ch', var.get(u'scanHexEscape')(Js(u'u')))
                    if var.get(u'ch'):
                        var.put(u'flags', var.get(u'ch'),u'+')
                        #for JS loop
                        var.put(u'str', Js(u'\\u'),u'+')
                        while (var.get(u'restore')<var.get(u'index')):
                            var.put(u'str', var.get(u'source').get(var.get(u'restore')),u'+')
                            pass
                            var.get(u'restore').PreInc()
                        
                        pass
                    else:
                        var.put(u'index', var.get(u'restore'))
                        var.put(u'flags', Js(u'u'),u'+')
                        var.put(u'str', Js(u'\\u'),u'+')
                        pass
                    PyJsLvalObject48_ = Js({})
                    var.get(u'throwErrorTolerant')(PyJsLvalObject48_,var.get(u'Messages').get(u'UnexpectedToken'),Js(u'ILLEGAL'))
                    pass
                else:
                    var.put(u'str', Js(u'\\'),u'+')
                    PyJsLvalObject49_ = Js({})
                    var.get(u'throwErrorTolerant')(PyJsLvalObject49_,var.get(u'Messages').get(u'UnexpectedToken'),Js(u'ILLEGAL'))
                    pass
                pass
            else:
                var.put(u'flags', var.get(u'ch'),u'+')
                var.put(u'str', var.get(u'ch'),u'+')
                pass
            pass
        PyJsLvalObject50_ = Js({u'value':var.get(u'flags'),u'literal':var.get(u'str')})
        return PyJsLvalObject50_
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'scanRegExpFlags'
    var.put(u'scanRegExpFlags', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(kind, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'kind':kind}, var)
        var.registers([u'list'])
        PyJsLvalArray25_ = Js([None])
        var.put(u'list', PyJsLvalArray25_)
        while 1:
            var.get(u'list').callprop(u'push',var.get(u'parseVariableDeclaration')(var.get(u'kind')))
            if var.get(u'match')(Js(u',')).neg():
                break
                pass
            var.get(u'lex')()
            pass
            if not (var.get(u'index')<var.get(u'length')):
                break
        pass
        return var.get(u'list')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseVariableDeclarationList'
    var.put(u'parseVariableDeclarationList', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'token', u'id', u'stricted', u'firstRestricted', u'message', u'tmp', u'params', u'defaults', u'body', u'previousStrict', u'node'])
        var.put(u'id', var.get(u'null'))
        PyJsLvalArray34_ = Js([None])
        var.put(u'params', PyJsLvalArray34_)
        PyJsLvalArray35_ = Js([None])
        var.put(u'defaults', PyJsLvalArray35_)
        var.put(u'node', var.get(u'Node').create())
        var.get(u'expectKeyword')(Js(u'function'))
        if var.get(u'match')(Js(u'(')).neg():
            var.put(u'token', var.get(u'lookahead'))
            var.put(u'id', var.get(u'parseVariableIdentifier')())
            if var.get(u'strict'):
                if var.get(u'isRestrictedWord')(var.get(u'token').get(u'value')):
                    var.get(u'throwErrorTolerant')(var.get(u'token'),var.get(u'Messages').get(u'StrictFunctionName'))
                    pass
                pass
            else:
                if var.get(u'isRestrictedWord')(var.get(u'token').get(u'value')):
                    var.put(u'firstRestricted', var.get(u'token'))
                    var.put(u'message', var.get(u'Messages').get(u'StrictFunctionName'))
                    pass
                elif var.get(u'isStrictModeReservedWord')(var.get(u'token').get(u'value')):
                    var.put(u'firstRestricted', var.get(u'token'))
                    var.put(u'message', var.get(u'Messages').get(u'StrictReservedWord'))
                    pass
                pass
            pass
        var.put(u'tmp', var.get(u'parseParams')(var.get(u'firstRestricted')))
        var.put(u'params', var.get(u'tmp').get(u'params'))
        var.put(u'defaults', var.get(u'tmp').get(u'defaults'))
        var.put(u'stricted', var.get(u'tmp').get(u'stricted'))
        var.put(u'firstRestricted', var.get(u'tmp').get(u'firstRestricted'))
        if var.get(u'tmp').get(u'message'):
            var.put(u'message', var.get(u'tmp').get(u'message'))
            pass
        var.put(u'previousStrict', var.get(u'strict'))
        var.put(u'body', var.get(u'parseFunctionSourceElements')())
        if (var.get(u'strict') and var.get(u'firstRestricted')):
            var.get(u'throwError')(var.get(u'firstRestricted'),var.get(u'message'))
            pass
        if (var.get(u'strict') and var.get(u'stricted')):
            var.get(u'throwErrorTolerant')(var.get(u'stricted'),var.get(u'message'))
            pass
        var.put(u'strict', var.get(u'previousStrict'))
        return var.get(u'node').callprop(u'finishFunctionExpression',var.get(u'id'),var.get(u'params'),var.get(u'defaults'),var.get(u'body'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseFunctionExpression'
    var.put(u'parseFunctionExpression', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(node, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'node':node}, var)
        var.registers([u'argument'])
        var.put(u'argument', var.get(u'null'))
        var.get(u'expectKeyword')(Js(u'return'))
        if var.get(u'state').get(u'inFunctionBody').neg():
            PyJsLvalObject86_ = Js({})
            var.get(u'throwErrorTolerant')(PyJsLvalObject86_,var.get(u'Messages').get(u'IllegalReturn'))
            pass
        if PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt',var.get(u'index')),Js(0x20)):
            if var.get(u'isIdentifierStart')(var.get(u'source').callprop(u'charCodeAt',(var.get(u'index')+Js(1)))):
                var.put(u'argument', var.get(u'parseExpression')())
                var.get(u'consumeSemicolon')()
                return var.get(u'node').callprop(u'finishReturnStatement',var.get(u'argument'))
                pass
            pass
        if var.get(u'peekLineTerminator')():
            return var.get(u'node').callprop(u'finishReturnStatement',var.get(u'null'))
            pass
        if var.get(u'match')(Js(u';')).neg():
            if (var.get(u'match')(Js(u'}')).neg() and PyJsStrictNeq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'EOF'))):
                var.put(u'argument', var.get(u'parseExpression')())
                pass
            pass
        var.get(u'consumeSemicolon')()
        return var.get(u'node').callprop(u'finishReturnStatement',var.get(u'argument'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseReturnStatement'
    var.put(u'parseReturnStatement', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'token', u'expr', u'startToken'])
        pass
        if (PyJsStrictNeq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Punctuator')) and PyJsStrictNeq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Keyword'))):
            var.put(u'expr', var.get(u'parsePostfixExpression')())
            pass
        elif (var.get(u'match')(Js(u'++')) or var.get(u'match')(Js(u'--'))):
            var.put(u'startToken', var.get(u'lookahead'))
            var.put(u'token', var.get(u'lex')())
            var.put(u'expr', var.get(u'parseUnaryExpression')())
            if ((var.get(u'strict') and PyJsStrictEq(var.get(u'expr').get(u'type'),var.get(u'Syntax').get(u'Identifier'))) and var.get(u'isRestrictedWord')(var.get(u'expr').get(u'name'))):
                PyJsLvalObject70_ = Js({})
                var.get(u'throwErrorTolerant')(PyJsLvalObject70_,var.get(u'Messages').get(u'StrictLHSPrefix'))
                pass
            if var.get(u'isLeftHandSide')(var.get(u'expr')).neg():
                PyJsLvalObject71_ = Js({})
                var.get(u'throwErrorTolerant')(PyJsLvalObject71_,var.get(u'Messages').get(u'InvalidLHSInAssignment'))
                pass
            var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishUnaryExpression',var.get(u'token').get(u'value'),var.get(u'expr')))
            pass
        elif (((var.get(u'match')(Js(u'+')) or var.get(u'match')(Js(u'-'))) or var.get(u'match')(Js(u'~'))) or var.get(u'match')(Js(u'!'))):
            var.put(u'startToken', var.get(u'lookahead'))
            var.put(u'token', var.get(u'lex')())
            var.put(u'expr', var.get(u'parseUnaryExpression')())
            var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishUnaryExpression',var.get(u'token').get(u'value'),var.get(u'expr')))
            pass
        elif ((var.get(u'matchKeyword')(Js(u'delete')) or var.get(u'matchKeyword')(Js(u'void'))) or var.get(u'matchKeyword')(Js(u'typeof'))):
            var.put(u'startToken', var.get(u'lookahead'))
            var.put(u'token', var.get(u'lex')())
            var.put(u'expr', var.get(u'parseUnaryExpression')())
            var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishUnaryExpression',var.get(u'token').get(u'value'),var.get(u'expr')))
            if ((var.get(u'strict') and PyJsStrictEq(var.get(u'expr').get(u'operator'),Js(u'delete'))) and PyJsStrictEq(var.get(u'expr').get(u'argument').get(u'type'),var.get(u'Syntax').get(u'Identifier'))):
                PyJsLvalObject72_ = Js({})
                var.get(u'throwErrorTolerant')(PyJsLvalObject72_,var.get(u'Messages').get(u'StrictDelete'))
                pass
            pass
        else:
            var.put(u'expr', var.get(u'parsePostfixExpression')())
            pass
        return var.get(u'expr')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseUnaryExpression'
    var.put(u'parseUnaryExpression', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'pos', u'loc', u'regex', u'token'])
        pass
        var.get(u'skipComment')()
        var.put(u'pos', var.get(u'index'))
        PyJsLvalObject110_ = Js({u'line':var.get(u'lineNumber'),u'column':(var.get(u'index')-var.get(u'lineStart'))})
        PyJsLvalObject53_ = Js({u'start':PyJsLvalObject110_})
        var.put(u'loc', PyJsLvalObject53_)
        var.put(u'regex', var.get(u'scanRegExp')())
        PyJsLvalObject54_ = Js({u'line':var.get(u'lineNumber'),u'column':(var.get(u'index')-var.get(u'lineStart'))})
        var.get(u'loc').put(u'end', PyJsLvalObject54_)
        if var.get(u'extra').get(u'tokenize').neg():
            if (var.get(u'extra').get(u'tokens').get(u'length')>Js(0)):
                var.put(u'token', var.get(u'extra').get(u'tokens').get((var.get(u'extra').get(u'tokens').get(u'length')-Js(1))))
                if (PyJsStrictEq(var.get(u'token').get(u'range').get(Js(0)),var.get(u'pos')) and PyJsStrictEq(var.get(u'token').get(u'type'),Js(u'Punctuator'))):
                    if (PyJsStrictEq(var.get(u'token').get(u'value'),Js(u'/')) or PyJsStrictEq(var.get(u'token').get(u'value'),Js(u'/='))):
                        var.get(u'extra').get(u'tokens').callprop(u'pop')
                        pass
                    pass
                pass
            PyJsLvalArray53_ = Js([var.get(u'pos'),var.get(u'index')])
            PyJsLvalObject55_ = Js({u'type':Js(u'RegularExpression'),u'value':var.get(u'regex').get(u'literal'),u'range':PyJsLvalArray53_,u'loc':var.get(u'loc')})
            var.get(u'extra').get(u'tokens').callprop(u'push',PyJsLvalObject55_)
            pass
        return var.get(u'regex')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'collectRegex'
    var.put(u'collectRegex', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(value, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'value':value}, var)
        var.registers([u'token'])
        var.put(u'token', var.get(u'lex')())
        if (PyJsStrictNeq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Punctuator')) or PyJsStrictNeq(var.get(u'token').get(u'value'),var.get(u'value'))):
            var.get(u'throwUnexpected')(var.get(u'token'))
            pass
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'expect'
    var.put(u'expect', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'start', u'loc', u'ch', u'comment'])
        pass
        if var.get(u'extra').get(u'comments'):
            var.put(u'start', (var.get(u'index')-Js(2)))
            PyJsLvalObject107_ = Js({u'line':var.get(u'lineNumber'),u'column':((var.get(u'index')-var.get(u'lineStart'))-Js(2))})
            PyJsLvalObject13_ = Js({u'start':PyJsLvalObject107_})
            var.put(u'loc', PyJsLvalObject13_)
            pass
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').callprop(u'charCodeAt',var.get(u'index')))
            if var.get(u'isLineTerminator')(var.get(u'ch')):
                if (PyJsStrictEq(var.get(u'ch'),Js(0x0D)) and PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt',(var.get(u'index')+Js(1))),Js(0x0A))):
                    var.get(u'index').PreInc()
                    pass
                var.get(u'lineNumber').PreInc()
                var.get(u'index').PreInc()
                var.put(u'lineStart', var.get(u'index'))
                if (var.get(u'index')>=var.get(u'length')):
                    PyJsLvalObject14_ = Js({})
                    var.get(u'throwError')(PyJsLvalObject14_,var.get(u'Messages').get(u'UnexpectedToken'),Js(u'ILLEGAL'))
                    pass
                pass
            elif PyJsStrictEq(var.get(u'ch'),Js(0x2A)):
                if PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt',(var.get(u'index')+Js(1))),Js(0x2F)):
                    var.get(u'index').PreInc()
                    var.get(u'index').PreInc()
                    if var.get(u'extra').get(u'comments'):
                        var.put(u'comment', var.get(u'source').callprop(u'slice',(var.get(u'start')+Js(2)),(var.get(u'index')-Js(2))))
                        PyJsLvalObject15_ = Js({u'line':var.get(u'lineNumber'),u'column':(var.get(u'index')-var.get(u'lineStart'))})
                        var.get(u'loc').put(u'end', PyJsLvalObject15_)
                        var.get(u'addComment')(Js(u'Block'),var.get(u'comment'),var.get(u'start'),var.get(u'index'),var.get(u'loc'))
                        pass
                    return var.get('undefined')
                    pass
                var.get(u'index').PreInc()
                pass
            else:
                var.get(u'index').PreInc()
                pass
            pass
        PyJsLvalObject16_ = Js({})
        var.get(u'throwError')(PyJsLvalObject16_,var.get(u'Messages').get(u'UnexpectedToken'),Js(u'ILLEGAL'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'skipMultiLineComment'
    var.put(u'skipMultiLineComment', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'number', u'start', u'ch'])
        pass
        var.put(u'ch', var.get(u'source').get(var.get(u'index')))
        var.get(u'assert')((var.get(u'isDecimalDigit')(var.get(u'ch').callprop(u'charCodeAt',Js(0))) or (PyJsStrictEq(var.get(u'ch'),Js(u'.')))),Js(u'Numeric literal must start with a decimal digit or a decimal point'))
        var.put(u'start', var.get(u'index'))
        var.put(u'number', Js(u''))
        if PyJsStrictNeq(var.get(u'ch'),Js(u'.')):
            var.put(u'number', var.get(u'source').get(var.get(u'index').PostInc()))
            var.put(u'ch', var.get(u'source').get(var.get(u'index')))
            if PyJsStrictEq(var.get(u'number'),Js(u'0')):
                if (PyJsStrictEq(var.get(u'ch'),Js(u'x')) or PyJsStrictEq(var.get(u'ch'),Js(u'X'))):
                    var.get(u'index').PreInc()
                    return var.get(u'scanHexLiteral')(var.get(u'start'))
                    pass
                if var.get(u'isOctalDigit')(var.get(u'ch')):
                    return var.get(u'scanOctalLiteral')(var.get(u'start'))
                    pass
                if (var.get(u'ch') and var.get(u'isDecimalDigit')(var.get(u'ch').callprop(u'charCodeAt',Js(0)))):
                    PyJsLvalObject37_ = Js({})
                    var.get(u'throwError')(PyJsLvalObject37_,var.get(u'Messages').get(u'UnexpectedToken'),Js(u'ILLEGAL'))
                    pass
                pass
            while var.get(u'isDecimalDigit')(var.get(u'source').callprop(u'charCodeAt',var.get(u'index'))):
                var.put(u'number', var.get(u'source').get(var.get(u'index').PostInc()),u'+')
                pass
            var.put(u'ch', var.get(u'source').get(var.get(u'index')))
            pass
        if PyJsStrictEq(var.get(u'ch'),Js(u'.')):
            var.put(u'number', var.get(u'source').get(var.get(u'index').PostInc()),u'+')
            while var.get(u'isDecimalDigit')(var.get(u'source').callprop(u'charCodeAt',var.get(u'index'))):
                var.put(u'number', var.get(u'source').get(var.get(u'index').PostInc()),u'+')
                pass
            var.put(u'ch', var.get(u'source').get(var.get(u'index')))
            pass
        if (PyJsStrictEq(var.get(u'ch'),Js(u'e')) or PyJsStrictEq(var.get(u'ch'),Js(u'E'))):
            var.put(u'number', var.get(u'source').get(var.get(u'index').PostInc()),u'+')
            var.put(u'ch', var.get(u'source').get(var.get(u'index')))
            if (PyJsStrictEq(var.get(u'ch'),Js(u'+')) or PyJsStrictEq(var.get(u'ch'),Js(u'-'))):
                var.put(u'number', var.get(u'source').get(var.get(u'index').PostInc()),u'+')
                pass
            if var.get(u'isDecimalDigit')(var.get(u'source').callprop(u'charCodeAt',var.get(u'index'))):
                while var.get(u'isDecimalDigit')(var.get(u'source').callprop(u'charCodeAt',var.get(u'index'))):
                    var.put(u'number', var.get(u'source').get(var.get(u'index').PostInc()),u'+')
                    pass
                pass
            else:
                PyJsLvalObject38_ = Js({})
                var.get(u'throwError')(PyJsLvalObject38_,var.get(u'Messages').get(u'UnexpectedToken'),Js(u'ILLEGAL'))
                pass
            pass
        if var.get(u'isIdentifierStart')(var.get(u'source').callprop(u'charCodeAt',var.get(u'index'))):
            PyJsLvalObject39_ = Js({})
            var.get(u'throwError')(PyJsLvalObject39_,var.get(u'Messages').get(u'UnexpectedToken'),Js(u'ILLEGAL'))
            pass
        PyJsLvalObject40_ = Js({u'type':var.get(u'Token').get(u'NumericLiteral'),u'value':var.get(u'parseFloat')(var.get(u'number')),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
        return PyJsLvalObject40_
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'scanNumericLiteral'
    var.put(u'scanNumericLiteral', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(ch, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'ch':ch}, var)
        return ((((((PyJsStrictEq(var.get(u'ch'),Js(0x24))) or (PyJsStrictEq(var.get(u'ch'),Js(0x5F)))) or (((var.get(u'ch')>=Js(0x41)) and (var.get(u'ch')<=Js(0x5A))))) or (((var.get(u'ch')>=Js(0x61)) and (var.get(u'ch')<=Js(0x7A))))) or (PyJsStrictEq(var.get(u'ch'),Js(0x5C)))) or ((((var.get(u'ch')>=Js(0x80))) and var.get(u'Regex').get(u'NonAsciiIdentifierStart').callprop(u'test',var.get(u'String').callprop(u'fromCharCode',var.get(u'ch'))))))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'isIdentifierStart'
    var.put(u'isIdentifierStart', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(value, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'value':value}, var)
        var.registers([u'token'])
        if var.get(u'extra').get(u'errors'):
            var.put(u'token', var.get(u'lookahead'))
            if (PyJsStrictNeq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Punctuator')) and PyJsStrictNeq(var.get(u'token').get(u'value'),var.get(u'value'))):
                var.get(u'throwErrorTolerant')(var.get(u'token'),var.get(u'Messages').get(u'UnexpectedToken'),var.get(u'token').get(u'value'))
                pass
            else:
                var.get(u'lex')()
                pass
            pass
        else:
            var.get(u'expect')(var.get(u'value'))
            pass
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'expectTolerant'
    var.put(u'expectTolerant', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'body', u'node'])
        pass
        var.get(u'skipComment')()
        var.get(u'peek')()
        var.put(u'node', var.get(u'Node').create())
        var.put(u'strict', var.get(u'false'))
        var.put(u'body', var.get(u'parseSourceElements')())
        return var.get(u'node').callprop(u'finishProgram',var.get(u'body'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseProgram'
    var.put(u'parseProgram', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(ch, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'ch':ch}, var)
        return (Js(u'01234567').callprop(u'indexOf',var.get(u'ch'))>=Js(0))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'isOctalDigit'
    var.put(u'isOctalDigit', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(ch, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'ch':ch}, var)
        return (((var.get(u'ch')>=Js(0x30)) and (var.get(u'ch')<=Js(0x39))))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'isDecimalDigit'
    var.put(u'isDecimalDigit', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'token', u'key', u'id', u'value', u'param', u'node'])
        var.put(u'node', var.get(u'Node').create())
        var.put(u'token', var.get(u'lookahead'))
        if PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Identifier')):
            var.put(u'id', var.get(u'parseObjectPropertyKey')())
            if (PyJsStrictEq(var.get(u'token').get(u'value'),Js(u'get')) and var.get(u'match')(Js(u':')).neg()):
                var.put(u'key', var.get(u'parseObjectPropertyKey')())
                var.get(u'expect')(Js(u'('))
                var.get(u'expect')(Js(u')'))
                PyJsLvalArray9_ = Js([None])
                var.put(u'value', var.get(u'parsePropertyFunction')(PyJsLvalArray9_))
                return var.get(u'node').callprop(u'finishProperty',Js(u'get'),var.get(u'key'),var.get(u'value'))
                pass
            if (PyJsStrictEq(var.get(u'token').get(u'value'),Js(u'set')) and var.get(u'match')(Js(u':')).neg()):
                var.put(u'key', var.get(u'parseObjectPropertyKey')())
                var.get(u'expect')(Js(u'('))
                var.put(u'token', var.get(u'lookahead'))
                if PyJsStrictNeq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Identifier')):
                    var.get(u'expect')(Js(u')'))
                    var.get(u'throwErrorTolerant')(var.get(u'token'),var.get(u'Messages').get(u'UnexpectedToken'),var.get(u'token').get(u'value'))
                    PyJsLvalArray10_ = Js([None])
                    var.put(u'value', var.get(u'parsePropertyFunction')(PyJsLvalArray10_))
                    pass
                else:
                    PyJsLvalArray11_ = Js([var.get(u'parseVariableIdentifier')()])
                    var.put(u'param', PyJsLvalArray11_)
                    var.get(u'expect')(Js(u')'))
                    var.put(u'value', var.get(u'parsePropertyFunction')(var.get(u'param'),var.get(u'token')))
                    pass
                return var.get(u'node').callprop(u'finishProperty',Js(u'set'),var.get(u'key'),var.get(u'value'))
                pass
            var.get(u'expect')(Js(u':'))
            var.put(u'value', var.get(u'parseAssignmentExpression')())
            return var.get(u'node').callprop(u'finishProperty',Js(u'init'),var.get(u'id'),var.get(u'value'))
            pass
        if (PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'EOF')) or PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Punctuator'))):
            var.get(u'throwUnexpected')(var.get(u'token'))
            pass
        else:
            var.put(u'key', var.get(u'parseObjectPropertyKey')())
            var.get(u'expect')(Js(u':'))
            var.put(u'value', var.get(u'parseAssignmentExpression')())
            return var.get(u'node').callprop(u'finishProperty',Js(u'init'),var.get(u'key'),var.get(u'value'))
            pass
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseObjectProperty'
    var.put(u'parseObjectProperty', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'param', u'body', u'node'])
        var.put(u'node', var.get(u'Node').create())
        var.get(u'expectKeyword')(Js(u'catch'))
        var.get(u'expect')(Js(u'('))
        if var.get(u'match')(Js(u')')):
            var.get(u'throwUnexpected')(var.get(u'lookahead'))
            pass
        var.put(u'param', var.get(u'parseVariableIdentifier')())
        if (var.get(u'strict') and var.get(u'isRestrictedWord')(var.get(u'param').get(u'name'))):
            PyJsLvalObject90_ = Js({})
            var.get(u'throwErrorTolerant')(PyJsLvalObject90_,var.get(u'Messages').get(u'StrictCatchVariable'))
            pass
        var.get(u'expect')(Js(u')'))
        var.put(u'body', var.get(u'parseBlock')())
        return var.get(u'node').callprop(u'finishCatchClause',var.get(u'param'),var.get(u'body'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseCatchClause'
    var.put(u'parseCatchClause', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'pos', u'line', u'start'])
        pass
        var.put(u'pos', var.get(u'index'))
        var.put(u'line', var.get(u'lineNumber'))
        var.put(u'start', var.get(u'lineStart'))
        var.put(u'lookahead', (var.get(u'collectToken')() if var.put(u'lookahead', (PyJsStrictNeq(var.get(u'extra').get(u'tokens').typeof(),Js(u'undefined')))) else var.get(u'advance')()))
        var.put(u'index', var.get(u'pos'))
        var.put(u'lineNumber', var.get(u'line'))
        var.put(u'lineStart', var.get(u'start'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'peek'
    var.put(u'peek', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'args'])
        PyJsLvalArray13_ = Js([None])
        var.put(u'args', PyJsLvalArray13_)
        var.get(u'expect')(Js(u'('))
        if var.get(u'match')(Js(u')')).neg():
            while (var.get(u'index')<var.get(u'length')):
                var.get(u'args').callprop(u'push',var.get(u'parseAssignmentExpression')())
                if var.get(u'match')(Js(u')')):
                    break
                    pass
                var.get(u'expectTolerant')(Js(u','))
                pass
            pass
        var.get(u'expect')(Js(u')'))
        return var.get(u'args')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseArguments'
    var.put(u'parseArguments', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(pattern, flags, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'pattern':pattern, u'flags':flags}, var)
        var.registers([u'value'])
        pass
        try:
            var.put(u'value', var.get(u'RegExp').create(var.get(u'pattern'),var.get(u'flags')))
            pass
        except PyJsException as PyJsTempException:
            PyJsHolder_65_92217679 = var.own.get(u'e')
            var.force_own_put(u'e', PyExceptionToJs(PyJsTempException))
            try:
                PyJsLvalObject43_ = Js({})
                var.get(u'throwError')(PyJsLvalObject43_,var.get(u'Messages').get(u'InvalidRegExp'))
                pass
            finally:
                if PyJsHolder_65_92217679 is not None:
                    var.own[u'e'] = PyJsHolder_65_92217679
                else:
                    del var.own[u'e']
                del PyJsHolder_65_92217679
        return var.get(u'value')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'testRegExp'
    var.put(u'testRegExp', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'type', u'expr', u'labeledBody', u'key', u'node'])
        var.put(u'type', var.get(u'lookahead').get(u'type'))
        if PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'EOF')):
            var.get(u'throwUnexpected')(var.get(u'lookahead'))
            pass
        if (PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'Punctuator')) and PyJsStrictEq(var.get(u'lookahead').get(u'value'),Js(u'{'))):
            return var.get(u'parseBlock')()
            pass
        var.put(u'node', var.get(u'Node').create())
        if PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'Punctuator')):
            while 1:
                SWITCHED = False
                CONDITION = ((var.get(u'lookahead').get(u'value')))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u';')):
                    return var.get(u'parseEmptyStatement')(var.get(u'node'))
                    SWITCHED = True
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'(')):
                    return var.get(u'parseExpressionStatement')(var.get(u'node'))
                    SWITCHED = True
                if True:
                    break
                    pass
                    SWITCHED = True
                break
            pass
        elif PyJsStrictEq(var.get(u'type'),var.get(u'Token').get(u'Keyword')):
            while 1:
                SWITCHED = False
                CONDITION = ((var.get(u'lookahead').get(u'value')))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'break')):
                    return var.get(u'parseBreakStatement')(var.get(u'node'))
                    SWITCHED = True
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'continue')):
                    return var.get(u'parseContinueStatement')(var.get(u'node'))
                    SWITCHED = True
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'debugger')):
                    return var.get(u'parseDebuggerStatement')(var.get(u'node'))
                    SWITCHED = True
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'do')):
                    return var.get(u'parseDoWhileStatement')(var.get(u'node'))
                    SWITCHED = True
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'for')):
                    return var.get(u'parseForStatement')(var.get(u'node'))
                    SWITCHED = True
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'function')):
                    return var.get(u'parseFunctionDeclaration')(var.get(u'node'))
                    SWITCHED = True
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'if')):
                    return var.get(u'parseIfStatement')(var.get(u'node'))
                    SWITCHED = True
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'return')):
                    return var.get(u'parseReturnStatement')(var.get(u'node'))
                    SWITCHED = True
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'switch')):
                    return var.get(u'parseSwitchStatement')(var.get(u'node'))
                    SWITCHED = True
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'throw')):
                    return var.get(u'parseThrowStatement')(var.get(u'node'))
                    SWITCHED = True
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'try')):
                    return var.get(u'parseTryStatement')(var.get(u'node'))
                    SWITCHED = True
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'var')):
                    return var.get(u'parseVariableStatement')(var.get(u'node'))
                    SWITCHED = True
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'while')):
                    return var.get(u'parseWhileStatement')(var.get(u'node'))
                    SWITCHED = True
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'with')):
                    return var.get(u'parseWithStatement')(var.get(u'node'))
                    SWITCHED = True
                if True:
                    break
                    pass
                    SWITCHED = True
                break
            pass
        var.put(u'expr', var.get(u'parseExpression')())
        if ((PyJsStrictEq(var.get(u'expr').get(u'type'),var.get(u'Syntax').get(u'Identifier'))) and var.get(u'match')(Js(u':'))):
            var.get(u'lex')()
            var.put(u'key', (Js(u'$')+var.get(u'expr').get(u'name')))
            if var.get(u'Object').get(u'prototype').get(u'hasOwnProperty').callprop(u'call',var.get(u'state').get(u'labelSet'),var.get(u'key')):
                PyJsLvalObject92_ = Js({})
                var.get(u'throwError')(PyJsLvalObject92_,var.get(u'Messages').get(u'Redeclaration'),Js(u'Label'),var.get(u'expr').get(u'name'))
                pass
            var.get(u'state').get(u'labelSet').put(var.get(u'key'), var.get(u'true'))
            var.put(u'labeledBody', var.get(u'parseStatement')())
            var.get(u'state').get(u'labelSet').delete(var.get(u'key'))
            return var.get(u'node').callprop(u'finishLabeledStatement',var.get(u'expr'),var.get(u'labeledBody'))
            pass
        var.get(u'consumeSemicolon')()
        return var.get(u'node').callprop(u'finishExpressionStatement',var.get(u'expr'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseStatement'
    var.put(u'parseStatement', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'properties', u'token', u'property', u'name', u'key', u'kind', u'map', u'toString', u'node'])
        PyJsLvalArray12_ = Js([None])
        var.put(u'properties', PyJsLvalArray12_)
        PyJsLvalObject63_ = Js({})
        var.put(u'map', PyJsLvalObject63_)
        var.put(u'toString', var.get(u'String'))
        var.put(u'node', var.get(u'Node').create())
        var.get(u'expect')(Js(u'{'))
        while var.get(u'match')(Js(u'}')).neg():
            var.put(u'property', var.get(u'parseObjectProperty')())
            if PyJsStrictEq(var.get(u'property').get(u'key').get(u'type'),var.get(u'Syntax').get(u'Identifier')):
                var.put(u'name', var.get(u'property').get(u'key').get(u'name'))
                pass
            else:
                var.put(u'name', var.get(u'toString')(var.get(u'property').get(u'key').get(u'value')))
                pass
            var.put(u'kind', (var.get(u'PropertyKind').get(u'Data') if var.put(u'kind', (PyJsStrictEq(var.get(u'property').get(u'kind'),Js(u'init')))) else (var.get(u'PropertyKind').get(u'Get') if (PyJsStrictEq(var.get(u'property').get(u'kind'),Js(u'get'))) else var.get(u'PropertyKind').get(u'Set'))))
            var.put(u'key', (Js(u'$')+var.get(u'name')))
            if var.get(u'Object').get(u'prototype').get(u'hasOwnProperty').callprop(u'call',var.get(u'map'),var.get(u'key')):
                if PyJsStrictEq(var.get(u'map').get(var.get(u'key')),var.get(u'PropertyKind').get(u'Data')):
                    if (var.get(u'strict') and PyJsStrictEq(var.get(u'kind'),var.get(u'PropertyKind').get(u'Data'))):
                        PyJsLvalObject64_ = Js({})
                        var.get(u'throwErrorTolerant')(PyJsLvalObject64_,var.get(u'Messages').get(u'StrictDuplicateProperty'))
                        pass
                    elif PyJsStrictNeq(var.get(u'kind'),var.get(u'PropertyKind').get(u'Data')):
                        PyJsLvalObject65_ = Js({})
                        var.get(u'throwErrorTolerant')(PyJsLvalObject65_,var.get(u'Messages').get(u'AccessorDataProperty'))
                        pass
                    pass
                else:
                    if PyJsStrictEq(var.get(u'kind'),var.get(u'PropertyKind').get(u'Data')):
                        PyJsLvalObject66_ = Js({})
                        var.get(u'throwErrorTolerant')(PyJsLvalObject66_,var.get(u'Messages').get(u'AccessorDataProperty'))
                        pass
                    elif (var.get(u'map').get(var.get(u'key'))&var.get(u'kind')):
                        PyJsLvalObject67_ = Js({})
                        var.get(u'throwErrorTolerant')(PyJsLvalObject67_,var.get(u'Messages').get(u'AccessorGetSet'))
                        pass
                    pass
                var.get(u'map').put(var.get(u'key'), var.get(u'kind'),u'|')
                pass
            else:
                var.get(u'map').put(var.get(u'key'), var.get(u'kind'))
                pass
            var.get(u'properties').callprop(u'push',var.get(u'property'))
            if var.get(u'match')(Js(u'}')).neg():
                var.get(u'expectTolerant')(Js(u','))
                pass
            pass
        var.get(u'expect')(Js(u'}'))
        return var.get(u'node').callprop(u'finishObjectExpression',var.get(u'properties'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseObjectInitialiser'
    var.put(u'parseObjectInitialiser', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(ch, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'ch':ch}, var)
        return ((((PyJsStrictEq(var.get(u'ch'),Js(0x0A))) or (PyJsStrictEq(var.get(u'ch'),Js(0x0D)))) or (PyJsStrictEq(var.get(u'ch'),Js(0x2028)))) or (PyJsStrictEq(var.get(u'ch'),Js(0x2029))))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'isLineTerminator'
    var.put(u'isLineTerminator', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'list', u'statement'])
        PyJsLvalArray24_ = Js([None])
        var.put(u'list', PyJsLvalArray24_)
        while (var.get(u'index')<var.get(u'length')):
            if var.get(u'match')(Js(u'}')):
                break
                pass
            var.put(u'statement', var.get(u'parseSourceElement')())
            if PyJsStrictEq(var.get(u'statement',throw=False).typeof(),Js(u'undefined')):
                break
                pass
            var.get(u'list').callprop(u'push',var.get(u'statement'))
            pass
        return var.get(u'list')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseStatementList'
    var.put(u'parseStatementList', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'token'])
        pass
        var.put(u'token', var.get(u'lookahead'))
        var.put(u'index', var.get(u'token').get(u'end'))
        var.put(u'lineNumber', var.get(u'token').get(u'lineNumber'))
        var.put(u'lineStart', var.get(u'token').get(u'lineStart'))
        var.put(u'lookahead', (var.get(u'collectToken')() if var.put(u'lookahead', (PyJsStrictNeq(var.get(u'extra').get(u'tokens').typeof(),Js(u'undefined')))) else var.get(u'advance')()))
        var.put(u'index', var.get(u'token').get(u'end'))
        var.put(u'lineNumber', var.get(u'token').get(u'lineNumber'))
        var.put(u'lineStart', var.get(u'token').get(u'lineStart'))
        return var.get(u'token')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'lex'
    var.put(u'lex', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'sourceElement', u'sourceElements', u'token', u'directive', u'firstRestricted', u'oldLabelSet', u'oldInIteration', u'oldInSwitch', u'oldInFunctionBody', u'oldParenthesisCount', u'node'])
        PyJsLvalArray30_ = Js([None])
        var.put(u'sourceElements', PyJsLvalArray30_)
        var.put(u'node', var.get(u'Node').create())
        var.get(u'expect')(Js(u'{'))
        while (var.get(u'index')<var.get(u'length')):
            if PyJsStrictNeq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'StringLiteral')):
                break
                pass
            var.put(u'token', var.get(u'lookahead'))
            var.put(u'sourceElement', var.get(u'parseSourceElement')())
            var.get(u'sourceElements').callprop(u'push',var.get(u'sourceElement'))
            if PyJsStrictNeq(var.get(u'sourceElement').get(u'expression').get(u'type'),var.get(u'Syntax').get(u'Literal')):
                break
                pass
            var.put(u'directive', var.get(u'source').callprop(u'slice',(var.get(u'token').get(u'start')+Js(1)),(var.get(u'token').get(u'end')-Js(1))))
            if PyJsStrictEq(var.get(u'directive'),Js(u'use strict')):
                var.put(u'strict', var.get(u'true'))
                if var.get(u'firstRestricted'):
                    var.get(u'throwErrorTolerant')(var.get(u'firstRestricted'),var.get(u'Messages').get(u'StrictOctalLiteral'))
                    pass
                pass
            else:
                if (var.get(u'firstRestricted').neg() and var.get(u'token').get(u'octal')):
                    var.put(u'firstRestricted', var.get(u'token'))
                    pass
                pass
            pass
        var.put(u'oldLabelSet', var.get(u'state').get(u'labelSet'))
        var.put(u'oldInIteration', var.get(u'state').get(u'inIteration'))
        var.put(u'oldInSwitch', var.get(u'state').get(u'inSwitch'))
        var.put(u'oldInFunctionBody', var.get(u'state').get(u'inFunctionBody'))
        var.put(u'oldParenthesisCount', var.get(u'state').get(u'parenthesizedCount'))
        PyJsLvalObject93_ = Js({})
        var.get(u'state').put(u'labelSet', PyJsLvalObject93_)
        var.get(u'state').put(u'inIteration', var.get(u'false'))
        var.get(u'state').put(u'inSwitch', var.get(u'false'))
        var.get(u'state').put(u'inFunctionBody', var.get(u'true'))
        var.get(u'state').put(u'parenthesizedCount', Js(0))
        while (var.get(u'index')<var.get(u'length')):
            if var.get(u'match')(Js(u'}')):
                break
                pass
            var.put(u'sourceElement', var.get(u'parseSourceElement')())
            if PyJsStrictEq(var.get(u'sourceElement',throw=False).typeof(),Js(u'undefined')):
                break
                pass
            var.get(u'sourceElements').callprop(u'push',var.get(u'sourceElement'))
            pass
        var.get(u'expect')(Js(u'}'))
        var.get(u'state').put(u'labelSet', var.get(u'oldLabelSet'))
        var.get(u'state').put(u'inIteration', var.get(u'oldInIteration'))
        var.get(u'state').put(u'inSwitch', var.get(u'oldInSwitch'))
        var.get(u'state').put(u'inFunctionBody', var.get(u'oldInFunctionBody'))
        var.get(u'state').put(u'parenthesizedCount', var.get(u'oldParenthesisCount'))
        return var.get(u'node').callprop(u'finishBlockStatement',var.get(u'sourceElements'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseFunctionSourceElements'
    var.put(u'parseFunctionSourceElements', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        try:
            var.get(u'throwError').callprop(u'apply',var.get(u'null'),var.get(u'arguments'))
            pass
        except PyJsException as PyJsTempException:
            PyJsHolder_65_66214253 = var.own.get(u'e')
            var.force_own_put(u'e', PyExceptionToJs(PyJsTempException))
            try:
                if var.get(u'extra').get(u'errors'):
                    var.get(u'extra').get(u'errors').callprop(u'push',var.get(u'e'))
                    pass
                else:
                    PyJsTempException = JsToPyException(var.get(u'e'))
                    raise PyJsTempException
                    pass
                pass
            finally:
                if PyJsHolder_65_66214253 is not None:
                    var.own[u'e'] = PyJsHolder_65_66214253
                else:
                    del var.own[u'e']
                del PyJsHolder_65_66214253
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'throwErrorTolerant'
    var.put(u'throwErrorTolerant', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(token, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'token':token}, var)
        return (((PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Identifier')) or PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Keyword'))) or PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'BooleanLiteral'))) or PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'NullLiteral')))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'isIdentifierName'
    var.put(u'isIdentifierName', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'ch'])
        pass
        var.get(u'skipComment')()
        if (var.get(u'index')>=var.get(u'length')):
            PyJsLvalObject56_ = Js({u'type':var.get(u'Token').get(u'EOF'),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'index'),u'end':var.get(u'index')})
            return PyJsLvalObject56_
            pass
        var.put(u'ch', var.get(u'source').callprop(u'charCodeAt',var.get(u'index')))
        if var.get(u'isIdentifierStart')(var.get(u'ch')):
            return var.get(u'scanIdentifier')()
            pass
        if ((PyJsStrictEq(var.get(u'ch'),Js(0x28)) or PyJsStrictEq(var.get(u'ch'),Js(0x29))) or PyJsStrictEq(var.get(u'ch'),Js(0x3B))):
            return var.get(u'scanPunctuator')()
            pass
        if (PyJsStrictEq(var.get(u'ch'),Js(0x27)) or PyJsStrictEq(var.get(u'ch'),Js(0x22))):
            return var.get(u'scanStringLiteral')()
            pass
        if PyJsStrictEq(var.get(u'ch'),Js(0x2E)):
            if var.get(u'isDecimalDigit')(var.get(u'source').callprop(u'charCodeAt',(var.get(u'index')+Js(1)))):
                return var.get(u'scanNumericLiteral')()
                pass
            return var.get(u'scanPunctuator')()
            pass
        if var.get(u'isDecimalDigit')(var.get(u'ch')):
            return var.get(u'scanNumericLiteral')()
            pass
        if (var.get(u'extra').get(u'tokenize') and PyJsStrictEq(var.get(u'ch'),Js(0x2F))):
            return var.get(u'advanceSlash')()
            pass
        return var.get(u'scanPunctuator')()
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'advance'
    var.put(u'advance', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(token, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'token':token}, var)
        if PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'EOF')):
            var.get(u'throwError')(var.get(u'token'),var.get(u'Messages').get(u'UnexpectedEOS'))
            pass
        if PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'NumericLiteral')):
            var.get(u'throwError')(var.get(u'token'),var.get(u'Messages').get(u'UnexpectedNumber'))
            pass
        if PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'StringLiteral')):
            var.get(u'throwError')(var.get(u'token'),var.get(u'Messages').get(u'UnexpectedString'))
            pass
        if PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Identifier')):
            var.get(u'throwError')(var.get(u'token'),var.get(u'Messages').get(u'UnexpectedIdentifier'))
            pass
        if PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Keyword')):
            if var.get(u'isFutureReservedWord')(var.get(u'token').get(u'value')):
                var.get(u'throwError')(var.get(u'token'),var.get(u'Messages').get(u'UnexpectedReserved'))
                pass
            elif (var.get(u'strict') and var.get(u'isStrictModeReservedWord')(var.get(u'token').get(u'value'))):
                var.get(u'throwErrorTolerant')(var.get(u'token'),var.get(u'Messages').get(u'StrictReservedWord'))
                return var.get('undefined')
                pass
            var.get(u'throwError')(var.get(u'token'),var.get(u'Messages').get(u'UnexpectedToken'),var.get(u'token').get(u'value'))
            pass
        var.get(u'throwError')(var.get(u'token'),var.get(u'Messages').get(u'UnexpectedToken'),var.get(u'token').get(u'value'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'throwUnexpected'
    var.put(u'throwUnexpected', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'elements', u'node'])
        PyJsLvalArray7_ = Js([None])
        var.put(u'elements', PyJsLvalArray7_)
        var.put(u'node', var.get(u'Node').create())
        var.get(u'expect')(Js(u'['))
        while var.get(u'match')(Js(u']')).neg():
            if var.get(u'match')(Js(u',')):
                var.get(u'lex')()
                var.get(u'elements').callprop(u'push',var.get(u'null'))
                pass
            else:
                var.get(u'elements').callprop(u'push',var.get(u'parseAssignmentExpression')())
                if var.get(u'match')(Js(u']')).neg():
                    var.get(u'expect')(Js(u','))
                    pass
                pass
            pass
        var.get(u'lex')()
        return var.get(u'node').callprop(u'finishArrayExpression',var.get(u'elements'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseArrayInitialiser'
    var.put(u'parseArrayInitialiser', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(id, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'id':id}, var)
        while 1:
            SWITCHED = False
            CONDITION = ((var.get(u'id')))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'class')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'enum')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'export')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'extends')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'import')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'super')):
                return var.get(u'true')
                SWITCHED = True
            if True:
                return var.get(u'false')
                pass
                SWITCHED = True
            break
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'isFutureReservedWord'
    var.put(u'isFutureReservedWord', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(start, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'start':start}, var)
        var.registers([u'number'])
        var.put(u'number', (Js(u'0')+var.get(u'source').get(var.get(u'index').PostInc())))
        while (var.get(u'index')<var.get(u'length')):
            if var.get(u'isOctalDigit')(var.get(u'source').get(var.get(u'index'))).neg():
                break
                pass
            var.put(u'number', var.get(u'source').get(var.get(u'index').PostInc()),u'+')
            pass
        if (var.get(u'isIdentifierStart')(var.get(u'source').callprop(u'charCodeAt',var.get(u'index'))) or var.get(u'isDecimalDigit')(var.get(u'source').callprop(u'charCodeAt',var.get(u'index')))):
            PyJsLvalObject35_ = Js({})
            var.get(u'throwError')(PyJsLvalObject35_,var.get(u'Messages').get(u'UnexpectedToken'),Js(u'ILLEGAL'))
            pass
        PyJsLvalObject36_ = Js({u'type':var.get(u'Token').get(u'NumericLiteral'),u'value':var.get(u'parseInt')(var.get(u'number'),Js(8)),u'octal':var.get(u'true'),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
        return PyJsLvalObject36_
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'scanOctalLiteral'
    var.put(u'scanOctalLiteral', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(id, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'id':id}, var)
        if (var.get(u'strict') and var.get(u'isStrictModeReservedWord')(var.get(u'id'))):
            return var.get(u'true')
            pass
        while 1:
            SWITCHED = False
            CONDITION = ((var.get(u'id').get(u'length')))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(2)):
                return (((PyJsStrictEq(var.get(u'id'),Js(u'if'))) or (PyJsStrictEq(var.get(u'id'),Js(u'in')))) or (PyJsStrictEq(var.get(u'id'),Js(u'do'))))
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(3)):
                return (((((PyJsStrictEq(var.get(u'id'),Js(u'var'))) or (PyJsStrictEq(var.get(u'id'),Js(u'for')))) or (PyJsStrictEq(var.get(u'id'),Js(u'new')))) or (PyJsStrictEq(var.get(u'id'),Js(u'try')))) or (PyJsStrictEq(var.get(u'id'),Js(u'let'))))
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(4)):
                return ((((((PyJsStrictEq(var.get(u'id'),Js(u'this'))) or (PyJsStrictEq(var.get(u'id'),Js(u'else')))) or (PyJsStrictEq(var.get(u'id'),Js(u'case')))) or (PyJsStrictEq(var.get(u'id'),Js(u'void')))) or (PyJsStrictEq(var.get(u'id'),Js(u'with')))) or (PyJsStrictEq(var.get(u'id'),Js(u'enum'))))
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(5)):
                return ((((((((PyJsStrictEq(var.get(u'id'),Js(u'while'))) or (PyJsStrictEq(var.get(u'id'),Js(u'break')))) or (PyJsStrictEq(var.get(u'id'),Js(u'catch')))) or (PyJsStrictEq(var.get(u'id'),Js(u'throw')))) or (PyJsStrictEq(var.get(u'id'),Js(u'const')))) or (PyJsStrictEq(var.get(u'id'),Js(u'yield')))) or (PyJsStrictEq(var.get(u'id'),Js(u'class')))) or (PyJsStrictEq(var.get(u'id'),Js(u'super'))))
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(6)):
                return ((((((PyJsStrictEq(var.get(u'id'),Js(u'return'))) or (PyJsStrictEq(var.get(u'id'),Js(u'typeof')))) or (PyJsStrictEq(var.get(u'id'),Js(u'delete')))) or (PyJsStrictEq(var.get(u'id'),Js(u'switch')))) or (PyJsStrictEq(var.get(u'id'),Js(u'export')))) or (PyJsStrictEq(var.get(u'id'),Js(u'import'))))
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(7)):
                return (((PyJsStrictEq(var.get(u'id'),Js(u'default'))) or (PyJsStrictEq(var.get(u'id'),Js(u'finally')))) or (PyJsStrictEq(var.get(u'id'),Js(u'extends'))))
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(8)):
                return (((PyJsStrictEq(var.get(u'id'),Js(u'function'))) or (PyJsStrictEq(var.get(u'id'),Js(u'continue')))) or (PyJsStrictEq(var.get(u'id'),Js(u'debugger'))))
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(10)):
                return (PyJsStrictEq(var.get(u'id'),Js(u'instanceof')))
                SWITCHED = True
            if True:
                return var.get(u'false')
                pass
                SWITCHED = True
            break
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'isKeyword'
    var.put(u'isKeyword', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'marker', u'markers', u'expr', u'token', u'prec', u'stack', u'right', u'operator', u'left', u'i'])
        pass
        var.put(u'marker', var.get(u'lookahead'))
        var.put(u'left', var.get(u'parseUnaryExpression')())
        if PyJsStrictEq(var.get(u'left'),var.get(u'PlaceHolders').get(u'ArrowParameterPlaceHolder')):
            return var.get(u'left')
            pass
        var.put(u'token', var.get(u'lookahead'))
        var.put(u'prec', var.get(u'binaryPrecedence')(var.get(u'token'),var.get(u'state').get(u'allowIn')))
        if PyJsStrictEq(var.get(u'prec'),Js(0)):
            return var.get(u'left')
            pass
        var.get(u'token').put(u'prec', var.get(u'prec'))
        var.get(u'lex')()
        PyJsLvalArray15_ = Js([var.get(u'marker'),var.get(u'lookahead')])
        var.put(u'markers', PyJsLvalArray15_)
        var.put(u'right', var.get(u'parseUnaryExpression')())
        PyJsLvalArray16_ = Js([var.get(u'left'),var.get(u'token'),var.get(u'right')])
        var.put(u'stack', PyJsLvalArray16_)
        while ((var.put(u'prec', var.get(u'binaryPrecedence')(var.get(u'lookahead'),var.get(u'state').get(u'allowIn'))))>Js(0)):
            while (((var.get(u'stack').get(u'length')>Js(2))) and ((var.get(u'prec')<=var.get(u'stack').get((var.get(u'stack').get(u'length')-Js(2))).get(u'prec')))):
                var.put(u'right', var.get(u'stack').callprop(u'pop'))
                var.put(u'operator', var.get(u'stack').callprop(u'pop').get(u'value'))
                var.put(u'left', var.get(u'stack').callprop(u'pop'))
                var.get(u'markers').callprop(u'pop')
                var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'markers').get((var.get(u'markers').get(u'length')-Js(1)))).callprop(u'finishBinaryExpression',var.get(u'operator'),var.get(u'left'),var.get(u'right')))
                var.get(u'stack').callprop(u'push',var.get(u'expr'))
                pass
            var.put(u'token', var.get(u'lex')())
            var.get(u'token').put(u'prec', var.get(u'prec'))
            var.get(u'stack').callprop(u'push',var.get(u'token'))
            var.get(u'markers').callprop(u'push',var.get(u'lookahead'))
            var.put(u'expr', var.get(u'parseUnaryExpression')())
            var.get(u'stack').callprop(u'push',var.get(u'expr'))
            pass
        var.put(u'i', (var.get(u'stack').get(u'length')-Js(1)))
        var.put(u'expr', var.get(u'stack').get(var.get(u'i')))
        var.get(u'markers').callprop(u'pop')
        while (var.get(u'i')>Js(1)):
            var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'markers').callprop(u'pop')).callprop(u'finishBinaryExpression',var.get(u'stack').get((var.get(u'i')-Js(1))).get(u'value'),var.get(u'stack').get((var.get(u'i')-Js(2))),var.get(u'expr')))
            var.put(u'i', Js(2),u'-')
            pass
        return var.get(u'expr')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseBinaryExpression'
    var.put(u'parseBinaryExpression', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'start', u'id', u'type'])
        pass
        var.put(u'start', var.get(u'index'))
        var.put(u'id', (var.get(u'getEscapedIdentifier')() if var.put(u'id', (PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt',var.get(u'index')),Js(0x5C)))) else var.get(u'getIdentifier')()))
        if PyJsStrictEq(var.get(u'id').get(u'length'),Js(1)):
            var.put(u'type', var.get(u'Token').get(u'Identifier'))
            pass
        elif var.get(u'isKeyword')(var.get(u'id')):
            var.put(u'type', var.get(u'Token').get(u'Keyword'))
            pass
        elif PyJsStrictEq(var.get(u'id'),Js(u'null')):
            var.put(u'type', var.get(u'Token').get(u'NullLiteral'))
            pass
        elif (PyJsStrictEq(var.get(u'id'),Js(u'true')) or PyJsStrictEq(var.get(u'id'),Js(u'false'))):
            var.put(u'type', var.get(u'Token').get(u'BooleanLiteral'))
            pass
        else:
            var.put(u'type', var.get(u'Token').get(u'Identifier'))
            pass
        PyJsLvalObject23_ = Js({u'type':var.get(u'type'),u'value':var.get(u'id'),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
        return PyJsLvalObject23_
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'scanIdentifier'
    var.put(u'scanIdentifier', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'token', u'node'])
        var.put(u'node', var.get(u'Node').create())
        var.put(u'token', var.get(u'lex')())
        if var.get(u'isIdentifierName')(var.get(u'token')).neg():
            var.get(u'throwUnexpected')(var.get(u'token'))
            pass
        return var.get(u'node').callprop(u'finishIdentifier',var.get(u'token').get(u'value'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseNonComputedProperty'
    var.put(u'parseNonComputedProperty', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(options, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'options':options}, var)
        var.registers([u'token', u'param', u'def'])
        pass
        var.put(u'token', var.get(u'lookahead'))
        var.put(u'param', var.get(u'parseVariableIdentifier')())
        var.get(u'validateParam')(var.get(u'options'),var.get(u'token'),var.get(u'token').get(u'value'))
        if var.get(u'match')(Js(u'=')):
            var.get(u'lex')()
            var.put(u'def', var.get(u'parseAssignmentExpression')())
            var.get(u'options').get(u'defaultCount').PreInc()
            pass
        var.get(u'options').get(u'params').callprop(u'push',var.get(u'param'))
        var.get(u'options').get(u'defaults').callprop(u'push',var.get(u'def'))
        return var.get(u'match')(Js(u')')).neg()
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseParam'
    var.put(u'parseParam', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'callee', u'args', u'node'])
        var.put(u'node', var.get(u'Node').create())
        var.get(u'expectKeyword')(Js(u'new'))
        var.put(u'callee', var.get(u'parseLeftHandSideExpression')())
        PyJsLvalArray14_ = Js([None])
        var.put(u'args', (var.get(u'parseArguments')() if var.put(u'args', var.get(u'match')(Js(u'('))) else PyJsLvalArray14_))
        return var.get(u'node').callprop(u'finishNewExpression',var.get(u'callee'),var.get(u'args'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseNewExpression'
    var.put(u'parseNewExpression', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'ch', u'str', u'classMarker', u'terminated', u'body'])
        pass
        var.put(u'ch', var.get(u'source').get(var.get(u'index')))
        var.get(u'assert')(PyJsStrictEq(var.get(u'ch'),Js(u'/')),Js(u'Regular expression literal must start with a slash'))
        var.put(u'str', var.get(u'source').get(var.get(u'index').PostInc()))
        var.put(u'classMarker', var.get(u'false'))
        var.put(u'terminated', var.get(u'false'))
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').get(var.get(u'index').PostInc()))
            var.put(u'str', var.get(u'ch'),u'+')
            if PyJsStrictEq(var.get(u'ch'),Js(u'\\')):
                var.put(u'ch', var.get(u'source').get(var.get(u'index').PostInc()))
                if var.get(u'isLineTerminator')(var.get(u'ch').callprop(u'charCodeAt',Js(0))):
                    PyJsLvalObject44_ = Js({})
                    var.get(u'throwError')(PyJsLvalObject44_,var.get(u'Messages').get(u'UnterminatedRegExp'))
                    pass
                var.put(u'str', var.get(u'ch'),u'+')
                pass
            elif var.get(u'isLineTerminator')(var.get(u'ch').callprop(u'charCodeAt',Js(0))):
                PyJsLvalObject45_ = Js({})
                var.get(u'throwError')(PyJsLvalObject45_,var.get(u'Messages').get(u'UnterminatedRegExp'))
                pass
            elif var.get(u'classMarker'):
                if PyJsStrictEq(var.get(u'ch'),Js(u']')):
                    var.put(u'classMarker', var.get(u'false'))
                    pass
                pass
            else:
                if PyJsStrictEq(var.get(u'ch'),Js(u'/')):
                    var.put(u'terminated', var.get(u'true'))
                    break
                    pass
                elif PyJsStrictEq(var.get(u'ch'),Js(u'[')):
                    var.put(u'classMarker', var.get(u'true'))
                    pass
                pass
            pass
        if var.get(u'terminated').neg():
            PyJsLvalObject46_ = Js({})
            var.get(u'throwError')(PyJsLvalObject46_,var.get(u'Messages').get(u'UnterminatedRegExp'))
            pass
        var.put(u'body', var.get(u'str').callprop(u'substr',Js(1),(var.get(u'str').get(u'length')-Js(2))))
        PyJsLvalObject47_ = Js({u'value':var.get(u'body'),u'literal':var.get(u'str')})
        return PyJsLvalObject47_
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'scanRegExpBody'
    var.put(u'scanRegExpBody', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.put(u'index', var.get(u'lookahead').get(u'start'))
        if PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'StringLiteral')):
            var.put(u'lineNumber', var.get(u'lookahead').get(u'startLineNumber'))
            var.put(u'lineStart', var.get(u'lookahead').get(u'startLineStart'))
            pass
        else:
            var.put(u'lineNumber', var.get(u'lookahead').get(u'lineNumber'))
            var.put(u'lineStart', var.get(u'lookahead').get(u'lineStart'))
            pass
        if var.get(u'extra').get(u'range'):
            PyJsLvalArray5_ = Js([var.get(u'index'),Js(0)])
            var.get(u'this').put(u'range', PyJsLvalArray5_)
            pass
        if var.get(u'extra').get(u'loc'):
            var.get(u'this').put(u'loc', var.get(u'SourceLocation').create())
            pass
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'Node'
    var.put(u'Node', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'loc', u'token', u'value'])
        pass
        var.get(u'skipComment')()
        PyJsLvalObject108_ = Js({u'line':var.get(u'lineNumber'),u'column':(var.get(u'index')-var.get(u'lineStart'))})
        PyJsLvalObject57_ = Js({u'start':PyJsLvalObject108_})
        var.put(u'loc', PyJsLvalObject57_)
        var.put(u'token', var.get(u'advance')())
        PyJsLvalObject58_ = Js({u'line':var.get(u'lineNumber'),u'column':(var.get(u'index')-var.get(u'lineStart'))})
        var.get(u'loc').put(u'end', PyJsLvalObject58_)
        if PyJsStrictNeq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'EOF')):
            var.put(u'value', var.get(u'source').callprop(u'slice',var.get(u'token').get(u'start'),var.get(u'token').get(u'end')))
            PyJsLvalArray48_ = Js([var.get(u'token').get(u'start'),var.get(u'token').get(u'end')])
            PyJsLvalObject59_ = Js({u'type':var.get(u'TokenName').get(var.get(u'token').get(u'type')),u'value':var.get(u'value'),u'range':PyJsLvalArray48_,u'loc':var.get(u'loc')})
            var.get(u'extra').get(u'tokens').callprop(u'push',PyJsLvalObject59_)
            pass
        return var.get(u'token')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'collectToken'
    var.put(u'collectToken', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(node, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'node':node}, var)
        var.registers([u'object', u'body'])
        pass
        if var.get(u'strict'):
            var.get(u'skipComment')()
            PyJsLvalObject87_ = Js({})
            var.get(u'throwErrorTolerant')(PyJsLvalObject87_,var.get(u'Messages').get(u'StrictModeWith'))
            pass
        var.get(u'expectKeyword')(Js(u'with'))
        var.get(u'expect')(Js(u'('))
        var.put(u'object', var.get(u'parseExpression')())
        var.get(u'expect')(Js(u')'))
        var.put(u'body', var.get(u'parseStatement')())
        return var.get(u'node').callprop(u'finishWithStatement',var.get(u'object'),var.get(u'body'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseWithStatement'
    var.put(u'parseWithStatement', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(expressions, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'expressions':expressions}, var)
        var.registers([u'i', u'len', u'param', u'params', u'defaults', u'defaultCount', u'options', u'rest'])
        pass
        PyJsLvalArray17_ = Js([None])
        var.put(u'params', PyJsLvalArray17_)
        PyJsLvalArray18_ = Js([None])
        var.put(u'defaults', PyJsLvalArray18_)
        var.put(u'defaultCount', Js(0))
        var.put(u'rest', var.get(u'null'))
        PyJsLvalObject106_ = Js({})
        PyJsLvalObject73_ = Js({u'paramSet':PyJsLvalObject106_})
        var.put(u'options', PyJsLvalObject73_)
        #for JS loop
        PyJsComma(var.put(u'i', Js(0)),var.put(u'len', var.get(u'expressions').get(u'length')))
        while (var.get(u'i')<var.get(u'len')):
            var.put(u'param', var.get(u'expressions').get(var.get(u'i')))
            if PyJsStrictEq(var.get(u'param').get(u'type'),var.get(u'Syntax').get(u'Identifier')):
                var.get(u'params').callprop(u'push',var.get(u'param'))
                var.get(u'defaults').callprop(u'push',var.get(u'null'))
                var.get(u'validateParam')(var.get(u'options'),var.get(u'param'),var.get(u'param').get(u'name'))
                pass
            elif PyJsStrictEq(var.get(u'param').get(u'type'),var.get(u'Syntax').get(u'AssignmentExpression')):
                var.get(u'params').callprop(u'push',var.get(u'param').get(u'left'))
                var.get(u'defaults').callprop(u'push',var.get(u'param').get(u'right'))
                var.get(u'defaultCount').PreInc()
                var.get(u'validateParam')(var.get(u'options'),var.get(u'param').get(u'left'),var.get(u'param').get(u'left').get(u'name'))
                pass
            else:
                return var.get(u'null')
                pass
            pass
            var.put(u'i', Js(1),u'+')
        
        if PyJsStrictEq(var.get(u'options').get(u'message'),var.get(u'Messages').get(u'StrictParamDupe')):
            var.get(u'throwError')((var.get(u'options').get(u'stricted') if var.get(u'strict') else var.get(u'options').get(u'firstRestricted')),var.get(u'options').get(u'message'))
            pass
        if PyJsStrictEq(var.get(u'defaultCount'),Js(0)):
            PyJsLvalArray19_ = Js([None])
            var.put(u'defaults', PyJsLvalArray19_)
            pass
        PyJsLvalObject74_ = Js({u'params':var.get(u'params'),u'defaults':var.get(u'defaults'),u'rest':var.get(u'rest'),u'stricted':var.get(u'options').get(u'stricted'),u'firstRestricted':var.get(u'options').get(u'firstRestricted'),u'message':var.get(u'options').get(u'message')})
        return PyJsLvalObject74_
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'reinterpretAsCoverFormalsList'
    var.put(u'reinterpretAsCoverFormalsList', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'ch', u'start'])
        pass
        var.put(u'start', (PyJsStrictEq(var.get(u'index'),Js(0))))
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').callprop(u'charCodeAt',var.get(u'index')))
            if var.get(u'isWhiteSpace')(var.get(u'ch')):
                var.get(u'index').PreInc()
                pass
            elif var.get(u'isLineTerminator')(var.get(u'ch')):
                var.get(u'index').PreInc()
                if (PyJsStrictEq(var.get(u'ch'),Js(0x0D)) and PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt',var.get(u'index')),Js(0x0A))):
                    var.get(u'index').PreInc()
                    pass
                var.get(u'lineNumber').PreInc()
                var.put(u'lineStart', var.get(u'index'))
                var.put(u'start', var.get(u'true'))
                pass
            elif PyJsStrictEq(var.get(u'ch'),Js(0x2F)):
                var.put(u'ch', var.get(u'source').callprop(u'charCodeAt',(var.get(u'index')+Js(1))))
                if PyJsStrictEq(var.get(u'ch'),Js(0x2F)):
                    var.get(u'index').PreInc()
                    var.get(u'index').PreInc()
                    var.get(u'skipSingleLineComment')(Js(2))
                    var.put(u'start', var.get(u'true'))
                    pass
                elif PyJsStrictEq(var.get(u'ch'),Js(0x2A)):
                    var.get(u'index').PreInc()
                    var.get(u'index').PreInc()
                    var.get(u'skipMultiLineComment')()
                    pass
                else:
                    break
                    pass
                pass
            elif (var.get(u'start') and PyJsStrictEq(var.get(u'ch'),Js(0x2D))):
                if ((PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt',(var.get(u'index')+Js(1))),Js(0x2D))) and (PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt',(var.get(u'index')+Js(2))),Js(0x3E)))):
                    var.put(u'index', Js(3),u'+')
                    var.get(u'skipSingleLineComment')(Js(3))
                    pass
                else:
                    break
                    pass
                pass
            elif PyJsStrictEq(var.get(u'ch'),Js(0x3C)):
                if PyJsStrictEq(var.get(u'source').callprop(u'slice',(var.get(u'index')+Js(1)),(var.get(u'index')+Js(4))),Js(u'!--')):
                    var.get(u'index').PreInc()
                    var.get(u'index').PreInc()
                    var.get(u'index').PreInc()
                    var.get(u'index').PreInc()
                    var.get(u'skipSingleLineComment')(Js(4))
                    pass
                else:
                    break
                    pass
                pass
            else:
                break
                pass
            pass
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'skipComment'
    var.put(u'skipComment', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(node, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'node':node}, var)
        var.registers([u'declarations'])
        pass
        var.get(u'expectKeyword')(Js(u'var'))
        var.put(u'declarations', var.get(u'parseVariableDeclarationList')())
        var.get(u'consumeSemicolon')()
        return var.get(u'node').callprop(u'finishVariableDeclaration',var.get(u'declarations'),Js(u'var'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseVariableStatement'
    var.put(u'parseVariableStatement', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(node, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'node':node}, var)
        var.get(u'expectKeyword')(Js(u'debugger'))
        var.get(u'consumeSemicolon')()
        return var.get(u'node').callprop(u'finishDebuggerStatement')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseDebuggerStatement'
    var.put(u'parseDebuggerStatement', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(code, options, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'code':code, u'options':options}, var)
        var.registers([u'toString', u'tokens'])
        pass
        var.put(u'toString', var.get(u'String'))
        if (PyJsStrictNeq(var.get(u'code',throw=False).typeof(),Js(u'string')) and (var.get(u'code').instanceof(var.get(u'String'))).neg()):
            var.put(u'code', var.get(u'toString')(var.get(u'code')))
            pass
        var.put(u'source', var.get(u'code'))
        var.put(u'index', Js(0))
        var.put(u'lineNumber', (Js(1) if var.put(u'lineNumber', ((var.get(u'source').get(u'length')>Js(0)))) else Js(0)))
        var.put(u'lineStart', Js(0))
        var.put(u'length', var.get(u'source').get(u'length'))
        var.put(u'lookahead', var.get(u'null'))
        PyJsLvalObject109_ = Js({})
        PyJsLvalObject98_ = Js({u'allowIn':var.get(u'true'),u'labelSet':PyJsLvalObject109_,u'inFunctionBody':var.get(u'false'),u'inIteration':var.get(u'false'),u'inSwitch':var.get(u'false'),u'lastCommentStart':(-Js(1))})
        var.put(u'state', PyJsLvalObject98_)
        PyJsLvalObject99_ = Js({})
        var.put(u'extra', PyJsLvalObject99_)
        PyJsLvalObject100_ = Js({})
        var.put(u'options', (var.get(u'options') or PyJsLvalObject100_))
        var.get(u'options').put(u'tokens', var.get(u'true'))
        PyJsLvalArray38_ = Js([None])
        var.get(u'extra').put(u'tokens', PyJsLvalArray38_)
        var.get(u'extra').put(u'tokenize', var.get(u'true'))
        var.get(u'extra').put(u'openParenToken', (-Js(1)))
        var.get(u'extra').put(u'openCurlyToken', (-Js(1)))
        var.get(u'extra').put(u'range', ((PyJsStrictEq(var.get(u'options').get(u'range').typeof(),Js(u'boolean'))) and var.get(u'options').get(u'range')))
        var.get(u'extra').put(u'loc', ((PyJsStrictEq(var.get(u'options').get(u'loc').typeof(),Js(u'boolean'))) and var.get(u'options').get(u'loc')))
        if (PyJsStrictEq(var.get(u'options').get(u'comment').typeof(),Js(u'boolean')) and var.get(u'options').get(u'comment')):
            PyJsLvalArray39_ = Js([None])
            var.get(u'extra').put(u'comments', PyJsLvalArray39_)
            pass
        if (PyJsStrictEq(var.get(u'options').get(u'tolerant').typeof(),Js(u'boolean')) and var.get(u'options').get(u'tolerant')):
            PyJsLvalArray40_ = Js([None])
            var.get(u'extra').put(u'errors', PyJsLvalArray40_)
            pass
        try:
            var.get(u'peek')()
            if PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'EOF')):
                return var.get(u'extra').get(u'tokens')
                pass
            var.get(u'lex')()
            while PyJsStrictNeq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'EOF')):
                try:
                    var.get(u'lex')()
                    pass
                except PyJsException as PyJsTempException:
                    PyJsHolder_6c65784572726f72_26803432 = var.own.get(u'lexError')
                    var.force_own_put(u'lexError', PyExceptionToJs(PyJsTempException))
                    try:
                        if var.get(u'extra').get(u'errors'):
                            var.get(u'extra').get(u'errors').callprop(u'push',var.get(u'lexError'))
                            break
                            pass
                        else:
                            PyJsTempException = JsToPyException(var.get(u'lexError'))
                            raise PyJsTempException
                            pass
                        pass
                    finally:
                        if PyJsHolder_6c65784572726f72_26803432 is not None:
                            var.own[u'lexError'] = PyJsHolder_6c65784572726f72_26803432
                        else:
                            del var.own[u'lexError']
                        del PyJsHolder_6c65784572726f72_26803432
                pass
            var.get(u'filterTokenLocation')()
            var.put(u'tokens', var.get(u'extra').get(u'tokens'))
            if PyJsStrictNeq(var.get(u'extra').get(u'comments').typeof(),Js(u'undefined')):
                var.get(u'tokens').put(u'comments', var.get(u'extra').get(u'comments'))
                pass
            if PyJsStrictNeq(var.get(u'extra').get(u'errors').typeof(),Js(u'undefined')):
                var.get(u'tokens').put(u'errors', var.get(u'extra').get(u'errors'))
                pass
            pass
        except PyJsException as PyJsTempException:
            PyJsHolder_65_4166534 = var.own.get(u'e')
            var.force_own_put(u'e', PyExceptionToJs(PyJsTempException))
            try:
                PyJsTempException = JsToPyException(var.get(u'e'))
                raise PyJsTempException
                pass
            finally:
                if PyJsHolder_65_4166534 is not None:
                    var.own[u'e'] = PyJsHolder_65_4166534
                else:
                    del var.own[u'e']
                del PyJsHolder_65_4166534
        finally:
            PyJsLvalObject101_ = Js({})
            var.put(u'extra', PyJsLvalObject101_)
            pass
        return var.get(u'tokens')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'tokenize'
    var.put(u'tokenize', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'expr', u'startToken', u'expressions'])
        var.put(u'startToken', var.get(u'lookahead'))
        var.put(u'expr', var.get(u'parseAssignmentExpression')())
        if var.get(u'match')(Js(u',')):
            PyJsLvalArray23_ = Js([var.get(u'expr')])
            var.put(u'expressions', PyJsLvalArray23_)
            while (var.get(u'index')<var.get(u'length')):
                if var.get(u'match')(Js(u',')).neg():
                    break
                    pass
                var.get(u'lex')()
                var.get(u'expressions').callprop(u'push',var.get(u'parseAssignmentExpression')())
                pass
            var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishSequenceExpression',var.get(u'expressions')))
            pass
        return var.get(u'expr')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseExpression'
    var.put(u'parseExpression', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'token', u'node'])
        var.put(u'node', var.get(u'Node').create())
        var.put(u'token', var.get(u'lex')())
        if (PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'StringLiteral')) or PyJsStrictEq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'NumericLiteral'))):
            if (var.get(u'strict') and var.get(u'token').get(u'octal')):
                var.get(u'throwErrorTolerant')(var.get(u'token'),var.get(u'Messages').get(u'StrictOctalLiteral'))
                pass
            return var.get(u'node').callprop(u'finishLiteral',var.get(u'token'))
            pass
        return var.get(u'node').callprop(u'finishIdentifier',var.get(u'token').get(u'value'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseObjectPropertyKey'
    var.put(u'parseObjectPropertyKey', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(keyword, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'keyword':keyword}, var)
        var.registers([u'token'])
        var.put(u'token', var.get(u'lex')())
        if (PyJsStrictNeq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Keyword')) or PyJsStrictNeq(var.get(u'token').get(u'value'),var.get(u'keyword'))):
            var.get(u'throwUnexpected')(var.get(u'token'))
            pass
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'expectKeyword'
    var.put(u'expectKeyword', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(condition, message, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'condition':condition, u'message':message}, var)
        if var.get(u'condition').neg():
            PyJsTempException = JsToPyException(var.get(u'Error').create((Js(u'ASSERT: ')+var.get(u'message'))))
            raise PyJsTempException
            pass
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'assert'
    var.put(u'assert', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        if var.get(u'match')(Js(u'{')):
            return var.get(u'parseFunctionSourceElements')()
            pass
        return var.get(u'parseAssignmentExpression')()
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseConciseBody'
    var.put(u'parseConciseBody', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'expr', u'args', u'property', u'startToken', u'previousAllowIn'])
        var.put(u'previousAllowIn', var.get(u'state').get(u'allowIn'))
        var.put(u'startToken', var.get(u'lookahead'))
        var.get(u'state').put(u'allowIn', var.get(u'true'))
        var.put(u'expr', (var.get(u'parseNewExpression')() if var.put(u'expr', var.get(u'matchKeyword')(Js(u'new'))) else var.get(u'parsePrimaryExpression')()))
        #for JS loop
        while 1:
            if var.get(u'match')(Js(u'.')):
                var.put(u'property', var.get(u'parseNonComputedMember')())
                var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishMemberExpression',Js(u'.'),var.get(u'expr'),var.get(u'property')))
                pass
            elif var.get(u'match')(Js(u'(')):
                var.put(u'args', var.get(u'parseArguments')())
                var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishCallExpression',var.get(u'expr'),var.get(u'args')))
                pass
            elif var.get(u'match')(Js(u'[')):
                var.put(u'property', var.get(u'parseComputedMember')())
                var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishMemberExpression',Js(u'['),var.get(u'expr'),var.get(u'property')))
                pass
            else:
                break
                pass
            pass
            
        var.get(u'state').put(u'allowIn', var.get(u'previousAllowIn'))
        return var.get(u'expr')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseLeftHandSideExpressionAllowCall'
    var.put(u'parseLeftHandSideExpressionAllowCall', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'block', u'node'])
        var.put(u'node', var.get(u'Node').create())
        var.get(u'expect')(Js(u'{'))
        var.put(u'block', var.get(u'parseStatementList')())
        var.get(u'expect')(Js(u'}'))
        return var.get(u'node').callprop(u'finishBlockStatement',var.get(u'block'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseBlock'
    var.put(u'parseBlock', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(kind, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'kind':kind}, var)
        var.registers([u'declarations', u'node'])
        var.put(u'node', var.get(u'Node').create())
        var.get(u'expectKeyword')(var.get(u'kind'))
        var.put(u'declarations', var.get(u'parseVariableDeclarationList')(var.get(u'kind')))
        var.get(u'consumeSemicolon')()
        return var.get(u'node').callprop(u'finishVariableDeclaration',var.get(u'declarations'),var.get(u'kind'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseConstLetDeclaration'
    var.put(u'parseConstLetDeclaration', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(offset, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'offset':offset}, var)
        var.registers([u'start', u'loc', u'ch', u'comment'])
        pass
        var.put(u'start', (var.get(u'index')-var.get(u'offset')))
        PyJsLvalObject112_ = Js({u'line':var.get(u'lineNumber'),u'column':((var.get(u'index')-var.get(u'lineStart'))-var.get(u'offset'))})
        PyJsLvalObject10_ = Js({u'start':PyJsLvalObject112_})
        var.put(u'loc', PyJsLvalObject10_)
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').callprop(u'charCodeAt',var.get(u'index')))
            var.get(u'index').PreInc()
            if var.get(u'isLineTerminator')(var.get(u'ch')):
                if var.get(u'extra').get(u'comments'):
                    var.put(u'comment', var.get(u'source').callprop(u'slice',(var.get(u'start')+var.get(u'offset')),(var.get(u'index')-Js(1))))
                    PyJsLvalObject11_ = Js({u'line':var.get(u'lineNumber'),u'column':((var.get(u'index')-var.get(u'lineStart'))-Js(1))})
                    var.get(u'loc').put(u'end', PyJsLvalObject11_)
                    var.get(u'addComment')(Js(u'Line'),var.get(u'comment'),var.get(u'start'),(var.get(u'index')-Js(1)),var.get(u'loc'))
                    pass
                if (PyJsStrictEq(var.get(u'ch'),Js(13)) and PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt',var.get(u'index')),Js(10))):
                    var.get(u'index').PreInc()
                    pass
                var.get(u'lineNumber').PreInc()
                var.put(u'lineStart', var.get(u'index'))
                return var.get('undefined')
                pass
            pass
        if var.get(u'extra').get(u'comments'):
            var.put(u'comment', var.get(u'source').callprop(u'slice',(var.get(u'start')+var.get(u'offset')),var.get(u'index')))
            PyJsLvalObject12_ = Js({u'line':var.get(u'lineNumber'),u'column':(var.get(u'index')-var.get(u'lineStart'))})
            var.get(u'loc').put(u'end', PyJsLvalObject12_)
            var.get(u'addComment')(Js(u'Line'),var.get(u'comment'),var.get(u'start'),var.get(u'index'),var.get(u'loc'))
            pass
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'skipSingleLineComment'
    var.put(u'skipSingleLineComment', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(node, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'node':node}, var)
        var.registers([u'body', u'test', u'oldInIteration'])
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
            pass
        return var.get(u'node').callprop(u'finishDoWhileStatement',var.get(u'body'),var.get(u'test'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseDoWhileStatement'
    var.put(u'parseDoWhileStatement', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        if PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Keyword')):
            while 1:
                SWITCHED = False
                CONDITION = ((var.get(u'lookahead').get(u'value')))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'const')):
                    SWITCHED = True
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'let')):
                    return var.get(u'parseConstLetDeclaration')(var.get(u'lookahead').get(u'value'))
                    SWITCHED = True
                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'function')):
                    return var.get(u'parseFunctionDeclaration')()
                    SWITCHED = True
                if True:
                    return var.get(u'parseStatement')()
                    pass
                    SWITCHED = True
                break
            pass
        if PyJsStrictNeq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'EOF')):
            return var.get(u'parseStatement')()
            pass
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseSourceElement'
    var.put(u'parseSourceElement', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(prefix, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'prefix':prefix}, var)
        var.registers([u'i', u'len', u'ch', u'code'])
        var.put(u'code', Js(0))
        var.put(u'len', (Js(4) if var.put(u'len', (PyJsStrictEq(var.get(u'prefix'),Js(u'u')))) else Js(2)))
        #for JS loop
        var.put(u'i', Js(0))
        while (var.get(u'i')<var.get(u'len')):
            if ((var.get(u'index')<var.get(u'length')) and var.get(u'isHexDigit')(var.get(u'source').get(var.get(u'index')))):
                var.put(u'ch', var.get(u'source').get(var.get(u'index').PostInc()))
                var.put(u'code', ((var.get(u'code')*Js(16))+Js(u'0123456789abcdef').callprop(u'indexOf',var.get(u'ch').callprop(u'toLowerCase'))))
                pass
            else:
                return Js(u'')
                pass
            pass
            var.get(u'i').PreInc()
        
        return var.get(u'String').callprop(u'fromCharCode',var.get(u'code'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'scanHexEscape'
    var.put(u'scanHexEscape', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(ch, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'ch':ch}, var)
        return (Js(u'0123456789abcdefABCDEF').callprop(u'indexOf',var.get(u'ch'))>=Js(0))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'isHexDigit'
    var.put(u'isHexDigit', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(id, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'id':id}, var)
        while 1:
            SWITCHED = False
            CONDITION = ((var.get(u'id')))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'implements')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'interface')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'package')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'private')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'protected')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'public')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'static')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'yield')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'let')):
                return var.get(u'true')
                SWITCHED = True
            if True:
                return var.get(u'false')
                pass
                SWITCHED = True
            break
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'isStrictModeReservedWord'
    var.put(u'isStrictModeReservedWord', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(token, allowIn, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'token':token, u'allowIn':allowIn}, var)
        var.registers([u'prec'])
        var.put(u'prec', Js(0))
        if (PyJsStrictNeq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Punctuator')) and PyJsStrictNeq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Keyword'))):
            return Js(0)
            pass
        while 1:
            SWITCHED = False
            CONDITION = ((var.get(u'token').get(u'value')))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'||')):
                var.put(u'prec', Js(1))
                break
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'&&')):
                var.put(u'prec', Js(2))
                break
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'|')):
                var.put(u'prec', Js(3))
                break
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'^')):
                var.put(u'prec', Js(4))
                break
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'&')):
                var.put(u'prec', Js(5))
                break
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'==')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'!=')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'===')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'!==')):
                var.put(u'prec', Js(6))
                break
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'<')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'>')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'<=')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'>=')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'instanceof')):
                var.put(u'prec', Js(7))
                break
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'in')):
                var.put(u'prec', (Js(7) if var.put(u'prec', var.get(u'allowIn')) else Js(0)))
                break
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'<<')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'>>')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'>>>')):
                var.put(u'prec', Js(8))
                break
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'+')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'-')):
                var.put(u'prec', Js(9))
                break
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'*')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'/')):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'%')):
                var.put(u'prec', Js(11))
                break
                SWITCHED = True
            if True:
                break
                pass
                SWITCHED = True
            break
        return var.get(u'prec')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'binaryPrecedence'
    var.put(u'binaryPrecedence', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(code, options, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'code':code, u'options':options}, var)
        var.registers([u'program', u'toString'])
        pass
        var.put(u'toString', var.get(u'String'))
        if (PyJsStrictNeq(var.get(u'code',throw=False).typeof(),Js(u'string')) and (var.get(u'code').instanceof(var.get(u'String'))).neg()):
            var.put(u'code', var.get(u'toString')(var.get(u'code')))
            pass
        var.put(u'source', var.get(u'code'))
        var.put(u'index', Js(0))
        var.put(u'lineNumber', (Js(1) if var.put(u'lineNumber', ((var.get(u'source').get(u'length')>Js(0)))) else Js(0)))
        var.put(u'lineStart', Js(0))
        var.put(u'length', var.get(u'source').get(u'length'))
        var.put(u'lookahead', var.get(u'null'))
        PyJsLvalObject113_ = Js({})
        PyJsLvalObject102_ = Js({u'allowIn':var.get(u'true'),u'labelSet':PyJsLvalObject113_,u'parenthesisCount':Js(0),u'inFunctionBody':var.get(u'false'),u'inIteration':var.get(u'false'),u'inSwitch':var.get(u'false'),u'lastCommentStart':(-Js(1))})
        var.put(u'state', PyJsLvalObject102_)
        PyJsLvalObject103_ = Js({})
        var.put(u'extra', PyJsLvalObject103_)
        if PyJsStrictNeq(var.get(u'options',throw=False).typeof(),Js(u'undefined')):
            var.get(u'extra').put(u'range', ((PyJsStrictEq(var.get(u'options').get(u'range').typeof(),Js(u'boolean'))) and var.get(u'options').get(u'range')))
            var.get(u'extra').put(u'loc', ((PyJsStrictEq(var.get(u'options').get(u'loc').typeof(),Js(u'boolean'))) and var.get(u'options').get(u'loc')))
            var.get(u'extra').put(u'attachComment', ((PyJsStrictEq(var.get(u'options').get(u'attachComment').typeof(),Js(u'boolean'))) and var.get(u'options').get(u'attachComment')))
            if ((var.get(u'extra').get(u'loc') and PyJsStrictNeq(var.get(u'options').get(u'source'),var.get(u'null'))) and PyJsStrictNeq(var.get(u'options').get(u'source'),var.get(u'undefined'))):
                var.get(u'extra').put(u'source', var.get(u'toString')(var.get(u'options').get(u'source')))
                pass
            if (PyJsStrictEq(var.get(u'options').get(u'tokens').typeof(),Js(u'boolean')) and var.get(u'options').get(u'tokens')):
                PyJsLvalArray41_ = Js([None])
                var.get(u'extra').put(u'tokens', PyJsLvalArray41_)
                pass
            if (PyJsStrictEq(var.get(u'options').get(u'comment').typeof(),Js(u'boolean')) and var.get(u'options').get(u'comment')):
                PyJsLvalArray42_ = Js([None])
                var.get(u'extra').put(u'comments', PyJsLvalArray42_)
                pass
            if (PyJsStrictEq(var.get(u'options').get(u'tolerant').typeof(),Js(u'boolean')) and var.get(u'options').get(u'tolerant')):
                PyJsLvalArray43_ = Js([None])
                var.get(u'extra').put(u'errors', PyJsLvalArray43_)
                pass
            if var.get(u'extra').get(u'attachComment'):
                var.get(u'extra').put(u'range', var.get(u'true'))
                PyJsLvalArray44_ = Js([None])
                var.get(u'extra').put(u'comments', PyJsLvalArray44_)
                PyJsLvalArray45_ = Js([None])
                var.get(u'extra').put(u'bottomRightStack', PyJsLvalArray45_)
                PyJsLvalArray46_ = Js([None])
                var.get(u'extra').put(u'trailingComments', PyJsLvalArray46_)
                PyJsLvalArray47_ = Js([None])
                var.get(u'extra').put(u'leadingComments', PyJsLvalArray47_)
                pass
            pass
        try:
            var.put(u'program', var.get(u'parseProgram')())
            if PyJsStrictNeq(var.get(u'extra').get(u'comments').typeof(),Js(u'undefined')):
                var.get(u'program').put(u'comments', var.get(u'extra').get(u'comments'))
                pass
            if PyJsStrictNeq(var.get(u'extra').get(u'tokens').typeof(),Js(u'undefined')):
                var.get(u'filterTokenLocation')()
                var.get(u'program').put(u'tokens', var.get(u'extra').get(u'tokens'))
                pass
            if PyJsStrictNeq(var.get(u'extra').get(u'errors').typeof(),Js(u'undefined')):
                var.get(u'program').put(u'errors', var.get(u'extra').get(u'errors'))
                pass
            pass
        except PyJsException as PyJsTempException:
            PyJsHolder_65_61930624 = var.own.get(u'e')
            var.force_own_put(u'e', PyExceptionToJs(PyJsTempException))
            try:
                PyJsTempException = JsToPyException(var.get(u'e'))
                raise PyJsTempException
                pass
            finally:
                if PyJsHolder_65_61930624 is not None:
                    var.own[u'e'] = PyJsHolder_65_61930624
                else:
                    del var.own[u'e']
                del PyJsHolder_65_61930624
        finally:
            PyJsLvalObject104_ = Js({})
            var.put(u'extra', PyJsLvalObject104_)
            pass
        return var.get(u'program')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parse'
    var.put(u'parse', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'op'])
        pass
        if PyJsStrictNeq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Punctuator')):
            return var.get(u'false')
            pass
        var.put(u'op', var.get(u'lookahead').get(u'value'))
        return (((((((((((PyJsStrictEq(var.get(u'op'),Js(u'=')) or PyJsStrictEq(var.get(u'op'),Js(u'*='))) or PyJsStrictEq(var.get(u'op'),Js(u'/='))) or PyJsStrictEq(var.get(u'op'),Js(u'%='))) or PyJsStrictEq(var.get(u'op'),Js(u'+='))) or PyJsStrictEq(var.get(u'op'),Js(u'-='))) or PyJsStrictEq(var.get(u'op'),Js(u'<<='))) or PyJsStrictEq(var.get(u'op'),Js(u'>>='))) or PyJsStrictEq(var.get(u'op'),Js(u'>>>='))) or PyJsStrictEq(var.get(u'op'),Js(u'&='))) or PyJsStrictEq(var.get(u'op'),Js(u'^='))) or PyJsStrictEq(var.get(u'op'),Js(u'|=')))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'matchAssign'
    var.put(u'matchAssign', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(startToken, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'startToken':startToken}, var)
        if var.get(u'extra').get(u'range'):
            PyJsLvalArray6_ = Js([var.get(u'startToken').get(u'start'),Js(0)])
            var.get(u'this').put(u'range', PyJsLvalArray6_)
            pass
        if var.get(u'extra').get(u'loc'):
            var.get(u'this').put(u'loc', var.get(u'WrappingSourceLocation').create(var.get(u'startToken')))
            pass
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'WrappingNode'
    var.put(u'WrappingNode', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'start', u'ch'])
        pass
        var.put(u'start', var.get(u'index').PostInc())
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').callprop(u'charCodeAt',var.get(u'index')))
            if PyJsStrictEq(var.get(u'ch'),Js(0x5C)):
                var.put(u'index', var.get(u'start'))
                return var.get(u'getEscapedIdentifier')()
                pass
            if var.get(u'isIdentifierPart')(var.get(u'ch')):
                var.get(u'index').PreInc()
                pass
            else:
                break
                pass
            pass
        return var.get(u'source').callprop(u'slice',var.get(u'start'),var.get(u'index'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'getIdentifier'
    var.put(u'getIdentifier', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(id, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'id':id}, var)
        return (PyJsStrictEq(var.get(u'id'),Js(u'eval')) or PyJsStrictEq(var.get(u'id'),Js(u'arguments')))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'isRestrictedWord'
    var.put(u'isRestrictedWord', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'test', u'consequent', u'statement', u'node'])
        PyJsLvalArray26_ = Js([None])
        var.put(u'consequent', PyJsLvalArray26_)
        var.put(u'node', var.get(u'Node').create())
        if var.get(u'matchKeyword')(Js(u'default')):
            var.get(u'lex')()
            var.put(u'test', var.get(u'null'))
            pass
        else:
            var.get(u'expectKeyword')(Js(u'case'))
            var.put(u'test', var.get(u'parseExpression')())
            pass
        var.get(u'expect')(Js(u':'))
        while (var.get(u'index')<var.get(u'length')):
            if ((var.get(u'match')(Js(u'}')) or var.get(u'matchKeyword')(Js(u'default'))) or var.get(u'matchKeyword')(Js(u'case'))):
                break
                pass
            var.put(u'statement', var.get(u'parseStatement')())
            var.get(u'consequent').callprop(u'push',var.get(u'statement'))
            pass
        return var.get(u'node').callprop(u'finishSwitchCase',var.get(u'test'),var.get(u'consequent'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseSwitchCase'
    var.put(u'parseSwitchCase', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'id', u'params', u'defaults', u'body', u'token', u'stricted', u'tmp', u'firstRestricted', u'message', u'previousStrict', u'node'])
        PyJsLvalArray32_ = Js([None])
        var.put(u'params', PyJsLvalArray32_)
        PyJsLvalArray33_ = Js([None])
        var.put(u'defaults', PyJsLvalArray33_)
        var.put(u'node', var.get(u'Node').create())
        var.get(u'expectKeyword')(Js(u'function'))
        var.put(u'token', var.get(u'lookahead'))
        var.put(u'id', var.get(u'parseVariableIdentifier')())
        if var.get(u'strict'):
            if var.get(u'isRestrictedWord')(var.get(u'token').get(u'value')):
                var.get(u'throwErrorTolerant')(var.get(u'token'),var.get(u'Messages').get(u'StrictFunctionName'))
                pass
            pass
        else:
            if var.get(u'isRestrictedWord')(var.get(u'token').get(u'value')):
                var.put(u'firstRestricted', var.get(u'token'))
                var.put(u'message', var.get(u'Messages').get(u'StrictFunctionName'))
                pass
            elif var.get(u'isStrictModeReservedWord')(var.get(u'token').get(u'value')):
                var.put(u'firstRestricted', var.get(u'token'))
                var.put(u'message', var.get(u'Messages').get(u'StrictReservedWord'))
                pass
            pass
        var.put(u'tmp', var.get(u'parseParams')(var.get(u'firstRestricted')))
        var.put(u'params', var.get(u'tmp').get(u'params'))
        var.put(u'defaults', var.get(u'tmp').get(u'defaults'))
        var.put(u'stricted', var.get(u'tmp').get(u'stricted'))
        var.put(u'firstRestricted', var.get(u'tmp').get(u'firstRestricted'))
        if var.get(u'tmp').get(u'message'):
            var.put(u'message', var.get(u'tmp').get(u'message'))
            pass
        var.put(u'previousStrict', var.get(u'strict'))
        var.put(u'body', var.get(u'parseFunctionSourceElements')())
        if (var.get(u'strict') and var.get(u'firstRestricted')):
            var.get(u'throwError')(var.get(u'firstRestricted'),var.get(u'message'))
            pass
        if (var.get(u'strict') and var.get(u'stricted')):
            var.get(u'throwErrorTolerant')(var.get(u'stricted'),var.get(u'message'))
            pass
        var.put(u'strict', var.get(u'previousStrict'))
        return var.get(u'node').callprop(u'finishFunctionDeclaration',var.get(u'id'),var.get(u'params'),var.get(u'defaults'),var.get(u'body'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseFunctionDeclaration'
    var.put(u'parseFunctionDeclaration', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'expr', u'token', u'startToken'])
        var.put(u'startToken', var.get(u'lookahead'))
        var.put(u'expr', var.get(u'parseLeftHandSideExpressionAllowCall')())
        if PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Punctuator')):
            if (((var.get(u'match')(Js(u'++')) or var.get(u'match')(Js(u'--')))) and var.get(u'peekLineTerminator')().neg()):
                if ((var.get(u'strict') and PyJsStrictEq(var.get(u'expr').get(u'type'),var.get(u'Syntax').get(u'Identifier'))) and var.get(u'isRestrictedWord')(var.get(u'expr').get(u'name'))):
                    PyJsLvalObject68_ = Js({})
                    var.get(u'throwErrorTolerant')(PyJsLvalObject68_,var.get(u'Messages').get(u'StrictLHSPostfix'))
                    pass
                if var.get(u'isLeftHandSide')(var.get(u'expr')).neg():
                    PyJsLvalObject69_ = Js({})
                    var.get(u'throwErrorTolerant')(PyJsLvalObject69_,var.get(u'Messages').get(u'InvalidLHSInAssignment'))
                    pass
                var.put(u'token', var.get(u'lex')())
                var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishPostfixExpression',var.get(u'token').get(u'value'),var.get(u'expr')))
                pass
            pass
        return var.get(u'expr')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parsePostfixExpression'
    var.put(u'parsePostfixExpression', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.get(u'expect')(Js(u'.'))
        return var.get(u'parseNonComputedProperty')()
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseNonComputedMember'
    var.put(u'parseNonComputedMember', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'i', u'entry', u'token', u'tokens'])
        PyJsLvalArray37_ = Js([None])
        var.put(u'tokens', PyJsLvalArray37_)
        #for JS loop
        var.put(u'i', Js(0))
        while (var.get(u'i')<var.get(u'extra').get(u'tokens').get(u'length')):
            var.put(u'entry', var.get(u'extra').get(u'tokens').get(var.get(u'i')))
            PyJsLvalObject97_ = Js({u'type':var.get(u'entry').get(u'type'),u'value':var.get(u'entry').get(u'value')})
            var.put(u'token', PyJsLvalObject97_)
            if var.get(u'extra').get(u'range'):
                var.get(u'token').put(u'range', var.get(u'entry').get(u'range'))
                pass
            if var.get(u'extra').get(u'loc'):
                var.get(u'token').put(u'loc', var.get(u'entry').get(u'loc'))
                pass
            var.get(u'tokens').callprop(u'push',var.get(u'token'))
            pass
            var.get(u'i').PreInc()
        
        var.get(u'extra').put(u'tokens', var.get(u'tokens'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'filterTokenLocation'
    var.put(u'filterTokenLocation', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'pos', u'line', u'start', u'found'])
        pass
        var.put(u'pos', var.get(u'index'))
        var.put(u'line', var.get(u'lineNumber'))
        var.put(u'start', var.get(u'lineStart'))
        var.get(u'skipComment')()
        var.put(u'found', PyJsStrictNeq(var.get(u'lineNumber'),var.get(u'line')))
        var.put(u'index', var.get(u'pos'))
        var.put(u'lineNumber', var.get(u'line'))
        var.put(u'lineStart', var.get(u'start'))
        return var.get(u'found')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'peekLineTerminator'
    var.put(u'peekLineTerminator', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(param, first, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'param':param, u'first':first}, var)
        var.registers([u'previousStrict', u'body', u'node'])
        var.put(u'node', var.get(u'Node').create())
        var.put(u'previousStrict', var.get(u'strict'))
        var.put(u'body', var.get(u'parseFunctionSourceElements')())
        if ((var.get(u'first') and var.get(u'strict')) and var.get(u'isRestrictedWord')(var.get(u'param').get(Js(0)).get(u'name'))):
            var.get(u'throwErrorTolerant')(var.get(u'first'),var.get(u'Messages').get(u'StrictParamName'))
            pass
        var.put(u'strict', var.get(u'previousStrict'))
        PyJsLvalArray8_ = Js([None])
        return var.get(u'node').callprop(u'finishFunctionExpression',var.get(u'null'),var.get(u'param'),PyJsLvalArray8_,var.get(u'body'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parsePropertyFunction'
    var.put(u'parsePropertyFunction', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(expr, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'expr':expr}, var)
        return (PyJsStrictEq(var.get(u'expr').get(u'type'),var.get(u'Syntax').get(u'Identifier')) or PyJsStrictEq(var.get(u'expr').get(u'type'),var.get(u'Syntax').get(u'MemberExpression')))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'isLeftHandSide'
    var.put(u'isLeftHandSide', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'start', u'code', u'code2', u'ch1', u'ch2', u'ch3', u'ch4'])
        var.put(u'start', var.get(u'index'))
        var.put(u'code', var.get(u'source').callprop(u'charCodeAt',var.get(u'index')))
        var.put(u'ch1', var.get(u'source').get(var.get(u'index')))
        while 1:
            SWITCHED = False
            CONDITION = ((var.get(u'code')))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(0x2E)):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(0x28)):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(0x29)):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(0x3B)):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(0x2C)):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(0x7B)):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(0x7D)):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(0x5B)):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(0x5D)):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(0x3A)):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(0x3F)):
                SWITCHED = True
            if SWITCHED or PyJsStrictEq(CONDITION, Js(0x7E)):
                var.get(u'index').PreInc()
                if var.get(u'extra').get(u'tokenize'):
                    if PyJsStrictEq(var.get(u'code'),Js(0x28)):
                        var.get(u'extra').put(u'openParenToken', var.get(u'extra').get(u'tokens').get(u'length'))
                        pass
                    elif PyJsStrictEq(var.get(u'code'),Js(0x7B)):
                        var.get(u'extra').put(u'openCurlyToken', var.get(u'extra').get(u'tokens').get(u'length'))
                        pass
                    pass
                PyJsLvalObject24_ = Js({u'type':var.get(u'Token').get(u'Punctuator'),u'value':var.get(u'String').callprop(u'fromCharCode',var.get(u'code')),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
                return PyJsLvalObject24_
                SWITCHED = True
            if True:
                var.put(u'code2', var.get(u'source').callprop(u'charCodeAt',(var.get(u'index')+Js(1))))
                if PyJsStrictEq(var.get(u'code2'),Js(0x3D)):
                    while 1:
                        SWITCHED = False
                        CONDITION = ((var.get(u'code')))
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(0x2B)):
                            SWITCHED = True
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(0x2D)):
                            SWITCHED = True
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(0x2F)):
                            SWITCHED = True
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(0x3C)):
                            SWITCHED = True
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(0x3E)):
                            SWITCHED = True
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(0x5E)):
                            SWITCHED = True
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(0x7C)):
                            SWITCHED = True
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(0x25)):
                            SWITCHED = True
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(0x26)):
                            SWITCHED = True
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(0x2A)):
                            var.put(u'index', Js(2),u'+')
                            PyJsLvalObject25_ = Js({u'type':var.get(u'Token').get(u'Punctuator'),u'value':(var.get(u'String').callprop(u'fromCharCode',var.get(u'code'))+var.get(u'String').callprop(u'fromCharCode',var.get(u'code2'))),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
                            return PyJsLvalObject25_
                            SWITCHED = True
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(0x21)):
                            SWITCHED = True
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(0x3D)):
                            var.put(u'index', Js(2),u'+')
                            if PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt',var.get(u'index')),Js(0x3D)):
                                var.get(u'index').PreInc()
                                pass
                            PyJsLvalObject26_ = Js({u'type':var.get(u'Token').get(u'Punctuator'),u'value':var.get(u'source').callprop(u'slice',var.get(u'start'),var.get(u'index')),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
                            return PyJsLvalObject26_
                            pass
                            SWITCHED = True
                        break
                    pass
                pass
                SWITCHED = True
            break
        var.put(u'ch4', var.get(u'source').callprop(u'substr',var.get(u'index'),Js(4)))
        if PyJsStrictEq(var.get(u'ch4'),Js(u'>>>=')):
            var.put(u'index', Js(4),u'+')
            PyJsLvalObject27_ = Js({u'type':var.get(u'Token').get(u'Punctuator'),u'value':var.get(u'ch4'),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
            return PyJsLvalObject27_
            pass
        var.put(u'ch3', var.get(u'ch4').callprop(u'substr',Js(0),Js(3)))
        if ((PyJsStrictEq(var.get(u'ch3'),Js(u'>>>')) or PyJsStrictEq(var.get(u'ch3'),Js(u'<<='))) or PyJsStrictEq(var.get(u'ch3'),Js(u'>>='))):
            var.put(u'index', Js(3),u'+')
            PyJsLvalObject28_ = Js({u'type':var.get(u'Token').get(u'Punctuator'),u'value':var.get(u'ch3'),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
            return PyJsLvalObject28_
            pass
        var.put(u'ch2', var.get(u'ch3').callprop(u'substr',Js(0),Js(2)))
        if (((PyJsStrictEq(var.get(u'ch1'),var.get(u'ch2').get(Js(1))) and ((Js(u'+-<>&|').callprop(u'indexOf',var.get(u'ch1'))>=Js(0))))) or PyJsStrictEq(var.get(u'ch2'),Js(u'=>'))):
            var.put(u'index', Js(2),u'+')
            PyJsLvalObject29_ = Js({u'type':var.get(u'Token').get(u'Punctuator'),u'value':var.get(u'ch2'),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
            return PyJsLvalObject29_
            pass
        if (Js(u'<>=!+-*%&|^/').callprop(u'indexOf',var.get(u'ch1'))>=Js(0)):
            var.get(u'index').PreInc()
            PyJsLvalObject30_ = Js({u'type':var.get(u'Token').get(u'Punctuator'),u'value':var.get(u'ch1'),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
            return PyJsLvalObject30_
            pass
        PyJsLvalObject31_ = Js({})
        var.get(u'throwError')(PyJsLvalObject31_,var.get(u'Messages').get(u'UnexpectedToken'),Js(u'ILLEGAL'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'scanPunctuator'
    var.put(u'scanPunctuator', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(options, node, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'options':options, u'node':node}, var)
        var.registers([u'previousStrict', u'body'])
        pass
        var.get(u'expect')(Js(u'=>'))
        var.put(u'previousStrict', var.get(u'strict'))
        var.put(u'body', var.get(u'parseConciseBody')())
        if (var.get(u'strict') and var.get(u'options').get(u'firstRestricted')):
            var.get(u'throwError')(var.get(u'options').get(u'firstRestricted'),var.get(u'options').get(u'message'))
            pass
        if (var.get(u'strict') and var.get(u'options').get(u'stricted')):
            var.get(u'throwErrorTolerant')(var.get(u'options').get(u'stricted'),var.get(u'options').get(u'message'))
            pass
        var.put(u'strict', var.get(u'previousStrict'))
        return var.get(u'node').callprop(u'finishArrowFunctionExpression',var.get(u'options').get(u'params'),var.get(u'options').get(u'defaults'),var.get(u'body'),PyJsStrictNeq(var.get(u'body').get(u'type'),var.get(u'Syntax').get(u'BlockStatement')))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseArrowFunctionExpression'
    var.put(u'parseArrowFunctionExpression', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(token, messageFormat, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'token':token, u'messageFormat':messageFormat}, var)
        var.registers([u'error', u'args', u'msg'])
        var.put(u'args', var.get(u'Array').get(u'prototype').get(u'slice').callprop(u'call',var.get(u'arguments'),Js(2)))
        @Js
        def PyJsLvalInline4_(whole, index, this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments, u'whole':whole, u'index':index}, var)
            var.get(u'assert')((var.get(u'index')<var.get(u'args').get(u'length')),Js(u'Message reference must be in range'))
            return var.get(u'args').get(var.get(u'index'))
            pass
            pass
        var.put(u'msg', var.get(u'messageFormat').callprop(u'replace',JsRegExp('/%(\\d)/g'),PyJsLvalInline4_))
        if PyJsStrictEq(var.get(u'token').get(u'lineNumber').typeof(),Js(u'number')):
            var.put(u'error', var.get(u'Error').create((((Js(u'Line ')+var.get(u'token').get(u'lineNumber'))+Js(u': '))+var.get(u'msg'))))
            var.get(u'error').put(u'index', var.get(u'token').get(u'start'))
            var.get(u'error').put(u'lineNumber', var.get(u'token').get(u'lineNumber'))
            var.get(u'error').put(u'column', ((var.get(u'token').get(u'start')-var.get(u'lineStart'))+Js(1)))
            pass
        else:
            var.put(u'error', var.get(u'Error').create((((Js(u'Line ')+var.get(u'lineNumber'))+Js(u': '))+var.get(u'msg'))))
            var.get(u'error').put(u'index', var.get(u'index'))
            var.get(u'error').put(u'lineNumber', var.get(u'lineNumber'))
            var.get(u'error').put(u'column', ((var.get(u'index')-var.get(u'lineStart'))+Js(1)))
            pass
        var.get(u'error').put(u'description', var.get(u'msg'))
        PyJsTempException = JsToPyException(var.get(u'error'))
        raise PyJsTempException
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'throwError'
    var.put(u'throwError', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'ch', u'code', u'cu1', u'cu2'])
        pass
        var.put(u'ch', var.get(u'source').get(var.get(u'index')))
        var.put(u'code', Js(0))
        if PyJsStrictEq(var.get(u'ch'),Js(u'}')):
            PyJsLvalObject17_ = Js({})
            var.get(u'throwError')(PyJsLvalObject17_,var.get(u'Messages').get(u'UnexpectedToken'),Js(u'ILLEGAL'))
            pass
        while (var.get(u'index')<var.get(u'length')):
            var.put(u'ch', var.get(u'source').get(var.get(u'index').PostInc()))
            if var.get(u'isHexDigit')(var.get(u'ch')).neg():
                break
                pass
            var.put(u'code', ((var.get(u'code')*Js(16))+Js(u'0123456789abcdef').callprop(u'indexOf',var.get(u'ch').callprop(u'toLowerCase'))))
            pass
        if ((var.get(u'code')>Js(0x10FFFF)) or PyJsStrictNeq(var.get(u'ch'),Js(u'}'))):
            PyJsLvalObject18_ = Js({})
            var.get(u'throwError')(PyJsLvalObject18_,var.get(u'Messages').get(u'UnexpectedToken'),Js(u'ILLEGAL'))
            pass
        if (var.get(u'code')<=Js(0xFFFF)):
            return var.get(u'String').callprop(u'fromCharCode',var.get(u'code'))
            pass
        var.put(u'cu1', (((((var.get(u'code')-Js(0x10000)))>>Js(10)))+Js(0xD800)))
        var.put(u'cu2', (((((var.get(u'code')-Js(0x10000)))&Js(1023)))+Js(0xDC00)))
        return var.get(u'String').callprop(u'fromCharCode',var.get(u'cu1'),var.get(u'cu2'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'scanUnicodeCodePointEscape'
    var.put(u'scanUnicodeCodePointEscape', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'oldParenthesisCount', u'token', u'expr', u'right', u'list', u'startToken'])
        pass
        var.put(u'oldParenthesisCount', var.get(u'state').get(u'parenthesisCount'))
        var.put(u'startToken', var.get(u'lookahead'))
        var.put(u'token', var.get(u'lookahead'))
        var.put(u'expr', var.get(u'parseConditionalExpression')())
        if (PyJsStrictEq(var.get(u'expr'),var.get(u'PlaceHolders').get(u'ArrowParameterPlaceHolder')) or var.get(u'match')(Js(u'=>'))):
            if (PyJsStrictEq(var.get(u'state').get(u'parenthesisCount'),var.get(u'oldParenthesisCount')) or PyJsStrictEq(var.get(u'state').get(u'parenthesisCount'),((var.get(u'oldParenthesisCount')+Js(1))))):
                if PyJsStrictEq(var.get(u'expr').get(u'type'),var.get(u'Syntax').get(u'Identifier')):
                    PyJsLvalArray20_ = Js([var.get(u'expr')])
                    var.put(u'list', var.get(u'reinterpretAsCoverFormalsList')(PyJsLvalArray20_))
                    pass
                elif PyJsStrictEq(var.get(u'expr').get(u'type'),var.get(u'Syntax').get(u'AssignmentExpression')):
                    PyJsLvalArray21_ = Js([var.get(u'expr')])
                    var.put(u'list', var.get(u'reinterpretAsCoverFormalsList')(PyJsLvalArray21_))
                    pass
                elif PyJsStrictEq(var.get(u'expr').get(u'type'),var.get(u'Syntax').get(u'SequenceExpression')):
                    var.put(u'list', var.get(u'reinterpretAsCoverFormalsList')(var.get(u'expr').get(u'expressions')))
                    pass
                elif PyJsStrictEq(var.get(u'expr'),var.get(u'PlaceHolders').get(u'ArrowParameterPlaceHolder')):
                    PyJsLvalArray22_ = Js([None])
                    var.put(u'list', var.get(u'reinterpretAsCoverFormalsList')(PyJsLvalArray22_))
                    pass
                if var.get(u'list'):
                    return var.get(u'parseArrowFunctionExpression')(var.get(u'list'),var.get(u'WrappingNode').create(var.get(u'startToken')))
                    pass
                pass
            pass
        if var.get(u'matchAssign')():
            if var.get(u'isLeftHandSide')(var.get(u'expr')).neg():
                PyJsLvalObject75_ = Js({})
                var.get(u'throwErrorTolerant')(PyJsLvalObject75_,var.get(u'Messages').get(u'InvalidLHSInAssignment'))
                pass
            if ((var.get(u'strict') and PyJsStrictEq(var.get(u'expr').get(u'type'),var.get(u'Syntax').get(u'Identifier'))) and var.get(u'isRestrictedWord')(var.get(u'expr').get(u'name'))):
                var.get(u'throwErrorTolerant')(var.get(u'token'),var.get(u'Messages').get(u'StrictLHSAssignment'))
                pass
            var.put(u'token', var.get(u'lex')())
            var.put(u'right', var.get(u'parseAssignmentExpression')())
            var.put(u'expr', var.get(u'WrappingNode').create(var.get(u'startToken')).callprop(u'finishAssignmentExpression',var.get(u'token').get(u'value'),var.get(u'expr'),var.get(u'right')))
            pass
        return var.get(u'expr')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseAssignmentExpression'
    var.put(u'parseAssignmentExpression', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'start', u'body', u'flags', u'value'])
        pass
        var.put(u'lookahead', var.get(u'null'))
        var.get(u'skipComment')()
        var.put(u'start', var.get(u'index'))
        var.put(u'body', var.get(u'scanRegExpBody')())
        var.put(u'flags', var.get(u'scanRegExpFlags')())
        var.put(u'value', var.get(u'testRegExp')(var.get(u'body').get(u'value'),var.get(u'flags').get(u'value')))
        if var.get(u'extra').get(u'tokenize'):
            PyJsLvalObject51_ = Js({u'type':var.get(u'Token').get(u'RegularExpression'),u'value':var.get(u'value'),u'lineNumber':var.get(u'lineNumber'),u'lineStart':var.get(u'lineStart'),u'start':var.get(u'start'),u'end':var.get(u'index')})
            return PyJsLvalObject51_
            pass
        PyJsLvalObject52_ = Js({u'literal':(var.get(u'body').get(u'literal')+var.get(u'flags').get(u'literal')),u'value':var.get(u'value'),u'start':var.get(u'start'),u'end':var.get(u'index')})
        return PyJsLvalObject52_
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'scanRegExp'
    var.put(u'scanRegExp', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'token', u'node'])
        var.put(u'node', var.get(u'Node').create())
        var.put(u'token', var.get(u'lex')())
        if PyJsStrictNeq(var.get(u'token').get(u'type'),var.get(u'Token').get(u'Identifier')):
            var.get(u'throwUnexpected')(var.get(u'token'))
            pass
        return var.get(u'node').callprop(u'finishIdentifier',var.get(u'token').get(u'value'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseVariableIdentifier'
    var.put(u'parseVariableIdentifier', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(node, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'node':node}, var)
        var.registers([u'init', u'test', u'update', u'left', u'right', u'body', u'oldInIteration', u'previousAllowIn'])
        var.put(u'previousAllowIn', var.get(u'state').get(u'allowIn'))
        var.put(u'init', var.put(u'test', var.put(u'update', var.get(u'null'))))
        var.get(u'expectKeyword')(Js(u'for'))
        var.get(u'expect')(Js(u'('))
        if var.get(u'match')(Js(u';')):
            var.get(u'lex')()
            pass
        else:
            if (var.get(u'matchKeyword')(Js(u'var')) or var.get(u'matchKeyword')(Js(u'let'))):
                var.get(u'state').put(u'allowIn', var.get(u'false'))
                var.put(u'init', var.get(u'parseForVariableDeclaration')())
                var.get(u'state').put(u'allowIn', var.get(u'previousAllowIn'))
                if (PyJsStrictEq(var.get(u'init').get(u'declarations').get(u'length'),Js(1)) and var.get(u'matchKeyword')(Js(u'in'))):
                    var.get(u'lex')()
                    var.put(u'left', var.get(u'init'))
                    var.put(u'right', var.get(u'parseExpression')())
                    var.put(u'init', var.get(u'null'))
                    pass
                pass
            else:
                var.get(u'state').put(u'allowIn', var.get(u'false'))
                var.put(u'init', var.get(u'parseExpression')())
                var.get(u'state').put(u'allowIn', var.get(u'previousAllowIn'))
                if var.get(u'matchKeyword')(Js(u'in')):
                    if var.get(u'isLeftHandSide')(var.get(u'init')).neg():
                        PyJsLvalObject77_ = Js({})
                        var.get(u'throwErrorTolerant')(PyJsLvalObject77_,var.get(u'Messages').get(u'InvalidLHSInForIn'))
                        pass
                    var.get(u'lex')()
                    var.put(u'left', var.get(u'init'))
                    var.put(u'right', var.get(u'parseExpression')())
                    var.put(u'init', var.get(u'null'))
                    pass
                pass
            if PyJsStrictEq(var.get(u'left',throw=False).typeof(),Js(u'undefined')):
                var.get(u'expect')(Js(u';'))
                pass
            pass
        if PyJsStrictEq(var.get(u'left',throw=False).typeof(),Js(u'undefined')):
            if var.get(u'match')(Js(u';')).neg():
                var.put(u'test', var.get(u'parseExpression')())
                pass
            var.get(u'expect')(Js(u';'))
            if var.get(u'match')(Js(u')')).neg():
                var.put(u'update', var.get(u'parseExpression')())
                pass
            pass
        var.get(u'expect')(Js(u')'))
        var.put(u'oldInIteration', var.get(u'state').get(u'inIteration'))
        var.get(u'state').put(u'inIteration', var.get(u'true'))
        var.put(u'body', var.get(u'parseStatement')())
        var.get(u'state').put(u'inIteration', var.get(u'oldInIteration'))
        return (var.get(u'node').callprop(u'finishForStatement',var.get(u'init'),var.get(u'test'),var.get(u'update'),var.get(u'body')) if (PyJsStrictEq(var.get(u'left',throw=False).typeof(),Js(u'undefined'))) else var.get(u'node').callprop(u'finishForInStatement',var.get(u'left'),var.get(u'right'),var.get(u'body')))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseForStatement'
    var.put(u'parseForStatement', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(ch, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'ch':ch}, var)
        return (((((((PyJsStrictEq(var.get(u'ch'),Js(0x24))) or (PyJsStrictEq(var.get(u'ch'),Js(0x5F)))) or (((var.get(u'ch')>=Js(0x41)) and (var.get(u'ch')<=Js(0x5A))))) or (((var.get(u'ch')>=Js(0x61)) and (var.get(u'ch')<=Js(0x7A))))) or (((var.get(u'ch')>=Js(0x30)) and (var.get(u'ch')<=Js(0x39))))) or (PyJsStrictEq(var.get(u'ch'),Js(0x5C)))) or ((((var.get(u'ch')>=Js(0x80))) and var.get(u'Regex').get(u'NonAsciiIdentifierPart').callprop(u'test',var.get(u'String').callprop(u'fromCharCode',var.get(u'ch'))))))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'isIdentifierPart'
    var.put(u'isIdentifierPart', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(keyword, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'keyword':keyword}, var)
        return (PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Keyword')) and PyJsStrictEq(var.get(u'lookahead').get(u'value'),var.get(u'keyword')))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'matchKeyword'
    var.put(u'matchKeyword', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(node, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'node':node}, var)
        var.registers([u'block', u'handlers', u'finalizer'])
        PyJsLvalArray28_ = Js([None])
        var.put(u'handlers', PyJsLvalArray28_)
        var.put(u'finalizer', var.get(u'null'))
        var.get(u'expectKeyword')(Js(u'try'))
        var.put(u'block', var.get(u'parseBlock')())
        if var.get(u'matchKeyword')(Js(u'catch')):
            var.get(u'handlers').callprop(u'push',var.get(u'parseCatchClause')())
            pass
        if var.get(u'matchKeyword')(Js(u'finally')):
            var.get(u'lex')()
            var.put(u'finalizer', var.get(u'parseBlock')())
            pass
        if (PyJsStrictEq(var.get(u'handlers').get(u'length'),Js(0)) and var.get(u'finalizer').neg()):
            PyJsLvalObject91_ = Js({})
            var.get(u'throwError')(PyJsLvalObject91_,var.get(u'Messages').get(u'NoCatchOrFinally'))
            pass
        PyJsLvalArray29_ = Js([None])
        return var.get(u'node').callprop(u'finishTryStatement',var.get(u'block'),PyJsLvalArray29_,var.get(u'handlers'),var.get(u'finalizer'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseTryStatement'
    var.put(u'parseTryStatement', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'expr'])
        pass
        var.get(u'expect')(Js(u'['))
        var.put(u'expr', var.get(u'parseExpression')())
        var.get(u'expect')(Js(u']'))
        return var.get(u'expr')
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseComputedMember'
    var.put(u'parseComputedMember', PyJsLvalTempHoisted)
    @Js
    def PyJsLvalTempHoisted(node, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'node':node}, var)
        var.registers([u'label', u'key'])
        var.put(u'label', var.get(u'null'))
        var.get(u'expectKeyword')(Js(u'continue'))
        if PyJsStrictEq(var.get(u'source').callprop(u'charCodeAt',var.get(u'index')),Js(0x3B)):
            var.get(u'lex')()
            if var.get(u'state').get(u'inIteration').neg():
                PyJsLvalObject78_ = Js({})
                var.get(u'throwError')(PyJsLvalObject78_,var.get(u'Messages').get(u'IllegalContinue'))
                pass
            return var.get(u'node').callprop(u'finishContinueStatement',var.get(u'null'))
            pass
        if var.get(u'peekLineTerminator')():
            if var.get(u'state').get(u'inIteration').neg():
                PyJsLvalObject79_ = Js({})
                var.get(u'throwError')(PyJsLvalObject79_,var.get(u'Messages').get(u'IllegalContinue'))
                pass
            return var.get(u'node').callprop(u'finishContinueStatement',var.get(u'null'))
            pass
        if PyJsStrictEq(var.get(u'lookahead').get(u'type'),var.get(u'Token').get(u'Identifier')):
            var.put(u'label', var.get(u'parseVariableIdentifier')())
            var.put(u'key', (Js(u'$')+var.get(u'label').get(u'name')))
            if var.get(u'Object').get(u'prototype').get(u'hasOwnProperty').callprop(u'call',var.get(u'state').get(u'labelSet'),var.get(u'key')).neg():
                PyJsLvalObject80_ = Js({})
                var.get(u'throwError')(PyJsLvalObject80_,var.get(u'Messages').get(u'UnknownLabel'),var.get(u'label').get(u'name'))
                pass
            pass
        var.get(u'consumeSemicolon')()
        if (PyJsStrictEq(var.get(u'label'),var.get(u'null')) and var.get(u'state').get(u'inIteration').neg()):
            PyJsLvalObject81_ = Js({})
            var.get(u'throwError')(PyJsLvalObject81_,var.get(u'Messages').get(u'IllegalContinue'))
            pass
        return var.get(u'node').callprop(u'finishContinueStatement',var.get(u'label'))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'parseContinueStatement'
    var.put(u'parseContinueStatement', PyJsLvalTempHoisted)
    Js(u'use strict')
    pass
    PyJsLvalObject2_ = Js({u'BooleanLiteral':Js(1),u'EOF':Js(2),u'Identifier':Js(3),u'Keyword':Js(4),u'NullLiteral':Js(5),u'NumericLiteral':Js(6),u'Punctuator':Js(7),u'StringLiteral':Js(8),u'RegularExpression':Js(9)})
    var.put(u'Token', PyJsLvalObject2_)
    PyJsLvalObject3_ = Js({})
    var.put(u'TokenName', PyJsLvalObject3_)
    var.get(u'TokenName').put(var.get(u'Token').get(u'BooleanLiteral'), Js(u'Boolean'))
    var.get(u'TokenName').put(var.get(u'Token').get(u'EOF'), Js(u'<end>'))
    var.get(u'TokenName').put(var.get(u'Token').get(u'Identifier'), Js(u'Identifier'))
    var.get(u'TokenName').put(var.get(u'Token').get(u'Keyword'), Js(u'Keyword'))
    var.get(u'TokenName').put(var.get(u'Token').get(u'NullLiteral'), Js(u'Null'))
    var.get(u'TokenName').put(var.get(u'Token').get(u'NumericLiteral'), Js(u'Numeric'))
    var.get(u'TokenName').put(var.get(u'Token').get(u'Punctuator'), Js(u'Punctuator'))
    var.get(u'TokenName').put(var.get(u'Token').get(u'StringLiteral'), Js(u'String'))
    var.get(u'TokenName').put(var.get(u'Token').get(u'RegularExpression'), Js(u'RegularExpression'))
    PyJsLvalArray2_ = Js([Js(u'('),Js(u'{'),Js(u'['),Js(u'in'),Js(u'typeof'),Js(u'instanceof'),Js(u'new'),Js(u'return'),Js(u'case'),Js(u'delete'),Js(u'throw'),Js(u'void'),Js(u'='),Js(u'+='),Js(u'-='),Js(u'*='),Js(u'/='),Js(u'%='),Js(u'<<='),Js(u'>>='),Js(u'>>>='),Js(u'&='),Js(u'|='),Js(u'^='),Js(u','),Js(u'+'),Js(u'-'),Js(u'*'),Js(u'/'),Js(u'%'),Js(u'++'),Js(u'--'),Js(u'<<'),Js(u'>>'),Js(u'>>>'),Js(u'&'),Js(u'|'),Js(u'^'),Js(u'!'),Js(u'~'),Js(u'&&'),Js(u'||'),Js(u'?'),Js(u':'),Js(u'==='),Js(u'=='),Js(u'>='),Js(u'<='),Js(u'<'),Js(u'>'),Js(u'!='),Js(u'!==')])
    var.put(u'FnExprTokens', PyJsLvalArray2_)
    PyJsLvalObject4_ = Js({u'AssignmentExpression':Js(u'AssignmentExpression'),u'ArrayExpression':Js(u'ArrayExpression'),u'ArrowFunctionExpression':Js(u'ArrowFunctionExpression'),u'BlockStatement':Js(u'BlockStatement'),u'BinaryExpression':Js(u'BinaryExpression'),u'BreakStatement':Js(u'BreakStatement'),u'CallExpression':Js(u'CallExpression'),u'CatchClause':Js(u'CatchClause'),u'ConditionalExpression':Js(u'ConditionalExpression'),u'ContinueStatement':Js(u'ContinueStatement'),u'DoWhileStatement':Js(u'DoWhileStatement'),u'DebuggerStatement':Js(u'DebuggerStatement'),u'EmptyStatement':Js(u'EmptyStatement'),u'ExpressionStatement':Js(u'ExpressionStatement'),u'ForStatement':Js(u'ForStatement'),u'ForInStatement':Js(u'ForInStatement'),u'FunctionDeclaration':Js(u'FunctionDeclaration'),u'FunctionExpression':Js(u'FunctionExpression'),u'Identifier':Js(u'Identifier'),u'IfStatement':Js(u'IfStatement'),u'Literal':Js(u'Literal'),u'LabeledStatement':Js(u'LabeledStatement'),u'LogicalExpression':Js(u'LogicalExpression'),u'MemberExpression':Js(u'MemberExpression'),u'NewExpression':Js(u'NewExpression'),u'ObjectExpression':Js(u'ObjectExpression'),u'Program':Js(u'Program'),u'Property':Js(u'Property'),u'ReturnStatement':Js(u'ReturnStatement'),u'SequenceExpression':Js(u'SequenceExpression'),u'SwitchStatement':Js(u'SwitchStatement'),u'SwitchCase':Js(u'SwitchCase'),u'ThisExpression':Js(u'ThisExpression'),u'ThrowStatement':Js(u'ThrowStatement'),u'TryStatement':Js(u'TryStatement'),u'UnaryExpression':Js(u'UnaryExpression'),u'UpdateExpression':Js(u'UpdateExpression'),u'VariableDeclaration':Js(u'VariableDeclaration'),u'VariableDeclarator':Js(u'VariableDeclarator'),u'WhileStatement':Js(u'WhileStatement'),u'WithStatement':Js(u'WithStatement')})
    var.put(u'Syntax', PyJsLvalObject4_)
    PyJsLvalObject111_ = Js({u'type':Js(u'ArrowParameterPlaceHolder')})
    PyJsLvalObject5_ = Js({u'ArrowParameterPlaceHolder':PyJsLvalObject111_})
    var.put(u'PlaceHolders', PyJsLvalObject5_)
    PyJsLvalObject6_ = Js({u'Data':Js(1),u'Get':Js(2),u'Set':Js(4)})
    var.put(u'PropertyKind', PyJsLvalObject6_)
    PyJsLvalObject7_ = Js({u'UnexpectedToken':Js(u'Unexpected token %0'),u'UnexpectedNumber':Js(u'Unexpected number'),u'UnexpectedString':Js(u'Unexpected string'),u'UnexpectedIdentifier':Js(u'Unexpected identifier'),u'UnexpectedReserved':Js(u'Unexpected reserved word'),u'UnexpectedEOS':Js(u'Unexpected end of input'),u'NewlineAfterThrow':Js(u'Illegal newline after throw'),u'InvalidRegExp':Js(u'Invalid regular expression'),u'UnterminatedRegExp':Js(u'Invalid regular expression: missing /'),u'InvalidLHSInAssignment':Js(u'Invalid left-hand side in assignment'),u'InvalidLHSInForIn':Js(u'Invalid left-hand side in for-in'),u'MultipleDefaultsInSwitch':Js(u'More than one default clause in switch statement'),u'NoCatchOrFinally':Js(u'Missing catch or finally after try'),u'UnknownLabel':Js(u'Undefined label \'%0\''),u'Redeclaration':Js(u'%0 \'%1\' has already been declared'),u'IllegalContinue':Js(u'Illegal continue statement'),u'IllegalBreak':Js(u'Illegal break statement'),u'IllegalReturn':Js(u'Illegal return statement'),u'StrictModeWith':Js(u'Strict mode code may not include a with statement'),u'StrictCatchVariable':Js(u'Catch variable may not be eval or arguments in strict mode'),u'StrictVarName':Js(u'Variable name may not be eval or arguments in strict mode'),u'StrictParamName':Js(u'Parameter name eval or arguments is not allowed in strict mode'),u'StrictParamDupe':Js(u'Strict mode function may not have duplicate parameter names'),u'StrictFunctionName':Js(u'Function name may not be eval or arguments in strict mode'),u'StrictOctalLiteral':Js(u'Octal literals are not allowed in strict mode.'),u'StrictDelete':Js(u'Delete of an unqualified identifier in strict mode.'),u'StrictDuplicateProperty':Js(u'Duplicate data property in object literal not allowed in strict mode'),u'AccessorDataProperty':Js(u'Object literal may not have data and accessor property with the same name'),u'AccessorGetSet':Js(u'Object literal may not have multiple get/set accessors with the same name'),u'StrictLHSAssignment':Js(u'Assignment to eval or arguments is not allowed in strict mode'),u'StrictLHSPostfix':Js(u'Postfix increment/decrement may not have eval or arguments operand in strict mode'),u'StrictLHSPrefix':Js(u'Prefix increment/decrement may not have eval or arguments operand in strict mode'),u'StrictReservedWord':Js(u'Use of future reserved word in strict mode')})
    var.put(u'Messages', PyJsLvalObject7_)
    PyJsLvalObject8_ = Js({u'NonAsciiIdentifierStart':var.get(u'RegExp').create(Js(u'[\xAA\xB5\xBA\xC0-\xD6\xD8-\xF6\xF8-\u02C1\u02C6-\u02D1\u02E0-\u02E4\u02EC\u02EE\u0370-\u0374\u0376\u0377\u037A-\u037D\u037F\u0386\u0388-\u038A\u038C\u038E-\u03A1\u03A3-\u03F5\u03F7-\u0481\u048A-\u052F\u0531-\u0556\u0559\u0561-\u0587\u05D0-\u05EA\u05F0-\u05F2\u0620-\u064A\u066E\u066F\u0671-\u06D3\u06D5\u06E5\u06E6\u06EE\u06EF\u06FA-\u06FC\u06FF\u0710\u0712-\u072F\u074D-\u07A5\u07B1\u07CA-\u07EA\u07F4\u07F5\u07FA\u0800-\u0815\u081A\u0824\u0828\u0840-\u0858\u08A0-\u08B2\u0904-\u0939\u093D\u0950\u0958-\u0961\u0971-\u0980\u0985-\u098C\u098F\u0990\u0993-\u09A8\u09AA-\u09B0\u09B2\u09B6-\u09B9\u09BD\u09CE\u09DC\u09DD\u09DF-\u09E1\u09F0\u09F1\u0A05-\u0A0A\u0A0F\u0A10\u0A13-\u0A28\u0A2A-\u0A30\u0A32\u0A33\u0A35\u0A36\u0A38\u0A39\u0A59-\u0A5C\u0A5E\u0A72-\u0A74\u0A85-\u0A8D\u0A8F-\u0A91\u0A93-\u0AA8\u0AAA-\u0AB0\u0AB2\u0AB3\u0AB5-\u0AB9\u0ABD\u0AD0\u0AE0\u0AE1\u0B05-\u0B0C\u0B0F\u0B10\u0B13-\u0B28\u0B2A-\u0B30\u0B32\u0B33\u0B35-\u0B39\u0B3D\u0B5C\u0B5D\u0B5F-\u0B61\u0B71\u0B83\u0B85-\u0B8A\u0B8E-\u0B90\u0B92-\u0B95\u0B99\u0B9A\u0B9C\u0B9E\u0B9F\u0BA3\u0BA4\u0BA8-\u0BAA\u0BAE-\u0BB9\u0BD0\u0C05-\u0C0C\u0C0E-\u0C10\u0C12-\u0C28\u0C2A-\u0C39\u0C3D\u0C58\u0C59\u0C60\u0C61\u0C85-\u0C8C\u0C8E-\u0C90\u0C92-\u0CA8\u0CAA-\u0CB3\u0CB5-\u0CB9\u0CBD\u0CDE\u0CE0\u0CE1\u0CF1\u0CF2\u0D05-\u0D0C\u0D0E-\u0D10\u0D12-\u0D3A\u0D3D\u0D4E\u0D60\u0D61\u0D7A-\u0D7F\u0D85-\u0D96\u0D9A-\u0DB1\u0DB3-\u0DBB\u0DBD\u0DC0-\u0DC6\u0E01-\u0E30\u0E32\u0E33\u0E40-\u0E46\u0E81\u0E82\u0E84\u0E87\u0E88\u0E8A\u0E8D\u0E94-\u0E97\u0E99-\u0E9F\u0EA1-\u0EA3\u0EA5\u0EA7\u0EAA\u0EAB\u0EAD-\u0EB0\u0EB2\u0EB3\u0EBD\u0EC0-\u0EC4\u0EC6\u0EDC-\u0EDF\u0F00\u0F40-\u0F47\u0F49-\u0F6C\u0F88-\u0F8C\u1000-\u102A\u103F\u1050-\u1055\u105A-\u105D\u1061\u1065\u1066\u106E-\u1070\u1075-\u1081\u108E\u10A0-\u10C5\u10C7\u10CD\u10D0-\u10FA\u10FC-\u1248\u124A-\u124D\u1250-\u1256\u1258\u125A-\u125D\u1260-\u1288\u128A-\u128D\u1290-\u12B0\u12B2-\u12B5\u12B8-\u12BE\u12C0\u12C2-\u12C5\u12C8-\u12D6\u12D8-\u1310\u1312-\u1315\u1318-\u135A\u1380-\u138F\u13A0-\u13F4\u1401-\u166C\u166F-\u167F\u1681-\u169A\u16A0-\u16EA\u16EE-\u16F8\u1700-\u170C\u170E-\u1711\u1720-\u1731\u1740-\u1751\u1760-\u176C\u176E-\u1770\u1780-\u17B3\u17D7\u17DC\u1820-\u1877\u1880-\u18A8\u18AA\u18B0-\u18F5\u1900-\u191E\u1950-\u196D\u1970-\u1974\u1980-\u19AB\u19C1-\u19C7\u1A00-\u1A16\u1A20-\u1A54\u1AA7\u1B05-\u1B33\u1B45-\u1B4B\u1B83-\u1BA0\u1BAE\u1BAF\u1BBA-\u1BE5\u1C00-\u1C23\u1C4D-\u1C4F\u1C5A-\u1C7D\u1CE9-\u1CEC\u1CEE-\u1CF1\u1CF5\u1CF6\u1D00-\u1DBF\u1E00-\u1F15\u1F18-\u1F1D\u1F20-\u1F45\u1F48-\u1F4D\u1F50-\u1F57\u1F59\u1F5B\u1F5D\u1F5F-\u1F7D\u1F80-\u1FB4\u1FB6-\u1FBC\u1FBE\u1FC2-\u1FC4\u1FC6-\u1FCC\u1FD0-\u1FD3\u1FD6-\u1FDB\u1FE0-\u1FEC\u1FF2-\u1FF4\u1FF6-\u1FFC\u2071\u207F\u2090-\u209C\u2102\u2107\u210A-\u2113\u2115\u2119-\u211D\u2124\u2126\u2128\u212A-\u212D\u212F-\u2139\u213C-\u213F\u2145-\u2149\u214E\u2160-\u2188\u2C00-\u2C2E\u2C30-\u2C5E\u2C60-\u2CE4\u2CEB-\u2CEE\u2CF2\u2CF3\u2D00-\u2D25\u2D27\u2D2D\u2D30-\u2D67\u2D6F\u2D80-\u2D96\u2DA0-\u2DA6\u2DA8-\u2DAE\u2DB0-\u2DB6\u2DB8-\u2DBE\u2DC0-\u2DC6\u2DC8-\u2DCE\u2DD0-\u2DD6\u2DD8-\u2DDE\u2E2F\u3005-\u3007\u3021-\u3029\u3031-\u3035\u3038-\u303C\u3041-\u3096\u309D-\u309F\u30A1-\u30FA\u30FC-\u30FF\u3105-\u312D\u3131-\u318E\u31A0-\u31BA\u31F0-\u31FF\u3400-\u4DB5\u4E00-\u9FCC\uA000-\uA48C\uA4D0-\uA4FD\uA500-\uA60C\uA610-\uA61F\uA62A\uA62B\uA640-\uA66E\uA67F-\uA69D\uA6A0-\uA6EF\uA717-\uA71F\uA722-\uA788\uA78B-\uA78E\uA790-\uA7AD\uA7B0\uA7B1\uA7F7-\uA801\uA803-\uA805\uA807-\uA80A\uA80C-\uA822\uA840-\uA873\uA882-\uA8B3\uA8F2-\uA8F7\uA8FB\uA90A-\uA925\uA930-\uA946\uA960-\uA97C\uA984-\uA9B2\uA9CF\uA9E0-\uA9E4\uA9E6-\uA9EF\uA9FA-\uA9FE\uAA00-\uAA28\uAA40-\uAA42\uAA44-\uAA4B\uAA60-\uAA76\uAA7A\uAA7E-\uAAAF\uAAB1\uAAB5\uAAB6\uAAB9-\uAABD\uAAC0\uAAC2\uAADB-\uAADD\uAAE0-\uAAEA\uAAF2-\uAAF4\uAB01-\uAB06\uAB09-\uAB0E\uAB11-\uAB16\uAB20-\uAB26\uAB28-\uAB2E\uAB30-\uAB5A\uAB5C-\uAB5F\uAB64\uAB65\uABC0-\uABE2\uAC00-\uD7A3\uD7B0-\uD7C6\uD7CB-\uD7FB\uF900-\uFA6D\uFA70-\uFAD9\uFB00-\uFB06\uFB13-\uFB17\uFB1D\uFB1F-\uFB28\uFB2A-\uFB36\uFB38-\uFB3C\uFB3E\uFB40\uFB41\uFB43\uFB44\uFB46-\uFBB1\uFBD3-\uFD3D\uFD50-\uFD8F\uFD92-\uFDC7\uFDF0-\uFDFB\uFE70-\uFE74\uFE76-\uFEFC\uFF21-\uFF3A\uFF41-\uFF5A\uFF66-\uFFBE\uFFC2-\uFFC7\uFFCA-\uFFCF\uFFD2-\uFFD7\uFFDA-\uFFDC]')),u'NonAsciiIdentifierPart':var.get(u'RegExp').create(Js(u'[\xAA\xB5\xBA\xC0-\xD6\xD8-\xF6\xF8-\u02C1\u02C6-\u02D1\u02E0-\u02E4\u02EC\u02EE\u0300-\u0374\u0376\u0377\u037A-\u037D\u037F\u0386\u0388-\u038A\u038C\u038E-\u03A1\u03A3-\u03F5\u03F7-\u0481\u0483-\u0487\u048A-\u052F\u0531-\u0556\u0559\u0561-\u0587\u0591-\u05BD\u05BF\u05C1\u05C2\u05C4\u05C5\u05C7\u05D0-\u05EA\u05F0-\u05F2\u0610-\u061A\u0620-\u0669\u066E-\u06D3\u06D5-\u06DC\u06DF-\u06E8\u06EA-\u06FC\u06FF\u0710-\u074A\u074D-\u07B1\u07C0-\u07F5\u07FA\u0800-\u082D\u0840-\u085B\u08A0-\u08B2\u08E4-\u0963\u0966-\u096F\u0971-\u0983\u0985-\u098C\u098F\u0990\u0993-\u09A8\u09AA-\u09B0\u09B2\u09B6-\u09B9\u09BC-\u09C4\u09C7\u09C8\u09CB-\u09CE\u09D7\u09DC\u09DD\u09DF-\u09E3\u09E6-\u09F1\u0A01-\u0A03\u0A05-\u0A0A\u0A0F\u0A10\u0A13-\u0A28\u0A2A-\u0A30\u0A32\u0A33\u0A35\u0A36\u0A38\u0A39\u0A3C\u0A3E-\u0A42\u0A47\u0A48\u0A4B-\u0A4D\u0A51\u0A59-\u0A5C\u0A5E\u0A66-\u0A75\u0A81-\u0A83\u0A85-\u0A8D\u0A8F-\u0A91\u0A93-\u0AA8\u0AAA-\u0AB0\u0AB2\u0AB3\u0AB5-\u0AB9\u0ABC-\u0AC5\u0AC7-\u0AC9\u0ACB-\u0ACD\u0AD0\u0AE0-\u0AE3\u0AE6-\u0AEF\u0B01-\u0B03\u0B05-\u0B0C\u0B0F\u0B10\u0B13-\u0B28\u0B2A-\u0B30\u0B32\u0B33\u0B35-\u0B39\u0B3C-\u0B44\u0B47\u0B48\u0B4B-\u0B4D\u0B56\u0B57\u0B5C\u0B5D\u0B5F-\u0B63\u0B66-\u0B6F\u0B71\u0B82\u0B83\u0B85-\u0B8A\u0B8E-\u0B90\u0B92-\u0B95\u0B99\u0B9A\u0B9C\u0B9E\u0B9F\u0BA3\u0BA4\u0BA8-\u0BAA\u0BAE-\u0BB9\u0BBE-\u0BC2\u0BC6-\u0BC8\u0BCA-\u0BCD\u0BD0\u0BD7\u0BE6-\u0BEF\u0C00-\u0C03\u0C05-\u0C0C\u0C0E-\u0C10\u0C12-\u0C28\u0C2A-\u0C39\u0C3D-\u0C44\u0C46-\u0C48\u0C4A-\u0C4D\u0C55\u0C56\u0C58\u0C59\u0C60-\u0C63\u0C66-\u0C6F\u0C81-\u0C83\u0C85-\u0C8C\u0C8E-\u0C90\u0C92-\u0CA8\u0CAA-\u0CB3\u0CB5-\u0CB9\u0CBC-\u0CC4\u0CC6-\u0CC8\u0CCA-\u0CCD\u0CD5\u0CD6\u0CDE\u0CE0-\u0CE3\u0CE6-\u0CEF\u0CF1\u0CF2\u0D01-\u0D03\u0D05-\u0D0C\u0D0E-\u0D10\u0D12-\u0D3A\u0D3D-\u0D44\u0D46-\u0D48\u0D4A-\u0D4E\u0D57\u0D60-\u0D63\u0D66-\u0D6F\u0D7A-\u0D7F\u0D82\u0D83\u0D85-\u0D96\u0D9A-\u0DB1\u0DB3-\u0DBB\u0DBD\u0DC0-\u0DC6\u0DCA\u0DCF-\u0DD4\u0DD6\u0DD8-\u0DDF\u0DE6-\u0DEF\u0DF2\u0DF3\u0E01-\u0E3A\u0E40-\u0E4E\u0E50-\u0E59\u0E81\u0E82\u0E84\u0E87\u0E88\u0E8A\u0E8D\u0E94-\u0E97\u0E99-\u0E9F\u0EA1-\u0EA3\u0EA5\u0EA7\u0EAA\u0EAB\u0EAD-\u0EB9\u0EBB-\u0EBD\u0EC0-\u0EC4\u0EC6\u0EC8-\u0ECD\u0ED0-\u0ED9\u0EDC-\u0EDF\u0F00\u0F18\u0F19\u0F20-\u0F29\u0F35\u0F37\u0F39\u0F3E-\u0F47\u0F49-\u0F6C\u0F71-\u0F84\u0F86-\u0F97\u0F99-\u0FBC\u0FC6\u1000-\u1049\u1050-\u109D\u10A0-\u10C5\u10C7\u10CD\u10D0-\u10FA\u10FC-\u1248\u124A-\u124D\u1250-\u1256\u1258\u125A-\u125D\u1260-\u1288\u128A-\u128D\u1290-\u12B0\u12B2-\u12B5\u12B8-\u12BE\u12C0\u12C2-\u12C5\u12C8-\u12D6\u12D8-\u1310\u1312-\u1315\u1318-\u135A\u135D-\u135F\u1380-\u138F\u13A0-\u13F4\u1401-\u166C\u166F-\u167F\u1681-\u169A\u16A0-\u16EA\u16EE-\u16F8\u1700-\u170C\u170E-\u1714\u1720-\u1734\u1740-\u1753\u1760-\u176C\u176E-\u1770\u1772\u1773\u1780-\u17D3\u17D7\u17DC\u17DD\u17E0-\u17E9\u180B-\u180D\u1810-\u1819\u1820-\u1877\u1880-\u18AA\u18B0-\u18F5\u1900-\u191E\u1920-\u192B\u1930-\u193B\u1946-\u196D\u1970-\u1974\u1980-\u19AB\u19B0-\u19C9\u19D0-\u19D9\u1A00-\u1A1B\u1A20-\u1A5E\u1A60-\u1A7C\u1A7F-\u1A89\u1A90-\u1A99\u1AA7\u1AB0-\u1ABD\u1B00-\u1B4B\u1B50-\u1B59\u1B6B-\u1B73\u1B80-\u1BF3\u1C00-\u1C37\u1C40-\u1C49\u1C4D-\u1C7D\u1CD0-\u1CD2\u1CD4-\u1CF6\u1CF8\u1CF9\u1D00-\u1DF5\u1DFC-\u1F15\u1F18-\u1F1D\u1F20-\u1F45\u1F48-\u1F4D\u1F50-\u1F57\u1F59\u1F5B\u1F5D\u1F5F-\u1F7D\u1F80-\u1FB4\u1FB6-\u1FBC\u1FBE\u1FC2-\u1FC4\u1FC6-\u1FCC\u1FD0-\u1FD3\u1FD6-\u1FDB\u1FE0-\u1FEC\u1FF2-\u1FF4\u1FF6-\u1FFC\u200C\u200D\u203F\u2040\u2054\u2071\u207F\u2090-\u209C\u20D0-\u20DC\u20E1\u20E5-\u20F0\u2102\u2107\u210A-\u2113\u2115\u2119-\u211D\u2124\u2126\u2128\u212A-\u212D\u212F-\u2139\u213C-\u213F\u2145-\u2149\u214E\u2160-\u2188\u2C00-\u2C2E\u2C30-\u2C5E\u2C60-\u2CE4\u2CEB-\u2CF3\u2D00-\u2D25\u2D27\u2D2D\u2D30-\u2D67\u2D6F\u2D7F-\u2D96\u2DA0-\u2DA6\u2DA8-\u2DAE\u2DB0-\u2DB6\u2DB8-\u2DBE\u2DC0-\u2DC6\u2DC8-\u2DCE\u2DD0-\u2DD6\u2DD8-\u2DDE\u2DE0-\u2DFF\u2E2F\u3005-\u3007\u3021-\u302F\u3031-\u3035\u3038-\u303C\u3041-\u3096\u3099\u309A\u309D-\u309F\u30A1-\u30FA\u30FC-\u30FF\u3105-\u312D\u3131-\u318E\u31A0-\u31BA\u31F0-\u31FF\u3400-\u4DB5\u4E00-\u9FCC\uA000-\uA48C\uA4D0-\uA4FD\uA500-\uA60C\uA610-\uA62B\uA640-\uA66F\uA674-\uA67D\uA67F-\uA69D\uA69F-\uA6F1\uA717-\uA71F\uA722-\uA788\uA78B-\uA78E\uA790-\uA7AD\uA7B0\uA7B1\uA7F7-\uA827\uA840-\uA873\uA880-\uA8C4\uA8D0-\uA8D9\uA8E0-\uA8F7\uA8FB\uA900-\uA92D\uA930-\uA953\uA960-\uA97C\uA980-\uA9C0\uA9CF-\uA9D9\uA9E0-\uA9FE\uAA00-\uAA36\uAA40-\uAA4D\uAA50-\uAA59\uAA60-\uAA76\uAA7A-\uAAC2\uAADB-\uAADD\uAAE0-\uAAEF\uAAF2-\uAAF6\uAB01-\uAB06\uAB09-\uAB0E\uAB11-\uAB16\uAB20-\uAB26\uAB28-\uAB2E\uAB30-\uAB5A\uAB5C-\uAB5F\uAB64\uAB65\uABC0-\uABEA\uABEC\uABED\uABF0-\uABF9\uAC00-\uD7A3\uD7B0-\uD7C6\uD7CB-\uD7FB\uF900-\uFA6D\uFA70-\uFAD9\uFB00-\uFB06\uFB13-\uFB17\uFB1D-\uFB28\uFB2A-\uFB36\uFB38-\uFB3C\uFB3E\uFB40\uFB41\uFB43\uFB44\uFB46-\uFBB1\uFBD3-\uFD3D\uFD50-\uFD8F\uFD92-\uFDC7\uFDF0-\uFDFB\uFE00-\uFE0F\uFE20-\uFE2D\uFE33\uFE34\uFE4D-\uFE4F\uFE70-\uFE74\uFE76-\uFEFC\uFF10-\uFF19\uFF21-\uFF3A\uFF3F\uFF41-\uFF5A\uFF66-\uFFBE\uFFC2-\uFFC7\uFFCA-\uFFCF\uFFD2-\uFFD7\uFFDA-\uFFDC]'))})
    var.put(u'Regex', PyJsLvalObject8_)
    PyJsLvalArray50_ = Js([None])
    PyJsLvalArray49_ = Js([None])
    @Js
    def PyJsLvalInline20_(expression, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'expression':expression}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'ExpressionStatement'))
        var.get(u'this').put(u'expression', var.get(u'expression'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline17_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'DebuggerStatement'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline27_(label, body, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'label':label, u'body':body}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'LabeledStatement'))
        var.get(u'this').put(u'label', var.get(u'label'))
        var.get(u'this').put(u'body', var.get(u'body'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline33_(body, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'body':body}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'Program'))
        var.get(u'this').put(u'body', var.get(u'body'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline28_(token, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'token':token}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'Literal'))
        var.get(u'this').put(u'value', var.get(u'token').get(u'value'))
        var.get(u'this').put(u'raw', var.get(u'source').callprop(u'slice',var.get(u'token').get(u'start'),var.get(u'token').get(u'end')))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline21_(init, test, update, body, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'init':init, u'test':test, u'update':update, u'body':body}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'ForStatement'))
        var.get(u'this').put(u'init', var.get(u'init'))
        var.get(u'this').put(u'test', var.get(u'test'))
        var.get(u'this').put(u'update', var.get(u'update'))
        var.get(u'this').put(u'body', var.get(u'body'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline16_(label, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'label':label}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'ContinueStatement'))
        var.get(u'this').put(u'label', var.get(u'label'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline8_(params, defaults, body, expression, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'params':params, u'defaults':defaults, u'body':body, u'expression':expression}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'ArrowFunctionExpression'))
        var.get(u'this').put(u'id', var.get(u'null'))
        var.get(u'this').put(u'params', var.get(u'params'))
        var.get(u'this').put(u'defaults', var.get(u'defaults'))
        var.get(u'this').put(u'body', var.get(u'body'))
        var.get(u'this').put(u'rest', var.get(u'null'))
        var.get(u'this').put(u'generator', var.get(u'false'))
        var.get(u'this').put(u'expression', var.get(u'expression'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline45_(test, body, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'test':test, u'body':body}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'WhileStatement'))
        var.get(u'this').put(u'test', var.get(u'test'))
        var.get(u'this').put(u'body', var.get(u'body'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline9_(operator, left, right, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'operator':operator, u'left':left, u'right':right}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'AssignmentExpression'))
        var.get(u'this').put(u'operator', var.get(u'operator'))
        var.get(u'this').put(u'left', var.get(u'left'))
        var.get(u'this').put(u'right', var.get(u'right'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline14_(param, body, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'param':param, u'body':body}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'CatchClause'))
        var.get(u'this').put(u'param', var.get(u'param'))
        var.get(u'this').put(u'body', var.get(u'body'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline6_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        if var.get(u'extra').get(u'range'):
            var.get(u'this').get(u'range').put(Js(1), var.get(u'index'))
            pass
        if var.get(u'extra').get(u'loc'):
            var.get(u'this').get(u'loc').put(u'end', var.get(u'Position').create())
            if var.get(u'extra').get(u'source'):
                var.get(u'this').get(u'loc').put(u'source', var.get(u'extra').get(u'source'))
                pass
            pass
        if var.get(u'extra').get(u'attachComment'):
            var.get(u'this').callprop(u'processComment')
            pass
        pass
        pass
    @Js
    def PyJsLvalInline26_(test, consequent, alternate, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'test':test, u'consequent':consequent, u'alternate':alternate}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'IfStatement'))
        var.get(u'this').put(u'test', var.get(u'test'))
        var.get(u'this').put(u'consequent', var.get(u'consequent'))
        var.get(u'this').put(u'alternate', var.get(u'alternate'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline7_(elements, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'elements':elements}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'ArrayExpression'))
        var.get(u'this').put(u'elements', var.get(u'elements'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline24_(id, params, defaults, body, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'id':id, u'params':params, u'defaults':defaults, u'body':body}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'FunctionExpression'))
        var.get(u'this').put(u'id', var.get(u'id'))
        var.get(u'this').put(u'params', var.get(u'params'))
        var.get(u'this').put(u'defaults', var.get(u'defaults'))
        var.get(u'this').put(u'body', var.get(u'body'))
        var.get(u'this').put(u'rest', var.get(u'null'))
        var.get(u'this').put(u'generator', var.get(u'false'))
        var.get(u'this').put(u'expression', var.get(u'false'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline25_(name, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'name':name}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'Identifier'))
        var.get(u'this').put(u'name', var.get(u'name'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline5_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'lastChild', u'trailingComments', u'bottomRight', u'last'])
        var.put(u'bottomRight', var.get(u'extra').get(u'bottomRightStack'))
        var.put(u'last', var.get(u'bottomRight').get((var.get(u'bottomRight').get(u'length')-Js(1))))
        if PyJsStrictEq(var.get(u'this').get(u'type'),var.get(u'Syntax').get(u'Program')):
            if (var.get(u'this').get(u'body').get(u'length')>Js(0)):
                return var.get('undefined')
                pass
            pass
        if (var.get(u'extra').get(u'trailingComments').get(u'length')>Js(0)):
            if (var.get(u'extra').get(u'trailingComments').get(Js(0)).get(u'range').get(Js(0))>=var.get(u'this').get(u'range').get(Js(1))):
                var.put(u'trailingComments', var.get(u'extra').get(u'trailingComments'))
                var.get(u'extra').put(u'trailingComments', PyJsLvalArray49_)
                pass
            else:
                var.get(u'extra').get(u'trailingComments').put(u'length', Js(0))
                pass
            pass
        else:
            if ((var.get(u'last') and var.get(u'last').get(u'trailingComments')) and (var.get(u'last').get(u'trailingComments').get(Js(0)).get(u'range').get(Js(0))>=var.get(u'this').get(u'range').get(Js(1)))):
                var.put(u'trailingComments', var.get(u'last').get(u'trailingComments'))
                var.get(u'last').delete(u'trailingComments')
                pass
            pass
        if var.get(u'last'):
            while (var.get(u'last') and (var.get(u'last').get(u'range').get(Js(0))>=var.get(u'this').get(u'range').get(Js(0)))):
                var.put(u'lastChild', var.get(u'last'))
                var.put(u'last', var.get(u'bottomRight').callprop(u'pop'))
                pass
            pass
        if var.get(u'lastChild'):
            if (var.get(u'lastChild').get(u'leadingComments') and (var.get(u'lastChild').get(u'leadingComments').get((var.get(u'lastChild').get(u'leadingComments').get(u'length')-Js(1))).get(u'range').get(Js(1))<=var.get(u'this').get(u'range').get(Js(0)))):
                var.get(u'this').put(u'leadingComments', var.get(u'lastChild').get(u'leadingComments'))
                var.get(u'lastChild').put(u'leadingComments', var.get(u'undefined'))
                pass
            pass
        elif ((var.get(u'extra').get(u'leadingComments').get(u'length')>Js(0)) and (var.get(u'extra').get(u'leadingComments').get((var.get(u'extra').get(u'leadingComments').get(u'length')-Js(1))).get(u'range').get(Js(1))<=var.get(u'this').get(u'range').get(Js(0)))):
            var.get(u'this').put(u'leadingComments', var.get(u'extra').get(u'leadingComments'))
            var.get(u'extra').put(u'leadingComments', PyJsLvalArray50_)
            pass
        if var.get(u'trailingComments'):
            var.get(u'this').put(u'trailingComments', var.get(u'trailingComments'))
            pass
        var.get(u'bottomRight').callprop(u'push',var.get(u'this'))
        pass
        pass
    @Js
    def PyJsLvalInline29_(accessor, object, property, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'accessor':accessor, u'object':object, u'property':property}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'MemberExpression'))
        var.get(u'this').put(u'computed', PyJsStrictEq(var.get(u'accessor'),Js(u'[')))
        var.get(u'this').put(u'object', var.get(u'object'))
        var.get(u'this').put(u'property', var.get(u'property'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline22_(left, right, body, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'left':left, u'right':right, u'body':body}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'ForInStatement'))
        var.get(u'this').put(u'left', var.get(u'left'))
        var.get(u'this').put(u'right', var.get(u'right'))
        var.get(u'this').put(u'body', var.get(u'body'))
        var.get(u'this').put(u'each', var.get(u'false'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline32_(operator, argument, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'operator':operator, u'argument':argument}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'UpdateExpression'))
        var.get(u'this').put(u'operator', var.get(u'operator'))
        var.get(u'this').put(u'argument', var.get(u'argument'))
        var.get(u'this').put(u'prefix', var.get(u'false'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline23_(id, params, defaults, body, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'id':id, u'params':params, u'defaults':defaults, u'body':body}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'FunctionDeclaration'))
        var.get(u'this').put(u'id', var.get(u'id'))
        var.get(u'this').put(u'params', var.get(u'params'))
        var.get(u'this').put(u'defaults', var.get(u'defaults'))
        var.get(u'this').put(u'body', var.get(u'body'))
        var.get(u'this').put(u'rest', var.get(u'null'))
        var.get(u'this').put(u'generator', var.get(u'false'))
        var.get(u'this').put(u'expression', var.get(u'false'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline19_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'EmptyStatement'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline34_(kind, key, value, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'kind':kind, u'key':key, u'value':value}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'Property'))
        var.get(u'this').put(u'key', var.get(u'key'))
        var.get(u'this').put(u'value', var.get(u'value'))
        var.get(u'this').put(u'kind', var.get(u'kind'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline40_(argument, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'argument':argument}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'ThrowStatement'))
        var.get(u'this').put(u'argument', var.get(u'argument'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline11_(body, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'body':body}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'BlockStatement'))
        var.get(u'this').put(u'body', var.get(u'body'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline18_(body, test, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'body':body, u'test':test}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'DoWhileStatement'))
        var.get(u'this').put(u'body', var.get(u'body'))
        var.get(u'this').put(u'test', var.get(u'test'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline41_(block, guardedHandlers, handlers, finalizer, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'block':block, u'guardedHandlers':guardedHandlers, u'handlers':handlers, u'finalizer':finalizer}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'TryStatement'))
        var.get(u'this').put(u'block', var.get(u'block'))
        var.get(u'this').put(u'guardedHandlers', var.get(u'guardedHandlers'))
        var.get(u'this').put(u'handlers', var.get(u'handlers'))
        var.get(u'this').put(u'finalizer', var.get(u'finalizer'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline42_(operator, argument, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'operator':operator, u'argument':argument}, var)
        var.get(u'this').put(u'type', (var.get(u'Syntax').get(u'UpdateExpression') if var.get(u'this').put(u'type', ((PyJsStrictEq(var.get(u'operator'),Js(u'++')) or PyJsStrictEq(var.get(u'operator'),Js(u'--'))))) else var.get(u'Syntax').get(u'UnaryExpression')))
        var.get(u'this').put(u'operator', var.get(u'operator'))
        var.get(u'this').put(u'argument', var.get(u'argument'))
        var.get(u'this').put(u'prefix', var.get(u'true'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline43_(declarations, kind, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'declarations':declarations, u'kind':kind}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'VariableDeclaration'))
        var.get(u'this').put(u'declarations', var.get(u'declarations'))
        var.get(u'this').put(u'kind', var.get(u'kind'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline35_(argument, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'argument':argument}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'ReturnStatement'))
        var.get(u'this').put(u'argument', var.get(u'argument'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline37_(test, consequent, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'test':test, u'consequent':consequent}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'SwitchCase'))
        var.get(u'this').put(u'test', var.get(u'test'))
        var.get(u'this').put(u'consequent', var.get(u'consequent'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline12_(label, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'label':label}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'BreakStatement'))
        var.get(u'this').put(u'label', var.get(u'label'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline44_(id, init, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'id':id, u'init':init}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'VariableDeclarator'))
        var.get(u'this').put(u'id', var.get(u'id'))
        var.get(u'this').put(u'init', var.get(u'init'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline15_(test, consequent, alternate, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'test':test, u'consequent':consequent, u'alternate':alternate}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'ConditionalExpression'))
        var.get(u'this').put(u'test', var.get(u'test'))
        var.get(u'this').put(u'consequent', var.get(u'consequent'))
        var.get(u'this').put(u'alternate', var.get(u'alternate'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline36_(expressions, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'expressions':expressions}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'SequenceExpression'))
        var.get(u'this').put(u'expressions', var.get(u'expressions'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline38_(discriminant, cases, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'discriminant':discriminant, u'cases':cases}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'SwitchStatement'))
        var.get(u'this').put(u'discriminant', var.get(u'discriminant'))
        var.get(u'this').put(u'cases', var.get(u'cases'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline10_(operator, left, right, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'operator':operator, u'left':left, u'right':right}, var)
        var.get(u'this').put(u'type', (var.get(u'Syntax').get(u'LogicalExpression') if var.get(u'this').put(u'type', ((PyJsStrictEq(var.get(u'operator'),Js(u'||')) or PyJsStrictEq(var.get(u'operator'),Js(u'&&'))))) else var.get(u'Syntax').get(u'BinaryExpression')))
        var.get(u'this').put(u'operator', var.get(u'operator'))
        var.get(u'this').put(u'left', var.get(u'left'))
        var.get(u'this').put(u'right', var.get(u'right'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline46_(object, body, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'object':object, u'body':body}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'WithStatement'))
        var.get(u'this').put(u'object', var.get(u'object'))
        var.get(u'this').put(u'body', var.get(u'body'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline31_(properties, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'properties':properties}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'ObjectExpression'))
        var.get(u'this').put(u'properties', var.get(u'properties'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline39_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'ThisExpression'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline13_(callee, args, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'callee':callee, u'args':args}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'CallExpression'))
        var.get(u'this').put(u'callee', var.get(u'callee'))
        var.get(u'this').put(u'arguments', var.get(u'args'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    @Js
    def PyJsLvalInline30_(callee, args, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'callee':callee, u'args':args}, var)
        var.get(u'this').put(u'type', var.get(u'Syntax').get(u'NewExpression'))
        var.get(u'this').put(u'callee', var.get(u'callee'))
        var.get(u'this').put(u'arguments', var.get(u'args'))
        var.get(u'this').callprop(u'finish')
        return var.get(u'this')
        pass
        pass
    PyJsLvalObject62_ = Js({u'processComment':PyJsLvalInline5_,u'finish':PyJsLvalInline6_,u'finishArrayExpression':PyJsLvalInline7_,u'finishArrowFunctionExpression':PyJsLvalInline8_,u'finishAssignmentExpression':PyJsLvalInline9_,u'finishBinaryExpression':PyJsLvalInline10_,u'finishBlockStatement':PyJsLvalInline11_,u'finishBreakStatement':PyJsLvalInline12_,u'finishCallExpression':PyJsLvalInline13_,u'finishCatchClause':PyJsLvalInline14_,u'finishConditionalExpression':PyJsLvalInline15_,u'finishContinueStatement':PyJsLvalInline16_,u'finishDebuggerStatement':PyJsLvalInline17_,u'finishDoWhileStatement':PyJsLvalInline18_,u'finishEmptyStatement':PyJsLvalInline19_,u'finishExpressionStatement':PyJsLvalInline20_,u'finishForStatement':PyJsLvalInline21_,u'finishForInStatement':PyJsLvalInline22_,u'finishFunctionDeclaration':PyJsLvalInline23_,u'finishFunctionExpression':PyJsLvalInline24_,u'finishIdentifier':PyJsLvalInline25_,u'finishIfStatement':PyJsLvalInline26_,u'finishLabeledStatement':PyJsLvalInline27_,u'finishLiteral':PyJsLvalInline28_,u'finishMemberExpression':PyJsLvalInline29_,u'finishNewExpression':PyJsLvalInline30_,u'finishObjectExpression':PyJsLvalInline31_,u'finishPostfixExpression':PyJsLvalInline32_,u'finishProgram':PyJsLvalInline33_,u'finishProperty':PyJsLvalInline34_,u'finishReturnStatement':PyJsLvalInline35_,u'finishSequenceExpression':PyJsLvalInline36_,u'finishSwitchCase':PyJsLvalInline37_,u'finishSwitchStatement':PyJsLvalInline38_,u'finishThisExpression':PyJsLvalInline39_,u'finishThrowStatement':PyJsLvalInline40_,u'finishTryStatement':PyJsLvalInline41_,u'finishUnaryExpression':PyJsLvalInline42_,u'finishVariableDeclaration':PyJsLvalInline43_,u'finishVariableDeclarator':PyJsLvalInline44_,u'finishWhileStatement':PyJsLvalInline45_,u'finishWithStatement':PyJsLvalInline46_})
    var.get(u'WrappingNode').put(u'prototype', var.get(u'Node').put(u'prototype', PyJsLvalObject62_))
    var.get(u'exports').put(u'version', Js(u'2.0.0-dev'))
    var.get(u'exports').put(u'tokenize', var.get(u'tokenize'))
    var.get(u'exports').put(u'parse', var.get(u'parse'))
    @Js
    def PyJsLvalInline3_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([u'name', u'types'])
        PyJsLvalObject105_ = Js({})
        var.put(u'types', PyJsLvalObject105_)
        if PyJsStrictEq(var.get(u'Object').get(u'create').typeof(),Js(u'function')):
            var.put(u'types', var.get(u'Object').callprop(u'create',var.get(u'null')))
            pass
        for temp in var.get(u'Syntax'):
            var.put(u'name', temp)
            if var.get(u'Syntax').callprop(u'hasOwnProperty',var.get(u'name')):
                var.get(u'types').put(var.get(u'name'), var.get(u'Syntax').get(var.get(u'name')))
                pass
            pass
        if PyJsStrictEq(var.get(u'Object').get(u'freeze').typeof(),Js(u'function')):
            var.get(u'Object').callprop(u'freeze',var.get(u'types'))
            pass
        return var.get(u'types')
        pass
        pass
    var.get(u'exports').put(u'Syntax', (PyJsLvalInline3_()))
    pass
    pass
(PyJsLvalInline1_(var.get(u'this'),PyJsLvalInline2_))
pass
esprima = var.get('esprima')
parse = esprima['parse']
parse(r'var j = 490 \n; a=4;(;')