
from staq.stack import Stack, StackFrame, StackCell 
from staq.function import Function, FunctionArgument
from termcolor import colored
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
    def __init__(self, name, session = None, stack = None):
        self.name = name
        self.endian = 'little'
        self.registers = {}
        self.session = session
        self.stack : Stack = stack


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

    def getReg(self, key):
        if key in self.registers:
            return self.registers[key].value
        
        return None
    
    def setReg(self,key, value):

        if key in self.registers:
            self.registers[key].value = value

    def leave(self):

        if self.stack.currentFrame:
            while self.stack.currentFrame.length() > 1:
                self.stack.pop()
            
            while self.stack.currentFrame.cells[0].size > 1:
                self.stack.pop()


    def ret(self):
        word = self.stack.pop()

        if word:
            self.setInstructionPointer(word.value)

    def registersToAnsi(self, width = 30, color='yellow'):

        #  ┌───────────────────────────────────┐
        #  │ esp: <value>                     │
        #  │ ebp: <value>                     │
        #  │ eax: <value>                     │
        #  │ ebx: <value>                     │
        #  └───────────────────────────────────┘

        #get the max length of the register names
        maxNameLength = 0
        for key in self.registers:
            if len(key) > maxNameLength:
                maxNameLength = len(key)
        
        maxValLength =  width - (maxNameLength + 5)

        out = colored(f"┌{'─' * maxNameLength}{'─' * (maxValLength +5)}┐\n", color)
        for key in self.registers:
            if self.registers[key].value:

                strVal = str(self.registers[key].value)

                truncVal = strVal.ljust(maxValLength)[:maxValLength]
                out += colored(f"│ {key.rjust(maxNameLength)} : {truncVal} │\n", color)

        out += colored(f"└{'─' * maxNameLength}{'─' * (maxValLength + 5)}┘\n", color)

        return out


    def call(self, callLine):


        regex = re.compile(r"(\S.*?)\((.*?)\)")

        match = regex.match(callLine)

        func : Function = None

        if match:

            functionName = match.group(1)

            args = match.group(2)

        else:
            functionName = callLine
            args = ""

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
        

        retCell = StackCell('ret', ['< ret to ??? >'])
        if currentFunction:

            if isinstance(currentFunction, Function):
                
                retCell.setWords(f'< {currentFunction.name}+?? >')
            else:
                retCell.setWords(f'< {currentFunction}+?? >')

        self.stack.push(retCell)

        if func:
            for local in func.locals:
                cell = self.session.tryParseLocalVar(local)
                if cell:
                    self.stack.push(cell)

        

    