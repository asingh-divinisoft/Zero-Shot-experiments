import cv2
import numpy as np

class EdgeBoxes():
    def __init__(self, model_path):
        "Loads the model for finding edge boxes. Download the model from https://github.com/opencv/opencv_extra/blob/master/testdata/cv/ximgproc/model.yml.gz"
        self.model = model_path
        try:
            self.edge_detection = cv2.ximgproc.createStructuredEdgeDetection(self.model)
        except:
            print('Invalid model path or the model file is corrupt.')
        
    def __call__(self, image_array, maxBoxes=30):
        "Provide an RGB image_array and maximum number of boxes to provide."
        self.im = image_array
#         rgb_im = cv2.cvtColor(self.im, cv.COLOR_BGR2RGB)
        edges = self.edge_detection.detectEdges(np.float32(self.im) / 255.0)

        orimap = self.edge_detection.computeOrientation(edges)
        edges = self.edge_detection.edgesNms(edges, orimap)

        edge_boxes = cv2.ximgproc.createEdgeBoxes()
        edge_boxes.setMaxBoxes(maxBoxes)
        return edge_boxes.getBoundingBoxes(edges, orimap)