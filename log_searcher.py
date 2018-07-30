import getopt
import sys

from log_store import LogStore

default_lines_limit = 100
default_ip_address = "localhost"


class LogSearcher(object):
    def __init__(self, argv):
        self.lines_limit = default_lines_limit
        self.ip_address = default_ip_address
        self.target_keyword = None
        self.log_path = None
        self.found = False
        self.parse_cmd_args(argv)
        self.log_store = LogStore(self.lines_limit)
        self.connect_to_server()
        self.try_to_find_data_in_log()

    def parse_cmd_args(self, argv):
        try:
            opts, args = getopt.getopt(argv, "i:p:t:l:", ["ip=", "log_path=", "target=", "lines_limit="])
        except getopt.GetoptError:
            print('log_search.py -i <ip> -p <log_path> -t <target_id> -l <lines_limit>')
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-i", "--ip"):
                self.ip_address = arg
            elif opt in ("-p", "--log_path"):
                self.log_path = arg
            elif opt in ("-t", "--target"):
                self.target_keyword = arg
            elif opt in ("-l", "--lines_limit"):
                self.lines_limit = int(arg)

        if self.log_path is None or self.target_keyword is None:
            print("You must specify log path and target keyword")
            print("Use arguments: -p <log_path> -t <target_id>")
            sys.exit(2)

    def connect_to_server(self):
        if self.ip_address in ("localhost", "127.0.0.1"):
            return
        else:
            """
            There should be a connection logic to the remote machine.
            But task too abstract and this method does nothing.
            """
            pass

    def try_to_find_data_in_log(self):
        log_file = self.get_log_file()

        for line in log_file:
            if self.found and self.lines_limit != 0:
                print(line)
                self.lines_limit -= 1
            elif self.lines_limit == 0:
                return
            else:
                self.check_current_line(line)

        if not self.found:
            print("Can't find keyword: {} in log: {} by address: {}".format(self.target_keyword, self.log_path,
                                                                            self.ip_address))

    def get_log_file(self):
        try:
            file = open(self.log_path, "r", encoding="utf-8")
            return file
        except FileNotFoundError:
            print("Can't find log with name: " + self.log_path)
            sys.exit(2)

    def check_current_line(self, line):
        if self.target_keyword in line:
            self.log_store.print_lines()
            print(line)
            self.found = True
        else:
            self.log_store.append(line)


if __name__ == "__main__":
    LogSearcher(sys.argv[1:])
