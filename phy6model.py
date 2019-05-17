import pygame 
import math
pygame.init()
h=700
w=700
win=pygame.display.set_mode((h,w))
pygame.display.set_caption("simple_phy6")
class ball(object):
	def __init__(self,x,y,ax,ay,color,radius,nu,mass):
		self.x=x
		self.y=y
		self.ax=ax
		self.ay=ay
		self.color=color
		self.radius=radius
		self.nu=0.7
		self.mass=mass*10
		self.velx=5
		self.vely=5
		self.speed=math.sqrt(self.velx**2 + self.vely**2)
		self.dirx=0
		self.diry=0
		self.collision=0
	def __draw__(self,win):
		if self.x>=w-self.radius :
			self.x=w-self.radius
		if self.x<=self.radius:
			self.x=self.radius
		if self.y>=h-self.radius:
			self.y=h-self.radius
		if self.y<self.radius:
			self.y=self.radius
		pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)
		pygame.display.update()
		win.fill((0,0,0))
	def frictionx(self):
		self.ax=5
		self.velx=self.velx-self.ax
		if self.velx<=0:
			self.dirx=0
			self.velx=0
			self.ax=ax
			return
		if self.dirx==-1:
			self.x=self.x-self.velx
		if self.dirx==1:
			self.x=self.x+self.velx		
	def frictiony(self):
		self.ay=5
		self.vely=self.vely-self.ay
		if self.vely<=0:
			self.diry=0
			self.vely=0
			self.ay=ay
			return
		if self.diry==-1:
			self.y=self.y+self.vely
		if self.diry==1:
			self.y=self.y-self.vely
	def __coll__(self):
		self.collision=1
		if self.x==w-self.radius or self.x==self.radius:
			while self.velx>0:
				self.frictionx()
				self.frictiony()
				self.x=int(self.x)
				self.y=int(self.y)
				self.__draw__(win)
				pygame.time.delay(40)
				print (self.velx)
		if self.y==h-self.radius or self.y==self.radius:
			while self.vely>0:
				self.frictiony()
				self.frictionx()
				self.y=int(self.y)
				self.x=int(self.x)
				self.__draw__(win)
				pygame.time.delay(40)
				print (self.vely)	
run=True
bot1=ball(50,50,3,3,(255,0,0),20,1,1)
ax=bot1.ax
vx=bot1.velx
vy=bot1.vely
ay=bot1.ay
while run:
	pygame.time.delay(50)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run=False
	keys=pygame.key.get_pressed()
	if bot1.x==w-bot1.radius:
		bot1.dirx=-1
		bot1.__coll__()
	if bot1.x==bot1.radius:
		bot1.dirx=1
		bot1.__coll__()
	if bot1.y==h-bot1.radius:
		bot1.diry=1
		bot1.__coll__()
	if bot1.y==bot1.radius:
		bot1.diry=-1
		bot1.__coll__()
	if keys[pygame.K_RIGHT] :
		bot1.velx=bot1.velx+bot1.ax
		bot1.x=bot1.x+bot1.velx
		bot1.dirx=1
	if not keys[pygame.K_RIGHT] and bot1.dirx==1:
		bot1.frictionx()
	if keys[pygame.K_LEFT] and bot1.x>bot1.radius:
		bot1.velx=bot1.velx+bot1.ax		
		bot1.x=bot1.x-bot1.velx
		bot1.dirx=-1
	if not keys[pygame.K_LEFT] and bot1.dirx==-1:
		bot1.frictionx()	
	if keys[pygame.K_UP] and bot1.y>=bot1.radius:
		bot1.vely=bot1.vely+bot1.ay
		bot1.y=bot1.y-bot1.vely
		bot1.diry=1
	if not keys[pygame.K_UP] and bot1.diry==1:
		bot1.frictiony()
	if keys[pygame.K_DOWN] and bot1.y<=h-bot1.radius:
		bot1.vely=bot1.vely+bot1.ay
		bot1.y=bot1.y+bot1.vely
		bot1.diry=-1
	if not keys[pygame.K_DOWN] and bot1.diry==-1:
		bot1.frictiony()
	if bot1.x>w-bot1.radius:
		bot1.x=w-bot1.radius
	if bot1.x<bot1.radius:
		bot1.x=bot1.radius
	if bot1.y>h-bot1.radius:
		bot1.y=h-bot1.radius
	if bot1.y<bot1.radius:
		bot1.y=bot1.radius
	bot1.x=int(bot1.x)
	bot1.y=int(bot1.y)
	bot1.__draw__(win)
	
pygame.quit()

