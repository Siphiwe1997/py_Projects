class Student:
    def __init__(self: object, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def print_details(self):
        return 'Hello, I\'m ' + self.firstname + ' ' + self.lastname


class Modules(Student):
    def __init__(self: object, fname, lname, mname):
        super().__init__(fname, lname)
        self.moduleName = mname

    def print_details(self):
        return Student.print_details(self) + '\nI\'m doing ' + self.moduleName + ' this semester'


class ModuleMark(Modules):
    def __init__(self: object, fname, lname, mname, mmark):
        super().__init__(fname, lname, mname)
        self.ModuleMark = mmark

    def print_details(self):
        return Modules.print_details(self) + '\nI got ' + str(self.ModuleMark) + ' %'

    def pass_description(self):
        if 74 < self.ModuleMark < 101:
            print('Passed with distinction')
        elif 49 < self.ModuleMark < 75:
            print('Passed')
        elif 44 < self.ModuleMark < 50:
            print('Qualify for supplement')
        elif 0 <= self.ModuleMark < 45:
            print('Failed')
        else:
            print('Please enter marks between 0 and 100')
