from tkinter import *
from tkinter.ttk import Treeview
from dao.StudentDao import StudentDao
from tkinter.simpledialog import *
import tkinter.messagebox
from po.student import Student

sd = StudentDao()
window = Tk()
window.geometry('800x500')

table = Treeview(columns=('sno', 'sname', 'ssex', 'sclass', 'smajor', 'sdept', 'sbir', 'stele'), show="headings")
table.column('sno', width=100)
table.column('sname', width=100)
table.column('ssex', width=100)
table.column('sclass', width=100)
table.column('smajor', width=100)
table.column('sdept', width=100)
table.column('sbir', width=100)
table.column('stele', width=100)
table.heading('sno', text='学号')
table.heading('sname', text='姓名')
table.heading('ssex', text='性别')
table.heading('sclass', text='班级')
table.heading('smajor', text='专业')
table.heading('sdept', text='院系')
table.heading('sbir', text='出生日期')
table.heading('stele', text='联系电话')


def load():
    for i in table.get_children():
        table.delete(i)
    for i in sd.list_book():
        table.insert('', END, values=i)


def add():
    sno = askstring('提示', '请输入学生学号')
    sname = askstring('提示', '请输入学生姓名')
    ssex = askstring('提示', '请输入学生性别')
    sclass = askstring('提示', '请输入学生班级')
    smajor = askstring('提示', '请输入学生专业')
    sdept = askstring('提示', '请输入学生院系')
    sbir = askstring('提示', '请输入学生出生日期')
    stele = askstring('提示', '请输入学生电话号码')
    if sno is not None and sname is not None:
        r = sd.addStudent(Student(sno=sno, sname=sname, ssex=ssex, sclass=sclass, smajor=smajor,
                                  sdept=sdept, sbir=sbir, stele=stele))
        tkinter.messagebox.showinfo(r,"成功增加数据")


def delete():
    sno = askstring('提示', '请输入学生学号')
    sname = askstring('提示', '请输入学生姓名')
    ssex = askstring('提示', '请输入学生性别')
    sclass = askstring('提示', '请输入学生班级')
    smajor = askstring('提示', '请输入学生专业')
    sdept = askstring('提示', '请输入学生院系')
    sbir = askstring('提示', '请输入学生出生日期')
    stele = askstring('提示', '请输入学生电话号码')
    if sno is not None and sname is not None:
        r = sd.addStudent(Student(sno=sno, sname=sname, ssex=ssex, sclass=sclass, smajor=smajor,
                                  sdept=sdept, sbir=sbir, stele=stele))
        tkinter.messagebox.showerror(r, "成功增加数据")


Button(text='加载', command=load).place(x=200, y=350)
Button(text='增加', command=add).place(x=400, y=350)
Button(text='删除', command=delete).place(x=600, y=350)

table.place(width=800, height=300)
window.mainloop()

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
