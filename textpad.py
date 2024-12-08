import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QColorDialog, QFontDialog, QMessageBox
)
from PyQt5.QtGui import QIcon, QColor, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSize

class TextPad(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize the text editor
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        # Initialize the GUI components
        self.initUI()

    def initUI(self):
        # Set main window properties
        self.setWindowTitle("TextPad")
        self.setGeometry(100, 100, 800, 600)

        # Create Menu Bar
        self.createMenuBar()

        # Create Tool Bar
        self.createToolBar()

        # Create Status Bar
        self.statusBar().showMessage("Welcome to TextPad!")

    def createMenuBar(self):
        menubar = self.menuBar()

        # File Menu
        fileMenu = menubar.addMenu("File")

        clearAction = QAction("Clear", self)
        clearAction.triggered.connect(self.clearText)
        fileMenu.addAction(clearAction)

        saveAction = QAction("Save", self)
        saveAction.triggered.connect(self.saveFile)
        fileMenu.addAction(saveAction)

        exitAction = QAction("Exit", self)
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        # Edit Menu
        editMenu = menubar.addMenu("Edit")

        cutAction = QAction("Cut", self)
        cutAction.triggered.connect(self.textEdit.cut)
        editMenu.addAction(cutAction)

        copyAction = QAction("Copy", self)
        copyAction.triggered.connect(self.textEdit.copy)
        editMenu.addAction(copyAction)

        pasteAction = QAction("Paste", self)
        pasteAction.triggered.connect(self.textEdit.paste)
        editMenu.addAction(pasteAction)

        # Format Menu
        formatMenu = menubar.addMenu("Format")

        fontAction = QAction("Font", self)
        fontAction.triggered.connect(self.selectFont)
        formatMenu.addAction(fontAction)

        colorAction = QAction("Color", self)
        colorAction.triggered.connect(self.selectColor)
        formatMenu.addAction(colorAction)

        # Help Menu
        helpMenu = menubar.addMenu("Help")

        aboutAction = QAction("About", self)
        aboutAction.triggered.connect(self.showAbout)
        helpMenu.addAction(aboutAction)

    def createToolBar(self):
        toolbar = self.addToolBar("Toolbar")

        toolbar.setIconSize(QSize(15, 15))

        # File toolbar actions
        clearIcon = QIcon("C:/Users/Adwait/OneDrive/Desktop/Projects/NIELIT/TextPadProject/ToolBarImages/clear.png")
        clearAction = QAction(clearIcon, "Clear", self)
        clearAction.triggered.connect(self.clearText)
        toolbar.addAction(clearAction)

        saveIcon = QIcon("C:/Users/Adwait/OneDrive/Desktop/Projects/NIELIT/TextPadProject/ToolBarImages/save.png")
        saveAction = QAction(saveIcon, "Save", self)
        saveAction.triggered.connect(self.saveFile)
        toolbar.addAction(saveAction)

        exitIcon = QIcon("C:/Users/Adwait/OneDrive/Desktop/Projects/NIELIT/TextPadProject/ToolBarImages/exit.png")
        exitAction = QAction(exitIcon, "Exit", self)
        exitAction.triggered.connect(self.close)
        toolbar.addAction(exitAction)

        toolbar.addSeparator()

        # Edit toolbar actions
        cutIcon = QIcon("C:/Users/Adwait/OneDrive/Desktop/Projects/NIELIT/TextPadProject/ToolBarImages/cut.png")
        cutAction = QAction(cutIcon, "Cut", self)
        cutAction.triggered.connect(self.textEdit.cut)
        toolbar.addAction(cutAction)

        copyIcon = QIcon("C:/Users/Adwait/OneDrive/Desktop/Projects/NIELIT/TextPadProject/ToolBarImages/copy.png")
        copyAction = QAction(copyIcon, "Copy", self)
        copyAction.triggered.connect(self.textEdit.copy)
        toolbar.addAction(copyAction)

        pasteIcon = QIcon("C:/Users/Adwait/OneDrive/Desktop/Projects/NIELIT/TextPadProject/ToolBarImages/paste.png")
        pasteAction = QAction(pasteIcon, "Paste", self)
        pasteAction.triggered.connect(self.textEdit.paste)
        toolbar.addAction(pasteAction)

        toolbar.addSeparator()

        # Format toolbar actions
        fontIcon = QIcon("C:/Users/Adwait/OneDrive/Desktop/Projects/NIELIT/TextPadProject/ToolBarImages/font.png")
        fontAction = QAction(fontIcon, "Font", self)
        fontAction.triggered.connect(self.selectFont)
        toolbar.addAction(fontAction)

        colorIcon = QIcon("C:/Users/Adwait/OneDrive/Desktop/Projects/NIELIT/TextPadProject/ToolBarImages/color.png")
        colorAction = QAction(colorIcon, "Color", self)
        colorAction.triggered.connect(self.selectColor)
        toolbar.addAction(colorAction)

    def clearText(self):
        self.textEdit.clear()
        self.statusBar().showMessage("Text cleared", 2000)

    def saveFile(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if filePath:
            with open(filePath, 'w') as file:
                file.write(self.textEdit.toPlainText())
            self.statusBar().showMessage("File saved", 2000)

    def selectFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)
            self.statusBar().showMessage("Font selected", 2000)

    def selectColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.textEdit.setTextColor(color)
            self.statusBar().showMessage("Color selected", 2000)

    def showAbout(self):
        QMessageBox.about(self, "About TextPad", "This is a simple text editor built using PyQt.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    textPad = TextPad()
    textPad.show()
    sys.exit(app.exec_())
