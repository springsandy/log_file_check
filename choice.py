def choice():
    level_data =['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

    print("1=>DEBUG / 2=>INFO / 3=>WARNING / 4=>ERROR / 5=>CRITICAL")
    level = input("이 다섯가지 중에 한가지를 선택하시오. -> ")

    print(level_data[int(level)-1])