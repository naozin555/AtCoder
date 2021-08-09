def bitwise_exclusive_or(a: int, b: int):
    for c in range(256):
        if bin(a ^ c) == bin(b):
            return c


if __name__ == '__main__':
    A, B = map(int, input().split())
    print(bitwise_exclusive_or(A, B))

    # best practice
    # A, B = map(int, input().split())
    # print(A ^ B)
