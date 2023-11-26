class Student:
    sno: str
    sname: str
    ssex: str
    sclass: str
    smajor: str
    sdept: str
    sbir: str
    stele: str

    def __init__(self, sno: str = None, sname: str = None, ssex: str = None, sclass: str = None, smajor: str = None,
                 sdept: str = None, sbir: str = None, stele: str = None):
        self.sno = sno
        self.sname = sname
        self.ssex = ssex
        self.sclass = sclass
        self.smajor = smajor
        self.sdept = sdept
        self.sbir = sbir
        self.stele = stele

    def __str__(self):
        return f"{self.sno},{self.sname},{self.ssex},{self.sclass},{self.smajor},{self.sdept},{self.sbir},{self.stele}"

class Course:
    cno: str
    cname: str
    tno: str
    ccredit: int

    def __init__(self, cno: str = None, cname: str = None, tno: str = None, ccredit: int = None):
        self.cno = cno
        self.cname = cname
        self.tno = tno
        self.ccredit = ccredit

    def __str__(self):
        return f"{self.cno},{self.cname},{self.tno},{self.ccredit}"

class SC:
    sno: str
    cno: str
    grade: int
    ccredit: int

    def __init__(self, sno: str = None, cno: str = None, grade: int = None, ccredit: int = None):
        self.sno = sno
        self.cno = cno
        self.grade = grade
        self.ccredit = ccredit

    def __str__(self):
        return f"{self.sno},{self.cno},{self.grade},{self.ccredit}"
