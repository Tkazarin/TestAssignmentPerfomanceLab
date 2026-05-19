import sys


def main():
    if len(sys.argv) < 2:
        print("Не указан путь к файлу")
        return

    nums = []
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                x = int(line)
            except ValueError:
                print("Файл должен содержать только целые числа")
                return
            nums.append(x)

    if not nums:
        print("Файл пуст")
        return

    nums.sort()
    len_nums = len(nums)
    median_nums = nums[len_nums // 2]
    moves = 0
    for x in nums:
        moves += abs(x - median_nums)

    if moves <= 20:
        print(moves)
    else:
        print("20 ходов недостаточно для приведения всех "
              "элементов массива к одному числу")


if __name__ == "__main__":
    main()
