Stacksim
========

Stacksim is a python package for simulating/visualizing stack operations. It also provides a sphinx extension for generating stack diagrams



CLI 
---


To run the cli, 

.. code::

    stacksim 

This will start the cli interface. Here is a quick example of some commands: 

.. code:: bash 

    (stacksim)>>  push etc: ... --size 64
    (stacksim)>>  call main(2, "hello" "world")
    (stacksim)>>  char buffer[64]
    (stacksim)>>  push i: 0x89 --note Same as 'int i = 0x89'
    (stacksim)>>  call printf("vars %d %d", 17, 38)
    (stacksim)>>  function myFunction(int a, int b)
    (stacksim)>>  call myFunction(56,78)




.. image:: doc/assets/images/stack1.png


Because this is really just a tool for visualization, types are not strictly defined or used. For instance `push "hello world"` will add a single  "word" (32 bits by default) to the stack, but show the value as "hello world"

Push 
~~~~

push will push a single `stack cell` onto the stack. A cell contains one or more words. Each cell can have a label, note, and words

.. code::

    push arg1: 0x56                 #Shortcut for 'push 0x56 --label arg1'
    push --label buffer --size 64   #creates a 64 word cell with no specified data 
    push buf: 1,2,3,4,5             #creates a 5 word cell with the values filled in 
    push <main+0x54> --note return  #creates a single word on the stack with no label, and a note

Pop
~~~

pop will remove words from the stack 

.. code:: 

    pop             #remove a single word 
    pop 4           #remove 4 words 
    pop frame       #remove current frame 


ret 
~~~

ret will pop one word and set the instruction pointer to the value popped. 

.. note:: the `CallingConvention` has a concept of registers, but they are not utilized/shown yet

Functions 
~~~~~~~~~

The ``call`` command gets run through a `CallingConvention` subclass (currently only cdecl is available) and performs operations according to the convention: 

- push arguments to stack 
- create a new stack frame 
- pushes return address 


You can declare functions to give the app context about argument type/size and labels, but you can also call arbitrary functions. It will just assume all arguments are a single row on the stack. 

.. code:: 

    function myFunction(int a, int b)
    call myFunction(41,32)

    call undeclareFunction(1,2,3,4)     # Will assume all args are 32 bit values and label arg1, arg2, arg3, etc

.. note:: A lot of common functions from libc are already loaded in. 

Sphinx
------

.. important:: not yet implemented 


This package also contains an extension for sphinx. Add the extension in `conf.py` and then you can use the `stack` directive 


.. code:: rst 

    .. stack:: 
        :showAddresses: 

        push etc: ... --size 64
        call main(2, "hello" "world")
        char buffer[64]
        call printf("vars %d %d", 17, 38)
        function myFunction(int a, int b)
        call myFunction(56,78)
