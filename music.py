from constants import *
import pygame

class MusicLoader():
  
    def load_start_music(self):
        pygame.mixer.music.load("/home/tense/workspace/github.com/TenseTeSigma/Audios/SpaceWave.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
    
    def load_lose_music(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load("/home/tense/workspace/github.com/TenseTeSigma/Audios/Ending.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()