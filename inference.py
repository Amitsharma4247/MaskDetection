import os
import cv2
from ultralytics import YOLO

model = YOLO(r"MaskDetection\best_openvino_model", task="detect")

def process_video(video_path, output_path):

    cap = cv2.VideoCapture(video_path)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break


        results = model.predict(frame, imgsz=320, half=True, conf=0.5, iou=0.6)
        
        for result in results:
            boxes = result[:5].boxes.numpy()
            for box in boxes:
                print("class", box.cls)
                print("xyxy", box.xyxy)
                print("conf", box.conf)

        im_array = results[0].plot()
        
        out.write(im_array)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

input_dir = r"F:\Projects\MaskDetection\Original Data\InputVideos"
output_dir = r"F:\Projects\MaskDetection\Original Data\OutputVideos"

os.makedirs(output_dir, exist_ok=True)

input_videos = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith(('.mp4', '.avi', '.mov'))]

output_videos = [os.path.join(output_dir, f"output_video{i+1}.mp4") for i in range(len(input_videos))]

for input_video, output_video in zip(input_videos, output_videos):
    process_video(input_video, output_video)
