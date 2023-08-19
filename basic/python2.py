from random import randint
import csv

user1 = {
    "name": "김동그라미",
    "age": 24,
    "gender": "여성",
}
user2 = {
    "name": "김네모",
    "age": 25,
    "gender": "남성",
}
user3 = {
    "name": "김세모",
    "age": 29,
    "gender": "남성",
}
user4 = {
    "name": "김육각형",
    "age": 29,
    "gender": "남성",
}
user5 = {
    "name": "김오각형",
    "age": 29,
    "gender": "남성",
}
users = [user1, user2, user3, user4, user5]

# 정의 코드를 여기에 적어주세요
if __name__ == "__main__":
    # 실행 코드를 여기에 적어주세요

    # 1. 모듈
    # 랜덤으로 뽑은 유저 3명을 담은 배열을 만들어 주세요
    random_users = []
    while len(random_users) < 3:
        random_index = randint(0, 4)
        random_user = users[random_index]

        is_user_selected = False
        for user in random_users:
            if user == random_user:
                is_user_selected = True
                break

        if is_user_selected is False:
            random_users.append(random_user)

    for random_user in random_users:
        print(random_user["name"])

    # 2. 사용자 입력
    name = input("이름을 알려줘: ")
    print(f"입력받은 이름: {name}")

    # 3. 파일 쓰기(w, a)
    file_writer = open("users.csv", "a", encoding="utf8", newline="\n")
    csv_file_writer = csv.writer(file_writer)
    email = input("이메일을 입력해주세요: ")
    password = input("비밀번호를 입력해주세요: ")
    nickname = input("별명을 입력해주세요: ")
    csv_file_writer.writerow([email, password, nickname])
    file_writer.close()

    # 4. 파일 읽기(r)
    file_reader = open("users.csv", "r", encoding="utf8", newline="\n")
    csv_file_reader = csv.reader(file_reader)
    for row in csv_file_reader:
        print(row)
