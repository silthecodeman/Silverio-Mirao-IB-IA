import PIL
from PIL import Image


if __name__ == "__main__":
  img = Image.open('Images/homer.jpg').convert('L')
  width = img.size[0] 
  height = img.size[1]
  for i in range(0,width):
        for j in range(0,height):
            data = img.getpixel((i,j))
            if data < 50:
                img.putpixel((i,j),(0))
            if data >= 50:
                img.putpixel((i,j),(255))
  img.save('dots.jpg')