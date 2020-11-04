def create_matrix(lines, columns):
    matrix = []
    for i in range(lines+1):
        matrix.append([])
        for j in range(columns+1):
            matrix[i].append(0)

    return matrix


def add_coordinates(matrix, x, y):
    matrix[x][y] += 1
    return matrix[x][y]


def main():
    matrix = create_matrix(500, 500)
    verification = 0

    for i in range(int(input())):
        x, y = map(int, input().split())
        if add_coordinates(matrix, x, y) > 1:
            verification = 1

    print(verification)


if __name__ == '__main__':
    main()
