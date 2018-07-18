#renthesisexport PATH=$PATH:/usr/local/gcc-arm-none-eabi-4_9-2015q1/bin
#!ausr/bin/python
#-*-coding:UTF-8 -*-


def generateParenthesis(N):
	ans=[]
	def backtrack(S='',left = 0,right = 0):
		if len(S)==2*N:
			ans.append(S)
			print(S)
			return
		if left < N:
			backtrack(S+'(',left+1,right)
		if right < left:
			backtrack(S+')',left,right+1)
		
	backtrack()
	return ans

N=int(input('N='))
generateParenthesis(N)
