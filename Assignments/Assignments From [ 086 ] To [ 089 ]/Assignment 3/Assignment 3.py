from PIL import Image

myImage = Image.open(
    "P:\Python Course\Assignments\Assignments From [ 086 ] To [ 089 ]\Assignment 3\elzero-pillow.png")

letter_l = myImage.crop((400, 0, 800, 400)).convert("L")
letter_l.save(
    "P:\Python Course\Assignments\Assignments From [ 086 ] To [ 089 ]\Assignment 3\grey-L.png")

second_column = myImage.crop((0, 400, 1200, 800)).rotate(180).convert("L")
second_column.save(
    "P:\Python Course\Assignments\Assignments From [ 086 ] To [ 089 ]\Assignment 3\second-column.png")
