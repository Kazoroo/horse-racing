import time
import random


horse = random.randint(1, 13)
position = random.randint(2, 13)


bet = int(input("Postaw zakład: "))

user_choice = int(input("Wybierz numer konia na którego chcesz postawić [1-13]: "))

print(f"Postawiłeś na konia {user_choice}")
time.sleep(1.5)

print("Trwa wyścig...")
time.sleep(3)


# wynik wyścigu
if user_choice == horse:
    award = bet * 3
    print(f"Twój koń skończył na 1. miejscu, wygrałeś! {award} trafia na twoje konto")
else:
    if position == 2:
        award = bet * 1.5
    if position == 3:
        award = bet * 1.25
    if position > 3:
        award = 0
    print(f"Przegrałeś, twój koń skończył na {position}. miejscu. Otrzymałeś {award} pieniądzy postawionych na zakład")
