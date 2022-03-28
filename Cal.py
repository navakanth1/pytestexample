def add2no(x, y):
    return x+y

def sub2no(x, y):
    return x-y

def mul2no(x, y):
    return x*y

def div2no(x, y):
    return x/y
a = int(input("enter 1st: "))
b = int(input("enter 2nd: "))

if __name__ == "__main__":
    add = add2no(a, b)
    subtract = sub2no(a, b)
    product = mul2no(a, b)
    divison = div2no(a, b)

print(add)
print(subtract)
print(product)
print(divison)