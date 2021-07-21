from tkinter import *

root = Tk()
root.title("Nado GUI")

root.geometry("600x480+100+300") #가로 세로 x좌표 y좌표
root.resizable(False, False) # 넓이 높이

btn1 = Button(root, text="버튼1")
btn1.pack()

#padx 폭 pady 높이
btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼2")
btn3.pack()

# width height 고정크기 text 량에 따라 크기변경 없음
btn4 = Button(root, width=10, height=3, text="버튼3")
btn4.pack()

# 창 고정
root.mainloop()
