import sys

N, M = map(int,input().split())

if not 300>=N>=1:
	print("N에 1과 300 사이의 숫자를 입력하세요.")
	sys.exit()
	
if not 300>=M>=1:
	print("M에 1과 300 사이의 숫자를 입력하세요.")
	sys.exit()

print(N*M-1)
