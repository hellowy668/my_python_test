'''
定义一个学生类，用来形容学生
'''
# 定义一个空的类
class Student():

    pass

# 定义一个对象
mingyue = Student()

# 定义一个用来描述python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    def doHonmework(self):
        print("我在做作业")

        #推荐在函数末尾使用return语句
        return None
# 实例化一个叫yueyue的学生，是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
# yueyue.doHonmework()