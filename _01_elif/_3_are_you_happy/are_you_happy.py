from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    happy = simpledialog.askstring(title = '', prompt= 'Are you happy?')
    if happy == 'Yes':
        messagebox.showinfo(title='', message='Keep doing whatever you are doing')
    elif happy =='No':
        notHappy = simpledialog.askstring(title = '', prompt = 'Do you want to be happy')
    if notHappy == 'Yes':
        messagebox.showinfo(title = '', message= 'Change something')
    elif notHappy == 'No':
        messagebox.showinfo(title='', message='Keep doing whatever you are doing')
    else:
        messagebox.showerror(title ='', message= 'Please answer Yes or No')

    pass
