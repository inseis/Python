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
users = [user1, user2, user3]


def decide_job(user):
    if user.get('gender') == '여성':
        if user.get('age') <= 23:
            return '학생'
        else:
            return '직장인'
    else:
        if user.get('age') <= 25:
            return '학생'
        else:
            return '직장인'


if __name__ == "__main__":
    for user in users:
        name = user['name']
        age = user['age']
        gender = user['gender']
        state = decide_job(user)
        print(f"{name}은 {age}살 {gender}이고 직업은 {state}입니다.")

    for number1 in range(2, 10):
        for number2 in range(1, 10):
            print(number1, "X", number2, "=", number1 * number2)
