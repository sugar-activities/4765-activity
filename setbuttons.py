import pygame
import sys
from random import *
from buttons import *



# WORKS ON U-T(Un-Tangled) ALGORITHM




class setbuttons:
  
  
    buttonslist=[]  
    
    def __init__(self):
        self.buttonslist=[]
        f=0
        while f==0:
            noofbuttons=25
            self.buttonslist=[]
        


            index=[(370+280,235),(370+280,300),(370+280,365),(370+280,430),(370+280,495),
                   (435+280,235),(435+280,300),(435+280,365),(435+280,430),(435+280,495),
                   (500+280,235),(500+280,300),(500+280,365),(500+280,430),(500+280,495),
                   (565+280,235),(565+280,300),(565+280,365),(565+280,430),(565+280,495),
                   (630+280,235),(630+280,300),(630+280,365),(630+280,430),(630+280,495)]
           
       
       
           # buttons' objects creation

    
            blockcheck=[]
            newblockcheck=[]

            amountofbuttons=[3,6,4,4,4,4]    #buttons sequence

            

            listofbuttons=[1,2,3,4,5,6,7]
        
            case=randint(1,7)     #2  random exclusion buttons
            listofbuttons.remove(case)

            directionlist=[3,4]

            leftdiagonal=[(370+280,235),(500+280,365),(630+280,495)]
            rightdiagonal=[(630+280,235),(500+280,365),(370+280,495)]
            
            vertical=horizontal=leftd=rightd=0

            for i in amountofbuttons:
                case=randint(0,len(listofbuttons)-1)  # random color index
        
                if i==3:
      
                    for k in range(i):
                        
                        if k!=0:
                            
                            if vertical==0 and horizontal==0 and leftd==0 and rightd==0:
                              
                                count=0
                                while(True):
                                    count+=1
                                    random=randint(0,len(index)-1)        
                                    randx=index[random][0]
                                    randy=index[random][1]
                                    newsum=randx+randy
                                    newdiff=randx-randy
                                    if count>len(index):          ########## Infinite Case Check ###############
                                        f=0
                                        break
                    
                                    if newsum==lastsum or newdiff==lastdiff or randx==lastx or randy==lasty:
                                        f=1
                                        if newsum==lastsum:
                                            rightd=1
                                        elif newdiff==lastdiff:
                                            leftd=1
                                        elif lastx==randx:
                                            vertical=1
                                        else:
                                            horizontal=1
                                        break
                            
                            
                                if f==0:
                                    break
                          
                            
                            else:
                                
                                count=0
                                while(True):
                                    count+=1
                                    random=randint(0,len(index)-1)        
                                    randx=index[random][0]
                                    randy=index[random][1]
                                    newsum=randx+randy
                                    newdiff=randx-randy
                                    if count>len(index):          ########## Infinite Case Check ###############
                                        f=0
                                        break
                                    if vertical==1:
                                        if lastx==randx:
                                            f=1
                                            break
                                    elif horizontal==1:
                                        if lasty==randy:
                                            f=1
                                            break
                                    elif rightd==1:
                                        if lastsum==newsum:
                                            f=1
                                            break
                                    else:
                                        if lastdiff==newdiff:
                                            f=1
                                            break
                              
                              
                             
                                
                        
                            
                            
                            
                        else:
                             
                             
                            random=randint(0,len(index)-1)
                            randx=index[random][0]
                            randy=index[random][1] 
                            lastx=randx
                            lasty=randy
                            lastsum=randx+randy
                            lastdiff=randx-randy
                            
                        
                            
                            
                        if(listofbuttons[case]==1):
                            self.buttonslist.append(button1(randx,randy))
                
                        if(listofbuttons[case]==2):
                            self.buttonslist.append(button2(randx,randy))
                 
                        if(listofbuttons[case]==3): 
                            self.buttonslist.append(button3(randx,randy))
                  
                        if(listofbuttons[case]==4):
                            self.buttonslist.append(button4(randx,randy))
                  
                        if(listofbuttons[case]==5):
                            self.buttonslist.append(button5(randx,randy))
                  
                        if(listofbuttons[case]==6):
                            self.buttonslist.append(button6(randx,randy))
                  
                        if(listofbuttons[case]==7):
                            self.buttonslist.append(button7(randx,randy))  
                                  
                        index.remove((randx,randy))
                    listofbuttons.remove(listofbuttons[case])
                          
                          
                              
                            
                          
                          
                          
                    if vertical==1:
                        tempx=self.buttonslist[0].x_axis
                        tempy=235
                        while(tempy<=495):
                            if not( tempy==self.buttonslist[0].y_axis or tempy==self.buttonslist[1].y_axis or tempy==self.buttonslist[2].y_axis):
                                newblockcheck.append((tempx,tempy))
                        
                            tempy+=65
                    #print len(blockcheck),' 1'
                
                    elif horizontal==1:
                        tempy=self.buttonslist[0].y_axis
                        tempx=370+280
                        while(tempx<=630+280):
                            if not( tempx==self.buttonslist[0].x_axis or tempx==self.buttonslist[1].x_axis or tempx==self.buttonslist[2].x_axis):
                                newblockcheck.append((tempx,tempy))
                        
                            tempx+=65
                    #print len(blockcheck),' 2'        
                        
                    elif leftd==1 and self.buttonslist[0].x_axis-self.buttonslist[0].y_axis==135:
                        tempx=370+280
                        tempy=235
                        while(tempx<=630+280 and tempy<=495):
                            if not((tempy==self.buttonslist[0].y_axis or tempy==self.buttonslist[1].y_axis or tempy==self.buttonslist[2].y_axis) and (tempx==self.buttonslist[0].x_axis or tempx==self.buttonslist[1].x_axis or tempx==self.buttonslist[2].x_axis)):
                                newblockcheck.append((tempx,tempy))
                        
                            tempx+=65
                            tempy+=65
                
                        #print len(blockcheck),' 3'
                
                    elif rightd==1 and self.buttonslist[0].x_axis+self.buttonslist[0].y_axis==865:
                        tempx=630+280
                        tempy=235
                        while(tempx>=370+280 and tempy<=495):
                            if not((tempy==self.buttonslist[0].y_axis or tempy==self.buttonslist[1].y_axis or tempy==self.buttonslist[2].y_axis) and (tempx==self.buttonslist[0].x_axis or tempx==self.buttonslist[1].x_axis or tempx==self.buttonslist[2].x_axis)):
                                newblockcheck.append((tempx,tempy))
                            
                            tempx-=65
                            tempy+=65
                
                          
                          
                          
                    continue
                
                
                
                if f==0:
                    break
                
                
                
                
                  
        
                    
                
                
                
                '''
                print 'this'
                print len(newblockcheck)
                '''
                
                
                f=0
                addx=addy=0
                lastbutno=0
                for j in range(i):
                    
                    
                    
                    if j==0:
                    
                        random=randint(0,len(index)-1)        
                        randx=index[random][0]
                        randy=index[random][1]
                        startx=randx
                        starty=randy
                        newsum=randx+randy
                        newdiff=randx-randy
                        
                        
                        if ((randx,randy) in newblockcheck):
                            newblockcheck.remove((randx,randy))
                            
                            
                            addx,addy=newblockcheck[0]
                            newblockcheck=[]
                            
                    
                    else:
                      
                        count=0
                        while(True):
                            count+=1
                            random=randint(0,len(index)-1)        
                            randx=index[random][0]
                            randy=index[random][1]
                            newsum=randx+randy
                            newdiff=randx-randy
                            
                            
                            
                            
                            if count>len(index):          ########## Infinite Case Check ###############
                                f=0
                                break
                    
                            if randx+130==lastx or randx-130==lastx  or randy-130==lasty  or randy+130==lasty :
                                continue
                                
                         
                            if ((newsum==lastsum or newdiff==lastdiff or randx==lastx or randy==lasty) and not(randx==addx and randy==addy)):
                                
                                
                                  
                                
                                
                                
                                if ((randx,randy) in newblockcheck):
                                  
                                    newblockcheck.remove((randx,randy))
                                    
                                    addx,addy=newblockcheck[0]
                                    newblockcheck=[]
                                    
                                    
                                f=1
                                break
                        
                        if f==0:
                            break
            
                        
                        
                    lastdiff=newdiff
                    lastsum=newsum
                    lastx=randx
                    lasty=randy
                    
                    
                    
    
                    if(listofbuttons[case]==1):
                        self.buttonslist.append(button1(randx,randy))
                        lastbutno=1
                        
                    if(listofbuttons[case]==2):
                        self.buttonslist.append(button2(randx,randy))
                        lastbutno=2
                              
                    if(listofbuttons[case]==3):
                        self.buttonslist.append(button3(randx,randy))
                        lastbutno=3
                              
                    if(listofbuttons[case]==4):
                        self.buttonslist.append(button4(randx,randy))
                        lastbutno=4
                              
                    if(listofbuttons[case]==5):
                        self.buttonslist.append(button5(randx,randy))
                        lastbutno=5
                              
                    if(listofbuttons[case]==6):
                        self.buttonslist.append(button6(randx,randy))
                        lastbutno=6
                              
                    if(listofbuttons[case]==7):
                        self.buttonslist.append(button7(randx,randy))    
                        lastbutno=7
                           
                    index.remove(index[random])
              
              
              
                          
                if(len(newblockcheck)==0):
                    addx=addy=0
          
                if f==0:
                    break
          
          
                listofbuttons.remove(listofbuttons[case])
                
                  
                
            if f==0:
                continue
                
                
                
