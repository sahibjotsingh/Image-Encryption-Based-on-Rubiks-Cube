from PIL import Image
from random import randint
import numpy as np
import json

myImage = Image.open("C:\\Users\\Hp-user\\Desktop\\startups\\Image encrypt\\Python\\flower-encrypted.png");
width, height = myImage.size
pixels = myImage.load()

fill = 1
array = [[fill for x in range(width)] for y in range(height)]

for y in range(height):
    for x in range(width):
        #lum = 255 - pixels[x,y] # Reversed luminosity
        array[y][x] = pixels[x,y] # Map values from range 0-255 to 0-1

with open("KR.txt", "r") as infile:
    KR = json.load(infile)

with open("KC.txt", "r") as infile:
    KC = json.load(infile)

for i in range(height):
    for j in range(width):
        if((j%2) != 0):
            array[i][j] = array[i][j] ^ KR[i]
        else:
            array[i][j] = array[i][j] ^ KR[height - 1 - i]

for j in range(width):
    for i in range(height):
        if((i%2) != 0):
            array[i][j] = array[i][j] ^ KC[j];
        else:
            array[i][j] = array[i][j] ^ KC[width - 1 - j]

for j in range(width):
    beta = 0
    for i in range(height):
        beta = ((beta % 2) + (array[i][j] % 2)) % 2
    if(beta == 0):
        for k in range(KC[j]):
            temp2 = array[0][j]
            for l in range(height - 1):
                array[l][j] = array[l+1][j]
            array[height - 1][j] = temp2
    else:
        for k in range(KC[j]):
            temp2 = array[height - 1][j]
            for l in range(height-1, -1, -1):
                array[l][j] = array[l-1][j]
            array[0][j] = temp2

for i in range(height):
    alpha = 0
    for j in range(width):
        alpha = ((alpha % 2) + (array[i][j] % 2)) % 2
    if(alpha == 0):
        for k in range(KR[i]):
            temp2 = array[i][0]
            for l in range(width - 1):
                array[i][l] = array[i][l+1]
            array[i][width - 1] = temp2
    else:
        for k in range(KR[i]):
            temp2 = array[i][width - 1]
            for l in range(width-1, -1, -1):
                array[i][l] = array[i][l-1]
            array[i][0] = temp2   

array1 = np.array(array, dtype=np.uint8)
new_image = Image.fromarray(array1)
new_image.save('C:\\Users\\Hp-user\\Desktop\\startups\\Image encrypt\\Python\\flower-decrypt.png')

               
