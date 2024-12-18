import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
import sys
from shots import Shot
from scoring import ScoreTracker
import time


def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.mixer.music.load("/home/tense/workspace/github.com/TenseTeSigma/Audios/Darius.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    score_tracker = ScoreTracker()

    bg = pygame.image.load("/home/tense/workspace/github.com/TenseTeSigma/Images/Sigmas.jpg")
    
    player_lives = 3

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if player.is_collide(asteroid):
                asteroid.kill()
                player.reset_position()
                player_lives = player_lives - 1
                if player_lives <= 0:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("/home/tense/workspace/github.com/TenseTeSigma/Audios/Ending.mp3")
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play()
                    bg = pygame.image.load("/home/tense/workspace/github.com/TenseTeSigma/Images/GameOver.jpg")
                    screen.blit(bg,(0,0))
                    pygame.display.update()
                    print("GAME OVER!, You ran out of lives.")
                    score_tracker.end_score()
                    time.sleep(5)
                    pygame.quit()
                    score_tracker.reset_score()
                    sys.exit()
                else:
                    print(f'You lost a life you have: {player_lives} lives remaining.')
                    player.draw(screen)

        for asteroid in asteroids:
            for shot in shots: 
                if shot.is_collide(asteroid):
                    shot.remove()
                    asteroid.split()
                    score_tracker.add_score()
                    score_tracker.streak()

        screen.fill("black")
        screen.blit(bg,(0,0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(144) / 1000
 
if __name__ == "__main__":
    main()