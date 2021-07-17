def solution(str1, str2):

    str1, str2 = str1.upper(), str2.upper()

    set1, set2, inter, union = {}, {}, 0, 0
    for i in range(len(str1)-1):
        if str1[i].isalpha() == True and str1[i+1].isalpha() == True:            
            key = str1[i]+str1[i+1]
            if key in set1: set1[key] += 1
            else : set1[key] = 1

    for i in range(len(str2)-1):
        if str2[i].isalpha() == True and str2[i+1].isalpha() == True:            
            key = str2[i]+str2[i+1]
            if key in set2: set2[key] += 1
            else : set2[key] = 1

    for key in set1:
        if key in set2:
            inter += min(set1[key], set2[key])  
            union += max(set1[key], set2[key])
            set2[key] = 0
        else : 
            union += set1[key]

    for key in set2:
        if set2[key] != 0:
            union += set2[key]

    if union == 0 : return 65536
    return int((inter/union)*65536)


str1 = "FRANCE"
str2 = "french"
print(solution(str1,str2))