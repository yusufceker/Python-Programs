import time
from tkinter import *
window = Tk()
window.title("Yusuf Çeker")
welc_label = Label(text="Welcome to Click and Create a File Program!",bg="red",fg="cyan")
choose_label = Label(text="Choose a File")

def Python():
    #Python Button Func
    file = open("python.txt","w",encoding="utf-8")
    file.write("Python is a high-level, general-purpose programming language. Its design philosophy emphasizes\n code readability with the use of significant indentation via the off-side rule")
    file.close()
def Java():
    #Java Button Func
    new_file = open("java.txt","w",encoding="utf-8")
    new_file.write("Java is an open source, object-oriented, platform-independent, highly\n efficient, multi-functional, high-level, both interpreted and compiled language developed by James Gosling, a Sun Microsystems engineer.")
    new_file.close()
def C():
    #Java Button Func
    my_file = open("c.txt","w",encoding="utf-8")
    my_file.write("C (pronounced /ˈsiː/ – like the letter c)[6] is a general-purpose computer programming language. It was created in the 1970s by Dennis Ritchie, and remains very widely used and influential. By design, C's features cleanly reflect the capabilities of the targeted CPUs. It has found lasting use in operating systems, device drivers, protocol stacks, though decreasingly[7] for application software. C is commonly used on computer \narchitectures that range from the largest supercomputers to the smallest microcontrollers and embedded systems.")
    my_file.close()
btn_python = Button(text="Python",fg="green",bg="yellow",command=Python)
btn_java = Button(text="Java",fg="blue",bg="red",command=Java)
btn_c = Button(text="C",fg="purple",bg="yellow",command=C)
btn_c.pack()
btn_java.pack()
btn_python.pack()
choose_label.pack()
welc_label.pack()
window.mainloop()