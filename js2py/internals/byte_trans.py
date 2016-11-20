from code import Code
from simplex import MakeError
from opcodes import *
from operations import *
from trans_utils import *

SPECIAL_IDENTIFIERS = {'true', 'false', 'this'}


class ByteCodeGenerator:
    def __init__(self, exe):
        self.exe = exe

        self.declared_continue_labels = {}
        self.declared_break_labels = {}

        self.implicit_breaks = []
        self.implicit_continues = []

        self.declared_vars = []

        self.function_tape = []


    def ArrayExpression(self, elements, **kwargs):
        for e in elements:
            self.emit(e)
        self.emit('LOAD_ARRAY', len(elements))
                                                        
    def AssignmentExpression(self, operator, left, right, **kwargs):
        operator = operator[:-1]
        if left['type'] == 'MemberExpression':
            self.emit(left['object'])
            if left['computed']:
                self.emit(left['property'])
                self.emit(right)
                if operator:
                    self.emit('STORE_MEMBER_OP', operator)
                else:
                    self.emit('STORE_MEMBER')
            else:
                self.emit(right)
                if operator:
                    self.emit('STORE_MEMBER_DOT_OP', left['property']['name'], operator)
                else:
                    self.emit('STORE_MEMBER_DOT', left['property']['name'])
        elif left['type'] == 'Identifier':
            if left['name'] in SPECIAL_IDENTIFIERS:
                raise MakeError('SyntaxError', 'Invalid left-hand side in assignment')
            self.emit(right)
            if operator:
                self.emit('STORE_OP', left['name'], operator)
            else:
                self.emit('STORE', left['name'])
        else:
            raise MakeError('SyntaxError', 'Invalid left-hand side in assignment')

                        
    def BinaryExpression(self, operator, left, right, **kwargs):
        self.emit(left)
        self.emit(right)
        self.emit('BINARY_OP', operator)
                                
    def BlockStatement(self, body, **kwargs):
        self._emit_statement_list(body)
                
    def BreakStatement(self, label, **kwargs):
        if label is None:
            self.emit('JUMP', self.implicit_breaks[-1])
        else:
            raise NotImplementedError('W8')
                
    def CallExpression(self, callee, arguments, **kwargs):
        if callee['type'] == 'MemberExpression':
            self.emit(callee['object'])
            if callee['computed']:
                self.emit(callee['property'])
                if arguments:
                    for e in arguments:
                        self.emit(e)
                    self.emit('LOAD_N_TUPLE', len(arguments))
                    self.emit('CALL_METHOD')
                else:
                    self.emit('CALL_METHOD_NO_ARGS')
            else:
                prop_name = to_key(callee['property'])
                if arguments:
                    for e in arguments:
                        self.emit(e)
                    self.emit('LOAD_N_TUPLE', len(arguments))
                    self.emit('CALL_METHOD_DOT', prop_name)
                else:
                    self.emit('CALL_METHOD_DOT_NO_ARGS', prop_name)
        else:
            self.emit(callee)
            if arguments:
                for e in arguments:
                    self.emit(e)
                self.emit('LOAD_N_TUPLE', len(arguments))
                self.emit('CALL')
            else:
                self.emit('CALL_NO_ARGS')
                        
    def ClassBody(self, body, **kwargs):
        raise NotImplementedError('Not available in ECMA 5.1')
                
    def ClassDeclaration(self, id, superClass, body, **kwargs):
        raise NotImplementedError('Not available in ECMA 5.1')
                                
    def ClassExpression(self, id, superClass, body, **kwargs):
        raise NotImplementedError('Not available in ECMA 5.1')

    def ConditionalExpression(self, test, consequent, alternate, **kwargs):
        alt = self.exe.get_new_label()
        end = self.exe.get_new_label()
        # ?
        self.emit(test)
        self.emit('JUMP_IF_FALSE', alt)
        # first val
        self.emit(consequent)
        self.emit('JUMP', end)
        # second val
        self.emit('LABEL', alt)
        self.emit(alternate)
        # end of ?: statement
        self.emit('LABEL', end)
                                
    def ContinueStatement(self, label, **kwargs):
        if label is None:
            self.emit('JUMP', self.implicit_continues[-1])
        else:
            raise NotImplementedError('W8')
                
    def DebuggerStatement(self, **kwargs):
        self.EmptyStatement(**kwargs)
        
    def DoWhileStatement(self, body, test, **kwargs):
        print('Hey')
                        
    def EmptyStatement(self, **kwargs):
        pass
        
    def ExpressionStatement(self, expression, **kwargs):
        self.emit('POP')
        self.emit(expression)
                
    def ForStatement(self, init, test, update, body, **kwargs):
        continue_label = self.exe.get_new_label()
        break_label = self.exe.get_new_label()
        first_start = self.exe.get_new_label()

        if init is not None:
            self.emit(init)
            print init,9
            if init['type'] != 'VariableDeclaration':
                self.emit('POP')

        # skip first update and go straight to test
        self.emit('JUMP', first_start)

        self.emit('LABEL', continue_label)
        self.emit(update)
        self.emit('POP')
        self.emit('LABEL', first_start)
        self.emit(test)
        self.emit('JUMP_IF_FALSE', break_label)

        # translate the body, remember to add and afterwards to remove implicit break/continue labels

        self.implicit_continues.append(continue_label)
        self.implicit_breaks.append(break_label)
        self.emit(body)
        self.implicit_continues.pop()
        self.implicit_breaks.pop()

        self.emit('JUMP', continue_label) # loop back
        self.emit('LABEL', break_label)
                                        
    def ForInStatement(self, left, right, body, **kwargs):
        raise NotImplementedError('Not available yet')
                                        
    def FunctionDeclaration(self, id, params, defaults, body, **kwargs):
        print('Hey')
                                                        
    def FunctionExpression(self, id, params, defaults, body, **kwargs):
        print('Hey')
                                                        
    def Identifier(self, name, **kwargs):
        if name=='true':
            self.emit('LOAD_BOOLEAN', 1)
        elif name=='false':
            self.emit('LOAD_BOOLEAN', 0)
        elif name=='undefined':
            self.emit('LOAD_UNDEFINED')
        else:
            self.emit('LOAD', name)
                
    def IfStatement(self, test, consequent, alternate, **kwargs):
        alt = self.exe.get_new_label()
        end = self.exe.get_new_label()
        # if
        self.emit(test)
        self.emit('JUMP_IF_FALSE', alt)
        # consequent
        self.emit(consequent)
        self.emit('JUMP', end)
        # alternate
        self.emit('LABEL', alt)
        if alternate is not None:
            self.emit(alternate)
        # end of if statement
        self.emit('LABEL', end)

                                
    def LabeledStatement(self, label, body, **kwargs):
        print('Hey')
                        
    def Literal(self, value, **kwargs):
        if value is None:
            self.emit('LOAD_NULL')
        elif isinstance(value, bool):
            self.emit('LOAD_BOOLEAN', int(value))
        elif isinstance(value, basestring):
            self.emit('LOAD_STRING', unicode(value))
        elif isinstance(value, (float, int, long)):
            self.emit('LOAD_NUMBER', float(value))
        elif isinstance(value, tuple):
            self.emit('LOAD_REGEXP', *value)

    def LogicalExpression(self, left, right, operator, **kwargs):
        end = self.exe.get_new_label()
        if operator == '&&':
            # AND
            self.emit(left)
            self.emit('JUMP_IF_FALSE_WITHOUT_POP', end)
            self.emit('POP')
            self.emit(right)
            self.emit('LABEL', end)
        elif operator == '||':
            # OR
            self.emit(left)
            self.emit('JUMP_IF_TRUE_WITHOUT_POP', end)
            self.emit('POP')
            self.emit(right)
            self.emit('LABEL', end)


    def MemberExpression(self, computed, object, property, **kwargs):
        if computed:
            self.emit(object)
            self.emit(property)
            self.emit('LOAD_MEMBER')
        else:
            self.emit(object)
            self.emit('LOAD_MEMBER_DOT', property['name'])
                                
    def NewExpression(self, callee, args, **kwargs):
        self.emit(callee)
        if args:
            n = len(args)
            for e in args:
                self.emit(e)
            self.emit('LOAD_N_TUPLE', n)
            self.emit('NEW')
        else:
            self.emit('NEW_NO_ARGS')

                        
    def ObjectExpression(self, properties, **kwargs):
        data = []
        for prop in properties:
            self.emit(prop['value'])
            if prop['computed']:
                raise NotImplementedError('ECMA 5.1 does not support computed object properties!')
            data.append((to_key(prop['key']), prop['kind'][0]))
        self.emit('LOAD_OBJECT', tuple(data))

    def PostfixExpression(self, operator, argument, prefix, **kwargs):
        incr = operator == "++"
        if argument['type'] == 'MemberExpression':
            if argument['computed']:
                pass

                                
    def Program(self, body, **kwargs):
        self.emit('LOAD_UNDEFINED')
        self.emit(body)
                
    def Pyimport(self, imp, **kwargs):
        raise NotImplementedError('Not available for bytecode interpreter yet, use translator.')
                        
    def Property(self, kind, key, computed, value, method, shorthand, **kwargs):
        raise NotImplementedError('Not available in ECMA 5.1')
                                                        
    def RestElement(self, argument, **kwargs):
        raise NotImplementedError('Not available in ECMA 5.1')
                
    def ReturnStatement(self, argument, **kwargs):
        if argument is None:
            self.emit('LOAD_UNDEFINED')
        else:
            self.emit(argument)
        self.emit('RETURN')
                
    def SequenceExpression(self, expressions, **kwargs):
        for e in expressions:
            self.emit(e)
            self.emit('POP')
        del self.exe.tape[-1]

    def SwitchCase(self, test, consequent, **kwargs):
        print('Hey')
                        
    def SwitchStatement(self, discriminant, cases, **kwargs):
        raise NotImplementedError('Will implement it tomorrow!')


    def ThisExpression(self, **kwargs):
        self.emit('LOAD_THIS')
        
    def ThrowStatement(self, argument, **kwargs):
        self.emit(argument)
        self.emit('THROW')
                
    def TryStatement(self, block, handler, finalizer, **kwargs):
        raise NotImplementedError('Will implement it tomorrow!')
                                                
    def UnaryExpression(self, operator, argument, **kwargs):
        if operator == 'typeof' and argument['type']=='Identifier':
            self.emit('TYPEOF', argument['name'])
        elif operator == 'delete':
            if argument['type'] == 'MemberExpression':
                self.emit(argument['object'])
                if argument['property']['type'] == 'Identifier':
                    self.emit('LOAD_STRING', unicode(argument['property']['name']))
                else:
                    self.emit(argument['property'])
                self.emit('DELETE_MEMBER')
            elif argument['type'] == 'Identifier':
                self.emit('DELETE', argument['name'])
            else:
                self.emit('LOAD_BOOLEAN', 1)
        elif operator in UNARY_OPERATIONS:
            self.emit(argument)
            self.emit('UNARY_OP', operator)
        else:
            raise MakeError('SyntaxError', 'Unknown unary operator %s' % operator)

                                
    def VariableDeclaration(self, declarations, kind, **kwargs):
        if kind != 'var':
            raise NotImplementedError('Only var variable declaration is supported by ECMA 5.1')
        for d in declarations:
            self.emit(d)

    def LexicalDeclaration(self, declarations, kind, **kwargs):
        raise NotImplementedError('Not supported by ECMA 5.1')
                        
    def VariableDeclarator(self, id, init, **kwargs):
        name = id['name']
        if  name in SPECIAL_IDENTIFIERS:
            raise MakeError('Invalid left-hand side in assignment')
        self.declared_vars.append(name);
        if init is not None:
            self.emit(init)
            self.emit('STORE', name)
            self.emit('POP')

                        
    def WhileStatement(self, test, body, **kwargs):
        continue_label = self.exe.get_new_label()
        break_label = self.exe.get_new_label()

        self.emit('LABEL', continue_label)
        self.emit(test)
        self.emit('JUMP_IF_FALSE', break_label)

        # translate the body, remember to add and afterwards remove implicit break/continue labels

        self.implicit_continues.append(continue_label)
        self.implicit_breaks.append(break_label)
        self.emit(body)
        self.implicit_continues.pop()
        self.implicit_breaks.pop()

        self.emit('JUMP', continue_label) # loop back
        self.emit('LABEL', break_label)


                        
    def WithStatement(self, object, body, **kwargs):
        raise NotImplementedError('Not implmented yet, wait 3 more days for it. Have to do my coursework :)')

    def _emit_statement_list(self, statements):
        for statement in statements:
            self.emit(statement)

    def emit(self, what, *args):
        ''' what can be either name of the op, or node, or a list of statements.'''
        if isinstance(what, basestring):
            return self.exe.emit(what, *args)
        elif isinstance(what, list):
            self._emit_statement_list(what)
        else:
            return getattr(self, what['type'])(**what)



from pyjsparser import parse
a = ByteCodeGenerator(Code())

a.emit(parse('''

for (var a = 0; a < 10; a += 1) {
a;}

'''))
print a.declared_vars
print a.exe.tape

from base import Scope

a.exe.compile()

print a.exe.run(Scope({}))



