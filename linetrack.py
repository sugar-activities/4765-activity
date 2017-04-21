import pygame
import sys


class linetrack:
    
    verticalup=0
    verticaldown=0
    horizontalleft=0
    horizontalright=0
    leftdiagup=0
    leftdiagdown=0
    
    rightdiagup=0
    rightdiagdown=0
    
    buttonx=0
    buttony=0
    flag=0
    
    
    def __init__(self,button,buttonslist):
        
        self.verticalup=(button.x_axis,button.y_axis)
        self.verticaldown=(button.x_axis,button.y_axis)
        
        self.horizontalleft=(button.x_axis,button.y_axis)
        self.horizontalright=(button.x_axis,button.y_axis)
        
        self.leftdiagup=(button.x_axis,button.y_axis)
        self.leftdiagdown=(button.x_axis,button.y_axis)
        
        self.rightdiagup=(button.x_axis,button.y_axis)
        self.rightdiagdown=(button.x_axis,button.y_axis)
        
        tempx1=0
        tempy1=0
        
        tempx2=0
        tempy2=0
        i=25
        
        self.buttonx=button.x_axis+i
        self.buttony=button.y_axis+i
        
        self.flag=0
        
        # For horizontal check
        tempx1=button.x_axis
        tempy1=button.y_axis
        f=0
        while(tempx1>=370+280):
            
            for i in buttonslist:
                if(i.y_axis==tempy1 and i.x_axis==tempx1 and button.butno==i.butno):
                    self.horizontalleft=(tempx1,button.y_axis)
                if(i.y_axis==tempy1 and i.x_axis==tempx1 and button.butno!=i.butno):
                    f=1
                    break
            
            if f==1:
                break
                
            tempx1-=65
        
        
        tempx1=button.x_axis
        tempy1=button.y_axis
        f=0
        while(tempx1<=630+280):
            
            for i in buttonslist:
                if(i.y_axis==tempy1 and i.x_axis==tempx1 and button.butno==i.butno):
                    self.horizontalright=(tempx1,button.y_axis)
                if(i.y_axis==tempy1 and i.x_axis==tempx1 and button.butno!=i.butno):
                    f=1
                    break
                  
            if f==1:
                break
                    
            tempx1+=65
            
            
            
        # For vertical check
        tempx1=button.x_axis
        tempy1=button.y_axis
        f=0
        while(tempy1>=235):
            for i in buttonslist:
                if(i.x_axis==tempx1 and i.y_axis==tempy1 and button.butno==i.butno):
                    self.verticalup=(button.x_axis,tempy1)
                if(i.x_axis==tempx1 and i.y_axis==tempy1 and button.butno!=i.butno):
                    f=1
                    break
                  
            if f==1:
                break
            
                 
            tempy1-=65
            
            
            
        tempx1=button.x_axis
        tempy1=button.y_axis
        
        f=0
        while(tempy1<=495):
            for i in buttonslist:
                if(i.x_axis==tempx1 and i.y_axis==tempy1 and button.butno==i.butno):
                    self.verticaldown=(button.x_axis,tempy1)
                if(i.x_axis==tempx1 and i.y_axis==tempy1 and button.butno!=i.butno):
                    f=1
                    break
                  
            if f==1:
                break
            
            tempy1+=65
            
            
            
        
        # For left Diagonal check
        tempx1=button.x_axis
        tempy1=button.y_axis
        total=button.x_axis+button.y_axis
        diff=button.x_axis-button.y_axis
        
        f=0
        while(tempx1>=370+280 and tempy1>=235):
            
            for i in buttonslist:
                if((tempx1-tempy1)==diff and i.x_axis==tempx1 and i.y_axis==tempy1 and button.butno==i.butno):
                   self.leftdiagup=(tempx1,tempy1)
                if((tempx1-tempy1)==diff and i.x_axis==tempx1 and i.y_axis==tempy1 and button.butno!=i.butno):
                   f=1
                   break
            
            if f==1:
                break        
                
            tempx1-=65
            tempy1-=65
            
            
            
        tempx1=button.x_axis
        tempy1=button.y_axis
        total=button.x_axis+button.y_axis
        diff=button.x_axis-button.y_axis   
       
       
        f=0
        while(tempx1<=630+280 and tempy1<=495):
            
            for i in buttonslist:
                if((tempx1-tempy1)==diff and i.x_axis==tempx1 and i.y_axis==tempy1 and button.butno==i.butno):
                   self.leftdiagdown=(tempx1,tempy1)
                if((tempx1-tempy1)==diff and i.x_axis==tempx1 and i.y_axis==tempy1 and button.butno!=i.butno):
                   f=1
                   break
                 
                 
            if f==1:
                break
                
            
            tempx1+=65
            tempy1+=65
            
            
        
        # For right Diagonal check
        
        tempx1=button.x_axis
        tempy1=button.y_axis
        total=button.x_axis+button.y_axis
        diff=button.x_axis-button.y_axis
        f=0
        while(tempx1<=630+280 and tempy1>=235):
            
            for i in buttonslist:
                if((tempx1+tempy1)==total and i.x_axis==tempx1 and i.y_axis==tempy1 and button.butno==i.butno):
                    self.rightdiagup=(tempx1,tempy1)
                if((tempx1+tempy1)==total and i.x_axis==tempx1 and i.y_axis==tempy1 and button.butno!=i.butno):
                    f=1
                    break
                  
            if f==1:
                break
                    
                
            tempx1+=65
            tempy1-=65
            
            
            
        tempx1=button.x_axis
        tempy1=button.y_axis
        total=button.x_axis+button.y_axis
        diff=button.x_axis-button.y_axis
        
        f=0
        while(tempx1>=370+280 and tempy1<=495):
            
            
            for i in buttonslist:
                if((tempx1+tempy1)==total and i.x_axis==tempx1 and i.y_axis==tempy1 and button.butno==i.butno):
                    self.rightdiagdown=(tempx1,tempy1)
                if((tempx1+tempy1)==total and i.x_axis==tempx1 and i.y_axis==tempy1 and button.butno!=i.butno):
                    f=1
                    break
                  
            if f==1:
                break
                
            tempx1-=65
            tempy1+=65
            
            
        
        
        
    def displayline(self,gameDisplay):
        
        
        i=25
        
        start_pos=(self.buttonx,self.buttony)
        white=(255,255,255)
        
        if self.flag==0:
            self.horizontalleft=list(self.horizontalleft)
            self.horizontalleft[0]+=i
            self.horizontalleft[1]+=i
            self.horizontalleft=tuple(self.horizontalleft)
        
            self.horizontalright=list(self.horizontalright)
            self.horizontalright[0]+=i
            self.horizontalright[1]+=i
            self.horizontalright=tuple(self.horizontalright)
        
            self.verticalup=list(self.verticalup)
            self.verticalup[0]+=i
            self.verticalup[1]+=i
            self.verticalup=tuple(self.verticalup)
        
            self.verticaldown=list(self.verticaldown)
            self.verticaldown[0]+=i
            self.verticaldown[1]+=i
            self.verticaldown=tuple(self.verticaldown)
        
            self.leftdiagup=list(self.leftdiagup)
            self.leftdiagup[0]+=i
            self.leftdiagup[1]+=i
            self.leftdiagup=tuple(self.leftdiagup)
        
            self.leftdiagdown=list(self.leftdiagdown)
            self.leftdiagdown[0]+=i
            self.leftdiagdown[1]+=i
            self.leftdiagdown=tuple(self.leftdiagdown)
        
            self.rightdiagup=list(self.rightdiagup)
            self.rightdiagup[0]+=i
            self.rightdiagup[1]+=i
            self.rightdiagup=tuple(self.rightdiagup)
        
            self.rightdiagdown=list(self.rightdiagdown)
            self.rightdiagdown[0]+=i
            self.rightdiagdown[1]+=i
            self.rightdiagdown=tuple(self.rightdiagdown)
        
            self.flag=1
        
        
        pygame.draw.line(gameDisplay, white, start_pos,(self.horizontalleft), 3)  #horizontalleft
        
        pygame.draw.line(gameDisplay, white, start_pos,(self.horizontalright), 3)  #horizontalright
        
        pygame.draw.line(gameDisplay, white, start_pos,(self.verticalup), 3)  #verticalup
        
        pygame.draw.line(gameDisplay, white, start_pos,(self.verticaldown), 3)  #verticaldown
        
        pygame.draw.line(gameDisplay, white, start_pos,(self.leftdiagup), 3)  #leftdiagup
        
        pygame.draw.line(gameDisplay, white, start_pos,(self.leftdiagdown), 3)  #leftdiagdown
        
        pygame.draw.line(gameDisplay, white, start_pos,(self.rightdiagup), 3)  #rightdiagup
        
        pygame.draw.line(gameDisplay, white, start_pos,(self.rightdiagdown), 3)  #rightdiagdown
        
        
        
