# 1.
for x in range(0, 151, 1):
    print(x)

# 2.
for x in range(5, 1000, 1):
    if x % 5 == 0:
        print(x)

# 3.
for x in range(1, 101, 1):
    if (x % 5) == 0:
        print("Coding")
    elif (x % 5) != 0:
        print(x)
    if (x % 10) == 0:
        print("Coding Dojo")


# 4.
oddNumSum = 0
for x in range(0, 500000, 1):
    if (x % 2) == 1:
        oddNumSum += x
print(oddNumSum)


# 5.
for x in range(2018, 0, -4):
    if (x % 2) == 0:
        print(x)


# 6.
lowNum = 1
highNum = 130
mult = 7
for x in range(lowNum, highNum, 1):
    if (x % mult) == 0:
        print(x)
