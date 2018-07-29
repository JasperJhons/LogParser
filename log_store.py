class LogStore(object):
    def __init__(self):
        self.__lines = []
        self.__line_counter = 0

    def append(self, line):
        if self.__line_counter != 100:
            self.__lines.append(line)
            self.__line_counter += 1
        else:
            self.__lines.pop(0)
            self.__lines.append(line)

    def print_lines(self):
        for line in self.__lines:
            print(line)
