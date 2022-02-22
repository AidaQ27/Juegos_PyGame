import pygame as pg
import random 
pg.init()


class Raqueta:
    def __init__(self, padre, x, y, ancho, alto, color = (255, 200, 85)):
        self.padre = padre
        self.x = x
        self.y = y
        self.color = color
        self.ancho = ancho
        self.alto = alto
        self.vx = 5
        self.vy = 0

    def dibujar(self):
        pg.draw.rect(self.padre, self.color, (self.x, self.y, self.ancho, self.alto))

class Bola:
    def __init__(self, x, y, padre,  color = (255, 255, 255), radio = 10, vx = 5, vy = 0):
        self.x = x
        self.y = y
        self.color = color
        self.radio = radio
        self.vx = 1
        self.vy = 1
        self.padre = padre
        

    def mover(self):
        self.x += self.vx 
        self.y += self.vy


        if self.x <= self.radio or self.x >= self.padre.get_width() - self.radio:
            self.vx *= -1

        #if self.radio >= self.x >= limDer - self.radio:

        if self.y <= self.radio or self.y >= self.padre.get_height() - self.radio:
            self.vy *= -1

    def dibujar(self):
        pg.draw.circle(self.padre, self.color, (self.x, self.y), self.radio)



class Game:
    def __init__(self, ancho=600, alto=800):
        self.pantalla = pg.display.set_mode((ancho, alto))
        self.bola = Bola(ancho // 2, alto // 2, self.pantalla, (255, 255, 0))
        self.raqueta = Raqueta(self.pantalla, ancho//2, alto - 30, 100, 25)

        """
        self.bolas = []
        num_bolas = random.randint(0, 50)
        for i in range(num_bolas):
            self.nueva_bola = Bola(random.randint(0,600), random.randint(0,800), self.pantalla, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), random.randint(10, 35))
            self.nueva_bola.vx = random.randint(-5, 1)
            self.nueva_bola.vy = random.randint(-5, 1)
            self.bolas.append(self.nueva_bola)
        """
        
        
    def bucle_ppal(self):
        game_over = False

        while not game_over:

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True

                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_LEFT:
                        self.raqueta.vx = -5

                    if evento.key == pg.K_RIGHT:
                        self.raqueta.vx = 5
                
                if evento.type == pg.KEYUP:
                    if evento.key in (pg.K_LEFT)



            
            

        
            #for i in range(len(self.bolas)):
                #self.bolas[i].mover()

                
            self.pantalla.fill((255, 0, 0))    
            self.bola.mover()
            self.bola.dibujar()
            self.raqueta.dibujar()
            
            #for i in range(len(self.bolas)):
                #self.bolas[i].dibujar()
            
            
            pg.display.flip()

    
if __name__ == '__main__':
    pg.init()

    game = Game()
    game.bucle_ppal()

    pg.quit()
    