def translate (image_path, num_images, max_translation):
    """Returns an array of images of length num_images randomly translated a random number of pixels up to max_rotation

    Translate takes the path to an image and generates randomly translated images, the desired number
    of times. Each translated image will not be translated more than the maximum distance provided.
    The translation can be in any direction.

    Inputs:
    -------
    image_path: string
        The file path of the image to be translated.
    num_images: integer
        The number of translated images to be returned.
    max_translation: integer
        The maximum distance in pixels that the image can be translated.

    Returns:
    --------
    translated_images: np.array
    """
