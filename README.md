# simple-video-encoder
a simple H.264 video encoder by PyQt5  

**requirements**:  
1. python 3.6
2. [ffmpeg-python](https://github.com/kkroening/ffmpeg-python)
3. ffmpeg (see the [question](https://stackoverflow.com/questions/54262306/ffmpeg-python-wrapper-ffmpeg-run-getting-filenotfounderror) in stackoverflow)
4. PyQt5
5. LAVFilters (see the [question](https://stackoverflow.com/questions/42801979/error-using-qmediaplayer-with-pyqt5-on-windows) in stackoverflow)  

**run main.py**
> cd .\video_encoder  
python main.py

**user guide**
1. File->Open->select the input video file
<img src='https://raw.githubusercontent.com/yujuezhao/simple-video-encoder/master/images/1.png' width='30%'>
<img src='https://raw.githubusercontent.com/yujuezhao/simple-video-encoder/master/images/3.png' width='30%'>
2. Settings->Set H264 Parameters
<img src='https://raw.githubusercontent.com/yujuezhao/simple-video-encoder/master/images/4.png' width='30%'>
<img src='https://raw.githubusercontent.com/yujuezhao/simple-video-encoder/master/images/5.png' width='30%'>
3. Encode->Begin Encode->type output filename
<img src='https://raw.githubusercontent.com/yujuezhao/simple-video-encoder/master/images/6.png' width='30%'>
4. Result (CRF=40)
<img src='https://raw.githubusercontent.com/yujuezhao/simple-video-encoder/master/images/7.png' width='30%'>

***
## MVC pattern in Python
It is my first time to use MVC pattern to write a GUI. [tutorial](https://www.giacomodebidda.com/mvc-pattern-in-python-introduction-and-basicmodel/) gives a neat mini-example to explain what MVC pattern is.  
Download these three .py files and run them can give a clear sense of MVC pattern [basics_backend.py](https://github.com/yujuezhao/simple-video-encoder/blob/master/video_encoder/Others/basic_backend.py), [model_view_controller.py](https://github.com/yujuezhao/simple-video-encoder/blob/master/video_encoder/Others/model_view_controller.py), [mvc_exceptions.py](https://github.com/yujuezhao/simple-video-encoder/blob/master/video_encoder/Others/mvc_exceptions.py).
***
## Exceptions handling 
I also learn something of exceptions handling in python. Thanks to the contributors in stackoverflow, my [problem](https://stackoverflow.com/questions/56411990/how-to-manage-exceptions-correctly-in-pyqt/56432762#56432762) could be tackled properly.
Here is my final solution,
```
def updateFilename(self):
    self.model.updateFilename(self.fileName)

def updateOutput(self):
    self.model.updateOutput(self.encodeDialog.output)

def encodeVideo(self):
    try:
        self.updateFilename()
        self.updateOutput()
        flag = True
    except (type_exc.PathIsEmpty, type_exc.FileAlreadyExists, type_exc.PathNotExists) as e:
        flag = False
        self.errorDialog.errorTypeChanged(e)
        self.errorDialog.exec_()

    if flag:
        self.model.encodeVideo()
```
