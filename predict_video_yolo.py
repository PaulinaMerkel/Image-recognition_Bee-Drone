import supervision as sv
import numpy as np
from ultralytics import YOLO

video_path = r"C:\Users\KI\OneDrive - IPH Hannover gGmbH\KI-Koordination\Digitalisierungsprojekt Imkerei\Aufnahmen_GoPro_2024\Neue_Videos\Berarbeitet\Drohne_rangezoomt.mp4"

model = YOLO(r"C:\Users\KI\OneDrive - IPH Hannover gGmbH\KI-Koordination\Digitalisierungsprojekt Imkerei\runs\detect\yolov8n31\weights\last.pt")  # choose model

video_info = sv.VideoInfo.from_video_path(video_path)

def process_frame(frame: np.ndarray, _) -> np.ndarray:
    results = model(frame, imgsz=1280)[0]

    # Extract bounding boxes, confidences, and class IDs
    boxes = results.boxes.xyxy.cpu().numpy()  # Bounding boxes
    confidences = results.boxes.conf.cpu().numpy()  # Confidence scores
    class_ids = results.boxes.cls.cpu().numpy().astype(int)  # Class IDs
    
    # Set the desired confidence threshold
    confidence_threshold = 0.5
    
    # Filter detections based on the confidence threshold
    indices = confidences >= confidence_threshold
    boxes = boxes[indices]
    confidences = confidences[indices]
    class_ids = class_ids[indices]
    
    # Create detections object
    detections = sv.Detections(
        xyxy=boxes,
        confidence=confidences,
        class_id=class_ids
    )

    bounding_box_annotator = sv.BoundingBoxAnnotator(thickness=4)
    label_annotator = sv.LabelAnnotator(text_thickness=4, text_scale=2)

    labels = [f"{model.names[class_id]} {confidence:0.2f}" for class_id, confidence in zip(class_ids, confidences)]

    frame = bounding_box_annotator.annotate(scene=frame, detections=detections)
    frame = label_annotator.annotate(scene=frame, detections=detections, labels=labels)

    return frame

sv.process_video(source_path=video_path, target_path="video_drohne.mp4", callback=process_frame)
