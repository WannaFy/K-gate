from tkinter import *

import data

from PIL import ImageTk, Image

def open_manual():
    import webbrowser
    webbrowser.open_new_tab('user manual.html')

def warning(string):
    warning_top = Tk()
    warning_top.geometry('400x200')
    warning_top.option_add("*Font", "Georgia")
    warning_label = Label(warning_top, text=string)
    warning_label.pack()
    confirm_button = Button(warning_top, text='confirm!', command=warning_top.destroy)
    confirm_button.pack()
    warning_top.mainloop()

def register():
    def check():
        if len(account.get())<=1:
            warning('用户名至少两个字符哦！')
        if password.get().isdigit() or len(password.get()) < 6 or ' ' in password.get():
            warning('密码必须不能是纯数字且应不少于六位且不能有空格')

        elif account.get() in data.account.keys():
            warning_top = Tk()
            warning_label = Label(warning_top, text='用户名已存在！')
            warning_label.pack()
            confirm_button = Button(warning_top, text='confirm!', command=warning_top.destroy)
            confirm_button.pack()
            warning_top.mainloop()
        else:
            def f():
                warning_top.destroy()
                top.destroy()

            data.account[account.get()] = password.get()
            with open('用户名和密码存储.txt', 'a') as fp:
                fp.write(account.get() + ' ' + password.get() + '\n')

            warning_top = Tk()
            warning_label = Label(warning_top, text='恭喜您已成功创建自己的账户！\n WELCOME TO Gate K')
            warning_label.pack()
            confirm_button = Button(warning_top, text='confirm!', command=f)
            confirm_button.pack()
            warning_top.mainloop()

    top = Tk()
    a_label = Label(top, text='account:')
    p_label = Label(top, text='password:')
    account = Entry(top, show=None, bd=5)
    password = Entry(top, show='*', bd=5)
    a_label.pack()
    account.pack()
    p_label.pack()
    password.pack()
    register_button = Button(top, text='确认注册', command=check)
    register_button.pack()


def sign_in():
    name=account.get()
    data.temp=name
    if data.account.get(name) == password.get():
        window0.destroy()
        warning_top = Tk()
        warning_label = Label(warning_top, text='！欢迎回家！'+name)
        warning_label.pack()
        confirm_button = Button(warning_top, text='confirm!', command=warning_top.destroy)
        confirm_button.pack()
        warning_top.mainloop()
        import play

    else:
        warning_top = Tk()
        warning_label = Label(warning_top, text='用户名不存在或者密码错误')
        warning_label.pack()
        confirm_button = Button(warning_top, text='confirm!', command=warning_top.destroy)
        confirm_button.pack()
        warning_top.mainloop()


def no_account_in():
    def ftest():
        a=answer_Entry.get()
        if a==str(answer):
            test_top.destroy()
            window0.destroy()
            warning('游客您好，您的默认用户名为:临时用户')
            data.temp='临时用户'
            import play
        else:
            warning('您的智商出了点问题')

    import random
    test=str(random.randint(0,20))+random.choice(['+','-','*'])+str(random.randint(0,20))
    answer=eval(test)
    test_top=Tk()
    test_top.title('临时用户质量检测')
    test_top.geometry('400x300')
    test_top.option_add("*Font", "Georgia")
    test_label=Label(test_top,text='请输入运算结果'+test+'=')
    answer_Entry=Entry(test_top)
    confirm_button=Button(test_top,text='确认提交',command=ftest)
    test_label.pack()
    answer_Entry.pack()
    confirm_button.pack()

window0 = Tk()
window0.option_add("*Font", "Georgia")
window0.iconbitmap('图标.ico')
window0.title('welcome to K号房!')
window0.geometry('800x500')
window0.wm_resizable(0, 0)
a_label = Label(window0, text='account:')
p_label = Label(window0, text='password:')
account = Entry(window0, show=None, bd=5)
password = Entry(window0, show='*', bd=5)

register_button = Button(window0, text='join us now!', command=register)
sign_in_button = Button(window0, text='sign in', command=sign_in)
no_account_in_button=Button(window0,text='游客登入',command=no_account_in)
manual_button=Button(window0,text='查看教程',command=open_manual)

a_label.pack()
account.pack()
p_label.pack()
password.pack()
sign_in_button.pack()
register_button.pack()
no_account_in_button.pack(side=BOTTOM)
manual_button.place(relx=0,rely=0.92)
window0.mainloop()
