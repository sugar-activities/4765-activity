import pygame
import gtk
import sys
import os



class about:
    
    

    def make(self,gameDisplay,sound):
        
        
        check=0
        myimage=pygame.image.load("images/me.jpg").convert()
        background=pygame.image.load("images/background.jpg").convert()
        background=pygame.transform.scale(background,(900,715))
        myimage=pygame.transform.scale(myimage,(80,80))
        
        
        crashed=False
        clock=pygame.time.Clock()
        
        
        font_path = "fonts/comicsans.ttf"
        font_size = 50
        font1= pygame.font.Font(font_path, font_size)
        back=pygame.image.load("buts/welcomescreen/back.png")
        back=pygame.transform.scale(back,(100,50))
        font2=pygame.font.Font(font_path,20)
        font3=pygame.font.Font(font_path,25)
        Dev=font1.render("Developer",1,(161,55,2))
        name=font3.render("Utkarsh Tiwari",1,(161,55,2))
        college=font2.render("Institute: JIIT, India",1,(161,55,2))
        contact=font2.render("Contact: https://facebook.com/iamutkarshtiwari",1,(161,55,2))
        if sound:
            s1=pygame.mixer.Sound("sound/button.ogg")
            s2=pygame.mixer.Sound("sound/success.ogg")
            s2.play(0)
        
        while not crashed:
            # Gtk events
            while gtk.events_pending():
                gtk.main_iteration()
            event=pygame.event.poll()
        
            if event.type == pygame.QUIT:
                crashed = True
            
            mos_x,mos_y=pygame.mouse.get_pos()
            
            
            gameDisplay.blit(background,(0+280-50,0))
            
            
            if back.get_rect(center=(455+280,535+80+15)).collidepoint(mos_x,mos_y):                                #BACK
                gameDisplay.blit(pygame.transform.scale(back,(110,55)),(440+280,520+80+15))
                
                if (pygame.mouse.get_pressed())[0]==1 and check==0:
                    if sound:
                        s1.play()
                    check=1
                    
                    return
                  
                if event.type==pygame.MOUSEBUTTONUP:
                    check=0
            
            else:
                gameDisplay.blit(back,(440+280,520+80+15))
                
                

            
            gameDisplay.blit(myimage,(340+280,340+80))
            
            gameDisplay.blit(Dev,(420+280,260+80))
            
            gameDisplay.blit(name,(460+280,380+80))
            
            gameDisplay.blit(college,(320+280,440+80))
            
            gameDisplay.blit(contact,(320+280,480+80))
            
            #gameDisplay.blit(back,(440,520))
            
                
                
            
            
            
            
            
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

   
