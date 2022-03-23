from typing import List

A: List[int] = [-3, 3, 8, 7, 9]
B: List[int] = [8, -5, 2, -7, 6]
C: List[int] = [2, -1, 0, -5, 3]
D: List[int] = [5, -8, 3, 0, 1]


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    z = 0
    for i in a:
        for j in b:
            for k in c:
                for l in d:
                    sum_abcd = i + j + k + l  # A[i] + B[j] + C[k] + D[l]
                    if sum_abcd == 0:
                        # print("A: %i\tB: %i\tC: %i\tD: %i" % (i, j, k, l))
                        z += 1

    return z


check_sum_of_four(A, B, C, D)