from tkinter import *
from tkinter.ttk import Treeview
from dao.StudentDao import *
import tkinter.messagebox
from po.student import *

sd = StudentDao()
cd = CourseDao()
scd = SCDao()


class StudentTableOperation:
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
                if r == "操作失败":
                    tkinter.messagebox.showerror(r, "数据增加失败")
                else:
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

        def deleteStudent():
            sno = entry_sno.get()
            sclass = entry_sclass.get()
            smajor = entry_smajor.get()
            sdept = entry_sdept.get()
            if sno != '':
                r = sd.delStudentBySno(Student(sno=sno))
                if r == "操作失败":
                    tkinter.messagebox.showerror(r, '删除失败')
                else:
                    tkinter.messagebox.showinfo(r, '成功删除')
                entry_sno.delete(0, END)
            elif sclass != '':
                r = sd.delStudentBySclass(Student(sclass=sclass))
                if r == "操作失败":
                    tkinter.messagebox.showerror(r, '删除失败')
                else:
                    tkinter.messagebox.showinfo(r, '成功删除')
                entry_sclass.delete(0, END)
            elif smajor != '':
                r = sd.deleStudentBySmajor(Student(smajor=smajor))
                if r == "操作失败":
                    tkinter.messagebox.showerror(r, '删除失败')
                else:
                    tkinter.messagebox.showinfo(r, '成功删除')
                entry_smajor.delete(0, END)
            elif sdept != '':
                r = sd.deleStudentBySdept(Student(sdept=sdept))
                if r == "操作失败":
                    tkinter.messagebox.showerror(r, '删除失败')
                else:
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

    def selectWindow(self):
        # choose_op_window.destroy()
        select_window = Tk(className='查询选项')
        select_window.geometry('600x400')
        Label(select_window, text='输入要查询学生的学号', font=('宋体', 14)).place(x=10, y=50)
        Label(select_window, text='查询该班级的全部学生', font=('宋体', 14)).place(x=10, y=125)
        Label(select_window, text='查询该专业的全部学生', font=('宋体', 14)).place(x=10, y=200)
        Label(select_window, text='查询该院系的全部学生', font=('宋体', 14)).place(x=10, y=275)

        def selectStudentBySno():
            info_window = Tk()
            info_window.title('学生信息')
            info_window.geometry('800x500')

            def loadStudent():
                sno = entry_sno.get()
                for i in table.get_children():
                    table.delete(i)
                for i in sd.list_student_by_sno(Student(sno=sno)):
                    table.insert('', END, values=i)
                entry_sno.delete(0, END)

            table = Treeview(info_window, columns=('sno', 'sname', 'ssex', 'sclass', 'smajor', 'sdept', 'sbir', 'stele'),
                             show="headings")
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
            table.place(width=800, height=300)

            loadStudent()
            btn_quit = Button(info_window, text='退出', width=10, height=2, command=info_window.destroy)
            btn_quit.place(x=360, y=400)
            info_window.mainloop()

        def selectStudentBySclass():
            info_window = Tk()
            info_window.title('学生信息')
            info_window.geometry('800x500')

            def loadStudent():
                sclass = entry_sclass.get()
                for i in table.get_children():
                    table.delete(i)
                for i in sd.list_student_by_sclass(Student(sclass=sclass)):
                    table.insert('', END, values=i)
                entry_sclass.delete(0, END)

            table = Treeview(info_window, columns=('sno', 'sname', 'ssex', 'sclass', 'smajor', 'sdept', 'sbir', 'stele'),
                             show="headings")
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
            table.place(width=800, height=300)

            loadStudent()
            btn_quit = Button(info_window, text='退出', width=10, height=2, command=info_window.destroy)
            btn_quit.place(x=360, y=400)
            info_window.mainloop()

        def selectStudentBySmajor():
            info_window = Tk()
            info_window.title('学生信息')
            info_window.geometry('800x500')

            def loadStudent():
                smajor = entry_smajor.get()
                for i in table.get_children():
                    table.delete(i)
                for i in sd.list_student_by_smajor(Student(smajor=smajor)):
                    table.insert('', END, values=i)
                entry_smajor.delete(0, END)

            table = Treeview(info_window, columns=('sno', 'sname', 'ssex', 'sclass', 'smajor', 'sdept', 'sbir', 'stele'),
                             show="headings")
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
            table.place(width=800, height=300)

            loadStudent()
            btn_quit = Button(info_window, text='退出', width=10, height=2, command=info_window.destroy)
            btn_quit.place(x=360, y=400)
            info_window.mainloop()

        def selectStudentBySdept():
            info_window = Tk()
            info_window.title('学生信息')
            info_window.geometry('800x500')

            def loadStudent():
                sdept = entry_sdept.get()
                for i in table.get_children():
                    table.delete(i)
                for i in sd.list_student_by_sdept(Student(sdept=sdept)):
                    table.insert('', END, values=i)
                entry_sdept.delete(0, END)

            table = Treeview(info_window, columns=('sno', 'sname', 'ssex', 'sclass', 'smajor', 'sdept', 'sbir', 'stele'),
                             show="headings")
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
            table.place(width=800, height=300)

            loadStudent()
            btn_quit = Button(info_window, text='退出', width=10, height=2, command=info_window.destroy)
            btn_quit.place(x=360, y=400)
            info_window.mainloop()

        def selectAllStudent():
            info_window = Tk()
            info_window.title('学生信息')
            info_window.geometry('800x500')

            def loadStudent():
                for i in table.get_children():
                    table.delete(i)
                for i in sd.list_student():
                    table.insert('', END, values=i)
                entry_sno.delete(0, END)

            table = Treeview(info_window, columns=('sno', 'sname', 'ssex', 'sclass', 'smajor', 'sdept', 'sbir', 'stele'),
                             show="headings")
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
            table.place(width=800, height=300)

            loadStudent()
            btn_quit = Button(info_window, text='退出', width=10, height=2, command=info_window.destroy)
            btn_quit.place(x=360, y=400)
            info_window.mainloop()


        var_sno = StringVar()
        entry_sno = Entry(select_window, textvariable=var_sno, font=('宋体', 14))
        entry_sno.place(x=220, y=50)
        btn_select_sno = Button(select_window, text='查询', command=selectStudentBySno)
        btn_select_sno.place(x=450, y=45)

        var_sclass = StringVar()
        entry_sclass = Entry(select_window, textvariable=var_sclass, font=('宋体', 14))
        entry_sclass.place(x=220, y=125)
        btn_select_sclass = Button(select_window, text='查询', command=selectStudentBySclass)
        btn_select_sclass.place(x=450, y=120)

        var_smajor = StringVar()
        entry_smajor = Entry(select_window, textvariable=var_smajor, font=('宋体', 14))
        entry_smajor.place(x=220, y=200)
        btn_select_smajor = Button(select_window, text='查询', command=selectStudentBySmajor)
        btn_select_smajor.place(x=450, y=195)

        var_sdept = StringVar()
        entry_sdept = Entry(select_window, textvariable=var_sdept, font=('宋体', 14))
        entry_sdept.place(x=220, y=275)
        btn_select_sdept = Button(select_window, text='查询', command=selectStudentBySdept)
        btn_select_sdept.place(x=450, y=270)

        btn_select_all = Button(select_window, text='查询全部学生', command=selectAllStudent)
        btn_quit = Button(select_window, text='退出', width=10, height=2, command=select_window.destroy)
        btn_select_all.place(x=10, y=330)
        btn_quit.place(x=270, y=330)

    def updateWindow(self):
        update_window = Tk(className='修改选项')
        update_window.geometry('600x500')
        Label(update_window, text='请输入要修改学生的学号', font=('宋体', 14)).place(x=10, y=50)
        Label(update_window, text='新姓名', font=('宋体', 14)).place(x=10, y=100)
        Label(update_window, text='新性别', font=('宋体', 14)).place(x=10, y=150)
        Label(update_window, text='新班级', font=('宋体', 14)).place(x=10, y=200)
        Label(update_window, text='新专业', font=('宋体', 14)).place(x=10, y=250)
        Label(update_window, text='新院系', font=('宋体', 14)).place(x=10, y=300)
        Label(update_window, text='新出生日期', font=('宋体', 14)).place(x=10, y=350)
        Label(update_window, text='新联系电话', font=('宋体', 14)).place(x=10, y=400)

        var_sno = StringVar()
        entry_sno = Entry(update_window, textvariable=var_sno, font=('宋体', 14))
        entry_sno.place(x=240, y=50)

        var_sname = StringVar()
        entry_sname = Entry(update_window, textvariable=var_sname, font=('宋体', 14))
        entry_sname.place(x=240, y=100)

        var_ssex = StringVar()
        entry_ssex = Entry(update_window, textvariable=var_ssex, font=('宋体', 14))
        entry_ssex.place(x=240, y=150)

        var_sclass = StringVar()
        entry_sclass = Entry(update_window, textvariable=var_sclass, font=('宋体', 14))
        entry_sclass.place(x=240, y=200)

        var_smajor = StringVar()
        entry_smajor = Entry(update_window, textvariable=var_smajor, font=('宋体', 14))
        entry_smajor.place(x=240, y=250)

        var_sdept = StringVar()
        entry_sdept = Entry(update_window, textvariable=var_sdept, font=('宋体', 14))
        entry_sdept.place(x=240, y=300)

        var_sbir = StringVar()
        entry_sbir = Entry(update_window, textvariable=var_sbir, font=('宋体', 14))
        entry_sbir.place(x=240, y=350)

        var_stele = StringVar()
        entry_stele = Entry(update_window, textvariable=var_stele, font=('宋体', 14))
        entry_stele.place(x=240, y=400)

        def updateStudent():
            sno = entry_sno.get()
            sname = entry_sname.get()
            ssex = entry_ssex.get()
            sclass = entry_sclass.get()
            smajor = entry_smajor.get()
            sdept = entry_sdept.get()
            sbir = entry_sbir.get()
            stele = entry_stele.get()
            flag = True
            if sno != '':
                if sname != '':
                    r1 = sd.updStudentName(Student(sno=sno, sname=sname))
                    if r1 == "修改失败":
                        tkinter.messagebox.showerror(r1, "学生姓名修改失败")
                        flag = False
                if ssex != '':
                    r2 = sd.updStudentSex(Student(sno=sno, ssex=ssex))
                    if r2 == "修改失败":
                        tkinter.messagebox.showerror(r2, "学生性别修改失败")
                        flag = False
                if sclass != '':
                    r3 = sd.updStudentClass(Student(sno=sno, sclass=sclass))
                    if r3 == "修改失败":
                        tkinter.messagebox.showerror(r3, "学生班级修改失败")
                        flag = False
                if smajor != '':
                    r4 = sd.updStudentMajor(Student(sno=sno, smajor=smajor))
                    if r4 == "修改失败":
                        tkinter.messagebox.showerror(r4, "学生专业修改失败")
                        flag = False
                if sdept != '':
                    r5 = sd.updStudentDept(Student(sno=sno, sdept=sdept))
                    if r5 == "修改失败":
                        tkinter.messagebox.showerror(r5, "学生院系修改失败")
                        flag = False
                if sbir != '':
                    r6 = sd.updStudentBir(Student(sno=sno, sbir=sbir))
                    if r6 == "修改失败":
                        tkinter.messagebox.showerror(r6, "学生出生日期修改失败")
                        flag = False
                if stele != '':
                    r7 = sd.updStudentTele(Student(sno=sno, stele=stele))
                    if r7 == "修改失败":
                        tkinter.messagebox.showerror(r7, "学生联系电话修改失败")
                        flag = False
                entry_sno.delete(0, END)
                entry_sname.delete(0, END)
                entry_ssex.delete(0, END)
                entry_sclass.delete(0, END)
                entry_smajor.delete(0, END)
                entry_sdept.delete(0, END)
                entry_sbir.delete(0, END)
                entry_stele.delete(0, END)
                if flag:
                    tkinter.messagebox.showinfo("操作成功", "该学生信息修改成功")
            else:
                tkinter.messagebox.showerror("操作失败", "修改的学生学号不能为空")

        btn_insert = Button(update_window, text='修改', command=updateStudent)
        btn_quit = Button(update_window, text='退出', command=update_window.destroy)
        btn_insert.place(x=220, y=450)
        btn_quit.place(x=320, y=450)


class CourseTableOperation:
    def insertWindow(self):
        insert_window = Tk(className='增加选项')
        insert_window.geometry('400x300')
        Label(insert_window, text='课程号', font=('宋体', 14)).place(x=10, y=50)
        Label(insert_window, text='课程名', font=('宋体', 14)).place(x=10, y=100)
        Label(insert_window, text='教师教工号', font=('宋体', 14)).place(x=10, y=150)
        Label(insert_window, text='课程学分', font=('宋体', 14)).place(x=10, y=200)

        var_cno = StringVar()
        entry_cno = Entry(insert_window, textvariable=var_cno, font=('宋体', 14))
        entry_cno.place(x=150, y=50)

        var_cname = StringVar()
        entry_cname = Entry(insert_window, textvariable=var_cname, font=('宋体', 14))
        entry_cname.place(x=150, y=100)

        var_tno = StringVar()
        entry_tno = Entry(insert_window, textvariable=var_tno, font=('宋体', 14))
        entry_tno.place(x=150, y=150)

        var_ccredit = DoubleVar()
        entry_ccredit = Entry(insert_window, textvariable=var_ccredit, font=('宋体', 14))
        entry_ccredit.place(x=150, y=200)

        def addCourse():
            cno = entry_cno.get()
            cname = entry_cname.get()
            tno = entry_tno.get()
            ccredit = entry_ccredit.get()
            if cno is not None and cname is not None and tno is not None and ccredit is not None:
                r = cd.addCourse(Course(cno=cno, cname=cname, tno=tno, ccredit=ccredit))
                if r == "操作失败":
                    tkinter.messagebox.showerror(r, "数据增加失败")
                else:
                    tkinter.messagebox.showinfo(r, "成功增加数据")
                # 清空输入文本框
                entry_cno.delete(0, END)
                entry_cname.delete(0, END)
                entry_tno.delete(0, END)
                entry_ccredit.delete(0, END)

        btn_insert = Button(insert_window, text='确定', command=addCourse)
        btn_quit = Button(insert_window, text='退出', command=insert_window.destroy)
        btn_insert.place(x=150, y=250)
        btn_quit.place(x=250, y=250)

    def deleteWindow(self):
        delete_window = Tk(className='删除选项')
        delete_window.geometry('600x300')
        Label(delete_window, text='输入要删除课程的课程号', font=('宋体', 14)).place(x=10, y=50)
        Label(delete_window, text='删除该课程名的全部课程', font=('宋体', 14)).place(x=10, y=125)
        Label(delete_window, text='删除该教工号教授的全部课程', font=('宋体', 14)).place(x=10, y=200)

        def deleteCourse():
            cno = entry_cno.get()
            cname = entry_cname.get()
            tno = entry_tno.get()
            if cno != '':
                r = cd.delCourseByCno(Course(cno=cno))
                if r == "操作失败":
                    tkinter.messagebox.showerror(r, '删除失败')
                else:
                    tkinter.messagebox.showinfo(r, '成功删除')
                entry_cno.delete(0, END)
            elif cname != '':
                r = cd.delCourseByCname(Course(cname=cname))
                if r == "操作失败":
                    tkinter.messagebox.showerror(r, '删除失败')
                else:
                    tkinter.messagebox.showinfo(r, '成功删除')
                entry_cname.delete(0, END)
            elif tno != '':
                r = cd.delCourseByTno(Course(tno=tno))
                if r == "操作失败":
                    tkinter.messagebox.showerror(r, '删除失败')
                else:
                    tkinter.messagebox.showinfo(r, '成功删除')
                entry_tno.delete(0, END)

        def deletAllCourse():
            msg = tkinter.messagebox.askokcancel('确认', '确定要删除所有数据吗?')
            if msg:
                r = cd.delCourseAll()
                if r == "操作失败":
                    tkinter.messagebox.showerror(r, '删除失败')
                else:
                    tkinter.messagebox.showinfo(r, '成功删除')


        var_cno = StringVar()
        entry_cno = Entry(delete_window, textvariable=var_cno, font=('宋体', 14))
        entry_cno.place(x=270, y=50)
        btn_delete_cno = Button(delete_window, text='删除', command=deleteCourse)
        btn_delete_cno.place(x=485, y=45)

        var_cname = StringVar()
        entry_cname = Entry(delete_window, textvariable=var_cname, font=('宋体', 14))
        entry_cname.place(x=270, y=125)
        btn_delete_cname = Button(delete_window, text='删除', command=deleteCourse)
        btn_delete_cname.place(x=485, y=120)

        var_tno = StringVar()
        entry_tno = Entry(delete_window, textvariable=var_tno, font=('宋体', 14))
        entry_tno.place(x=270, y=200)
        btn_delete_tno = Button(delete_window, text='删除', command=deleteCourse)
        btn_delete_tno.place(x=485, y=195)

        btn_delete_all = Button(delete_window, text='删除全部数据', command=deletAllCourse)
        btn_quit = Button(delete_window, text='退出', width=10, height=2, command=delete_window.destroy)
        btn_delete_all.place(x=10, y=240)
        btn_quit.place(x=270, y=240)

    def selectWindow(self):
        # choose_op_window.destroy()
        select_window = Tk(className='查询选项')
        select_window.geometry('600x400')
        Label(select_window, text='输入要查询课程的课程号', font=('宋体', 14)).place(x=10, y=50)
        Label(select_window, text='查询该课程名的全部课程', font=('宋体', 14)).place(x=10, y=125)
        Label(select_window, text='查询该教工号教师的全部课程', font=('宋体', 14)).place(x=10, y=200)
        Label(select_window, text='查询该学分的所有课程', font=('宋体', 14)).place(x=10, y=275)

        def selectCourseByCno():
            info_window = Tk()
            info_window.title('课程信息')
            info_window.geometry('800x500')

            def loadCourse():
                cno = entry_cno.get()
                for i in table.get_children():
                    table.delete(i)
                for i in cd.list_course_by_cno(Course(cno=cno)):
                    table.insert('', END, values=i)
                entry_cno.delete(0, END)

            table = Treeview(info_window, columns=('cno', 'cname', 'tno', 'ccredit'), show="headings")
            table.column('cno', width=100)
            table.column('cname', width=100)
            table.column('tno', width=100)
            table.column('ccredit', width=100)
            table.heading('cno', text='课程号')
            table.heading('cname', text='课程名')
            table.heading('tno', text='教工号')
            table.heading('ccredit', text='学分')
            table.place(width=800, height=300)

            loadCourse()
            btn_quit = Button(info_window, text='退出', width=10, height=2, command=info_window.destroy)
            btn_quit.place(x=360, y=400)
            info_window.mainloop()

        def selectCourseByCname():
            info_window = Tk()
            info_window.title('课程信息')
            info_window.geometry('800x500')

            def loadCourse():
                cname = entry_cname.get()
                for i in table.get_children():
                    table.delete(i)
                for i in cd.list_course_by_cname(Course(cname=cname)):
                    table.insert('', END, values=i)
                entry_cname.delete(0, END)

            table = Treeview(info_window, columns=('cno', 'cname', 'tno', 'ccredit'), show="headings")
            table.column('cno', width=100)
            table.column('cname', width=100)
            table.column('tno', width=100)
            table.column('ccredit', width=100)
            table.heading('cno', text='课程号')
            table.heading('cname', text='课程名')
            table.heading('tno', text='教工号')
            table.heading('ccredit', text='学分')
            table.place(width=800, height=300)

            loadCourse()
            btn_quit = Button(info_window, text='退出', width=10, height=2, command=info_window.destroy)
            btn_quit.place(x=360, y=400)
            info_window.mainloop()

        def selectCourseByTno():
            info_window = Tk()
            info_window.title('课程信息')
            info_window.geometry('800x500')

            def loadCourse():
                tno = entry_tno.get()
                for i in table.get_children():
                    table.delete(i)
                for i in cd.list_course_by_tno(Course(tno=tno)):
                    table.insert('', END, values=i)
                entry_tno.delete(0, END)

            table = Treeview(info_window, columns=('cno', 'cname', 'tno', 'ccredit'), show="headings")
            table.column('cno', width=100)
            table.column('cname', width=100)
            table.column('tno', width=100)
            table.column('ccredit', width=100)
            table.heading('cno', text='课程号')
            table.heading('cname', text='课程名')
            table.heading('tno', text='教工号')
            table.heading('ccredit', text='学分')
            table.place(width=800, height=300)

            loadCourse()
            btn_quit = Button(info_window, text='退出', width=10, height=2, command=info_window.destroy)
            btn_quit.place(x=360, y=400)
            info_window.mainloop()

        def selectCourseByCredit():
            info_window = Tk()
            info_window.title('课程信息')
            info_window.geometry('800x500')

            def loadCourse():
                ccredit = entry_ccredit.get()
                for i in table.get_children():
                    table.delete(i)
                for i in cd.list_course_by_ccredit(Course(ccredit=ccredit)):
                    table.insert('', END, values=i)
                entry_ccredit.delete(0, END)

            table = Treeview(info_window, columns=('cno', 'cname', 'tno', 'ccredit'), show="headings")
            table.column('cno', width=100)
            table.column('cname', width=100)
            table.column('tno', width=100)
            table.column('ccredit', width=100)
            table.heading('cno', text='课程号')
            table.heading('cname', text='课程名')
            table.heading('tno', text='教工号')
            table.heading('ccredit', text='学分')
            table.place(width=800, height=300)

            loadCourse()
            btn_quit = Button(info_window, text='退出', width=10, height=2, command=info_window.destroy)
            btn_quit.place(x=360, y=400)
            info_window.mainloop()

        def selectAllCourse():
            info_window = Tk()
            info_window.title('学生信息')
            info_window.geometry('800x500')

            def loadCourse():
                for i in table.get_children():
                    table.delete(i)
                for i in cd.list_course():
                    table.insert('', END, values=i)
                entry_cno.delete(0, END)

            table = Treeview(info_window, columns=('cno', 'cname', 'tno', 'ccredit'),show="headings")
            table.column('cno', width=100)
            table.column('cname', width=100)
            table.column('tno', width=100)
            table.column('ccredit', width=100)
            table.heading('cno', text='课程号')
            table.heading('cname', text='课程名')
            table.heading('tno', text='教工号')
            table.heading('ccredit', text='学分')
            table.place(width=800, height=300)

            loadCourse()
            btn_quit = Button(info_window, text='退出', width=10, height=2, command=info_window.destroy)
            btn_quit.place(x=360, y=400)
            info_window.mainloop()


        var_cno = StringVar()
        entry_cno = Entry(select_window, textvariable=var_cno, font=('宋体', 14))
        entry_cno.place(x=270, y=50)
        btn_select_cno = Button(select_window, text='查询', command=selectCourseByCno)
        btn_select_cno.place(x=490, y=45)

        var_cname = StringVar()
        entry_cname = Entry(select_window, textvariable=var_cname, font=('宋体', 14))
        entry_cname.place(x=270, y=125)
        btn_select_cname = Button(select_window, text='查询', command=selectCourseByCname)
        btn_select_cname.place(x=490, y=120)

        var_tno = StringVar()
        entry_tno = Entry(select_window, textvariable=var_tno, font=('宋体', 14))
        entry_tno.place(x=270, y=200)
        btn_select_tno = Button(select_window, text='查询', command=selectCourseByTno)
        btn_select_tno.place(x=490, y=195)

        var_ccredit = DoubleVar()
        entry_ccredit = Entry(select_window, textvariable=var_ccredit, font=('宋体', 14))
        entry_ccredit.place(x=270, y=275)
        btn_select_ccredit = Button(select_window, text='查询', command=selectCourseByCredit)
        btn_select_ccredit.place(x=490, y=270)

        btn_select_all = Button(select_window, text='查询全部课程', command=selectAllCourse)
        btn_quit = Button(select_window, text='退出', width=10, height=2, command=select_window.destroy)
        btn_select_all.place(x=10, y=330)
        btn_quit.place(x=270, y=330)

    def updateWindow(self):
        update_window = Tk(className='修改选项')
        update_window.geometry('600x300')
        Label(update_window, text='请输入要修改课程的课程号', font=('宋体', 14)).place(x=10, y=50)
        Label(update_window, text='新课程名', font=('宋体', 14)).place(x=10, y=100)
        Label(update_window, text='新教工号', font=('宋体', 14)).place(x=10, y=150)
        Label(update_window, text='新课程学分', font=('宋体', 14)).place(x=10, y=200)

        var_cno = StringVar()
        entry_cno = Entry(update_window, textvariable=var_cno, font=('宋体', 14))
        entry_cno.place(x=250, y=50)

        var_cname = StringVar()
        entry_cname = Entry(update_window, textvariable=var_cname, font=('宋体', 14))
        entry_cname.place(x=250, y=100)

        var_tno = StringVar()
        entry_tno = Entry(update_window, textvariable=var_tno, font=('宋体', 14))
        entry_tno.place(x=250, y=150)

        var_ccredit = DoubleVar()
        entry_ccredit = Entry(update_window, textvariable=var_ccredit, font=('宋体', 14))
        entry_ccredit.place(x=250, y=200)

        def updateCourse():
            cno = entry_cno.get()
            cname = entry_cname.get()
            tno = entry_tno.get()
            ccredit = entry_ccredit.get()
            flag = True
            if cno != '':
                if cname != '':
                    r1 = cd.updCourseName(Course(cno=cno, cname=cname))
                    if r1 == "修改失败":
                        tkinter.messagebox.showerror(r1, "课程名称修改失败")
                        flag = False
                if tno != '':
                    r2 = cd.updCourseTno(Course(cno=cno, tno=tno))
                    if r2 == "修改失败":
                        tkinter.messagebox.showerror(r2, "课程教工号修改失败")
                        flag = False
                if ccredit != '':
                    r3 = cd.updCourseCreit(Course(cno=cno, ccredit=ccredit))
                    if r3 == "修改失败":
                        tkinter.messagebox.showerror(r3, "课程学分修改失败")
                        flag = False
                entry_cno.delete(0, END)
                entry_cname.delete(0, END)
                entry_tno.delete(0, END)
                entry_ccredit.delete(0, END)
                if flag:
                    tkinter.messagebox.showinfo("操作成功", "该课程信息修改成功")
            else:
                tkinter.messagebox.showerror("操作失败", "修改的课程课程号不能为空")

        btn_insert = Button(update_window, text='修改', command=updateCourse)
        btn_quit = Button(update_window, text='退出', command=update_window.destroy)
        btn_insert.place(x=220, y=250)
        btn_quit.place(x=320, y=250)


class SCTableOperation:
    def insertWindow(self):
        insert_window = Tk(className='增加选项')
        insert_window.geometry('400x250')
        Label(insert_window, text='学号', font=('宋体', 14)).place(x=10, y=50)
        Label(insert_window, text='课程号', font=('宋体', 14)).place(x=10, y=100)
        Label(insert_window, text='课程成绩', font=('宋体', 14)).place(x=10, y=150)

        var_sno = StringVar()
        entry_sno = Entry(insert_window, textvariable=var_sno, font=('宋体', 14))
        entry_sno.place(x=150, y=50)

        var_cno = StringVar()
        entry_cno = Entry(insert_window, textvariable=var_cno, font=('宋体', 14))
        entry_cno.place(x=150, y=100)

        var_grade = IntVar()
        entry_grade = Entry(insert_window, textvariable=var_grade, font=('宋体', 14))
        entry_grade.place(x=150, y=150)

        def addSC():
            sno = entry_sno.get()
            cno = entry_cno.get()
            grade = entry_grade.get()
            tuple_ccredit = cd.selectCreditByCno(Course(cno=cno))
            ccredit = tuple_ccredit[0][0]
            if sno is not None and cno is not None and ccredit is not None:
                r = scd.addSC(SC(sno=sno, cno=cno, grade=grade, ccredit=ccredit))
                if r == "操作失败":
                    tkinter.messagebox.showerror(r, "数据增加失败")
                else:
                    tkinter.messagebox.showinfo(r, "成功增加数据")
                # 清空输入文本框
                entry_sno.delete(0, END)
                entry_cno.delete(0, END)
                entry_grade.delete(0, END)

        btn_insert = Button(insert_window, text='确定', command=addSC)
        btn_quit = Button(insert_window, text='退出', command=insert_window.destroy)
        btn_insert.place(x=150, y=200)
        btn_quit.place(x=250, y=200)

    def deleteWindow(self):
        delete_window = Tk(className='删除选项')
        delete_window.geometry('700x300')
        Label(delete_window, text='删除该学号学生的全部信息', font=('宋体', 14)).place(x=10, y=50)
        Label(delete_window, text='删除该课程号的全部信息', font=('宋体', 14)).place(x=10, y=125)
        Label(delete_window, text='删除该学生该门课程的信息', font=('宋体', 14)).place(x=10, y=200)

        def deleteSC():
            sno = entry_sno.get()
            cno = entry_cno.get()
            sno1 = entry_sno1.get()
            cno1 = entry_cno1.get()
            if sno != '':
                r = scd.delSCBySno(SC(sno=sno))
                if r == "操作失败":
                    tkinter.messagebox.showerror(r, '删除失败')
                else:
                    tkinter.messagebox.showinfo(r, '成功删除')
                entry_sno.delete(0, END)
            elif cno != '':
                r = scd.delSCByCno(SC(cno=cno))
                if r == "操作失败":
                    tkinter.messagebox.showerror(r, '删除失败')
                else:
                    tkinter.messagebox.showinfo(r, '成功删除')
                entry_cno.delete(0, END)
            elif sno1 != '' and cno1 != '':
                r = scd.delSCBySnoAndCno(SC(sno=sno1, cno=cno1))
                if r == "操作失败":
                    tkinter.messagebox.showerror(r, '删除失败')
                else:
                    tkinter.messagebox.showinfo(r, '成功删除')
                entry_sno1.delete(0, END)
                entry_cno1.delete(0, END)

        def deletAllSC():
            msg = tkinter.messagebox.askokcancel('确认', '确定要删除所有数据吗?')
            if msg:
                r = scd.delSCAll()
                if r == "操作失败":
                    tkinter.messagebox.showerror(r, '删除失败')
                else:
                    tkinter.messagebox.showinfo(r, '成功删除')


        var_sno = StringVar()
        entry_sno = Entry(delete_window, textvariable=var_sno, font=('宋体', 14))
        entry_sno.place(x=270, y=50)
        btn_delete_sno = Button(delete_window, text='删除', command=deleteSC)
        btn_delete_sno.place(x=485, y=45)

        var_cno = StringVar()
        entry_cno = Entry(delete_window, textvariable=var_cno, font=('宋体', 14))
        entry_cno.place(x=270, y=125)
        btn_delete_cno = Button(delete_window, text='删除', command=deleteSC)
        btn_delete_cno.place(x=485, y=120)

        var_sno1 = StringVar()
        entry_sno1 = Entry(delete_window, textvariable=var_sno1, width=15, font=('宋体', 14))
        entry_sno1.place(x=270, y=200)
        var_cno1 = StringVar()
        entry_cno1 = Entry(delete_window, textvariable=var_cno1, width=15, font=('宋体', 14))
        entry_cno1.place(x=450, y=200)
        btn_delete_sno_cno = Button(delete_window, text='删除', command=deleteSC)
        btn_delete_sno_cno.place(x=615, y=195)

        btn_delete_all = Button(delete_window, text='删除全部数据', command=deletAllSC)
        btn_quit = Button(delete_window, text='退出', width=10, height=2, command=delete_window.destroy)
        btn_delete_all.place(x=10, y=240)
        btn_quit.place(x=300, y=240)

    def selectWindow(self):
        # choose_op_window.destroy()
        select_window = Tk(className='查询选项')
        select_window.geometry('760x320')
        Label(select_window, text='查询该学号学生的全部选课情况', font=('宋体', 14)).place(x=10, y=50)
        Label(select_window, text='查询该课程号课程的全部选课情况', font=('宋体', 14)).place(x=10, y=125)
        Label(select_window, text='查询该学号学生该门课程号课程选课情况', font=('宋体', 14)).place(x=10, y=200)

        def selectSCBySno():
            info_window = Tk()
            info_window.title('学生课程信息')
            info_window.geometry('800x500')

            def loadSC():
                sno = entry_sno.get()
                sname_tuple = sd.selectSnameBySno(Student(sno=sno))
                sname = sname_tuple[0][0]
                cname_tuple = []
                val = scd.list_sc_by_sno(SC(sno=sno))
                avg_grade_tuple = scd.avgGradeBySno(SC(sno=sno))
                avg_grade = avg_grade_tuple[0][0]
                for i in range(0, len(val)):
                    cname_tuple.append(cd.selectCnameByCno(Course(cno=val[i][1]))[0][0])
                for i in table.get_children():
                    table.delete(i)
                for i in range(0, len(val)):
                    table.insert('', END, values=(val[i][0], sname, val[i][1], cname_tuple[i], val[i][2], val[i][3]))
                entry_sno.delete(0, END)
                return avg_grade

            table = Treeview(info_window, columns=('sno', 'sname', 'cno', 'cname', 'grade', 'ccredit'), show="headings")
            table.column('sno', width=100)
            table.column('sname', width=100)
            table.column('cno', width=100)
            table.column('cname', width=100)
            table.column('grade', width=100)
            table.column('ccredit', width=100)
            table.heading('sno', text='学号')
            table.heading('sname', text='姓名')
            table.heading('cno', text='课程号')
            table.heading('cname', text='课程名')
            table.heading('grade', text='课程成绩')
            table.heading('ccredit', text='学分')
            table.place(width=800, height=300)

            avg_grade = loadSC()
            Label(info_window, text='该学生平均成绩：', font=('宋体', 12)).place(x=0, y=340)
            Label(info_window, text=avg_grade, font=('宋体', 12)).place(x=120, y=340)
            btn_quit = Button(info_window, text='退出', width=10, height=2, command=info_window.destroy)
            btn_quit.place(x=360, y=400)
            info_window.mainloop()

        def selectSCByCno():
            info_window = Tk()
            info_window.title('学生课程信息')
            info_window.geometry('800x500')

            def loadSC():
                cno = entry_cno.get()
                cname_tuple = cd.selectCnameByCno(Course(cno=cno))
                cname = cname_tuple[0][0]
                sname_tuple = []
                val = scd.list_sc_by_cno(SC(cno=cno))
                avg_grade_tuple = scd.avgGradeByCno(SC(cno=cno))
                avg_grade = avg_grade_tuple[0][0]
                for i in range(0, len(val)):
                    sname_tuple.append(sd.selectSnameBySno(Student(sno=val[i][0]))[0][0])
                for i in table.get_children():
                    table.delete(i)
                for i in range(0, len(val)):
                    table.insert('', END, values=(val[i][0], sname_tuple[i], val[i][1], cname, val[i][2], val[i][3]))
                entry_cno.delete(0, END)
                return avg_grade

            table = Treeview(info_window, columns=('sno', 'sname', 'cno', 'cname', 'grade', 'ccredit'), show="headings")
            table.column('sno', width=100)
            table.column('sname', width=100)
            table.column('cno', width=100)
            table.column('cname', width=100)
            table.column('grade', width=100)
            table.column('ccredit', width=100)
            table.heading('sno', text='学号')
            table.heading('sname', text='姓名')
            table.heading('cno', text='课程号')
            table.heading('cname', text='课程名')
            table.heading('grade', text='课程成绩')
            table.heading('ccredit', text='学分')
            table.place(width=800, height=300)

            avg_grade = loadSC()
            Label(info_window, text='该课程平均成绩：', font=('宋体', 12)).place(x=0, y=340)
            Label(info_window, text=avg_grade, font=('宋体', 12)).place(x=120, y=340)
            btn_quit = Button(info_window, text='退出', width=10, height=2, command=info_window.destroy)
            btn_quit.place(x=360, y=400)
            info_window.mainloop()

        def selectSCBySnoAndCno():
            info_window = Tk()
            info_window.title('学生课程信息')
            info_window.geometry('800x500')

            def loadSC():
                sno = entry_sno1.get()
                sname_tuple = sd.selectSnameBySno(Student(sno=sno))
                sname = sname_tuple[0][0]
                cno = entry_cno1.get()
                cname_tuple = cd.selectCnameByCno(Course(cno=cno))
                cname = cname_tuple[0][0]
                val = scd.list_sc_by_sno_and_cno(SC(sno=sno, cno=cno))
                for i in table.get_children():
                    table.delete(i)
                for i in range(0, len(val)):
                    table.insert('', END, values=(val[i][0], sname, val[i][1], cname, val[i][2], val[i][3]))
                entry_sno1.delete(0, END)
                entry_cno1.delete(0, END)

            table = Treeview(info_window, columns=('sno', 'sname', 'cno', 'cname', 'grade', 'ccredit'), show="headings")
            table.column('sno', width=100)
            table.column('sname', width=100)
            table.column('cno', width=100)
            table.column('cname', width=100)
            table.column('grade', width=100)
            table.column('ccredit', width=100)
            table.heading('sno', text='学号')
            table.heading('sname', text='姓名')
            table.heading('cno', text='课程号')
            table.heading('cname', text='课程名')
            table.heading('grade', text='课程成绩')
            table.heading('ccredit', text='学分')
            table.place(width=800, height=300)

            loadSC()
            btn_quit = Button(info_window, text='退出', width=10, height=2, command=info_window.destroy)
            btn_quit.place(x=360, y=400)
            info_window.mainloop()

        def selectAllSC():
            info_window = Tk()
            info_window.title('学生课程信息')
            info_window.geometry('800x500')

            def loadSC():
                sname_tuple = []
                cname_tuple = []
                val = scd.list_sc()
                for i in range(0, len(val)):
                    sname_tuple.append(sd.selectSnameBySno(Student(sno=val[i][0]))[0][0])
                for i in range(0, len(val)):
                    cname_tuple.append(cd.selectCnameByCno(Course(cno=val[i][1]))[0][0])
                for i in table.get_children():
                    table.delete(i)
                for i in range(0, len(val)):
                    table.insert('', END, values=(val[i][0], sname_tuple[i], val[i][1], cname_tuple[i], val[i][2], val[i][3]))
                entry_sno1.delete(0, END)
                entry_cno1.delete(0, END)

            table = Treeview(info_window, columns=('sno', 'sname', 'cno', 'cname', 'grade', 'ccredit'), show="headings")
            table.column('sno', width=100)
            table.column('sname', width=100)
            table.column('cno', width=100)
            table.column('cname', width=100)
            table.column('grade', width=100)
            table.column('ccredit', width=100)
            table.heading('sno', text='学号')
            table.heading('sname', text='姓名')
            table.heading('cno', text='课程号')
            table.heading('cname', text='课程名')
            table.heading('grade', text='课程成绩')
            table.heading('ccredit', text='学分')
            table.place(width=800, height=300)

            loadSC()
            btn_quit = Button(info_window, text='退出', width=10, height=2, command=info_window.destroy)
            btn_quit.place(x=360, y=400)
            info_window.mainloop()

        var_sno = StringVar()
        entry_sno = Entry(select_window, textvariable=var_sno, font=('宋体', 14))
        entry_sno.place(x=310, y=50)
        btn_select_sno = Button(select_window, text='查询', command=selectSCBySno)
        btn_select_sno.place(x=530, y=45)

        var_cno = StringVar()
        entry_cno = Entry(select_window, textvariable=var_cno, font=('宋体', 14))
        entry_cno.place(x=310, y=125)
        btn_select_cno = Button(select_window, text='查询', command=selectSCByCno)
        btn_select_cno.place(x=530, y=120)

        var_sno1 = StringVar()
        entry_sno1 = Entry(select_window, textvariable=var_sno1, width=15, font=('宋体', 14))
        entry_sno1.place(x=360, y=200)
        var_cno1 = StringVar()
        entry_cno1 = Entry(select_window, textvariable=var_cno1, width=15, font=('宋体', 14))
        entry_cno1.place(x=540, y=200)
        btn_select_tno = Button(select_window, text='查询', command=selectSCBySnoAndCno)
        btn_select_tno.place(x=705, y=195)

        btn_select_all = Button(select_window, text='查询全部信息', command=selectAllSC)
        btn_quit = Button(select_window, text='退出', width=10, height=2, command=select_window.destroy)
        btn_select_all.place(x=10, y=250)
        btn_quit.place(x=340, y=250)

    def updateWindow(self):
        update_window = Tk(className='修改选项')
        update_window.geometry('600x250')
        Label(update_window, text='请输入要修改学生的学号', font=('宋体', 14)).place(x=10, y=50)
        Label(update_window, text='请输入要修改该学生哪门课程号', font=('宋体', 14)).place(x=10, y=100)
        Label(update_window, text='新课程成绩', font=('宋体', 14)).place(x=10, y=150)

        var_sno = StringVar()
        entry_sno = Entry(update_window, textvariable=var_sno, font=('宋体', 14))
        entry_sno.place(x=300, y=50)

        var_cno = StringVar()
        entry_cno = Entry(update_window, textvariable=var_cno, font=('宋体', 14))
        entry_cno.place(x=300, y=100)

        var_grade = IntVar()
        entry_grade = Entry(update_window, textvariable=var_grade, font=('宋体', 14))
        entry_grade.place(x=300, y=150)

        def updateSC():
            sno = entry_sno.get()
            cno = entry_cno.get()
            grade = entry_grade.get()
            if sno != '' and cno != '' and grade != '':
                r = scd.updSCGrade(SC(sno=sno, cno=cno, grade=grade))
                if r == "修改失败":
                    tkinter.messagebox.showerror(r, "课程名称修改失败")
                entry_sno.delete(0, END)
                entry_cno.delete(0, END)
                entry_grade.delete(0, END)
                tkinter.messagebox.showinfo("操作成功", "该学生课程信息修改成功")
            else:
                tkinter.messagebox.showerror("操作失败", "修改条目的学号和课程号都不能为空")

        btn_insert = Button(update_window, text='修改', command=updateSC)
        btn_quit = Button(update_window, text='退出', command=update_window.destroy)
        btn_insert.place(x=220, y=200)
        btn_quit.place(x=320, y=200)


student_table_op = StudentTableOperation()
course_table_op = CourseTableOperation()
sc_table_op = SCTableOperation()


def chooseStudentOp():
    choose_table_window.destroy()
    global choose_op_window
    choose_op_window = Tk()
    choose_op_window.title('操作选项')
    width = 72
    height = 1
    Button(choose_op_window, text='增加', width=width, height=height,
           command=student_table_op.insertWindow, bg='light yellow', font='楷体').grid(row=0, column=1, padx=10, pady=20)
    Button(choose_op_window, text='删除', width=width, height=height,
           command=student_table_op.deleteWindow, bg='light yellow', font='楷体').grid(row=10, column=1, padx=10, pady=20)
    Button(choose_op_window, text='查找', width=width, height=height,
           command=student_table_op.selectWindow, bg='light yellow', font='楷体').grid(row=20, column=1, padx=10, pady=20)
    Button(choose_op_window, text='修改', width=width, height=height,
           command=student_table_op.updateWindow, bg='light yellow', font='楷体').grid(row=30, column=1, padx=10, pady=20)
    Button(choose_op_window, text='返回', width=width, height=height,
           command=chooseTable, bg='light cyan', font='楷体').grid(row=40, column=1, padx=10, pady=20)
    # choose_op_window.geometry('750x400')


def chooseCourseOp():
    choose_table_window.destroy()
    global choose_op_window
    choose_op_window = Tk()
    choose_op_window.title('操作选项')
    width = 72
    height = 1
    Button(choose_op_window, text='增加', width=width, height=height,
           command=course_table_op.insertWindow, bg='light yellow', font='楷体').grid(row=0, column=1, padx=10, pady=20)
    Button(choose_op_window, text='删除', width=width, height=height,
           command=course_table_op.deleteWindow, bg='light yellow', font='楷体').grid(row=10, column=1, padx=10, pady=20)
    Button(choose_op_window, text='查找', width=width, height=height,
           command=course_table_op.selectWindow, bg='light yellow', font='楷体').grid(row=20, column=1, padx=10, pady=20)
    Button(choose_op_window, text='修改', width=width, height=height,
           command=course_table_op.updateWindow, bg='light yellow', font='楷体').grid(row=30, column=1, padx=10, pady=20)
    Button(choose_op_window, text='返回', width=width, height=height,
           command=chooseTable, bg='light cyan', font='楷体').grid(row=40, column=1, padx=10, pady=20)
    # choose_op_window.geometry('750x400')


def chooseSCOp():
    choose_table_window.destroy()
    global choose_op_window
    choose_op_window = Tk()
    choose_op_window.title('操作选项')
    width = 72
    height = 1
    Button(choose_op_window, text='增加', width=width, height=height,
           command=sc_table_op.insertWindow, bg='light yellow', font='楷体').grid(row=0, column=1, padx=10, pady=20)
    Button(choose_op_window, text='删除', width=width, height=height,
           command=sc_table_op.deleteWindow, bg='light yellow', font='楷体').grid(row=10, column=1, padx=10, pady=20)
    Button(choose_op_window, text='查找', width=width, height=height,
           command=sc_table_op.selectWindow, bg='light yellow', font='楷体').grid(row=20, column=1, padx=10, pady=20)
    Button(choose_op_window, text='修改', width=width, height=height,
           command=sc_table_op.updateWindow, bg='light yellow', font='楷体').grid(row=30, column=1, padx=10, pady=20)
    Button(choose_op_window, text='返回', width=width, height=height,
           command=chooseTable, bg='light cyan', font='楷体').grid(row=40, column=1, padx=10, pady=20)


def checkUser():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        ckd = checkDao(username=usr_name, password=usr_pwd)
        return True
    except Exception as e:
        tkinter.messagebox.showerror("登录失败", "请检查账号密码是否正确")
        return False


def chooseTable():
    user_flag = checkUser()
    if not user_flag:
        return
    global flag
    if flag == 1:
        logInWindow.destroy()
    flag += 1
    if 'choose_op_window' in globals():
        choose_op_window.destroy()
    global choose_table_window
    choose_table_window = Tk()
    choose_table_window.title("表选项")
    # choose_table_window.geometry('750x400')
    width = 72
    height = 1
    Button(choose_table_window, text='学生信息表', width=width, height=height,
           command=chooseStudentOp, bg='light yellow', font='楷体').grid(row=0, column=1, padx=10, pady=20)
    Button(choose_table_window, text='学生选课成绩表', width=width, height=height,
           command=chooseSCOp, bg='light yellow', font='楷体').grid(row=10, column=1, padx=10, pady=20)
    Button(choose_table_window, text='课程信息表', width=width, height=height,
           command=chooseCourseOp, bg='light yellow', font='楷体').grid(row=20, column=1, padx=10, pady=20)

global usr_name
global usr_pwd

flag = 1
logInWindow = Tk()
logInWindow.title('登录')
logInWindow.geometry('400x300')
Label(logInWindow, text='UserID', font=('Arial', 14)).place(x=10, y=150)
Label(logInWindow, text='Password', font=('Arial', 14)).place(x=10, y=190)

var_usr_name = StringVar()
entry_usr_name = Entry(logInWindow, textvariable=var_usr_name, font=('Arial', 14))
entry_usr_name.place(x=120, y=155)

var_usr_pwd = StringVar()
entry_usr_pwd = Entry(logInWindow, textvariable=var_usr_pwd, font=('Arial', 14), show='*')
entry_usr_pwd.place(x=120, y=195)

title = Label(logInWindow, text='学生学籍管理系统', bg='white', font=('Arial', 30), width=30, height=2)
title.pack()

btn_login = Button(logInWindow, text='Login', command=chooseTable)
btn_login.place(x=185, y=250)

logInWindow.mainloop()

