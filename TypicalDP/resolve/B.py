
### 入力
# f = open("input/inputB.txt", "r")
# A, B = [int(n) for n in f.readline().split()]
# arr_A = [int(n) for n in f.readline().split()]
# arr_B = [int(n) for n in f.readline().split()]

A, B = [int(n) for n in input().split()]
arr_A = [int(n) for n in input().split()]
arr_B = [int(n) for n in input().split()]

### その1
# 先手(a, すぬけ)の得点をreturnする
# arr_Aの先頭がi, arr_Bの先頭がj
# i+jの偶奇で先手後手を判断
# def rec_game(i, j):
#     # 終了条件
#     if i == len(arr_A) and j == len(arr_B):
#         return 0
#     # Aの山がなくなる
#     elif i == len(arr_A):
#         # 先手
#         if (i + j) % 2 == 0:
#             return rec_game(i, j+1) + arr_B[j]
#         # 後手
#         else:
#             return rec_game(i, j+1)
#     # Bの山がなくなる
#     elif j == len(arr_B):
#         # 先手
#         if (i + j) % 2 == 0:
#             return rec_game(i + 1, j) + arr_A[i]
#         # 後手
#         else:
#             return rec_game(i + 1, j)
#     # どちらの山も残ってる
#     else:
#         # 先手(戻り値が大きくなるものを選択しなければならない)
#         if (i + j) % 2 == 0:
#             return max(rec_game(i + 1, j) + arr_A[i], rec_game(i, j + 1) + arr_B[j])
#         # 後手(次の先手の得点が小さくなるものを選択)
#         else:
#             return min(rec_game(i + 1, j), rec_game(i, j + 1))

    
# print(rec_game(0, 0))


### その2
# 先手(a, すぬけ)の得点をreturnする
# arr_Aの先頭がi, arr_Bの先頭がj
# i+jの偶奇で先手後手を判断

# dp = [[None]*(B+1) for _ in range(A+1)]

# def rec_game(i, j):
#     # 終了条件
#     if dp[i][j] is not None:
#         return dp[i][j]
#     elif i == A and j == B:
#         return 0
#     # Aの山がなくなる
#     elif i == A:
#         # 先手
#         if (i + j) % 2 == 0:
#             dp[i][j] = rec_game(i, j+1) + arr_B[j]
#             return dp[i][j]
#         # 後手
#         else:
#             dp[i][j] = rec_game(i, j+1)
#             return dp[i][j]
#     # Bの山がなくなる
#     elif j == B:
#         # 先手
#         if (i + j) % 2 == 0:
#             dp[i][j] = rec_game(i + 1, j) + arr_A[i]
#             return dp[i][j]
#         # 後手
#         else:
#             dp[i][j] = rec_game(i + 1, j)
#             return dp[i][j]
#     # どちらの山も残ってる
#     else:
#         # 先手(戻り値が大きくなるものを選択しなければならない)
#         if (i + j) % 2 == 0:
#             dp[i][j] = max(rec_game(i + 1, j) + arr_A[i], rec_game(i, j + 1) + arr_B[j])
#             return dp[i][j]
#         # 後手(次の先手の得点が小さくなるものを選択)
#         else:
#             dp[i][j] = min(rec_game(i + 1, j), rec_game(i, j + 1))
#             return dp[i][j]
            

# print(rec_game(0, 0))

### その3
# 先手(a, すぬけ)の得点をreturnする
# arr_Aの先頭がi, arr_Bの先頭がj
# i+jの偶奇で先手後手を判断

dp = [[None]*(B+1) for _ in range(A+1)]

def rec_game():
    for i in range(A, -1, -1):
        for j in range(B, -1, -1):
            # 終了条件
            if i == A and j == B:
                dp[i][j] = 0
            # Aの山がなくなる
            elif i == A:
                # 先手
                if (i + j) % 2 == 0:
                    dp[i][j] = dp[i][j+1] + arr_B[j]
                # 後手
                else:
                    dp[i][j] = dp[i][j+1]
                    
            # Bの山がなくなる
            elif j == B:
                # 先手
                if (i + j) % 2 == 0:
                    dp[i][j] = dp[i+1][j] + arr_A[i]
                # 後手
                else:
                    dp[i][j] = dp[i+1][j]
            # どちらも残ってる
            else:
                # 先手
                if (i + j) % 2 == 0:
                    dp[i][j] = max(dp[i+1][j] + arr_A[i], dp[i][j+1] + arr_B[j])
                # 後手
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1])

rec_game()
print(dp[0][0])
