from ultralytics import YOLO
ai = YOLO("best.pt")
ai(source="test.mp4",show = True,save = True)