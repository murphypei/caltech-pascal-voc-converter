Caltech Pedestrian Dataset Converter to VOC2007 Dataset format
============================

# Requirements

- OpenCV 2.4.13
- Python 2.7+, 3.4+, 3.5+
- NumPy 1.10+
- SciPy 0.16+

# Caltech Pedestrian Dataset Example

1. Download caltech dataset and convert it to images and annotations.json

```
$ ./shells/download.sh
$ ./caltech/convert_annotations.py
$ ./caltech/convert_seqs.py
```

Each `.seq` movie is separated into `.png` images. Each image's filename is consisted of `{set**}_{V***}_{frame_num}.png`. According to [the official site](http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/), `set06`~`set10` are for test dataset, while the rest are for training dataset.

(Number of objects: 346621)

2. Draw Bounding Boxes for test

you can draw bounding boxes in the images and get a video for checking

```
$ ./tests/test_plot_annotations.py
```
