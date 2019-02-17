#!/usr/bin/env python3

class Person:
    # constructor
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
    
    # functions
    def walk():
        pass    

    # functions
    def write():
        pass

    # api
    def talk(self, diff_person, string):
        diff_person.say(string)

    # functions
    def say(self, string):
        print(self.name, " say ", string)


def main():
    a = Person("trang", 19)
    b = Person("thao", 19)

    a.talk(b, "hello") 


if __name__ == '__main__':
    main()
    


