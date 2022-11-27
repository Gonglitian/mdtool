move_in_flag = 0


def clean_code(file_path, new_path):
    with open(file_path, encoding='utf-8',  mode='r') as file:
        with open(new_path, encoding='utf-8',  mode='w') as new_file:
            for line in file.readlines():
                if not move_in_flag:
                    new_file.write(line)
                if "```" in line:
                    if move_in_flag == 0:
                        move_in_flag = 1
                    else:
                        move_in_flag = 0
                        new_file.write("    ```")


def add_seq(file_path, new_path):
    deepth = {1: 0, 2: 0, 3: 0, 4: 0}
    n = len(deepth)
    last_count = 0
    with open(file_path, encoding='utf-8',  mode='r') as file:
        with open(new_path, encoding='utf-8',  mode='w') as new_file:
            for line in file.readlines():
                len_line = len(line)
                if line[0] == "#":
                    count = 0
                    for i, char in enumerate(line):
                        if line[i] == '#':
                            count += 1
                            if i+1 < len_line:  # 避免下标越界
                                if line[i+1] != "#":  # 只检测连续的"#"
                                    break
                            else:
                                break

                    if count < last_count:
                        for i in range(count+1, n+1):
                            deepth[i] = 0
                    deepth[count] += 1
                    last_count = count

                    #根据
                    seq = list(deepth.values())[:count]
                    temp = str()
                    for x in seq:
                        temp += str(x)
                    seq = '.'.join(temp)
                    seq += ' '
                    temp_line = line[:count+1] + seq + line[count+1:]
                    new_file.write(temp_line)
                else:
                    new_file.write(line)


if __name__ == '__main__':
    add_seq("test.md", "output.md")
