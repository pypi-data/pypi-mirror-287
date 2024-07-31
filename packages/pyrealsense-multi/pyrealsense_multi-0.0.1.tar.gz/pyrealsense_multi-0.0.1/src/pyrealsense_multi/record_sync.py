import datetime
import os.path

import pyrealsense2 as rs
import cv2
import threading
import numpy as np

import time

from align_frames import FrameAligner

global record_status


def start_recording(save_path=None, record_duration: float = 7200) -> str:
    """
    Start recording for multi-cameras.

    :param record_duration: Video duration (seconds).
    :param save_path: Path to saving videos and timestamp file.

    :return: Path for videos and timestamp files.
    """

    ctx = rs.context()

    serial_numbers = []
    for device in ctx.query_devices():
        serial_numbers.append(device.get_info(rs.camera_info.serial_number))

    if not save_path:
        date_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        save_path = os.path.join('data', date_str)

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    pipelines = []
    video_writers = []
    timestamp_writers = []
    threads = []

    global record_status
    record_status = True

    for camera_serial_number in serial_numbers:
        pipeline = init_camera_pipline(camera_serial_number)
        pipelines.append(pipeline)

        timestamp_writer = open(os.path.join(save_path, f'{camera_serial_number}.csv'), "w")
        timestamp_writer.write('frame_number,timestamp\n')
        timestamp_writers.append(timestamp_writer)

        video_writer = init_video_writer(os.path.join(save_path, f'{camera_serial_number}.mp4'))
        video_writers.append(video_writer)

        thread = threading.Thread(target=capture, args=(pipeline, timestamp_writer, video_writer))
        threads.append(thread)

    for thread in threads:
        thread.start()

    print("Start recording!")

    time.sleep(record_duration)
    time.sleep(5)
    record_status = False

    time.sleep(3)

    for thread in threads:
        thread.join()

    for i in range(len(serial_numbers)):
        pipelines[i].stop()
        video_writers[i].release()
        timestamp_writers[i].close()

    print("Recording over! ")

    return save_path


def init_camera_pipline(camera_id):
    config = rs.config()
    config.enable_device(camera_id)
    config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
    pipeline = rs.pipeline()
    pipeline.start(config)
    return pipeline


def init_video_writer(file_name):
    width = 1280
    height = 720
    fps = 30
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(file_name, fourcc, fps, (width, height))
    return video_writer


def capture(pipeline, timestamp_writer, video_writer):
    time.sleep(5)  # wait for start of cameras
    global record_status
    while record_status:
        # 等待获取主相机帧
        frames = pipeline.wait_for_frames()

        # 从帧中提取RGB图像数据
        color_frame = frames.get_color_frame()
        if not color_frame:
            print('Color frame not available!\n')
            continue
        # 获取帧的时间戳并写入文件
        timestamp = color_frame.get_timestamp()
        frame_number = color_frame.frame_number
        timestamp_writer.write(f"{frame_number},{timestamp}\n")

        # 获取图像数据并写入视频
        color_image = np.asanyarray(color_frame.get_data())
        video_writer.write(color_image)  # 写入主相机RGB视频


if __name__ == "__main__":
    path = start_recording()
    fa = FrameAligner(path=path)
    fa.align_frames()
