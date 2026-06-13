class student:
    grade = 9
    name = "penguin"

    def introduction(self):
        print("Hi, I am a student")

    def details (self):
            print("My name is", self.name)
            print("I study in Grade", self.grade)

obj = student()
obj.introduction()
obj.details()