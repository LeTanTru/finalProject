from tkinter import *
from tkinter import messagebox
import time
import colors
from customs import *


class QueueVisualization:
    def __init__(self, root):
        self.window = root
        self.window.config(bg=colors.bg_window)

        # init size of canvas
        self.canvas_width = 800
        self.canvas_height = 500
        self.block_store = []
        self.front_pointer_coords = []
        self.tail_pointer_coords = []
        self.queue_element = []
        self.block_value_store = []
        # init push and pop buttons
        self.push_btn = None
        self.pop_btn = None

        self.queue_container_label = None
        self.front_pointer_label = None
        self.tail_pointer_label = None
        self.front_pointer_index = None
        self.tail_pointer_index = None

        self.element_take_label = None
        self.element_take_entry = None
        self.go_pushing_btn = None
        self.new_element_value = None
        self.heading_name = None
        self.subheading = None
        self.number_set_x = 40
        self.number_set_y = 447
        self.block_up = 401
        self.block_left = 26
        self.block_right = self.block_left + 46
        self.block_down = self.block_up + 45
        self.right_achieve = 570
        self.front_pointer_x = 420
        self.front_pointer_start_x = 632
        self.front_pointer_start_y = 200

        self.tail_pointer_start_x = 632
        self.tail_pointer_start_y = 200
        self.space_between_two_indexes = 54
        self.decrease_x = 0

        self.move_delay = 0.005
        self.deleted_element_delay = 0.3

        self.delete_element_x = 750

        self.queue_canvas = Canvas(
            self.window,
            width=self.canvas_width,
            height=self.canvas_height,
            bg=colors.bg_canvas,
            relief=GROOVE,
            bd=5,
        )
        self.queue_canvas.pack(fill=BOTH)

        self.create_heading_and_sub_heading()
        self.create_queue_container()
        self.create_somes_buttons()
        self.create_queue_index()
        self.create_front_pointer()
        self.center_window(800, 600)

    # center window
    def center_window(self, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 4
        self.window.geometry(f"{width}x{height}+{x}+{y}")

    def create_heading_and_sub_heading(self):
        self.heading_name = Label(
            self.queue_canvas,
            text="Queue Visualization",
            bg=colors.bg_canvas,
            fg="red",
            font=("Arial", 30, "bold"),
        )
        self.heading_name.place(x=200, y=20)

        self.subheading = Label(
            self.queue_canvas,
            text="Index",
            bg=colors.bg_canvas,
            fg="red",
            font=("Arial", 20, "bold"),
        )
        self.subheading.place(x=70, y=200)

        self.queue_container_label = Label(
            self.queue_canvas,
            text="Queue Container",
            bg=colors.bg_canvas,
            fg="red",
            font=("Arial", 20, "bold"),
        )
        self.queue_container_label.place(x=290, y=400)

    def create_somes_buttons(self):
        self.push_btn = HoverButton(
            self.window,
            text="PUSH",
            font=("Arial", 15, "bold"),
            bg="black",
            fg="gray",
            relief=RAISED,
            bd=2,
            command=self.push_element,
            cursor="hand2",
            width=10,
        )
        self.push_btn.place(x=450, y=535)

        self.pop_btn = HoverButton(
            self.window,
            text="POP",
            font=("Arial", 15, "bold"),
            bg="black",
            fg="gray",
            relief=RAISED,
            bd=2,
            command=self.pop_data,
            cursor="hand2",
            width=10,
        )
        self.pop_btn.place(x=600, y=535)

    def create_front_pointer(self):
        self.front_pointer_coords = [
            self.front_pointer_start_x,
            self.front_pointer_start_y,
            self.front_pointer_start_x - 10,
            self.front_pointer_start_y - 20,
            self.front_pointer_start_x - 5,
            self.front_pointer_start_y - 20,
            self.front_pointer_start_x - 5,
            self.front_pointer_start_y - 65,
            self.front_pointer_start_x + 5,
            self.front_pointer_start_y - 65,
            self.front_pointer_start_x + 5,
            self.front_pointer_start_y - 20,
            self.front_pointer_start_x + 10,
            self.front_pointer_start_y - 20,
        ]
        self.front_pointer_index = self.queue_canvas.create_polygon(
            self.front_pointer_coords, outline="black", fill="red", width=1
        )

        self.front_pointer_label = Label(
            self.queue_canvas,
            text="Front / Tail",
            bg=colors.bg_canvas,
            fg="red",
            font=("Arial", 15, "bold"),
        )
        self.front_pointer_label.place(
            x=self.front_pointer_coords[0] - 50, y=self.front_pointer_coords[7] - 35
        )

        self.tail_pointer_label = Label(
            self.queue_canvas,
            text="Tail",
            bg=colors.bg_canvas,
            fg="red",
            font=("Arial", 15, "bold"),
        )

    def create_queue_index(self):
        n = 8
        start = 190
        space = 54
        index = []
        for i in range(n):
            index.append(i)
        for i in range(len(index) - 1, -1, -1):
            index[i] = Label(
                self.queue_canvas,
                text=str(i),
                bg=colors.bg_canvas,
                fg="red",
                font=("Arial", 20, "bold"),
            )
            index[i].place(x=start, y=200)
            start += space

        index[0] = Label(
            self.queue_canvas,
            text=str(-1),
            bg=colors.bg_canvas,
            fg="red",
            font=("Arial", 20, "bold"),
        )
        index[0].place(x=start - 9, y=200)

    def create_queue_container(self):
        self.queue_canvas.create_line(175, 250, 605, 250, fill="red", width=4)
        self.queue_canvas.create_line(175, 300, 605, 300, fill="red", width=4)
        # self.queue_canvas.create_line(177, 250, 603, 250, fill="red", width=4)
        # self.queue_canvas.create_line(177, 300, 603, 300, fill="red", width=4)

    def push_element(self):
        if len(self.queue_element) == 8:
            messagebox.showerror("Overflow", "Queue is full !")
        else:
            self.push_btn.config(state=DISABLED)
            self.pop_btn.config(state=DISABLED)

            self.element_take_label = Label(
                self.window,
                text="Enter the element value",
                bg=colors.bg_window,
                fg="brown",
                font=("Arial", 12, "bold"),
            )
            self.element_take_label.place(x=200, y=536)

            self.element_take_entry = Entry(
                self.window,
                font=("Arial", 13, "bold"),
                bg="white",
                fg="blue",
                relief=SUNKEN,
                bd=5,
            )
            self.element_take_entry.place(x=200, y=560)
            self.element_take_entry.focus()

            self.go_pushing_btn = HoverButton(
                self.window,
                text="Push",
                font=("Arial", 10, "bold"),
                bg="blue",
                fg="red",
                relief=RAISED,
                bd=3,
                padx=3,
                pady=3,
                cursor="hand2",
                command=self.create_new_element,
            )
            self.go_pushing_btn.place(x=400, y=560)

    def create_new_element(self):
        try:
            if self.element_take_entry.get() == "":
                messagebox.showerror("Error", "Enter an integer !!!")
                return
            self.element_take_label.place_forget()
            self.element_take_entry.place_forget()
            self.go_pushing_btn.place_forget()

            self.block_store.insert(
                0,
                self.queue_canvas.create_rectangle(
                    self.block_left,
                    self.block_up,
                    self.block_right,
                    self.block_down,
                    fill="black",
                    width=2,
                    outline="red",
                ),
            )

            self.new_element_value = int(self.element_take_entry.get())
            self.queue_element.insert(0, self.new_element_value)
            x1, y1, x2, y2 = self.queue_canvas.coords(self.block_store[0])
            text_x = (x1 + x2) / 2
            text_y = (y1 + y2) / 2

            self.block_value_store.insert(
                0,
                self.queue_canvas.create_text(
                    text_x,
                    text_y,
                    text=self.new_element_value,
                    font=("Arial", 15, "bold"),
                    fill="white",
                ),
            )
            self.element_take_entry.delete(0, END)
            self.element_take_entry.insert(0, "")
            # print(self.queue_element)
            self.push_data()
        except Exception as e:
            print(e)
            self.pop_btn.config(state=NORMAL)
            self.push_btn.config(state=NORMAL)
            self.queue_canvas.delete(self.block_store[0])
            messagebox.showerror("Error", "Just only input integer !!!")

    def update_front_pointer_coords(self):
        self.front_pointer_coords = [
            self.front_pointer_start_x,
            self.front_pointer_start_y,
            self.front_pointer_start_x - 10,
            self.front_pointer_start_y - 20,
            self.front_pointer_start_x - 5,
            self.front_pointer_start_y - 20,
            self.front_pointer_start_x - 5,
            self.front_pointer_start_y - 65,
            self.front_pointer_start_x + 5,
            self.front_pointer_start_y - 65,
            self.front_pointer_start_x + 5,
            self.front_pointer_start_y - 20,
            self.front_pointer_start_x + 10,
            self.front_pointer_start_y - 20,
        ]

    def update_tail_pointer_coords(self):
        self.tail_pointer_coords = [
            self.tail_pointer_start_x,
            self.tail_pointer_start_y,
            self.tail_pointer_start_x - 10,
            self.tail_pointer_start_y - 20,
            self.tail_pointer_start_x - 5,
            self.tail_pointer_start_y - 20,
            self.tail_pointer_start_x - 5,
            self.tail_pointer_start_y - 65,
            self.tail_pointer_start_x + 5,
            self.tail_pointer_start_y - 65,
            self.tail_pointer_start_x + 5,
            self.tail_pointer_start_y - 20,
            self.tail_pointer_start_x + 10,
            self.tail_pointer_start_y - 20,
        ]

    def push_data(self):
        try:
            self.right_achieve -= self.decrease_x

            # move down new element
            while self.number_set_y > 300:
                self.queue_canvas.delete(self.block_store[0])
                self.queue_canvas.delete(self.block_value_store[0])

                self.number_set_y -= 2
                self.block_up -= 2
                self.block_down -= 2

                self.block_store.pop(0)
                self.block_value_store.pop(0)
                self.block_store.insert(
                    0,
                    self.queue_canvas.create_rectangle(
                        self.block_left,
                        self.block_up,
                        self.block_right,
                        self.block_down,
                        fill="black",
                        width=2,
                        outline="red",
                    ),
                )

                x1, y1, x2, y2 = self.queue_canvas.coords(self.block_store[0])
                text_x = (x1 + x2) / 2
                text_y = (y1 + y2) / 2
                self.block_value_store.insert(
                    0,
                    self.queue_canvas.create_text(
                        text_x,
                        text_y,
                        text=self.new_element_value,
                        font=("Arial", 15, "bold"),
                        fill="white",
                    ),
                )
                time.sleep(self.move_delay)
                self.window.update()

            # move right new element
            while self.number_set_x < self.right_achieve:
                self.queue_canvas.delete(self.block_store[0])
                self.queue_canvas.delete(self.block_value_store[0])

                self.number_set_x += 2
                self.block_left += 2
                self.block_right += 2

                self.block_store.pop(0)
                self.block_value_store.pop(0)
                self.block_store.insert(
                    0,
                    self.queue_canvas.create_rectangle(
                        self.block_left,
                        self.block_up,
                        self.block_right,
                        self.block_down,
                        width=2,
                        outline="red",
                        fill="black",
                    ),
                )

                x1, y1, x2, y2 = self.queue_canvas.coords(self.block_store[0])
                text_x = (x1 + x2) / 2
                text_y = (y1 + y2) / 2
                self.block_value_store.insert(
                    0,
                    self.queue_canvas.create_text(
                        text_x,
                        text_y,
                        text=self.queue_element[0],
                        font=("Arial", 15, "bold"),
                        fill="white",
                    ),
                )
                time.sleep(self.move_delay)
                self.window.update()

            # move front pointer and tail pointer when enqueueing new element
            i = self.space_between_two_indexes
            j = 0
            while i > 0:
                if len(self.queue_element) <= 1:
                    self.queue_canvas.delete(self.front_pointer_index)

                    self.front_pointer_start_x -= 1
                    self.update_front_pointer_coords()

                    self.front_pointer_index = self.queue_canvas.create_polygon(
                        self.front_pointer_coords, outline="black", fill="red", width=1
                    )

                    self.front_pointer_label.place(
                        x=self.front_pointer_coords[0] - 50,
                        y=self.front_pointer_coords[7] - 35,
                    )

                    self.tail_pointer_label = Label(
                        self.queue_canvas,
                        text="Tail",
                        bg=colors.bg_canvas,
                        fg="red",
                        font=("Arial", 15, "bold"),
                    )

                    self.tail_pointer_start_x = self.front_pointer_start_x
                else:
                    self.queue_canvas.delete(self.tail_pointer_index)

                    self.front_pointer_label.configure(text="Front")
                    self.front_pointer_label.place(
                        x=self.front_pointer_coords[0] - 30,
                        y=self.front_pointer_coords[7] - 35,
                    )

                    self.tail_pointer_start_x -= 1
                    self.update_tail_pointer_coords()
                    self.tail_pointer_index = self.queue_canvas.create_polygon(
                        self.tail_pointer_coords, outline="black", fill="red", width=1
                    )

                    self.tail_pointer_label.configure(bg=colors.bg_canvas)

                    self.tail_pointer_label.place(
                        x=self.tail_pointer_coords[0] - 20,
                        y=self.tail_pointer_coords[7] - 35,
                    )

                i -= 1
                time.sleep(self.move_delay)
                self.window.update()
            # print(
            #     [
            #         "push",
            #         ["self.tail_pointer_start_x", self.tail_pointer_start_x],
            #         ["self.front_pointer_start_x", self.front_pointer_start_x],
            #     ]
            # )
            self.reset_block_start_position()
        except Exception as e:
            print(e)

    def reset_block_start_position(self):
        self.push_btn.config(state=NORMAL)
        self.pop_btn.config(state=NORMAL)
        self.number_set_x = 40
        self.number_set_y = 447
        self.block_up = 401
        self.block_left = 26
        self.block_right = self.block_left + 46
        self.block_down = self.block_up + 44
        self.decrease_x = 54

    def pop_data(self):
        if len(self.queue_element) == 0:
            messagebox.showinfo("Underflow", "Queue is empty !")
        else:
            self.push_btn.config(state=DISABLED)
            self.pop_btn.config(state=DISABLED)
            n = len(self.queue_element)
            x1, y1, x2, y2 = self.queue_canvas.coords(self.block_store[n - 1])
            items = self.queue_canvas.find_closest(x1, y1)
            front_queue_element = self.queue_element.pop()

            for item in items:
                if item == self.block_store[n - 1]:
                    while x2 < self.delete_element_x:
                        self.queue_canvas.delete(self.block_store[n - 1])
                        self.queue_canvas.delete(self.block_value_store[n - 1])

                        x1 += 2
                        x2 += 2

                        self.block_store[n - 1] = self.queue_canvas.create_rectangle(
                            x1,
                            252,
                            x2,
                            252 + 45,
                            fill="black",
                            width=2,
                            outline="red",
                        )

                        xx1, yy1, xx2, yy2 = self.queue_canvas.coords(
                            self.block_store[n - 1]
                        )
                        text_x = (xx1 + xx2) / 2
                        text_y = (yy1 + yy2) / 2
                        self.block_value_store[n - 1] = self.queue_canvas.create_text(
                            text_x,
                            text_y,
                            text=front_queue_element,
                            font=("Arial", 15, "bold"),
                            fill="white",
                        )

                        time.sleep(self.move_delay)
                        self.window.update()
                    self.right_achieve += self.decrease_x
                    time.sleep(self.deleted_element_delay)
                    self.queue_canvas.delete(self.block_store[n - 1])
                    self.queue_canvas.delete(self.block_value_store[n - 1])
                    self.update_queue_after_pop_data()
                    self.block_store.pop()
                    self.block_value_store.pop()

            self.push_btn.config(state=NORMAL)
            self.pop_btn.config(state=NORMAL)

    def update_queue_after_pop_data(self):
        # print(self.queue_element)
        n = len(self.queue_element)
        i = n
        right = 602
        # move all element to right after dequeueing
        while i > 0:
            x1, y1, x2, y2 = self.queue_canvas.coords(self.block_store[i - 1])
            x = x2
            items = self.queue_canvas.find_closest(x1, y1)
            for item in items:
                if item == self.block_store[i - 1]:
                    while x2 < right:
                        self.queue_canvas.delete(self.block_store[i - 1])
                        self.queue_canvas.delete(self.block_value_store[i - 1])

                        x1 += 2
                        x2 += 2
                        self.block_store[i - 1] = self.queue_canvas.create_rectangle(
                            x1,
                            252,
                            x2,
                            252 + 45,
                            fill="black",
                            width=2,
                            outline="red",
                        )

                        xx1, yy1, xx2, yy2 = self.queue_canvas.coords(
                            self.block_store[i - 1]
                        )

                        text_x = (xx1 + xx2) / 2
                        text_y = (yy1 + yy2) / 2

                        self.block_value_store[i - 1] = self.queue_canvas.create_text(
                            text_x,
                            text_y,
                            text=self.queue_element[i - 1],
                            font=("Arial", 15, "bold"),
                            fill="white",
                        )

                        time.sleep(self.move_delay)
                        self.window.update()
                    right -= self.decrease_x
            i -= 1

        i = self.space_between_two_indexes

        if n == 0:
            while i > 0:
                self.queue_canvas.delete(self.tail_pointer_index)
                self.queue_canvas.delete(self.front_pointer_index)

                self.front_pointer_start_x += 1
                self.update_front_pointer_coords()
                self.front_pointer_index = self.queue_canvas.create_polygon(
                    self.front_pointer_coords,
                    fill="red",
                    outline="black",
                    width=1,
                )

                self.front_pointer_label.configure(bg=colors.bg_canvas)

                self.front_pointer_label.place(
                    x=self.front_pointer_coords[0] - 50,
                    y=self.front_pointer_coords[7] - 35,
                )
                i -= 1
                time.sleep(self.move_delay)
                self.window.update()
            self.front_pointer_start_x = 632
            self.front_pointer_label.configure(text="Front / Tail")
            self.queue_canvas.delete(self.tail_pointer_index)
            self.tail_pointer_label.place_forget()
        elif n == 1:
            while i > 0:
                self.queue_canvas.delete(self.tail_pointer_index)

                self.tail_pointer_label.place_forget()

                self.tail_pointer_start_x += 1
                self.update_tail_pointer_coords()

                self.tail_pointer_index = self.queue_canvas.create_polygon(
                    self.tail_pointer_coords,
                    fill="red",
                    outline="black",
                    width=1,
                )

                self.tail_pointer_label.configure(bg=colors.bg_canvas)

                self.front_pointer_label.configure(text="Front / Tail")
                self.front_pointer_label.place(
                    x=self.front_pointer_coords[0] - 50,
                    y=self.front_pointer_coords[7] - 35,
                )
                i -= 1
                time.sleep(self.move_delay)
                self.window.update()
        elif n > 1:
            while i > 0:
                self.queue_canvas.delete(self.tail_pointer_index)

                self.tail_pointer_start_x += 1
                self.update_tail_pointer_coords()
                self.tail_pointer_index = self.queue_canvas.create_polygon(
                    self.tail_pointer_coords,
                    fill="red",
                    outline="black",
                    width=1,
                )

                self.tail_pointer_label.configure(bg=colors.bg_canvas)

                self.tail_pointer_label.place(
                    x=self.tail_pointer_coords[0] - 20,
                    y=self.tail_pointer_coords[7] - 35,
                )

                i -= 1
                time.sleep(self.move_delay)
                self.window.update()

        # print(
        #     [
        #         n,
        #         "pop",
        #         ["self.tail_pointer_start_x", self.tail_pointer_start_x],
        #         ["self.front_pointer_start_x", self.front_pointer_start_x],
        #     ]
        # )


# center window
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 3
    window.geometry(f"{width}x{height}+{x}+{y}")


if __name__ == "__main__":
    window = Tk()
    window.title("Queue Visualization")
    window.maxsize(800, 600)
    window.minsize(800, 600)
    QueueVisualization(window)
    window.mainloop()
