
# Manhole Detection

This project identifies manholes- open and closed, persons and cars.

![Alt Text](https://github.com/bhamakpillutla/Custom-ObjectDetection-Manhole-Detection/blob/master/models/research/object_detection/Output/capture2122.JPG)


## Commands
## Create the tensorflow environment
```bash
C:\> conda create -n tensorflowone pip python=3.5
C:\> activate tensorflow1
```

## Install Packages
``` bash
* (tensorflowone) C:\>python -m pip install --upgrade pip
* (tensorflowone):\> pip install --ignore-installed --upgrade tensorflow-gpu
* (tensorflowone)C:\> conda install -c anaconda protobuf
* (tensorflowone)C:\> pip install pillow
* (tensorflowone)C:\> pip install lxml
* (tensorflowone)C:\> pip install Cython
* (tensorflowone)C:\> pip install contextlib2
* (tensorflowone)C:\> pip install jupyter
*(tensorflowone)C:\> pip install matplotlib
* (tensorflowone)C:\> pip install pandas
* (tensorflowone)C:\> pip install opencv-python
``` 

## Create a folder with name tensorflow1 and paste the contents of this repository there.

```bash
(tensorflowone) C:\> set PYTHONPATH=C:\tensorflow1\models;C:\tensorflow1\models\research;C:\tensorflow1\models\research\slim
``` 
(Note: Every time the "tensorflowone" virtual environment is exited, the PYTHONPATH variable is reset and needs to be set up again. You can use "echo %PYTHONPATH% to see if it has been set or not.)


```bash
(tensorflowone) C:\tensorflow1\models\research> protoc --python_out=. .\object_detection\protos\anchor_generator.proto .\object_detection\protos\argmax_matcher.proto .\object_detection\protos\bipartite_matcher.proto .\object_detection\protos\box_coder.proto .\object_detection\protos\box_predictor.proto .\object_detection\protos\eval.proto .\object_detection\protos\faster_rcnn.proto .\object_detection\protos\faster_rcnn_box_coder.proto .\object_detection\protos\grid_anchor_generator.proto .\object_detection\protos\hyperparams.proto .\object_detection\protos\image_resizer.proto .\object_detection\protos\input_reader.proto .\object_detection\protos\losses.proto .\object_detection\protos\matcher.proto .\object_detection\protos\mean_stddev_box_coder.proto .\object_detection\protos\model.proto .\object_detection\protos\optimizer.proto .\object_detection\protos\pipeline.proto .\object_detection\protos\post_processing.proto .\object_detection\protos\preprocessor.proto .\object_detection\protos\region_similarity_calculator.proto .\object_detection\protos\square_box_coder.proto .\object_detection\protos\ssd.proto .\object_detection\protos\ssd_anchor_generator.proto .\object_detection\protos\string_int_label_map.proto .\object_detection\protos\train.proto .\object_detection\protos\keypoint_box_coder.proto .\object_detection\protos\multiscale_anchor_generator.proto .\object_detection\protos\graph_rewriter.proto .\object_detection\protos\calibration.proto .\object_detection\protos\flexible_grid_anchor_generator.proto


(tensorflowone) C:\tensorflow1\models\research> python setup.py build

(tensorflowone) C:\tensorflow1\models\research> python setup.py install
```
## xml to csv file
```bash
(tensorflowone)C:\tensorflow1\models\research\object_detection> python xml_to_csv.py
```

## Generate tf records
``` bash
python generate_tfrecord.py --csv_input=images\train_labels.csv --image_dir=images\train --output_path=train.record

python generate_tfrecord.py --csv_input=images\test_labels.csv --image_dir=images\test --output_path=test.record
```
## Model Training
``` bash
python train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/faster_rcnn_inception_v2_pets.config
```

## Generate the model file
``` bash
python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/faster_rcnn_inception_v2_pets.config --trained_checkpoint_prefix training/model.ckpt-XXXX --output_directory inference_graph
```


This project runs on tensorflow-gpu ==1.8 and protobuf == 3.7.0 without any errors and uses Tensorflow Object Detection API.
