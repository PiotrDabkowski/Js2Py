from js2py.pyjs import *
var = Scope( JS_BUILTINS )
var['window'] = var
set_global_object(var)
var.registers([])
@Js
def PyJs_kupa_45_(factory, this, arguments, var=var):
    var = Scope({u'this':this, u'factory':factory, u'arguments':arguments}, var)
    var.registers([u'factory'])
    var.get(u'console').callprop(u'log', Js(u'here'))
    if PyJsStrictNeq(var.get(u'exports',throw=False).typeof(),Js(u'undefined')):
        var.get(u'factory')(var.get(u'exports'))
    else:
        PyJs_Object_46_ = Js({})
        var.get(u'window').put(u'hljs', var.get(u'factory')(PyJs_Object_46_))
        if (PyJsStrictEq(var.get(u'define',throw=False).typeof(),Js(u'function')) and var.get(u'define').get(u'amd')):
            @Js
            def PyJs_anonymous_47_(this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments}, var)
                var.registers([])
                return var.get(u'window').get(u'hljs')
            PyJs_anonymous_47_.func_name = u'anonymous'
            var.get(u'define')(Js(u'hljs'), Js([]), PyJs_anonymous_47_
            )
PyJs_kupa_45_.func_name = u'kupa'

@Js
def PyJs_anonymous_0_(hljs, this, arguments, var=var):
    var = Scope({u'this':this, u'hljs':hljs, u'arguments':arguments}, var)
    var.registers([u'blockLanguage', u'compileLanguage', u'fixMarkup', u'tag', u'escape', u'listLanguages', u'registerLanguage', u'languages', u'hljs', u'nodeStream', u'aliases', u'initHighlightingOnLoad', u'configure', u'highlightAuto', u'testRe', u'initHighlighting', u'getLanguage', u'mergeStreams', u'highlightBlock', u'isNotHighlighted', u'buildClassName', u'inherit', u'highlight', u'options'])
    @Js
    def PyJsHoisted_blockLanguage_(block, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'block':block}, var)
        var.registers([u'i', u'length', u'classes', u'block', u'match'])
        var.put(u'classes', (var.get(u'block').get(u'className')+Js(u' ')))
        var.put(u'classes', (var.get(u'block').get(u'parentNode').get(u'className') if var.get(u'block').get(u'parentNode') else Js(u'')), u'+')
        var.put(u'match', JsRegExp(u'/\\blang(?:uage)?-([\\w-]+)\\b/').callprop(u'exec', var.get(u'classes')))
        if var.get(u'match'):
            return (var.get(u'match').get(u'1') if var.get(u'getLanguage')(var.get(u'match').get(u'1')) else Js(u'no-highlight'))
        var.put(u'classes', var.get(u'classes').callprop(u'split', JsRegExp(u'/\\s+/')))
        #for JS loop
        PyJsComma(var.put(u'i', Js(0.0)),var.put(u'length', var.get(u'classes').get(u'length')))
        while (var.get(u'i')<var.get(u'length')):
            if (var.get(u'getLanguage')(var.get(u'classes').get(var.get(u'i'))) or var.get(u'isNotHighlighted')(var.get(u'classes').get(var.get(u'i')))):
                return var.get(u'classes').get(var.get(u'i'))
            (var.put(u'i',var.get(u'i')+Js(1))-Js(1))
    PyJsHoisted_blockLanguage_.func_name = u'blockLanguage'
    var.put(u'blockLanguage', PyJsHoisted_blockLanguage_)
    @Js
    def PyJsHoisted_initHighlightingOnLoad_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        var.get(u'addEventListener')(Js(u'DOMContentLoaded'), var.get(u'initHighlighting'), Js(False))
        var.get(u'addEventListener')(Js(u'load'), var.get(u'initHighlighting'), Js(False))
    PyJsHoisted_initHighlightingOnLoad_.func_name = u'initHighlightingOnLoad'
    var.put(u'initHighlightingOnLoad', PyJsHoisted_initHighlightingOnLoad_)
    @Js
    def PyJsHoisted_getLanguage_(name, this, arguments, var=var):
        var = Scope({u'this':this, u'name':name, u'arguments':arguments}, var)
        var.registers([u'name'])
        return (var.get(u'languages').get(var.get(u'name')) or var.get(u'languages').get(var.get(u'aliases').get(var.get(u'name'))))
    PyJsHoisted_getLanguage_.func_name = u'getLanguage'
    var.put(u'getLanguage', PyJsHoisted_getLanguage_)
    @Js
    def PyJsHoisted_compileLanguage_(language, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'language':language}, var)
        var.registers([u'reStr', u'compileMode', u'language', u'langRe'])
        @Js
        def PyJsHoisted_reStr_(re, this, arguments, var=var):
            var = Scope({u'this':this, u're':re, u'arguments':arguments}, var)
            var.registers([u're'])
            return ((var.get(u're') and var.get(u're').get(u'source')) or var.get(u're'))
        PyJsHoisted_reStr_.func_name = u'reStr'
        var.put(u'reStr', PyJsHoisted_reStr_)
        @Js
        def PyJsHoisted_compileMode_(mode, parent, this, arguments, var=var):
            var = Scope({u'this':this, u'mode':mode, u'parent':parent, u'arguments':arguments}, var)
            var.registers([u'terminators', u'parent', u'expanded_contains', u'mode', u'compiled_keywords', u'flatten'])
            if var.get(u'mode').get(u'compiled'):
                return var.get('undefined')
            var.get(u'mode').put(u'compiled', var.get(u'true'))
            var.get(u'mode').put(u'keywords', (var.get(u'mode').get(u'keywords') or var.get(u'mode').get(u'beginKeywords')))
            if var.get(u'mode').get(u'keywords'):
                PyJs_Object_5_ = Js({})
                var.put(u'compiled_keywords', PyJs_Object_5_)
                @Js
                def PyJs_anonymous_6_(className, str, this, arguments, var=var):
                    var = Scope({u'className':className, u'this':this, u'arguments':arguments, u'str':str}, var)
                    var.registers([u'className', u'str'])
                    if var.get(u'language').get(u'case_insensitive'):
                        var.put(u'str', var.get(u'str').callprop(u'toLowerCase'))
                    @Js
                    def PyJs_anonymous_7_(kw, this, arguments, var=var):
                        var = Scope({u'this':this, u'kw':kw, u'arguments':arguments}, var)
                        var.registers([u'pair', u'kw'])
                        var.put(u'pair', var.get(u'kw').callprop(u'split', Js(u'|')))
                        var.get(u'compiled_keywords').put(var.get(u'pair').get(u'0'), Js([var.get(u'className'), (var.get(u'Number')(var.get(u'pair').get(u'1')) if var.get(u'pair').get(u'1') else Js(1.0))]))
                    PyJs_anonymous_7_.func_name = u'anonymous'
                    var.get(u'str').callprop(u'split', Js(u' ')).callprop(u'forEach', PyJs_anonymous_7_
                    )
                PyJs_anonymous_6_.func_name = u'anonymous'
                var.put(u'flatten', PyJs_anonymous_6_
                )
                if (var.get(u'mode').get(u'keywords').typeof()==Js(u'string')):
                    var.get(u'flatten')(Js(u'keyword'), var.get(u'mode').get(u'keywords'))
                else:
                    @Js
                    def PyJs_anonymous_8_(className, this, arguments, var=var):
                        var = Scope({u'className':className, u'this':this, u'arguments':arguments}, var)
                        var.registers([u'className'])
                        var.get(u'flatten')(var.get(u'className'), var.get(u'mode').get(u'keywords').get(var.get(u'className')))
                    PyJs_anonymous_8_.func_name = u'anonymous'
                    var.get(u'Object').callprop(u'keys', var.get(u'mode').get(u'keywords')).callprop(u'forEach', PyJs_anonymous_8_
                    )
                var.get(u'mode').put(u'keywords', var.get(u'compiled_keywords'))
            var.get(u'mode').put(u'lexemesRe', var.get(u'langRe')((var.get(u'mode').get(u'lexemes') or JsRegExp(u'/\\b\\w+\\b/')), var.get(u'true')))
            if var.get(u'parent'):
                if var.get(u'mode').get(u'beginKeywords'):
                    var.get(u'mode').put(u'begin', ((Js(u'\\b(')+var.get(u'mode').get(u'beginKeywords').callprop(u'split', Js(u' ')).callprop(u'join', Js(u'|')))+Js(u')\\b')))
                if var.get(u'mode').get(u'begin').neg():
                    var.get(u'mode').put(u'begin', JsRegExp(u'/\\B|\\b/'))
                var.get(u'mode').put(u'beginRe', var.get(u'langRe')(var.get(u'mode').get(u'begin')))
                if (var.get(u'mode').get(u'end').neg() and var.get(u'mode').get(u'endsWithParent').neg()):
                    var.get(u'mode').put(u'end', JsRegExp(u'/\\B|\\b/'))
                if var.get(u'mode').get(u'end'):
                    var.get(u'mode').put(u'endRe', var.get(u'langRe')(var.get(u'mode').get(u'end')))
                var.get(u'mode').put(u'terminator_end', (var.get(u'reStr')(var.get(u'mode').get(u'end')) or Js(u'')))
                if (var.get(u'mode').get(u'endsWithParent') and var.get(u'parent').get(u'terminator_end')):
                    var.get(u'mode').put(u'terminator_end', ((Js(u'|') if var.get(u'mode').get(u'end') else Js(u''))+var.get(u'parent').get(u'terminator_end')), u'+')
            if var.get(u'mode').get(u'illegal'):
                var.get(u'mode').put(u'illegalRe', var.get(u'langRe')(var.get(u'mode').get(u'illegal')))
            if PyJsStrictEq(var.get(u'mode').get(u'relevance'),var.get(u'undefined')):
                var.get(u'mode').put(u'relevance', Js(1.0))
            if var.get(u'mode').get(u'contains').neg():
                var.get(u'mode').put(u'contains', Js([]))
            var.put(u'expanded_contains', Js([]))
            @Js
            def PyJs_anonymous_9_(c, this, arguments, var=var):
                var = Scope({u'this':this, u'c':c, u'arguments':arguments}, var)
                var.registers([u'c'])
                if var.get(u'c').get(u'variants'):
                    @Js
                    def PyJs_anonymous_10_(v, this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments, u'v':v}, var)
                        var.registers([u'v'])
                        var.get(u'expanded_contains').callprop(u'push', var.get(u'inherit')(var.get(u'c'), var.get(u'v')))
                    PyJs_anonymous_10_.func_name = u'anonymous'
                    var.get(u'c').get(u'variants').callprop(u'forEach', PyJs_anonymous_10_
                    )
                else:
                    var.get(u'expanded_contains').callprop(u'push', (var.get(u'mode') if (var.get(u'c')==Js(u'self')) else var.get(u'c')))
            PyJs_anonymous_9_.func_name = u'anonymous'
            var.get(u'mode').get(u'contains').callprop(u'forEach', PyJs_anonymous_9_
            )
            var.get(u'mode').put(u'contains', var.get(u'expanded_contains'))
            @Js
            def PyJs_anonymous_11_(c, this, arguments, var=var):
                var = Scope({u'this':this, u'c':c, u'arguments':arguments}, var)
                var.registers([u'c'])
                var.get(u'compileMode')(var.get(u'c'), var.get(u'mode'))
            PyJs_anonymous_11_.func_name = u'anonymous'
            var.get(u'mode').get(u'contains').callprop(u'forEach', PyJs_anonymous_11_
            )
            if var.get(u'mode').get(u'starts'):
                var.get(u'compileMode')(var.get(u'mode').get(u'starts'), var.get(u'parent'))
            @Js
            def PyJs_anonymous_12_(c, this, arguments, var=var):
                var = Scope({u'this':this, u'c':c, u'arguments':arguments}, var)
                var.registers([u'c'])
                return (((Js(u'\\.?(')+var.get(u'c').get(u'begin'))+Js(u')\\.?')) if var.get(u'c').get(u'beginKeywords') else var.get(u'c').get(u'begin'))
            PyJs_anonymous_12_.func_name = u'anonymous'
            var.put(u'terminators', var.get(u'mode').get(u'contains').callprop(u'map', PyJs_anonymous_12_
            ).callprop(u'concat', Js([var.get(u'mode').get(u'terminator_end'), var.get(u'mode').get(u'illegal')])).callprop(u'map', var.get(u'reStr')).callprop(u'filter', var.get(u'Boolean')))
            @Js
            def PyJs_anonymous_14_(this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments}, var)
                var.registers([])
                return var.get(u"null")
            PyJs_anonymous_14_.func_name = u'anonymous'
            PyJs_Object_13_ = Js({u'exec':PyJs_anonymous_14_
            })
            var.get(u'mode').put(u'terminators', (var.get(u'langRe')(var.get(u'terminators').callprop(u'join', Js(u'|')), var.get(u'true')) if var.get(u'terminators').get(u'length') else PyJs_Object_13_))
        PyJsHoisted_compileMode_.func_name = u'compileMode'
        var.put(u'compileMode', PyJsHoisted_compileMode_)
        @Js
        def PyJsHoisted_langRe_(value, PyJsArg_676c6f62616c_, this, arguments, var=var):
            var = Scope({u'this':this, u'global':PyJsArg_676c6f62616c_, u'arguments':arguments, u'value':value}, var)
            var.registers([u'global', u'value'])
            return var.get(u'RegExp').create(var.get(u'reStr')(var.get(u'value')), ((Js(u'm')+(Js(u'i') if var.get(u'language').get(u'case_insensitive') else Js(u'')))+(Js(u'g') if var.get(u'global') else Js(u''))))
        PyJsHoisted_langRe_.func_name = u'langRe'
        var.put(u'langRe', PyJsHoisted_langRe_)
        pass
        pass
        pass
        var.get(u'compileMode')(var.get(u'language'))
    PyJsHoisted_compileLanguage_.func_name = u'compileLanguage'
    var.put(u'compileLanguage', PyJsHoisted_compileLanguage_)
    @Js
    def PyJsHoisted_isNotHighlighted_(language, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'language':language}, var)
        var.registers([u'language'])
        return JsRegExp(u'/no-?highlight|plain|text/').callprop(u'test', var.get(u'language'))
    PyJsHoisted_isNotHighlighted_.func_name = u'isNotHighlighted'
    var.put(u'isNotHighlighted', PyJsHoisted_isNotHighlighted_)
    @Js
    def PyJsHoisted_buildClassName_(prevClassName, currentLang, resultLang, this, arguments, var=var):
        var = Scope({u'this':this, u'prevClassName':prevClassName, u'currentLang':currentLang, u'arguments':arguments, u'resultLang':resultLang}, var)
        var.registers([u'prevClassName', u'currentLang', u'result', u'language', u'resultLang'])
        var.put(u'language', (var.get(u'aliases').get(var.get(u'currentLang')) if var.get(u'currentLang') else var.get(u'resultLang')))
        var.put(u'result', Js([var.get(u'prevClassName').callprop(u'trim')]))
        if var.get(u'prevClassName').callprop(u'match', JsRegExp(u'/\\bhljs\\b/')).neg():
            var.get(u'result').callprop(u'push', Js(u'hljs'))
        if PyJsStrictEq(var.get(u'prevClassName').callprop(u'indexOf', var.get(u'language')),(-Js(1.0))):
            var.get(u'result').callprop(u'push', var.get(u'language'))
        return var.get(u'result').callprop(u'join', Js(u' ')).callprop(u'trim')
    PyJsHoisted_buildClassName_.func_name = u'buildClassName'
    var.put(u'buildClassName', PyJsHoisted_buildClassName_)
    @Js
    def PyJsHoisted_fixMarkup_(value, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'value':value}, var)
        var.registers([u'value'])
        if var.get(u'options').get(u'tabReplace'):
            @Js
            def PyJs_anonymous_22_(match, p1, this, arguments, var=var):
                var = Scope({u'this':this, u'p1':p1, u'arguments':arguments, u'match':match}, var)
                var.registers([u'p1', u'match'])
                return var.get(u'p1').callprop(u'replace', JsRegExp(u'/\\t/g'), var.get(u'options').get(u'tabReplace'))
            PyJs_anonymous_22_.func_name = u'anonymous'
            var.put(u'value', var.get(u'value').callprop(u'replace', JsRegExp(u'/^((<[^>]+>|\\t)+)/gm'), PyJs_anonymous_22_
            ))
        if var.get(u'options').get(u'useBR'):
            var.put(u'value', var.get(u'value').callprop(u'replace', JsRegExp(u'/\\n/g'), Js(u'<br>')))
        return var.get(u'value')
    PyJsHoisted_fixMarkup_.func_name = u'fixMarkup'
    var.put(u'fixMarkup', PyJsHoisted_fixMarkup_)
    @Js
    def PyJsHoisted_registerLanguage_(name, language, this, arguments, var=var):
        var = Scope({u'this':this, u'name':name, u'language':language, u'arguments':arguments}, var)
        var.registers([u'lang', u'name', u'language'])
        var.put(u'lang', var.get(u'languages').put(var.get(u'name'), var.get(u'language')(var.get(u'hljs'))))
        if var.get(u'lang').get(u'aliases'):
            @Js
            def PyJs_anonymous_28_(alias, this, arguments, var=var):
                var = Scope({u'this':this, u'alias':alias, u'arguments':arguments}, var)
                var.registers([u'alias'])
                var.get(u'aliases').put(var.get(u'alias'), var.get(u'name'))
            PyJs_anonymous_28_.func_name = u'anonymous'
            var.get(u'lang').get(u'aliases').callprop(u'forEach', PyJs_anonymous_28_
            )
    PyJsHoisted_registerLanguage_.func_name = u'registerLanguage'
    var.put(u'registerLanguage', PyJsHoisted_registerLanguage_)
    @Js
    def PyJsHoisted_inherit_(parent, obj, this, arguments, var=var):
        var = Scope({u'this':this, u'obj':obj, u'arguments':arguments, u'parent':parent}, var)
        var.registers([u'parent', u'obj', u'result', u'key'])
        PyJs_Object_1_ = Js({})
        var.put(u'result', PyJs_Object_1_)
        for PyJsTemp in var.get(u'parent'):
            var.put(u'key', PyJsTemp)
            var.get(u'result').put(var.get(u'key'), var.get(u'parent').get(var.get(u'key')))
        if var.get(u'obj'):
            for PyJsTemp in var.get(u'obj'):
                var.put(u'key', PyJsTemp)
                var.get(u'result').put(var.get(u'key'), var.get(u'obj').get(var.get(u'key')))
        return var.get(u'result')
    PyJsHoisted_inherit_.func_name = u'inherit'
    var.put(u'inherit', PyJsHoisted_inherit_)
    @Js
    def PyJsHoisted_highlightAuto_(text, languageSubset, this, arguments, var=var):
        var = Scope({u'this':this, u'text':text, u'arguments':arguments, u'languageSubset':languageSubset}, var)
        var.registers([u'text', u'second_best', u'result', u'languageSubset'])
        var.put(u'languageSubset', ((var.get(u'languageSubset') or var.get(u'options').get(u'languages')) or var.get(u'Object').callprop(u'keys', var.get(u'languages'))))
        PyJs_Object_20_ = Js({u'relevance':Js(0.0),u'value':var.get(u'escape')(var.get(u'text'))})
        var.put(u'result', PyJs_Object_20_)
        var.put(u'second_best', var.get(u'result'))
        @Js
        def PyJs_anonymous_21_(name, this, arguments, var=var):
            var = Scope({u'this':this, u'name':name, u'arguments':arguments}, var)
            var.registers([u'current', u'name'])
            if var.get(u'getLanguage')(var.get(u'name')).neg():
                return var.get('undefined')
            var.put(u'current', var.get(u'highlight')(var.get(u'name'), var.get(u'text'), Js(False)))
            var.get(u'current').put(u'language', var.get(u'name'))
            if (var.get(u'current').get(u'relevance')>var.get(u'second_best').get(u'relevance')):
                var.put(u'second_best', var.get(u'current'))
            if (var.get(u'current').get(u'relevance')>var.get(u'result').get(u'relevance')):
                var.put(u'second_best', var.get(u'result'))
                var.put(u'result', var.get(u'current'))
        PyJs_anonymous_21_.func_name = u'anonymous'
        var.get(u'languageSubset').callprop(u'forEach', PyJs_anonymous_21_
        )
        if var.get(u'second_best').get(u'language'):
            var.get(u'result').put(u'second_best', var.get(u'second_best'))
        return var.get(u'result')
    PyJsHoisted_highlightAuto_.func_name = u'highlightAuto'
    var.put(u'highlightAuto', PyJsHoisted_highlightAuto_)
    @Js
    def PyJsHoisted_testRe_(re, lexeme, this, arguments, var=var):
        var = Scope({u'lexeme':lexeme, u're':re, u'this':this, u'arguments':arguments}, var)
        var.registers([u'lexeme', u're', u'match'])
        var.put(u'match', (var.get(u're') and var.get(u're').callprop(u'exec', var.get(u'lexeme'))))
        return (var.get(u'match') and (var.get(u'match').get(u'index')==Js(0.0)))
    PyJsHoisted_testRe_.func_name = u'testRe'
    var.put(u'testRe', PyJsHoisted_testRe_)
    @Js
    def PyJsHoisted_tag_(node, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'arguments':arguments}, var)
        var.registers([u'node'])
        return var.get(u'node').get(u'nodeName').callprop(u'toLowerCase')
    PyJsHoisted_tag_.func_name = u'tag'
    var.put(u'tag', PyJsHoisted_tag_)
    @Js
    def PyJsHoisted_initHighlighting_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'blocks'])
        if var.get(u'initHighlighting').get(u'called'):
            return var.get('undefined')
        var.get(u'initHighlighting').put(u'called', var.get(u'true'))
        var.put(u'blocks', var.get(u'document').callprop(u'querySelectorAll', Js(u'pre code')))
        var.get(u'Array').get(u'prototype').get(u'forEach').callprop(u'call', var.get(u'blocks'), var.get(u'highlightBlock'))
    PyJsHoisted_initHighlighting_.func_name = u'initHighlighting'
    var.put(u'initHighlighting', PyJsHoisted_initHighlighting_)
    @Js
    def PyJsHoisted_nodeStream_(node, this, arguments, var=var):
        var = Scope({u'node':node, u'this':this, u'arguments':arguments}, var)
        var.registers([u'node', u'result'])
        var.put(u'result', Js([]))
        @Js
        def PyJs__nodeStream_2_(node, offset, this, arguments, var=var):
            var = Scope({u'node':node, u'this':this, u'arguments':arguments, u'offset':offset}, var)
            var.registers([u'node', u'offset', u'child'])
            #for JS loop
            var.put(u'child', var.get(u'node').get(u'firstChild'))

            while var.get(u'child'):
                if (var.get(u'child').get(u'nodeType')==Js(3.0)):
                    var.put(u'offset', var.get(u'child').get(u'nodeValue').get(u'length'), u'+')
                else:
                    if (var.get(u'child').get(u'nodeType')==Js(1.0)):
                        PyJs_Object_3_ = Js({u'event':Js(u'start'),u'offset':var.get(u'offset'),u'node':var.get(u'child')})
                        var.get(u'result').callprop(u'push', PyJs_Object_3_)
                        var.put(u'offset', var.get(u'_nodeStream')(var.get(u'child'), var.get(u'offset')))
                        if var.get(u'tag')(var.get(u'child')).callprop(u'match', JsRegExp(u'/br|hr|img|input/')).neg():
                            PyJs_Object_4_ = Js({u'event':Js(u'stop'),u'offset':var.get(u'offset'),u'node':var.get(u'child')})
                            var.get(u'result').callprop(u'push', PyJs_Object_4_)
                var.put(u'child', var.get(u'child').get(u'nextSibling'))
            return var.get(u'offset')
        PyJs__nodeStream_2_.func_name = u'_nodeStream'
        PyJs__nodeStream_2_
        (var.get(u'node'), Js(0.0))
        return var.get(u'result')
    PyJsHoisted_nodeStream_.func_name = u'nodeStream'
    var.put(u'nodeStream', PyJsHoisted_nodeStream_)
    @Js
    def PyJsHoisted_escape_(value, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'value':value}, var)
        var.registers([u'value'])
        return var.get(u'value').callprop(u'replace', JsRegExp(u'/&/gm'), Js(u'&amp;')).callprop(u'replace', JsRegExp(u'/</gm'), Js(u'&lt;')).callprop(u'replace', JsRegExp(u'/>/gm'), Js(u'&gt;'))
    PyJsHoisted_escape_.func_name = u'escape'
    var.put(u'escape', PyJsHoisted_escape_)
    @Js
    def PyJsHoisted_highlight_(name, value, ignore_illegals, continuation, this, arguments, var=var):
        var = Scope({u'arguments':arguments, u'name':name, u'this':this, u'continuation':continuation, u'value':value, u'ignore_illegals':ignore_illegals}, var)
        var.registers([u'continuation', u'keywordMatch', u'mode_buffer', u'subMode', u'result', u'startNewMode', u'processLexeme', u'index', u'top', u'isIllegal', u'current', u'continuations', u'processSubLanguage', u'relevance', u'buildSpan', u'match', u'ignore_illegals', u'endOfMode', u'count', u'processKeywords', u'name', u'language', u'value', u'processBuffer'])
        @Js
        def PyJsHoisted_keywordMatch_(mode, match, this, arguments, var=var):
            var = Scope({u'this':this, u'mode':mode, u'match':match, u'arguments':arguments}, var)
            var.registers([u'match', u'mode', u'match_str'])
            var.put(u'match_str', (var.get(u'match').get(u'0').callprop(u'toLowerCase') if var.get(u'language').get(u'case_insensitive') else var.get(u'match').get(u'0')))
            return (var.get(u'mode').get(u'keywords').callprop(u'hasOwnProperty', var.get(u'match_str')) and var.get(u'mode').get(u'keywords').get(var.get(u'match_str')))
        PyJsHoisted_keywordMatch_.func_name = u'keywordMatch'
        var.put(u'keywordMatch', PyJsHoisted_keywordMatch_)
        @Js
        def PyJsHoisted_processBuffer_(this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments}, var)
            var.registers([])
            return (var.get(u'processSubLanguage')() if PyJsStrictNeq(var.get(u'top').get(u'subLanguage'),var.get(u'undefined')) else var.get(u'processKeywords')())
        PyJsHoisted_processBuffer_.func_name = u'processBuffer'
        var.put(u'processBuffer', PyJsHoisted_processBuffer_)
        @Js
        def PyJsHoisted_processLexeme_(buffer, lexeme, this, arguments, var=var):
            var = Scope({u'buffer':buffer, u'lexeme':lexeme, u'this':this, u'arguments':arguments}, var)
            var.registers([u'origin', u'buffer', u'lexeme', u'new_mode', u'end_mode'])
            var.put(u'mode_buffer', var.get(u'buffer'), u'+')
            if PyJsStrictEq(var.get(u'lexeme'),var.get(u'undefined')):
                var.put(u'result', var.get(u'processBuffer')(), u'+')
                return Js(0.0)
            var.put(u'new_mode', var.get(u'subMode')(var.get(u'lexeme'), var.get(u'top')))
            if var.get(u'new_mode'):
                var.put(u'result', var.get(u'processBuffer')(), u'+')
                var.get(u'startNewMode')(var.get(u'new_mode'), var.get(u'lexeme'))
                return (Js(0.0) if var.get(u'new_mode').get(u'returnBegin') else var.get(u'lexeme').get(u'length'))
            var.put(u'end_mode', var.get(u'endOfMode')(var.get(u'top'), var.get(u'lexeme')))
            if var.get(u'end_mode'):
                var.put(u'origin', var.get(u'top'))
                if (var.get(u'origin').get(u'returnEnd') or var.get(u'origin').get(u'excludeEnd')).neg():
                    var.put(u'mode_buffer', var.get(u'lexeme'), u'+')
                var.put(u'result', var.get(u'processBuffer')(), u'+')
                while 1:
                    if var.get(u'top').get(u'className'):
                        var.put(u'result', Js(u'</span>'), u'+')
                    var.put(u'relevance', var.get(u'top').get(u'relevance'), u'+')
                    var.put(u'top', var.get(u'top').get(u'parent'))
                    if not (var.get(u'top')!=var.get(u'end_mode').get(u'parent')):
                        break
                if var.get(u'origin').get(u'excludeEnd'):
                    var.put(u'result', var.get(u'escape')(var.get(u'lexeme')), u'+')
                var.put(u'mode_buffer', Js(u''))
                if var.get(u'end_mode').get(u'starts'):
                    var.get(u'startNewMode')(var.get(u'end_mode').get(u'starts'), Js(u''))
                return (Js(0.0) if var.get(u'origin').get(u'returnEnd') else var.get(u'lexeme').get(u'length'))
            if var.get(u'isIllegal')(var.get(u'lexeme'), var.get(u'top')):
                PyJsTempException = JsToPyException(var.get(u'Error').create(((((Js(u'Illegal lexeme "')+var.get(u'lexeme'))+Js(u'" for mode "'))+(var.get(u'top').get(u'className') or Js(u'<unnamed>')))+Js(u'"'))))
                raise PyJsTempException
            var.put(u'mode_buffer', var.get(u'lexeme'), u'+')
            return (var.get(u'lexeme').get(u'length') or Js(1.0))
        PyJsHoisted_processLexeme_.func_name = u'processLexeme'
        var.put(u'processLexeme', PyJsHoisted_processLexeme_)
        @Js
        def PyJsHoisted_isIllegal_(lexeme, mode, this, arguments, var=var):
            var = Scope({u'lexeme':lexeme, u'this':this, u'mode':mode, u'arguments':arguments}, var)
            var.registers([u'lexeme', u'mode'])
            return (var.get(u'ignore_illegals').neg() and var.get(u'testRe')(var.get(u'mode').get(u'illegalRe'), var.get(u'lexeme')))
        PyJsHoisted_isIllegal_.func_name = u'isIllegal'
        var.put(u'isIllegal', PyJsHoisted_isIllegal_)
        @Js
        def PyJsHoisted_endOfMode_(mode, lexeme, this, arguments, var=var):
            var = Scope({u'lexeme':lexeme, u'this':this, u'mode':mode, u'arguments':arguments}, var)
            var.registers([u'lexeme', u'mode'])
            if var.get(u'testRe')(var.get(u'mode').get(u'endRe'), var.get(u'lexeme')):
                while (var.get(u'mode').get(u'endsParent') and var.get(u'mode').get(u'parent')):
                    var.put(u'mode', var.get(u'mode').get(u'parent'))
                return var.get(u'mode')
            if var.get(u'mode').get(u'endsWithParent'):
                return var.get(u'endOfMode')(var.get(u'mode').get(u'parent'), var.get(u'lexeme'))
        PyJsHoisted_endOfMode_.func_name = u'endOfMode'
        var.put(u'endOfMode', PyJsHoisted_endOfMode_)
        @Js
        def PyJsHoisted_processSubLanguage_(this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments}, var)
            var.registers([u'result'])
            if (var.get(u'top').get(u'subLanguage') and var.get(u'languages').get(var.get(u'top').get(u'subLanguage')).neg()):
                return var.get(u'escape')(var.get(u'mode_buffer'))
            var.put(u'result', (var.get(u'highlight')(var.get(u'top').get(u'subLanguage'), var.get(u'mode_buffer'), var.get(u'true'), var.get(u'continuations').get(var.get(u'top').get(u'subLanguage'))) if var.get(u'top').get(u'subLanguage') else var.get(u'highlightAuto')(var.get(u'mode_buffer'))))
            if (var.get(u'top').get(u'relevance')>Js(0.0)):
                var.put(u'relevance', var.get(u'result').get(u'relevance'), u'+')
            if (var.get(u'top').get(u'subLanguageMode')==Js(u'continuous')):
                var.get(u'continuations').put(var.get(u'top').get(u'subLanguage'), var.get(u'result').get(u'top'))
            return var.get(u'buildSpan')(var.get(u'result').get(u'language'), var.get(u'result').get(u'value'), Js(False), var.get(u'true'))
        PyJsHoisted_processSubLanguage_.func_name = u'processSubLanguage'
        var.put(u'processSubLanguage', PyJsHoisted_processSubLanguage_)
        @Js
        def PyJsHoisted_subMode_(lexeme, mode, this, arguments, var=var):
            var = Scope({u'lexeme':lexeme, u'this':this, u'mode':mode, u'arguments':arguments}, var)
            var.registers([u'i', u'lexeme', u'mode'])
            #for JS loop
            var.put(u'i', Js(0.0))

            while (var.get(u'i')<var.get(u'mode').get(u'contains').get(u'length')):
                if var.get(u'testRe')(var.get(u'mode').get(u'contains').get(var.get(u'i')).get(u'beginRe'), var.get(u'lexeme')):
                    return var.get(u'mode').get(u'contains').get(var.get(u'i'))
                (var.put(u'i',var.get(u'i')+Js(1))-Js(1))
        PyJsHoisted_subMode_.func_name = u'subMode'
        var.put(u'subMode', PyJsHoisted_subMode_)
        @Js
        def PyJsHoisted_startNewMode_(mode, lexeme, this, arguments, var=var):
            var = Scope({u'lexeme':lexeme, u'this':this, u'mode':mode, u'arguments':arguments}, var)
            var.registers([u'lexeme', u'markup', u'mode'])
            var.put(u'markup', (var.get(u'buildSpan')(var.get(u'mode').get(u'className'), Js(u''), var.get(u'true')) if var.get(u'mode').get(u'className') else Js(u'')))
            if var.get(u'mode').get(u'returnBegin'):
                var.put(u'result', var.get(u'markup'), u'+')
                var.put(u'mode_buffer', Js(u''))
            else:
                if var.get(u'mode').get(u'excludeBegin'):
                    var.put(u'result', (var.get(u'escape')(var.get(u'lexeme'))+var.get(u'markup')), u'+')
                    var.put(u'mode_buffer', Js(u''))
                else:
                    var.put(u'result', var.get(u'markup'), u'+')
                    var.put(u'mode_buffer', var.get(u'lexeme'))
            PyJs_Object_16_ = Js({u'value':var.get(u'top')})
            PyJs_Object_15_ = Js({u'parent':PyJs_Object_16_})
            var.put(u'top', var.get(u'Object').callprop(u'create', var.get(u'mode'), PyJs_Object_15_))
        PyJsHoisted_startNewMode_.func_name = u'startNewMode'
        var.put(u'startNewMode', PyJsHoisted_startNewMode_)
        @Js
        def PyJsHoisted_buildSpan_(classname, insideSpan, leaveOpen, noPrefix, this, arguments, var=var):
            var = Scope({u'classname':classname, u'this':this, u'arguments':arguments, u'leaveOpen':leaveOpen, u'noPrefix':noPrefix, u'insideSpan':insideSpan}, var)
            var.registers([u'openSpan', u'classPrefix', u'leaveOpen', u'noPrefix', u'closeSpan', u'classname', u'insideSpan'])
            var.put(u'classPrefix', (Js(u'') if var.get(u'noPrefix') else var.get(u'options').get(u'classPrefix')))
            var.put(u'openSpan', (Js(u'<span class="')+var.get(u'classPrefix')))
            var.put(u'closeSpan', (Js(u'') if var.get(u'leaveOpen') else Js(u'</span>')))
            var.put(u'openSpan', (var.get(u'classname')+Js(u'">')), u'+')
            return ((var.get(u'openSpan')+var.get(u'insideSpan'))+var.get(u'closeSpan'))
        PyJsHoisted_buildSpan_.func_name = u'buildSpan'
        var.put(u'buildSpan', PyJsHoisted_buildSpan_)
        @Js
        def PyJsHoisted_processKeywords_(this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments}, var)
            var.registers([u'keyword_match', u'last_index', u'result', u'match'])
            if var.get(u'top').get(u'keywords').neg():
                return var.get(u'escape')(var.get(u'mode_buffer'))
            var.put(u'result', Js(u''))
            var.put(u'last_index', Js(0.0))
            var.get(u'top').get(u'lexemesRe').put(u'lastIndex', Js(0.0))
            var.put(u'match', var.get(u'top').get(u'lexemesRe').callprop(u'exec', var.get(u'mode_buffer')))
            while var.get(u'match'):
                var.put(u'result', var.get(u'escape')(var.get(u'mode_buffer').callprop(u'substr', var.get(u'last_index'), (var.get(u'match').get(u'index')-var.get(u'last_index')))), u'+')
                var.put(u'keyword_match', var.get(u'keywordMatch')(var.get(u'top'), var.get(u'match')))
                if var.get(u'keyword_match'):
                    var.put(u'relevance', var.get(u'keyword_match').get(u'1'), u'+')
                    var.put(u'result', var.get(u'buildSpan')(var.get(u'keyword_match').get(u'0'), var.get(u'escape')(var.get(u'match').get(u'0'))), u'+')
                else:
                    var.put(u'result', var.get(u'escape')(var.get(u'match').get(u'0')), u'+')
                var.put(u'last_index', var.get(u'top').get(u'lexemesRe').get(u'lastIndex'))
                var.put(u'match', var.get(u'top').get(u'lexemesRe').callprop(u'exec', var.get(u'mode_buffer')))
            return (var.get(u'result')+var.get(u'escape')(var.get(u'mode_buffer').callprop(u'substr', var.get(u'last_index'))))
        PyJsHoisted_processKeywords_.func_name = u'processKeywords'
        var.put(u'processKeywords', PyJsHoisted_processKeywords_)
        var.put(u'language', var.get(u'getLanguage')(var.get(u'name')))
        if var.get(u'language').neg():
            PyJsTempException = JsToPyException(var.get(u'Error').create(((Js(u'Unknown language: "')+var.get(u'name'))+Js(u'"'))))
            raise PyJsTempException
        var.get(u'compileLanguage')(var.get(u'language'))
        var.put(u'top', (var.get(u'continuation') or var.get(u'language')))
        PyJs_Object_17_ = Js({})
        var.put(u'continuations', PyJs_Object_17_)
        var.put(u'result', Js(u''))
        #for JS loop
        var.put(u'current', var.get(u'top'))
        while (var.get(u'current')!=var.get(u'language')):
            if var.get(u'current').get(u'className'):
                var.put(u'result', (var.get(u'buildSpan')(var.get(u'current').get(u'className'), Js(u''), var.get(u'true'))+var.get(u'result')))
            var.put(u'current', var.get(u'current').get(u'parent'))
        var.put(u'mode_buffer', Js(u''))
        var.put(u'relevance', Js(0.0))
        try:
            var.put(u'index', Js(0.0))
            while var.get(u'true'):
                var.get(u'top').get(u'terminators').put(u'lastIndex', var.get(u'index'))
                var.put(u'match', var.get(u'top').get(u'terminators').callprop(u'exec', var.get(u'value')))
                if var.get(u'match').neg():
                    break
                var.put(u'count', var.get(u'processLexeme')(var.get(u'value').callprop(u'substr', var.get(u'index'), (var.get(u'match').get(u'index')-var.get(u'index'))), var.get(u'match').get(u'0')))
                var.put(u'index', (var.get(u'match').get(u'index')+var.get(u'count')))
            var.get(u'processLexeme')(var.get(u'value').callprop(u'substr', var.get(u'index')))
            #for JS loop
            var.put(u'current', var.get(u'top'))
            while var.get(u'current').get(u'parent'):
                if var.get(u'current').get(u'className'):
                    var.put(u'result', Js(u'</span>'), u'+')
                var.put(u'current', var.get(u'current').get(u'parent'))
            PyJs_Object_18_ = Js({u'relevance':var.get(u'relevance'),u'value':var.get(u'result'),u'language':var.get(u'name'),u'top':var.get(u'top')})
            return PyJs_Object_18_
        except PyJsException as PyJsTempException:
            PyJsHolder_65_10510828 = var.own.get(u'e')
            var.force_own_put(u'e', PyExceptionToJs(PyJsTempException))
            try:
                if (var.get(u'e').get(u'message').callprop(u'indexOf', Js(u'Illegal'))!=(-Js(1.0))):
                    PyJs_Object_19_ = Js({u'relevance':Js(0.0),u'value':var.get(u'escape')(var.get(u'value'))})
                    return PyJs_Object_19_
                else:
                    PyJsTempException = JsToPyException(var.get(u'e'))
                    raise PyJsTempException
            finally:
                if PyJsHolder_65_10510828 is not None:
                    var.own[u'e'] = PyJsHolder_65_10510828
                else:
                    del var.own[u'e']
                del PyJsHolder_65_10510828
    PyJsHoisted_highlight_.func_name = u'highlight'
    var.put(u'highlight', PyJsHoisted_highlight_)
    @Js
    def PyJsHoisted_mergeStreams_(original, highlighted, value, this, arguments, var=var):
        var = Scope({u'highlighted':highlighted, u'this':this, u'original':original, u'value':value, u'arguments':arguments}, var)
        var.registers([u'selectStream', u'nodeStack', u'render', u'stream', u'value', u'highlighted', u'processed', u'close', u'open', u'original', u'result'])
        @Js
        def PyJsHoisted_open_(node, this, arguments, var=var):
            var = Scope({u'node':node, u'this':this, u'arguments':arguments}, var)
            var.registers([u'node', u'attr_str'])
            @Js
            def PyJsHoisted_attr_str_(a, this, arguments, var=var):
                var = Scope({u'a':a, u'this':this, u'arguments':arguments}, var)
                var.registers([u'a'])
                return ((((Js(u' ')+var.get(u'a').get(u'nodeName'))+Js(u'="'))+var.get(u'escape')(var.get(u'a').get(u'value')))+Js(u'"'))
            PyJsHoisted_attr_str_.func_name = u'attr_str'
            var.put(u'attr_str', PyJsHoisted_attr_str_)
            pass
            var.put(u'result', (((Js(u'<')+var.get(u'tag')(var.get(u'node')))+var.get(u'Array').get(u'prototype').get(u'map').callprop(u'call', var.get(u'node').get(u'attributes'), var.get(u'attr_str')).callprop(u'join', Js(u'')))+Js(u'>')), u'+')
        PyJsHoisted_open_.func_name = u'open'
        var.put(u'open', PyJsHoisted_open_)
        @Js
        def PyJsHoisted_selectStream_(this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments}, var)
            var.registers([])
            if (var.get(u'original').get(u'length').neg() or var.get(u'highlighted').get(u'length').neg()):
                return (var.get(u'original') if var.get(u'original').get(u'length') else var.get(u'highlighted'))
            if (var.get(u'original').get(u'0').get(u'offset')!=var.get(u'highlighted').get(u'0').get(u'offset')):
                return (var.get(u'original') if (var.get(u'original').get(u'0').get(u'offset')<var.get(u'highlighted').get(u'0').get(u'offset')) else var.get(u'highlighted'))
            return (var.get(u'original') if (var.get(u'highlighted').get(u'0').get(u'event')==Js(u'start')) else var.get(u'highlighted'))
        PyJsHoisted_selectStream_.func_name = u'selectStream'
        var.put(u'selectStream', PyJsHoisted_selectStream_)
        @Js
        def PyJsHoisted_render_(event, this, arguments, var=var):
            var = Scope({u'this':this, u'event':event, u'arguments':arguments}, var)
            var.registers([u'event'])
            (var.get(u'open') if (var.get(u'event').get(u'event')==Js(u'start')) else var.get(u'close'))(var.get(u'event').get(u'node'))
        PyJsHoisted_render_.func_name = u'render'
        var.put(u'render', PyJsHoisted_render_)
        @Js
        def PyJsHoisted_close_(node, this, arguments, var=var):
            var = Scope({u'node':node, u'this':this, u'arguments':arguments}, var)
            var.registers([u'node'])
            var.put(u'result', ((Js(u'</')+var.get(u'tag')(var.get(u'node')))+Js(u'>')), u'+')
        PyJsHoisted_close_.func_name = u'close'
        var.put(u'close', PyJsHoisted_close_)
        var.put(u'processed', Js(0.0))
        var.put(u'result', Js(u''))
        var.put(u'nodeStack', Js([]))
        pass
        pass
        pass
        pass
        while (var.get(u'original').get(u'length') or var.get(u'highlighted').get(u'length')):
            var.put(u'stream', var.get(u'selectStream')())
            var.put(u'result', var.get(u'escape')(var.get(u'value').callprop(u'substr', var.get(u'processed'), (var.get(u'stream').get(u'0').get(u'offset')-var.get(u'processed')))), u'+')
            var.put(u'processed', var.get(u'stream').get(u'0').get(u'offset'))
            if (var.get(u'stream')==var.get(u'original')):
                var.get(u'nodeStack').callprop(u'reverse').callprop(u'forEach', var.get(u'close'))
                while 1:
                    var.get(u'render')(var.get(u'stream').callprop(u'splice', Js(0.0), Js(1.0)).get(u'0'))
                    var.put(u'stream', var.get(u'selectStream')())
                    if not (((var.get(u'stream')==var.get(u'original')) and var.get(u'stream').get(u'length')) and (var.get(u'stream').get(u'0').get(u'offset')==var.get(u'processed'))):
                        break
                var.get(u'nodeStack').callprop(u'reverse').callprop(u'forEach', var.get(u'open'))
            else:
                if (var.get(u'stream').get(u'0').get(u'event')==Js(u'start')):
                    var.get(u'nodeStack').callprop(u'push', var.get(u'stream').get(u'0').get(u'node'))
                else:
                    var.get(u'nodeStack').callprop(u'pop')
                var.get(u'render')(var.get(u'stream').callprop(u'splice', Js(0.0), Js(1.0)).get(u'0'))
        return (var.get(u'result')+var.get(u'escape')(var.get(u'value').callprop(u'substr', var.get(u'processed'))))
    PyJsHoisted_mergeStreams_.func_name = u'mergeStreams'
    var.put(u'mergeStreams', PyJsHoisted_mergeStreams_)
    @Js
    def PyJsHoisted_listLanguages_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        return var.get(u'Object').callprop(u'keys', var.get(u'languages'))
    PyJsHoisted_listLanguages_.func_name = u'listLanguages'
    var.put(u'listLanguages', PyJsHoisted_listLanguages_)
    @Js
    def PyJsHoisted_configure_(user_options, this, arguments, var=var):
        var = Scope({u'this':this, u'user_options':user_options, u'arguments':arguments}, var)
        var.registers([u'user_options'])
        var.put(u'options', var.get(u'inherit')(var.get(u'options'), var.get(u'user_options')))
    PyJsHoisted_configure_.func_name = u'configure'
    var.put(u'configure', PyJsHoisted_configure_)
    @Js
    def PyJsHoisted_highlightBlock_(block, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'block':block}, var)
        var.registers([u'node', u'resultNode', u'language', u'text', u'result', u'originalStream', u'block'])
        var.put(u'language', var.get(u'blockLanguage')(var.get(u'block')))
        if var.get(u'isNotHighlighted')(var.get(u'language')):
            return var.get('undefined')
        pass
        if var.get(u'options').get(u'useBR'):
            var.put(u'node', var.get(u'document').callprop(u'createElementNS', Js(u'http://www.w3.org/1999/xhtml'), Js(u'div')))
            var.get(u'node').put(u'innerHTML', var.get(u'block').get(u'innerHTML').callprop(u'replace', JsRegExp(u'/\\n/g'), Js(u'')).callprop(u'replace', JsRegExp(u'/<br[ \\/]*>/g'), Js(u'\n')))
        else:
            var.put(u'node', var.get(u'block'))
        var.put(u'text', var.get(u'node').get(u'textContent'))
        var.put(u'result', (var.get(u'highlight')(var.get(u'language'), var.get(u'text'), var.get(u'true')) if var.get(u'language') else var.get(u'highlightAuto')(var.get(u'text'))))
        var.put(u'originalStream', var.get(u'nodeStream')(var.get(u'node')))
        if var.get(u'originalStream').get(u'length'):
            var.put(u'resultNode', var.get(u'document').callprop(u'createElementNS', Js(u'http://www.w3.org/1999/xhtml'), Js(u'div')))
            var.get(u'resultNode').put(u'innerHTML', var.get(u'result').get(u'value'))
            var.get(u'result').put(u'value', var.get(u'mergeStreams')(var.get(u'originalStream'), var.get(u'nodeStream')(var.get(u'resultNode')), var.get(u'text')))
        var.get(u'result').put(u'value', var.get(u'fixMarkup')(var.get(u'result').get(u'value')))
        var.get(u'block').put(u'innerHTML', var.get(u'result').get(u'value'))
        var.get(u'block').put(u'className', var.get(u'buildClassName')(var.get(u'block').get(u'className'), var.get(u'language'), var.get(u'result').get(u'language')))
        PyJs_Object_23_ = Js({u'language':var.get(u'result').get(u'language'),u're':var.get(u'result').get(u'relevance')})
        var.get(u'block').put(u'result', PyJs_Object_23_)
        if var.get(u'result').get(u'second_best'):
            PyJs_Object_24_ = Js({u'language':var.get(u'result').get(u'second_best').get(u'language'),u're':var.get(u'result').get(u'second_best').get(u'relevance')})
            var.get(u'block').put(u'second_best', PyJs_Object_24_)
    PyJsHoisted_highlightBlock_.func_name = u'highlightBlock'
    var.put(u'highlightBlock', PyJsHoisted_highlightBlock_)
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
    PyJs_Object_25_ = Js({u'classPrefix':Js(u'hljs-'),u'tabReplace':var.get(u"null"),u'useBR':Js(False),u'languages':var.get(u'undefined')})
    var.put(u'options', PyJs_Object_25_)
    pass
    pass
    pass
    PyJs_Object_26_ = Js({})
    var.put(u'languages', PyJs_Object_26_)
    PyJs_Object_27_ = Js({})
    var.put(u'aliases', PyJs_Object_27_)
    pass
    pass
    pass
    var.get(u'hljs').put(u'highlight', var.get(u'highlight'))
    var.get(u'hljs').put(u'highlightAuto', var.get(u'highlightAuto'))
    var.get(u'hljs').put(u'fixMarkup', var.get(u'fixMarkup'))
    var.get(u'hljs').put(u'highlightBlock', var.get(u'highlightBlock'))
    var.get(u'hljs').put(u'configure', var.get(u'configure'))
    var.get(u'hljs').put(u'initHighlighting', var.get(u'initHighlighting'))
    var.get(u'hljs').put(u'initHighlightingOnLoad', var.get(u'initHighlightingOnLoad'))
    var.get(u'hljs').put(u'registerLanguage', var.get(u'registerLanguage'))
    var.get(u'hljs').put(u'listLanguages', var.get(u'listLanguages'))
    var.get(u'hljs').put(u'getLanguage', var.get(u'getLanguage'))
    var.get(u'hljs').put(u'inherit', var.get(u'inherit'))
    var.get(u'hljs').put(u'IDENT_RE', Js(u'[a-zA-Z]\\w*'))
    var.get(u'hljs').put(u'UNDERSCORE_IDENT_RE', Js(u'[a-zA-Z_]\\w*'))
    var.get(u'hljs').put(u'NUMBER_RE', Js(u'\\b\\d+(\\.\\d+)?'))
    var.get(u'hljs').put(u'C_NUMBER_RE', Js(u'(\\b0[xX][a-fA-F0-9]+|(\\b\\d+(\\.\\d*)?|\\.\\d+)([eE][-+]?\\d+)?)'))
    var.get(u'hljs').put(u'BINARY_NUMBER_RE', Js(u'\\b(0b[01]+)'))
    var.get(u'hljs').put(u'RE_STARTERS_RE', Js(u'!|!=|!==|%|%=|&|&&|&=|\\*|\\*=|\\+|\\+=|,|-|-=|/=|/|:|;|<<|<<=|<=|<|===|==|=|>>>=|>>=|>=|>>>|>>|>|\\?|\\[|\\{|\\(|\\^|\\^=|\\||\\|=|\\|\\||~'))
    PyJs_Object_29_ = Js({u'begin':Js(u'\\\\[\\s\\S]'),u'relevance':Js(0.0)})
    var.get(u'hljs').put(u'BACKSLASH_ESCAPE', PyJs_Object_29_)
    PyJs_Object_30_ = Js({u'className':Js(u'string'),u'begin':Js(u"'"),u'end':Js(u"'"),u'illegal':Js(u'\\n'),u'contains':Js([var.get(u'hljs').get(u'BACKSLASH_ESCAPE')])})
    var.get(u'hljs').put(u'APOS_STRING_MODE', PyJs_Object_30_)
    PyJs_Object_31_ = Js({u'className':Js(u'string'),u'begin':Js(u'"'),u'end':Js(u'"'),u'illegal':Js(u'\\n'),u'contains':Js([var.get(u'hljs').get(u'BACKSLASH_ESCAPE')])})
    var.get(u'hljs').put(u'QUOTE_STRING_MODE', PyJs_Object_31_)
    PyJs_Object_32_ = Js({u'begin':JsRegExp(u"/\\b(a|an|the|are|I|I'm|isn't|don't|doesn't|won't|but|just|should|pretty|simply|enough|gonna|going|wtf|so|such)\\b/")})
    var.get(u'hljs').put(u'PHRASAL_WORDS_MODE', PyJs_Object_32_)
    @Js
    def PyJs_anonymous_33_(begin, end, inherits, this, arguments, var=var):
        var = Scope({u'inherits':inherits, u'this':this, u'begin':begin, u'end':end, u'arguments':arguments}, var)
        var.registers([u'inherits', u'begin', u'end', u'mode'])
        PyJs_Object_34_ = Js({u'className':Js(u'comment'),u'begin':var.get(u'begin'),u'end':var.get(u'end'),u'contains':Js([])})
        PyJs_Object_35_ = Js({})
        var.put(u'mode', var.get(u'hljs').callprop(u'inherit', PyJs_Object_34_, (var.get(u'inherits') or PyJs_Object_35_)))
        var.get(u'mode').get(u'contains').callprop(u'push', var.get(u'hljs').get(u'PHRASAL_WORDS_MODE'))
        PyJs_Object_36_ = Js({u'className':Js(u'doctag'),u'begin':Js(u'(?:TODO|FIXME|NOTE|BUG|XXX):'),u'relevance':Js(0.0)})
        var.get(u'mode').get(u'contains').callprop(u'push', PyJs_Object_36_)
        return var.get(u'mode')
    PyJs_anonymous_33_.func_name = u'anonymous'
    var.get(u'hljs').put(u'COMMENT', PyJs_anonymous_33_
    )
    var.get(u'hljs').put(u'C_LINE_COMMENT_MODE', var.get(u'hljs').callprop(u'COMMENT', Js(u'//'), Js(u'$')))
    var.get(u'hljs').put(u'C_BLOCK_COMMENT_MODE', var.get(u'hljs').callprop(u'COMMENT', Js(u'/\\*'), Js(u'\\*/')))
    var.get(u'hljs').put(u'HASH_COMMENT_MODE', var.get(u'hljs').callprop(u'COMMENT', Js(u'#'), Js(u'$')))
    PyJs_Object_37_ = Js({u'className':Js(u'number'),u'begin':var.get(u'hljs').get(u'NUMBER_RE'),u'relevance':Js(0.0)})
    var.get(u'hljs').put(u'NUMBER_MODE', PyJs_Object_37_)
    PyJs_Object_38_ = Js({u'className':Js(u'number'),u'begin':var.get(u'hljs').get(u'C_NUMBER_RE'),u'relevance':Js(0.0)})
    var.get(u'hljs').put(u'C_NUMBER_MODE', PyJs_Object_38_)
    PyJs_Object_39_ = Js({u'className':Js(u'number'),u'begin':var.get(u'hljs').get(u'BINARY_NUMBER_RE'),u'relevance':Js(0.0)})
    var.get(u'hljs').put(u'BINARY_NUMBER_MODE', PyJs_Object_39_)
    PyJs_Object_40_ = Js({u'className':Js(u'number'),u'begin':(((((((((var.get(u'hljs').get(u'NUMBER_RE')+Js(u'('))+Js(u'%|em|ex|ch|rem'))+Js(u'|vw|vh|vmin|vmax'))+Js(u'|cm|mm|in|pt|pc|px'))+Js(u'|deg|grad|rad|turn'))+Js(u'|s|ms'))+Js(u'|Hz|kHz'))+Js(u'|dpi|dpcm|dppx'))+Js(u')?')),u'relevance':Js(0.0)})
    var.get(u'hljs').put(u'CSS_NUMBER_MODE', PyJs_Object_40_)
    PyJs_Object_42_ = Js({u'begin':JsRegExp(u'/\\[/'),u'end':JsRegExp(u'/\\]/'),u'relevance':Js(0.0),u'contains':Js([var.get(u'hljs').get(u'BACKSLASH_ESCAPE')])})
    PyJs_Object_41_ = Js({u'className':Js(u'regexp'),u'begin':JsRegExp(u'/\\//'),u'end':JsRegExp(u'/\\/[gimuy]*/'),u'illegal':JsRegExp(u'/\\n/'),u'contains':Js([var.get(u'hljs').get(u'BACKSLASH_ESCAPE'), PyJs_Object_42_])})
    var.get(u'hljs').put(u'REGEXP_MODE', PyJs_Object_41_)
    PyJs_Object_43_ = Js({u'className':Js(u'title'),u'begin':var.get(u'hljs').get(u'IDENT_RE'),u'relevance':Js(0.0)})
    var.get(u'hljs').put(u'TITLE_MODE', PyJs_Object_43_)
    PyJs_Object_44_ = Js({u'className':Js(u'title'),u'begin':var.get(u'hljs').get(u'UNDERSCORE_IDENT_RE'),u'relevance':Js(0.0)})
    var.get(u'hljs').put(u'UNDERSCORE_TITLE_MODE', PyJs_Object_44_)
    return var.get(u'hljs')
PyJs_anonymous_0_.func_name = u'anonymous'

var.put(u'a', PyJs_kupa_45_(PyJs_anonymous_0_))
print var['hljs']['highlight']('JavaScript', 'hey')
