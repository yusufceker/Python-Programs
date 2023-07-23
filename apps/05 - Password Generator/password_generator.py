import random

lower_letters = "abcdefghijklmnopqrstuvwxyz" #lower let
upper_letters = "ABCDEFGHIJKLMNOPQRSTYVWXYZ" #uppers let
num = "0123456789" #numbers
symbol = "[]{}#()*:_-" #sembol(turkish)

ans = lower_letters + upper_letters + num + symbol

lenght = 6 #uzunluk(turkish)
password = "".join(random.sample(ans,lenght))
print("Generated password is ",password)