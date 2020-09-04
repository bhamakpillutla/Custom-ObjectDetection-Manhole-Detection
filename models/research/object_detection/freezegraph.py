import tensorflow as tf
import os
from tensorflow.python.tools import freeze_graph

# From tensorflow/models/research/  run this:
#protoc object_detection/protos/*.proto --python_out=.
# From tensorflow/models/research/
#export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
#MAKE SURE TO DOWNLOAD TENSORFLOW 1.4 with pip install tensorflow==1.4

sess=tf.Session()   
sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)) 
#First let's load meta graph and restore weights
saver = tf.train.import_meta_graph('C:/tensorflow1/models/research/object_detection/inference_graph/model.ckpt.meta')
tf.reset_default_graph()
saver.restore(sess,tf.train.latest_checkpoint('C:/tensorflow1/models/research/object_detection/training/'))
tf.train.write_graph(sess.graph_def, 'C:/tensorflow1/models/research/object_detection/inference_graph/','frozen_inference_graph.pb')


freeze_graph.freeze_graph('C:/tensorflow1/models/research/object_detection/inference_graph/frozen_inference_graph.pb',
              input_binary = False,
              input_checkpoint = 'C:/tensorflow1/models/research/object_detection/training/model.ckpt-1682',
              output_node_names = "num_detections,detection_boxes,detection_scores,detection_classes",
              #output_node_names = "num_detections,detection_boxes,detection_scores,detection_classes",
              output_graph = 'C:/tensorflow1/models/research/object_detection/tflite/newbytes1.4.bytes',
              clear_devices = True, initializer_nodes = "",input_saver = "",
              restore_op_name = "save/restore_all", filename_tensor_name = "save/Const:0")


