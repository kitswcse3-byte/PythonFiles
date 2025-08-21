def sum_all(*args):
    total = 0
    for num in args:
        total += num
    print("Sum:", total)
sum_all(1, 2)
sum_all(10, 20, 30, 40)
