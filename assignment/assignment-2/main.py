from csv_file_manager import read_csv_file, write_csv_file
import random

if __name__ == "__main__":
    csv_file_name = "users.csv"

    all_information = read_csv_file(csv_file_name)
    print("모든 정보:")
    for info in all_information:
        print(info)

    for i in range(6):  # 6명의 사용자 정보 입력 받기
        email = input("이메일을 입력해주세요 (exit 입력 시 종료): ")
        if email.lower() == "exit":
            break
        password = input("비밀번호를 입력해주세요: ")
        nickname = input("별명을 입력해주세요: ")
        information = [email, password, nickname]
        write_csv_file(csv_file_name, information)
        all_information.append(information)

        print("모든 정보:")
        for info in all_information:
            print(info)

        if len(all_information) >= 6:
            random_users = random.sample(all_information, 2)
            print("랜덤 추출 2명:")
            for random_user in random_users:
                print(random_user[2])
