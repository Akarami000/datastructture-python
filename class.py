# class myclass:
#     x=5

# p1=myclass()

# print(p1.x)

###############class with function#############

# class myclass:
#     def __init__(sel,name,age):
#         sel.name=name
#         sel.age=age


# p1 = myclass("akshay",21)

# print(p1.name)
# print(p1.age)

# class myclass:
#     def __init__(sel,name,age):
#         sel.name=name
#         sel.age=age

#     def my(a):
#      print("i am "+a.name)

# p1 = myclass("akshay",21)
# p1.my()




###################################################inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
# class myclass():
#     def __init__(sel,name,age):
#         sel.name=name
#         sel.age=age

#     def printname(sel):
#         print(sel.name,sel.age)

# class stu(myclass):
#     def __init__(sel,name,age):
#         myclass.__init__(sel,name,age)

# x=stu("akshay",21)
# x.printname()                
###############################################################################



##################using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.



# class myclass:
#     def __init__(sel,name,age):
#         sel.name=name
#         sel.age=age

#     def check(sel):
#         print(sel.name,sel.age) 

# class next(myclass):
#      def __init__(sel,name,age):
#          super().__init__(name,age)
#          sel.graduation=2019

# x=next("akshay",21)
# print(x.graduation)
# x.check()

###############################
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from #####iter()



# a=["akshay","jack","ranger","king"]

# nex=iter(a)

# print(next(nex))
# print(next(nex))

#################################### using StopIteration ###### using iter ####### using next

# class it:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#       if self.a<20:  
#         x=self.a
#         self.a+=1
#         return x

#       else:
#           raise StopIteration  

# c=it()
# myiter=iter(c)

# for x in myiter :
#     print(x)

#####################################################
#################### using global


# def glob():
#     global x
#     x=300

# glob()
# print(x)

# modules

