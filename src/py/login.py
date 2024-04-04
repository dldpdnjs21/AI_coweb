from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msgbox
import hashlib
import base64
import pymysql
import pandas as pd
money =""
name =""
def login():
    global user_id,password,window
    window = Tk()
    window.title("Login")
    window.resizable(False,False)
    user_id, password = StringVar(), StringVar()
    ttk.Label(window, text = "Username : ").grid(row = 0, column = 0, padx = 10, pady = 10)
    ttk.Label(window, text = "Password : ").grid(row = 1, column = 0, padx = 10, pady = 10)
    ttk.Entry(window, textvariable = user_id).grid(row = 0, column = 1, padx = 10, pady = 10)
    ttk.Entry(window, textvariable = password,show="*").grid(row = 1, column = 1, padx = 10, pady = 10)
    ttk.Button(window, text = "Login", command = check_data).grid(row = 2, column = 1, padx = 10, pady = 10)
    window.mainloop()

def check_data():
    global name,money,window
    id = user_id.get()
    pw = password.get()
    if len(str(id)) == 0 :
        msgbox.showwarning("경고", "아이디를 입력해주세요")
    elif len(str(pw)) == 0 :
        msgbox.showwarning("경고", "비밀번호를 입력해주세요")
    else:
        db = pymysql.connect(
            host="jjn3912.iptime.org",
            user="coweb",
            password="@jjn7723912",
            database="cowab"
        )
        pw = hashlib.sha256(pw.encode())
        pwh = pw.hexdigest()
        cursor = db.cursor()
        sql = f"SELECT * FROM user WHERE id = %s "
        cursor.execute(sql,[id])
        result = cursor.fetchone()
        name = result[2]
        money = result[3]
    if f'{pwh}' == f'{result[1]}':
        window.destroy()
        main_pro()

    else:
        msgbox.showwarning("경고","아이디나 비밀번호가 틀렸습니다 다시 확인해주세요.")

def main_pro():
    global name,money
    user_name = name
    main_window = Tk()
    main_window.title=("Coweb")
    main_window.geometry("800x600+1000+200")
    main_window.resizable(False,False)
    ttk.Label(main_window, text=f"환영합니다 {user_name} 님").place(x = 670, y = 5)
    ttk.Label(main_window, text=f"잔액: {money} 원").place(x=670, y=20)
    ttk.Button(main_window, text ="충전", command = charge_money).place(x=690, y=35)
    main_window.mainloop()

def charge_money():
    global amount,charge,charge_window
    charge_window= Tk()
    charge = StringVar()
    charge_window.title = ("금액 충전")
    ttk.Label(charge_window, text="충전금액: ").grid(row=0, column=0, padx=10, pady=10)
    ttk.Entry(charge_window, textvariable= charge).grid(row=0, column=1, padx=10, pady=10)
    ttk.Button(charge_window, text="충전", command=charge_send).grid(row=2, column=1, padx=10, pady=10)
    charge_window.mainloop()


def charge_send():
    global money,user_id,charge_window
    amount = charge.get()
    curmoney = int(money)
    print(amount)

    # id = user_id
    # amount_bal = int(amount)
    # total = curmoney + amount_bal
    # print(id)
    # print(amount)


login()
