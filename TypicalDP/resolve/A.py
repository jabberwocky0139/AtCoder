f = open("input/inputA.txt") ## debug
N = int(f.readline()) ## debug
arr_input = [int(i) for i in f.readline().split()] ## debug

# N = int(input())
# arr_input = [int(i) for i in input().split()]

ans = set([0])

### その1
def rec_search(n, l, arr_input):
    # 終了条件
    if l == len(arr_input):
        ans.add(n)
    # 継続条件
    else:
        rec_search(n + arr_input[l], l+1, arr_input)
        rec_search(n, l+1, arr_input)

rec_search(0, 0, arr_input)
print(len(ans))

### その2
# for i in arr_input:
#     #tmp = []
#     for ele in ans:
#         tmp.append(ele + i)
#     for ele in tmp:
#         ans.add(ele)

# print(ans)
