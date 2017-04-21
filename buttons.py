import pygame

import sys


class button1:
        
    but=pygame.image.load("buts/b1.png")
    but=pygame.transform.scale(but,(50,50))
    butno=1
    i=0
    flag=0
    def __init__(self,x,y):
        self.x_axis=x
        self.y_axis=y   
        self.butno=1
        self.i=0
        self.flag=0
    def display(self,gameDisplay):
        gameDisplay.blit(self.but,(self.x_axis,self.y_axis+(0.2*(self.i**2))))
        if self.flag==1:
            self.i+=1
        
        
            
            
            
            

class button2:
        
    but=pygame.image.load("buts/b2.png")
    but=pygame.transform.scale(but,(50,50))
    butno=2
    i=0
    flag=0
    def __init__(self,x,y):
        self.x_axis=x
        self.y_axis=y   
        self.butno=2
        self.i=0
        self.flag=0
    def display(self,gameDisplay):
        gameDisplay.blit(self.but,(self.x_axis,self.y_axis+(0.2*(self.i**2))))
        if self.flag==1:
            self.i+=1
        
        


class button3:
        
    but=pygame.image.load("buts/b3.png")
    but=pygame.transform.scale(but,(50,50))
    butno=3
    i=0
    flag=0
    def __init__(self,x,y):
        self.x_axis=x
        self.y_axis=y   
        self.butno=3
        self.i=0
        self.flag=0
    def display(self,gameDisplay):
        gameDisplay.blit(self.but,(self.x_axis,self.y_axis+(0.2*(self.i**2))))
        if self.flag==1:
            self.i+=1
         
        
            
            
class button4:
        
    but=pygame.image.load("buts/b4.png")
    but=pygame.transform.scale(but,(50,50))
    butno=4
    i=0
    flag=0
    def __init__(self,x,y):
        self.x_axis=x
        self.y_axis=y   
        self.butno=4   
        self.i=0
        self.flag=0
    def display(self,gameDisplay):
        gameDisplay.blit(self.but,(self.x_axis,self.y_axis+(0.2*(self.i**2))))
        if self.flag==1:
            self.i+=1
            
            
            
            
            
            
            
class button5:
        
    but=pygame.image.load("buts/b5.png")
    but=pygame.transform.scale(but,(50,50))
    butno=5
    i=0
    flag=0
    def __init__(self,x,y):
        self.x_axis=x
        self.y_axis=y   
        self.butno=5
        self.i=0
        self.flag=0
    def display(self,gameDisplay):
        gameDisplay.blit(self.but,(self.x_axis,self.y_axis+(0.2*(self.i**2))))
        if self.flag==1:
            self.i+=1
            
            
        
            
            
            
            
class button6:
        
    but=pygame.image.load("buts/b6.png")
    but=pygame.transform.scale(but,(50,50))
    butno=6
    i=0
    flag=0
    def __init__(self,x,y):
        self.x_axis=x
        self.y_axis=y   
        self.butno=6
        self.i=0
        self.flag=0
    def display(self,gameDisplay):
        gameDisplay.blit(self.but,(self.x_axis,self.y_axis+(0.2*(self.i**2))))
        if self.flag==1:
            self.i+=1
            
        
        

class button7:
        
    but=pygame.image.load("buts/b7.png")
    but=pygame.transform.scale(but,(50,50))
    butno=7
    i=0
    flag=0
    def __init__(self,x,y):
        self.x_axis=x
        self.y_axis=y   
        self.butno=7
        self.i=0
        self.flag=0
    def display(self,gameDisplay):
        gameDisplay.blit(self.but,(self.x_axis,self.y_axis+(0.2*(self.i**2))))
        if self.flag==1:
            self.i+=1
            
        
       

