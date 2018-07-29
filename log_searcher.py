import getopt
import sys

from log_store import LogStore


class LogSearcher(object):
    def __init__(self, argv):
        self.__parse_cmd_args(argv)
        self.line_counter = 100
        self.found = False
        self.log_store = LogStore()
        self.connect_to_server(self.ip)
        self.try_to_find_data_in_log()

    def __parse_cmd_args(self, argv):
        try:
            opts, args = getopt.getopt(argv, "i:l:t:", ["ip=", "log=", "target="])
        except getopt.GetoptError:
            print('log_search.py -i <ip> -l <log> -t <target_id>')
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-i", "--ip"):
                self.ip = arg
            elif opt in ("-l", "--log"):
                self.log = arg
            elif opt in ("-t", "--target"):
                self.target_keyword = arg

    def connect_to_server(self, ip):
        """
        There should be a connection logic to the remote machine.
        But task too abstract and this method does nothing.
        """
        pass

    def try_to_find_data_in_log(self):
        log_file = self.get_log_file()

        for line in log_file:
            if self.found and self.line_counter != 0:
                print(line)
                self.line_counter -= 1
            elif self.line_counter == 0:
                return
            else:
                self.check_current_line(line)

        if not self.found:
            print("Can't find keyword: {} in log: {} by address: {}".format(self.target_keyword, self.log, self.ip))

    def get_log_file(self):
        try:
            file = open(self.log, "r", encoding="utf-8")
            return file
        except FileNotFoundError:
            print("Can't find log with name: " + self.log)
            sys.exit(2)

    def check_current_line(self, line):
        if str(self.target_keyword) in line:
            self.log_store.print_lines()
            print(line)
            self.found = True
        else:
            self.log_store.append(line)


if __name__ == "__main__":
    LogSearcher(sys.argv[1:])
