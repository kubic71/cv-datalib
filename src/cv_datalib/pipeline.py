class DataPipeline:
    def __init__(self, pipeline_config: PipelineConfig):
        self.pipeline_config = pipeline_config

    def run(self):
        # Dataset
        #    splits: List[Split]
        #    metadata: DatasetMetadata

        # Split
        #    name: str
        #    images: List[DataImage]


        # Pipeline config specifies things like transforms, input and output dataset formats, train-test split parameters, etc.
        pipeline_config = config.load_pipeline_config()

        # Loader
        loader = Loader(pipeline_config)
        dataset: Dataset = loader.load_dataset()

        # Train-test split (if applicable)
        #   - raw dataset will have one split 'raw', which will be splitted by Splitter into train and test splits
        #   - dataset, which already has splits, will pass through the splitter unchanged
        splitter = Splitter(dataset, pipeline_config)
        dataset = splitter.split_dataset(dataset)

        # transformation pipeline
        transform = Transform(pipeline_config)
        dataset.splits = map(transform.transform, dataset.splits)

        # export to the output format
        exporter = Exporter(pipeline_config)
        exporter.export(dataset)

