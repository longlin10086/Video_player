import add_action_ui


class add_action:
    def __init__(self):
        self.action_window = add_action_ui.Ui_Form()
        self.count = 0
        self.action_name = ""
        self.current_item = 0

        self.is_add = True

    def set_up(self):
        self.action_window.ActionChooseBox.addItem("")
        self.action_window.ActionChooseBox.addItem("")
        self.action_window.ActionChooseBox.setItemText(0, "Add action")
        self.action_window.ActionChooseBox.setItemText(1, "Action1: ")

    def add_action(self):
        self.action_name = self.action_window.ActionEdit.text()
        if self.action_window.ActionChooseBox.currentText() == "Add action":
            self.is_add = True
            if self.action_name != "":
                self.count += 1
        else:
            self.current_item = self.action_window.ActionChooseBox.currentIndex()
            self.is_add = False

    def add_combo_item(self):
        self.action_window.ActionChooseBox.addItem("")
        self.action_window.ActionChooseBox.setItemText(
            self.count + 1, f"Action{self.count+1}: ")

    def cancel_text(self):
        if self.action_window.ActionChooseBox.currentText() == "Add action":
            self.action_window.ActionEdit.setText("")
        else:
            self.action_window.ActionEdit.setText(self.action_name)
