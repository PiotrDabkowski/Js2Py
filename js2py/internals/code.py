from opcodes import *
from space import *
from ctx import *

class Code:
    '''Can generate, store and run sequence of ops representing js code'''
    def __init__(self, is_strict=False):
        self.tape = []
        self.compiled = False
        self.label_locs = None
        self.is_strict = is_strict

        self.contexts = []
        self.return_locs = []
        self.__label_count = 0

    def get_new_label(self):
        self.__label_count += 1
        return self.__label_count

    def emit(self, op_code, *args):
        ''' Adds op_code with specified args to tape '''
        self.tape.append(OP_CODES[op_code](args))

    def compile(self):
        ''' Records locations of labels and compiles the code '''
        if self.compiled:
            return # already compiled
        self.label_locs = {}
        loc = 0
        while loc < len(self.tape):
            if type(self.tape[loc]) == LABEL:
                self.label_locs[self.tape[loc].num] = loc
                del self.tape[loc]
                continue
            loc += 1
        self.compiled = True

    def _call(self, func, this, args):
        ''' Calls a bytecode function func
            NOTE:  use !ONLY! when calling functions from native methods! '''
        assert not func.is_native
        # fake call - the the runner to return to the end of the file
        old_contexts = self.contexts
        old_return_locs = self.return_locs

        self.contexts = [FakeCtx()]
        self.return_locs = [len(self.tape)] # target line after return

        # todo prepare my ctx
        my_ctx = None

        # execute dunction
        ret = self.run(my_ctx, starting_loc=self.label_locs[func.code])

        # bring back old execution
        self.contexts = old_contexts
        self.return_locs = old_return_locs

        return ret


    def run(self, ctx, starting_loc=0):
        loc = starting_loc
        end = len(self.tape)
        while loc < end:
            # execute instruction
            status = self.tape[loc].eval(ctx)

            # check status for special actions
            if status is not None:
                if type(status) == int:  # jump to label
                    loc = self.label_locs[status]
                    continue

                elif len(status)==2:  # a call or a return!
                    # call: (new_ctx, func_loc_label_num)
                    if status[0] is not None:
                        # append old state to the stack
                        self.contexts.append(ctx)
                        self.return_locs.append(loc+1)
                        # set new state
                        loc = self.label_locs[status[1]]
                        ctx = status[0]
                        continue

                    # return: (None, None)
                    else:
                        return_value = ctx.stack.pop()
                        ctx = self.contexts.pop()
                        ctx.stack.append(return_value)

                        loc = self.return_locs.pop()
                        continue
            # next instruction
            loc += 1

        return ctx.stack.pop()

