names = [] # get and process input for a list of names
assignments = [] # get and process input for a list of the number of assignments
grades = [] # get and process input for a list of grades

## message string to be used for each student
## HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. Your current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

## write a for loop that iterates through each set of names, assignments, and grades to print each student's message
names = list(input("Enter names separated by commas: ").title().split(","))
assignments = list(input("Enter assignments separated by commas: ").title().split(","))
grades = list(input("Enter grades separated by commas: ").title().split(","))

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
    
    