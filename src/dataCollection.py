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

  def get_neiboring_colors(self, img):
    cords = []
    for i in range(0,self.width):
      for j in range(0,self.height):
        pxl_color = img.getpixel((i,j))  
        direcs = {"up":(0,1), "down":(0,-1), "left":(1,0), "right":(-1,0)}

        for direc in direcs.items():
          label = direc[0]
          hor, vert = direc[1]
          try:
            pxl = img.getpixel((i+hor,j+vert))
            if pxl != pxl_color:
              cordinate = ((i + abs(i - (i + hor))),(j + abs(j - (j + vert))))
              cords.append(str(cordinate))
          except Exception as e:
            pass

    return tuple(set(cords))


  def replace_uncommon(self, repl_color=(200,200,200), perc_float=3):
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
  
  def get_cords_lst(self, img):
    lst = list()
    for i in self.get_neiboring_colors(img):
      cord = [int(j) for j in i.replace("(","").replace(")","").replace(" ","").split(",")]
      x_y = [cord[0],0]

      if self.height/2 > cord[1]:
        x_y[1] = abs(cord[1] -  self.height)
      else:
        x_y[1] =  abs(self.height - cord[1])

      lst.append(tuple(x_y))

    return lst

def main_process_get_cords(path, binP, rad, perc):
  myImage = imageManipulator(path)
  print(f"""
        Area: {myImage.pxl_area}\n
        Width: {myImage.width}\n
        Height = {myImage.height}\n
        Center = ({myImage.width/2},{myImage.height/2})
        """)
  myImage.changeTo_Bit(bin_pal=binP)
  myImage.denoiseImage(radius=rad)
  myImage.replace_uncommon(perc_float=perc)
  return myImage.get_cords_lst(myImage.currentImage)

if __name__ == "__main__":
  cords = main_process_get_cords("../Images/homer.jpg", 6, 7, 2.00) #path to image, bit change, radius of denoising, percent of uncommons to replace
