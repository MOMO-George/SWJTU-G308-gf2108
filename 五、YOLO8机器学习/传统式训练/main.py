#pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117
#pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple 或者 https: // pypi.mirrors.ustc.edu.cn/simple

from ultralytics import YOLO

def train_yolov8():
    a1 = YOLO("yolov8n.pt")
    a1.train(
        data="data.yaml", 
        epochs=100,
        batch=16,
        imgsz=640,
        workers=4,
        device=0
    )

# 关键：主进程保护语句
if __name__ == '__main__':
    train_yolov8()