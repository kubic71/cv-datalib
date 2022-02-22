from cv_datalib.image import DataImage
import pandas as pd
from typing import List

class Split:
    def __init__(self, name: str, images: List[DataImage]):
        self.name = name
        self.images = images

    def __getitem__(self, index: int) -> DataImage:
        return self.images[index]

    def add_image(self, image: DataImage) -> None:
        self.images.append(image)

    def __len__(self) -> int:
        return len(self.images)


class Dataset:
    def __init__(self, splits: List[Split]):
        self.splits = splits


class Splitter:
    def __init__(self):
        pass

    def split_dataset(self, dataset: Dataset) -> Dataset:
        # Not implemented yet
        return dataset