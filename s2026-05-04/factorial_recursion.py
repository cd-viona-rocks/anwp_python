
# count = 10
# while True:

#     if count < 5:
#         break

#     print(count, "infinity")
#     count += 1

# 0! = 1
# 1! = 1
# 2! = 2 * 1
# 3! = 3 * 2 * 1
# 
# 1000! = 1000 * 999 * . . * 1


def fac(n: int) -> int:
    
    if n < 0:
        raise("negative numbers are mathematical not defined")
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    print(f"factorial({n}) = {n} * factorial({n-1})")
    return n * fac(n-1)
    # 10,9,8,7,6,5,4,3,2 * 1


# for i in range(11):
#     print(i, fac(i))

fac(-1)

