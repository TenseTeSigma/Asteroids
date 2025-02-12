import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
import sys
from shots import Shot, Missle
from scoring import ScoreTracker
import time
from music import MusicLoader

def main():
    pygame.init()
    pygame.mixer.init()
    running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    shots = pygame.sprite.Group()
    missles = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable, missles)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    score_tracker = ScoreTracker()
    music_tracker = MusicLoader()

    bg = pygame.image.load("/home/tense/workspace/github.com/TenseTeSigma/Images/Stars.jpg")
    
    player_lives = 3
    music_tracker.load_start_music()

    while running:
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_CAPSLOCK: #Exit if  key is pressed
                    running = False         

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if player.is_collide(asteroid):
                asteroid.kill()
                player.reset_position(asteroid)
                player_lives = player_lives - 1

                if player_lives <= 0:
                    music_tracker.load_lose_music()
                    bg = pygame.image.load("/home/tense/workspace/github.com/TenseTeSigma/Images/GameOver.jpg")
                    screen.blit(bg,(0,0))
                    pygame.display.update()
                    print("GAME OVER!, You ran out of lives.")
                    score_tracker.end_score()
                    time.sleep(3)
                    pygame.quit()
                    sys.exit()
                else:
                    print(f'You lost a life you have: {player_lives} lives remaining.')

        for asteroid in asteroids:
            for shot in shots: 
                if shot.is_collide(asteroid):
                    shot.remove()
                    asteroid.split()
                    score_tracker.add_score()
                    score_tracker.streak()
        
        for asteroid in asteroids:
            for missle in missles:
                if missle.is_collide(asteroid):
                    missle.remove()
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