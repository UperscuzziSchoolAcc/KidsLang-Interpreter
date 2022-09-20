"""
KidsLang Interpreter, made by Greyson Rowland
"""
i = 0
def incrementI(n):
    global i
    i += int(n)
f = open("myCode.kl")
def ifPartInString(part, string):
    for i in range(len(string)):
        if string[i: len(part)] == part:
            return True
    return False
def sayStringWithout(part, string):
    if ifPartInString(part, string):
        return string[len(part):len(string)]
lines = f.readlines()
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

def execute(command, loop, exec):
    #print("before:", command)
    command = command.strip()
    #print("after:", command)
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