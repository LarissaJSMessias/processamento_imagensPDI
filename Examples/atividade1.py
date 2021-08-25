
import numpy as np
from PIL import Image  
from numpy import asarray
  
def main():
    # Open image
    image = Image.open('images/lena.jpg')
    print(image.format)
    print(image.size)
    print(image.mode)
    print(image.bits)
    print(image.getextrema())
    # convert image to numpy array    
    npImage = np.array(image) 
    print(type(npImage ))
    # summarize shape
    print(npImage.shape)

    # values os a windows 5 X 5 (printa os valores normais da imagem)
    print(npImage[0:5, 0:5])

    # inverte os pixels
    npImage =  (255 - npImage);

    # values os a windows 5 X 5  (printar com os pixels invertido)
    print(npImage[0:5, 0:5])


    #Convert ndarray image to Pillow image
    image2 = Image.fromarray(npImage)
    image2.show()
    image2.save("imageminvertidaLENA.jpg")

    # create the histogram
    histogram, bin_edges = np.histogram(npImage, bins=256, range=(0, 255))
    print(histogram.shape)

if __name__ == "__main__":
    main()