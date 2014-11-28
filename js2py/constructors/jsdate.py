from js2py.base import *
import datetime
import time

@Js
def Date(year, month, date, hours, minutes, seconds, ms):
    tmtup = tuple(datetime.datetime.utcnow().timetuple())
    return date_constructor(*tmtup).callprop('toString')

Date.Class = 'Date'


@Js
def date_constructor(year, month, date, hours, minutes, seconds, ms):
    raise NotImplementedError('Date is not implemented yet! Sorry!')


Date.create = date_constructor

