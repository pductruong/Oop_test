
from Game import*


def main():
    
    game = Game()
    while True:
        game.Draw()
        game.handle_event()
        game.Update()
        game.GetCanvas().update()


    

if __name__=='__main__':
    main()