import do_file
import find_files
import read_file

if __name__ == '__main__':
    filename = find_files.finder()
    if not do_file.check_file(filename.replace(".jpg", ".txt")):
        do_file.to_ascii(filename)
    read_file.to_console(filename)

