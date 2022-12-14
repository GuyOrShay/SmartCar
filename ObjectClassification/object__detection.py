import numpy as np
import cv2
import os,time
import tensorflow as tf
from ObjectClassification.object_detection.utils import label_map_util
from ObjectClassification.object_detection.utils import visualization_utils as vis_utils
from PIL import Image
import time

def test_tensor():
    # Init camera 
    cap = cv2.VideoCapture(0)
    cap.set(3,640) # set Width
    cap.set(4,480) # set Height

    # Init tf model
    MODEL_NAME = 'ObjectClassification/ssdlite_mobilenet_v2_coco' #fast
    PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb' 
    PATH_TO_LABELS = os.path.join('ObjectClassification/data', 'mscoco_label_map.pbtxt') 
    NUM_CLASSES = 90 
    IMAGE_SIZE = (12, 8) 
    fileAlreadyExists = os.path.isfile(PATH_TO_CKPT) 
    if not fileAlreadyExists:
        print('Model does not exsist !')
        exit("Error")

    print(PATH_TO_LABELS)
    # LOAD GRAPH
    print('Loading...')
    detection_graph = tf.Graph() 
    with detection_graph.as_default(): 
        od_graph_def = tf.compat.v1.GraphDef()
        with tf.io.gfile.GFile(PATH_TO_CKPT, 'rb') as fid: 
            serialized_graph = fid.read() 
            od_graph_def.ParseFromString(serialized_graph) 
            tf.import_graph_def(od_graph_def, name='')
    label_map = label_map_util.load_labelmap(PATH_TO_LABELS) 
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True) 
    category_index = label_map_util.create_category_index(categories)
    print('Finish Load Graph..')

    # Main
    t_start = time.time()
    fps = 0

    with detection_graph.as_default():
        with tf.compat.v1.Session(graph=detection_graph) as sess:
            while True:
                ret, frame = cap.read()
                # frame = cv2.flip(frame, -1) # Flip camera vertically
                frame = cv2.resize(frame,(320,240))
                ##############
                #frame_i = cv2.imread("./Services/Camera/status2.jpg")
                #frame = cv2.resize(frame_i,[640,640])
                image_np_expanded = np.expand_dims(frame, axis=0) 
                image_tensor = detection_graph.get_tensor_by_name('image_tensor:0') 
                detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0') 
                detection_scores = detection_graph.get_tensor_by_name('detection_scores:0') 
                detection_classes = detection_graph.get_tensor_by_name('detection_classes:0') 
                num_detections = detection_graph.get_tensor_by_name('num_detections:0')
                
                #print('Running detection..') 
                
                st = time.time()
                (boxes, scores, classes, num) = sess.run( 
                    [detection_boxes, detection_scores, detection_classes, num_detections], 
                    feed_dict={image_tensor: image_np_expanded}) 
                et = time.time()
                elapsed_time = et - st
                print('Execution time of prediction:', elapsed_time, 'seconds')
                #print('Done.  Visualizing..') 
                vis_utils.visualize_boxes_and_labels_on_image_array(
                        frame,
                        np.squeeze(boxes),
                        np.squeeze(classes).astype(np.int32),
                        np.squeeze(scores),
                        category_index,
                        use_normalized_coordinates=True,
                        line_thickness=8)

                #print(scores)
                #s = [x for x in category_index if x == 44]  # list of all elements with .n==30
                #print(s)
                ##############
                
                detected = classes[0]
                for idx, x in enumerate(detected):
                    if(boxes[0][idx][0] != 0.0):
                        print(category_index[detected[idx]]['name'] , scores[0][idx])
                fps = fps + 1
                mfps = fps / (time.time() - t_start)
                cv2.putText(frame, "FPS " + str(int(mfps)), (10,10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
                cv2.imshow('frame', frame)
        
                k = cv2.waitKey(500) & 0xff
                if k == 27: # press 'ESC' to quit
                    break
    
    cap.release()
    cv2.destroyAllWindows()

