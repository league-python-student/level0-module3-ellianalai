from tkinter import simpledialog, Tk
#from playsound import playsound

can_play_sounds = True
def play_mister_zee():
    if can_play_sounds:
        print('Yay shiny Objects!!')
        pass
         #playsound(play_mister_zee)
    else:
        print("Mister Zee requires shiny objects")

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    shiny = simpledialog.askstring(title = '', prompt = "how many shiny objects do you want?")
    for i in range (int (shiny)):
        play_mister_zee()




def many_shiny_objects():
    # TODO 1) Call the method above to play Mister Zee

    # TODO 2) Ask the user how many shiny objects they want

    # TODO 3) Play the sound that many times

    pass



