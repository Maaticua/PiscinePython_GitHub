from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def main():
    """Charge une image, la "zoom" (slice) et l'affiche"""
    try:
        img = ft_load("animal.jpeg")
        zoom_img = img[200:600, 400:800, 0:1]

        plt.imshow(zoom_img)
        plt.show()

    except Exception as e:
        print(e)
    

if __name__ == "__main__":
    main()
