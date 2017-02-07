# You have a record of  students. Each record contains the student's name, and their percent marks
# in Maths, Physics and Chemistry. Output the average percentage marks obtained by the student whose name is given
# by the user, correct to two decimal places.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}                      # Empty Dictionary: Key Value Pairs

    for _ in range(n):
        name, *line = input().split()       # Advance Unpacking
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    avg = sum(student_marks[query_name]) / float(len(student_marks[query_name]))

    print("{0:.2f}".format(avg))                      # Print up to decimal places
