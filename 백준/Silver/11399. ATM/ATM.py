#N명의 사람이 줄을 서 있음
#최솟값을 구하는 프로그램

def ATM(n, timeList):
    result = 0
    #작은 순서로 정렬
    timeList.sort()
    
    for i in timeList:
        result += i * n
        n -= 1
    
    return result    
    
    """ 원래 돌면서 5번 더하고 4번 더하고 하려던 코드
    for i in n:
        j = i
        while j < n:
            result = timeList           
            j += 1   
            pass
    
    """
    
n = int(input()) #사람수
timeList = list(map(int, input().split()))

print(ATM(n, timeList))