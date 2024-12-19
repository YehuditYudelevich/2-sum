import pygame
import time
pygame.init()
w,h=1000,800
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption("2sum")
colors={
    "screen":(255, 250, 240),
    "black":(0,0,0),
    "orange":(255, 165, 0),
    "light_green":(204, 255, 204),
    "green": (57, 255, 20)           
    
}
def the_array(array,curr_index,target):
    len_array=len(array)
    font=pygame.font.Font(None,40)
    text=font.render("The target is: "+str(target),True,colors["black"])
    screen.blit(text,(20,40))
    for i in range(len_array):
        if i==curr_index:
            pygame.draw.rect(screen,colors["orange"],(20+i*76,100,80,50))
            pygame.draw.rect(screen,colors["black"],(20+i*76,100,80,50),4)
        else:
            pygame.draw.rect(screen,colors["light_green"],(20+i*76,100,80,50))
        pygame.draw.rect(screen,colors["black"],(20+i*76,100,80,50),2)
        font=pygame.font.Font(None,36)
        font2=pygame.font.Font(None,22)
        text2=font2.render(str(i),True,colors["black"])
        screen.blit(text2,(20+i*76+30,100+60))
        text=font.render(str(array[i]),True,colors["black"])
        screen.blit(text,(20+i*75+30,110))

def the_algo(array, target):
    pygame.draw.rect(screen,colors["light_green"],(20,260,260,400),border_radius=10)
    pygame.draw.rect(screen,colors["green"],(20,260,260,400),6,10)
    font=pygame.font.Font(None,35)
    text=font.render("The dictionary:",True,colors["black"])
    screen.blit(text,(40,220))  
    my_array={}
    for i, num in enumerate(array):
        the_array(array,i,target)
        diff = target - num
        if diff in my_array:
            pygame.draw.rect(screen,colors["light_green"],(480,260,400,150),border_radius=10)
            pygame.draw.rect(screen,colors["green"],(480,260,400,150),4,10)


            font = pygame.font.Font(None, 50)
            text = font.render("Found!", True, colors["black"])
            screen.blit(text, (500, 270))
            text = font.render(f"Indices: ({my_array[diff]}, {i})", True, colors["black"])
    
            screen.blit(text, (500, 310))
            text2=font.render(f"target={diff}+{num}",True,colors["black"])
            screen.blit(text2,(500,350))
            pygame.display.update()
            pygame.time.delay(5000)
            pygame.quit()
            return my_array[diff], i
        
        
        my_array[num] = i
        font = pygame.font.Font(None, 30)
        y_position = 300 + i * 30
        text = font.render(f"diff: {diff}:   index: {i}", True, colors["black"])
        screen.blit(text, (50, y_position))
        text2=font.render(f"difference={target}-{num}",True,colors["black"])
        screen.blit(text2,(300,y_position))

        pygame.display.update()
        pygame.time.delay(1200)  


def main():
    arr=[3,4,1,9,7,10,11,20,2,8,0]
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        screen.fill(colors["screen"])
        the_array(arr,-1,9)
        the_algo(arr,9)
        pygame.display.flip()
        pygame.time.delay(100)
    pygame.quit()
main()

