from constants import *

class MusicLoader():
  def __init__(self):

    def load_start_music(self):
        pygame.mixer.music.load("/home/tense/workspace/github.com/TenseTeSigma/Audios/Darius.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    
    def load_lose_music(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load("/home/tense/workspace/github.com/TenseTeSigma/Audios/Ending.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()