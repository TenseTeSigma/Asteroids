from constants import *

class ScoreTracker():
  def __init__(self):

    self.player_score = 0
    self.score_on_kill = 2 
    
  def add_score(self):
    self.player_score = self.player_score + self.score_on_kill
      
  def streak(self):
    if self.player_score == 40:
      self.score_on_kill *= 2
      
    if self.player_score == 100:
      self.score_on_kill *= 2

  def end_score(self):
    print(f"Your final score was {self.player_score}")
    self.player_score = 0
