import pygame
import sys

pygame.init()
clock=pygame.time.Clock()

win_width=700
win_height=600 #dimensions of the window (win)
window=pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("PONG")

w = 119; a = 97; s = 115; d = 100

#rectangles drawings:
ball=pygame.Rect(win_width/2-15, win_height/2-15 ,30,30) #pygame.Rect(x,y,width,height) 
player1=pygame.Rect(win_width-20,win_height/2-50, 10,100)
player2=pygame.Rect(10,win_height/2-50, 10,100)
bgcolor=pygame.Color('black')
grey=(200,200,200)
ball_velocity_xaxis=5
ball_velocity_yaxis=5
player1_velocity=0
player2_velocity=0
player1_score=0
player2_score=0
score_font=pygame.font.Font(None,80) #size of font is 80. None uses default system font

#working mechanisms:
def ball_mechanism():
    global ball_velocity_xaxis,ball_velocity_yaxis
    ball.x+=ball_velocity_xaxis
    ball.y+=ball_velocity_yaxis
    #some collisions with walls of the window:
    if ball.top<=0 or ball.bottom>=win_height:
        ball_velocity_yaxis*=-1 #reverse the ball speed vertically (y axis)
    if ball.left<=0:
        score("player1")
        reset()
    if ball.right>=win_width:
        # ball_velocity_xaxis*=-1 #reverse ball speed horizzontrally (x axis)
        score("player2")
        reset()
    
    #collisons with paddles:
    #rect1.colliderect(rect2)--> no collison returs false and collison  returns true
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_velocity_xaxis*=-1

def player1_mechanism():
    player1.y+=player1_velocity
    if player1.top<=0:
        player1.top=0
    if player1.bottom>=win_height:
        player1.bottom=win_height

def player2_mechanism():
    player2.y+=player2_velocity
    if player2.top<=0:
        player2.top=0
    if player2.bottom>=win_height:
        player2.bottom=win_height

def reset():
    ball.center=(win_width/2, win_height/2)

def score(wins):
    global player1_score, player2_score
    if wins=="player2":
        player2_score+=1
    if wins=="player1":
        player1_score+=1

#pygame.draw(surface, color, rect)
#colors --> (r,g,b) where each r g b range is form 0 to 255. 0-->no color, 255--> pure color  use (r,g,b) or use color object --> pygame.color('name')

while True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT: #for quitting event of the game
            pygame.quit()
            sys.exit()
        #player 1 manual movement
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                player1_velocity+=10
            if event.key==pygame.K_UP:
                player1_velocity-=10
        if event.type==pygame.KEYUP:        
            if event.key==pygame.K_DOWN:
                player1_velocity-=10
            if event.key==pygame.K_UP:
                player1_velocity+=10

        #player2 manual movement
        if event.type==pygame.KEYDOWN:
            if event.key==w:
                player2_velocity-=10
            if event.key==s:
                player2_velocity+=10
        if event.type==pygame.KEYUP:
            if event.key==w:
                player2_velocity+=10
            if event.key==s:
                player2_velocity-=10
            

    ball_mechanism()
    player1_mechanism()
    player2_mechanism()

    window.fill(bgcolor)
    player2_score_surface=score_font.render(str(player2_score), True, "white") #render texts onto the surfaces , true(antialiasing) gives clear visuals of the rendered text else it will be more pixelated
    player1_score_surface=score_font.render(str(player1_score), True, "white")
    window.blit(player2_score_surface,(win_width/4,20)) #blit draws the rendered text  , takes blit(source_surface , destination_surface)
    window.blit(player1_score_surface,(3*win_width/4,20))
    
    pygame.draw.rect(window,grey,player1)
    pygame.draw.rect(window,grey,player2)
    pygame.draw.ellipse(window,grey,ball)
    pygame.display.flip()
    clock.tick(60) #fps