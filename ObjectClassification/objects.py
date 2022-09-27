import numpy as np
import cv2
import os
import tensorflow as tf
from ObjectClassification.detectedObject import detectedObject
from ObjectClassification.object_detection.utils import label_map_util
from ObjectClassification.object_detection.utils import visualization_utils as vis_utils
 
class objects:
    def __init__(self ,filename ):
        self.PATH_TO_CKPT = 'ObjectClassification/ssdlite_mobilenet_v2_coco/frozen_inference_graph.pb'
        self.PATH_TO_LABELS = os.path.join('ObjectClassification/data', 'mscoco_label_map.pbtxt') 
        self.NUM_CLASSES = 90 
        self.IMAGE_SIZE = (12, 8) 
        self.filename = filename

    def load_model(self):
        fileAlreadyExists = os.path.isfile(self.PATH_TO_CKPT) 
        if not fileAlreadyExists:
            print('Model does not exsist !')
            exit("Error")
        print('Loading model')
        self.detection_graph = tf.Graph() 
        with self.detection_graph.as_default(): 
            od_graph_def = tf.compat.v1.GraphDef()
            with tf.io.gfile.GFile(self.PATH_TO_CKPT, 'rb') as fid: 
                serialized_graph = fid.read() 
                od_graph_def.ParseFromString(serialized_graph) 
                tf.import_graph_def(od_graph_def, name='')
        label_map = label_map_util.load_labelmap(self.PATH_TO_LABELS) 
        categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=self.NUM_CLASSES, use_display_name=True) 
        self.category_index = label_map_util.create_category_index(categories)
        print('Finish Load Graph..')
    
    def predict(self):
        self.detection_graph.as_default()
        sess =tf.compat.v1.Session(graph=self.detection_graph)
        frame_i = cv2.imread( self.filename)
        frame = cv2.resize(frame_i,[640,640])
        image_np_expanded = np.expand_dims(frame, axis=0) 
        image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0') 
        detection_boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0') 
        detection_scores = self.detection_graph.get_tensor_by_name('detection_scores:0') 
        detection_classes = self.detection_graph.get_tensor_by_name('detection_classes:0') 
        num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')
        
        (boxes, scores, classes, num) = sess.run( 
            [detection_boxes, detection_scores, detection_classes, num_detections], 
            feed_dict={image_tensor: image_np_expanded}) 

        return self.detectObjectAndaccuracy(boxes, classes, scores)
        
    def detectObjectAndaccuracy(self ,boxes, classes, scores):
        objects = []
        detected = classes[0]
        for idx, x in enumerate(detected):
            if(boxes[0][idx][0] != 0.0):
                objects.append(detectedObject(self.category_index[detected[idx]]['name'],scores[0][idx]))
        return objects

    

