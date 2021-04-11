from tkinter import simpledialog, messagebox, Tk
import webbrowser


# Use this function to play a video from the internet
def play_video(url):
    webbrowser.open(url)

# =================== DO NOT MODIFY THE CODE ABOVE ===========================


if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    cats = simpledialog.askinteger(title= '', prompt = 'How many cats do you have?')
    if cats > 3:
        messagebox.showinfo(title = '', message = 'You are a crazy cat lady')
    elif cats < 3 and cats >0:

        play_video('https://www.google.com/url?sa=i&url=https%3A%2F%2Fgiphy.com%2Fexplore%2Ftime-to-move&psig=AOvVaw1VUXbehLn9wW56eAszMskE&ust=1618255685148000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCOCf96329u8CFQAAAAAdAAAAABAD')

    elif cats == 0:
        play_video('https://www.google.com/search?q=a+frog+sitting+on+a+bench+like+a+human&rlz=1CARJNJ_enUS842&sxsrf=ALeKk03xNKY-pgQuOWTOVvshKtS5ghIkbw:1618169383531&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiLpqra9vbvAhWbJDQIHZNpBuoQ_AUoAXoECAEQAw&biw=1366&bih=617&safe=active&ssui=on#imgrc=d_HqJ4Jz_VDj9M')



    # TODO 1) Make a new window variable, window = Tk()
    #      2) Hide the window using the window's .withdraw() method
    #      3) Ask the user how many cats they have
    #      4) If they have 3 or more cats, tell them they are a crazy cat lady
    #      5) If they have less than 3 cats AND more than 0 cats, call the
    #         play_video function below to show them a cat video
    #      6) If they have 0 cats, show them a video of A Frog Sitting on a
    #         Bench Like a Human

    pass
