# Zero-Shot-Object-Detection-Segmentation
DIH Project

#### Created Model for training
Model completed.

#### Processed Annotation Files for seen and unseen classes

#### Feature Extraction took 8 hours for MSCOCO (6 lakh objects). And 12 hours for VG (10 lakh objects).

#### Code is ready for obtaining non-overlapping boxes, just a litter modification is required for bigger boxes.
#### Filtered boxes which had size nearly 224x224 or greater than that and then took 100 images from each class and trained on them and got 0.25% i.e. 0.0025 accuracy on TRAINING data!! Before it was 0.0011 accuracy on TRAINING data!
#### Will see what happens after training on all the filtered images.

### Need to read implementation details from the paper https://arxiv.org/pdf/1804.04340.pdf.
### Need to work on Edge Boxes.
### Need to extract features for unseen ground truth objects and generate their targets (labels/string) for evaluation.
### Need to understand and implement Recall@K for evaluation of model.
