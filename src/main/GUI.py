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
    def insertWindow(self):
        insert_window = Tk(className='增加选项')
        Label(insert_window, text='学号', font=('宋体', 14)).place(x=10, y=50)
        Label(insert_window, text='姓名', font=('宋体', 14)).place(x=10, y=100)
        Label(insert_window, text='性别', font=('宋体', 14)).place(x=10, y=150)
        Label(insert_window, text='班级', font=('宋体', 14)).place(x=10, y=200)
        Label(insert_window, text='专业', font=('宋体', 14)).place(x=10, y=250)
        Label(insert_window, text='院系', font=('宋体', 14)).place(x=10, y=300)
        Label(insert_window, text='出生日期', font=('宋体', 14)).place(x=10, y=350)
        Label(insert_window, text='联系电话', font=('宋体', 14)).place(x=10, y=400)

        var_sno = StringVar()
        entry_sno = Entry(insert_window, textvariable=var_sno, font=('宋体', 14))
        entry_sno.place(x=100, y=50)

        var_sname = StringVar()
        entry_sname = Entry(insert_window, textvariable=var_sname, font=('宋体', 14))
        entry_sname.place(x=100, y=100)

        var_ssex = StringVar()
        entry_ssex = Entry(insert_window, textvariable=var_ssex, font=('宋体', 14))
        entry_ssex.place(x=100, y=150)

        var_sclass = StringVar()
        entry_sclass = Entry(insert_window, textvariable=var_sclass, font=('宋体', 14))
        entry_sclass.place(x=100, y=200)

        var_smajor = StringVar()
        entry_smajor = Entry(insert_window, textvariable=var_smajor, font=('宋体', 14))
        entry_smajor.place(x=100, y=250)

        var_sdept = StringVar()
        entry_sdept = Entry(insert_window, textvariable=var_sdept, font=('宋体', 14))
        entry_sdept.place(x=100, y=300)

        var_sbir = StringVar()
        entry_sbir = Entry(insert_window, textvariable=var_sbir, font=('宋体', 14))
        entry_sbir.place(x=100, y=350)

        var_stele = StringVar()
        entry_stele = Entry(insert_window, textvariable=var_stele, font=('宋体', 14))
        entry_stele.place(x=100, y=400)


        def textPrint():
            print(var_sno.get())
            print(var_sname.get())
            print(var_ssex.get())
            print(var_sclass.get())
            print(var_smajor.get())
            print(var_sdept.get())
            print(var_sbir.get())
            print(var_stele.get())

        btn_insert = Button(insert_window, text='确定', command=textPrint)
        btn_quit = Button(insert_window, text='退出', command=textPrint)
        btn_insert.place(x=150, y=450)
        btn_quit.place(x=250, y=450)

        insert_window.geometry('400x500')


table_op = TableOperation()

def chooseOp():
    choose_table_window.destroy()
    global choose_op_window
    choose_op_window = Tk()
    choose_op_window.title('操作选项')
    width = 72
    height = 1
    Button(choose_op_window, text='增加', width=width, height=height,
           command=table_op.insertWindow, bg='light yellow', font='楷体').grid(row=0, column=1, padx=10, pady=20)
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

