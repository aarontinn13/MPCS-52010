CPU EMULATOR FOR MPCS 52010
===============================================================================
Run on Ubuntu 16.04
Created with Python 3.7 (Compiled with Cython for performance reasons)

The Project folder has 5 main modules:
  -Emulator.py
  -CPU.py
  -Cache.py
  -Ram.py
  -Address.py

The project also contains several .pyc extension files which are automatically created when importing these files as modules.

===============================================================================
Emulator.py
This is the main file that is run to generate all of the inputs and algorithms, it contains all of the inputs, algorithms, and settings which calls all of the functions directly.

CPU.py
Emulator creates an instance of the CPU which then creates the instance of every other module in the project. This is the brain which does all of the loading and storing and coordinating
between all of the other modules.

Cache.py
This is where the Cache data is stored and reads / writes are kept.

Ram.py
This is where all of the RAM data is stored.

Address.py
This is where all of the address conversions happen, it takes a raw integer address, converts it to byte for its respective part (i.e. Index, offset, tag), then converts that byte Address
to its integer value to find in the cache or RAM.

===============================================================================

Cython

Due to performance reasons (average an hour to run 480x480 MM algorithm) I needed to compile. 
