"""Test the hello app"""

from pytestqt.qt_compat import qt_api

from hello import HelloWidget

def test_hello(qtbot):
    """test clicking changes a label"""
    widget = HelloWidget()
    qtbot.addWidget(widget)

    # click in the Greet button and make sure it updates the appropriate label
    qtbot.mouseClick(widget.button_greet, qt_api.QtCore.Qt.MouseButton.LeftButton)

    assert widget.greet_label.text() == "Hello!"
