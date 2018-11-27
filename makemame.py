from PIL import Image
import random
import os

def make(im):
    template = Image.open("template.jpg")
    im1 = Image.open('memes/' + random.choice(os.listdir('memes/'))).resize((350,350))
    if im == "":
        im2 = Image.open('memes/' + random.choice(os.listdir('memes/'))).resize((350,350))
    else:
        im2 = Image.open(im).resize((350,350))
    region1 = (50,100)
    region2 = (450, 100)
    template.paste(im1, region1)
    template.paste(im2, region2)
    template.save("badmeme.png")