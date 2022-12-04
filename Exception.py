# def add (x):
#     x /= 0
#     print(x)

# add(5)

try:
    x = 10/4
    print(x)

except ZeroDivisionError:
    print("ZeroDivisionError")

except ValueError:
    print("eror found")

else:
    print("No error found")

finally:
    print("i will be alwas printed")