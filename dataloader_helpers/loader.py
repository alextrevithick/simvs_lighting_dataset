from functools import partial
from typing import FrozenSet, Optional
import click

from .datasets import load_dataset, DatasetFeature, Dataset
from .datasets.colmap import load_colmap_dataset
from .evaluation import EvaluationProtocol, DefaultEvaluationProtocol

DEFAULT_FEATURES: FrozenSet[DatasetFeature] = frozenset({"color", "points3D_xyz"})

def load_colmap_data(
    data_path: str,
    split: str,
    features: FrozenSet[DatasetFeature] = DEFAULT_FEATURES,
    load_features: bool = False,
    evaluation_protocol: EvaluationProtocol = DefaultEvaluationProtocol(),
    images_path: str = "images",
) -> Dataset:
    """
    Loads a dataset processed with Colmap using the standard loader configuration.

    Args:
        data_path: Path to the root dataset directory.
        split: Dataset split to load ('train', 'test', etc.).
        features: Set of features required from the dataset. Defaults to {color, points3D_xyz}.
        load_features: Whether to load features immediately. Defaults to False.
        evaluation_protocol: The evaluation protocol to use.
        images_path: Relative path to the images directory within the data_path.

    Returns:
        The loaded dataset dictionary.
    """
    return load_dataset(
        data_path,
        split,
        features,
        load_features=load_features,
        load_dataset_fn=load_colmap_dataset,
        images_path=images_path,
        evaluation_protocol=evaluation_protocol.get_name(),
    )

@click.command()
@click.option("--data", "data_path", type=str, required=True, help="Path to the dataset directory.")
@click.option("--split", type=str, default="test", help="Dataset split to load (e.g., 'train', 'test').")
@click.option("--load-features", is_flag=True, default=False, help="Load features immediately.")
@click.option("--images-path", type=str, default="images", help="Relative path to images directory.")
def main(data_path: str, split: str, load_features: bool, images_path: str):
    """Loads a Colmap dataset and prints basic information."""
    print(f"Loading dataset from: {data_path}")
    print(f"Split: {split}, Load Features: {load_features}, Images Path: {images_path}")
    try:
        dataset = load_colmap_data(
            data_path=data_path,
            split=split,
            load_features=load_features,
            images_path=images_path,
            # Using default features and evaluation protocol
        )
        print("Dataset loaded successfully!")
        print(f"  Number of cameras: {len(dataset['cameras'])}")
        if "images" in dataset and dataset["images"]:
             print(f"  Number of images: {len(dataset['images'])}")
             print(f"  First image shape: {dataset['images'][0].shape}")
        if "points3D_xyz" in dataset and dataset["points3D_xyz"] is not None:
            print(f"  Number of 3D points: {len(dataset['points3D_xyz'])}")

    except Exception as e:
        print(f"Error loading dataset: {e}")

if __name__ == "__main__":
    main() # pylint: disable=no-value-for-parameter
