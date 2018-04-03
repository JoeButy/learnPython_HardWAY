x = range(0,20)
x[0] =True and True # true
x[1] = False and True # false
x[2]=1 == 1 and 2 == 1 # False
x[3]="test" == "test" # true
x[4]=1==1 or 2!=1 # true
x[5]=True and 1 ==1 # true
x[6]=False and 0!=0 # false
x[7]=True or 1 == 1 # true
x[8]="test" == "testing" # false
x[9]=1 != 0 and 2 ==1 # false
x[10]="test" != "testing" # true
x[11]="test" == 1 # false
x[12]=not(True and False) #true
x[13]=not(1 ==1 and 0!=1)#false
x[14]=not(10==1 or 1000==1000) # false
x[15]=not(1 != 10 or 3==4) #false
x[16]=not("testing" == "testing" and "Zed" == "Cool Guy") #true
x[17]=1 == 1 and (not("testing" == 1 or 1 ==0)) # true
x[18]="chuncky" == "bacon" and (not(3==4 or 3==3)) # false
x[19]=3==3 and (not("testing" == "testing" or "Python" == "Fun")) # false
for i,v in enumerate(x):
	print i+2,v