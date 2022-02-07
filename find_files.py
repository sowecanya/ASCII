import glob


def finder():
    patterns = glob.glob('sample/*.jpg')

    for pattern_index, pattern_name in enumerate(patterns):
        print(f'[{pattern_index + 1}] - {pattern_name}')

    selected_pattern_number = input('\nВведите номер фото: ')
    selected_pattern = patterns[int(selected_pattern_number) - 1]
    return selected_pattern
