# SECRET NUMBER GAME (you can play with your friend)

secret_number = str(input("enter secret number: "))
answer = str(input("in your opinion what's the secret number?: "))

if answer == secret_number:
    print("Good Work! You have entered the correct secret number. Congratulations!")
elif answer != secret_number:
    print("Ooopppsss! You have entered incorrect secret number! Try again...")
    while answer != secret_number:
        secret_number = str(input("enter secret number: "))
        answer = str(input("in your opinion what's the secret number?: "))
        if answer == secret_number:
            print("Good Work! You have entered the correct secret number. Congratulations!")
else:
    print("try again later...")


