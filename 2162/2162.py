def verify_higher(a, b, c):
    return a < b > c


def verify_lower(a, b, c):
    return a > b < c


def verify_hills(hills, n):
    verification = 1

    if n == 2 and hills[0] == hills[1]:
        verification = 0

    for i in range(1, n-1):
        if verify_higher(int(hills[i-1]), int(hills[i]), int(hills[i+1])):
            continue
        elif verify_lower(int(hills[i-1]), int(hills[i]), int(hills[i+1])):
            continue
        else:
            verification = 0
        i += 1

    return verification


def main():
    n = int(input())
    hills = input().split()

    print(verify_hills(hills, n))


if __name__ == '__main__':
    main()
