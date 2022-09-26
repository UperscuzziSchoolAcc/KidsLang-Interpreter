"""
KidsLang Interpreter, made by Greyson Rowland (2022)
"""

import re, time

error = False
mainLoop = 0
f = open("myCode.kl")
lines = f.readlines()
variables = {"answer": "there is no answer yet"}

def throwError(statement):
    global error
    error = True
    print("Error on line",str(mainLoop + 1) + ":",statement)
    
def computeOperations(command):
    spl = command.split()
    locLoop = 0
    while locLoop < len(spl):
        op = spl[locLoop]
        if op == "+":
            try:
                ta = str(int(spl[locLoop - 1]) + int(spl[locLoop + 1]))
                spl[locLoop - 1] = ta
                spl.pop(locLoop)
                spl.pop(locLoop)
                locLoop -= 1
            except:
                throwError("You can't add a letter with a number.")
        if op == "-":
            try:
                ta = str(int(spl[locLoop - 1]) - int(spl[locLoop + 1]))
                spl[locLoop - 1] = ta
                spl.pop(locLoop)
                spl.pop(locLoop)
                locLoop -= 1
            except:
                throwError("You can't subtract a letter with a number.")
        if op == "*":
            try:
                ta = str(int(spl[locLoop - 1]) * int(spl[locLoop + 1]))
                spl[locLoop - 1] = ta
                spl.pop(locLoop)
                spl.pop(locLoop)
                locLoop -= 1
            except:
                throwError("You can't multiply a letter with a number.")
        if op == "/":
            try:
                ta = str(int(spl[locLoop - 1]) / int(spl[locLoop + 1]))
                spl[locLoop - 1] = ta
                spl.pop(locLoop)
                spl.pop(locLoop)
                locLoop -= 1
            except:
                throwError("You can't divide a letter with a number.")
        if op == "..":
            ta = str(spl[locLoop - 1]) + str(spl[locLoop + 1])
            spl[locLoop - 1] = ta
            spl.pop(locLoop)
            spl.pop(locLoop)
            locLoop -= 1
        if op == "__":
            ta = str(spl[locLoop - 1]) + " " + str(spl[locLoop + 1])
            spl[locLoop - 1] = ta
            spl.pop(locLoop)
            spl.pop(locLoop)
            locLoop -= 1
        if op == "=":
            if str(spl[locLoop - 1]) == str(spl[locLoop + 1]):
                spl[locLoop - 1] = "True"
            else:
                spl[locLoop - 1] = "False"
            spl.pop(locLoop)
            spl.pop(locLoop)
            locLoop -= 1
        if op == "!=":
            if str(spl[locLoop - 1]) != str(spl[locLoop + 1]):
                spl[locLoop - 1] = "True"
            else:
                spl[locLoop - 1] = "False"
            spl.pop(locLoop)
            spl.pop(locLoop)
            locLoop -= 1
        if op == ">":
            try:
                if int(spl[locLoop - 1]) > int(spl[locLoop + 1]):
                    spl[locLoop - 1] = "True"
                else:
                    spl[locLoop - 1] = "False"
                spl.pop(locLoop)
                spl.pop(locLoop)
                locLoop -= 1
            except:
                throwError("You cant use that operator on a letter and a number")
        if op == "<":
            try:
                if int(spl[locLoop - 1]) < int(spl[locLoop + 1]):
                    spl[locLoop - 1] = "True"
                else:
                    spl[locLoop - 1] = "False"
                spl.pop(locLoop)
                spl.pop(locLoop)
                locLoop -= 1
            except:
                throwError("You cant use that operator on a letter and a number")
        if op == "/+":
            spl[locLoop] = "+"
        if op == "/-":
            spl[locLoop] = "-"
        if op == "/*":
            spl[locLoop] = "*"
        if op == "//":
            spl[locLoop] = "/"
        if op == "/..":
            spl[locLoop] = ".."
        if op == "/__":
            spl[locLoop] = "__"
        if op == "/=":
            spl[locLoop] = "="
        if op == "/!=":
            spl[locLoop] = "!="
        if op == "/>":
            spl[locLoop] = ">"
        if op == "/<":
            spl[locLoop] = "<"
        locLoop += 1
    return " ".join(spl)

def getLoopParts(loop):
    global mainLoop
    toRet = []
    i = loop + 1
    while lines[i - 1] != "end":
        toRet.append(lines[i].strip())
        i += 1
        mainLoop += len(toRet)
    toRet.pop()
    return toRet

def convertVariables(command):
    a = command.split()
    for i in range(len(a)):
        if variables.get(a[i]) != None:
            a[i] = variables.get(a[i])
        elif a[i][1:len(a[i])] in variables.keys() != None and a[i][0] == "/":
            a[i] = a[i][1:len(a[i])]
    return " ".join(a)

def execute(command, loop, run):
    ss = command.split()
    command = command.strip()
    if ss[0] != "make":
        command = convertVariables(command)
    else:
        FH = ss[0:2]
        SH = convertVariables(" ".join(ss[2:len(ss)]))
        command = " ".join(FH) + " " + "".join(SH)
    command = computeOperations(command)
    ss = command.split()
    s = re.split(r'(\s+)', command)
    if s[0] == "say":
        if run == True:
            print("".join(s[1:len(s)]))
    elif s[0] == "--":
        if run == True:
            pass
    elif s[0] == "make":
        if run == True:
            variables[ss[1]] = "".join(s[3:len(s)]).strip()
    elif s[0] == "repeat":
        if run == True:
            toRep = getLoopParts(mainLoop)
            for a in range(int(ss[1])):
                for b in range(len(toRep)):
                    execute(toRep[b], loop, True)
    elif s[0] == "wait":
        if run == True:
            try:
                time.sleep(int(ss[1]))
            except:
                throwError("You cannot wait with a letter!")
    elif s[0] == "ask":
        if run == True:
            variables["answer"] = input("".join(s[1:len(s)]) + " ")
    else:
         return "error"   

while mainLoop < len(lines):
    if error:
        break
    command = lines[mainLoop]
    if execute(command, mainLoop, False):
        print("Error on line " + str(mainLoop + 1) + ", did you spell something wrong?")
        break
    execute(command, mainLoop, True)
    mainLoop += 1
