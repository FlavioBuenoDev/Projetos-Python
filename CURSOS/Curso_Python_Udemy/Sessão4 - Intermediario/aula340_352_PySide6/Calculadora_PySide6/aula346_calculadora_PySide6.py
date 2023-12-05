import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel  # type: ignore # noqa 
# from PySide6.QtWidgets import QApplication, QLabel #type: ignore #noqa 


def temp_label(texto):
    """Creates a label with text."""
    label1 = QLabel(texto) # Initialize label
    label1.setStyleSheet('font-size: 150px;') # Set font size
    return label1  # Return created label


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow(parent=None)  # type: ignore
    window.addWidgetToVLayout(temp_label('Label 1'))
    
    window.adjustFixedSize()

    window.show()
    app.exec()

    