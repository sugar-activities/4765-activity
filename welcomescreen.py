import gtk
import pygame
import sys
import os
from about import *
from rules import *




class welcome:
    
    
    
    def make(self,gameDisplay,sound):
         
        i=0
        white=(255,255,255)
        black=(0,0,0)
        disp_width=800
        disp_height=600
        crashed=False
        clock=pygame.time.Clock()
        
        
        background=pygame.image.load("buts/welcomescreen/welcome.jpg").convert()                #background image load
        play=pygame.transform.scale(pygame.image.load("buts/welcomescreen/play.png"),(160,160))
        conti=pygame.image.load("buts/welcomescreen/continue.png")
        newgame=pygame.image.load("buts/welcomescreen/newgame.png")
        back=pygame.image.load("buts/welcomescreen/back.png")
        abouts=pygame.transform.scale(pygame.image.load("buts/welcomescreen/about.png"),(80,80))
        title=pygame.transform.scale(pygame.image.load("buts/welcomescreen/title.png"),(400,160))
        helps=pygame.transform.scale(pygame.image.load("buts/welcomescreen/help.png"),(80,80))
        background.set_alpha(255)

        background=pygame.transform.scale(background,(disp_width+100,disp_height+180))
        
        
        contix=0
        contiy=0
        newgamex=0
        newgamey=0
        backx=0
        backy=0
        ru=0
        
        
        playx=0
        playy=0
        aboutx=0
        abouty=0
        helpx=0
        helpy=0
        
        playclick=0
        
        backclick=0
        t=0
        flag=0


        white=(255,255,255)
        
        
        check=0
        #sound=[]
        
        s1=pygame.mixer.Sound("sound/button.ogg")
        bk=pygame.mixer.Sound("sound/bk_menu.ogg")
        if sound:
            bk.play(-1)
        flag1=flag2=0

        
        while not crashed:                        ############################### MAIN GAME LOOP BEGINS #############################################

            # Gtk events
            while gtk.events_pending():
                gtk.main_iteration()

            event=pygame.event.poll()
        
            if event.type == pygame.QUIT:
                crashed = True
            
            mos_x,mos_y=pygame.mouse.get_pos()
            
            gameDisplay.fill(black)
            gameDisplay.blit(background,(0-50+280,0-60))
            
            if play.get_rect(center=(185+playx+280,360+playy)).collidepoint(mos_x,mos_y):                                #PLAY
                gameDisplay.blit(pygame.transform.scale(play,(180,180)),(100+playx+280,275+playy))
                if (pygame.mouse.get_pressed())[0]==1 and check==0:
                    if sound:
                        s1.play()
                    playclick=1
                    t1=t2=0
                    flag2=0
                    check=1
                if event.type==pygame.MOUSEBUTTONUP:
                    check=0
                
                
            else:
                if 100+playx+280>0:
                    gameDisplay.blit(play,(100+playx+280,275+playy))
        
        
            if abouts.get_rect(center=(95+280,545)).collidepoint(mos_x,mos_y):                                #ABOUT
                gameDisplay.blit(pygame.transform.scale(abouts,(90,90)),(50+280,500))
                if (pygame.mouse.get_pressed())[0]==1 and check==0:
                    if sound:
                        s1.play()
                    flag=1
                    check=1
                    gameDisplay.fill(black)
                    a=about()
                    a.make(gameDisplay,sound)
                    

                if event.type==pygame.MOUSEBUTTONUP:
                    check=0
        
            else:
                
                gameDisplay.blit(abouts,(50+280,500))
             
            
            
            
        
            if helps.get_rect(center=(275+280,545)).collidepoint(mos_x,mos_y):                                #HELP
                gameDisplay.blit(pygame.transform.scale(helps,(90,90)),(230+280,500))
                if (pygame.mouse.get_pressed())[0]==1 and check==0:
                    if sound:
                        s1.play()
                    gameDisplay.fill(black)
                    ru=rule()
                    ru.make(gameDisplay,sound)
                    check=1
                    
                if event.type==pygame.MOUSEBUTTONUP:
                    check=0
                
                
            else:
                gameDisplay.blit(helps,(230+280,500))
                
            
            
            if os.path.getsize("score.pkl") > 0:
                if conti.get_rect(center=(50+contix+60+280,-170+contiy+20)).collidepoint(mos_x,mos_y):                                #CONTINUE
                    gameDisplay.blit(pygame.transform.scale(conti,(260,75)),(50+contix+280,-170+contiy))
                    if (pygame.mouse.get_pressed())[0]==1 and check==0:
                        if sound:
                            pygame.mixer.stop()
                        gameDisplay.fill(black)
                        return 0
                        check=1
                        
                    if event.type==pygame.MOUSEBUTTONUP:
                        check=0
            
                else:
                    if 50+contix+280>0:
                        gameDisplay.blit(conti,(50+contix+280,-170+contiy))
                    
            
                    
            if newgame.get_rect(center=(25+newgamex+90+280,-50+newgamey+10)).collidepoint(mos_x,mos_y):                                #NEWGAME
                gameDisplay.blit(pygame.transform.scale(newgame,(260,75)),(25+newgamex+280,-50+newgamey))
                if (pygame.mouse.get_pressed())[0]==1 and check==0:
                    if sound:
                        pygame.mixer.stop()
                        s1.play()
                    check=1
                    
                    gameDisplay.fill(black)
                    return 1
                    
                    
                    
                if event.type==pygame.MOUSEBUTTONUP:
                    
                    check=0
                    
                
            else:
                if -50+newgamey>0:
                    gameDisplay.blit(newgame,(25+newgamex+280,-50+newgamey))
                    
                    
            if back.get_rect(center=(280+backx+90+280,-70+backy+20+10)).collidepoint(mos_x,mos_y):                                #BACK
                gameDisplay.blit(pygame.transform.scale(back,(150,75)),(290+backx+280,-50+backy))
                if (pygame.mouse.get_pressed())[0]==1 and check==0:
                    if sound:    
                        s1.play()
                    backclick=1
                    t1=t2=0
                    flag1=0
                    check=1
                if event.type==pygame.MOUSEBUTTONUP:
                    check=0
                
                
            else:
                if -50+backy>0:
                    gameDisplay.blit(back,(290+backx+280,-50+backy))
            
                
            '''    
            if (-150+newgamey>0):    
                gameDisplay.blit(newgame,(50+newgamex,-150+newgamey))
                
            if -50+contiy>0:
                gameDisplay.blit(conti,(25+contix,-50+contiy))
            if -50+backy>0:
                gameDisplay.blit(back,(250+backx,-50+backy))
            
            '''
            gameDisplay.blit(title,(20+280,10))          #Title Window
            
            
            # iNCREMENT DECREMENT
            
            
            
            
            if playclick==1:
                
                
                
                if 100+playx+280>0 and flag1==0:
                    playx-=(0.2*(t1**1))
                    t1+=1
                
                else:
                    playy=-450
                    playx=0
                    flag1=1
                
                if -50+newgamey>370:
                    playclick=0
                
                else:
                    newgamey+=(0.2*(t2**1))
                    contiy+=(0.2*(t2**1))
                    backy+=(0.2*(t2**1))
                    t2+=1
                    

                
            '''   
            
            pygame.draw.circle(gameDisplay,(255,255,255), (int(50+contix+60),int(-170+contiy+20)),5,2)   #continye
            
            pygame.draw.circle(gameDisplay,(255,255,255), (int(25+newgamex+90),int(-50+newgamey+10)),5,2)    #new game
            
            pygame.draw.circle(gameDisplay,(255,255,255), (int(185+playx),int(360+playy)),5,2)
             
            pygame.draw.circle(gameDisplay,(255,255,255), (int(280+backx+90),int(-70+backy+20+20)),5,2)
            '''   
                
                
            if backclick==1:    
                    
                if 25+newgamex+280>0 and flag2==0:
                    newgamex-=(0.2*(t2**1))
                    contix-=(0.2*(t2**1))
                    backx-=(0.2*(t2**1))
                    t2+=1
                    
                else:
                    newgamey=0
                    newgamex=0
                    
                    contix=0
                    contiy=0
                    
                    backx=0
                    backy=0
                    flag2=1
                    
                
                if playy>=0:
                    backclick=0
            
                else:
                    playy+=(0.2*(t1**1))
                    t1+=1
                     
            pygame.display.update()
            clock.tick(50)
     
            if crashed==True:                                   # Game crash or Close check
                pygame.quit()
                sys.exit()   
            


        event1=pygame.event.poll()                                 
        if event1.type == pygame.QUIT:
            crashed=True
   
        if crashed==True:
            pygame.quit()
            sys.exit()


