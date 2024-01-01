#LOOPS 
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
for i in range(0,4):
    n = int(input())
arr = map(int, input().split())
arr = list(arr)
for i in arr:
    for j in arr:
        if(i>j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp  
print(arr)