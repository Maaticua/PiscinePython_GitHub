from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
    """Charge une image, affiche ses dimensions et retourne ses pixels en RGB."""
    if path.lower().endswith(('.jpg', '.jpeg')):
        try:   
            pic = Image.open(path)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {path}")
    
        try:
            pic_array = np.array(pic)
        except Exception as e:
            raise ValueError(f"Error converting image to numpy array: {e}")

        print(f"The shape of image is: {pic_array.shape}")

        return pic_array
    else:
        raise ValueError("Unsupported file format. Please provide a .jpg or .jpeg image.")
    