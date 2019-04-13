import tkinter as tk
from dungeon import *
from PIL import ImageTk, Image
from copy import deepcopy
from tkinter import messagebox


class Level(tk.Frame):
    images = {'E': './pictures/enemy.png', 'H': './pictures/enemy.png', '.': './pictures/path.png',
              '#': './pictures/walla.png', 'G': './pictures/princess.png', 'T': './pictures/treasure.png'}

    def setUI(self):
        self.rowconfigure(len(self.layout) + 2+3, weight=3)
        self.columnconfigure(len(self.layout[0]), weight=3)
        for idx_row, row in enumerate(self.layout):
            for idx_col, elem in enumerate(row):
                image = Image.open(Level.images[elem])
                label_image = ImageTk.PhotoImage(image)
                label = tk.Label(self, image=label_image,highlightthickness = 0, bd = 0)
                label.photo = label_image
                label.grid(row=idx_row + 2, column=idx_col)
        self.master.text.delete(1.0,tk.END)
        self.master.text.insert(tk.INSERT,'.\n '.join(self.log))
        
        label = tk.Label(self, fg="orange", bg="black", text="Welcome to Level: {}".format(
            self.chosen_level), font=("Courier", 44), anchor=tk.CENTER)
        label.grid(row=0, columnspan=6)
       
    def __init__(self, master, chosen_level, hero):
        super().__init__(master,bg="black")
        self.start_game(master, chosen_level, hero)

    def start_game(self, master, chosen_level, hero):
        self.hero = hero
        self.log = []
        self.map = Dungeon('./levels/level' + str(chosen_level) + '.txt')
        self.map.spawn(deepcopy(self.hero))
        self.layout = self.map.print_map()
        self.chosen_level = chosen_level
        self.master = master
        self.setUI()

    def next(self):
        print("in next")
        self.start_game(self.master, self.chosen_level + 1, self.hero)

    def moving(self, event):
        if event.keysym in self.map.directions:
            self.log = self.map.move_hero(event.keysym)
        #print log#

            # print(self.log)
            # if 'treasure' in self.log[-1]:
            #     prize = messagebox.showinfo('Treasure', self.log[-1])
            if self.log != [] and self.log[-1] == 'Level Completed':
                self.next()
            if self.log != [] and self.log[-1] == 'Game Over':
                self.over()
            else:
                self.setUI()

    def over(self):
        error = messagebox.showerror("Game Over!", "Sorry, you lost!")


def main():

    root = tk.Tk()
    root.geometry("800x600")
    root.title("Dungeons and Pythons")
    image = Image.open('./pictures/dungeon.jpg')
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(root, image=background_image)
    background_label.photo = background_image
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    current_level = None
    window = tk.Frame(root, bg="black", borderwidth=1)
    window.pack(side=tk.BOTTOM, anchor=tk.W)
    # frame = tk.Frame(borderwidth=1)
    # frame.pack(fill=BOTH, expand=True)

    window.rowconfigure(7, weight=1)
    window.columnconfigure(2, weight=1)
    hero_name_label = tk.Label(
        window, text="Enter hero name:", bg="black", fg="orange")
    hero_name_label.grid(row=2, column=0)
    # hero_name_label.pack()
    hero_nick_label = tk.Label(
        window, text="Enter hero nickname:", bg="black", fg="orange")
    hero_nick_label.grid(row=3, column=0)
    # hero.hero_nick_label.pack()
    hero_health_label = tk.Label(
        window, text="Enter hero health:", bg="black", fg="orange")
    hero_health_label.grid(row=4, column=0)
    # hero_health_label.pack()
    hero_mana_label = tk.Label(
        window, text="Enter hero mana:", bg="black", fg="orange")
    hero_mana_label.grid(row=5, column=0)
    # hero_mana_label.pack()
    hero_mana_regen_rate = tk.Label(
        window, text='Enter hero mana-regen', bg="black", fg="orange")
    hero_mana_regen_rate.grid(row=6, column=0)

    level_label = tk.Label(window, text="Pick a level:",
                           bg="black", fg="orange")
    level_label.grid(row=7, column=0)
    # level_label.pack()

    hero_name_entry = tk.Entry(window, bg="black", fg="orange")
    hero_name_entry.grid(row=2, column=1)
    # hero_health_entry.pack()
    hero_nick_entry = tk.Entry(window, bg="black", fg="orange")
    hero_nick_entry.grid(row=3, column=1)
    # hero_name_entry.pack()
    hero_health_entry = tk.Entry(window, bg="black", fg="orange")
    hero_health_entry.grid(row=4, column=1)
    # hero_nick_entry.pack()
    hero_mana_entry = tk.Entry(window, bg="black", fg="orange")
    hero_mana_entry.grid(row=5, column=1)

    hero_mana_regen_rate = tk.Entry(window, bg="black", fg="orange")
    hero_mana_regen_rate.grid(row=6, column=1)
    # hero_mana_entry.pack()
    level_input = tk.Entry(window, bg="black", fg="orange")
    level_input.grid(row=7, column=1)
    # level_input.pack()

    def create_lvl():
        nonlocal background_label
        background_label.place_forget()
        text = tk.Text(root,bg="black", fg="orange",font=("Courier", 14),height=3)
        text.pack(side=tk.BOTTOM)
        root.text = text
        current_level = Level(root, int(level_input.get()), Hero(hero_name_entry.get(
        ), hero_nick_entry.get(), int(hero_health_entry.get()), int(hero_mana_entry.get()), int(hero_mana_regen_rate.get())))
        window.destroy()
        current_level.pack()
        current_level.focus_set()
        current_level.bind("<KeyPress>", current_level.moving)
        
        text.bind("<KeyPress>",current_level.moving)

    start = tk.Button(window, text="Submit", width=20, bg="black", fg="orange",
                      command=lambda: create_lvl())
    start.grid(row=8, columnspan=2)

    root.mainloop()
if __name__ == '__main__':
    main()
