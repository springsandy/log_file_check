def file_r():
    f = open('./a.log', 'r')
    line = f.readlines()
    for line_num, line_data in enumerate(line):
        line_list = line_data.split()
        print("%d %s" %(line_num+1, line_list), end='\n')
    f.close()