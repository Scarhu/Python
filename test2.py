#!/usr/bin/python
#-*- coding:utf-8 -*-
def searchInsert(nums,target):
	l=range(len(nums))
	for i in l:
		if nums[i]==target:
			print(i)
			return 
		elif nums[i]<target and nums[i+1]>target:
			print(i+1)
			return

b=[1,3,5,7,9,11,13,15]
searchInsert(b,8) 
