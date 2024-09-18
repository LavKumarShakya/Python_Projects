# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     q = [x, y, z]
#     p = []
#     for i in range(0,x+1):
#         for j in range(0,y+1):
#             for k in range(0,z+1):
#                 p.append([i,j,k])
#     for i in p:
#         c = 0
#         for j in i:
#             c= c+j
#         if c == n:
#             p.remove(i)
#     print(p)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    s = list(arr)
    sarr = sorted(set(s),reverse = True)
    print(sarr[2])
    print(arr)