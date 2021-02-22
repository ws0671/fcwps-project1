#하노이 탑
#hanoi(N,start,to)
#N개의 원반을 start에서 to로 옮기는 과정

def move(N, start, to):
	print("{}번 원반을 {}에서 {}로 이동".format(N,start,to))

def hanoi(N, start, to , via):
	if N==1:
		move(1, start, to)
	else:
		hanoi(N-1,start,via,to)
		move(N,start,to)
		hanoi(N-1,via,to,start)

