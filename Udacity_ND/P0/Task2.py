"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

from enum import IntEnum


class TextHeader(IntEnum):
    SENDER = 0,
    RECEIVER = 1,
    TS = 2,


class CallHeader(IntEnum):
    CALLER = 0,
    RECEIVER = 1,
    TS = 2,
    DURATION = 3,


# with open('texts.csv', 'r') as f:
#     reader = csv.reader(f)
#     texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    numbers = {}
    for call_record in reader:
        if call_record[CallHeader.CALLER] in numbers:
            numbers[call_record[CallHeader.CALLER]] += int(call_record[CallHeader.DURATION])
        else:
            numbers[call_record[CallHeader.CALLER]] = int(call_record[CallHeader.DURATION])
        
        if call_record[CallHeader.RECEIVER] in numbers:
            numbers[call_record[CallHeader.RECEIVER]] += int(call_record[CallHeader.DURATION])
        else:
            numbers[call_record[CallHeader.RECEIVER]] = int(call_record[CallHeader.DURATION])
    max_dur_number = max(numbers, key=numbers.get)
    print(f"{max_dur_number} spent the longest time, {numbers[max_dur_number]} seconds, on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during September 2016.".
"""
