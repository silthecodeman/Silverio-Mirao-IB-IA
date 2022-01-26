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

def pickBin6(x):
    if x < 43:
        return 0
    elif x >= 43 and x < 128:
        return 85
    elif x >= 128 and x < 213:
        return 171
    else:
        return 255