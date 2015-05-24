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

class HoistStack(Stack):
    NAME = 'PyJsHoisted%s%d_'

HoistStack = HoistStack()

class InlineStack(Stack):
    NAME = 'PyJsInline%s%d_'

InlineStack = InlineStack()


def to_key(literal_or_identifier):
    ''' returns string representation of this object'''
    k = None
    if literal_or_identifier['type']=='Identifier':
        k = literal_or_identifier['name']
    elif literal_or_identifier['type']=='Literal':
        k = literal_or_identifier['value']
        if isinstance(k, float):
            k = unicode(float_repr(k))
        else:
            k = unicode(k)
    return k

def trans(ele):
    """delegates to appriopriate translating node"""
    return ele





# ==== IDENTIFIERS AND LITERALS  =======



def Literal(type, value, raw, regexp=None):
    if regexp: # regexp
        return 'JsRegExp(%s)' % repr(value)
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
        if property == 'Literal':
            prop = repr(to_key(property))
        else: # worst case
            prop = trans(property) + '.to_string().value'
    else: # always the same since not computed (obj.prop accessor)
        prop = repr(to_key(property))
    return far_left + '.get(%s)' % prop


def ThisExpression(type):
    return 'var.get(u"this")'


def CallExpression(type, callee, args):
    args = [trans(e) for e in args]
    if callee['type']=='MemberExpression':
        far_left = trans(callee['object'])
        if callee['computed']:  # obj[prop] type accessor
            # may be literal which is the same in every case so we can save some time on conversion
            if callee['property'] == 'Literal':
                prop = repr(to_key(callee['property']))
            else: # worst case
                prop = trans(callee['property']) + '.to_string().value'  # its not a string literal! so no repr
        else: # always the same since not computed (obj.prop accessor)
            prop = repr(to_key(callee['property']))
        args.insert(0, prop)
        return far_left + '.callprop(%s)' % ', '.join(args)
    else: # standard call
        return trans(callee) + '(%s)' % ', '.join(args)



# ========== ARRAYS ============


def ArrayExpression(type, elements):  # todo fix null inside problem
    return 'Js(%s)' % repr([trans(e) for e in elements])



# ========== OBJECTS =============

def ObjectExpression(type, properties):
    name = InlineStack.require('Object')
    elems = []
    after = ''
    for p in properties:
        if p['kind']!='init':
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
    k = to_key()
    if key is None:
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


def AssignmentExpression(type, operator, left, right):
    if left['type']=='Identifier':
        return 'var.put(%s, %s, %s)' % (repr(to_key(left)), trans(right), operator)
    elif left['type']=='MemberExpression':
        far_left = trans(left['object'])
        if left['computed']:  # obj[prop] type accessor
            # may be literal which is the same in every case so we can save some time on conversion
            if left['property'] == 'Literal':
                prop = repr(to_key(left['property']))
            else: # worst case
                prop = trans(left['property']) + '.to_string().value'  # its not a string literal! so no repr
        else: # always the same since not computed (obj.prop accessor)
            prop = repr(to_key(left['property']))
        return far_left + '.put(%s, %s, %s)' % (repr(prop), trans(right), operator)
    else:
        raise SyntaxError('Invalid left hand side in assignment!')


def SequenceExpression(type, expressions):
    return reduce(js_comma, (trans(e) for e in expressions))


def NewExpression(type, callee, args):
    return trans(callee) + '.create(%s)' % ', '.join(trans(e) for e in args)

def ConditionalExpression(type, test, consequent, alternate):
    return '(%s if %s else %s)' % (trans(consequent), trans(test), trans(alternate))



# ===========  STATEMENTS =============



def BlockStatement(type, body):
    self.type = Syntax.BlockStatement
    self.body = body




def BreakStatement(type, label):
    self.type = Syntax.BreakStatement
    self.label = label



def CatchClause(type, param, body):
    self.type = Syntax.CatchClause
    self.param = param
    self.body = body



def ContinueStatement(type, label):
    self.type = Syntax.ContinueStatement
    self.label = label




def DebuggerStatement(type):
    return 'pass\n'




def DoWhileStatement(type, body, test):
    self.type = Syntax.DoWhileStatement
    self.body = body
    self.test = test




def EmptyStatement(type):
    return 'pass\n'




def ExpressionStatement(type, expression):
    self.type = Syntax.ExpressionStatement
    self.expression = expression



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
    self.type = Syntax.IfStatement
    self.test = test
    self.consequent = consequent
    self.alternate = alternate




def LabeledStatement(type, label, body):
    self.type = Syntax.LabeledStatement
    self.label = label
    self.body = body


def ReturnStatement(type, argument):
    self.type = Syntax.ReturnStatement
    self.argument = argument



def SwitchCase(type, test, consequent):
    self.type = Syntax.SwitchCase
    self.test = test
    self.consequent = consequent


def SwitchStatement(type, discriminant, cases):
    self.type = Syntax.SwitchStatement
    self.discriminant = discriminant
    self.cases = cases


def ThrowStatement(type, argument):
    self.type = Syntax.ThrowStatement
    self.argument = argument


def TryStatement(type, block, handler, finalizer):
    self.type = Syntax.TryStatement
    self.block = block
    self.guardedHandlers = []
    self.handlers = [handler] if handler else []
    self.handler = handler
    self.finalizer = finalizer


def LexicalDeclaration(type, declarations, kind):
    self.type = Syntax.VariableDeclaration
    self.declarations = declarations
    self.kind = kind



def VariableDeclarator(type, id, init):
    self.type = Syntax.VariableDeclarator
    self.id = id
    self.init = init

def VariableDeclaration(type, declarations):
    self.type = Syntax.VariableDeclaration
    self.declarations = declarations
    self.kind = 'var'


def WhileStatement(type, test, body):
    self.type = Syntax.WhileStatement
    self.test = test
    self.body = body


def WithStatement(type, object, body):
    self.type = Syntax.WithStatement
    self.object = object
    self.body = body

def Program(type, body):
    self.type = Syntax.Program
    self.body = body


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
PostfixExpression = UpdateExpression()