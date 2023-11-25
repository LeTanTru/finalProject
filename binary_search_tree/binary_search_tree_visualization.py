from tkinter import *
from random import randint
from tkinter import messagebox
from variables import *
from customs import *
import time


class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BST:
    def __init__(self, root):
        self.window = root
        self.canvas = Canvas(
            self.window,
            bg=BACKGROUND_COLOR,
        )
        self.canvas.pack(side=TOP, fill=BOTH, expand=2)

        self.generate_random_tree_btn = None
        self.insert_btn = None
        self.delete_btn = None
        self.search_btn = None
        self.input_field = None
        self.root_node = None

        self.create_some_buttons()
        self.center_window(WINDOW_WIDTH, WINDOW_HEIGHT)

    # center window
    def center_window(self, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 4
        self.window.geometry(f"{width}x{height}+{x}+{y}")

    def create_some_buttons(self):
        pass
        self.generate_random_tree_btn = HoverButton(
            self.window,
            text="Generate random tree",
            font=("Arial 15"),
            cursor="hand2",
            width=25,
            bd=4,
            relief=GROOVE,
            command=self.generate_random_tree,
        )
        self.generate_random_tree_btn.pack(side=LEFT, fill=X, expand=1)

        self.insert_btn = HoverButton(
            self.window,
            text="Insert",
            font=("Arial 15"),
            cursor="hand2",
            width=20,
            bd=4,
            relief=GROOVE,
            command=self.insert_node_to_tree,
        )
        self.insert_btn.pack(side=LEFT, fill=X, expand=1)

        self.search_btn = HoverButton(
            self.window,
            text="Search",
            font=("Arial 15"),
            cursor="hand2",
            width=20,
            bd=4,
            relief=GROOVE,
            command=self.search_node_on_tree,
        )
        self.search_btn.pack(side=LEFT, fill=X, expand=1)

        self.delete_btn = HoverButton(
            self.window,
            text="Delete",
            font=("Arial 15"),
            cursor="hand2",
            width=20,
            bd=4,
            relief=GROOVE,
            command=self.delete_node_on_tree,
        )
        self.delete_btn.pack(side=LEFT, fill=X, expand=1)

        self.input_field = Entry(
            self.window,
            font=("Arial 15"),
            width=18,
            bd=4,
            relief=GROOVE,
        )
        self.input_field.pack(side=LEFT, fill=X, expand=1)
        self.input_field.focus()

    def calculate_left_child_position(
        self, parent_position_x, parent_position_y, child_depth
    ):
        left_child_position_x = (
            parent_position_x - ((WINDOW_WIDTH - X_PADDING) / pow(2, child_depth)) / 2
        )
        left_child_position_y = parent_position_y + NODE_RADIUS * 4
        return (left_child_position_x, left_child_position_y)

    def calculate_right_child_position(
        self, parent_position_x, parent_position_y, child_depth
    ):
        right_child_position_x = (
            parent_position_x + ((WINDOW_WIDTH - X_PADDING) / pow(2, child_depth)) / 2
        )
        right_child_position_y = parent_position_y + NODE_RADIUS * 4
        return (right_child_position_x, right_child_position_y)

    def insert_node_without_animation(self, root_node, value, node_depth):
        if node_depth > MAX_DEPTH:
            return root_node

        if root_node is None:
            root_node = Node(value)
            return root_node

        if value < root_node.value:
            root_node.left_child = self.insert_node_without_animation(
                root_node.left_child, value, node_depth + 1
            )
        elif value > root_node.value:
            root_node.right_child = self.insert_node_without_animation(
                root_node.right_child, value, node_depth + 1
            )

        return root_node

    def draw_tree(self, root_node, root_position_x, root_position_y, node_depth):
        if root_node is None:
            return

        if root_node.left_child is not None:
            (
                left_child_position_x,
                left_child_position_y,
            ) = self.calculate_left_child_position(
                root_position_x, root_position_y, node_depth + 1
            )

            self.canvas.create_line(
                root_position_x,
                root_position_y,
                left_child_position_x,
                left_child_position_y,
                fill=LINE_COLOR,
                width=5,
            )
            self.draw_tree(
                root_node.left_child,
                left_child_position_x,
                left_child_position_y,
                node_depth + 1,
            )

        if root_node.right_child is not None:
            (
                right_child_position_x,
                right_child_position_y,
            ) = self.calculate_right_child_position(
                root_position_x, root_position_y, node_depth + 1
            )
            self.canvas.create_line(
                root_position_x,
                root_position_y,
                right_child_position_x,
                right_child_position_y,
                fill=LINE_COLOR,
                width=5,
            )
            self.draw_tree(
                root_node.right_child,
                right_child_position_x,
                right_child_position_y,
                node_depth + 1,
            )

        self.create_oval_with_text(
            root_position_x,
            root_position_y,
            NODE_RADIUS,
            NODE_COLOR,
            root_node.value,
            TEXT_COLOR,
            FONT_SIZE,
        )
        self.window.update()

    def clear_canvas_and_draw_tree(self):
        tree_position_x = WINDOW_WIDTH / 2
        tree_position_y = Y_PADDING
        self.canvas.delete("all")
        self.draw_tree(self.root_node, tree_position_x, tree_position_y, 0)

    def generate_random_tree(self):
        self.root_node = None
        number_of_insert = 0
        while number_of_insert < 20 or number_of_insert > 35:
            number_of_insert = randint(MIN_VALUE, MAX_VALUE)

        for x in range(number_of_insert):
            node_value = randint(MIN_VALUE, MAX_VALUE)
            self.root_node = self.insert_node_without_animation(
                self.root_node, node_value, 0
            )

        root_position_x = WINDOW_WIDTH / 2
        root_position_y = Y_PADDING

        self.canvas.delete("all")

        self.draw_tree(self.root_node, root_position_x, root_position_y, 0)

    def print_tree(self, root_node):
        if root_node is not None:
            self.print_tree(root_node.left_child)
            print(root_node.value, end=" ")
            self.print_tree(root_node.right_child)

    def insert_node(
        self, root_node, value, root_position_x, root_position_y, node_depth
    ):
        if node_depth > MAX_DEPTH:
            messagebox.showinfo(title="Insert node", message="Max depth reached")
            return root_node

        if root_node is None:
            root_node = Node(value)
            return root_node

        self.create_oval_with_text(
            root_position_x,
            root_position_y - 3 * NODE_RADIUS,
            NODE_RADIUS,
            HIGHLIGHT_COLOR,
            value,
            HIGHLIGHT_TEXT_COLOR,
            FONT_SIZE,
        )
        self.window.update()
        time.sleep(ANIMATION_DELAY)

        if value < root_node.value:
            self.create_rectangle_with_text(
                root_position_x,
                root_position_y - 1.5 * NODE_RADIUS,
                NODE_RADIUS / 1.5,
                NODE_RADIUS / 1.5,
                HIGHLIGHT_COLOR,
                "<",
                HIGHLIGHT_TEXT_COLOR,
                FONT_SIZE,
            )
            self.window.update()
            time.sleep(ANIMATION_DELAY)

            (
                left_child_position_x,
                left_child_position_y,
            ) = self.calculate_left_child_position(
                root_position_x, root_position_y, node_depth + 1
            )

            root_node.left_child = self.insert_node(
                root_node.left_child,
                value,
                left_child_position_x,
                left_child_position_y,
                node_depth + 1,
            )
        elif value > root_node.value:
            self.create_rectangle_with_text(
                root_position_x,
                root_position_y - 1.5 * NODE_RADIUS,
                NODE_RADIUS / 1.5,
                NODE_RADIUS / 1.5,
                HIGHLIGHT_COLOR,
                ">",
                HIGHLIGHT_TEXT_COLOR,
                FONT_SIZE,
            )
            self.window.update()
            time.sleep(ANIMATION_DELAY)

            (
                right_child_position_x,
                right_child_position_y,
            ) = self.calculate_right_child_position(
                root_position_x,
                root_position_y,
                node_depth + 1,
            )
            root_node.right_child = self.insert_node(
                root_node.right_child,
                value,
                right_child_position_x,
                right_child_position_y,
                node_depth + 1,
            )
        elif value == root_node.value:
            messagebox.showinfo(title="Insert node", message="Node already in tree")

        return root_node

    def create_oval_with_text(
        self, center_x, center_y, radius, oval_color, text, text_color, font_size
    ):
        oval = self.canvas.create_oval(
            center_x - radius,
            center_y - radius,
            center_x + radius,
            center_y + radius,
            fill=oval_color,
            width=0,
        )
        text = self.canvas.create_text(
            center_x,
            center_y,
            text=text,
            fill=text_color,
            font=("Arial", int(font_size), "bold"),
        )

    def is_valid_input(self, value) -> bool:
        try:
            value = int(value)
        except ValueError:
            messagebox.showerror(title="ERROR", message="Invalid input")
            return False

        if value > MAX_VALUE:
            messagebox.showerror(
                title="ERROR", message="Input value exceeding max allowed"
            )
            return False
        if value < MIN_VALUE:
            messagebox.showerror(title="ERROR", message="Input value under min allowed")
            return False
        return True

    def create_rectangle_with_text(
        self,
        center_x,
        center_y,
        width,
        height,
        rectangle_color,
        text,
        text_color,
        font_size,
    ):
        self.canvas.create_rectangle(
            center_x - width / 2,
            center_y - height / 2,
            center_x + width / 2,
            center_y + height / 2,
            fill=rectangle_color,
            width=0,
        )

        self.canvas.create_text(
            center_x,
            center_y,
            text=text,
            fill=text_color,
            font=("Arial", int(font_size), "bold"),
        )

    def insert_node_to_tree(self):
        value = self.input_field.get()
        if not self.is_valid_input(value):
            return

        value = int(value)

        root_position_x = WINDOW_WIDTH / 2
        root_position_y = Y_PADDING

        self.disable_UI()

        self.root_node = self.insert_node(
            self.root_node, value, root_position_x, root_position_y, 0
        )

        time.sleep(0.5)

        self.canvas.delete("all")
        self.draw_tree(self.root_node, root_position_x, root_position_y, 0)

        self.enable_UI()
        self.print_tree(self.root_node)

    def search_node(
        self, root_node, value, root_position_x, root_position_y, node_depth
    ):
        if self.root_node is None:
            messagebox.showinfo(title="Search node", message="Tree is empty !")
            return

        if root_node is None:
            messagebox.showinfo(title="Search node", message="Node not found !")
            return

        self.create_oval_with_text(
            root_position_x,
            root_position_y - 3 * NODE_RADIUS,
            NODE_RADIUS,
            HIGHLIGHT_COLOR,
            value,
            HIGHLIGHT_TEXT_COLOR,
            FONT_SIZE,
        )
        self.window.update()
        time.sleep(ANIMATION_DELAY)

        if value < root_node.value:
            self.create_rectangle_with_text(
                root_position_x,
                root_position_y - 1.5 * NODE_RADIUS,
                NODE_RADIUS / 1.5,
                NODE_RADIUS / 1.5,
                HIGHLIGHT_COLOR,
                "<",
                HIGHLIGHT_TEXT_COLOR,
                FONT_SIZE,
            )
            self.window.update()
            time.sleep(ANIMATION_DELAY)

            (
                left_child_position_x,
                left_child_position_y,
            ) = self.calculate_left_child_position(
                root_position_x,
                root_position_y,
                node_depth + 1,
            )
            self.search_node(
                root_node.left_child,
                value,
                left_child_position_x,
                left_child_position_y,
                node_depth + 1,
            )
        elif value > root_node.value:
            self.create_rectangle_with_text(
                root_position_x,
                root_position_y - 1.5 * NODE_RADIUS,
                NODE_RADIUS / 1.5,
                NODE_RADIUS / 1.5,
                HIGHLIGHT_COLOR,
                ">",
                HIGHLIGHT_TEXT_COLOR,
                FONT_SIZE,
            )
            self.window.update()
            time.sleep(ANIMATION_DELAY)

            (
                right_child_position_x,
                right_child_position_y,
            ) = self.calculate_right_child_position(
                root_position_x,
                root_position_y,
                node_depth + 1,
            )
            self.search_node(
                root_node.right_child,
                value,
                right_child_position_x,
                right_child_position_y,
                node_depth + 1,
            )
        elif value == root_node.value:
            self.create_rectangle_with_text(
                root_position_x,
                root_position_y - 1.5 * NODE_RADIUS,
                NODE_RADIUS / 1.5,
                NODE_RADIUS / 1.5,
                HIGHLIGHT_COLOR,
                "=",
                HIGHLIGHT_TEXT_COLOR,
                FONT_SIZE,
            )
            self.create_oval_with_text(
                root_position_x,
                root_position_y,
                NODE_RADIUS,
                HIGHLIGHT_COLOR,
                value,
                HIGHLIGHT_TEXT_COLOR,
                FONT_SIZE,
            )
            self.window.update()
            time.sleep(ANIMATION_DELAY)

    def search_node_on_tree(self):
        value = self.input_field.get()

        if not self.is_valid_input(value):
            return
        value = int(value)
        self.input_field.delete(0, END)
        root_position_x = WINDOW_WIDTH / 2
        root_position_y = Y_PADDING

        self.disable_UI()
        self.search_node(self.root_node, value, root_position_x, root_position_y, 0)
        time.sleep(1)
        self.canvas.delete("all")
        self.draw_tree(self.root_node, root_position_x, root_position_y, 0)
        self.enable_UI()

    def get_min_node(self, root_node, root_position_x, root_position_y, node_depth):
        if root_node.left_child is None:
            self.create_rectangle_with_text(
                root_position_x,
                root_position_y - 1.5 * NODE_RADIUS,
                NODE_RADIUS,
                NODE_RADIUS / 1.5,
                HIGHLIGHT_COLOR,
                "MIN",
                HIGHLIGHT_TEXT_COLOR,
                FONT_SIZE / 1.5,
            )
            self.create_oval_with_text(
                root_position_x,
                root_position_y,
                NODE_RADIUS,
                HIGHLIGHT_COLOR,
                root_node.value,
                HIGHLIGHT_TEXT_COLOR,
                FONT_SIZE,
            )
            self.window.update()
            time.sleep(ANIMATION_DELAY)

            return root_node.value
        else:
            self.create_rectangle_with_text(
                root_position_x,
                root_position_y - 1.5 * NODE_RADIUS,
                NODE_RADIUS,
                NODE_RADIUS / 1.5,
                HIGHLIGHT_COLOR,
                "<<",
                HIGHLIGHT_TEXT_COLOR,
                FONT_SIZE,
            )
            self.window.update()
            time.sleep(ANIMATION_DELAY)

            (
                left_child_position_x,
                left_child_position_y,
            ) = self.calculate_left_child_position(
                root_position_x, root_position_y, node_depth + 1
            )
            return self.get_min_node(
                root_node.left_child,
                left_child_position_x,
                left_child_position_y,
                node_depth + 1,
            )

    def get_max_node(self, root_node, root_position_x, root_position_y, node_depth):
        if root_node.right_child is None:
            self.create_rectangle_with_text(
                root_position_x,
                root_position_y - 1.5 * NODE_RADIUS,
                NODE_RADIUS,
                NODE_RADIUS / 1.5,
                HIGHLIGHT_COLOR,
                "MAX",
                HIGHLIGHT_TEXT_COLOR,
                FONT_SIZE / 1.5,
            )
            self.create_oval_with_text(
                root_position_x,
                root_position_y,
                NODE_RADIUS,
                HIGHLIGHT_COLOR,
                root_node.value,
                HIGHLIGHT_TEXT_COLOR,
                FONT_SIZE,
            )
            self.window.update()
            time.sleep(ANIMATION_DELAY)

            return root_node.value
        else:
            self.create_rectangle_with_text(
                root_position_x,
                root_position_y - 1.5 * NODE_RADIUS,
                NODE_RADIUS,
                NODE_RADIUS / 1.5,
                HIGHLIGHT_COLOR,
                ">>",
                HIGHLIGHT_TEXT_COLOR,
                FONT_SIZE,
            )
            self.window.update()
            time.sleep(ANIMATION_DELAY)

            (
                right_child_position_x,
                right_child_position_y,
            ) = self.calculate_right_child_position(
                root_position_x, root_position_y, node_depth + 1
            )
            return self.get_max_node(
                root_node.right_child,
                right_child_position_x,
                right_child_position_y,
                node_depth + 1,
            )

    def delete_node(
        self,
        root_node,
        value,
        root_position_x,
        root_position_y,
        node_depth,
    ):
        if root_node is None:
            messagebox.showinfo(title="Delete", message="Node not found")
            return None

        self.create_oval_with_text(
            root_position_x,
            root_position_y - 3 * NODE_RADIUS,
            NODE_RADIUS,
            HIGHLIGHT_COLOR,
            value,
            HIGHLIGHT_TEXT_COLOR,
            FONT_SIZE,
        )
        self.window.update()
        time.sleep(ANIMATION_DELAY)

        if value < root_node.value:
            self.create_rectangle_with_text(
                root_position_x,
                root_position_y - 1.5 * NODE_RADIUS,
                NODE_RADIUS / 1.5,
                NODE_RADIUS / 1.5,
                HIGHLIGHT_COLOR,
                "<",
                HIGHLIGHT_TEXT_COLOR,
                FONT_SIZE,
            )
            self.window.update()
            time.sleep(ANIMATION_DELAY)

            (
                left_child_position_x,
                left_child_position_y,
            ) = self.calculate_left_child_position(
                root_position_x, root_position_y, node_depth + 1
            )
            root_node.left_child = self.delete_node(
                root_node.left_child,
                value,
                left_child_position_x,
                left_child_position_y,
                node_depth + 1,
            )
        elif value > root_node.value:
            self.create_rectangle_with_text(
                root_position_x,
                root_position_y - 1.5 * NODE_RADIUS,
                NODE_RADIUS / 1.5,
                NODE_RADIUS / 1.5,
                HIGHLIGHT_COLOR,
                ">",
                HIGHLIGHT_TEXT_COLOR,
                FONT_SIZE,
            )
            self.window.update()
            time.sleep(ANIMATION_DELAY)

            (
                right_child_position_x,
                right_child_position_y,
            ) = self.calculate_right_child_position(
                root_position_x, root_position_y, node_depth + 1
            )
            root_node.right_child = self.delete_node(
                root_node.right_child,
                value,
                right_child_position_x,
                right_child_position_y,
                node_depth + 1,
            )
        elif value == root_node.value:
            self.create_rectangle_with_text(
                root_position_x,
                root_position_y - 1.5 * NODE_RADIUS,
                NODE_RADIUS / 1.5,
                NODE_RADIUS / 1.5,
                HIGHLIGHT_COLOR,
                "=",
                HIGHLIGHT_TEXT_COLOR,
                FONT_SIZE,
            )
            self.create_oval_with_text(
                root_position_x,
                root_position_y,
                NODE_RADIUS,
                HIGHLIGHT_COLOR,
                value,
                HIGHLIGHT_TEXT_COLOR,
                FONT_SIZE,
            )
            self.window.update()
            time.sleep(ANIMATION_DELAY)

            if root_node.left_child is None and root_node.right_child is None:
                return None

            self.clear_canvas_and_draw_tree()

            if root_node.right_child is not None:
                self.create_rectangle_with_text(
                    root_position_x,
                    root_position_y - 1.5 * NODE_RADIUS,
                    6.5 * NODE_RADIUS,
                    NODE_RADIUS / 1.5,
                    HIGHLIGHT_COLOR,
                    "REPLACE WITH MIN >>",
                    HIGHLIGHT_TEXT_COLOR,
                    FONT_SIZE / 1.5,
                )

                self.window.update()
                time.sleep(ANIMATION_DELAY)

                (
                    right_child_position_x,
                    right_child_position_y,
                ) = self.calculate_right_child_position(
                    root_position_x, root_position_y, node_depth + 1
                )
                root_node.value = self.get_min_node(
                    root_node.right_child,
                    right_child_position_x,
                    right_child_position_y,
                    node_depth + 1,
                )

                self.create_oval_with_text(
                    root_position_x,
                    root_position_y,
                    NODE_RADIUS,
                    HIGHLIGHT_COLOR,
                    root_node.value,
                    HIGHLIGHT_TEXT_COLOR,
                    FONT_SIZE,
                )
                self.window.update()
                time.sleep(ANIMATION_DELAY)

                self.clear_canvas_and_draw_tree()

                self.create_rectangle_with_text(
                    root_position_x,
                    root_position_y - 1.5 * NODE_RADIUS,
                    6.5 * NODE_RADIUS,
                    NODE_RADIUS / 1.5,
                    HIGHLIGHT_COLOR,
                    "DELETE DUPLICATE >>",
                    HIGHLIGHT_TEXT_COLOR,
                    FONT_SIZE / 1.5,
                )

                self.window.update()
                time.sleep(ANIMATION_DELAY)

                root_node.right_child = self.delete_node(
                    root_node.right_child,
                    root_node.value,
                    right_child_position_x,
                    right_child_position_y,
                    node_depth + 1,
                )
            else:
                self.create_rectangle_with_text(
                    root_position_x,
                    root_position_y - 1.5 * NODE_RADIUS,
                    6.5 * NODE_RADIUS,
                    NODE_RADIUS / 1.5,
                    HIGHLIGHT_COLOR,
                    "<< REPLACE WITH MAX",
                    HIGHLIGHT_TEXT_COLOR,
                    FONT_SIZE / 1.5,
                )

                self.window.update()
                time.sleep(ANIMATION_DELAY)

                (
                    left_child_position_x,
                    left_child_position_y,
                ) = self.calculate_left_child_position(
                    root_position_x, root_position_y, node_depth + 1
                )
                root_node.value = self.get_max_node(
                    root_node.left_child,
                    left_child_position_x,
                    left_child_position_y,
                    node_depth + 1,
                )

                self.create_oval_with_text(
                    root_position_x,
                    root_position_y,
                    NODE_RADIUS,
                    HIGHLIGHT_COLOR,
                    root_node.value,
                    HIGHLIGHT_TEXT_COLOR,
                    FONT_SIZE,
                )
                self.window.update()
                time.sleep(ANIMATION_DELAY)

                self.clear_canvas_and_draw_tree()

                self.create_rectangle_with_text(
                    root_position_x,
                    root_position_y - 1.5 * NODE_RADIUS,
                    6.5 * NODE_RADIUS,
                    NODE_RADIUS / 1.5,
                    HIGHLIGHT_COLOR,
                    "<< DELETE DUPLICATE",
                    HIGHLIGHT_TEXT_COLOR,
                    FONT_SIZE / 1.5,
                )

                self.window.update()
                time.sleep(ANIMATION_DELAY)

                root_node.left_child = self.delete_node(
                    root_node.left_child,
                    root_node.value,
                    left_child_position_x,
                    left_child_position_y,
                    node_depth + 1,
                )
        return root_node

    def delete_node_on_tree(self):
        value = self.input_field.get()
        if not self.is_valid_input(value):
            return
        value = int(value)

        self.input_field.delete(0, END)

        root_position_x = WINDOW_WIDTH / 2
        root_position_y = Y_PADDING

        self.disable_UI()
        self.root_node = self.delete_node(
            self.root_node,
            value,
            root_position_x,
            root_position_y,
            0,
        )

        time.sleep(1)
        self.canvas.delete("all")

        self.draw_tree(self.root_node, root_position_x, root_position_y, 0)

        self.enable_UI()

    def disable_UI(self):
        self.generate_random_tree_btn.config(state=DISABLED)
        self.insert_btn.config(state=DISABLED)
        self.delete_btn.config(state=DISABLED)
        self.search_btn.config(state=DISABLED)
        self.input_field.config(state=DISABLED)

    def enable_UI(self):
        self.generate_random_tree_btn.config(state=NORMAL)
        self.insert_btn.config(state=NORMAL)
        self.delete_btn.config(state=NORMAL)
        self.search_btn.config(state=NORMAL)
        self.input_field.config(state=NORMAL)


if __name__ == "__main__":
    window = Tk()

    window.title("Binary Search Tree Visualizer")
    window.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)
    window.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
    BST(window)
    window.mainloop()
