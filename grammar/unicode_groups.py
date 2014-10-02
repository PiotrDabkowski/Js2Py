import unicodedata
from collections import defaultdict
import sys

def unicode_chr(x):
    return eval("u'\\u"+((6-len(hex(x)))*'0'+hex(x)[2:])+"'")

uc = defaultdict(list)
for c in map(unicode_chr, xrange(sys.maxunicode + 1)):
    uc[unicodedata.category(c)].append(c)

UnicodeLetter = uc['Lu']+ uc['Ll']+ uc['Lt'] + uc['Lm'] + uc['Lo'] + uc['Nl']
UnicodeCombiningMark = uc['Mn'] + uc['Mc']
UnicodeDigit = uc['Nd']
UnicodeConnectorPunctuation = uc['Pc']

IdentifierPart = UnicodeLetter + UnicodeCombiningMark + UnicodeDigit + UnicodeConnectorPunctuation
