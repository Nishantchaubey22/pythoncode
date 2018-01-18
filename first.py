#Write a program to count the number of even and odd numbers
#Sample numbers=(1,2,3,4,5,6,7,8,9)
count_even=0
count_odd=0
for value in range(1,10):
	if value%2==0:
		count_even+=1
	else:
		count_odd+=1
print(count_even)
print(count_odd)
print("Code complete")
