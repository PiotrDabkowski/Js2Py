from __future__ import unicode_literals
from pyjsparserdata import *
from friendly_nodes import *
class self: pass


class Stack:
    NAME = 'UNKNOWN'
    def __init__(self):
        self.reset()

    def require(self, typ):
        name = self.NAME % (typ, len(self.stack))
        self.stack[name] = None
        return name

    def define(self, name, val):
        self.stack[name] = val

    def reset(self):
        self.stack = {}


class ContextStack:
    def __init__(self):
        self.reset()

    def reset(self):
        self.to_register = set([])
        self.to_define = {}

    def register(self, var):
        self.to_register.add(var)

    def define(self, name, code):
        self.to_define[name] = code
        self.register(name)

    def get_code(self):
        code = 'var.registers([%s])\n' % ', '.join(self.to_register)
        for name, func_code in self.to_define.iteritems():
            code += func_code
            code += 'PyJsLvalTempHoisted.func_name = %s\n' % name
        return code




Context = ContextStack()

class InlineStack(Stack):
    NAME = 'PyJsInline%s%d_'

InlineStack = InlineStack()



def to_key(literal_or_identifier):
    ''' returns string representation of this object'''
    if literal_or_identifier['type']=='Identifier':
        return literal_or_identifier['name']
    elif literal_or_identifier['type']=='Literal':
        k = literal_or_identifier['value']
        if isinstance(k, float):
            return unicode(float_repr(k))
        elif 'regex' in literal_or_identifier:
            return compose_regex(k)
        else:
            return unicode(k)

def trans(ele):
    """delegates to appriopriate translating node"""
    return globals()[ele['type']](**ele)



# ==== IDENTIFIERS AND LITERALS  =======



def Literal(type, value, raw, regex=None):
    if regex: # regex
        return 'JsRegExp(%s)' % repr(compose_regex(value))
    elif value is None:  # null
        return 'var.get(u"null")'
    # Todo template
    # String, Bool, Float
    return 'Js(%s)' % repr(value)

def Identifier(type, name):
    return 'var.get(%s)' % repr(name)


def MemberExpression(type, computed, object, property):
    far_left = trans(object)
    if computed:  # obj[prop] type accessor
        # may be literal which is the same in every case so we can save some time on conversion
        if property['type'] == 'Literal':
            prop = repr(to_key(property))
        else: # worst case
            prop = trans(property)
    else: # always the same since not computed (obj.prop accessor)
        prop = repr(to_key(property))
    return far_left + '.get(%s)' % prop


def ThisExpression(type):
    return 'var.get(u"this")'


def CallExpression(type, callee, arguments):
    arguments = [trans(e) for e in arguments]
    if callee['type']=='MemberExpression':
        far_left = trans(callee['object'])
        if callee['computed']:  # obj[prop] type accessor
            # may be literal which is the same in every case so we can save some time on conversion
            if callee['property']['type'] == 'Literal':
                prop = repr(to_key(callee['property']))
            else: # worst case
                prop = trans(callee['property'])  # its not a string literal! so no repr
        else: # always the same since not computed (obj.prop accessor)
            prop = repr(to_key(callee['property']))
        arguments.insert(0, prop)
        return far_left + '.callprop(%s)' % ', '.join(arguments)
    else: # standard call
        return trans(callee) + '(%s)' % ', '.join(arguments)



# ========== ARRAYS ============


def ArrayExpression(type, elements):  # todo fix null inside problem
    return 'Js([%s])' % ', '.join(trans(e) for e in elements)



# ========== OBJECTS =============

def ObjectExpression(type, properties):
    name = InlineStack.require('Object')
    elems = []
    after = ''
    for p in properties:
        if p['kind']=='init':
            elems.append('%s:%s' % Property(**p))
        elif p['kind']=='set':
            k, setter = Property(**p)  # setter is just a lval reffereing to that function, it will be defined in InlineStack automatically
            after += '%s.define_own_property(%s, {"set":%s})\n' % (name, k, setter)
        elif p['kind']=='get':
            k, getter = Property(**p)
            after += '%s.define_own_property(%s, {"get":%s})\n' % (name, k, getter)
        else:
            raise RuntimeError('Unexpected object propery kind')
    obj = '%s = Js({%s})\n' % (name, ','.join(elems))
    InlineStack.define(name, obj+after)
    return name



def Property(type, kind, key, computed, value, method, shorthand):
    if shorthand or computed:
        raise NotImplementedError('Shorthand and Computed properties not implemented!')
    k = to_key(key)
    if k is None:
        raise SyntaxError('Invalid key in dictionary! Or bug in Js2Py')
    v = trans(value)
    return repr(k), v


# ========== EXPRESSIONS ============



def UnaryExpression(type, operator, argument, prefix):
    a = trans(argument)
    if operator=='delete':
        if argument['type'] in {'Identifier', 'MemberExpression'}:
            # means that operation is valid
            return js_delete(a)
        return a   # otherwise not valid, just perform expression
    elif operator=='typeof':
        return js_typeof(a)
    return UNARY[operator](a)

def BinaryExpression(type, operator, left, right):
    a = trans(left)
    b = trans(right)
    # delegate to our friends
    return BINARY[operator](a,b)


def UpdateExpression(type, operator, argument, prefix):
    a = trans(argument)
    return js_postfix(a, operator=='++', not prefix)


def AssignmentExpression(type, operator, left, right): # todo fix operator
    operator = operator[:-1]
    if left['type']=='Identifier':
        if operator:
            return 'var.put(%s, %s, %s)' % (repr(to_key(left)), trans(right), repr(operator))
        else:
            return 'var.put(%s, %s)' % (repr(to_key(left)), trans(right))
    elif left['type']=='MemberExpression':
        far_left = trans(left['object'])
        if left['computed']:  # obj[prop] type accessor
            # may be literal which is the same in every case so we can save some time on conversion
            if left['property']['type'] == 'Literal':
                prop = repr(to_key(left['property']))
            else: # worst case
                prop = trans(left['property'])   # its not a string literal! so no repr
        else: # always the same since not computed (obj.prop accessor)
            prop = repr(to_key(left['property']))
        if operator:
            return far_left + '.put(%s, %s, %s)' % (prop, trans(right), repr(operator))
        else:
            return far_left + '.put(%s, %s)' % (prop, trans(right))
    else:
        raise SyntaxError('Invalid left hand side in assignment!')


def SequenceExpression(type, expressions):
    return reduce(js_comma, (trans(e) for e in expressions))


def NewExpression(type, callee, arguments):
    return trans(callee) + '.create(%s)' % ', '.join(trans(e) for e in arguments)

def ConditionalExpression(type, test, consequent, alternate):
    return '(%s if %s else %s)' % (trans(consequent), trans(test), trans(alternate))



# ===========  STATEMENTS =============



def BlockStatement(type, body):
    return ''.join(trans(e) for e in body)


def ExpressionStatement(type, expression):
    return trans(expression) + '\n'  # end expression space with new line


def BreakStatement(type, label):
    if label:
        return 'raise %s("%s")\n' % (get_break_label(label['name']))
    else:
        return 'break\n'


def ContinueStatement(type, label):
    if label:
        return 'raise %s("%s")\n' % (get_continue_label(label['name']))
    else:
        return 'continue\n'

def ReturnStatement(type, argument):
    return 'return %s\n' % (trans(argument) if argument else "var.get('undefined')")


def EmptyStatement(type):
    return 'pass\n'


def DebuggerStatement(type):
    return 'pass\n'


def DoWhileStatement(type, body, test):
    inside = trans(body) + 'if not %s:\n' % trans(test) + indent('break\n')
    return  'while 1:\n' + indent(inside)


def ForStatement(type, init, test, update, body):
    self.type = Syntax.ForStatement
    self.init = init
    self.test = test
    self.update = update
    self.body = body


def ForInStatement(type, left, right, body):
    self.type = Syntax.ForInStatement
    self.left = left
    self.right = right
    self.body = body
    self.each = False


def IfStatement(type, test, consequent, alternate):
    # NOTE we cannot do elif because function definition inside elif statement would not be possible!
    IF = 'if %s:\n' % trans(test)
    IF += indent(trans(consequent))
    ELSE = 'else:\n' + indent(trans(alternate))
    return IF + ELSE


def LabeledStatement(type, label, body):
    # todo consider using smarter approach!
    inside = trans(body)
    defs = ''
    if inside.startswith('while ') or inside.startswith('for ') or inside.startswith('#for'):
        # we have to add contine label as well...
        # 3 or 1 since #for loop type has more lines before real for.
        sep = 1 if not inside.startswith('#for') else 3
        cont_label = get_continue_label(label)
        temp = inside.split('\n')
        injected = 'try:\n'+'\n'.join(temp[sep:])
        injected += 'except %s:\n    pass\n'%cont_label
        inside = '\n'.join(temp[:sep])+'\n'+indent(injected)
        defs += 'class %s(Exception): pass\n'%cont_label
    break_label = get_break_label(label)
    inside = 'try:\n%sexcept %s:\n    pass\n'% (indent(inside), break_label)
    defs += 'class %s(Exception): pass\n'%break_label
    return defs + inside


def StatementList(lis):
    if lis:
        return ''.join(trans(e) for e in lis)
    else:
        return 'pass\n'



def SwitchStatement(type, discriminant, cases):
    #TODO there will be a problem with continue in a switch statement.... FIX IT
    code = 'while 1:\n' + indent('SWITCHED = False\nCONDITION = (%s)\n')
    code = code % trans(discriminant)
    for case in cases:
        case_code = None
        if case['test']: # case (x):
            case_code = 'if SWITCHED or PyJsStrictEq(CONDITION, %s):\n' % (trans(case['test']))
        else:  # default:
            case_code = 'if True:\n'
        case_code += indent('SWITCHED = True\n')
        case_code += indent(StatementList(case['consequent']))
        # one more indent for whole
        code += indent(case_code)
    # prevent infinite loop and sort out nested switch...
    code += indent('SWITCHED = True\nbreak\n')
    return code


def ThrowStatement(type, argument):
    return 'PyJsTempException = JsToPyException(%s)\nraise PyJsTempException\n' % trans(argument)


def TryStatement(type, block, handler, handlers, guardedHandlers, finalizer):
    self.type = Syntax.TryStatement
    self.block = block
    self.guardedHandlers = []
    self.handlers = [handler] if handler else []
    self.handler = handler
    self.finalizer = finalizer

def CatchClause(type, param, body):
    self.type = Syntax.CatchClause
    self.param = param
    self.body = body


def LexicalDeclaration(type, declarations, kind):
    raise NotImplementedError('let and const not implemented yet but they will be soon! Check github for updates.')


def VariableDeclarator(type, id, init):
    name = id['name']
    # register the name if not already registered
    Context.register(name)
    if init:
        return 'var.put(%s, %s)\n' % (repr(name), trans(init))
    return ''


def VariableDeclaration(type, declarations, kind):
    code = ''.join(trans(d) for d in declarations)
    return code if code else 'pass\n'



def WhileStatement(type, test, body):
    return 'while %s:\n'%trans(test) + indent(trans(body))



def WithStatement(type, object, body):
    raise NotImplementedError('With statement not implemented!')

def Program(type, body):
    InlineStack.reset()
    code = ''.join(trans(e) for e in body)
    # here add hoisted elements (register variables and define functions)
    code = Context.get_code() + code
    # replace all inline variables
    return code



# ======== FUNCTIONS ============

def FunctionDeclaration(type, id, params, defaults, body):
    self.type = Syntax.FunctionDeclaration
    self.id = id
    self.params = params
    self.defaults = defaults
    self.body = body
    self.generator = False
    self.expression = False



def FunctionExpression(type, id, params, defaults, body):
    self.type = Syntax.FunctionExpression
    self.id = id
    self.params = params
    self.defaults = defaults
    self.body = body
    self.generator = False
    self.expression = False

LogicalExpression = BinaryExpression
PostfixExpression = UpdateExpression


import pyjsparser

c = '''do {a = 4} while (3)'''

x = pyjsparser.PyJsParser().parse(c)
print trans(x)

