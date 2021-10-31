from tkinter import *

def Call():
    # 텍스트를 화면(window)에 추가
    msg = Label(window, text = "You pressed the button")
    msg.place(x = 30, y = 50)
    button["highlightbackground"] = "blue"
    button["fg"] = "white"

window = Tk()
window.title("tkinter_Example")
window.geometry("360x360")    
button = Button(text = "press me", command = Call)
button.place(x = 30, y = 20, width = 100, height = 25)
window.mainloop()