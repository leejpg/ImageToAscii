from PIL import Image, ImageEnhance
import math


def imageName(path: str):
    name = path.split('/')[-1].split('.')[0]
    return 'result_' + name + '.txt'

dir = input("insert the location of file: ")
buf = int(input("inset the width of final ascii image: "))

with Image.open(dir) as image:
    wi, he = image.size
    r = he / wi
    
    img = (image.convert('L').resize((math.floor(buf), math.floor(r * buf))))
    gimg = ImageEnhance.Contrast(img).enhance(3)

result = open(imageName(dir), 'w')

ascii_char = [' ','.',':','-','=','+','*','#','%','@']
#ascii_char = "$ @ B % 8 & W M # * o a h k b d p q w m Z O 0 Q L C J U Y X z c v u n x r j f t / () 1 [] ? - _ + ~ <> i ! l I ; : , ^ . ".split(" ")
w, h = gimg.size

ascii_char.reverse()

def intensityConv(charset, value): # receives a color value (0 to 255) and convert proportionally to a index on ascii_char array
    index = math.floor((len(charset) / 255) * value) - 1
    if index < 0:
        index += 1
    return charset[index]

for j in range(h):
    for i in range(w):
        char = intensityConv(ascii_char, gimg.getpixel((i, j)))

        if i == w-1:
            char += '\n'

        result.writelines(char)
result.close()



