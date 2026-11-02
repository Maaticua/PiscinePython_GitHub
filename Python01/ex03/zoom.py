from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    """Charge une image, la "zoom" (slice) et l'affiche"""
    try:
        img = ft_load("animal.jpeg")
        print(img)

        zoom_img = img[200:600, 400:800, 0:1]

        print(f"New shape after slicing: {zoom_img.shape}")
        print(zoom_img)

        plt.imshow(zoom_img, cmap="gray")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
