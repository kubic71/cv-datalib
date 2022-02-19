# Computer vision dataset handling library

## Vision
- Loaders for different dataset formats
    - connector to Azure blob store
- General representation of  the Dataset
    - Images, Bounding boxes, Polygons, categories
- Transforms, augmentations on the dataset
    - Can be custom (like collage generation)
- Exporters to different image and annotation formats
- Visualization and dataset exploration
    - Voxel51

## Pipeline
```python
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
```
