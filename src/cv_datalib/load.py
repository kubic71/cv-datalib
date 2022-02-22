import numpy as np
from cv_datalib.dataset import Dataset, Split
from cv_datalib.image import DataImage
from cv_datalib.annotation import BboxAnnotation
from typing import Dict, List



class Loader:
    def __init__(self, path: str) -> None:
        self.path = path

    def load_dataset(self) -> Dataset:
        raise NotImplementedError(f"load({self.path}): Not implemented yet")




def download_aml_dataset(subscription_id: str, resource_group: str, workspace_name: str, dataset_name: str, dest_path: str = "./") -> List[Dict]:
    # azureml-core of version 1.0.72 or higher is required
    # azureml-dataprep[pandas] of version 1.1.34 or higher is required
    from azureml.core import Workspace, Dataset
    from os import path
    from cv_datalib.dataset import AmlDataset
    workspace = Workspace(subscription_id, resource_group, workspace_name)

    dataset = Dataset.get_by_name(workspace, name=dataset_name)
    # download the dataset to a local path
    dataset.download("image_url", dest_path, overwrite=True)
    df = dataset.to_pandas_dataframe()

    dataset = []

    for index, row in df.iterrows():
        image_path = path.join(dest_path, str(row["image_url"]))
        annots: np.ndarray = row["label"]
        dataset.append({"image_path": image_path, "annotations": annots, "image_width": row["image_width"], "image_height": row["image_height"]})

    return dataset


class AzureLocalLoader(Loader):
    def __init__(self, dataset: List[Dict]):
        # dataset is the output of download_aml_dataset
        # each element of dataset is a dict with the following keys:
        #  image_path - path to the image
        #  annotations - list of annotations, each element is a dict with the following keys:
        #     label - label name
        #     topX - top left x coordinate
        #     topY - top left y coordinate
        #     bottomX - bottom x coordinate
        #     bottomY -  bottom y coordinate

        self.dataset = dataset

    def load_dataset(self) -> Dataset:
        # parse the self.dataset into a Dataset object with only one split "raw"
        # convert the annotations to BboxAnnotation objects

        split = Split("raw", [])

        for image in self.dataset:

            annots = []
            for bbox_annot in image["annotations"]:
                x, y = bbox_annot["topX"], bbox_annot["topY"]
                w, h = bbox_annot["bottomX"] - x, bbox_annot["bottomY"] - y

                annots.append(BboxAnnotation(bbox_annot["label"], x, y, w, h))

            split.add_image(DataImage(image_path=image["image_path"], annotations=annots, image_size=(image["image_width"], image["image_height"])))

        return Dataset([split])