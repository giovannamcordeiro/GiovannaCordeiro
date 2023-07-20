import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus, LargeCactus
#from dino_runner.components.obstacles.pipe import SmallPipe, LargePipe
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import BIRD, SMALL_CACTUS, LARGE_CACTUS


class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:      
            if random.randint(0, 2) == 0:
              self.obstacles.append(Bird(BIRD))
            elif random.randint(0, 2) == 1:
               self.obstacles.append(Cactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 2:
               self.obstacles.append(LargeCactus(LARGE_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)   
            if game.player.dino_rect.colliderect(obstacle.rect):
              if not game.player.has_power_up:
                pygame.time.delay(500)
                game.playing = False
                game.death_count += 1
                break
              else:
                self.obstacles.remove(obstacle)
 
    def reset_obstacles(self):
        self.obstacles = []
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)        