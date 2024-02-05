A, B = map(int,input().split())

if not A>0:
	print("A가 0보다 작습니다.")
elif not B<10:
	print("B가 10보다 큽니다.")
else:
	print(A+B)
