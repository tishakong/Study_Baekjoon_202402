Str = input()
dict = {}
count = 0

Str = Str.upper()

for i in range(len(Str)):
    currentChar = Str[i]
    if dict.get(currentChar) == None:
        dict[currentChar]=1
    else:
        for key,value in dict.items():
            if key == currentChar:
                dict[currentChar]=value+1

maxItem = max(dict, key = dict.get)
maxValue = dict[maxItem]

for key, value in dict.items():
    if value == maxValue:
        count +=1

if count>1:
    print("?")
else:
    print(maxItem)

    
