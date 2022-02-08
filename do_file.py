from PIL import Image, ImageDraw, ImageFont
import os
from loader import WIDTH_OF_REGION, HEIGHT_OF_REGION


char_map = {}


def check_file(filename):
    return os.path.exists(f"{filename}")


def char_image(char):
    """
    Получает картинку с символами нарисованными на ней символами
    :param char:
    :return: chr
    """
    font = ImageFont.truetype("Menlo-Regular.woff", 40)
    image = Image.new('RGB', (50, 50), (255, 255, 255))
    drawer = ImageDraw.Draw(image)
    drawer.text((0, 0), char, font=font, fill=(0, 0, 0))
    image = image.convert('1')
    return image


def avg_gray_value(image) -> int:
    """
    Получает значения серого картинки
    :param image:
    :return: int
    """
    width, height = image.size
    total_pixels_value = width * height * 255
    gray_value = 0
    for x in range(0, width):
        for y in range(0, height):
            gray_value += image.getpixel((x, y))
    return int(gray_value/total_pixels_value*10000)


def split_image(image) -> list:
    """
    Сплитит значения в список
    :param image:
    :return: list
    """
    regions = []
    count = 0
    for y in range(0, image.height-HEIGHT_OF_REGION, HEIGHT_OF_REGION):
        count += 1
        for x in range(0, image.width-WIDTH_OF_REGION, WIDTH_OF_REGION):
            rect = (x, y, x + WIDTH_OF_REGION, y + HEIGHT_OF_REGION)
            regions.append(image.crop(rect))
    return regions


def create_char_map(start_index: int, end_index: int):
    """
    Создает карту, которая будет соединена со значениями
    :param start_index:
    :param end_index:
    :return:
    """
    load_characters(start_index, end_index)
    normalize_char_map()
    fill_char_map()


def load_characters(start_index: int, end_index: int):
    """
    Загружает уникальные серые значения в карту символов
    :param start_index: int
    :param end_index: int
    """
    for index in range(start_index, end_index):
        char_img = char_image(chr(index))
        grey_value = avg_gray_value(char_img)
        if grey_value not in char_map:
            temp = {grey_value: chr(index)}
            char_map.update(temp)


def normalize_char_map():
    """
    Рисует значения, самые темные 0, самые светлые 10
    """
    global char_map
    temp_map = {}
    max_value = 0
    min_value = 10000
    for value in char_map:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value
    for value in char_map:
        temp_value = int(((10000-0)*(value-min_value)) / (max_value-min_value) + 0)
        temp_map.update({temp_value: char_map.get(value)})
    char_map = temp_map


def fill_char_map():
    """
    Проверяет пустые значения
    """
    recent = None
    for index in range(0, 10001):
        if index in char_map:
            recent = index
        else:
            char_map.update({index: char_map.get(recent)})


def to_ascii(filename: str):
    """
    Собирает вместе и создает картинку ASCII
    :param filename:
    """
    image = Image.open(filename).convert('L')
    create_char_map(33, 750)
    regions = split_image(image)
    columns = int(image.width / WIDTH_OF_REGION)
    if len(regions) % columns != 0:
        columns -= 1
    for index in range(0, len(regions)):
        with open(filename.replace(".jpg", ".txt"), "a", encoding="utf-16") as result:
            if index % columns == 0 and index != 0:
                result.write("\n")
            result.write(char_map.get(avg_gray_value(regions[index])))

