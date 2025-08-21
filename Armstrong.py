def check_armstrong():
    num = int(input("Enter a number: "))
    temp = num
    digits = len(str(num))
    result = 0

    while temp > 0:
        digit = temp % 10
        result += digit ** digits
        temp //= 10

    if result == num:
        print(num, "is an Armstrong Number")
    else:
        print(num, "is NOT an Armstrong Number")
check_armstrong()
