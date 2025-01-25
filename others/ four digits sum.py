"""
Consider all codes made of four digits (0−9). How many of them have a sum of digits equal to S? For example, for S = 4, there are 35 such codes in total. Some of them are 0022, 1003, 1111, 2020, 4000.

Write a function:

int solution(int S);

that, given an integer S, returns the number of four-digit codes whose sum of digits is equal to S.

Examples:

For S = 35, the possible codes are: 9998, 9989, 9899, 8999. The function should return 4.
For S = 4, the function should return 35.
For S = 2, the function should return 10.
Assume that:

S is an integer within the range [0..36].
"""


def solution(S):
    S = min(S, 36 - S)

    a = [[0, 0, 0, 0]]

    for _ in range(S):
        b = []
        for l in a:
            for i in range(4):
                if l[i] < 9:
                    new_l = l.copy()
                    new_l[i] += 1
                    if new_l not in b:
                        b.append(new_l)
        a = b

    return len(a)


def solution2(S):
    S = min(S, 36 - S)

    dp = [1] + [0] * S

    for _ in range(4):
        new_dp = [0] * (S + 1)
        for s in range(S + 1):
            for digit in range(10):
                if s + digit <= S:
                    new_dp[s + digit] += dp[s]
        dp = new_dp

    return dp[S]


import time

start = time.time()
S = 19
res = solution2(S)
print(res)
end = time.time()
print(end - start)
