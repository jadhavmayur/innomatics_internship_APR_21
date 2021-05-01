if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    student_score=student_marks[query_name]
    percentage=(sum(student_score)/len(student_score))
    print('{0:.2f}'.format(percentage))
        