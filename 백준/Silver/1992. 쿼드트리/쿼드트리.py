def quad_tree(matrix, x, y, size):
    global result
    
    #인접한 게 전부 같은지(압축 가능한지) 확인하는 변수
    ok = True
    target = matrix[x][y]
    
    for i in range(x,x+size):
        for j in range(y,y+size):
            if matrix[i][j] != target:
                ok = False
                break
        if not ok:
            break
        
    #ok면 괄호 따로 씌워줄 필요 없이 그냥 숫자 넣으면 됨
    if ok:
        result = result + str(target) #스택을 써야하나?
        
    #ok가 false면 괄호도 씌워주고 4조각으로 다시 나눠야함
    else:
        result = result + '('
        new_size = size // 2
        for i in range(2):
            for j in range(2):
                quad_tree(matrix, x + i * new_size, y + j * new_size, new_size)
        result = result + ')'

#결과 출력할 변수 초기화
result = ''

#입력
n = int(input())
matrix = []
for i in range(n):
    line = input()
    matrix.append(list(map(int,line)))

#함수 실행
quad_tree(matrix, 0, 0, n)

#결과 출력
print(result)