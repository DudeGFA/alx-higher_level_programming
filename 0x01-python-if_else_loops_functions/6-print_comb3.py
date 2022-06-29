a=0
b=0
for i in range(1, 80):
    if sorted(str(i)) == list(str(i)):
        print("{:02}".format(i), end=", ")
print("89")
