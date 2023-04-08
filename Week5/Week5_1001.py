from tkinter import *
from time import *

fnameList = ["Fox (1).png", "Fox (2).png", "Fox (3).png", "Fox (4).png", "Fox (5).png", "Fox (6).png", "Fox (7).png", "Fox (8).png", "Fox (9).png", "Fox (10).png"]
PhotoList = [None] * 10
num = 0

def clickNext():
    global num
    num += 1
    if num > 9:
        num = 0
    photo = PhotoImage(file = "./PNG/" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    
def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 9
    photo = PhotoImage(file = "./PNG/" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    
window = Tk()
window.geometry("500x300")
window.title("폭스 로저씨의 개발이야기")

btnPrev = Button(window, text = "<< 이전", command = clickPrev)
btnNext = Button(window, text = "다음 >>", command = clickNext)

photo = PhotoImage(file = "PNG/" + fnameList[0])
pLabel = Label(window, image = photo)

btnPrev.place(x = 150, y = 10)
btnNext.place(x = 350, y = 10)
pLabel.place(x = 150, y = 50)

window.mainloop()