#Create a program that manages a list of student names, allowing the user to add, remove, and display the list.

class check():
    def __init__(self):
        self.n=[]
    def add(self, a):
        return self.n.append(a)
    def remove(self, b):
        return self.n.remove(b)
    def display(self):
        return self.n

obj= check()

option = 1

while option != 0:
    print("0 : Exit \n 1 : Add \n 2 : Remove \n 3 : Display")
    option= int(input("Enter The Options Given Below:"))
    if option == 1:
        n = input("Enter Name To Append:")
        obj.add(n)
        print("List: ", obj.display())
    elif option == 2:
        n = input("Enter String to remove: ")
        obj.remove(n)
        print("List: ", obj.display())

    elif option == 3:
        print("List: ", obj.display())
    elif option == 0:
        print("Exiting!")
    else:
        print("Invalid choice!!")

print()