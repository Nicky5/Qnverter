from inspect import isgeneratorfunction
from random import randint, random

from PyQt5 import Qt
from PyQt5.QtCore import QObject, pyqtSignal, QEvent, QSize, QRect, Qt, QStringListModel
from PyQt5.QtGui import QPainter, QColor, QTextFormat, QPixmap, QPen, QBrush, QPalette, QTextCursor
from PyQt5.QtWidgets import QWidget, QPlainTextEdit, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QScrollArea, \
    QCompleter, QLineEdit, QLabel, QApplication, QStackedWidget, QSizePolicy, QAbstractButton, QToolButton, QDialog, \
    QErrorMessage, QDesktopWidget, QSpacerItem
import sys

from PySide6.QtCore import Slot

import scripts

class LineNumberArea(QWidget):
    """

    """

    def __init__(self, editor):
        QWidget.__init__(self, editor)
        self._code_editor = editor

    def sizeHint(self):
        """

        :return:
        """
        return QSize(self._code_editor.line_number_area_width(), 0)

    def paintEvent(self, event):
        """

        :param event:
        """
        self._code_editor.lineNumberAreaPaintEvent(event)

class CodeEditor(QPlainTextEdit):
    """

    """

    def __init__(self, no_rec=False):
        super().__init__()
        self.line_number_area = LineNumberArea(self)
        self.result_board = CodeEditor(no_rec=True) if no_rec else None

        self.blockCountChanged[int].connect(self.update_line_number_area_width)
        self.updateRequest[QRect, int].connect(self.update_line_number_area)
        self.cursorPositionChanged.connect(self.highlight_current_line)

        self.update_line_number_area_width(0)
        self.highlight_current_line()

    def line_number_area_width(self):
        """

        :return:
        """
        digits = 1
        max_num = max(1, self.blockCount())
        while max_num >= 10:
            max_num *= 0.1
            digits += 1

        space = 3 + self.fontMetrics().horizontalAdvance('9') * digits
        return space

    def resizeEvent(self, e):
        """

        :param e:
        """
        super().resizeEvent(e)
        cr = self.contentsRect()
        width = self.line_number_area_width()
        rect = QRect(cr.left(), cr.top(), width, cr.height())
        self.line_number_area.setGeometry(rect)

    def lineNumberAreaPaintEvent(self, event):
        """

        :param event:
        """
        painter = QPainter(self.line_number_area)
        painter.fillRect(event.rect(), QBrush(QColor(49, 51, 53)))
        block = self.firstVisibleBlock()
        block_number = block.blockNumber()
        offset = self.contentOffset()
        top = self.blockBoundingGeometry(block).translated(offset).top()
        bottom = top + self.blockBoundingRect(block).height()

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(block_number + 1)
                painter.setPen(Qt.lightGray)
                width = self.line_number_area.width()
                height = self.fontMetrics().height()
                painter.drawText(0, int(top), width, height, Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            block_number += 1

    @Slot()
    def update_line_number_area_width(self, newBlockCount):
        """

        :param newBlockCount:
        """
        self.setViewportMargins(self.line_number_area_width(), 0, 0, 0)

    @Slot()
    def update_line_number_area(self, rect, dy):
        """

        :param rect:
        :param dy:
        """
        if dy:
            self.line_number_area.scroll(0, dy)
        else:
            width = self.line_number_area.width()
            self.line_number_area.update(0, rect.y(), width, rect.height())

        if rect.contains(self.viewport().rect()):
            self.update_line_number_area_width(0)

    @Slot()
    def highlight_current_line(self):
        """

        """
        extra_selections = []

        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()

            # selection.setStyleSheet('background-color: #323232;')
            selection.format.setBackground(QColor(50, 50, 50))

            selection.format.setProperty(QTextFormat.FullWidthSelection, True)

            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()

            extra_selections.append(selection)

        self.setExtraSelections(extra_selections)

    def setPlainText(self, p_str):
        cursor = QTextCursor(self.textCursor())
        cursor.beginEditBlock()
        cursor.select(QTextCursor.Document)
        cursor.insertText(p_str)
        cursor.movePosition(QTextCursor.End)
        cursor.endEditBlock()

    def insertPlainTextAtEnd(self, p_str):
        cursor = QTextCursor(self.textCursor())
        cursor.beginEditBlock()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(p_str)
        cursor.movePosition(QTextCursor.End)
        cursor.endEditBlock()

    def text(self):
        temp = self
        return temp.toPlainText()

class Text:
    """

    """

    def __init__(self, text, selected):
        self.full_text: str = text
        self.selected: str = selected
        self.text: str = text
        if selected:
            self.text: str = selected

class Window(QWidget):
    """

    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qnverter")

        self.resize(800, 800)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.main_layout = QVBoxLayout()
        self.text_box_layout = QHBoxLayout()
        self.titlebar = QHBoxLayout()

        self.text_box_a = CodeEditor()
        self.text_box_b = CodeEditor()
        self.text_box_layout.addWidget(self.text_box_a)
        self.text_box_layout.addWidget(self.text_box_b)

        self.command_button = QPushButton('Command Button')
        self.titlebar.addWidget(self.command_button, 1)

        self.main_layout.addLayout(self.titlebar)
        self.main_layout.addLayout(self.text_box_layout)

        self.setLayout(self.main_layout)

        self.command_button.clicked.connect(self.start_selection)

    def start_selection(self):
        selection_menu = Selection()
        dialogue = QDialog()

        dialogue.setFixedHeight(485)
        dialogue.setFixedWidth(320)
        dialogue.setWindowFlags(Qt.FramelessWindowHint)
        dialogue.setWindowModality(Qt.ApplicationModal)

        centre = (self.x() + (self.frameGeometry().width() // 2) - (320 // 2),
                  self.y() + (self.frameGeometry().height() // 2) - (485 // 2))
        dialogue.move(centre[0], centre[1])

        selection_menu.setParent(dialogue)
        uuid = dialogue.exec()

        if uuid is None:
            return
        script = get_script_from_uuid(uuid)
        if script is None:
            return

        temp = self.text_box_a
        plain_text = temp.toPlainText()
        selected_text = plain_text[temp.textCursor().selectionStart():temp.textCursor().selectionEnd()]
        if isgeneratorfunction(script.event):
            self.text_box_b.setPlainText('')
            try:
                for i in script.event(Text(plain_text, selected_text)):
                    self.text_box_b.insertPlainTextAtEnd(i)
            except Exception as e:
                print('an exeption has occurred', e)
                error_dialog = QErrorMessage()
                error_dialog.showMessage(
                    f'I am vewy sowwy but an exeption occuwed that my pwogwam cannot handle \n hewe awe a few details wegawding the ewwow:\n{e}')
                error_dialog.exec()
        else:
            result = 'error'
            try:
                result = script.event(Text(plain_text, selected_text))
            except Exception as e:
                print('an exeption has occurred', e)
                error_dialog = QErrorMessage()
                error_dialog.showMessage(
                    f'I am vewy sowwy but an exeption occuwed that my pwogwam cannot handle \n hewe awe a few details wegawding the ewwow:\n{e}')
                error_dialog.exec()
            self.text_box_b.setPlainText(str(result))

class Selection(QWidget):
    """

    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("command selection")
        # self.setFixedWidth(320)
        # self.setFixedHeight(640)

        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.main_Layout = QVBoxLayout()
        self.script_Layout = QVBoxLayout()
        self.script_Layout = QVBoxLayout()
        self.script_Layout.setAlignment(Qt.AlignTop)

        self.titlebar = QHBoxLayout()

        self.model = QStringListModel()

        temp = []
        for i in scripts.items:
            temp.extend(i.keys)

        self.model.setStringList(set(temp))
        self.completer = QCompleter()
        self.completer.setModel(self.model)

        self.searchbar = QLineEdit('')
        self.searchbar.textChanged.connect(self.update_items)
        self.searchbar.setCompleter(self.completer)
        self.titlebar.addWidget(self.searchbar, 1)

        self.main_Layout.setAlignment(Qt.AlignTop)
        self.script_Layout.setAlignment(Qt.AlignTop)
        self.titlebar.setAlignment(Qt.AlignRight)

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.main_Layout.addLayout(self.titlebar)
        self.main_Layout.addWidget(self.scroll)

        self.update_items()
        self.setLayout(self.main_Layout)
        self.setMaximumWidth(320)

    def update_items(self):

        for i in get_children(self.script_Layout):
            i.setParent(None)

        for i in scripts.items:
            if self.searchbar.text() is None or search_help(i.keys, self.searchbar.text()):
                self.script_Layout.addWidget(i.itemrender(i))

        self.widget.setLayout(self.script_Layout)
        self.scroll.setWidget(self.widget)

class Item:

    def __init__(self, event, name="example name", tags="some tags spearated by space", icon="icon.png",
                 author="me",
                 description="this description is used to describe some stuff thatb is extra and not really used "
                             "other than for texting but ok"):
        self.event = event
        self.name = name
        self.tags = tags
        self.icon = 'resources/' + icon
        self.author = author
        self.description = description
        self.uuid = randint(-2147483648, 2147483648)
        self.itemrender = Itemrender
        self.keys = [self.name] + self.tags.split(' ')
        try:
            self.keys.remove('')
        except ValueError:
            pass

    def init_render(self):
        self.itemrender(self)

    @staticmethod
    def example(text: Text):
        if text.selected is not None:
            return text.selected
        return text.full_text

class Itemrender(QAbstractButton):
    """

    """
    icon_size = 32

    def __init__(self, item):
        super().__init__(None)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.item = item
        self.main_layout = QHBoxLayout()
        self.main_layout.setAlignment(Qt.AlignLeft)

        self.icon_label = QLabel()
        self.icon = QPixmap(item.icon)
        if self.icon.isNull():
            self.icon = QPixmap('icon.png')
        self.icon = self.icon.scaledToHeight(Itemrender.icon_size)
        self.icon = self.icon.scaledToWidth(Itemrender.icon_size)
        self.icon_label.setPixmap(self.icon)

        self.title = QLabel(item.name)
        self.title.setStyleSheet(''' font-size: 18px; ''')
        self.title.setMaximumWidth(400)
        self.description = QLabel(item.description)
        self.description.setMaximumWidth(400)
        self.label_box = QVBoxLayout()
        self.label_box.addWidget(self.title)
        self.label_box.addWidget(self.description)
        self.label_box.setAlignment(Qt.AlignTop)

        self.main_layout.addWidget(self.icon_label)
        self.main_layout.addSpacing(10)
        self.main_layout.addLayout(self.label_box)
        self.setToolTip(f'author: {self.item.author} [{self.item.tags}]')

        # self.setGeometry(0, 0, 960, self.width())
        # self.resize(self.main_layout.sizeHint())
        self.setLayout(self.main_layout)

        self.title.setWordWrap(True)
        self.description.setWordWrap(True)
        self.title.adjustSize()
        self.description.adjustSize()
        self.clicked.connect(self.mouse_action)
        self.background = QWidget()

        self.label_box.setSpacing(0)
        self.main_layout.setSpacing(0)
        self.setMinimumHeight(self.title.height() + self.description.height())

    def focusInEvent(self, QFocusEvent):
        self.setStyleSheet('background-color: #2F8174;')

    def focusOutEvent(self, QFocusEvent):
        self.setStyleSheet('background-color: #292F34;')

    def mouse_action(self):
        self.parent().parent().parent().parent().parent().done(self.item.uuid)

    def paintEvent(self, QPaintEvent):
        # lol fancul
        pass

def search_help(my_list: list, query: str):
    for i in my_list:
        if query in i or i in query:
            return True
    return False

def get_children(layout):
    return [layout.itemAt(i).widget() for i in range(layout.count())]

def get_script_from_uuid(uuid):
    for i in scripts.items:
        if i.uuid == uuid:
            return i

def command_selection():
    """

    """
    # selection.show()
    pass

def set_scripts():
    for i in scripts.items:
        i.init_render()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    set_scripts()
    window = Window()
    window.show()
    app.exec()
