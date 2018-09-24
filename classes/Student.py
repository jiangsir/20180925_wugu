class Student(object):
    #-------------------    
    # 建構元
    #-------------------
    def __init__(self, stuNo, stuName, deptNo):
        self.stuNo=stuNo
        self.stuName=stuName
        self.deptNo=deptNo

    #-------------------    
    # 取出系名的方法
    #-------------------        
    def dept(self):
        if self.deptNo=='6':
            return '資管系'
        else:
            return '其他系'

    #-------------------    
    # 取出學制的方法
    #-------------------            
    def division(self):
        if self.stuNo[0]=='N':
            return '進修推廣部'
        else:
            return '日間部'
