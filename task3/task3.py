import sys
import json


def fill_values(tests, values_map):
    for test in tests:
        if test["id"] in values_map:
            test["value"] = values_map[test["id"]]
        if "values" in test and test["values"]:
            fill_values(test["values"], values_map)


def main():
    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]

    try:
        with open(values_path, "r", encoding="utf-8") as f:
            values_data = json.load(f)
        with open(tests_path, "r", encoding="utf-8") as f:
            tests_data = json.load(f)
    except (FileNotFoundError, OSError):
        print("Файл не найден или невозможно открыть")
        return

    values_map = {}
    for item in values_data["values"]:
        values_map[item["id"]] = item["value"]

    fill_values(tests_data["tests"], values_map)

    try:
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(tests_data, f, ensure_ascii=False, indent=2)
    except (FileNotFoundError, OSError):
        print("Файл не найден или невозможно открыть")
        return


if __name__ == "__main__":
    main()
