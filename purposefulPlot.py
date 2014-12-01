#! /usr/bin/env python
from numpy import * # I SHOULD do this, because the user won't enter "np.sin(x)" ...
import matplotlib.pyplot as plt

if(raw_input("Do you want to enter your own equation?\nTip: the default one may be is more beautiful.\n")[0].lower() == 'y'):
	lRange = eval(raw_input("Enter the left range of x: "))
	rRange = eval(raw_input("Enter the right range of x: "))
	samples = int(raw_input("How may samples do you want? ")) # the number of samples, should be an int.
	x = linspace(lRange, rRange, samples) # Create samples
	equa = raw_input("\nEnter the equation of f(x): ")
	try:
		y = eval(equa)
	except: # Sometimes the system didn't support the calculation of aranges, we do it ourself.
		xlist = linspace(lRange, rRange, samples) # Can't use x straightly
		y = linspace(lRange, rRange, samples)
		for i in range(len(xlist)):
			x = xlist[i] # The user will enter functions like "x+3".
			y[i] = eval(equa)
		x = xlist

	plt.plot(x, y)
	plt.xlabel("$x$")
	plt.ylabel("$y$")
	plt.grid('on')
	plt.title("DIY Function", fontsize = 20)
else:
	x = arange(-pi, pi, 0.01)
	y1 = sin(x)
	y2 = sin(x) ** 2
	y3 = cos(x)

	plt.subplot(121) # subplot
	plt.plot(x, y1, label = "$y=\sinx$")
	plt.plot(x, y2, label = "$y=\sin^2x$")
	plt.plot(x, y3, label = "$y=\cosx$")
	plt.xlabel("$x$")
	plt.ylabel("$y$")
	plt.legend(loc = 'lower right') # 4 is also acceptable instead of lower right
	plt.grid("on")

	plt.subplot(122, polar = True) # POLAR
	plt.plot(x, y1, label = "$r=\sin\\theta$")
	plt.plot(x, y2, label = "$r=\sin^2\\theta$")
	plt.plot(x, y3, label = "$r=\cos\\theta$")
	# Labels failed in the polar scale :(
	plt.legend(loc = 'lower center', bbox_to_anchor = (0.5, -0.5)) # 8
	plt.grid("on")
	
	plt.suptitle("Trigonometric Functions!", fontsize = 20)
	
if(raw_input("Done.\nDo you want to save the figure instead of showing it?")[0].lower() == 'y'):
	plt.savefig("purposeful_Pic(df).pdf")
else:
	plt.show()