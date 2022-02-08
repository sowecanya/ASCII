import time


def to_console(filename: str):
    with open(filename.replace(".jpg", ".txt"), "r", encoding="utf-16") as text:
        for line in text:
            print(line, end="")
            time.sleep(0.05)

