from typing import List


def booby_prize(num: int, scores_list: List[int]):
    dic = {i + 1: score for i, score in zip(range(num), scores)}
    scores_list.sort()
    booby = [k for k, v in dic.items() if v == scores_list[n-2]]
    return booby[0]


if __name__ == '__main__':
    n = int(input())
    scores = [int(x) for x in input().split()]
    print(booby_prize(n, scores))

    # model answer
    # N = int(input())
    # A = list(map(int,input().split()))
    # v = []
    # for i in range(N):
    #     v.append((A[i], i+1))
    # v.sort()
    # v.reverse()
    # print(v[1][1])

