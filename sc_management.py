class StudentManager:
    """定义学生类"""
    def __init__(self):
        self.students={}

    def add_student(self,student_id,name,age,score=None):
        if student_id in self.students:
            raise ValueError(f"学生{student_id}已存在")
        if not isinstance(age,int) or age<0 or age>150:
            raise ValueError(age,f"年龄{age},不在合法范围内(1~150)")
        self.students[student_id]={
            "name" : name,
            "age" : age,
            "score": score or []
        }
        print(f"√ 添加学生{name}c成功")

        def remove_student(self, student_id):
            if student_id not in self.students:
                raise ValueError(f"学生{student_id}不存在")
            name = self.students[student_id]["name"]
            del self.students[student_id]
            print(f"√ 删除学生{name}成功")
        def update_student(self, student_id, **kwargs):
            if student_id not in self.students:
                raise ValueError(f"学生{student_id}不存在")
            name = self.students[student_id]["name"]
            for key,value in kwargs.items():
                if key in ["name","age","score"]:
                    self.students[student_id][key]=value
            print(f"√ 更新学生{name}成功")
        def add_score(self, student_id, score):
            if student_id not in self.students:
                raise ValueError(f"学生{student_id}不存在")
            if not isinstance(score,{int,float}) or score<0 or score>100:
                raise ValueError(f"成绩{score}不在合法范围内(0~100)")
            self.students[student_id]["score"].append(score)
            print(f"√ 添加学生{name}的考试成绩{score}成功")

        def get_student_average(self, student_id):
            if student_id not in self.students:
                raise ValueError(f"学生{student_id}不存在")
            score = self.students[student_id]["score"]
            if not score:
                return 0
            return sum(score)/len(score)