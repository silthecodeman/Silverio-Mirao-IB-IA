from pick_bins import pickBin6, pickBin9
from denoising import get_average_color
from PIL import Image as openImage

class imageManipulator:
  
  def __init__(self, path):
    self.image = openImage.open(path).convert("RGB")
    self.width = self.image.size[0] 
    self.height = self.image.size[1]
    self.pxl_area = self.width * self.height
    self.currentImage = self.image

  def pixel_ratio(self, img):
    all_pixels = dict()

    for i in range(0,self.width):
      for j in range(0,self.height):
        pixel = str(img.getpixel((i,j)))
        if pixel not in all_pixels:
          all_pixels[pixel] = 1
        else:
          all_pixels[pixel] += 1

    #pprint.pprint(all_pixels, width=1)
    return all_pixels

  def replace_uncommon(self, repl_color=(100,64,0), perc_float=3):
    pixels_amt = self.pixel_ratio(self.currentImage)
    bad_pixels = dict()

    for i in pixels_amt:
      between_deci = str((pixels_amt[i] / (self.height * self.width)) * 100).split(".")
      percent = float(between_deci[0] + "." + between_deci[1][:2])

      if percent <= perc_float:
        bad_pixels[i] = pixels_amt[i]

    for i in range(0,self.width):
      for j in range(0,self.height):
        pxl_color = self.currentImage.getpixel((i,j))    
        if str(pxl_color) in bad_pixels:
          self.currentImage.putpixel((i,j),repl_color)

  def changeTo_Bit(self, bin_pal=9, show=False):

    pickBin = lambda x: None

    if bin_pal == 6:
      pickBin = pickBin6
    elif bin_pal == 9:
      pickBin = pickBin9

    for i in range(0,self.width):
      for j in range(0,self.height):
        pxl_color = self.currentImage.getpixel((i,j))
        new_pxl_color = (pickBin(pxl_color[0]), pickBin(pxl_color[1]), pickBin(pxl_color[2]))
        self.currentImage.putpixel((i,j),new_pxl_color)

  def denoiseImage(self, radius=5):

    newImage = self.image
    for i in range(0,self.width):
      for j in range(0,self.height):
        color = get_average_color(i,j,self.currentImage,self.width,self.height,radius)
        newImage.putpixel((i,j),color)
    self.currentImage = newImage
  

if __name__ == "__main__":
  myImage = imageManipulator('../Images/homer.jpg')
  print(myImage.height * myImage.width)
  myImage.changeTo_Bit(bin_pal=6)
  myImage.denoiseImage(radius=5)
  myImage.replace_uncommon(perc_float=3.00)
  myImage.currentImage.show()
