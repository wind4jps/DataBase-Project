from tkinter import *
from tkinter.ttk import Treeview
from dao.StudentDao import StudentDao
from tkinter.simpledialog import *
import tkinter.messagebox
from po.student import Student

sd = StudentDao()
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
        insert_window.geometry('400x500')
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

        def addStudent():
            sno = entry_sno.get()
            sname = entry_sname.get()
            ssex = entry_ssex.get()
            sclass = entry_sclass.get()
            smajor = entry_smajor.get()
            sdept = entry_sdept.get()
            sbir = entry_sbir.get()
            stele = entry_stele.get()
            if sno is not None and sname is not None:
                r = sd.addStudent(Student(sno=sno, sname=sname, ssex=ssex, sclass=sclass, smajor=smajor,
                                          sdept=sdept, sbir=sbir, stele=stele))
                tkinter.messagebox.showinfo(r, "成功增加数据")
                # 清空输入文本框
                entry_sno.delete(0, END)
                entry_sname.delete(0, END)
                entry_ssex.delete(0, END)
                entry_sclass.delete(0, END)
                entry_smajor.delete(0, END)
                entry_sdept.delete(0, END)
                entry_sbir.delete(0, END)
                entry_stele.delete(0, END)

        btn_insert = Button(insert_window, text='确定', command=addStudent)
        btn_quit = Button(insert_window, text='退出', command=insert_window.destroy)
        btn_insert.place(x=150, y=450)
        btn_quit.place(x=250, y=450)

    def deleteWindow(self):
        delete_window = Tk(className='删除选项')
        delete_window.geometry('600x400')
        Label(delete_window, text='输入要删除学生的学号', font=('宋体', 14)).place(x=10, y=50)
        Label(delete_window, text='删除该班级的全部学生', font=('宋体', 14)).place(x=10, y=125)
        Label(delete_window, text='删除该专业的全部学生', font=('宋体', 14)).place(x=10, y=200)
        Label(delete_window, text='删除该院系的全部学生', font=('宋体', 14)).place(x=10, y=275)

        def textPrint():
            print(entry_sno.get())

        def deleteStudent():
            sno = entry_sno.get()
            sclass = entry_sclass.get()
            smajor = entry_smajor.get()
            sdept = entry_sdept.get()
            if sno != '':
                r = sd.delStudentBySno(Student(sno=sno))
                tkinter.messagebox.showinfo(r, '成功删除')
                entry_sno.delete(0, END)
            elif sclass != '':
                r = sd.delStudentBySclass(Student(sclass=sclass))
                tkinter.messagebox.showinfo(r, '成功删除')
                entry_sclass.delete(0, END)
            elif smajor != '':
                r = sd.deleStudentBySmajor(Student(smajor=smajor))
                tkinter.messagebox.showinfo(r, '成功删除')
                entry_smajor.delete(0, END)
            elif sdept != '':
                r = sd.deleStudentBySdept(Student(sdept=sdept))
                tkinter.messagebox.showinfo(r, '成功删除')
                entry_sdept.delete(0, END)

        def deletAllStudent():
            msg = tkinter.messagebox.askokcancel('确认', '确定要删除所有数据吗?')
            if msg:
                r = sd.deleStudentAll()
                tkinter.messagebox.showinfo(r, '删除成功')


        var_sno = StringVar()
        entry_sno = Entry(delete_window, textvariable=var_sno, font=('宋体', 14))
        entry_sno.place(x=220, y=50)
        btn_delete_sno = Button(delete_window, text='删除', command=deleteStudent)
        btn_delete_sno.place(x=450, y=45)

        var_sclass = StringVar()
        entry_sclass = Entry(delete_window, textvariable=var_sclass, font=('宋体', 14))
        entry_sclass.place(x=220, y=125)
        btn_delete_sclass = Button(delete_window, text='删除', command=deleteStudent)
        btn_delete_sclass.place(x=450, y=120)

        var_smajor = StringVar()
        entry_smajor = Entry(delete_window, textvariable=var_smajor, font=('宋体', 14))
        entry_smajor.place(x=220, y=200)
        btn_delete_smajor = Button(delete_window, text='删除', command=deleteStudent)
        btn_delete_smajor.place(x=450, y=195)

        var_sdept = StringVar()
        entry_sdept = Entry(delete_window, textvariable=var_sdept, font=('宋体', 14))
        entry_sdept.place(x=220, y=275)
        btn_delete_sdept = Button(delete_window, text='删除', command=deleteStudent)
        btn_delete_sdept.place(x=450, y=270)

        btn_delete_all = Button(delete_window, text='删除全部数据', command=deletAllStudent)
        btn_quit = Button(delete_window, text='退出', width=10, height=2, command=delete_window.destroy)
        btn_delete_all.place(x=10, y=330)
        btn_quit.place(x=270, y=330)


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
           command=table_op.deleteWindow, bg='light yellow', font='楷体').grid(row=10, column=1, padx=10, pady=20)
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
    # print(var_user_name.get())
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

