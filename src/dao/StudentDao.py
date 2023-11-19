from util.DbUtil import DbUtil
from po.student import Student

class StudentDao:
    su: DbUtil

    def __init__(self):
        self.su = DbUtil()

    def addStudent(self, s: Student):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)',
                            (s.sno, s.sname, s.ssex, s.sclass, s.smajor, s.sdept, s.sbir, s.stele))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def delStudent(self, s: Student):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('delete from student where sno = %s', (s.sno))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def selStudentBySno(self, s: Student):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('select * from student where sno = %s', (s.sno))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def selStudentBySname(self, s: Student):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('select * from student where sname = %s', (s.sname))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def updStudent(self, s: Student):   # TODO：单独更新某一行的某一属性
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('update student set sname = %s where sno = %s', (s.sname, s.sno))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def list_book(self, page: int = 1, rows: int = 10):
        try:
            assert isinstance(self.su, DbUtil)
            start = (page - 1) * rows + 1
            return self.su.executeList('select * from student limit %d,%d'
                                        % (start, rows))
        except Exception as e:
            print(e)
            return '操作失败'