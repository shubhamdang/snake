import pygame
import random
import time
pygame.init()																					
font=pygame.font.SysFont(None,20)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,138,255)
clock=pygame.time.Clock()
display_width=1000
display_height=600
screen=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("first")
a=False
lx=display_width/2
ly=display_height/2
l=0
k=0
FPs=10000
block_size=10
def snake(block_size,snakelist):
	for XnY in snakelist:
		pygame.draw.rect(screen,red,[XnY[0],XnY[1],block_size,block_size])
def message(msg,color):
	screentext=font.render(msg,True,color)
	screen.blit(screentext,[(display_width/2)-30,display_height/2])
def score(msg,color):
	screentext=font.render(msg,True,color)
	screen.blit(screentext,[970,10])
def gameloop():
	display_width=1000
	display_height=600
	screen=pygame.display.set_mode((display_width,display_height))
	pygame.display.set_caption("first")
	a=False
	lx=display_width/2
	ly=display_height/2
	l=0
	k=0
	FPs=30
	block_size=10
	gameover=False
	snakelist=[]
	snakelength=1
	q=0
	applex=round(random.randrange(0,display_width-block_size)/10.0)*10.0
	appley=round(random.randrange(0,display_height-block_size)/10.0)*10.0
	while  not a:
		while gameover == True:
		    screen.fill(white)
		    message(" GAME OVER ! press c to continue and q to quit",red)
		    pygame.display.update() 
		    for event in pygame.event.get():
		    	if event.type==pygame.QUIT:
		    		gameover=False
		        	a=True	
		        if event.type==pygame.KEYDOWN :
		        	if event.key==pygame.K_q:
		        		gameover=False
		        		a=True
		        	if event.key==pygame.K_c:
		        		gameloop()
		for event in pygame.event.get():
			print(event)
			if event.type==pygame.QUIT:
				a=True
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_LEFT:
					l=-block_size
					k=0
				elif event.key==pygame.K_RIGHT:
					l=block_size
					k=0
				elif event.key==pygame.K_UP:
					k=-block_size
					l=0
				elif event.key==pygame.K_DOWN:
					k=block_size
					l=0
			# if event.type==pygame.KEYUP:
			# 	if event.key==pygame.K_LEFT or event.key== pygame.K_RIGHT:
			# 		l=0
		if lx >=display_width  or lx<=0 or ly>=display_height or ly<=0 :
			gameover=True
		lx+=l
		ly+=k
		screen.fill(white)
		snakehead=[]
		snakehead.append(lx)
		snakehead.append(ly)
		snakelist.append(snakehead)
		if len(snakelist) >snakelength:
			del snakelist[0]
		for eachelement in snakelist[:-1]:
			if eachelement== snakehead:
				gameover=True


		snake(block_size,snakelist)
		pygame.draw.rect(screen,green,[applex,appley,block_size,block_size])
		score(str(q),red)
		pygame.display.update()
		if lx==applex and ly==appley:
			applex=round(random.randrange(0,display_width-block_size)/10.0)*10.0
			appley=round(random.randrange(0,display_height-block_size)/10.0)*10.0
			snakelength+=1
			q+=10
	
		clock.tick(FPs)
	message("B Bye!.........",red)
	pygame.display.update()
	time.sleep( 0.5)
	pygame.quit()
	quit()

gameloop()







