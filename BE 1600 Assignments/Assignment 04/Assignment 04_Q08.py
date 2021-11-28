def print_average():
    user_number = int(input("Type a number: "))
    total = 0
    acc = 0

    if user_number < 0:
        print("Average was 0:")
        return
        
    while user_number >= 0:
        total += user_number
        acc += 1
        user_number = int(input("Type a number: "))

    print("Average was",total/acc)

print_average()

