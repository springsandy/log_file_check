from file import file_r

def choice():
    level_data =['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    choice_data = []
    log_data = file_r()

    print("1=>DEBUG / 2=>INFO / 3=>WARNING / 4=>ERROR / 5=>CRITICAL")
    level = input("이 다섯가지 중에 한가지를 선택하시오. -> ")

    print("level은 ", level_data[int(level) - 1], "입니다.")
    for x in log_data:
        if level_data[int(level)-1] == x[1]:
            print("파일의 위치는 ", x[2] ,"에 ", x[3] ,"줄에 위치해있으며, 메세지 내용은 '", x[4] ,"'입니다.")
            choice_data.append(x)

    print(level_data[int(level)-1], "의 총 개수는 ", len(choice_data) ,"개 입니다.")