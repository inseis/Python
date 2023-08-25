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
        all_information.append(information)  # 새 정보 추가

        print("모든 정보:")
        for info in all_information:
            print(info)

        if len(all_information) >= 6:
            random_users = random.sample(all_information, 2)
            print("랜덤 추출 2명:")
            for random_user in random_users:
                print(random_user[2])  # 사용자의 이름 출력















# csv_file_manager.py 파일의 함수 2개를 완성하세요
# main.py 파일에서 csv_file_manager.py 파일의 함수 2개를 가져와서 코드를 작성하세요
# main.py 파일에서 아래의 유저들을 콘솔에서 입력받고, csv 파일에 데이터를 쓸 수 있도록 코드를 작성하세요
# 유저의 이메일을 입력받을 때, exit를 입력하면 프로그램이 종료되도록 만들어주세요
# 유저 1명이 추가될 때마다, 현재 csv 파일에 저장된 모든 유저들의 목록을 전부 출력해주세요
# 추가할 유저 정보는 이메일, 비밀번호, 이름으로 아래와 같습니다
# xxx@xxx.com | 1234 | 김세모
# zzz@zzz.com | 1234 | 김동그라미
# qqq@qqq.com | 1234 | 쵸단
# www@www.com | 1234 | 마젠타
# eee@eee.com | 1234 | 냥뇽녕냥
# 마지막으로 6명의 유저를 모두 입력받은 후 랜덤으로 2명의 유저를 선택해서 이름만 출력해주세요
