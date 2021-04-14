try:
  import Tkinter as tk
except ImportError:
  import tkinter as tk
from tkinter import StringVar
from PIL import ImageTk, Image
from tkinter import ttk

win = tk.Tk()

#text = tk.Text(win,bg="white")
#win.wm_attributes("transparentcolor", "yellow")

def event1():
    global entry1
    global v
    global dropdown
    print(dropdown.current(),dropdown.get())
    t1=entry1.get()  #取得用戶所輸入的文字
    area=float(t1)
    comStr=dropdown.get()
    if comStr=="平方公尺":
        number=area*3.3058
    elif comStr=="甲":
        number=area*0.00034
    elif comStr=="分":
        number=area*0.0034
    elif comStr=="公頃":
        number=area*0.03306
    v.set(str(number))

win.wm_title("面積換算小程式")                 # 設定抬頭名稱
win.minsize(width=400, height=200)   # 320,200
win.maxsize(width=400, height=200)  # 1024 768
win.resizable(width=False, height=False) # 是否可以改變視窗大小
#background_image = ImageTk.PhotoImage(Image.open("background.jpg"))    #加入背景圖片
#background_label = tk.Label(win, image=background_image)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

labeltwd =tk.Label(win,text="面積換算",font=18)
labeltwd.place(x=10,y=10)

entry1=tk.Entry(win)
entry1.place(x=10,y=40)

label2 =tk.Label(win,text="坪")
label2.place(x=150,y=40)

btn1 =tk.Button(win,text="換算",command=event1)
btn1.place(x=10,y=80)

v =StringVar()
label1=tk.Label(win,textvariable=v)
label1.place(x=60,y=150)

dropdown = ttk.Combobox(win,
                        values = [
                            '平方公尺',
                            '甲',
                            '分',
                            '公頃'])

dropdown.place(x=10,y=120)
dropdown.current()


win.mainloop()