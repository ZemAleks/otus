import csv
import json

from hw5_testdata.test_data import JSON_FILE_W


def parse_users(json_file_name: str) -> list:
    users_list = []
    users_key = ["name", "gender", "address", "age"]

    with open(json_file_name, "r") as json_file:
        users_origin = json.load(json_file)

    for user_default in users_origin:
        data = {key: value for key, value in user_default.items() if key in users_key}
        users_list.append(data)

    return users_list


def parse_books(csv_file_name):
    books_list = []
    books_keys = ["Title", "Author", "Pages", "Genre"]

    with open(csv_file_name, "r") as csv_file:
        for row in csv.DictReader(csv_file):
            data = {key: value for key, value in row.items() if key in books_keys}
            if "Pages" in data:
                data["Pages"] = int(data["Pages"])
            books_list.append(data)

    return books_list


def parse_assign(books_list: list, users_list: list) -> list:
    result_list = []
    books_per_user = len(books_list) // len(users_list)
    remaining_books = len(books_list) % len(users_list)

    for i, user_default in enumerate(users_list):
        merger_user_books = books_list[i * books_per_user: (i + 1) * books_per_user]

        if i < remaining_books:
            merger_user_books.append(books_list[len(users_list) * books_per_user + i])

        user_default["books"] = merger_user_books
        result_list.append(user_default)

    return result_list


def export_json(result_list):

    with open(JSON_FILE_W, "w") as file:
        res = json.dumps(result_list, indent=4)
        file.write(res)


def main():
    json_file_name = "users.json"
    csv_file_name = "books.csv"

    users_processed = parse_users(json_file_name)
    books_processed = parse_books(csv_file_name)

    result = parse_assign(books_processed, users_processed)
    export_json(result)


if __name__ == "__main__":
    main()
