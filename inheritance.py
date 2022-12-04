#single inheritance
#multiple inheritance
#multilevel ingeritance

# class Parent:
#     def __init__(self) -> None:
#         self.string1 = "I am a parent"

    
# class Child(Parent):
#     def __init__(self) -> None:
#         self.string2 = "I am achild"
#         super().__init__()

# c = Child()
# print(c.string2)

#multiple inheritance

# class GrandParent:
#     def __init__(self) -> None:
#         self.string = "I am a grand parent"

# class Parent():
#     def __init__(self) -> None:
#         self.string = "I am a parent"

    
# class Child(Parent,GrandParent):
#     def __init__(self) -> None:
        
#         # super().__init__()
#         # super().__init__()
#         Parent.__init__(self)
#         self.string = "I am achild"
#         GrandParent.__init__(self)

# c = Child()
# print(c.string)

#multilevel ingeritance

class GrandParent:
    def __init__(self) -> None:
        self.string = "I am a grand parent"

class Parent(GrandParent):
    def __init__(self) -> None:
        self.string = "I am a parent"
        super().__init__()

    
class Child(Parent):
    def __init__(self) -> None:
        
        # super().__init__()
        # super().__init__()
        Parent.__init__(self)
        # self.string = "I am achild"
        
c = Child()
print(c.string)