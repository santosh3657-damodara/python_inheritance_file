class Parent:
    def __init__(self):
        print('parent method')
        
    def m1(self):
        print('m1 method executed')
        
    def m2(self):
        print('m2 method executed')
        
class Child(Parent):
     def m3(self):
         print('child class method')
         
     def m4(self):
         print('child of secound class')
         
s=Child()
s.m1()
s.m2()
s.m3()
s.m4()
