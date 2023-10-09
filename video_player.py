from video_player_ui import Ui_MainWindow
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    Qt,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
    QKeyEvent)
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QMenuBar,
    QSizePolicy,
    QSpacerItem,
    QStatusBar,
    QVBoxLayout,
    QFileDialog,
    QWidget,
    QMessageBox)
import cv2
import numpy as np
import yolov5
import add_action
import pandas as pd


class video_player(QMainWindow, QWidget):
    """ video_player 类，项目主体，即项目主要界面
    """
    def __init__(self):
        """
        :argument: _ui_window 项目主页面的ui
        :argument: _add_action_window 点击add_action按钮后的弹出界面
        :argument: _file_path 视频文件的path
        :argument: _history_path 上一次打开的视频文件path
        :argument: _action_array 包含9个Radio Button的集合
        :argument: _dataframe pandas中的表格（缓存）
        :argument: filename 保存csv的文件名字
        :argument: _is_on 判断当前视频播放是否结束的标签
        """
        super().__init__()
        self._ui_window = Ui_MainWindow()
        self._ui_window.setupUi(self)

        # self._space_press_event(Qt.Key_Space)

        self._add_action_ui = add_action.add_action()
        self._add_action_window = QMainWindow()
        self._add_action_ui.action_window.setupUi(self._add_action_window)
        self._add_action_window.setWindowTitle("Add action")
        self._add_action_ui.set_up()

        self._file_path = None
        self._history_path = None
        self._is_first_time = True
        self._ui_window.Load.clicked.connect(self._open_file)

        self._action_array = [
            self._ui_window.Action_1,
            self._ui_window.Action_2,
            self._ui_window.Action_3,
            self._ui_window.Action_4,
            self._ui_window.Action_5,
            self._ui_window.Action_6,
            self._ui_window.Action_7,
            self._ui_window.Action_8,
            self._ui_window.Action_9]

        self._dataframe = None
        self.file_name = None

        self._model = yolov5.load('./yolov5s.pt')
        self._clear_value()
        self._mode = "Viewmode"
        self._ui_window.comboBox.currentTextChanged.connect(self._set_mode)

        self._is_on = True
        self._button_mode = "Pause"
        self._ui_window.Pause.clicked.connect(self._pause_and_play_video)

        self._is_changing_flag = False
        self._ui_window.frame_slider.setMinimum(1)
        self._ui_window.frames_slider.setMinimum(1)
        self._ui_window.frame_slider.sliderPressed.connect(self._pause_video)
        self._ui_window.frame_slider.sliderReleased.connect(
            self._slider_value_changed)
        self._ui_window.frames_slider.valueChanged.connect(
            self._double_slider_value_changed)

        self._ui_window.AddAction.clicked.connect(self._add_action)
        self._add_action_ui.action_window.SaveButton.clicked.connect(
            self._add_action_button)
        self._add_action_ui.action_window.ActionChooseBox.currentIndexChanged.connect(
            self._change_action_text)
        self._add_action_ui.action_window.CancelButton.clicked.connect(
            self._add_action_ui.cancel_text)

        self._read_or_write = "write"
        self._ui_window.Write.clicked.connect(self._data_write_and_read)
        self._ui_window.Conf.clicked.connect(self._read_csv)

        self._ui_window.Screenshot.clicked.connect(self._screenshot)
        self._ui_window.Save.clicked.connect(self._save_to_csv)

        self._ui_window.retranslateUi(self)
        self._ui_window.current.setText("Current frame: 0")
        self._ui_window.total.setText("Total frames: 0")

    def _clear_value(self):
        """
        对所有配置进行初始化操作，恢复到最开始时的样式
        """
        # 三个value表示yolo中视频的左右中值，以方便切割
        self._left_value = 9999999999
        self._right_value = 0
        self._middle_value = 0

        self._current_frame = 1
        self._total_frame = 0

        self.width = 0
        self.height = 0

        self._ui_window.current_action_text.setText("Current action: ")

        for action in self._action_array:
            action.hide()
            action.setCheckable(False)

        self._ui_window.Action_1.setCheckable(True)
        self._ui_window.Action_1.setChecked(True)
        self._ui_window.Action_1.show()
        self._ui_window.Action_1.setText("Background action")

    def _open_file(self):
        """
        打开对应视频文件，用opencv加载
        """
        self._history_path = self._file_path
        self._file_path, _ = QFileDialog.getOpenFileName(
            self._ui_window.Load, "请选择对应文件", ".", "mp4(*.mp4);;avi(*.avi);;flv(*.flv)")
        if self._is_first_time:
            self._history_path = self._file_path
        print(self._file_path)
        if self._file_path:
            self._clear_value()
            self._cap = cv2.VideoCapture(self._file_path)
            # self._cap.set(cv2.CAP_PROP_POS_FRAMES, self._current_frame)
            self._play_video()

    def _set_frame(self):
        """
        将opencv获取到的当前帧转化成qt中的pixmap以显示出来
        """
        self._cap.set(cv2.CAP_PROP_POS_FRAMES, self._current_frame-1)
        ret, frame = self._cap.read()
        if ret:
            self.width = int(self._cap.get(3))
            self.height = int(self._cap.get(4))
            # obtain the converted frame image
            self._frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            self._change_frame()

            frame_image = QImage(
                self._frame.tostring(),
                self.width,
                self.height,
                self._frame.strides[0],
                QImage.Format.Format_RGB888)
            self._ui_window.video_player.setPixmap(
                QPixmap.fromImage(frame_image).scaled(
                    self._ui_window.video_player.size(),
                    aspectMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding))

    def get_frame(self):
        # return current frame image
        return self._frame

    def _obtain_frame(self):
        """
        获取视频的相关数据后对ui进行初始化配置
        """
        self._current_frame = int(self._cap.get(cv2.CAP_PROP_POS_FRAMES))
        self._total_frame = int(self._cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self._ui_window.current.setText(
            f"Current frame: {self._current_frame}")
        self._ui_window.total.setText(f"Total frames: {self._total_frame}")
        if self._is_first_time:
            self._end_frame = self._total_frame
            self._is_first_time = False
        self._change_frame_edit()

    def _play_video(self):
        """
        播放视频，即对当前图像界面进行刷新
        """
        while True:
            self._current_frame += 1
            self._set_frame()
            self._obtain_frame()
            self._is_spinbox_clicked()
            self._is_slider_clicked()
            if cv2.waitKey(1) == ord('q') or (not self._is_on):
                break
            if self._current_frame > self._end_frame:
                self._pause_video()
        # self._cap.release()

    def _single_frame_edit(self):
        """
        在ui中显示单帧参数修改slider的数据
        """
        self._ui_window.frame_slider.setMaximum(self._total_frame)
        self._ui_window.frame_slider.setValue(self._current_frame)
        self._ui_window.frame_slider.setSliderPosition(self._current_frame)
        self._ui_window.frame_edit.setMaximum(self._total_frame)
        self._ui_window.frame_edit.setValue(self._current_frame)

    def _pause_and_play_video(self):
        """
        判断当前视频状态是暂停还是播放，作出相应行为
        """
        match self._button_mode:
            case "Pause":
                self._is_on = False
                self._cap.set(cv2.CAP_PROP_POS_FRAMES, self._current_frame)
                self._change_frame_edit()
                self._button_mode = "Play"
                self._ui_window.Pause.setText("Play")
                self._ui_window.frame_edit.valueChanged.connect(
                    self._edit_value_changed)
                self._ui_window.min_frame.valueChanged.connect(
                    self._min_value_changed)
                self._ui_window.max_frame.valueChanged.connect(
                    self._max_value_changed)
            case "Play":
                self._is_on = True
                self._cap.set(cv2.CAP_PROP_POS_FRAMES, self._current_frame)
                self._change_frame_edit()
                self._button_mode = "Pause"
                self._ui_window.Pause.setText("Pause")
                self._play_video()

    def _slider_value_changed(self):
        """
        修改单帧slider后发生的行为
        """
        if self._is_changing_flag:
            return
        self._current_frame = self._ui_window.frame_slider.sliderPosition()
        self._set_frame()
        self._obtain_frame()

    def _pause_video(self):
        self._button_mode = "Pause"
        print(self._dataframe)
        self._pause_and_play_video()

    def _is_spinbox_clicked(self):
        """
        检查spinbox是否被点击，如果有则将视频暂停等待修改
        """
        if self._ui_window.frame_edit.hasFocus() or self._ui_window.max_frame.hasFocus(
        ) or self._ui_window.min_frame.hasFocus():
            self._pause_video()

    def _is_slider_clicked(self):
        """
        检查slider是否被点击，如果有则将视频暂停等待修改
        """
        if self._ui_window.frames_slider.hasFocus():
            self._pause_video()

    def _edit_value_changed(self):
        """
        修改spinbox的值后发生的行为
        """
        if self._is_changing_flag:
            return
        self._current_frame = self._ui_window.frame_edit.value()
        self._set_frame()
        self._obtain_frame()

    def _min_value_changed(self):
        """
        修改帧数所能到达的最小值
        """
        if self._is_changing_flag:
            return
        self._current_frame = self._ui_window.min_frame.value()
        self._set_frame()
        self._obtain_frame()

    def _max_value_changed(self):
        """
        修改帧数所能到达的最大值
        """
        if self._is_changing_flag:
            return
        self._end_frame = self._ui_window.max_frame.value()
        self._set_frame()
        self._obtain_frame()

    def _double_slider_value_changed(self):
        """
        修改slider的值后发生的行为（含两个滑块的slider）
        """
        if self._is_changing_flag:
            return
        _current_frame, _end_frame = self._ui_window.frames_slider.value()
        self._current_frame = _current_frame
        self._end_frame = _end_frame
        self._set_frame()
        self._obtain_frame()

    def _double_frame_edit(self):
        """
        修改spinbox的值后发生的行为（含两个滑块的slider）
        """
        self._ui_window.min_frame.setMaximum(self._total_frame)
        self._ui_window.max_frame.setMaximum(self._total_frame)
        self._ui_window.frames_slider.setMaximum(self._total_frame)

        self._ui_window.min_frame.setValue(self._current_frame)
        self._ui_window.frames_slider.setValue(
            (self._current_frame, self._end_frame))
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
        left_x = min(
            person_table['xmax'][0],
            person_table['xmax'][1],
            self._left_value)
        right_x = max(
            person_table['xmin'][0],
            person_table['xmin'][1],
            self._right_value)
        self._middle_value = int((left_x + right_x) / 2)

    def _change_frame(self):
        # detect the comboBox to choose which image should be shown
        image = np.zeros(self._frame.shape, np.uint8)
        self._obtain_current_frame_middle_value()
        match self._mode:
            case "Viewmode":
                return
            case "Left person":
                image[:self.height,
                      :self._middle_value] = self._frame[:self.height,
                                                         :self._middle_value]
                self._obtain_action(image)
                file_path, _ = self._file_path.split('.')
                self.file_name = f"{file_path}_left"
                return
            case "Right person":
                image[:self.height,
                      self._middle_value:] = self._frame[:self.height,
                                                         self._middle_value:]
                self._obtain_action(image)
                file_path, _ = self._file_path.split('.')
                self.file_name = f"{file_path}_right"
                return

    def _obtain_action(self, image):
        """
        初始化pandas的dataframe
        :param image: yolo处理后的image图像
        """
        self._frame = image
        if self._dataframe is None:
            self._creat_panda_table()
        self._ui_window.current_action_text.setText(
            f"Current action: {self._dataframe['Action'][self._current_frame]}")
        self._connect_action_frame()

    def _add_action(self):
        self._add_action_window.show()

    def _add_action_button(self):
        """
        在ui界面中显示新增的action按钮
        """
        self._add_action_ui.add_action()
        if self._add_action_ui.action_name != "" and self._add_action_ui.is_add:
            self._action_array[self._add_action_ui.count].setText(
                self._add_action_ui.action_name)
            self._action_array[self._add_action_ui.count].show()
            self._action_array[self._add_action_ui.count].setCheckable(True)
            self._action_array[self._add_action_ui.count].setChecked(True)
            self._add_action_ui.add_combo_item()
        if (not self._add_action_ui.is_add) and self._add_action_ui.action_name != "":
            self._action_array[self._add_action_ui.current_item -
                               1].setText(self._add_action_ui.action_name)
            self._action_array[self._add_action_ui.current_item -
                               1].setChecked(True)

    def _change_action_text(self):
        self._add_action_ui.current_item = self._add_action_ui.action_window.ActionChooseBox.currentIndex()
        if self._add_action_ui.action_window.ActionChooseBox.currentText() == "Add action":
            text = ""
        else:
            text = self._action_array[self._add_action_ui.current_item - 1].text()
        self._add_action_ui.action_name = text
        self._add_action_ui.action_window.ActionEdit.setText(text)

    def _creat_panda_table(self):
        index = [i for i in range(1, self._total_frame + 1)]
        self._dataframe = pd.DataFrame(columns=['Action'], index=index)
        self._dataframe['Action'] = 'Background action'
        self._dataframe.index.name = "Frame"


    def _connect_action_frame(self):
        """
        将当前的action按钮与当前帧进行关联捆绑
        """
        action_name = ""
        for action in self._action_array:
            if action.isChecked():
                action_name = action.text()
                break
        if self._read_or_write == "write":
            self._dataframe['Action'][self._current_frame - 1] = action_name

    def _save_to_csv(self):
        print("save")
        with open(f"{self.file_name}.csv", 'w'):
            self._dataframe.to_csv(path_or_buf=f"{self.file_name}.csv")

    def _read_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(self._ui_window.Conf, "请选择对应文件", ".", "csv(*.csv)")
        self._dataframe = pd.read_csv(file_path, index_col="Frame")
        action = self._dataframe['Action']
        action_tuple = set(action)
        action_tuple.discard('Background action')
        action_list = list(action_tuple)
        for i in range(0, len(action_list)):
            self._action_array[i+1].setText(action_list[i])
            self._action_array[i+1].show()
            self._action_array[i+1].setCheckable(True)
            self._action_array[i+1].setChecked(True)
            self._add_action_ui.count += 1

        print(action_tuple)

    def _data_write_and_read(self):
        """
        检查当前是write模式还是read模式
        """
        match self._read_or_write:
            case "write":
                self._ui_window.Write.setText("Read")
                self._read_or_write = "read"
                return
            case "read":
                self._ui_window.Write.setText("Write")
                self._read_or_write = "write"
                return
