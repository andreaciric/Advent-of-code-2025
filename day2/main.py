def is_invalid_id(n: int) -> bool:
        s = str(n)

        if len(s) % 2 != 0:
            return False

        half = len(s) // 2
        return s[:half] == s[half:]

def is_invalid_id2(n: int) -> bool:

    s = str(n)
    full_length = len(s)

    for sub_length in range(1, full_length // 2 + 1):
        if full_length % sub_length != 0:
            continue  
        num_repeats = full_length // sub_length
        if num_repeats < 2:
            continue

        block = s[:sub_length]
        if block * num_repeats == s:
            return True

    return False

def sum_invalid_ids(ranges_line: str) -> int:

    sum1 = 0
    sum2 = 0

    for part in ranges_line.split(","):
        part = part.strip()

        start_str, end_str = part.split("-")
        start = int(start_str)
        end = int(end_str)

        for n in range(start, end + 1):
            if (is_invalid_id(n)):
                sum1 += n
            if (is_invalid_id2(n)):
                sum2 += n
    return sum1, sum2

def main():
    try:
        with open("input.txt", "r") as f:
            IDs = f.read().strip()
    except FileNotFoundError:
        print("Error: Input file not found.")
        return

    result1, result2 = sum_invalid_ids(IDs)
    print("Sum of invalid IDs (part1):", result1)
    print("Sum of invalid IDs (part2):", result2)


if __name__ == "__main__":
    main()