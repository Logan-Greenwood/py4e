largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        inum = int(num)
        if largest is None:
            largest = inum
        if largest < inum:
            largest = inum

        # print("num is",num)
        # print("max is",largest)

        if smallest is None:
            smallest = inum
        elif inum < smallest:
            smallest = inum
    except:
        print("Invalid input")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)
