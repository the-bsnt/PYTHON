from PIL import Image


def compress_image(input_image_path, output_image_path, quality):
    """
    Compress a JPG image to a specified quality level.

    :param input_image_path: Path to the input JPG image.
    :param output_image_path: Path where the compressed image will be saved.
    :param quality: The quality level of the output image (1-100).
    """
    # Open an image file
    with Image.open(input_image_path) as img:
        # Save the image with the specified quality
        img.save(output_image_path, "JPEG", quality=quality)


# Example usage
input_image_path = "sumit12.jpg"
output_image_path = "images/sumit_basnet_transcript12.jpg"
quality = 30  # Adjust the quality (1-100), lower means more compression
compress_image(input_image_path, output_image_path, quality)
