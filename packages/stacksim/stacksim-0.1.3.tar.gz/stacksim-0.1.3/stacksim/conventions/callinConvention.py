
from stacksim.stack import Stack, StackFrame, StackCell 
from stacksim.function import Function, FunctionArgument
import re

class Register():
    def __init__(self, name, size, description):
        self.name = name
        self.size = size
        self.type = type
        self.value = None
        self.description = None


class CallingConvention():
    """
        Base Class for calling conventions
    """
    def __init__(self, name, session = None):
        self.name = name
        self.stack = Stack()
        self.wordSize = 4
        self.endian = 'little'
        self.registers = {}
        self.session = session

    def setInstructionPointer(self, val):
        pass

    def pop(self):
       return self.stack.pop()

    def push(self,cell):
        self.stack.push(cell)
    
    def popFrame(self):
       return self.stack.popFrame()
    
    def pushFrame(self, frame):
        self.stack.pushFrame(frame)


    def call(self, callLine):


        regex = re.compile(r"(\S.*?)\((.*?)\)")

        match = regex.match(callLine)

        func : Function = None

        if match:

            functionName = match.group(1)

            args = match.group(2)

            if args.strip() == "":
                args = []
            else:
                args = match.group(2).split(',')






            if functionName in self.session.functions:

                func  = self.session.functions[functionName]
                
                for i in reversed(range(len(args))):
                    label = f'{functionName}.arg{i+1}'
                    if i < len(func.args) and func.args[i].name: 
                        label = func.args[i].name
                    

                    cell = StackCell(  label, [args[i].strip()])
                    self.stack.push(cell)


            else:
                for i in reversed(range(len(args))):

                    label = f'{functionName}.arg{i+1}'

                    cell = StackCell(  label, [args[i].strip()])

                    self.stack.push(cell)

            currentFunction = self.session.getCurrentFunction()

            self.stack.pushFrame(StackFrame(functionName))
            

            retCell = StackCell('ret', ['< ret to caller >'])
            if currentFunction:

                if isinstance(currentFunction, Function):
                    
                    retCell.setWords(f'< ret to {currentFunction.name} >')
                else:
                    retCell.setWords(f'< ret to {currentFunction} >')

            self.stack.push(retCell)

            if func:
                for local in func.locals:
                    cell = self.session.tryParseLocalVar(local)
                    if cell:
                        self.stack.push(cell)

        

