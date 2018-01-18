#Write a program to get the Fibonacci series between 0 to 50
x=0
y=1
print(x)
while(y<50):
	if(y>50):
		break
	print(y)
	x,y=y,x+y
