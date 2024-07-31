## Install
```shell
pip install multi-camera-recording
```

## Quick use
Start recording and then align frames
```python
from multi-camera-recording.record_sync import start_recording
from multi-camera-recording.align_frames import FrameAligner

path = start_recording()
fa = FrameAligner(path=path)
fa.align_frames()
```    
