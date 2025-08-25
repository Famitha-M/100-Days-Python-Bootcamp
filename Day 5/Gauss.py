total=0
for num in range(1,101):
    total+=num
print(total)


for i in range(1,101):
    if i%3==0:
        print("Fizz")
    if i%5==0:
        print("Buzz")
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    print(i)
