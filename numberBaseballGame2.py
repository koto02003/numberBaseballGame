from random import randint

#정답 숫자 생성
def generate_numbers():
    numbers = []
    i = 0
    new_number = 0
    while i < 4:
        new_number = randint(0, 9)
        if new_number not in numbers:
            numbers.append(new_number)
            i += 1
    print("0과 9 사이의 서로 다른 숫자 4개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

#숫자 예측
def take_guess():
    print("숫자를 입력하세요 : ", end=' ')
    i = 0
    inp_list = []
    inp_list = list(map(int, input().split()))

    return inp_list

#점수 판별
def get_score(guess, solution):
    strike_count = 0
    ball_count = 0
    i = 0

    while i < len(guess):
        if guess[i] == solution[i]:
            strike_count += 1
            i += 1
        elif guess[i] in solution:
            ball_count += 1
            i += 1
        else:
            i += 1
    return strike_count, ball_count


# 게임 시작
ANSWER = generate_numbers()
tries = 0

while 1:
    GUESS = take_guess()
    strike, ball = get_score(GUESS, ANSWER)
    if strike == ball == 0:
        print("OUT")
    else:
        print("{}S {}B ".format(strike, ball))

    if strike == 4:
        tries += 1
        break
    else:
        tries += 1

print("축하합니다. {}번 만에 숫자 4개의 값과 위치를 모두 맞추셨습니다.".format(tries))