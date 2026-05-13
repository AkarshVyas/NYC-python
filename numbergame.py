import random
com = random.randint(1,100)
tries = 0

while True:
    tries = tries + 1
    hum = int(input("guess your number between 1 - 100 :- "))

    if hum == com:
        print(f"congratulations you have won  in {tries} tries!")
        break

    elif hum > com:
        print("sorry wrong guess go lower !")

    elif hum < com:
        print("sorry wrong guess go higher !")