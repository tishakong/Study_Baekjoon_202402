def d_q(matrix, row, col, size):
    global m, z, o

    ok = True
    target = matrix[row][col] #비교할 기준 숫자
    
    for i in range(row, row + size):
        for j in range(col, col +size):
            #i,j로 행렬 값 꺼내와서 값 비교하고 다르면 ok를 false로 바꾸고 break
            if matrix[i][j] != target:
                ok = False
                break
        if ok == False:
            break

    #ok가 true인 상태로 끝나면 m z o 에 해당하는거 +1
    if ok:
        if target == -1:
            m += 1
        elif target == 0:
            z += 1
        else:
            o += 1

    #ok가 false인 상태로 끝나면 d_q 재호출하면서 9개로 쪼개기 => 행 열 3으로 나누기
    else:
        new_size = size // 3
        for i in range(3):
            for j in range(3):
                d_q(matrix, row + i * new_size, col + j * new_size, new_size)

#근데 이게 분할정복 문제인지 잘 모르겠아요

#예제 입력 받기
n = int(input())
matrix = []

#입력값으로 매트릭스 만들기
for i in range(n):
    line = input()
    matrix.append(list(map(int,line.split())))

#프린트할 -1, 0, 1 개수 변수 초기화
m = z = o = 0

d_q(matrix, 0, 0, n)


print(m) #-1
print(z) #0
print(o) #1
