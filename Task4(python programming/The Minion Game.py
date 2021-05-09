def minion_game(string):
    # your code goes here
    con_sum=0
    vow_sum=0
    vowels="AEIOU"
    
    for i in range(len(string)):
        if string[i] not in vowels:
            con_sum=con_sum+(len(string)-i)
        else:
            vow_sum=vow_sum+(len(string)-i)
    if con_sum >vow_sum:
        print("Stuart",con_sum)
    elif vow_sum >con_sum:
        print("Kevin",vow_sum)
    else:
        print("Draw")
            
if __name__ == '__main__':
    s = input()
    minion_game(s)