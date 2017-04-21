import pygame
import sys


class track:
     
     coordinatelist=[]
     
     
     def __init__(self):
         self.coordinatelist=[]
         self.lastdiff=0
         self.lasttotal=0
         self.lastx=0
         self.lasty=0
         self.vertical=0
         self.horizontal=0
         self.rightd=0
         self.leftd=0
     
     def insert(self,button):
         if len(self.coordinatelist)>0:
             if button not in self.coordinatelist:
                 self.coordinatelist.append(button)
                
         else:
             self.coordinatelist.append(button)
             
             
             
             
             
             
     
     def display(self,gameDisplay):
         for j in self.coordinatelist:
            
             pygame.draw.circle(gameDisplay,[255,255,255],[j.x_axis+25,j.y_axis+25],32,5)
             
             
             
             
class scissorrun:
     
     sentcoordinatelist=[]
     down=0
     increment=[]
     x=0
     j=0
     k=0
     length=0
     sound=[]
     
     def __init__(self,coordinatelist):
         self.sentcoordinatelist=coordinatelist
         self.length=len(coordinatelist)
         
         for i in range(len(coordinatelist)):
             self.increment.append(0)
         self.x=0
         self.k=0
         self.j=0
         self.y=0
         self.cp=(0,0)
         self.sound=[]
         
         
     def display(self,gameDisplay):
         
         
         scis=pygame.mixer.Sound("sound/scissors.ogg")
         ground=pygame.mixer.Sound("sound/ground1.ogg")
         
         x1=self.sentcoordinatelist[0].x_axis
         y1=self.sentcoordinatelist[0].y_axis
         
         x2=self.sentcoordinatelist[1].x_axis
         y2=self.sentcoordinatelist[1].y_axis
         
         right1=pygame.transform.scale(pygame.image.load("scissor/s1.png"),(180,100))
         right2=pygame.transform.scale(pygame.image.load("scissor/s2.png"),(180,100))
         right3=pygame.transform.scale(pygame.image.load("scissor/s3.png"),(180,100))
         
         left1=pygame.transform.flip(right1,True,False)         
         left2=pygame.transform.flip(right2,True,False)         
         left3=pygame.transform.flip(right3,True,False)
         
         
         up1=pygame.transform.rotate(right1,-90)         
         up2=pygame.transform.rotate(right2,-90)         
         up3=pygame.transform.rotate(right3,-90)
         
         
         down1=pygame.transform.rotate(right1,90)         
         down2=pygame.transform.rotate(right2,90)         
         down3=pygame.transform.rotate(right3,90)
         
         
         downleft1=pygame.transform.rotate(left1,-45)         
         downleft2=pygame.transform.rotate(left2,-45)         
         downleft3=pygame.transform.rotate(left3,-45)
         
         
         downright1=pygame.transform.rotate(right1,45)         
         downright2=pygame.transform.rotate(right2,45)         
         downright3=pygame.transform.rotate(right3,45)
         
         
         upleft1=pygame.transform.rotate(left1,45)         
         upleft2=pygame.transform.rotate(left2,45)         
         upleft3=pygame.transform.rotate(left3,45)


         upright1=pygame.transform.rotate(right1,-45)         
         upright2=pygame.transform.rotate(right2,-45)         
         upright3=pygame.transform.rotate(right3,-45)
         
         
         
         frameright=[right1,right2,right3]
         frameleft=[left1,left2,left3]
         
         frameup=[up1,up2,up3]
         framedown=[down1,down2,down3]
         
         framedownleft=[downleft1,downleft2,downleft3]
         framedownright=[downright1,downright2,downright3]
         
         frameupleft=[upleft1,upleft2,upleft3]
         frameupright=[upright1,upright2,upright3]
         
         
         # Horizontal left case
         if y1==y2 and x1< x2:
             
             self.cp=(self.x+10+175+50+280,y1+25)
             
             
             if(self.j>10):
                 self.k+=1
                 self.j=0
             
             if(self.k>2):
                 self.k=0
             
             gameDisplay.blit(frameleft[self.k],(100-50+self.x+50+280,y1-25))
             
             self.j+=1
             #if( -50+x>sentcoordinatelist[0].x_axis):
             self.x+=8   #scissor speed
             
             
             
         # Horizontal right case
         if y1==y2 and x1> x2:
             
             self.cp=(self.x+890-50+280,y1+25)
             
             
             if(self.j>10):
                 self.k+=1
                 self.j=0
             
             if(self.k>2):
                 self.k=0
             
             gameDisplay.blit(frameright[self.k],(850+self.x-50+280,y1-25))
             
             self.j+=1
             #if( -50+x>sentcoordinatelist[0].x_axis):
             self.x-=8   #scissor speed
         
         #vertical down case
         if x1==x2 and y1<y2 :
             
             if(self.j>10):
                 self.k+=1
                 self.j=0
             
             if(self.k>2):
                 self.k=0
             
             gameDisplay.blit(framedown[self.k],(x1-25,100-50+self.y))
             
             self.j+=1
             #if( -50+x>sentcoordinatelist[0].x_axis):
             self.y+=8   #scissor speed 
             
             self.cp=(x1+25,100+self.y+25+60)
             
             
             
         #vertical up case
         if x1==x2 and y1>y2 :
             
             if(self.j>10):
                 self.k+=1
                 self.j=0
             
             if(self.k>2):
                 self.k=0
             
             gameDisplay.blit(frameup[self.k],(x1-25,650+self.y))
             
             self.j+=1
             #if( -50+x>sentcoordinatelist[0].x_axis):
             self.y-=8   #scissor speed 
             
             self.cp=(x1+25,self.y+695)
         
         
         #downleft case
           
         if x1-y1==x2-y2 and (x1<x2) :
             
             if(self.j>10):
                 self.k+=1
                 self.j=0
             
             if(self.k>2):
                 self.k=0
             
             gameDisplay.blit(framedownleft[self.k],(-20+self.x+200+10+280 ,200-20-(x1-y1)+self.x+10+280))
             
             self.j+=1
             #if( -50+x>sentcoordinatelist[0].x_axis):
             self.y+=8   #scissor speed
             self.x+=8
             
             self.cp=(self.x-20+65+260+280,-20-(x1-y1)+self.y+65+260+280)
             
             
         
         #downright case
         
         if x1+y1==x2+y2 and (x1>x2) :
             
             if(self.j>10):
                 self.k+=1
                 self.j=0
             
             if(self.k>2):
                 self.k=0
             
             gameDisplay.blit(framedownright[self.k],(820+self.x-90+280-100 ,(x1+y1)-self.x-820-140+90-280+100))
             
             self.j+=1
             #if( -50+x>sentcoordinatelist[0].x_axis):
             self.y+=8   #scissor speed
             self.x-=8
             
             self.cp=(820+self.x+65-90+280,(x1+y1)-self.x-820-12+90-280)
             
         
         #upleft case
         
         if x1+y1==x2+y2 and (x1<x2) :
             
             if(self.j>10):
                 self.k+=1
                 self.j=0
             
             if(self.k>2):
                 self.k=0
             
             gameDisplay.blit(frameupleft[self.k],(-20+self.x+150+280 ,(x1+y1)-self.x+20-140-5-150-280))
             
             self.j+=1
             #if( -50+x>sentcoordinatelist[0].x_axis):
             self.y-=8   #scissor speed
             self.x+=8
             
             self.cp=(-20+self.x+120+150+280,(x1+y1)-self.x+20-60-5-150-280)
         
         #upright case
         
         if x1-y1==x2-y2 and (x1>x2) :
             
             if(self.j>10):
                 self.k+=1
                 self.j=0
             
             if(self.k>2):
                 self.k=0
             
             gameDisplay.blit(frameupright[self.k],(820+self.x-100+280 ,820-(x1-y1)+self.x-100+280))
             
             self.j+=1
             #if( -50+x>sentcoordinatelist[0].x_axis):
             self.y-=8   #scissor speed
             self.x-=8
             
             self.cp=(820+self.x+80-100+280 ,820-(x1-y1)+self.x+80-100+280)
             
         
         
         sound=[] 
         count1=0
         count2=0
         for i in self.sentcoordinatelist:
             
                    
             if i.but.get_rect(center=(i.x_axis+25,i.y_axis+25)).collidepoint(self.cp):
                 i.flag=1
                 
                 
                 if count1<=self.length:
                     scis.play(0)
                     count1+=1
             
             
                 
                 
             i.display(gameDisplay)
             
             
             
             if (i.y_axis+(0.2*(i.i**2)))>615:
                 
                 
                 if count2<=self.length:
                     ground.play(0)
                     count2+=1
             
             #pygame.draw.circle(gameDisplay,(255,255,255), self.cp,5,2)
                 
             '''
             if i.y_axis+i.i==604:
                 #pygame.mixer.music.stop()
                    
             '''    
             #self.increment[j]+=1  
             
         '''         
         for k in self.sound:
             k.play()
         self.down+=1
         '''
     
            
            
