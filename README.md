# Caltech Pedestrian Dataset Converter to VOC2007 format

## Requirements

- OpenCV 2.4.13
- Python 2.7+, 3.4+, 3.5+
- NumPy 1.10+
- SciPy 0.16+

## Usage (Caltech Pedestrian Dataset Example)

1. **Prepare dataset**

    Download caltech dataset and convert it to images and annotations.json.

    ```
    $ ./shells/download.sh
    $ ./caltech/convert_annotations.py
    $ ./caltech/convert_seqs.py
    ```

    Each `.seq` movie is separated into `.png` images. Each image's filename is consisted of `{set**}_{V***}_{frame_num}.png`. According to [the official site](http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/), `set06`~`set10` are for test dataset, while the rest are for training dataset.

    (Number of objects: 346621)

2. **Draw and Test**

    You can draw bounding boxes in the images and get a video for checking.

    ```
    $ ./tests/test_plot_annotations.py
    ```

3. **Create VOC2007 format dataset**

    Convert images to VOC2007 format dataset.

    ```
    $ ./voc/convert_to_voc.py [annotations.json] [images_path] [voc_path]
    ```

    * config your properties for VOC2007 annotations and train and test sets in `config.py`.
    * make voc_path dir empty is better.