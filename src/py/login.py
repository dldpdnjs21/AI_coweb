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
    global name,money,window,id,db
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
    return
def main_pro():
    global name,money,amount,main_window
    user_name = name
    main_window = Tk()
    main_window.title=("Coweb")
    main_window.geometry("800x600+1000+200")
    main_window.resizable(False,False)
    amount = IntVar()
    ttk.Label(main_window, text=f"환영합니다 {user_name} 님").place(x = 670, y = 5)
    ttk.Label(main_window, text=f"잔액: {money} 원").place(x=670, y=20)
    ttk.Entry(main_window, textvariable= amount).place(x=660, y=40)
    ttk.Button(main_window, text ="충전", command = charge_form).place(x=690, y=65)
    main_window.mainloop()
# def charge_form():
#     global char_window
#     char_window = Tk()
#     char_window.title = ("Charge")
#     char_window.resizable(False,False)
#     ttk.Label(char_window, text="충전금액 : ").grid(row=1, column=0, padx=10, pady=10)
#     ttk.Entry(char_window, textvariable= amount).grid(row=1, column=1, padx=10, pady=10)
#     ttk.Button(char_window, text = "충전", command = charge_money).grid(row = 2, column = 1, padx = 10, pady = 10)
#     char_window.mainloop()
def charge_money():
    amountm = amount.get()
    moneyset = int(amountm)
    cursor = db.cursor()
    sql = f"UPDATE user SET money = money + {moneyset} WHERE id = '{id}' "
    cursor.execute(sql)
    db.commit()
    sql = f"SELECT * FROM user WHERE id = %s "
    cursor.execute(sql,[id])
    result = cursor.fetchone()
    moneyup = result[3]
    char_window.destroy()
    ttk.Label(main_window, text=f"잔액: {moneyup} 원").place(x=670, y=20)


def buy_coin():
    btc_cost = btc_cost.get()
    cursor = db.cursor()
    sql = f"UPDATE user SET money = money - {btc_cost} WHERE id = '{id}' "
    cursor.execute(sql)
    db.commit()
    sql = f"SELECT * FROM user WHERE id = %s "
    cursor.execute(sql, [id])
    result = cursor.fetchone()
    moneyup = result[3]
    char_window.destroy()
    ttk.Label(main_window, text=f"잔액: {moneyup} 원").place(x=670, y=20)

def sell_coin():
    btc_cost = btc_cost.get()
    cursor = db.cursor()
    sql = f"UPDATE user SET money = money + {btc_cost} WHERE id = '{id}' "
    cursor.execute(sql)
    db.commit()
    sql = f"SELECT * FROM user WHERE id = %s "
    cursor.execute(sql, [id])
    result = cursor.fetchone()
    moneyup = result[3]
    char_window.destroy()
    ttk.Label(main_window, text=f"잔액: {moneyup} 원").place(x=670, y=20)


login()
