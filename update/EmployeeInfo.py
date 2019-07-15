# Copyright (c) 2016, 2018, Oracle and/or its affiliates.  All rights reserved.
import sys

class EmployeeInfo:
    def __init__(self, body):
        print("Building employee...", file=sys.stderr)
        try:
            self.empno = body["empno"]
            self.ename = body["ename"]
            self.job = body["job"]
            self.mgr = body["mgr"]
            self.hiredate = body["hiredate"]
            self.sal = body["sal"]
            self.comm = body["comm"]
            self.deptno = body["deptno"]
        except KeyError as e:
            raise Exception("key:" + str(e) + " does not have a value. Input a JSON object with the fields: empno, ename, job, mgr, hiredate, sal, comm, deptno")

    def getEmpno(self):
        return self.empno

    def setEmpno(self, num):
        self.empno = num

    def getEname(self):
        return self.ename

    def setEname(self, name):
        self.ename = name

    def getJob(self):
        return self.job

    def setJob(self, job):
        self.job = job

    def getMgr(self):
        return self.mgr

    def setMgr(self, mgr):
        self.mgr = mgr

    def getHiredate(self):
        return self.hiredate

    def setHiredate(self, hiredate):
        self.hiredate = hiredate

    def getSal(self):
        return self.sal

    def setSal(self, sal):
        self.sal = sal

    def getComm(self):
        return self.comm

    def setComm(self, comm):
        self.comm = comm

    def getDeptno(self):
        return self.deptno

    def setDeptno(self, deptno):
        self.deptno = deptno

    def __str__(self):
        return "EmployeeInfo{" + "empno=" + self.empno + ", ename=" + self.ename + ", job=" + self.job + ", mgr=" + self.mgr + ", hiredate=" + self.hiredate + ", sal=" + self.sal + ", comm=" + self.comm + ", deptno=" + self.deptno + '}'
