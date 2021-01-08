# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 10:49:42 2021

@author: leo
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QTranslator
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, 
                             QTabWidget, QMenuBar, QMenu, QAction,
                             QActionGroup, QVBoxLayout, QHBoxLayout, 
                             QLabel,
                             QPushButton,
                             QTreeWidget,
                             QTreeWidgetItem,
                             QFrame)

 
class DemoTabWidget(QMainWindow):
    def __init__(self, parent=None):
        super(DemoTabWidget, self).__init__(parent)   
        
        self.setWindowTitle(self.tr('Collection') )     
        self.resize(480, 360)
      
        self.initUi()
        
    def initUi(self):        
        self.initMenu()
        self.status=self.statusBar() #创建状态栏
        
        self.tw = QTabWidget(self)
        self.tw.addTab(self.createWidget(0), self.tr('常规'))
        self.tw.addTab(self.createWidget(1), self.tr('快捷方式'))
        self.tw.addTab(self.createWidget(2), self.tr('兼容性'))
        self.tw.addTab(self.createWidget(3), self.tr('安全'))
        self.tw.addTab(self.createWidget(4), self.tr('详细信息'))
        self.tw.addTab(self.createWidget(5), self.tr('以前的版本'))
        self.tw.addTab(self.createTabWiget(6),self.tr('帧框'))
        
        self.setCentralWidget(self.tw)
        
            
    def initMenu(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu(self.tr('文件'))
        aExit = QAction(self.tr('Exit'), self)
        aExit.triggered.connect(self.close)
        fileMenu.addAction(aExit)
        
        posMenu = menuBar.addMenu(self.tr('标签条位置'))
        
        aNorth = QAction(self.tr('上方'), self)
        aNorth.setCheckable(True)
        aNorth.setChecked(True)
        aNorth.triggered.connect(lambda:self.changeTabPos(0))
        aSouth = QAction(self.tr('下方'), self)
        aSouth.setCheckable(True)
        aSouth.triggered.connect(lambda:self.changeTabPos(1))
        aWest = QAction(self.tr('左边'), self)
        aWest.setCheckable(True)
        aWest.triggered.connect(lambda:self.changeTabPos(2))
        aEast = QAction(self.tr('右边'), self)
        aEast.setCheckable(True)
        aEast.triggered.connect(lambda:self.changeTabPos(3))
    
        posGroup = QActionGroup(self)
        posGroup.addAction(aNorth)
        posGroup.addAction(aSouth)
        posGroup.addAction(aWest)
        posGroup.addAction(aEast)
        
        posMenu.addAction(aNorth)
        posMenu.addAction(aSouth)
        posMenu.addAction(aWest)
        posMenu.addAction(aEast)
        
        #标签条形状
        shapeMenu = menuBar.addMenu(self.tr('标签条形状'))
        aRounded = QAction(self.tr('圆角矩形'), self)
        aRounded.setCheckable(True)
        aRounded.setChecked(True)
        aRounded.triggered.connect(lambda:self.changeTabShape(0))
        aTriangular = QAction(self.tr('三角形'), self)
        aTriangular.setCheckable(True)
        aTriangular.triggered.connect(lambda:self.changeTabShape(1))
        
        shapeGroup = QActionGroup(self)
        shapeGroup.addAction(aRounded)
        shapeGroup.addAction(aTriangular)
        
        shapeMenu.addAction(aRounded)
        shapeMenu.addAction(aTriangular)
        
    def changeTabPos(self, index):
        switcher = {
            0: QTabWidget.North,
            1: QTabWidget.South,
            2: QTabWidget.West,
            3: QTabWidget.East
        }
        self.tw.setTabPosition(switcher.get(index))
        
    def changeTabShape(self, index):
        if index == 0:
            self.tw.setTabShape(QTabWidget.Rounded)
        else:
            self.tw.setTabShape(QTabWidget.Triangular)
            
    def createWidget(self, index):
        wid = QWidget()
        layout = QVBoxLayout(wid)
        label = QLabel(wid)
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont(self.font().family(), 36))
        label.setText(self.tr("选项卡 {}").format(index + 1))
        
        layout.addWidget(label)
        wid.setLayout(layout)
        return wid
    
    def createSettingsTabWiget( self , index):
       wid = QWidget()                
       funLayout = QHBoxLayout(wid)
       
       hwFrame =  QFrame( )
       hwFrame.setFrameStyle(QFrame.Box|QFrame.Raised)        
       recorderFrame =  QFrame( )
       recorderFrame.setFrameStyle(QFrame.Box|QFrame.Raised)           
       playFrame =  QFrame( )
       
       playFrame.setFrameStyle(QFrame.Box|QFrame.Raised)          
       buttonFrame =  QFrame( )
       buttonLayout = QVBoxLayout()
       buttonFrame.setLayout(buttonLayout)
       buttonNameList = [self.tr("settings"),self.tr("start"),self.tr("covert")]
           
       btn_settings = QPushButton(buttonNameList[0])           
       buttonLayout.addWidget(btn_settings)
       btn_start = QPushButton(buttonNameList[1])           
       buttonLayout.addWidget(btn_start)  
       btn_covert = QPushButton(buttonNameList[2])           
       buttonLayout.addWidget(btn_covert) 
       buttonLayout.addStretch(0)       
       
       funLayout.addWidget(hwFrame)
       funLayout.addWidget(recorderFrame)
       funLayout.addWidget(playFrame)
       funLayout.addWidget(buttonFrame)
       funLayout.setStretch(0, 4)
       funLayout.setStretch(1, 4)
       funLayout.setStretch(2, 4)       
       funLayout.setStretch(3, 1)
       
       return wid
    
    def createTabWiget(self,index):
       wid = QWidget() 
       layout = QHBoxLayout(wid)      

       ########################################################################
       treeLayout = QHBoxLayout()       
       treeframe = QFrame( )
       treeframe.setFrameStyle(QFrame.Box|QFrame.Raised) 
       treeframe.setLayout(treeLayout)             
       layout.addWidget(treeframe)
                   
       rightframe = QFrame( )
       rightframe.setFrameStyle(QFrame.Box|QFrame.Raised)  
       layout.addWidget(rightframe) 
       ########################################################################
       wid.setLayout(layout) 
       
       layout.setStretch(0, 2)
       layout.setStretch(1, 11)
       
   
       twSetting = QTabWidget(rightframe)

       twSetting.addTab(self.createSettingsTabWiget(0), self.tr('collection'))

       
       return wid
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoTabWidget()
    window.show()
    sys.exit(app.exec())
