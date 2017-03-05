import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

class MenuBar(QtGui.QMainWindow):
   def __init__(self):
        super(MenuBar, self).__init__()
        
        self.initUI()
                    

   def initUI(self):

      self.setGeometry(50,50,500,300)
      self.setWindowTitle("PYQT tut")
      self.setWindowIcon(QtGui.QIcon('pylogo.png'))

     
      exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
      exitAction.setShortcut('Ctrl+Q')
      exitAction.setStatusTip('Exit application')
      exitAction.triggered.connect(QtGui.qApp.quit)
   
      openEditor = QtGui.QAction('&Editor',self)
      openEditor.setShortcut('Ctrl+E')
      openEditor.setStatusTip('Open Editor')
      openEditor.triggered.connect(self.editor)



      openFile = QtGui.QAction('&Open File',self)
      openFile.setShortcut('Ctrl+O')
      openFile.setStatusTip('Open File')
      openFile.triggered.connect(self.file_open)


      
      

      saveFile = QtGui.QAction('&Save File',self)
      saveFile.setShortcut('Ctrl+S')
      saveFile.setStatusTip('Save File')
      saveFile.triggered.connect(self.file_save)


      
      


      mainmenu = self.menuBar()
      file_menu = mainmenu.addMenu('File')
      edit_menu = mainmenu.addMenu('Edit')
      view_menu = mainmenu.addMenu('View')
      theme_menu = mainmenu.addMenu('Theme')



      

      file_menu.addAction(openFile)
      file_menu.addAction(saveFile)
      file_menu.addAction(exitAction)

      edit_menu.addAction(openEditor)

      self.setWindowTitle("PYQT tut")
      self.show()

   def file_open(self):
      name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
      file = open(name,'r')

      self.editor()

      with file:
         text = file.read()
         self.textEdit.setText(text)

   def editor(self):
      self.textEdit = QtGui.QTextEdit()
      self.setCentralWidget(self.textEdit)

   def file_save(self):
      name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
      file = open(name,'w')
      text = self.textEdit.toPlainText()
      file.write(text)
      file.close()


   
def main():
    
   app = QtGui.QApplication(sys.argv)
   ex = MenuBar()
   sys.exit(app.exec_())


if __name__ == '__main__':
    main()    