from collections import defaultdict

def solution(clothes):
    answer = 1

    clothes_dict = defaultdict(list)
    print(clothes_dict)
    for sample, category in clothes:
        clothes_dict[category].append(sample)
    
    for i in clothes_dict.keys():
        print(i)
        answer *= len(clothes_dict[i]) + 1

    # Remove the case of All None elements
    answer -= 1
    return answer

clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))
