def read_input(filename):

    ranges = []
    ids = []

    with open(filename, "r") as f:
        lines = [line.strip() for line in f]

    i = 0
    while i < len(lines) and lines[i] != "":
        start, end = lines[i].split("-")
        ranges.append((int(start), int(end)))
        i += 1

    i += 1

    while i < len(lines):
        if lines[i] != "":
            ids.append(int(lines[i]))
        i += 1

    return ranges, ids

def count_fresh_ids(ranges, ids):

    result = 0

    for ingredient_id in ids:
        for start, end in ranges:
            if start <= ingredient_id <= end:
                result += 1
                break

    return result

def merge_ranges(ranges):

    if not ranges:
        return []

    ranges.sort()
    merged = [ranges[0]]

    for start, end in ranges[1:]:
        prev_start, prev_end = merged[-1]

        if start <= prev_end + 1:
            merged[-1] = (prev_start, max(prev_end, end))
        else:
            merged.append((start, end))

    return merged

def count_fresh_ids_total(ranges):

    total = 0
    for start, end in ranges:
        total += (end - start + 1)

    return total

def main():
    ranges, ids = read_input("input.txt")
    result = count_fresh_ids(ranges, ids)
    ranges_total = merge_ranges(ranges)
    result_total = count_fresh_ids_total(ranges_total)
    print("Number of fresh ingredient IDs:", result)
    print("Total number of fresh ingredients:", result_total)

if __name__ == "__main__":
    main()