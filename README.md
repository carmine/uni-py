# uni-py
Code from various online courses (coursera, udacity, etc.), in python

# Prerequisites

## Virtualenv
- Installing IPython on the mac is [problematic](http://stackoverflow.com/questions/33004708/osx-el-capitan-sudo-pip-install-oserror-errno-1-operation-not-permitted).
- Probably better hygiene to use Virtualenv anyway.
- Instructions (assuming you have python and pip installed already):
```
pip install virtualenv
virtualenv class-env
source class-env/bin/activate
pip install IPython
```

# Links
1. [Idiomatic Python](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html)
2. [Python 101](http://www.davekuhlman.org/python_101.html)

# "Classes"
- [Python 101](http://www.davekuhlman.org/python_101.html)
  - Summary:
    - Useful if you've read about Python before and are just trying to refresh your memory.
  - Nuggets:
    - `In []:` - this is the IPython prompt
    - `In []: import this` - the zen of python
    - `flake8 package` - the modular source code checker: pep8, pyflakes and co
    - Tuples are like lists, but are not mutable.
    - range/xrange - xrange gone in 3.x. range creates whole list, xrange is a generator.
      - So, if you create 1B numbers, range chews up memory.
    - dictionary
      - Dictionary views mutate as the underlying dictionary mutates.
      - use `in`, `get` takes default value, `setdefault` to set value if doesn't exist
    - Files - use `with` to open file, and have it closed when done
    - `None` is a singleton. Use cases are similar to using nil / null.
    - id(obj) return integer ID of the object
    - Modules - finding them through sys.path, PYTHONPATH env.
    - And __iterator__ is something that satisfies the iterator protocol. Clue: If it's an iterator, you can use it in a for: statement.
    - A __generator__ is a class or function that implements an iterator, i.e. that implements the iterator protocol.
