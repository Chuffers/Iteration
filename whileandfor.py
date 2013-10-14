#enter message and repeat a number of times

message = input("Please enter a message: ")
repeats = int(input("Please enter the number of times you wuld like your message repeating: "))
for count in range(repeats):
    print(message)
if repeats != int:
    print("Please enter a valid number")

