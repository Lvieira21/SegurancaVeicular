from PyQt5.Qt import QThread
from pygame import mixer

class Alerta(QThread):
    
    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
        
    def __del__(self):
        self.wait()
        
    def run(self):
        mixer.music.load("Beep\\beep.mp3")
        mixer.music.play()