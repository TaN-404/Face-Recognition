from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, 
                            QGraphicsOpacityEffect, QSizePolicy)
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QMovie, QColor, QPainter

class LoadingOverlay(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_NoSystemBackground)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        # Semi-transparent background
        self.setStyleSheet("background-color: rgba(50, 50, 50, 150);")
        
        # Main layout
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Loading GIF
        self.loading_label = QLabel(self)
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.loading_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # Load and configure the GIF
        self.movie = QMovie("assets/gifs/7efs.gif")
        print(f"GIF valid: {self.movie.isValid()}")
        print(f"Frame count: {self.movie.frameCount()}")
        self.movie.setCacheMode(QMovie.CacheAll)
        self.loading_label.setMovie(self.movie)
        
        layout.addWidget(self.loading_label)
        
        # Initially hidden
        self.hide()

    def showEvent(self, event):
        self.raise_()
        self.movie.start()
        super().showEvent(event)

    def hideEvent(self, event):
        self.movie.stop()
        super().hideEvent(event)

    def paintEvent(self, event):
        """Add semi-transparent overlay"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), QColor(50, 50, 50, 150))