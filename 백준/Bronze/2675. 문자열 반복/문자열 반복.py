T = int(input())

CaseList = []

if(T!=1):
    for i in range(0,T):
        CaseList.append(input())

    for i in range(0,T):
        CurrentProcess = CaseList[i]
        Separation=CurrentProcess.split()
    
        Str = Separation[1]

        for i in range(len(Str)):
            print(Str[i]*int(Separation[0]), end="")

        print()
else:
    CaseList.append(input())
    Separation=CaseList[0].split()
    
    Str = Separation[1]

    for i in range(len(Str)):
        print(Str[i]*int(Separation[0]), end="")
