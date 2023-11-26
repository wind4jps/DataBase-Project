from util.DbUtil import DbUtil
from po.student import *

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

    def delStudentBySno(self, s: Student):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('delete from student where sno = %s', (s.sno))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def delStudentBySclass(self, s: Student):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('delete from student where sclass = %s', (s.sclass))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def deleStudentBySmajor(self, s: Student):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('delete from student where smajor = %s', (s.smajor))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def deleStudentBySdept(self, s: Student):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('delete from student where sdept = %s', (s.sdept))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def deleStudentAll(self):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('delete from student')
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def updStudentName(self, s: Student):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('update student set sname = "%s" where sno = %s', (s.sname, s.sno))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def updStudentClass(self, s: Student):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('update student set sclass = %s where sno = %s', (s.sclass, s.sno))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def updStudentSex(self, s: Student):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('update student set ssex = %s where sno = %s', (s.ssex, s.sno))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def updStudentMajor(self, s: Student):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('update student set smajor = "%s" where sno = %s', (s.smajor, s.sno))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def updStudentDept(self, s: Student):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('update student set sdept = "%s" where sno = %s', (s.sdept, s.sno))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def updStudentBir(self, s: Student):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('update student set sbir = %s where sno = %s', (s.sbir, s.sno))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def updStudentTele(self, s: Student):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('update student set stele = %s where sno = %s', (s.stele, s.sno))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def list_student_by_sno(self, s: Student, page: int = 1, rows: int = 10):
        try:
            assert isinstance(self.su, DbUtil)
            start = (page - 1) * rows + 1
            return self.su.executeList('select * from student where sno = %s limit %d,%d'
                                        % (s.sno, 0, rows))
        except Exception as e:
            print(e)
            return '操作失败'

    def list_student_by_sclass(self, s: Student, page: int = 1, rows: int = 10):
        try:
            assert isinstance(self.su, DbUtil)
            start = (page - 1) * rows + 1
            return self.su.executeList('select * from student where sclass = %s limit %d,%d'
                                       % (s.sclass, 0, rows))
        except Exception as e:
            print(e)
            return '操作失败'

    def list_student_by_smajor(self, s: Student, page: int = 1, rows: int = 10):
        try:
            assert isinstance(self.su, DbUtil)
            start = (page - 1) * rows + 1
            return self.su.executeList('select * from student where smajor = "%s" limit %d,%d'
                                        % (s.smajor, 0, rows))
        except Exception as e:
            print(e)
            return '操作失败'

    def list_student_by_sdept(self, s: Student, page: int = 1, rows: int = 10):
        try:
            assert isinstance(self.su, DbUtil)
            start = (page - 1) * rows + 1
            return self.su.executeList('select * from student where sdept = "%s" limit %d,%d'
                                        % (s.sdept, 0, rows))
        except Exception as e:
            print(e)
            return '操作失败'

    def list_student(self, page: int = 1, rows: int = 10):
        try:
            assert isinstance(self.su, DbUtil)
            start = (page - 1) * rows + 1
            return self.su.executeList('select * from student limit %d,%d'
                                        % (0, rows))
        except Exception as e:
            print(e)
            return '操作失败'


class CourseDao:
    su: DbUtil

    def __init__(self):
        self.su = DbUtil()

    def addCourse(self, c: Course):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('insert into course values(%s,%s,%s,%s)',
                            (c.cno, c.cname, c.tno, c.ccredit))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def delCourseByCno(self, c: Course):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('delete from course where cno = %s', (c.cno))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def delCourseByCname(self, c: Course):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('delete from course where cname = %s', (c.cname))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def delCourseByTno(self, c: Course):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('delete from course where tno = %s', (c.tno))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def delCourseAll(self):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('delete from course')
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def updCourseName(self, c: Course):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('update course set cname = %s where cno = %s', (c.cname, c.cno))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def updCourseTno(self, c: Course):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('update course set tno = %s where cno = %s', (c.tno, c.cno))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def updCourseCreit(self, c: Course):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('update course set ccredit = %s where cno = %s', (c.ccredit, c.cno))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"


    def list_course_by_cno(self, c: Course, page: int = 1, rows: int = 10):
        try:
            assert isinstance(self.su, DbUtil)
            start = (page - 1) * rows + 1
            return self.su.executeList('select * from course where cno = %s limit %d,%d'
                                        % (c.cno, 0, rows))
        except Exception as e:
            print(e)
            return '操作失败'

    def list_course_by_cname(self, c: Course, page: int = 1, rows: int = 10):
        try:
            assert isinstance(self.su, DbUtil)
            start = (page - 1) * rows + 1
            return self.su.executeList('select * from course where cname = "%s" limit %d,%d'
                                        % (c.cname, 0, rows))
        except Exception as e:
            print(e)
            return '操作失败'

    def list_course_by_tno(self, c: Course, page: int = 1, rows: int = 10):
        try:
            assert isinstance(self.su, DbUtil)
            start = (page - 1) * rows + 1
            return self.su.executeList('select * from course where tno = %s limit %d,%d'
                                        % (c.tno, 0, rows))
        except Exception as e:
            print(e)
            return '操作失败'

    def list_course_by_ccredit(self, c: Course, page: int = 1, rows: int = 10):
        try:
            assert isinstance(self.su, DbUtil)
            start = (page - 1) * rows + 1
            return self.su.executeList('select * from course where ccredit = %s limit %d,%d'
                                        % (c.ccredit, 0, rows))
        except Exception as e:
            print(e)
            return '操作失败'

    def list_course(self, page: int = 1, rows: int = 10):
        try:
            assert isinstance(self.su, DbUtil)
            start = (page - 1) * rows + 1
            return self.su.executeList('select * from course limit %d,%d'
                                        % (0, rows))
        except Exception as e:
            print(e)
            return '操作失败'

class SCDao:
    su: DbUtil

    def __init__(self):
        self.su = DbUtil()

    def addSC(self, sc: SC):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('insert into sc values(%s,%s,%s,%s)',
                            (sc.sno, sc.cno, sc.grade, sc.ccredit))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def delSCBySno(self, sc: SC):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('delete from sc where cno = %s ', (sc.cno))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def delSCByCno(self, sc: SC):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('delete from sc where cno = %s', (sc.cno))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def delSCBySnoAndCno(self, sc: SC):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('delete from sc where sno = %s and cno = %cno', (sc.sno, sc.cno))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def delSCAll(self):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('delete from sc')
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def updCourseName(self, c: Course):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('update course set cname = %s where cno = %s', (c.cname, c.cno))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def updCourseTno(self, c: Course):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('update course set tno = %s where cno = %s', (c.tno, c.cno))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"

    def updCourseCreit(self, c: Course):
        try:
            assert isinstance(self.su, DbUtil)
            self.su.execute('update course set ccredit = %s where cno = %s', (c.ccredit, c.cno))
            return "操作成功"
        except Exception as e:
            print(e)
            return "操作失败"


    def list_course_by_cno(self, c: Course, page: int = 1, rows: int = 10):
        try:
            assert isinstance(self.su, DbUtil)
            start = (page - 1) * rows + 1
            return self.su.executeList('select * from course where cno = %s limit %d,%d'
                                        % (c.cno, 0, rows))
        except Exception as e:
            print(e)
            return '操作失败'

    def list_course_by_cname(self, c: Course, page: int = 1, rows: int = 10):
        try:
            assert isinstance(self.su, DbUtil)
            start = (page - 1) * rows + 1
            return self.su.executeList('select * from course where cname = "%s" limit %d,%d'
                                        % (c.cname, 0, rows))
        except Exception as e:
            print(e)
            return '操作失败'

    def list_course_by_tno(self, c: Course, page: int = 1, rows: int = 10):
        try:
            assert isinstance(self.su, DbUtil)
            start = (page - 1) * rows + 1
            return self.su.executeList('select * from course where tno = %s limit %d,%d'
                                        % (c.tno, 0, rows))
        except Exception as e:
            print(e)
            return '操作失败'

    def list_course_by_ccredit(self, c: Course, page: int = 1, rows: int = 10):
        try:
            assert isinstance(self.su, DbUtil)
            start = (page - 1) * rows + 1
            return self.su.executeList('select * from course where ccredit = %s limit %d,%d'
                                        % (c.ccredit, 0, rows))
        except Exception as e:
            print(e)
            return '操作失败'

    def list_course(self, page: int = 1, rows: int = 10):
        try:
            assert isinstance(self.su, DbUtil)
            start = (page - 1) * rows + 1
            return self.su.executeList('select * from course limit %d,%d'
                                        % (0, rows))
        except Exception as e:
            print(e)
            return '操作失败'
