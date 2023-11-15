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