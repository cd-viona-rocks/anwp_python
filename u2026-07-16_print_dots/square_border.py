n = 20

print()
for x in range(n):  
    print("     ", end="") 
    for y in range(n):
        if x != 0 and x != n-1 and y != 0 and y != n-1:
            print(" . ", end="")
        else:            
            print(" X ", end="")
    print()
print()


#  python .\square_border.py

#       X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X 
#       X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  X 
#       X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  X 
#       X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  X 
#       X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  X 
#       X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  X 
#       X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  X 
#       X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  X 
#       X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  X 
#       X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  X 
#       X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  X 
#       X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  X 
#       X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  X 
#       X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  X 
#       X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  X 
#       X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  X 
#       X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  X 
#       X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  X 
#       X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  X 
#       X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X 
