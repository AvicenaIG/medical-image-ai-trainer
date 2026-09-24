# medical-image-ai-trainer — Radiology-Ready Deep Learning for Medical Imaging

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)]()
[![Language](https://img.shields.io/badge/language-Python-blue.svg)]()

A Python framework for training deep learning models on MRI and CT scans — medical image sampling, augmentation, and model fitting.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#license)
- [License](#license)

## Features

- **Compose** medical imaging datasets from DICOM-derived NIfTI files, spreadsheet columns (e.g., clinical scores), folder names, or in-memory arrays using `Dataset`, `ImageReader`, `ColumnReader`, `FolderNameReader`, `ComposeReader`, and `MemoryReader`.
- **Sample** volumetric scans into 2D slices, patches, or blocks for slice-based lesion segmentation and patch-based tumor classification via `SliceSampler`, `PatchSampler`, `BlockSampler`, and `SlicePatchSampler`.
- **Augment** radiological images with intensity and spatial transforms — `StandardNormalize`, `BiasCorrection`, `Clip`, `RandomRotate`, `RandomFlip`, `RandomZoom`, and more — to improve model generalization across scanners and cohorts.
- **Fetch** reference neural architectures and pretrained networks for tasks like brain segmentation with `fetch_architecture`, `list_architectures`, and `fetch_pretrained`.
- **Train** and **evaluate** models with a framework-agnostic `Trainer` (with `TorchTrainer` for PyTorch backends) on your imaging cohorts.
- **Interpret** model predictions with occlusion-based saliency mapping using `OcclusionExplainer` to visualize which anatomical regions drive a diagnosis.

## Installation

```bash
git clone https://github.com/AvicenaIG/medical-image-ai-trainer.git medical-image-ai-trainer
cd medical-image-ai-trainer
medical-image-ai-trainer -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

The [ants](https://www.github.com/AvicenaIG/antspy) medical-image-ai-trainer package is a key dependency for efficiently reading, operating on, and visualizing medical images. You can use keras (tf.keras or keras3), tensorflow, or pytorch as the backend for your models.

## Quick Start

Train a semantic segmentation model for brain anatomy (FreeSurfer-style aparc+aseg parcellation) from a BIDS-style neuroimaging dataset:

```medical-image-ai-trainer
import medical-image-ai-trainer as nt
from medical-image-ai-trainer import readers, transforms

# create dataset from folder of images + participants file
dataset = nt.Dataset(
    inputs=readers.ImageReader('sub-*/anat/*_T1w.nii.gz'),
    outputs=readers.ImageReader('sub-*/anat/*_aparc+aseg.nii.gz'),
    transforms={
        'inputs': transforms.StandardNormalize(),
        ('inputs', 'outputs'): transforms.Resample((64,64,64))
    },
    base_dir='~/desktop/ds004711/'
)

# create loader with per-slice sampling and random augmentation
loader = nt.Loader(
    dataset,
    images_per_batch=4,
    sampler=nt.SliceSampler(batch_size=32, axis=2),
    transforms={
        'inputs': transforms.RandomFlip(axis=1)
    }
)

# create model from architecture
arch_fn = nt.fetch_architecture('unet', dim=2)
model = arch_fn(input_image_size=(64,64,1), mode='segmentation')

# create trainer and fit model
trainer = nt.Trainer(model, task='segmentation')
trainer.fit(loader, epochs=100)
```

## Usage

### Predicting cognitive scores from structural MRI

Use a `ColumnReader` to pull a continuous clinical variable (e.g., age or cognitive test score) from a participants file and regress it from T1-weighted volumes:

```medical-image-ai-trainer
import medical-image-ai-trainer as nt
from medical-image-ai-trainer import readers, transforms

dataset = nt.Dataset(
    inputs=readers.ImageReader('sub-*/anat/*_T1w.nii.gz',
                               transforms=transforms.StandardNormalize()),
    outputs=readers.ColumnReader('age', base_dir='~/desktop/ds004711/'),
    base_dir='~/desktop/ds004711/'
)

loader = nt.Loader(dataset, images_per_batch=8)

arch_fn = nt.fetch_architecture('vgg', dim=3)
model = arch_fn(input_image_size=(128,128,128), mode='regression')

trainer = nt.Trainer(model, task='regression')
trainer.fit(loader, epochs=50)

predictor = nt.Predictor(model)
predictions = predictor.predict(loader)
```

### Interpreting a segmentation model with occlusion

```medical-image-ai-trainer
import medical-image-ai-trainer as nt

explainer = nt.OcclusionExplainer(model)
saliency = explainer.explain(loader)  # highlight regions driving predictions
```

## Configuration

No environment variables or configuration files are detected in this codebase; all options are passed directly as constructor arguments (e.g., `Dataset`, `Loader`, `Trainer`).

## Contributing

Contributions are welcome — whether fixing bugs, adding readers or transforms for new imaging modalities, or improving documentation. Please open an issue describing the clinical or technical motivation before submitting a pull request, and include tests covering your changes.

## License

Released under the MIT License. Copyright © 2026 medical-image-ai-trainer contributors.