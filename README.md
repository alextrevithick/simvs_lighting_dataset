# SimVS Lighting Dataset Loader

This code is still in an experimental state.

This repository provides a dataloader for the SimVS inconsistent lighting dataset, designed to help researchers experiment on 3D generation from sparse and inconsistent images. 

## Dataset

The SimVS dataset is available for download here:
[https://drive.google.com/file/d/1MiqzN4YAqUUKHnftYKOi8iV4PzoN9c_J/view?usp=sharing](https://drive.google.com/file/d/1MiqzN4YAqUUKHnftYKOi8iV4PzoN9c_J/view?usp=sharing)

### Dataset Description

This dataset was created specifically to address the lack of existing datasets with multiple illumination conditions and ground truth images under consistent lighting. SimVS provides:

- 5 real-world scenes, each captured under 3 separate lighting conditions
- For each scene, 3 monocular videos taken with approximately the same camera trajectory but different lighting
- Camera pose information for all images, jointly calculated using [Hierarchical Localization](https://github.com/cvg/Hierarchical-Localization)

Note that some scenes in the dataset are not distortion-corrected.

### Intended Use

The dataset is designed for evaluating novel-view synthesis methods under inconsistent lighting. The typical experimental setup involves:

1. Using 3 frames (one from each inconsistent video) as input
2. Rendering novel views that match the lighting condition of one of the videos
3. Evaluating the results against held-out ground truth images from that lighting condition

The dataset contains multiple scenes processed with Colmap, including camera parameters and multi-view images.

## Usage

The main entry point is `colmap_dataloader.py`, which demonstrates how to load a scene from the dataset.

For example, to load the chess scene from the SimVS inconsistent lighting dataset:

```bash
python colmap_dataloader.py --data /path/to/simvs/dataset/chess --split train --load-features
```

The `--load-features` flag is required to actually load the image data rather than just the metadata.

This script utilizes functions from the `dataloader_helpers` directory to parse Colmap outputs and load image data.

## Implementation Details

This dataloader is a minimal adaptation from the wonderful WildGaussians repository:
[https://github.com/jkulhanek/wild-gaussians](https://github.com/jkulhanek/wild-gaussians)

Please refer to the original repository for the full WildGaussians method, including training, rendering, and evaluation code.

**Authors of the original work:** Jonas Kulhanek, Songyou Peng, Zuzana Kukelova, Marc Pollefeys, Torsten Sattler

**Paper:** [WildGaussians: 3D Gaussian Splatting in the Wild (NeurIPS 2024)](https://arxiv.org/pdf/2407.08447)
