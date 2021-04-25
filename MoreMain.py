def calc_tax(amount, tax_rate):
    tax = amount * tax_rate  # local variable
    return tax

def main():
    tax = calc_tax(85.0, 0.5)  # local variable
    print(f"Tax {tax}")

if __name__ == "__main__":
    main()