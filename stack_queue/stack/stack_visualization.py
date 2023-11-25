from tkinter import *
from tkinter import messagebox
import time
import colors
from customs import *


class StackVisualization:
    def __init__(self, root):
        self.window = root
        self.window.config(bg=colors.bg_window)

        # init store element is pushed to top stack
        self.stack_element = []

        # init store coords of per element
        self.coord_blocks = []

        # init store rectangle
        self.block_store = []

        # init store value inside rectangle
        self.value = []

        # init store coords of pointer points to top stack element
        self.top_pointer_coords = []

        # decrease from bottom stack to top stack
        self.extra_decrease = 0

        # index of per element in stack
        self.index = 0

        # init some UI elements
        self.heading_name = None
        self.sub_heading = None
        self.stack_container_label = None
        self.push_btn = None
        self.pop_btn = None
        self.element_take_entry = None
        self.element_take_label = None
        self.push_go_btn = None
        self.top_pointer_index = None
        self.new_element_value = None
        self.top_pointer_label = None
        # init empty stack index

        self.index_neg = None

        # init size of canvas
        self.canvas_width = 600
        self.canvas_height = 500

        # init coords
        self.number_set_x = 40
        self.number_set_y = 110
        self.block_up = 100
        self.block_left = 26
        self.block_right = 72
        self.block_down = 135
        self.down_achieve = 400
        self.top_pointer_start_x = 320
        self.top_pointer_start_y = 420

        # init canvas
        self.stack_canvas = Canvas(
            self.window,
            width=self.canvas_width,
            height=self.canvas_height,
            bg=colors.bg_canvas,
            relief=GROOVE,
            bd=5,
        )
        self.stack_canvas.pack(fill=BOTH)

        # call some methods to create base UI
        self.create_heading_and_sub_heading()
        self.create_some_buttons()
        self.create_top_pointer()
        self.create_stack_container()
        self.create_stack_index()
        self.center_window(600, 600)

    def center_window(self, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 4
        self.window.geometry(f"{width}x{height}+{x}+{y}")

    # create heading and subheading
    def create_heading_and_sub_heading(self):
        self.heading_name = Label(
            self.stack_canvas,
            text="Stack Visualization",
            bg=colors.bg_canvas,
            fg="red",
            font=("Arial", 30, "bold"),
        )
        self.heading_name.place(x=125, y=20)

        self.sub_heading = Label(
            self.stack_canvas,
            text="Index number",
            bg=colors.bg_canvas,
            fg="red",
            font=("Arial", 15, "bold"),
        )
        self.sub_heading.place(x=20, y=300)

        self.stack_container_label = Label(
            self.stack_canvas,
            text="Stack Container",
            bg=colors.bg_canvas,
            fg="red",
            font=("Arial", 20, "bold"),
        )
        self.stack_container_label.place(x=180, y=450)

    # create push and pop buttons
    def create_some_buttons(self):
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
        self.push_btn.place(x=30, y=535)

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
        self.pop_btn.place(x=450, y=535)

    # create top pointer points to top stack element
    def create_top_pointer(self):
        self.top_pointer_coords = [
            self.top_pointer_start_x,
            self.top_pointer_start_y,
            self.top_pointer_start_x + 15,
            self.top_pointer_start_y - 10,
            self.top_pointer_start_x + 15,
            self.top_pointer_start_y - 5,
            self.top_pointer_start_x + 65,
            self.top_pointer_start_y - 5,
            self.top_pointer_start_x + 65,
            self.top_pointer_start_y + 5,
            self.top_pointer_start_x + 15,
            self.top_pointer_start_y + 5,
            self.top_pointer_start_x + 15,
            self.top_pointer_start_y + 10,
        ]

        self.top_pointer_index = self.stack_canvas.create_polygon(
            self.top_pointer_coords, outline="black", fill="red", width=1.5
        )

        self.top_pointer_label = Label(
            self.stack_canvas,
            text="Top",
            bg=colors.bg_canvas,
            fg="red",
            font=("Arial", 15, "bold"),
        )
        self.top_pointer_label.place(
            x=self.top_pointer_coords[6] + 10, y=self.top_pointer_coords[7] - 10
        )

    # create stack containter
    def create_stack_container(self):
        self.stack_canvas.create_line(250, 150, 250, 402, fill="#A2CD5A", width=4)
        self.stack_canvas.create_line(250, 400, 300, 400, fill="#A2CD5A", width=4)
        self.stack_canvas.create_line(300, 150, 300, 402, fill="#A2CD5A", width=4)
        for i in range(6):
            self.block_store.append(i)
        for i in range(6):
            self.value.append(i)

    # create stack element index
    def create_stack_index(self):
        n = 6
        self.index_neg = Label(
            self.stack_canvas,
            text="-1",
            fg="blue",
            bg=colors.bg_canvas,
            font=("Arial", 15, "bold"),
        )
        self.index_neg.place(x=215, y=405)

        index = []

        for i in range(n):
            index.append(i)

        yy = 365
        for i in range(len(index)):
            index[i] = Label(
                self.stack_canvas,
                text=str(i),
                fg="blue",
                bg=colors.bg_canvas,
                font=("Arial", 15, "bold"),
            )
            index[i].place(x=220, y=yy)

            yy -= 40

    # push element method
    def push_element(self):
        if len(self.stack_element) == 6:
            messagebox.showinfo("Overflow", "Stack is full !!!")
        else:
            self.push_btn.config(state=DISABLED)
            self.pop_btn.config(state=DISABLED)

            # create label entry
            self.element_take_label = Label(
                self.window,
                text="Enter the element value",
                bg=colors.bg_window,
                fg="brown",
                font=("Arial", 12, "bold"),
            )
            self.element_take_label.place(x=200, y=536)

            # create entry to get value
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

            # create add button to push value to stack
            self.push_go_btn = HoverButton(
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
            self.push_go_btn.place(x=400, y=560)

    def create_new_element(self):
        try:
            if self.element_take_entry.get() == "":
                messagebox.showerror("Error", "Enter an integer !!!")
                return
            self.element_take_label.place_forget()
            self.element_take_entry.place_forget()
            self.push_go_btn.place_forget()

            self.block_store[self.index] = self.stack_canvas.create_rectangle(
                self.block_left,
                self.block_up,
                self.block_right,
                self.block_down,
                fill="black",
                width=2,
                outline="blue",
            )

            self.new_element_value = int(self.element_take_entry.get())
            self.stack_element.append(self.new_element_value)
            print(self.stack_element)
            x1, y1, x2, y2 = self.stack_canvas.coords(self.block_store[self.index])
            text_x = (x1 + x2) / 2
            text_y = (y1 + y2) / 2
            self.value[self.index] = self.stack_canvas.create_text(
                text_x,
                text_y,
                text=self.new_element_value,
                font=("Arial", 10, "bold"),
                fill="white",
            )
            self.element_take_entry.delete(0, END)
            self.element_take_entry.insert(0, "")

            self.push_data()
        except:
            self.stack_canvas.delete(self.block_store[self.index])
            messagebox.showerror("Error", "Just only input integer !!!")
            self.pop_btn.config(state=NORMAL)
            self.push_btn.config(state=NORMAL)
            pass

    def push_data(self):
        try:
            # set position for per block
            self.down_achieve -= 28 + self.extra_decrease

            while self.number_set_x < 265:
                self.stack_canvas.delete(self.block_store[self.index])
                self.stack_canvas.delete(self.value[self.index])

                self.number_set_x += 2
                self.block_left += 2
                self.block_right += 2
                self.block_store[self.index] = self.stack_canvas.create_rectangle(
                    self.block_left,
                    self.block_up,
                    self.block_right,
                    self.block_down,
                    fill="black",
                    width=2,
                    outline="blue",
                )
                x1, y1, x2, y2 = self.stack_canvas.coords(self.block_store[self.index])
                text_x = (x1 + x2) / 2
                text_y = (y1 + y2) / 2
                self.value[self.index] = self.stack_canvas.create_text(
                    text_x,
                    text_y,
                    text=self.new_element_value,
                    font=("Arial", 10, "bold"),
                    fill="white",
                )
                time.sleep(0.01)
                self.window.update()

            while self.number_set_y < self.down_achieve:
                self.stack_canvas.delete(self.block_store[self.index])
                self.stack_canvas.delete(self.value[self.index])

                self.number_set_y += 2
                self.block_up += 2
                self.block_down += 2
                self.block_store[self.index] = self.stack_canvas.create_rectangle(
                    self.block_left,
                    self.block_up,
                    self.block_right,
                    self.block_down,
                    fill="black",
                    width=2,
                    outline="blue",
                )
                x1, y1, x2, y2 = self.stack_canvas.coords(self.block_store[self.index])
                text_x = (x1 + x2) / 2
                text_y = (y1 + y2) / 2
                self.value[self.index] = self.stack_canvas.create_text(
                    text_x,
                    text_y,
                    text=self.new_element_value,
                    font=("Arial", 10, "bold"),
                    fill="white",
                )
                time.sleep(0.005)
                self.window.update()

            # set top index pointer
            i = 40
            while i > 0:
                self.top_pointer_start_y -= 1
                i -= 1
                self.stack_canvas.delete(self.top_pointer_index)
                self.top_pointer_coords = [
                    self.top_pointer_start_x,
                    self.top_pointer_start_y,
                    self.top_pointer_start_x + 15,
                    self.top_pointer_start_y - 10,
                    self.top_pointer_start_x + 15,
                    self.top_pointer_start_y - 5,
                    self.top_pointer_start_x + 65,
                    self.top_pointer_start_y - 5,
                    self.top_pointer_start_x + 65,
                    self.top_pointer_start_y + 5,
                    self.top_pointer_start_x + 15,
                    self.top_pointer_start_y + 5,
                    self.top_pointer_start_x + 15,
                    self.top_pointer_start_y + 10,
                ]
                self.top_pointer_index = self.stack_canvas.create_polygon(
                    self.top_pointer_coords, outline="black", fill="red", width=1.5
                )
                self.top_pointer_label.place(
                    x=self.top_pointer_coords[6] + 10,
                    y=self.top_pointer_coords[7] - 10,
                )
                time.sleep(0.005)
                self.window.update()
            self.coord_blocks.append(
                self.stack_canvas.coords(self.block_store[self.index])
            )
            self.index += 1
            self.reset_block_start_position()
        except:
            pass

    # reset block position
    def reset_block_start_position(self):
        self.push_btn.config(state=NORMAL)
        self.pop_btn.config(state=NORMAL)

        self.block_left = 26
        self.block_up = 100
        self.block_right = 72
        self.block_down = 135
        self.number_set_x = 40
        self.number_set_y = 110
        self.extra_decrease = 12

    # pop element methods
    def pop_data(self):  # Data containing block get out from stack container
        if len(self.stack_element) == 0:  # Stack container empty checking
            messagebox.showinfo("Underflow", "Stack is empty")
        else:
            x1, y1, x2, y2 = self.stack_canvas.coords(self.block_store[self.index - 1])
            items = self.stack_canvas.find_closest(x1, y1)
            top_stack_element = self.stack_element.pop()
            for item in items:
                if item == self.block_store[self.index - 1]:
                    while y1 > 80:
                        self.stack_canvas.delete(self.block_store[self.index - 1])
                        self.stack_canvas.delete(self.value[self.index - 1])

                        y1 -= 2
                        y2 -= 2
                        self.block_store[
                            self.index - 1
                        ] = self.stack_canvas.create_rectangle(
                            252,
                            y1,
                            252 + 45,
                            y2,
                            fill="black",
                            width=2,
                            outline="blue",
                        )
                        xx1, yy1, xx2, yy2 = self.stack_canvas.coords(
                            self.block_store[self.index - 1]
                        )
                        text_x = (xx1 + xx2) / 2
                        text_y = (yy1 + yy2) / 2
                        self.value[self.index - 1] = self.stack_canvas.create_text(
                            text_x,
                            text_y,
                            text=top_stack_element,
                            font=("Arial", 10, "bold"),
                            fill="white",
                        )
                        time.sleep(0.01)
                        self.window.update()
                    time.sleep(0.5)
                    self.stack_canvas.delete(self.block_store[self.index - 1])
                    self.stack_canvas.delete(self.value[self.index - 1])
                    self.stack_canvas.delete(self.top_pointer_index)
                    i = 40

                    while i > 0:
                        self.stack_canvas.delete(self.top_pointer_index)
                        self.top_pointer_start_y += 1
                        self.top_pointer_coords = [
                            self.top_pointer_start_x,
                            self.top_pointer_start_y,
                            self.top_pointer_start_x + 15,
                            self.top_pointer_start_y - 10,
                            self.top_pointer_start_x + 15,
                            self.top_pointer_start_y - 5,
                            self.top_pointer_start_x + 65,
                            self.top_pointer_start_y - 5,
                            self.top_pointer_start_x + 65,
                            self.top_pointer_start_y + 5,
                            self.top_pointer_start_x + 15,
                            self.top_pointer_start_y + 5,
                            self.top_pointer_start_x + 15,
                            self.top_pointer_start_y + 10,
                        ]
                        self.top_pointer_index = self.stack_canvas.create_polygon(
                            self.top_pointer_coords,
                            outline="black",
                            fill="red",
                            width=1.5,
                        )
                        self.top_pointer_label.place(
                            x=self.top_pointer_coords[6] + 10,
                            y=self.top_pointer_coords[7] - 10,
                        )
                        self.push_btn.config(state=DISABLED)
                        self.pop_btn.config(state=DISABLED)
                        i -= 1
                        time.sleep(0.01)
                        self.window.update()
                    self.down_achieve += 28 + self.extra_decrease
            self.index -= 1
            self.push_btn.config(state=NORMAL)
            self.pop_btn.config(state=NORMAL)
            self.reset_block_start_position()


if __name__ == "__main__":
    window = Tk()
    window.title("Stack Visualization")
    window.maxsize(600, 600)
    window.minsize(600, 600)
    StackVisualization(window)
    window.mainloop()
