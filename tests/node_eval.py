import subprocess
from tempfile import  NamedTemporaryFile
import six
import re
import os

class NodeJsError(Exception):
    pass

def node_eval_js(code):
    ERR_MARKER = "<<<ERROR_MARKER>>>"
    ERR_REGEXP = ERR_MARKER + r'([\s\S]*?)' + ERR_MARKER
    interceptor_code = """
    try {
        var res = eval(%s);
        console.log(res);
    } catch (e) {
        throw new Error(getErrMarker() + e + getErrMarker())
    }
    function getErrMarker() {
        return %s;
    }
    """ % (repr(code), repr(ERR_MARKER))
    f = NamedTemporaryFile(delete=False, suffix='.js')
    f.write(interceptor_code.encode('utf-8') if six.PY3 else interceptor_code)
    f.close()
    p = subprocess.Popen(['node', f.name], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = map(lambda x: x.decode('utf-8') if six.PY3 else x, p.communicate())
    os.unlink(f.name)
    if not p.returncode:
        return out
    # try to get clear error message
    match = re.search(ERR_REGEXP, err)
    if match and len(match.groups()) == 1:
        raise NodeJsError(match.groups()[0])
    else:
        raise NodeJsError(err)


if __name__ == '__main__':
    print(node_eval_js('x = 5;x'))