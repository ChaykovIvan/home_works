def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


def get_password(n):
    result = ""
    divisors = find_divisors(n)

    for i in range(1, n):
        for j in range(i + 1, n):
            for divisor in divisors:
                if (i + j) % divisor == 0:
                    result += str(i) + str(j)
                    break
    return result


n = int(input("Введите число (от 3 до 20): "))
password = get_password(n)
print("Нужный пароль:", password)
