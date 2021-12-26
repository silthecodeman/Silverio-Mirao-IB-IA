import PIL
from PIL import Image as openImage
class imageManipulator:
  
  def __init__(self, path):
    self.image = openImage.open(path).convert("RGB")
    self.width = self.image.size[0] 
    self.height = self.image.size[1]
    self.currentImage = self.image

  def newWhiteImage(self):
    newImage = self.image
    for i in range(0,self.width):
      for j in range(0,self.height):
        newImage.putpixel((i,j),(255,255,255))
    return newImage

  def changeTo_9Bit(self, show=False):
    
    def pickBin9(x):
      if x < 18:
        return 0
      elif x >= 18 and x < 54:
        return 36
      elif x >= 54 and x < 90:
        return 72
      elif x >= 90 and x < 127:
        return 109
      elif x >= 127 and x < 163:
        return 145
      elif x >= 163 and x < 200:
        return 182
      elif x >= 200 and x < 236:
        return 218
      else:
        return 255

    for i in range(0,self.width):
      for j in range(0,self.height):
        pxl_color = self.currentImage.getpixel((i,j))
        new_pxl_color = (pickBin9(pxl_color[0]), pickBin9(pxl_color[1]), pickBin9(pxl_color[2]))
        self.currentImage.putpixel((i,j),new_pxl_color)

  def denoiseImage(self):
    def mostFrequentTuple(lst):
      lst = [str(i) for i in lst]
      counter = 0
      num = lst[0]
      for i in lst:
          curr_frequency = lst.count(i)
          if(curr_frequency> counter):
              counter = curr_frequency
              num = i
  
      return tuple(num)



    sampleArea = 2
    for i in range(0,self.width):
      for j in range(0,self.height):
        tuple_list = list()
        for x in range(-sampleArea,sampleArea+1):
          for y in range(-sampleArea,sampleArea+1):
            if x >= 0 and y >= 0 and x <= self.width and y <= self.height:
              tuple_list.append(self.currentImage.getpixel((i,j)))
        new_pxl_color = mostFrequentTuple(tuple_list)
        self.currentImage.putpixel((i,j),new_pxl_color)

if __name__ == "__main__":
  myImage = imageManipulator('Images/spongebob.jpg')
  myImage.changeTo_9Bit()
  myImage.currentImage.show()