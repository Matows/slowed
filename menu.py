import sys
import pygame as pg
from constants import font as slowed_font
from constants import BLACK, RED, GREEN, BLUE, WHITE, GREY, FPS

class Button():

    def __init__(self, x, y, text, color, center=True, width=300, height=75, font=slowed_font):
        self.text = text
        self.color = color

        self.image = pg.Surface((width, height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        self.text_surface = font.render(text, True, (255,255,255))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.centerx = self.rect.centerx
        self.text_rect.centery = self.rect.centery
        self.image.blit(self.text_surface, self.text_rect)

        if center:
            self.rect.centerx = x
            self.rect.centery = y
        else:
            self.rect.x = x
            self.rect.y = y

    def hoover(self, mx, my):
        return self.rect.collidepoint(mx, my)

    def draw(self, surface):
        self.image.blit(self.text_surface, self.text_rect)
        surface.blit(self.image, self.rect)

def main_menu(screen):
    WIDTH, HEIGHT = screen.get_size()

    classique = Button(WIDTH // 2, HEIGHT // 2 - 100, 'Classique', BLUE)
    contremontre = Button(WIDTH // 2, HEIGHT // 2 , 'Contre la montre', RED)
    quitter = Button(WIDTH // 2, HEIGHT // 2 + 100, 'Quitter', GREY)

    click = False

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                click = True

        mx, my = pg.mouse.get_pos()

        if classique.hoover(mx, my):
            if click:
                game(screen, True)
        if contremontre.hoover(mx, my):
            if click:
                game(screen, False)
        if quitter.hoover(mx, my):
            if click:
                pg.quit()
                sys.exit()

        screen.fill((0,0,0))

        myfont = pg.font.Font(None, 40)
        textSurface = myfont.render("SLOWED", True, (255,255,255))
        textRect = textSurface.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 2 - 200)

        classique.draw(screen)
        contremontre.draw(screen)
        quitter.draw(screen)

        click = False

        screen.blit(textSurface, textRect)
        pg.display.update()
        pg.time.Clock().tick(FPS)
