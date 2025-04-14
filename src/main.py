from simulator import *
import pygame

def main():
    pygame.init()
    s = Simulator()
    s.main_loop()
    pygame.quit()

if __name__ == '__main__':
    main()