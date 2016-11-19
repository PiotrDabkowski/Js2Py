from simplex import *
from conversions import *


# ------------------------------------------------------------------------------
# Unary operations

# -x
def minus_uop(self):
    return -to_number(self)

# +x
def plus_uop(self):  # +u
    return to_number(self)

# !x
def logical_negation_uop(self):  # !u  cant do 'not u' :(
    return not to_boolean(self)

# typeof x
def typeof_uop(self):
    if is_callable(self):
        return 'function'
    typ = Type(self).lower()
    if typ == 'null':
        typ = 'object'  # absolutely idiotic...
    return typ

# ~u
def bit_invert_uop(self):
    return float(to_int32(~to_int32(self)))

# void
def void_op(self):
    return undefined


UNARY_OPERATIONS = {
    '+': plus_uop,
    '-': minus_uop,
    '!': logical_negation_uop,
    'typeof': typeof_uop,
    '~': bit_invert_uop,
    'void': void_op,
}

# ------------------------------------------------------------------------------
# ----- binary ops -------

# Bitwise operators
#  <<, >>,  &, ^, |, ~



# <<
def bit_lshift_op(self, other):
    lnum = to_int32(self)
    rnum = to_uint32(other)
    shiftCount = rnum & 0x1F
    return float(to_int32(lnum << shiftCount))

# >>
def bit_rshift_op(self, other):
    lnum = to_int32(self)
    rnum = to_uint32(other)
    shiftCount = rnum & 0x1F
    return float(to_int32(lnum >> shiftCount))

# >>>
def bit_bshift_op(self, other):
    lnum = to_uint32(self)
    rnum = to_uint32(other)
    shiftCount = rnum & 0x1F
    return float(to_uint32(lnum >> shiftCount))

# &
def bit_and_op(self, other):
    lnum = to_int32(self)
    rnum = to_int32(other)
    return float(to_int32(lnum & rnum))

# ^
def bit_xor_op(self, other):
    lnum = to_int32(self)
    rnum = to_int32(other)
    return float(to_int32(lnum ^ rnum))

# |
def bit_or_op(self, other):
    lnum = to_int32(self)
    rnum = to_int32(other)
    return float(to_int32(lnum | rnum))

# Additive operators
# + and - are implemented here

# +
def add_op(self, other):
    a = to_primitive(self)
    b = to_primitive(other)
    if a.TYPE == 'String' or b.TYPE == 'String':  # string wins hehe
        return a.to_string().value + b.to_string().value
    a = a.to_number()
    b = b.to_number()
    return a.value + b.value

# -
def sub_op(self, other):
    return to_number(self) - to_number(other)

# Multiplicative operators
# *, / and % are implemented here

# *
def mul_op(self, other):
    return to_number(self) * to_number(other)

# /
def div_op(self, other):
    a = to_number(self)
    b = to_number(other)
    if b:
        return a / float(b)  # ensure at least one is a float.
    if not a or a != a:
        return NaN
    return Infinity if a > 0 else -Infinity

# %
def mod_op(self, other):
    a = to_number(self)
    b = to_number(other)
    if abs(a) == Infinity or not b:
        return NaN
    if abs(b) == Infinity:
        return a
    pyres = a % b  # different signs in python and javascript
    # python has the same sign as b and js has the same
    # sign as a.
    if a < 0 and pyres > 0:
        pyres -= abs(b)
    elif a > 0 and pyres < 0:
        pyres += abs(b)
    return float(pyres)



# Comparisons
# <, <=, !=, ==, >=, > are implemented here.
def abstract_relational_comparison(self, other, self_first=True):
    ''' self<other if self_first else other<self.
       Returns the result of the question: is self smaller than other?
       in case self_first is false it returns the answer of:
                                           is other smaller than self.
       result is PyJs type: bool or undefined'''
    px = self.to_primitive('Number')
    py = other.to_primitive('Number')
    if not self_first:  # reverse order
        px, py = py, px
    if not (Type(px) == 'String' and Type(py) == 'String'):
        px, py = px.to_number(), py.to_number()
        if px.is_nan() or py.is_nan():
            return None
        return px.value < py.value  # same cmp algorithm
    else:
        # I am pretty sure that python has the same
        # string cmp algorithm but I have to confirm it
        return px.value < py.value

# <
def less_op(self, other):
    res = abstract_relational_comparison(self, other, True)
    if res is None:
        return False
    return res

# <=
def less_eq_op(self, other):
    res = abstract_relational_comparison(self, other, False)
    if res is None:
        return False
    return not res

# >=
def greater_eq_op(self, other):
    res = abstract_relational_comparison(self, other, True)
    if res is None:
        return False
    return not res

# >
def greater_op(self, other):
    res = abstract_relational_comparison(self, other, False)
    if res is None:
        return False
    return res


# equality

def abstract_equality_op(self, other):
    ''' returns the result of JS == compare.
       result is PyJs type: bool'''
    tx, ty = self.TYPE, other.TYPE
    if tx == ty:
        if tx == 'Undefined' or tx == 'Null':
            return True
        if tx == 'Number' or tx == 'String' or tx == 'Boolean':
            return self == other
        return self is other  # Object
    elif (tx == 'Undefined' and ty == 'Null') or (ty == 'Undefined' and tx == 'Null'):
        return True
    elif tx == 'Number' and ty == 'String':
        return abstract_equality_op(self, to_number(other))
    elif tx == 'String' and ty == 'Number':
        return abstract_equality_op(to_number(self), other)
    elif tx == 'Boolean':
        return abstract_equality_op(to_number(self), other)
    elif ty == 'Boolean':
        return abstract_equality_op(self, to_number(other))
    elif (tx == 'String' or tx == 'Number') and is_object(other):
        return abstract_equality_op(self, to_primitive(other))
    elif (ty == 'String' or ty == 'Number') and self.is_object():
        return abstract_equality_op(to_primitive(self), other)
    else:
        return False

def abstract_inequality_op(self, other):
    return not abstract_equality_op(self, other)


def strict_equality_op(self, other):
    typ = Type(self)
    if typ != Type(other):
        return False
    if typ == 'Undefined' or typ == 'Null':
        return True
    if typ == 'Boolean' or typ == 'String' or typ == 'Number':
        return self == other
    else:  # object
        return self is other  # Id compare.


def strict_inequality_op(self, other):
    return not strict_equality_op(self, other)

def instanceof_op(self, other):
    '''checks if self is instance of other'''
    if not hasattr(other, 'has_instance'):
        return False
    return other.has_instance(self)


def contains_op(self, other):
    '''checks if self contains other'''
    if not self.is_object():
        raise MakeError('TypeError', "You can\'t use 'in' operator to search in non-objects")
    return self.has_property(to_string(other).value)


BINARY_OPERATIONS = {
    '+': add_op,
    '-': sub_op,

    '*': mul_op,
    '/': div_op,
    '%': mod_op,

    '<<': bit_lshift_op,
    '>>': bit_rshift_op,
    '>>>': bit_bshift_op,
    '|': bit_or_op,
    '&': bit_and_op,
    '^': bit_xor_op,

    '==': abstract_equality_op,
    '!=': abstract_inequality_op,
    '===': strict_equality_op,
    '!==': strict_inequality_op,
    '<': less_op,
    '<=': less_eq_op,
    '>': greater_op,
    '>=': greater_eq_op,
}

