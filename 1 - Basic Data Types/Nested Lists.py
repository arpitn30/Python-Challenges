# Print the name(s) of any student(s) having the second lowest grade in Physics;
# If there are multiple students, order their names alphabetically and print each one on a new line.

from operator import itemgetter

if __name__ == '__main__':
    students = []
    mini = 999
    for i in range(int(input())):
        name = input()
        score = float(input())
        if(mini > score):
            mini = score
        students.append([name, score])
    # max(students, itemgetter(1)) returns a list instead of float

    mini2 = 999
    for student in students:
        if mini < student[1] < mini2:
            mini2 = student[1]

    students.sort(key=itemgetter(0))    # Gets the first item in the list
    for student in students:
        if student[1] == mini2:
            print(student[0], end="\n")
