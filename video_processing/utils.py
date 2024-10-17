import os
from PIL import Image
import pyheif

def convert_to_jpg(image_path):
    """Converts an image to JPG format if it is not already a JPG, and deletes the original file."""
    
    if image_path.lower().endswith(".avif"):
        jpg_image_path = image_path.rsplit('.', 1)[0] + '.jpg'
        
        try:
            # Read the AVIF file using pyheif
            heif_file = pyheif.read(image_path)
            
            # Convert the AVIF file to a Pillow Image object
            image = Image.frombytes(
                heif_file.mode, 
                heif_file.size, 
                heif_file.data,
                "raw",
                heif_file.mode,
                heif_file.stride,
            )
            
            # Convert and save as JPG
            image = image.convert("RGB")
            image.save(jpg_image_path, "JPEG")
            
            # Remove the original AVIF file
            os.remove(image_path)
            print(f"Successfully converted and deleted image: {image_path}")
            return jpg_image_path
        except Exception as e:
            print(f"Failed to convert image: {e}")
            raise ValueError(f"Could not convert image: {image_path}")
    
    # For other image formats, handle them normally
    try:
        img = Image.open(image_path)
        if img.format != 'JPEG':
            jpg_image_path = image_path.rsplit('.', 1)[0] + '.jpg'
            img = img.convert('RGB')  # Convert to RGB for JPG
            img.save(jpg_image_path, 'JPEG')
            os.remove(image_path)
            return jpg_image_path
    except Exception as e:
        raise ValueError(f"Could not process image: {image_path}, Error: {e}")
    
    return image_path  # Return the original path if it's already a JPG
