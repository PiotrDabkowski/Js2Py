from distutils.core import setup

long_desc = '''Translates JavaScript to Python code. Js2Py is able to translate and execute virtually any JavaScript code.

Js2Py is written in pure python and does not have any dependencies. Basically an implementation of JavaScript core in pure python.


    import js2py

    f = js2py.eval_js( "function (name) {return name.length}" )

    f("Piotr")

    # returns 5


More examples at: https://github.com/PiotrDabkowski/Js2Py
'''

setup(
    name='Js2Py',
    version='0.30',
    packages=['js2py', 'js2py.utils', 'js2py.prototypes', 'js2py.translators', 'js2py.constructors', 'js2py.host'],
    url='https://github.com/PiotrDabkowski/Js2Py',
    install_requires = ['tzlocal>=1.2'],
    license='MIT',
    author='Piotr Dabkowski',
    author_email='piotr.dabkowski@balliol.ox.ac.uk',
    description='JavaScript to Python Translator & JavaScript interpreter written in 100% pure Python.',
    long_description=long_desc
)
