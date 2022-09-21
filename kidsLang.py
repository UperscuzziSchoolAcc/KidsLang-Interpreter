"""
KidsLang Interpreter, made by Greyson Rowland (2022)
"""
import time
f = open("myCode.kl")
lines = f.readlines()
i = 0
variables = {}
def incrementI(n):
    global i
    i += int(n)
def ifPartInString(part, string):
    for i in range(len(string)):
        if string[i: len(part)] == part:
            return True
    return False
def sayStringWithout(part, string):
    if ifPartInString(part, string):
        return string[len(part):len(string)]
def getWord(word, string):
    return string.split()[word - 1]
def getRepeatLines(line):
    a = []
    iter = 1
    while not ifPartInString("end" ,lines[line + iter]):
        curr = lines[line + iter]
        a.append(curr.strip())
        iter += 1
        if iter == len(lines):
            return "error"
    return a
def convertVariables(command):
    if len(variables) != 0:
        spread = command.split()
        for a in range(len(spread)):
            for b in range(len(variables)):
                if list(variables.keys())[b] == spread[a]:
                    spread[a] = variables[spread[a]]
        return " ".join(spread)
    else:
        return command
def execute(command, loop, exec):
    command = command.strip()
    if command.strip()[0] != "make":
        command = convertVariables(command)
    if command[0:4] == "say ":
        if exec == True:
            print(sayStringWithout("say ", command))
    elif command[0:7] == "repeat ":
        if exec == True:
            rpt = getRepeatLines(loop)
            for a in range(int(sayStringWithout("repeat ", command))):
                for b in range(len(rpt)):
                    execute(rpt[b], loop + (b - 1), True)
            incrementI(len(rpt))
    elif command[0:3] == "end":
        pass
    elif command[0:2] == "--":
        pass
    elif command[0:5] == "make ":
        if exec == True:
            varName = getWord(2, command)
            varValue = command[5 + len(varName) + 1:len(command)]
            variables[str(varName)] = varValue
    elif command[0:5] == "wait ":
        sl = command.split()[1]
        time.sleep(int(sl))
    else:
        print("Error on line " + str(loop + 1) + ", did you spell something wrong?")
        return "error"

#####################################################
        
while i < len(lines):
    if execute(lines[i], i, False) != "error":
        execute(lines[i], i, True)
    else:
        break
    i += 1
