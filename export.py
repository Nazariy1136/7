from ultralytics import YOLO

model = YOLO("nano.pt")
model.export(format="edgetpu")
