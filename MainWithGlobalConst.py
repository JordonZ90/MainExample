TAX_RATE = 0.05  # Global constant


def calc_tax(amount):
    tax = amount * TAX_RATE
    return tax


def main():
    amount = calc_tax(330)
    print(f"Tax rate {TAX_RATE}, amount {round(amount, 2)}")


if __name__ == "__main__":
    main()
