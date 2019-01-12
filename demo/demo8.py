def print_line(line, content):
    print(content * line)


def print_five(line, content):
    """打印五行

    :param line: 一行多少个
    :param content: 内容
    """
    i = 0
    while i < 5:
        print_line(line, content)
        i += 1


print_five(5, "1")
