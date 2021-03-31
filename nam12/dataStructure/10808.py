import sys

string = sys.stdin.readline().rstrip()

stack = [0 for _ in range(26)]
for i in range(len(string)):
    stack[ord(string[i])-97] += 1


for i in range(26):
    print(stack[i], end=" ")

# print* 활요해보기.
# unpacking이 된다. 