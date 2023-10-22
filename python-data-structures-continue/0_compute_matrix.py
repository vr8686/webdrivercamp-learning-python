#!/usr/bin/python3

def compute_matrix(matrix=[]):
    def square(n):
        return n * n
    result = []
    for x in matrix:
        y = list(map(square, x))
        result.append(y)
    return result


if __name__ == "__main__":
    matrix = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]

print(f"Original: {matrix}")
print(f"Modified: {compute_matrix(matrix)}")
