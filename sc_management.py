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
        def list_students(self):
            print("-" * 60)
            print("学生列表：")
            for student_id,info in self.students.items():  # noqa: PLR1704
                avg_score = self.get_student_average(student_id)
                print(f"学号：{student_id}，姓名：{info['name']}，年龄：{info['age']}，考试成绩：{info['score']}，平均分：{avg_score:.1f}")
            print("-" * 60)
        def surche_student(self, keyword):
            results = []
            for student_id, info in self.students.items():  # noqa: PLR1704
                if (keyword.lower() in info["name"].lower() or 
                keyword in student_id):
                    results.append((student_id, info))

                if results:
                  print(f"\n找到 {len(results)} 个匹配结果:")
            for student_id, info in results:
                print(f"学号: {student_id}, 姓名: {info['name']}")
            else:  # noqa: PLW0120
                print("未找到匹配的学生")
# 测试学生管理系统
if __name__ == "__main__":
    sm = StudentManager()
    
    try:
        # 添加学生
        sm.add_student("2023001", "张三", 20)
        sm.add_student("2023002", "李四", 21)
        sm.add_student("2023003", "王五", 19)
        
        # 添加成绩
        sm.add_score("2023001", 85)
        sm.add_score("2023001", 92)
        sm.add_score("2023002", 78)
        sm.add_score("2023002", 88)
        
        # 列出所有学生
        sm.list_students()
        
        # 搜索学生
        sm.search_student("张")
        
    except ValueError as e:
        print(f"错误: {e}")