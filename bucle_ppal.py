import pygame as pg

pg.init()

pantalla = pg.display.set_mode((600, 800))

game_over = False

x= 300
y = 400

velocidad_x = 5
velocidad_y = 7

while not game_over:
    # Primero: procesar eventos
    eventos = pg.event.get()
    for evento in eventos:
        if evento.type == pg.QUIT:
            game_over = True
        
    # Modificar los objetos del juego
    x += velocidad_x
    y += velocidad_y

    if x >= 600 - 10 or x <= 0 + 10:  #(-10)El radio de la bola, para que no se hunda en la pantalla.
        velocidad_x *= -1
    if y >= 800 - 10 or y <= 0 + 10:
        velocidad_y *= -1
    

    
    # Aqui no hay nada que hacer
    

    # Refrescar la pantalla
    pantalla.fill((255, 0, 0))
    bola = pg.draw.circle(pantalla, (255, 255, 0), (x, y), 10)
   

    pg.display.flip()

pg.quit()

    

