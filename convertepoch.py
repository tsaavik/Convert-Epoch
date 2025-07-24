#!/usr/bin/env python3
import re
import sys
import time

print("This program reads epoch seconds from stdin and converts them, ctrl-d to end/cancel")

epoch_pattern = r'(\d\d\d\d\d\d\d\d\d\d)'
for line in sys.stdin:
    epoch_str = re.search(epoch_pattern, line)
    if epoch_str:
        epoch = int(epoch_str.group())
        timestamp = time.strftime("%a %b %d %H:%M:%S %Y",
                                  time.localtime(epoch))
        print(line.replace(epoch_str.group(), timestamp))
    else:
        print(line)
