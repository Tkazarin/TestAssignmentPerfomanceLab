import sys
from decimal import Decimal, getcontext, InvalidOperation

getcontext().prec = 100


def point_position(x, y, cx, cy, rx, ry):
    x -= cx
    y -= cy
    res = (x * x) / (rx * rx) + (y * y) / (ry * ry)
    if res == 1:
        return 0
    elif res < 1:
        return 1
    else:
        return 2


def main():
    if len(sys.argv) != 3:
        print("Неверное количество аргументов")
        return

    try:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except (FileNotFoundError, OSError):
        print("Файл не найден или невозможно открыть")
        return

    if len(lines) < 2:
        print("Должно быть 2 непустых строки")
        return

    try:
        cx, cy = map(Decimal, lines[0].split())
        rx, ry = map(Decimal, lines[1].split())
    except ValueError:
        print("Недостаточно значений")
        return

    if rx <= 0 or ry <= 0:
        print("Отрицательные значения в аргументах")
        return

    points = []
    try:
        with open(sys.argv[2], "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    x, y = map(Decimal, line.split())
                    points.append((x, y))
                except (ValueError, InvalidOperation):
                    print("Недостаточно значений строке или неверный формат")
                    return
    except (FileNotFoundError, OSError):
        print("Файл не найден или невозможно открыть")
        return

    for x, y in points:
        print(point_position(x, y, cx, cy, rx, ry))


if __name__ == "__main__":
    main()
