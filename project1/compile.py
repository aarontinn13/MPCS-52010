from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [ Extension("Emulator", ["Emulator.py"]),
                Extension("Cache", ["Cache.py"]),
                Extension("CPU", ["CPU.py"]),
                Extension("RAM", ["RAM.py"]),
                Extension("Address", ["Address.py"]),
                Extension("main", ["main.py"])]

setup(name= "Cache Emulator", cmdclass={'build_ext': build_ext}, ext_modules=ext_modules)