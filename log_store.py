class LogStore(object):
    def __init__(self, lines_limit):
        self.__lines = []
        self.__lines_limit = lines_limit

    def append(self, line):
        if self.__lines_limit != 0:
            self.__lines.append(line)
            self.__lines_limit -= 1
        else:
            self.__lines.pop(0)
            self.__lines.append(line)

    def print_lines(self):
        for line in self.__lines:
            print(line)
