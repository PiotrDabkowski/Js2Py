from ..base import *
from ..conversions import *
from ..func_utils import *
from pyjsparser import parse
from ..byte_trans import ByteCodeGenerator, Code




def Function(this, args):
    # convert arguments to python list of strings
    a = map(to_string, tuple(args))
    _body = u';'
    _args = ()
    if len(a):
        _body = u'%s;' % a[-1]
        _args = a[:-1]
    return executable_function(_body, _args, args.space, global_context=True)


# you can use this one lovely piece of function to compile and execute code on the fly! Watch out though as it may generate lots of code.
# todo tape cleanup? we dont know which pieces are needed and which are not so rather impossible without smarter machinery
def executable_function(_body, _args, space, global_context=True):

    func_str = u'(function (%s) { ; %s ; });' % (u', '.join(_args), _body)

    skip = space.byte_generator.exe.get_new_label()
    space.byte_generator.emit('JUMP', skip)
    space.byte_generator.emit(parse(func_str)['body'])
    space.byte_generator.emit('LABEL', skip)
    space.byte_generator.emit('NOP')
    space.byte_generator.exe.compile()

    ctx = space.GlobalObj if global_context else space.exe.current_ctx
    space.byte_generator.exe.tape[-1].eval(ctx)
    func = ctx.stack.pop()
    return func


def executable_code(code_str, space, global_context=True):
    start = space.byte_generator.exe.get_new_label()
    skip = space.byte_generator.exe.get_new_label()
    space.byte_generator.emit('JUMP', skip)
    space.byte_generator.emit('LABEL', start)
    space.byte_generator.emit(parse(code_str))
    space.byte_generator.emit('LABEL', skip)
    space.byte_generator.emit('NOP')
    space.byte_generator.exe.compile()

    ctx = space.GlobalObj if global_context else space.exe.current_ctx
    def ex_code():
        ret, status, token = space.byte_generator.exe.execute_fragment_under_context(ctx, start, skip)
        if status == 0:
            return ret
        elif status==3:
            raise token
        else:
            raise RuntimeError('Unexpected return status during JIT execution')
    return ex_code




def _eval(this, args):
    code_str = to_string(get_arg(args, 0))
    return executable_code(code_str, args.space, global_context=True)()

def log(this, args):
    print ' '.join(map(to_string, args))