#!/usr/bin/python
#-*-coding:utf-8 -*-

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

if __name__=="__main__":
	stock_max,stock_min,stock_close,stock_ammount=np.loadtxt('6.SH600000.txt',delimiter='\t',encoding='ISO-8859-1',skiprows=2,usecols=(2,3,4,5),unpack=True)
	N=100
	stock_close=stock_close[:N]
	print (stock_close)

	n=5
	weight=np.ones(n)
	weight/=weight.sum()
	print(weight)
	stock_sma=np.convolve(stock_close,weight,mode='valid')

	weight=np.linspace(1,0,n)
	weight=np.exp(weight)
	weight/=weight.sum()
	print(weight)
	stock_ema=np.convolve(stock_close,weight,mode='valid')
	
	t=np.arange(n-1,N)
	poly=np.polyfit(t,stock_ema,10)
	print(poly)
	stock_ema_hat=np.polyval(poly,t)

	mpl.rcParams['font.sans-serif']=[u'SimHei']
	mpl.rcParams['axes.unicode_minus']=False
	plt.plot(np.arange(N),stock_close,'ro-',linewidth=2,label=u'yyyyyyy')
	t=np.arange(n-1,N)
	plt.plot(t,stock_sma,'b-',linewidth=2,label=u'jjjjjjj')
	plt.plot(t,stock_ema,'g-',linewidth=2,label=u'zzzzzzz')
	plt.legend(loc='upper right')
	plt.grid(True)
	plt.show()

	plt.figure(figsize=(9,6))
	plt.plot(np.arange(N),stock_close,'r-',linewidth=1,label=u'y2')
	plt.plot(t,stock_ema,'g-',linewidth=2,label=u'z2')
	plt.plot(t,stock_ema_hat,'m-',linewidth=3,label=u'z2g')
	plt.legend(loc='upper right')
	plt.grid(True)
	plt.show()
