#-*- coding:utf-8 -*-

def MaxSum(m, n, a):
	if n < m or m < 1:
			return 0
	
	#构造(m+1)行 * (n+1)列的二维数组b
	b = [[0 for i in range(n+1)] for j in range(m+1)] 

	for i in range(m+1):
			b[i][0] = 0
	
	for i in range(n+1):
			b[0][j] = 0

	#枚举子段数目，从1开始，迭代到m， 递推出b[i][j]的值
	for i in range(1,m+1):
			for j in range(i, n-m+i+1): #n-m+i限制避免多余运算，当i=m时，j最大为n
					if j>i:
							b[i][j] = b[i][j-1] + a[j] #a[j]和a[j-1]一起，都在第i个子段中
							for k in range(i-1, j):
									if b[i][j] < b[i-1][k]+a[j]:
											b[i][j] = b[i-1][k]+a[j] #a[j]单独作为第i个子段
					else:
							b[i][j] = b[i-1][j-1] + a[j] #当i=j时，每一项都要分成一个子段(j个元素分成j段)

	sum = b[m][m]
	for j in range(m, n+1):
			if sum < b[m][j]:
					sum = b[m][j]

	return sum

if __name__ == "__main__":
#	a = [0, 2, 3, -7, 6, 4, -5]

#	for i in range(len(a)):
#			print a[i], " ",

#	print 

#	print "数组a的最大连续子段和为:", MaxSum(3, 6, a)


	with open("data.txt", "r") as f:
		while True:
				m = f.readline()
				if not m:break
				m = int(m)
				n = int(f.readline())
				a = map(int, f.readline().split())
				for i in range(1, len(a)):
						print a[i], '|',
				print
				print "数组a的最大连续%s子段和为：" % m, MaxSum(m, n, a)
				print 
	
