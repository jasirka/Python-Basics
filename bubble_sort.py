num = [5, 2, 9, 1, 4]

def bubble_sort(num):
    n=len(num)
    for i in range(n):
        for j in range(0, n-i-1):
            if num[j] > num[j+1]:
                num[j],num[j+1] = num[j+1],num[j]
    return num

print(bubble_sort(num))