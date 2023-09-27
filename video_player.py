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
    QWidget, QMessageBox)
import cv2
import numpy as np
import yolov5
import add_action
import sys


class video_player():

    def __init__(self):
        super().__init__()
        self.window = QMainWindow()
        self._ui_window = Ui_MainWindow()
        self._ui_window.setupUi(self.window)

        self._add_action_ui = add_action.add_action()
        self._add_action_window = QMainWindow()
        self._add_action_ui.action_window.setupUi(self._add_action_window)
        self._add_action_window.setWindowTitle("Add action")
        self._add_action_ui.set_up()




        self._file_path = None
        self._history_path = None
        self._is_first_time = True
        self._ui_window.Load.clicked.connect(self._open_file)

        self._action_array = [self._ui_window.Action_1, self._ui_window.Action_2, self._ui_window.Action_3,
                              self._ui_window.Action_4, self._ui_window.Action_5, self._ui_window.Action_6,
                              self._ui_window.Action_7, self._ui_window.Action_8, self._ui_window.Action_9]


        self._model = yolov5.load('yolov5s.pt')
        self._clear_value()
        self._mode = "Viewmode"
        self._ui_window.comboBox.currentTextChanged.connect(self._set_mode)


        self._is_on = True
        self._button_mode = "Pause"
        self._ui_window.Pause.clicked.connect(self._pause_and_play_video)


        self._is_changing_flag = False
        self._ui_window.frame_slider.sliderPressed.connect(self._pause_video)
        self._ui_window.frame_slider.sliderReleased.connect(self._slider_value_changed)
        self._ui_window.frames_slider.valueChanged.connect(self._double_slider_value_changed)

        self._ui_window.AddAction.clicked.connect(self._add_action)
        self._add_action_ui.action_window.SaveButton.clicked.connect(self._add_action_button)
        self._add_action_ui.action_window.ActionChooseBox.currentIndexChanged.connect(self._change_action_text)
        self._add_action_ui.action_window.CancelButton.clicked.connect(self._add_action_ui.cancel_text)


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

        self.width = 0
        self.height = 0

        for action in self._action_array:
            action.hide()
            action.setCheckable(False)

        self._ui_window.Action_1.setCheckable(True)
        self._ui_window.Action_1.setChecked(True)
        self._ui_window.Action_1.show()
        self._ui_window.Action_1.setText("Background Action")


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
        # set the current frame to show
        self._cap.set(cv2.CAP_PROP_POS_FRAMES, self._current_frame)
        ret, frame = self._cap.read()
        if ret:
            self.width = int(self._cap.get(3))
            self.height = int(self._cap.get(4))
            self._frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # obtain the converted frame image

            self._change_frame()

            frame_image = QImage(self._frame.tostring(), self.width, self.height, self._frame.strides[0], QImage.Format.Format_RGB888)
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

    def _set_mode(self):
        self._mode = self._ui_window.comboBox.text()

    def _obtain_current_frame_middle_value(self):
        # use yolo to obtain the middle value of the human
        results = self._model(self._frame)
        table = results.pandas().xyxy[0]
        person_table = table[table['name'] == 'person']
        left_x = min(person_table['xmax'][0], person_table['xmax'][1], self._left_value)
        right_x = max(person_table['xmin'][0], person_table['xmin'][1], self._right_value)
        self._middle_value = int((left_x + right_x) / 2)

    def _change_frame(self):
        # detect the comboBox to choose which image should be shown
        image = np.zeros(self._frame.shape, np.uint8)
        self._obtain_current_frame_middle_value()
        match self._mode:
            case "Viewmode":
                return
            case "Left person":
                image[:self.height, :self._middle_value] = self._frame[:self.height, :self._middle_value]
                self._frame = image
                return
            case "Right person":
                image[:self.height, self._middle_value:] = self._frame[:self.height, self._middle_value:]
                self._frame = image
                return

    def _add_action(self):
        self._add_action_window.show()

    def _add_action_button(self):
        self._add_action_ui.add_action()
        if self._add_action_ui.action_name != "" and self._add_action_ui.is_add:
            self._action_array[self._add_action_ui.count].setText(self._add_action_ui.action_name)
            self._action_array[self._add_action_ui.count].show()
            self._action_array[self._add_action_ui.count].setCheckable(True)
            self._action_array[self._add_action_ui.count].setChecked(True)
            self._add_action_ui.add_combo_item()
        if (not self._add_action_ui.is_add) and self._add_action_ui.action_name != "":
            self._action_array[self._add_action_ui.current_item-1].setText(self._add_action_ui.action_name)
            self._action_array[self._add_action_ui.current_item-1].setChecked(True)

    def _change_action_text(self):
        self._add_action_ui.current_item = self._add_action_ui.action_window.ActionChooseBox.currentIndex()
        if self._add_action_ui.action_window.ActionChooseBox.currentText() == "Add action":
            text = ""
        else:
            text = self._action_array[self._add_action_ui.current_item-1].text()
        self._add_action_ui.action_name = text
        self._add_action_ui.action_window.ActionEdit.setText(text)