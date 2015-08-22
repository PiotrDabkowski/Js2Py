from distutils.core import setup

setup(
    name='Js2Py',
    version='0.26',
    packages=['js2py', 'js2py.utils', 'js2py.prototypes', 'js2py.translators', 'js2py.constructors', 'js2py.host'],
    url='https://github.com/PiotrDabkowski/Js2Py',
    install_requires = ['tzlocal>=1.2'],
    license='GPL',
    author='Piotr Dabkowski',
    author_email='piotr.dabkowski@balliol.ox.ac.uk',
    description='JavaScript to Python translator'
)
