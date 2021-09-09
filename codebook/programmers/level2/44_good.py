from itertools import combinations
import collections

def solution(orders, course):

    result = []

    for course_size in course:
            order_combinations = []
            for order in orders:
                order_combinations += combinations(sorted(order), course_size)
    
    most_ordered = collections.Counter(order_combinations).most_common()
    print(most_ordered)
    result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

print(solution(orders, course))
