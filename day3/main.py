
def max_joltage_in_bank(bank: str) -> int:
    digits = [int(c) for c in bank.strip()]
    
    max_left = digits[0]
    best = -1

    for j in range(1, len(digits)):
        temp = 10 * max_left + digits[j]
        if temp > best:
            best = temp
        
        if digits[j] > max_left:
            max_left = digits[j]

    return best

def max_joltage_in_bank_12(bank: str) -> int:

    k = 12
    digits = [int(c) for c in bank.strip()]
    n = len(digits)

    remove = n - k
    stack = []

    for d in digits:
        while remove and stack and stack[-1] < d:
            stack.pop()
            remove -= 1
        stack.append(d)

    if remove > 0:
        stack = stack[:-remove]

    result_digits = stack[:k]
    return int("".join(str(d) for d in result_digits))



def main():
    result = 0
    result_12 = 0

    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            bank_max = max_joltage_in_bank(line)
            result += bank_max

            bank_max_12 = max_joltage_in_bank_12(line)
            result_12 += bank_max_12

    print("Total output joltage:", result)
    print("Total output joltage 12:", result_12)


if __name__ == "__main__":
    main()