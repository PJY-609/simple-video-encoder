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

