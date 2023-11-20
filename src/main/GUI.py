from tkinter import *
from tkinter.ttk import Treeview
from dao.StudentDao import StudentDao
from tkinter.simpledialog import *
import tkinter.messagebox
from po.student import Student

# sd = StudentDao()
# window = Tk()
# window.geometry('800x500')
#
# table = Treeview(columns=('sno', 'sname', 'ssex', 'sclass', 'smajor', 'sdept', 'sbir', 'stele'), show="headings")
# table.column('sno', width=100)
# table.column('sname', width=100)
# table.column('ssex', width=100)
# table.column('sclass', width=100)
# table.column('smajor', width=100)
# table.column('sdept', width=100)
# table.column('sbir', width=100)
# table.column('stele', width=100)
# table.heading('sno', text='学号')
# table.heading('sname', text='姓名')
# table.heading('ssex', text='性别')
# table.heading('sclass', text='班级')
# table.heading('smajor', text='专业')
# table.heading('sdept', text='院系')
# table.heading('sbir', text='出生日期')
# table.heading('stele', text='联系电话')
#
#
# def load():
#     for i in table.get_children():
#         table.delete(i)
#     for i in sd.list_book():
#         table.insert('', END, values=i)
#
#
# def add():
#     sno = askstring('提示', '请输入学生学号')
#     sname = askstring('提示', '请输入学生姓名')
#     ssex = askstring('提示', '请输入学生性别')
#     sclass = askstring('提示', '请输入学生班级')
#     smajor = askstring('提示', '请输入学生专业')
#     sdept = askstring('提示', '请输入学生院系')
#     sbir = askstring('提示', '请输入学生出生日期')
#     stele = askstring('提示', '请输入学生电话号码')
#     if sno is not None and sname is not None:
#         r = sd.addStudent(Student(sno=sno, sname=sname, ssex=ssex, sclass=sclass, smajor=smajor,
#                                   sdept=sdept, sbir=sbir, stele=stele))
#         tkinter.messagebox.showinfo(r,"成功增加数据")
#
#
# def delete():
#     sno = askstring('提示', '请输入学生学号')
#     sname = askstring('提示', '请输入学生姓名')
#     ssex = askstring('提示', '请输入学生性别')
#     sclass = askstring('提示', '请输入学生班级')
#     smajor = askstring('提示', '请输入学生专业')
#     sdept = askstring('提示', '请输入学生院系')
#     sbir = askstring('提示', '请输入学生出生日期')
#     stele = askstring('提示', '请输入学生电话号码')
#     if sno is not None and sname is not None:
#         r = sd.addStudent(Student(sno=sno, sname=sname, ssex=ssex, sclass=sclass, smajor=smajor,
#                                   sdept=sdept, sbir=sbir, stele=stele))
#         tkinter.messagebox.showerror(r, "成功增加数据")
#
#
# Button(text='加载', command=load).place(x=200, y=350)
# Button(text='增加', command=add).place(x=400, y=350)
# Button(text='删除', command=delete).place(x=600, y=350)
#
# table.place(width=800, height=300)
# window.mainloop()

class TableOperation:

class Choose:
    num = ''
    name = ''
    major = ''
    size = '800x500'
    width = 20
    height = 1

    def intoInsert(self):
        top2 = Tk(className='增加选项')
        # TODO:利用弹窗实现数据插入


def chooseOp():
    choose_table_window.destroy()
    global choose_op_window
    choose_op_window = Tk()
    choose_op_window.title('操作选项')
    width = 72
    height = 1
    Button(choose_op_window, text='增加', width=width, height=height,
           command=textCommand, bg='light yellow', font='楷体').grid(row=0, column=1, padx=10, pady=20)
    Button(choose_op_window, text='删除', width=width, height=height,
           command=textCommand, bg='light yellow', font='楷体').grid(row=10, column=1, padx=10, pady=20)
    Button(choose_op_window, text='查找', width=width, height=height,
           command=textCommand, bg='light yellow', font='楷体').grid(row=20, column=1, padx=10, pady=20)
    Button(choose_op_window, text='修改', width=width, height=height,
           command=textCommand, bg='light yellow', font='楷体').grid(row=30, column=1, padx=10, pady=20)
    Button(choose_op_window, text='返回', width=width, height=height,
           command=chooseTable, bg='light cyan', font='楷体').grid(row=40, column=1, padx=10, pady=20)
    choose_op_window.geometry('750x400')

def textCommand():
    print("ok")


def chooseTable():
    global flag
    if flag == 1:
        logInWindow.destroy()
    flag += 1
    if 'choose_op_window' in globals():
        choose_op_window.destroy()
    global choose_table_window
    choose_table_window = Tk()
    choose_table_window.title("表选项")
    width = 72
    height = 1
    Button(choose_table_window, text='学生信息表', width=width, height=height,
           command=chooseOp, bg='light yellow', font='楷体').grid(row=0, column=1, padx=10, pady=20)
    Button(choose_table_window, text='学生选课成绩表', width=width, height=height,
           command=chooseOp, bg='light yellow', font='楷体').grid(row=10, column=1, padx=10, pady=20)
    Button(choose_table_window, text='课程信息表', width=width, height=height,
           command=chooseOp, bg='light yellow', font='楷体').grid(row=20, column=1, padx=10, pady=20)


flag = 1
logInWindow = Tk()
logInWindow.title('登录')
logInWindow.geometry('400x300')
Label(logInWindow, text='UserID', font=('Arial', 14)).place(x=10, y=150)
Label(logInWindow, text='Password', font=('Arial', 14)).place(x=10, y=190)

var_user_name = StringVar()
entry_usr_name = Entry(logInWindow, textvariable=var_user_name, font=('Arial', 14))
entry_usr_name.place(x=120, y=155)

var_usr_pwd = StringVar()
entry_usr_pwd = Entry(logInWindow, textvariable=var_usr_pwd, font=('Arial', 14), show='*')
entry_usr_pwd.place(x=120, y=195)

title = Label(logInWindow, text='学生学籍管理系统', bg='white', font=('Arial', 30), width=30, height=2)
title.pack()

btn_login = Button(logInWindow, text='Login', command=chooseTable)
btn_login.place(x=185, y=250)

logInWindow.mainloop()

