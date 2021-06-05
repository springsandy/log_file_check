def file_r():
    f = open('./a.log', 'r')
    log_data = []
    line_num = 1

    line = f.readline()
    while line:
        line = line.rstrip('\n')
        line_data = line.split(', ')
        print("%d %s %s %s %s %s\n" %(line_num, line_data[0], line_data[1], line_data[2], line_data[3], line_data[4]), end='')
        log_data.append(line_data)
        line = f.readline()
        line_num += 1

    print("총 수정해야될 부분의 개수", line_num-1 ,"입니다.")
    print(log_data)

    f.close()

    return log_data