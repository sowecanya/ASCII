import time
import os


def to_console(filename):
    with open(filename.replace(".jpg", ".txt"), "r", encoding="utf-8") as text:
        for line in text:
            print(line, end="")
            time.sleep(0.05)

    # os.remove("result.txt")
