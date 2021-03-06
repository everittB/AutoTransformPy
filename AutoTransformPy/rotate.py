def rotate (image_path, num_images, max_rotation):
    """Returns an array of images of length num_images randomly rotated a random degree up to max_rotation

    Rotate takes the path to an image and generates randomly rotated images, the desired number
    of times. Each rotated image will not be rotated more than the maximum rotation
    angle provided. The rotation can be both clockwise or counter-clockwise.

    Inputs:
    -------
    image_path: string
        The file path of the image to be rotated.
    num_images: integer
        The number of rotated images to be returned.
    max_rotation: integer
        The maximum allowable rotation for any of the rotated images. Can be
        between 1 and 360.

    Returns:
    --------
    rotated_images: np.array
    """
