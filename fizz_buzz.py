def fizzbuzz(num):
    try:
        if num % 3 == 0 and num != 0:
            print("fizz!\n")
        elif num % 5 == 0 and num != 0:
            print("buzz!\n")
        elif num % 15 == 0 and num != 0:
            print("fizzbuzz!\n")
        else:
            print(num)
    except Exception as e:
        return e


for i in range(0, 256):
    fizzbuzz(i)
