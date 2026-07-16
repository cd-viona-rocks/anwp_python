n = 20

print()
for x in range(n):  
    print("     ", end="") 
    for y in range(n):
        if x >= y:
            print(" X ", end="")         
        else:
            print(" . ", end="")
    print()
print()


#  python .\square_triag_lower.py

#       X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 
#       X  X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 
#       X  X  X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 
#       X  X  X  X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 
#       X  X  X  X  X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 
#       X  X  X  X  X  X  .  .  .  .  .  .  .  .  .  .  .  .  .  . 
#       X  X  X  X  X  X  X  .  .  .  .  .  .  .  .  .  .  .  .  . 
#       X  X  X  X  X  X  X  X  .  .  .  .  .  .  .  .  .  .  .  . 
#       X  X  X  X  X  X  X  X  X  .  .  .  .  .  .  .  .  .  .  . 
#       X  X  X  X  X  X  X  X  X  X  .  .  .  .  .  .  .  .  .  . 
#       X  X  X  X  X  X  X  X  X  X  X  .  .  .  .  .  .  .  .  . 
#       X  X  X  X  X  X  X  X  X  X  X  X  .  .  .  .  .  .  .  . 
#       X  X  X  X  X  X  X  X  X  X  X  X  X  .  .  .  .  .  .  . 
#       X  X  X  X  X  X  X  X  X  X  X  X  X  X  .  .  .  .  .  . 
#       X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  .  .  .  .  . 
#       X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  .  .  .  . 
#       X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  .  .  . 
#       X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  .  . 
#       X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  . 
#       X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X 
