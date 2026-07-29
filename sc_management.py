class StudentManager:
    """定义学生类"""
    def __init__(self):
        self.students={}

    def add_student(self,student_id,name,age,score=None):
        if student_id in self.students:
            raise ValueError(f"学生{student_id}已存在")
        if not isinstance(age,int) or age<0 or age>150:
            raise ValueError(age,f"年龄{age},不在合法范围内(1~150)")
        self.student[student_id]={
            “name" : name,
            "age" : age,
            "score" : score or []
        }