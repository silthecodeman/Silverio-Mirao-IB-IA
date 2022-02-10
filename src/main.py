from dataCollection import main_process_get_cords
import matplotlib.pyplot as plt
import time
def seperate_cords(cords):
  used = list()
  groups = list()
  
  return groups

def show_values(cords):
  x_val = [x[0] for x in cords]
  y_val = [x[1] for x in cords]

  plt.scatter(x_val,y_val)
  plt.show()    

if __name__ == "__main__":
  cords = main_process_get_cords("../Images/scoobydoo.png", 6, 7, 2.00) #path to image, bit change (6,9), radius of denoising (7,5,3), percent of uncommons to replace
  show_values(cords)
  #print('seperation started')
  #print(f'length of cords: {len(cords)}')
  #print(seperate_cords(cords))