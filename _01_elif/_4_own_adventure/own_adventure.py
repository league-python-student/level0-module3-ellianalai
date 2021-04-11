from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    adventure = simpledialog.askstring(title ="Own Adventure", prompt ='It is nearing to the end of school day and you are getting restless. Do you just sit there or secretly text on your phone')
    if adventure == 'wait there':
        phone = simpledialog.askstring(title = 'Own Adventure', prompt = 'The school bell rings and you grab your phone. You check it and see that an app you have never seen before got downloaded on your phone. Do you open it or delete it?')
    if adventure == 'secretly text on your phone':
        messagebox.showinfo(title = 'Own adventure', prompt= 'Your teacher catches you and your phone gets confiscated. The End')
