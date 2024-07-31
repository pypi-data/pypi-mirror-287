import os

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import cv2


class FrameAligner:
    def __init__(self, path):
        self.path = path
        self.cameras = self.get_cameras()
        self.fps = self.get_fps()
        self.camera_number = len(self.cameras)

    def get_cameras(self):
        cameras = [file.split('.')[0] for file in os.listdir(self.path) if file.endswith('.mp4')]
        return cameras

    def get_fps(self):
        cap = cv2.VideoCapture(os.path.join(self.path, self.cameras[0] + '.mp4'))
        fps = cap.get(cv2.CAP_PROP_FPS)
        return fps

    def show_aligned_frames(self, df_frame=None, save=False):
        """

        :param save:
        :param df_frame: The first frame ID in the to-check series in corresponding camera.
        :param path: Path to folder containing csv files.
        """
        if df_frame is None:

            df_frame = pd.DataFrame(np.arange(4).reshape(-1, 1).repeat(len(self.cameras), axis=1), columns=self.cameras)
            df_frame['slice_id'] = 0

        readers = [cv2.VideoCapture(os.path.join(self.path, f'{camera}.mp4')) for camera in self.cameras]

        slice_ids = df_frame['slice_id'].unique()
        for slice_id in slice_ids:
            df_frame_ids_slice = df_frame.query("slice_id == @ slice_id")

            img = []
            for camera, reader in zip(self.cameras, readers):

                frames = []
                for frame_id in df_frame_ids_slice[camera]:
                    reader.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
                    _, frame = reader.read()
                    frames.append(frame)

                img_v = np.vstack(frames)
                img.append(img_v)

            img = np.hstack(img)

            figsize = np.array(img.shape)[-2::-1] // 240
            plt.figure(figsize=figsize)
            plt.imshow(img)
            plt.axis('off')
            plt.tight_layout()

            if save:
                plt.savefig(os.path.join(self.path, f'check_{slice_id}.png'))
            else:
                plt.show()

    def align_frames(self, frame_number_to_check=4, to_excel=True, arti_check=False, kw_fix=None, kw_check=None):
        if kw_fix is None:
            kw_fix = {}
        if kw_check is None:
            kw_check = {}

        if 'frame_number_in_series' not in kw_check:
            kw_check['frame_number_in_series'] = frame_number_to_check

        def confirm_timestamps_in_loop(timestamps, fix_fun, check_fun, kw_fix=None, kw_check=None):
            """
            Call fix function for timestamp until confirmed artificially
            :param timestamps: Table or any type of timestamps.
            :param fix_fun: Function for fix timestamps.
            :param check_fun: Function for check timestamps.
            :param kw_fix: K-W args for fix_fun().
            :param kw_check: K-W args for check_fun().
            """
            if kw_check is None:
                kw_check = {}
            if kw_fix is None:
                kw_fix = {}

            flag_fix = ''
            while flag_fix != 'n':
                if flag_fix == 'y':
                    timestamps = fix_fun(timestamps, **kw_fix)
                    flag_fix = check_fun(**kw_check)
                else:
                    print('Please check and enter y or n.')
                    check_fun(**kw_check)
                    flag_fix = input('Need fix? [y/n] \n')

            return timestamps

        def fix_timestamp_label(timestamp_labels):
            str_input = input('Input label to fix like "row column value" (1-index): ')
            str_input = str_input.split(' ')
            str_input = np.array(str_input).astype('int')
            r = str_input[0] - 1
            c = str_input[1] - 1
            v = str_input[2]
            timestamp_labels[r, c] = v
            return timestamp_labels

        def show_timestamp_labels():
            print('Timestamp (ms): ')
            print(timestamp_labels)
            print('Temporal difference (ms): ')
            print(np.diff(timestamp_labels, axis=0))

        def acquire_timestamp_label():
            timestamp_labels = []
            for i in range(self.camera_number):
                for j in range(frame_number_to_check):
                    timestamp = input(f'Input timestamp (ms) in row {j + 1} and column {i + 1}: ')
                    try:
                        timestamp = int(timestamp)
                    except ValueError:
                        print('Value error, input again:\n')
                        timestamp = input(f'Input timestamp (ms) in row {j + 1} and column {i + 1}: ')
                    timestamp_labels.append(timestamp)

            print('Input finish! \n')
            timestamp_labels = (np.array(timestamp_labels)
                                .reshape(frame_number_to_check, self.camera_number, order='F')
                                .astype('int'))
            return timestamp_labels

        def fix_frame_id(df_timestamp, shift=None):
            """
            Shift frame ID in the timestamp table
            """
            if shift is None:
                shift = input('Shift input as "i j ..." according to camera number: ')
                shift = shift.split(' ')
                shift = np.array(shift).astype('int')

            for i_camera, camera_serial_number in enumerate(self.cameras):
                df_timestamp.loc[
                    df_timestamp.query('camera_serial_number == @camera_serial_number').index,
                    'frame_id'
                ] += shift[i_camera]

            return df_timestamp

        def label_to_rel_frame_id(timestamp_labels=None):

            """
            :param timestamp_labels: Arrays of timestamp labels in milliseconds.
            """

            if timestamp_labels is None:
                frame_id_rel = np.arange(frame_number_to_check).reshape(-1, 1).repeat(self.camera_number, 1)
            else:
                ts_ms_rel = timestamp_labels - timestamp_labels.min(axis=(0, 1))
                frame_diff = 1e3 / self.fps
                frame_id_rel = (ts_ms_rel / frame_diff).round().astype('int')

            return frame_id_rel

        # Integrate tables to one table
        df_frame = self.reorder_frame_table()

        if arti_check:
            # Check the first few frames
            print('\nStep 1: Label these timestamps: \n')
            self.show_aligned_frames(save=False)

            # Label and check the first few frames visually until confirmed
            timestamp_labels = acquire_timestamp_label()
            timestamp_labels = confirm_timestamps_in_loop(timestamp_labels, fix_timestamp_label, show_timestamp_labels)

            # Fix frame_id by timestamp_labels
            rel_frame_id = label_to_rel_frame_id(timestamp_labels=timestamp_labels)
            assert (
                np.all(np.diff(rel_frame_id) ==
                       np.diff(df_frame.iloc[:frame_number_to_check].to_numpy()), axis=(0, 1))
            ), 'Frame number mismatch'
            df_frame = fix_frame_id(df_frame, rel_frame_id[0, :])

            # Check aligned frames visually until confirmed
            print('\nStep 2: Check the aligned frames and fix if needed: \n')
            df_frame = confirm_timestamps_in_loop(df_frame, fix_frame_id, self.show_aligned_frames,
                                                  kw_check=kw_check)

        # Save the table
        if to_excel:
            df_frame = df_frame.pivot(columns='camera_serial_number', index='frame_id', values='frame_number_video')
            df_frame.to_csv(os.path.join(path_test, 'aligned_frames.csv'), sep=',', na_rep='')

        return df_frame

    def reorder_frame_table(self):
        frame_files = [file for file in os.listdir(self.path) if
                       (file.endswith('.csv')) and (not file.startswith('aligned_frames'))]

        df_frame = pd.DataFrame()
        for i_camera, file in enumerate(frame_files):
            camera_serial_number = file.replace('.csv', '')
            df_frame_tmp = pd.read_csv(os.path.join(self.path, file))
            df_frame_tmp['camera_serial_number'] = camera_serial_number

            df_frame_tmp['frame_id'] = (df_frame_tmp['frame_number'] - df_frame_tmp['frame_number'].min())
            df_frame = pd.concat([df_frame, df_frame_tmp], axis=0)

        df_frame = df_frame.reset_index(names='frame_number_video')
        return df_frame


if __name__ == "__main__":
    path_test = r'D:\BaiduNetdiskDownload\demo\demo_741_1\video'
    fa = FrameAligner(path=path_test)
    fa.align_frames()
