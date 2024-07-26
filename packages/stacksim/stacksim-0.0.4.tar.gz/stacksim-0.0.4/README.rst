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


Functions 
~~~~~~~~~

You can declare functions to give the app context about argument type/size and labels, but you can also call arbitrary functions. It will just assume all arguments are a single row on the stack. 

A lot of common functions from libc are already loaded in. 

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
