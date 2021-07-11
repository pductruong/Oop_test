
from Game import*



def main():
    
    game = Game()
    while True:
        game.Update()
        game.Draw()
        game.GetCanvas().update()


    

if __name__=='__main__':
    main()