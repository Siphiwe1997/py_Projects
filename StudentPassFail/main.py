import Students

stud = Students.Modules('Thembe','Ngubane','Data structures')
stud.print_details()

print('\n')
studMark = Students.ModuleMark('Siphiwe', 'Ngubane','Programming in Python', 76)
print(studMark.print_details())

print('\n')
studMark.pass_description()