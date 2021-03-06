#               Copyright (c) 2021 Zenqi.

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys
import os
from importlib import import_module

def get_root_path(import_name: str) -> str:
    """
    Find the root path for the module.
    Argument:
        import_name (str):
            The name of the module to get the root path.
    """

    module = sys.modules.get(import_name)

    if module is not None and hasattr(module, "__file__"):
        return os.path.dirname(os.path.realpath(module.__file__))

def import_string(module: str):
    """
    Import the given module path.
    """

    try:
        _module, func = module.strip(' ').rsplit('.', 1)

    except ValueError:
        raise ImportError('It looks like module {} is not a valid module'.format(module))


    mod = import_module(_module)
    
    try:
        return (mod, getattr(mod, func))
    except AttributeError:
        # TODO: NO ATTRIBUTE
        raise ImportError('Module has no attribute: %s' % (func))
    