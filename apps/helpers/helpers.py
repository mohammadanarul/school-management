from random import randint


def bd_number_generator(prefix="018"):
    return f"{prefix}{randint(12345678,99999999)}"


if __name__ == "__main__":
    print(f'number: {bd_number_generator("019")}')
