class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def plot(self):
        message = f"-- My name is {self.first_name} {self.last_name}"
        print(message)
        return


class Student(Person):
    def __init__(self, first_name, last_name, student_id):
        super().__init__(first_name, last_name)
        self.student_id = student_id
    
    def plot(self):
        super().plot()
        message = f"and my student number is {self.student_id}"
        print(message)
        return

p1 = Person("James", "Bond")
s1 = Student("Johnny", "English", 321)
p1.plot()
s1.plot()
