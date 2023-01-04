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


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    first_rec = next(reader)
    print(f"First record of texts, {first_rec[TextHeader.SENDER]} texts {first_rec[TextHeader.RECEIVER]} at time {first_rec[TextHeader.TS]}")

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    last_rec = calls[-1]
    print(f"Last record of calls, {last_rec[CallHeader.CALLER]} calls {last_rec[CallHeader.RECEIVER]} at time {last_rec[CallHeader.TS]}, lasting {last_rec[CallHeader.DURATION]} seconds")


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
