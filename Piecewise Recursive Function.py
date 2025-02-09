#This is an easier problem i saw in one olympiad book. 
'''A function 𝑓 f is defined on integers such that for 𝑛 ∈ 𝑍:
𝑓 ( 𝑛 ) = { 𝑛 − 3 , if 𝑛 ≥ 1000 
          𝑓 ( 𝑓 ( 𝑛 + 5 ) ) , if 𝑛 < 1000}
​ Find 𝑓 ( 84 ) 
'''
def func(nth):
	func = 1 #number of composite functions
	while func != 0: 
		while nth <100:
			func+=1
			nth+=5
			
		while nth>=100:
		 	func-=1
		 	nth -= 3
		
	return nth

print(func(84))
