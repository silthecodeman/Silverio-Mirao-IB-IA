def get_average_color(x,y,currentImage,width,height,rad):
      tups = list()
      if rad == 7:
          tups = [a for b in [
                [(x-i,y+3) for i in range(-1,2)],
                [(x-i,y+2) for i in range(-2,3)],
                [(x-i,y+1) for i in range(-3,4)],
                [(x-i,y) for i in range(-3,4)],
                [(x-i,y-1) for i in range(-3,4)],
                [(x-i,y-2) for i in range(-2,3)],
                [(x-i,y-3) for i in range(-1,2)]
                ] for a in b]
      elif rad == 5:
        tups = [a for b in [
                [(x-i,y+2) for i in range(-1,2)],
                [(x-i,y+1) for i in range(-2,3)],
                [(x-i,y) for i in range(-2,3)],
                [(x-i,y-1) for i in range(-2,3)],
                [(x-i,y-2) for i in range(-1,2)]
                ] for a in b]
      elif rad == 3:
        tups = [a for b in [
                [(x-i,y+1) for i in range(-1,2)],
                [(x-i,y) for i in range(-1,2)],
                [(x-i,y-1) for i in range(-1,2)]
        ] for a in b]
      else:
        print("unsupported rad input")
        exit()

      badtups = list()

      for tup in tups:
        if tup[0] < 0 or tup[0] > width or tup[1] < 0 or tup[1] > height:
          badtups.append(tup)

      tups = [i for i in tups if i not in badtups]
      colors = dict()

      for tup in tups:
        color = str()
        try:
          color = str(currentImage.getpixel(tup))
        except:
          pass
        if color not in colors:
          colors[color] = 1
        else:
          colors[color] += 1

      best_color = ["", 0]
      for color in colors:
        if colors[color] > best_color[1] and color != "":
          best_color = [color, colors[color]]

      final_tup = tuple([int(i) for i in best_color[0].replace("(","").replace(")","").split(", ")])
      return final_tup