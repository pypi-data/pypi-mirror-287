
from stacksim.cdeclConvention import CdeclConvention
from stacksim.stack import Stack, StackFrame, StackCell
from stacksim.function import Function, FunctionArgument, parseCFile
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
    "int8": 1,
    "uint8": 1,
    "int16": 2,
    "uint16": 2,
    "int32": 4,
    "uint32": 4,
    "int64": 8,
    "uint64": 8,
}


class StackSession():
    def __init__(self):
        self.conv = CdeclConvention(self)
        self.stack = self.conv.stack
        self.functions = {}
        self.parser = argparse.ArgumentParser(description='Stack Visualizer')
        self.init_args()
        self.loadLibcFuntions()
        self.commands = []

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
            elif args.count.lower() == 'locals':
                self.stack.popLocals()
            elif args.count.lower() == 'all':
                self.stack.clear()
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
            cell.setSize(args.size)
        
        if args.label:
            cell.label = args.label

        if args.address:
            cell.address = args.address

        if args.note:

            note = " ".join(args.note)

            cell.setNote(note)



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
    
    def tryParseLocalVar(self, line):
        
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
            parts[1] = parts[1].split("--")[0]
            val = parts[1].replace(";","")
            val = yaml.safe_load(val)

        if match:
            varType = match.group(1).strip()

            varName = match.group(2)

            arraySize = match.group(4) if match.group(4) else None

            cell = StackCell(varName)

            if "_t" in varType:
                varType = varType.replace("_t","")

            if varType not in sizeDict:
                return None
            
            if ptr:
                sizeBytes = 4
            else:
                sizeBytes = sizeDict.get(varType, 4)

            if arraySize:
                sizeBytes = sizeBytes * int(arraySize)
            
            size = int((sizeBytes + 3) / 4)

            cell.setWords(val)
            cell.setSize(size)
            cell.label = varName


            line = line.replace(match.group(0), 'local')


            return cell

        else:
            return None
            
    def localCmd(self, cell, args):

        if args.note:
            cell.setNote(" ".join(args.note))

        if args.color:
            cell.color = args.color

        self.stack.push(cell)

    def saveCmd(self, args):
        filename = args.filename


        with open(filename, 'w') as f:
            if filename.endswith('.lst'):
                for cmd in self.commands:
                    if not cmd.startswith("save"):
                        if not cmd.endswith("\n"):
                            cmd += "\n"
                        f.write(cmd)
            
            elif filename.endswith('.html'):

                f.write(self.stack.toHtml())

                
        


    def loadCmd(self, args):
        filename = args.filename

        if filename.endswith('.c'):
            functions = parseCFile(filename)
            for func in functions:
                self.addFunction(func)

    def writeCmd(self, args):

        valLine = " ".join(args.values)
        values = valLine.split(",")

        #strip 
        values = [x.strip() for x in values]

        address  = None

        if args.address:
            address = args.address

        self.stack.write(values, address)


    def noteCmd(self, args):
        note = " ".join(args.note)
        self.stack.setNote(note, args.address, args.color)

    def run(self, callLine = None, limit = 20):

        called = True

        functionCall = None
        
        if callLine:
            callLine = callLine.strip()
            if callLine == "":
                callLine = None

        if callLine:
            functionCall = callLine
        elif self.stack.currentFrame and self.stack.currentFrame.function:
            functionName = self.stack.currentFrame.function

            if functionName in self.functions:
                function = self.functions[functionName]
                if len(function.calls) > 0:
                    functionCall  = function.calls[0]

        if not functionCall:
            functionCall = "main()"

        self.conv.call(functionCall)
        limit -= 1

        while  called and (limit > 0):
            
            if self.stack.currentFrame and self.stack.currentFrame.function: 
                functionName = self.stack.currentFrame.function

                if functionName in self.functions:
                    function = self.functions[functionName]

                    if len(function.calls) > 0:
                        call = function.calls[0]
                        self.conv.call(call)
                        called = True

            limit -= 1

    def runCmd(self, args):

        call = None
        if args.function:
            call = " ".join(args.function)


        self.run(call, limit = args.limit)

    def parseCommand(self, line):

        self.commands.append(line)

        local = self.tryParseLocalVar(line)

        if local:
            line = f"local {line}"
            args = self.parser.parse_args(line.split(" "))
            self.localCmd(local, args)
        else:
            args = self.parser.parse_args(line.split(" "))

            #print(args)
            args.func(args)

    



    # Initialize the argument parser
    def init_args(self):

        subparsers = self.parser.add_subparsers(dest='command', help='sub-command help')


        #local command 
        local_parser = subparsers.add_parser('local', help='local help')
        local_parser.add_argument('local', nargs='*', help='Local variable declaration')
        local_parser.add_argument('--note','-n', nargs='*', help='Note for the cell')
        local_parser.add_argument('--color', '-c', type=str, help="Color of the cell")
        local_parser.set_defaults(func=self.localCmd)

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
        push_parser.add_argument('--size', '-s', type=int, help='Type of value')
        push_parser.add_argument('--label','-l', help='Label for the value')
        push_parser.add_argument('--address','-a', help='Address for the value')
        push_parser.add_argument('--note','-n', nargs='*', help='Note for the value')
        push_parser.set_defaults(func=self.pushCmd)

        #frame command
        frame_parser = subparsers.add_parser('frame', help='frame help')
        frame_parser.add_argument('name',  help='Name of the frame')
        frame_parser.add_argument('--color', '-c', help='Color of the frame')
        frame_parser.add_argument('--address', '-a', help='address of the frame ')
        frame_parser.add_argument('--size', '-s', type=int, help='size of the frame')
        frame_parser.set_defaults(func=self.frameCmd)

        #call parser
        call_parser = subparsers.add_parser('call', help='call help')
        call_parser.add_argument('function', nargs="*", help='Function to call')
        call_parser.set_defaults(func=self.callCmd)

        #function 
        function_parser = subparsers.add_parser('function', help="function help")
        function_parser.add_argument('function', nargs="*", help='Function signature')
        function_parser.set_defaults(func=self.functionCmd)

        #save 
        save_parser = subparsers.add_parser('save', help='save help')
        save_parser.add_argument('filename', nargs="?", type=str, help='Filename to save', default='.stack.lst')
        save_parser.set_defaults(func=self.saveCmd)

        #load
        load_parser = subparsers.add_parser('load', help='load help')
        load_parser.add_argument('filename', type=str, help='Filename to load')
        load_parser.set_defaults(func=self.loadCmd)

        #run 
        run_parser = subparsers.add_parser('run', aliases=['r'], help='run help')
        run_parser.add_argument('function', nargs="*", help='Function call to start, if not provided will use the first call in the current function, or main if no function is active')
        run_parser.add_argument('--limit', '-l', type=int, help='Limit of calls to make', default=20)
        run_parser.set_defaults(func=self.runCmd)

        #write 
        write_parser = subparsers.add_parser('write', aliases=['w','wr'], help='write help')
        write_parser.add_argument('values', nargs="*", help='Values to write')
        write_parser.add_argument('--address', '-a', type=str, help='Address to write to can be a reference to a cell &<cellName>+4')
        write_parser.add_argument('--count', '-c', type=int, help='Repeated writes', default=1)
        write_parser.add_argument('--file', '-f', type=str, help='binary file to write')
        write_parser.set_defaults(func=self.writeCmd)


        #note
        note_parser = subparsers.add_parser('note', help='note help')
        note_parser.add_argument('note', nargs="*", help='Note to add')
        note_parser.add_argument('--color', '-c', type=str, help='Color of the note', default='red')
        note_parser.add_argument('--address', '-a', type=str, help='Address of the note')
        note_parser.set_defaults(func=self.noteCmd)


