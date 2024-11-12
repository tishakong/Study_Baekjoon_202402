def sugar(n):
    result = n // 5 # 5개짜리 봉지 수 확인
    balance = n % 5 # 3으로 나눠지는지 확인할 봉지
    
    if balance == 0:
        return result
    
    while True:
        if balance % 3 == 0:
            result += balance // 3
            return result
        else:
            result -= 1
            balance += 5
            if balance > n:
                return -1
        
n = int(input())
memo = {}

print(sugar(n))