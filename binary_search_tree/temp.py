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

        self.traversing_result = []
        self.index = 0
        self.create_some_buttons()
        self.create_traversing_result()
        self.center_window(WINDOW_WIDTH, WINDOW_HEIGHT)

    # center window
    def center_window(self, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 4
        self.window.geometry(f"{width}x{height}+{x}+{y}")

    def create_some_buttons(self):
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
            # command=self.insert_node_to_tree,
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
            # command=self.search_node_on_tree,
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
            # command=self.delete_node_on_tree,
        )
        self.delete_btn.pack(side=LEFT, fill=X, expand=1)

        self.input_field = Entry(
            self.window,
            font=("Arial 15"),
            bd=4,
            relief=GROOVE,
        )
        self.input_field.pack(side=LEFT, fill=X, expand=1)
        self.input_field.focus()

        self.pre_order = HoverButton(
            self.window,
            text="Pre Order",
            font=("Arial 15"),
            cursor="hand2",
            bd=4,
            relief=GROOVE,
            command=self.print_tree_pre_order_traversal,
        )
        self.pre_order.place(x=680, y=700)

        self.in_order = HoverButton(
            self.window,
            text="In Order",
            font=("Arial 15"),
            cursor="hand2",
            bd=4,
            relief=GROOVE,
            command=self.print_tree_in_order_traversal,
        )
        self.in_order.place(x=805, y=700)

        self.post_order = HoverButton(
            self.window,
            text="Post Order",
            font=("Arial 15"),
            cursor="hand2",
            bd=4,
            relief=GROOVE,
            command=self.print_tree_post_order_traversal,
        )
        self.post_order.place(x=910, y=700)

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

    def print_tree_pre_order_traversal(self):
        root_position_x = WINDOW_WIDTH / 2
        root_position_y = Y_PADDING
        if self.index != 0:
            self.draw_tree(self.root_node, root_position_x, root_position_y, 0)
        self.index = 0
        self.clear_traversing_result()
        self.print_tree_pre_order(self.root_node, root_position_x, root_position_y, 0)

    def print_tree_pre_order(
        self, root_node, root_position_x, root_position_y, node_depth
    ):
        if root_node is None:
            return

        self.create_oval_with_text(
            root_position_x,
            root_position_y,
            NODE_RADIUS,
            "red",
            root_node.value,
            TEXT_COLOR,
            FONT_SIZE,
        )

        self.traversing_result[self.index].config(text=str(root_node.value))
        self.index += 1

        time.sleep(ANIMATION_DELAY)
        self.window.update()

        if root_node.left_child is not None:
            (
                left_child_position_x,
                left_child_position_y,
            ) = self.calculate_left_child_position(
                root_position_x, root_position_y, node_depth + 1
            )

            self.print_tree_pre_order(
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
            self.print_tree_pre_order(
                root_node.right_child,
                right_child_position_x,
                right_child_position_y,
                node_depth + 1,
            )

    def print_tree_in_order_traversal(self):
        root_position_x = WINDOW_WIDTH / 2
        root_position_y = Y_PADDING
        if self.index != 0:
            self.draw_tree(self.root_node, root_position_x, root_position_y, 0)
        self.index = 0
        self.clear_traversing_result()
        self.print_tree_in_order(self.root_node, root_position_x, root_position_y, 0)

    def print_tree_in_order(
        self, root_node, root_position_x, root_position_y, node_depth
    ):
        if root_node is None:
            return

        if root_node.left_child is not None:
            (
                left_child_position_x,
                left_child_position_y,
            ) = self.calculate_left_child_position(
                root_position_x, root_position_y, node_depth + 1
            )

            self.print_tree_in_order(
                root_node.left_child,
                left_child_position_x,
                left_child_position_y,
                node_depth + 1,
            )

        self.create_oval_with_text(
            root_position_x,
            root_position_y,
            NODE_RADIUS,
            "red",
            root_node.value,
            TEXT_COLOR,
            FONT_SIZE,
        )

        self.traversing_result[self.index].config(text=str(root_node.value))
        self.index += 1

        time.sleep(ANIMATION_DELAY)
        self.window.update()

        if root_node.right_child is not None:
            (
                right_child_position_x,
                right_child_position_y,
            ) = self.calculate_right_child_position(
                root_position_x, root_position_y, node_depth + 1
            )
            self.print_tree_in_order(
                root_node.right_child,
                right_child_position_x,
                right_child_position_y,
                node_depth + 1,
            )

    def print_tree_post_order_traversal(self):
        root_position_x = WINDOW_WIDTH / 2
        root_position_y = Y_PADDING
        if self.index != 0:
            self.draw_tree(self.root_node, root_position_x, root_position_y, 0)
        self.index = 0
        self.clear_traversing_result()
        self.print_tree_post_order(self.root_node, root_position_x, root_position_y, 0)

    def print_tree_post_order(
        self, root_node, root_position_x, root_position_y, node_depth
    ):
        if root_node is None:
            return

        if root_node.left_child is not None:
            (
                left_child_position_x,
                left_child_position_y,
            ) = self.calculate_left_child_position(
                root_position_x, root_position_y, node_depth + 1
            )

            self.print_tree_post_order(
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
            self.print_tree_post_order(
                root_node.right_child,
                right_child_position_x,
                right_child_position_y,
                node_depth + 1,
            )

        self.create_oval_with_text(
            root_position_x,
            root_position_y,
            NODE_RADIUS,
            "red",
            root_node.value,
            TEXT_COLOR,
            FONT_SIZE,
        )

        self.traversing_result[self.index].config(text=str(root_node.value))
        self.index += 1

        time.sleep(ANIMATION_DELAY)
        self.window.update()

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

    def create_traversing_result(self):
        number_of_nodes = 29
        for i in range(number_of_nodes):
            self.traversing_result.append(i)
        start = 10
        space = 40
        end_line = 610
        for i in range(number_of_nodes):
            self.traversing_result[i] = Label(
                self.window,
                bg="lightblue",
                fg="red",
                font=("Arial", 12, "bold"),
                bd=2,
                width=3,
                relief=SUNKEN,
            )
            self.traversing_result[i].place(x=start, y=end_line)
            start += space
            if start > 1150:
                start = 10
                end_line += 30

    def clear_traversing_result(self):
        for i in range(len(self.traversing_result)):
            self.traversing_result[i].config(text="")


if __name__ == "__main__":
    window = Tk()

    window.title("Binary Search Tree Visualizer")
    window.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)
    window.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
    BST(window)
    window.mainloop()
