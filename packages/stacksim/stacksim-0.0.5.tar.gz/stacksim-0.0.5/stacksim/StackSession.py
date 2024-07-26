
from stacksim.CdeclConvention import CdeclConvention
from stacksim.Stack import Stack, StackFrame, StackCell
from stacksim.function import Function, FunctionArgument
import re
import yaml
import json
import argparse


libc_functions = [
    "int main(int argc, char* argv)",

    "int printf(const char *format, ...);",
    "int scanf(const char *format, ...);",
    "FILE *fopen(const char *filename, const char *mode);",
    "int fclose(FILE *stream);",
    "size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);",
    "size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream);",
    "void *malloc(size_t size);",
    "void free(void *ptr);",
    "void *memcpy(void *dest, const void *src, size_t n);",
    "void *memset(void *s, int c, size_t n);",
    "char *strcpy(char *dest, const char *src);",
    "size_t strlen(const char *s);",
    "int strcmp(const char *s1, const char *s2);",
    "char *strcat(char *dest, const char *src);",
    "int atoi(const char *str);",
    "void exit(int status);",
    "void qsort(void *base, size_t nmemb, size_t size, int (*compar)(const void *, const void *));",
    "void *bsearch(const void *key, const void *base, size_t nmemb, size_t size, int (*compar)(const void *, const void *));",
]


sizeDict = {
    "void": 0,
    "char": 1,
    "unsigned char": 1,
    "signed char": 1,
    "short": 2,
    "unsigned short": 2,
    "int": 4,
    "unsigned int": 4,
    "long": 4,
    "unsigned long": 4,
    "long long": 8,
    "unsigned long long": 8,
    "float": 4,
    "double": 8,
    "long double": 16,  # This can vary, but 16 bytes is a common size
    "int8_t": 1,
    "uint8_t": 1,
    "int16_t": 2,
    "uint16_t": 2,
    "int32_t": 4,
    "uint32_t": 4,
    "int64_t": 8,
    "uint64_t": 8,
}


class StackSession():
    def __init__(self):
        self.conv = CdeclConvention(self)
        self.stack = self.conv.stack
        self.functions = {}
        self.parser = argparse.ArgumentParser(description='Stack Visualizer')
        self.init_args()
        self.loadLibcFuntions()

    def loadYaml(self, obj):


        if isinstance(obj, str):
            with open(obj) as f:
                obj = yaml.safe_load(f)


        order = 'normal'

        if 'stackBase' in obj:
            self.stack.baseAddress = obj['stackBase']
        
        if 'order' in obj:
            order = obj['order']

        if 'functions' in obj:
            for func in obj['functions']:
                self.addFunction(Function.fromString(func))
    

        if 'stack' in obj:

            nodes = []
            if order == 'normal':
                nodes = reversed(obj['stack'])
            else:
                nodes = obj['stack']

            for node in nodes:
                
               if isinstance(node, dict) and 'function' in node:
                   #Create a new frame 
                   frame = StackFrame.fromObj(node, order= order)
                   self.stack.pushFrame(frame)
                   self.stack.currentFrame = None
               else:
                    cell = StackCell.fromObj(node)
                    self.stack.push(cell)
        
        self.stack.applyAddresses()


    
    def getCurrentFunction(self):

        if self.stack.currentFrame:

            if self.stack.currentFrame.function:
                return self.stack.currentFrame.function
            
        
        return None

    def addFunction(self, function):
        self.functions[function.name] = function


    def loadLibcFuntions(self):
        
        for f in libc_functions:
            newFunc = Function.fromString(f)

            self.addFunction(newFunc)

    def parseFrame(self,words):
        
        line = " ".join(words[1:])
        self.stack.pushFrame(StackFrame(line))

    def frameCmd(self, args):
        frame = StackFrame(args.name)
        if args.color:
            frame.color = args.color
        self.stack.pushFrame(frame)

    def popCmd(self, args):

        if args.count and isinstance(args.count,str):
            if args.count.lower() == 'frame':
                self.stack.popFrame()
            else:
                count = int(args.count)
                self.stack.pop(count)
        else:
            self.stack.pop()

    def retCmd(self, args):

        ret = self.stack.pop()
        self.conv.setInstructionPointer(ret)

    def pushCmd(self, args):
        cell = StackCell()

        if args.value:

            line = " ".join(args.value)

            parts = line.split(":")

            if len(parts) > 1:
                cell.label = parts[0]

                words = parts[1].strip().split(",")
                words = [x.strip() for x in words]

                cell.setWords(words)
            else:
                words = parts[0].split(",")
                words = [x.strip() for x in words]
                cell.setWords(parts[0].split(","))


        if args.size:
            cell.size = args.size
        
        if args.label:
            cell.label = args.label

        if args.address:
            cell.address = args.address

        if args.note:

            note = " ".join(args.note)

            cell.note = note



        self.stack.push(cell)


    def parseFunction(self, line):

        function = Function.fromString(line)
        self.addFunction(function)

   
    def callCmd(self, args):
            

            line = " ".join(args.function)
    
            self.conv.call(line)

    def functionCmd(self,args):
        line = " ".join(args.function)
        function = Function.fromString(line)
        self.addFunction(function)
    
    def parseLocalVar(self, line):
        
        parts = line.split("=")

        
        revar = re.compile(r"(\w[\w\s\*]*\w)\s+(\w+)(\[(\d*)\])?")

        ptr = False

        decl = parts[0]
        if "*" in decl:
            ptr = True
            decl = decl.replace("*","")

        match = revar.match(decl)
        val = []
        if len(parts) > 1:
            val = parts[1].replace(";","")
            val = yaml.safe_load(val)

        if match:
            varType = match.group(1).strip()

            varName = match.group(2)

            arraySize = match.group(4) if match.group(4) else None

            cell = StackCell(varName)

            if varType not in sizeDict:
                return False
            
            if ptr:
                sizeBytes = 4
            else:
                sizeBytes = sizeDict.get(varType, 4)

            if arraySize:
                sizeBytes = sizeBytes * int(arraySize)
            
            size = int((sizeBytes + 3) / 4)

            cell.setWords(val)
            cell.size = size 
            cell.label = varName

            self.stack.push(cell)
            return True

        else:
            return False

            

    
    def parseCommand(self, line):
        """
            Handles a command 

            #Define a function
            function addTwo@0x454545(int a, int b)

            #Push to the stack
            push 0x00000001 # Push a single word 
            push [1,23,4,5] # Push multiple words 
            push "sting of data" Push a string  
            push 0x00*45  push 45 words of same value 
            push [1,2,3]*45 push 

            #Pop from the stack
            pop
            pop 4 # pop 4 words 
            pop frame # pop the current frame

            #Call a defined Function 
            call addTwo 4 5 

            #Call undefined function 
            call addThree[0x455677] int32:45 int32:34 int32:456
        """

        #check if its a variable 
        if not self.parseLocalVar(line):

            args = self.parser.parse_args(line.split(" "))

            #print(args)
            args.func(args)


    # Initialize the argument parser
    def init_args(self):

        subparsers = self.parser.add_subparsers(dest='command', help='sub-command help')

        # pop command
        pop_parser = subparsers.add_parser('pop', help='pop help')
        pop_parser.add_argument('count', type=str, nargs='?', help='Number of elements to pop', default=1)
        pop_parser.set_defaults(func=self.popCmd)

        #ret command
        ret_parser = subparsers.add_parser('ret', help='ret help')
        ret_parser.set_defaults(func=self.retCmd)
        
        #push command
        push_parser = subparsers.add_parser('push', help='push help')
        push_parser.add_argument('value', nargs='*', help='Value to push', default='')
        push_parser.add_argument('--size', type=int, help='Type of value')
        push_parser.add_argument('--label','-l', help='Label for the value')
        push_parser.add_argument('--address','-a', help='Address for the value')
        push_parser.add_argument('--note','-n', nargs='*', help='Note for the value')
        push_parser.set_defaults(func=self.pushCmd)

        #frame command
        frame_parser = subparsers.add_parser('frame', help='frame help')
        frame_parser.add_argument('name', help='Name of the frame')
        frame_parser.add_argument('--color', help='Color of the frame')
        frame_parser.set_defaults(func=self.frameCmd)

        #call parser
        call_parser = subparsers.add_parser('call', help='call help')
        call_parser.add_argument('function', nargs="*", help='Function to call')
        call_parser.set_defaults(func=self.callCmd)

        #function 
        function_parser = subparsers.add_parser('function', help="function help")
        function_parser.add_argument('function', nargs="*", help='Function signature')
        function_parser.set_defaults(func=self.functionCmd)