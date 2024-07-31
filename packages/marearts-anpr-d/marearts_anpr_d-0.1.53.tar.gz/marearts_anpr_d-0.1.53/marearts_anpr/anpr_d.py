import cv2
import numpy as np
import os
from marearts_anpr import xywh2xyxy, nms, draw_detections, anpr_d_SecureModel


class ma_anpr_d:

    def __init__(self, path, conf_thres=0.7, iou_thres=0.5):
        self.conf_threshold = conf_thres
        self.iou_threshold = iou_thres
        
        try:
            self.initialize_model(path)
        except Exception as e:
            print(f"Error during initialization: {e}")
            raise

    def __call__(self, image):
        return self.detect_objects(image)

    def get_execution_provider(self):
        return 'CPUExecutionProvider'
        
    def initialize_model(self, path):
        provider = self.get_execution_provider()
        print(f"Execution provider: {provider}")
        try:
            self.session = anpr_d_SecureModel(path, providers=[provider])
            print("Model session initialized.")
        except Exception as e:
            print(f"Failed to initialize anpr_d_SecureModel: {e}")
            raise

        try:
            self.get_input_details()
            self.get_output_details()
        except Exception as e:
            print(f"Failed to get model details: {e}")
            raise

    def get_input_details(self):
        try:
            model_inputs = self.session.get_model_inputs()
            self.input_names = model_inputs
            self.input_shape = self.session.get_model_inputs()[0].shape
            self.input_height = self.input_shape[2]
            self.input_width = self.input_shape[3]
        except Exception as e:
            print(f"Error getting input details: {e}")
            raise

    def get_output_details(self):
        try:
            model_outputs = self.session.get_model_outputs()
            self.output_names = model_outputs
        except Exception as e:
            print(f"Error getting output details: {e}")
            raise
    

    def detect_objects(self, image):
        input_tensor = self.prepare_input(image)

        # Perform inference on the image
        outputs = self.inference(input_tensor)

        self.boxes, self.scores, self.class_ids = self.process_output(outputs)
        
        # Ensure boxes, scores, and class_ids have the same length
        if len(self.boxes) != len(self.scores) or len(self.boxes) != len(self.class_ids):
            return []   

        detections = []
        for i in range(len(self.boxes)):
            detection = {
                'box': self.boxes[i].tolist(),  # Convert numpy array to Python list
                'score': self.scores[i],
                'class_id': self.class_ids[i]
            }
            detections.append(detection)

        return detections
    
    def inference(self, input_tensor):
        outputs = self.session.run_inference(input_tensor)
        return outputs
    
    def prepare_input(self, image):
        self.img_height, self.img_width = image.shape[:2]
        
        # Resize input image
        input_img = cv2.resize(image, (self.input_width, self.input_height))
        
        # Convert BGR to RGB and scale pixel values to [0, 1]
        # Combine these two operations to save computation
        input_img = (cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB) / 255.0).astype(np.float32)
        
        # Reorder dimensions
        input_img = np.transpose(input_img, (2, 0, 1))
        
        # Add batch dimension
        input_tensor = np.expand_dims(input_img, axis=0)

        return input_tensor

    def process_output(self, output):
        predictions = np.squeeze(output[0]).T

        # Filter out object confidence scores below threshold
        scores = np.max(predictions[:, 4:], axis=1)
        predictions = predictions[scores > self.conf_threshold, :]
        scores = scores[scores > self.conf_threshold]

        if len(scores) == 0:
            return [], [], []

        # Get the class with the highest confidence
        class_ids = np.argmax(predictions[:, 4:], axis=1)

        # Get bounding boxes for each object
        boxes = self.extract_boxes(predictions)

        # Apply non-maxima suppression to suppress weak, overlapping bounding boxes
        indices = nms(boxes, scores, self.iou_threshold)

        return boxes[indices], scores[indices], class_ids[indices]
    
    def extract_boxes(self, predictions):
        # Extract boxes from predictions
        boxes = predictions[:, :4]

        # Scale boxes to original image dimensions
        boxes = self.rescale_boxes(boxes)

        # Convert boxes to xyxy format
        boxes = xywh2xyxy(boxes)

        return boxes
    
    def rescale_boxes(self, boxes):

        # Rescale boxes to original image dimensions
        input_shape = np.array([self.input_width, self.input_height, self.input_width, self.input_height])
        boxes = np.divide(boxes, input_shape, dtype=np.float32)
        boxes *= np.array([self.img_width, self.img_height, self.img_width, self.img_height])
        return boxes
    
    def draw_detections(self, image, draw_scores=True, mask_alpha=0.4):
        return draw_detections(image, self.boxes, self.scores,
                               self.class_ids, mask_alpha)