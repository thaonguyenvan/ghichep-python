numlist = list()
x = 0
print("Please enter a list of number,enter 'done' to finish\n")
while True:
    x = x + 1
    inp = input("Enter a number %d: " %(x))
    if inp == 'done' :
        break
    value = float(inp)
    numlist.append(value)
print('Sum: ', sum(numlist))
average = sum(numlist) / len(numlist)
print('Average:', average)