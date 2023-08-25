import csv
def read_csv_file(csv_file_name):
    file_reader = open("users.csv", "r", encoding="utf8", newline="\n")
    csv_file_reader = csv.reader(file_reader)
    for row in csv_file_reader:
        print(row)
    read_contents = []
    return read_contents


def write_csv_file(csv_file_name, contents):
    file_writer = open("users.csv", "a", encoding="utf8", newline="\n")
    csv_file_writer = csv.writer(file_writer)
    email = input("이메일을 입력해주세요: ")
    password = input("비밀번호를 입력해주세요: ")
    nickname = input("별명을 입력해주세요: ")
    csv_file_writer.writerow([email, password, nickname])
    file_writer.close()



if __name__ == "__main__":
    pass
