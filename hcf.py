def compute_hcf(x , y):
    if x >y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
            if(x % i == 0) and  (y % i == 0):
                hcf = i
                return hcf
x = int(input("enter a number"))
y = int(input("enter a number"))
print(compute_hcf(x , y))