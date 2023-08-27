import csv


def read_csv_file(csv_file_name):
    read_contents = []
    with open(csv_file_name, "r", encoding="utf8", newline="\n") as file_reader:
        csv_file_reader = csv.reader(file_reader)
        for row in csv_file_reader:
            read_contents.append(row)
    return read_contents


def write_csv_file(csv_file_name, contents):
    with open(csv_file_name, "a", encoding="utf8", newline="\n") as file_writer:
        csv_file_writer = csv.writer(file_writer)
        csv_file_writer.writerow(contents)


if __name__ == "__main__":
    pass
