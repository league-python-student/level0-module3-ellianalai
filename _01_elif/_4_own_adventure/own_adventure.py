from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
if __name__ == '__main__':
    window = Tk()
    window.withdraw()


    adventure = simpledialog.askstring(title ="Own Adventure", prompt ='It is nearing to the end of school day and you are getting restless. Do you just sit there or secretly text on your phone')
    if adventure == 'sit there':
        phone = simpledialog.askstring(title = 'Own Adventure', prompt = 'The school bell rings and you grab your phone. You check it and see that an app you have never seen before got downloaded on your phone. Do you open it or delete it?')
        if phone == 'open it':
            messagebox.showinfo(title = "Own Adventure", message = 'When you click it, in a whirl of light, you get transported to this beautiful place and you live there happily forever. The End')
        elif phone == 'delete it':
            messagebox.showinfo(title = "Own Adventure", message = "You live the rest of your life wondering what would have happened if you opened the app and you die wondering too. The End. ")
    elif adventure == 'secretly text on your phone':
        messagebox.showinfo(title = 'Own adventure', message= 'Your teacher catches you and your phone gets confiscated. The End')
