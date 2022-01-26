from PIL import Image as openImage

if __name__ == "__main__":
    image = openImage.open('colorScale.png')

    width = image.size[0] 
    height = image.size[1]

    myPixels = list()
    myValues = list()

    for i in range(0,width):
        for j in range(0,height):
            pxl = image.getpixel((i,j))

            for i in pxl:
                if i not in myValues:
                    myValues.append(i)
            if pxl not in myPixels:
              myPixels.append(pxl)

    print(myValues)
    for i in range(len(myValues)-1):
        if i == 0:
            continue
        print((myValues[i]-myValues[i-1])/2)