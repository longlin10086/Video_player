from video_player_ui import Ui_MainWindow
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon, Qt,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenuBar,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout, QFileDialog,
    QWidget)
import cv2
import numpy as np
# import yolov5
import pandas



class video_player():

    def __init__(self):
        super().__init__()
        self.window = QMainWindow()
        self._ui_window = Ui_MainWindow()
        self._ui_window.setupUi(self.window)


        self._file_path = None
        self._history_path = None
        self._is_first_time = True
        self._ui_window.Load.clicked.connect(self._open_file)

        # self._model = yolov5.load('yolov5s.pt')
        self._clear_value()


        self._is_on = True
        self._button_mode = "Pause"
        self._ui_window.Pause.clicked.connect(self._pause_and_play_video)


        self._is_changing_flag = False
        self._ui_window.frame_slider.sliderPressed.connect(self._pause_video)
        self._ui_window.frame_slider.sliderReleased.connect(self._slider_value_changed)
        self._ui_window.frames_slider.valueChanged.connect(self._double_slider_value_changed)

        self._ui_window.Screenshot.clicked.connect(self._screenshot)

        self._ui_window.retranslateUi(self.window)
        self._ui_window.current.setText("Current frame: 0")
        self._ui_window.total.setText("Total frames: 0")

    def _clear_value(self):
        self._left_value = 9999999999
        self._right_value = 0
        self._middle_value = 0

        self._current_frame = 0
        self._total_frame = 0

    def _open_file(self):
        self._history_path = self._file_path
        self._file_path, _ = QFileDialog.getOpenFileName(self._ui_window.Load, "请选择对应文件", ".", "mp4(*.mp4);;avi(*.avi);;flv(*.flv)")
        if self._is_first_time:
            self._history_path = self._file_path
        print(self._file_path)
        if self._file_path:
            self._clear_value()
            self._cap = cv2.VideoCapture(self._file_path)
            self._cap.set(cv2.CAP_PROP_POS_FRAMES, self._current_frame)
            self._play_video()

    def _set_frame(self):
        self._cap.set(cv2.CAP_PROP_POS_FRAMES, self._current_frame)
        ret, frame = self._cap.read()
        if ret:
            width = int(self._cap.get(3))
            height = int(self._cap.get(4))
            self._frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # obtain the converted frame image
            frame_image = QImage(self._frame.tostring(), width, height, self._frame.strides[0], QImage.Format.Format_RGB888)
            self._ui_window.video_player.setPixmap(QPixmap.fromImage(frame_image).scaled(self._ui_window.video_player.size(), aspectMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding))

    def get_frame(self):
        # return current frame image
        return self._frame
    def _obtain_frame(self):
        self._current_frame = int(self._cap.get(cv2.CAP_PROP_POS_FRAMES))
        self._total_frame = int(self._cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self._ui_window.current.setText(f"Current frame: {self._current_frame}")
        self._ui_window.total.setText(f"Total frames: {self._total_frame}")
        if self._is_first_time:
            self._end_frame = self._total_frame
            self._is_first_time = False
        self._change_frame_edit()


    def _play_video(self):
        while True:
            self._obtain_frame()
            self._set_frame()
            self._is_spinbox_clicked()
            self._is_slider_clicked()
            if cv2.waitKey(1) == ord('q') or (not self._is_on):
                break
            if self._current_frame > self._end_frame:
                self._pause_video()
        # self._cap.release()

    def _single_frame_edit(self):
        self._ui_window.frame_slider.setMaximum(self._total_frame)
        self._ui_window.frame_slider.setValue(self._current_frame)
        self._ui_window.frame_slider.setSliderPosition(self._current_frame)
        self._ui_window.frame_edit.setMaximum(self._total_frame)
        self._ui_window.frame_edit.setValue(self._current_frame)

    def _pause_and_play_video(self):
        match self._button_mode:
            case "Pause":
                self._is_on = False
                self._cap.set(cv2.CAP_PROP_POS_FRAMES, self._current_frame)
                self._change_frame_edit()
                self._button_mode = "Play"
                self._ui_window.Pause.setText("Play")
                self._ui_window.frame_edit.valueChanged.connect(self._edit_value_changed)
                self._ui_window.min_frame.valueChanged.connect(self._min_value_changed)
                self._ui_window.max_frame.valueChanged.connect(self._max_value_changed)
            case "Play":
                self._is_on = True
                self._cap.set(cv2.CAP_PROP_POS_FRAMES, self._current_frame)
                self._change_frame_edit()
                self._button_mode = "Pause"
                self._ui_window.Pause.setText("Pause")
                self._play_video()

    def _slider_value_changed(self):
        print("trigger_slider")
        if self._is_changing_flag:
            return
        self._current_frame = self._ui_window.frame_slider.sliderPosition()
        self._set_frame()
        self._obtain_frame()

    def _pause_video(self):
        self._button_mode = "Pause"
        self._pause_and_play_video()

    def _is_spinbox_clicked(self):
        if self._ui_window.frame_edit.hasFocus() or self._ui_window.max_frame.hasFocus() or self._ui_window.min_frame.hasFocus():
            self._pause_video()

    def _is_slider_clicked(self):
        if self._ui_window.frames_slider.hasFocus():
            self._pause_video()
    def _edit_value_changed(self):
        if self._is_changing_flag:
            return
        print("edit_value")
        self._current_frame = self._ui_window.frame_edit.value()-1
        self._set_frame()
        self._obtain_frame()

    def _min_value_changed(self):
        if self._is_changing_flag:
            return
        print("min_value")
        self._current_frame = self._ui_window.min_frame.value()-1
        self._set_frame()
        self._obtain_frame()

    def _max_value_changed(self):
        if self._is_changing_flag:
            return
        print("max_value")
        self._end_frame = self._ui_window.max_frame.value()
        self._set_frame()
        self._obtain_frame()

    def _double_slider_value_changed(self):
        if self._is_changing_flag:
            return
        _current_frame, _end_frame = self._ui_window.frames_slider.value()
        self._current_frame = _current_frame-1
        self._end_frame = _end_frame
        self._set_frame()
        self._obtain_frame()

    def _double_frame_edit(self):
        self._ui_window.min_frame.setMaximum(self._total_frame)
        self._ui_window.max_frame.setMaximum(self._total_frame)
        self._ui_window.frames_slider.setMaximum(self._total_frame)

        self._ui_window.min_frame.setValue(self._current_frame)
        self._ui_window.frames_slider.setValue((self._current_frame, self._end_frame))
        self._ui_window.max_frame.setValue(self._end_frame)

    def _change_frame_edit(self):
        self._is_changing_flag = True
        self._single_frame_edit()
        self._double_frame_edit()
        self._is_changing_flag = False

    def _screenshot(self):
        # take a screenshot and save it to the img directory
        img = self._ui_window.video_player.pixmap()
        print("save")
        img.save(f'./img/{self._current_frame}.png', "PNG")

    def get_play_mode(self):
        # obtain the current mode of comboBox
        return self._ui_window.comboBox.text()

    # def _detect_change_comboBox_mode(self):
    #     match self.get_play_mode():
    #         case "Viewmode":
    #             return
    #         case "Left person":
    #             pass
    #         case "Right pserson":
    #             pass
    #
    # def _obtain_current_frame_middle_value(self):
    #     results = self._model(self._frame)
    #     table = results.pandas().xyxy[0]
    #     person_table = table[table['name'] == 'person']
    #     left_x = min(person_table['xmax'][0], person_table['xmax'][1], left_x)
    #     right_x = max(person_table['xmin'][0], person_table['xmin'][1], right_x)
    #     middle = int((left_x + right_x) / 2)
    #
