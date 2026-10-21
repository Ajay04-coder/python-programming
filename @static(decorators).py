# class Student():
#     def ajay(self):
#         print("ajay")
# s1=Student()
# s1.ajay()
'''in above programme ajay method takes self argument which is mandatory for all functions which 
we write in class but using static method removes this compulsion an example code is given below'''
class Student():
    @staticmethod
    def ajay ():
        print("hello")
s1=Student()
s1.ajay()