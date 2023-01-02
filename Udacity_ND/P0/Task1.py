"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
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


unique_numbers = set()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    for record in reader:
        unique_numbers.update([record[TextHeader.SENDER], record[TextHeader.RECEIVER]])

    # texts = list(reader) this will create unnecessary loop
print(f"There are {len(unique_numbers)} different telephone numbers in the records.")

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    for record in reader:
        unique_numbers.update([record[CallHeader.CALLER], record[CallHeader.RECEIVER]])
    calls = list(reader)

print(f"There are {len(unique_numbers)} different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
