if __name__ == '__main__':
    name_grade=[]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_grade.append([name,score])
    sort_list=sorted(list(set([x[1] for x in name_grade])))
    get_second_lowest=sort_list[1]
    
   
        
    second_low=[]
    for student in name_grade:
        if get_second_lowest==student[1]:
            second_low.append(student[0])
            
    for student in sorted(second_low):
        print(student) 
    