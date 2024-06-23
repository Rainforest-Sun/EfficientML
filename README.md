# CS3512 Course Project in SJTU
## 项目简介
本项目将YOLOv5Lite(s)模型部署到Jetson Nano开发板上，实现了多路Webcam数据流的读取和目标检测，同时集成了舵机控制功能。通过Webcam类进行多路视频流读取，在`detect.py`中实现了识别和跟踪目标并转动舵机的功能，并在`servo.py`中封装了基于Adafruit库的舵机控制代码。
## 项目文件结构介绍
- `detect.py`：用于目标检测的脚本。
- `export.py`：用于模型导出的脚本。
- `log`：存放日志文件的目录，用于记录模型训练和测试过程中的日志信息。
- `models`：包含模型定义和配置文件。
- `requirements.txt`：项目所需的依赖包列表。
- `scripts`：包含各种辅助脚本，用于数据处理、模型转换、评估等任务。
- `servo_test.py`：用于测试Servo的脚本。
- `siamfc`：与SiamFC模型相关的文件目录，包含模型定义、数据集处理、跟踪器等。
- `test.py`：用于测试模型的脚本。
- `test_siamfc.py`：用于测试SiamFC模型的脚本。
- `train.py`：用于训练模型的脚本。
- `utils`：包含各种工具函数和模块，支持模型训练和推理过程。
- `weights`：存放预训练权重文件的目录。
## 主要功能

1. **多路Webcam数据流读取**：通过Webcam类实现多路视频流的读取和处理。
2. **目标检测和跟踪**：在`detect.py`中实现了基于YOLOv5Lite(s)模型的目标检测和跟踪功能。
3. **舵机控制**：在`servo.py`中封装了基于Adafruit库的舵机控制代码，实现了识别和跟踪目标后的舵机转动功能。

## 运行模型推理

`detect.py` 脚本可以在多种数据源上运行推理，自动从 [最新的YOLOv5-Lite发布版本](https://github.com/ppogg/YOLOv5-Lite/releases) 下载模型，并将结果保存到 `runs/detect` 目录。

```bash
$ python detect.py --source 0  # webcam
                            file.jpg  # image 
                            file.mp4  # video
                            path/  # directory
                            path/*.jpg  # glob
                            'https://youtu.be/NUsoVlDFqZg'  # YouTube
                            'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```