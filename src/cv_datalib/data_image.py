from PIL import Image

class DataImage:
    """
    DataImage is an internal representation of loaded dataset image.
    It represents a single image in the dataset together with its object annotations or segmentation information.

    It is then passed to the transformation pipeline, after which the whole dataset is exported to the output format.
    """

    def __init__(self, image_path: str, annotations: list, image_size: tuple = None):
        self.image_path = image_path
        self.annotations = annotations
        self.image_size = image_size


    def __str__(self):
        return f"DataImage(image_path={self.image_path}, image_size={self.image_size})"


    def __repr__(self):
        return self.__str__()

    def read_image(self):
        return Image.open(self.image_path)


    def filename(self):
        return self.image_path.split('/')[-1]


