# SimVS Lighting Dataset Loader

This repository provides a dataloader for the SimVS inconsistent lighting dataset, designed to help researchers experiment on 3D generation from sparse and inconsistent images.

## Scene Previews

<div align="center">
  <table>
    <tr>
      <td align="center"><b>Bear</b></td>
      <td align="center"><b>Boop</b></td>
      <td align="center"><b>Chair</b></td>
      <td align="center"><b>Chess</b></td>
      <td align="center"><b>Statue</b></td>
    </tr>
    <tr>
      <td align="center"><img src="scene_gifs/bear.gif" width="160"/></td>
      <td align="center"><img src="scene_gifs/boop.gif" width="160"/></td>
      <td align="center"><img src="scene_gifs/chair.gif" width="160"/></td>
      <td align="center"><img src="scene_gifs/chess.gif" width="160"/></td>
      <td align="center"><img src="scene_gifs/statue.gif" width="160"/></td>
    </tr>
  </table>
</div>

## SimVS Paper

This dataset is part of the research presented in:

**SimVS: Simulating World Inconsistencies for Robust View Synthesis**

[Project Page](https://alextrevithick.com/simvs/) | CVPR 2025

SimVS addresses the challenge of real-world 3D reconstruction where scenes often contain inconsistencies - objects move, and lighting changes over time. The method uses generative augmentation to simulate inconsistencies and trains a generative model to produce consistent multiview images from sparse, inconsistent inputs. This dataset specifically focuses on scenes with varying illumination conditions.

## Installation

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Dataset

The SimVS dataset is available for download here:
[https://drive.google.com/file/d/1MiqzN4YAqUUKHnftYKOi8iV4PzoN9c_J/view?usp=sharing](https://drive.google.com/file/d/1MiqzN4YAqUUKHnftYKOi8iV4PzoN9c_J/view?usp=sharing)

### Dataset Description

This dataset was created specifically to address the lack of existing datasets with multiple illumination conditions and ground truth images under consistent lighting. SimVS provides:

- 5 real-world scenes, each captured under 3 separate lighting conditions
- For each scene, 3 monocular videos taken with approximately the same camera trajectory but different lighting
- Camera pose information for all images, jointly calculated using [Hierarchical Localization](https://github.com/cvg/Hierarchical-Localization)

Note that some scenes in the dataset are not distortion-corrected.

### Dataset Structure

Each scene in the dataset follows the same directory structure:

```
scene_name/
├── images/         # All images from all lighting conditions
├── sparse/         # 3D reconstruction information extracted by COLMAP
├── train_list.txt  # List of image filenames to use for training
└── test_list.txt   # List of image filenames to use for testing
```

Key components:
- `images/`: Contains all captured images across different lighting conditions
- `sparse/`: Contains the COLMAP reconstruction data including camera parameters, points, and image registrations
- `train_list.txt`: Text file listing the filenames of images designated for training
- `test_list.txt`: Text file listing the filenames of images designated for testing/evaluation

The dataloader uses these files to identify which images belong to which split and to load the appropriate camera parameters and image data.

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

This dataset is compatible with the original [WildGaussians](https://github.com/jkulhanek/wild-gaussians) training code, allowing you to seamlessly integrate it into the original framework for experiments with inconsistent lighting conditions.

## Implementation Details

This dataloader is a minimal adaptation from the wonderful WildGaussians repository:
[https://github.com/jkulhanek/wild-gaussians](https://github.com/jkulhanek/wild-gaussians)

Please refer to the original repository for the full WildGaussians method, including training, rendering, and evaluation code.

**Authors of the original work:** Jonas Kulhanek, Songyou Peng, Zuzana Kukelova, Marc Pollefeys, Torsten Sattler

**Paper:** [WildGaussians: 3D Gaussian Splatting in the Wild (NeurIPS 2024)](https://arxiv.org/pdf/2407.08447)

## Citation

If you use this dataset in your research, please cite:

```
@article{trevithick2024simvs,
  title={SimVS: Simulating World Inconsistencies for Robust View Synthesis},
  author={Alex Trevithick and Roni Paiss and Philipp Henzler and Dor Verbin and Rundi Wu and Hadi Alzayer and Ruiqi Gao and Ben Poole and Jonathan T. Barron and Aleksander Holynski and Ravi Ramamoorthi and Pratul P. Srinivasan},
  journal={arXiv},
  year={2024}
}
