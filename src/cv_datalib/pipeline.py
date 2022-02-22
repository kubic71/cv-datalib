from cv_datalib.load import Loader
from cv_datalib.export import Exporter
from cv_datalib.dataset import Dataset, Split, Splitter
from cv_datalib.transform import Transform



class DataPipeline:
    def __init__(self, loader: Loader, splitter: Splitter, transform: Transform, exporter: Exporter):
        self.loader = loader
        self.splitter = splitter
        self.transform = transform
        self.exporter = exporter

    def run(self):

        # Loader
        dataset: Dataset = self.loader.load_dataset()

        # Train-test split (if applicable)
        #   - raw dataset will have one split 'raw', which will be splitted by Splitter into train and test splits
        #   - dataset, which already has splits, will pass through the splitter unchanged
        dataset = self.splitter.split_dataset(dataset)

        # transformation pipeline
        dataset.splits = map(self.transform.transform, dataset.splits)

        # export to the output format
        self.exporter.export(dataset)


if __name__ == "__main__":
    dummy_pipeline = DataPipeline(
        loader=Loader("/path/to/dataset"),
        splitter=Splitter(),
        transform=Transform(),
        exporter=Exporter()
            )

    dummy_pipeline.run()