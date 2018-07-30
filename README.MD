## This is a simple log parser that can find the keyword in the log file and print the specified number of lines around the line with this keyword (by default, the number of lines is +100 and -100)

### To run it just type following command:
```
python log_searcher.py -p <PATH_TO_LOG> -t <TARGET_KEYWORD>
```
### Required parameters:

* Path to log file
```
-p <PATH_TO_LOG>
```
* Target keyword 
```
-t <TARGET_KEYWORD>
```

### You can also use additional parameters:

* IP address of remote server with logs
```
-i <IP_ADDRESS_OF_REMOTE_MACHINE>
```

* Limit of the lines that will be printed out
```
-l <LINES_LIMIT>
```
