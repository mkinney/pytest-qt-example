from pytestqt.qt_compat import qt_api

from messageboxex import Window

def test_app(qtbot):
    widget = Window()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.btn1, qt_api.QtCore.Qt.MouseButton.LeftButton)
    assert widget.label.text() == "About clicked"
