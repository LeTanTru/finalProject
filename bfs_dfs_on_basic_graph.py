# Graph Traversing #
from tkinter import *
import time


class GraphTraversal:
    def __init__(self, root):
        self.window = root
        self.make_canvas = Canvas(
            self.window, bg="deepskyblue", relief=RAISED, bd=7, width=500, height=500
        )
        self.make_canvas.pack()

        # status label initialization
        self.status = None

        # some list initialization bt default
        self.vertex_store = []
        self.total_circle = []
        self.queue_bfs = []
        self.stack_dfs = []
        self.input_entry = None
        # some default function call
        self.basic_set_up()
        self.create_vertex()
        # self.create_traversing_result()

    def basic_set_up(self):
        heading = Label(
            self.make_canvas,
            text="Graph Traversing Visualization",
            bg="deepskyblue",
            fg="firebrick1",
            font=("Arial", 20, "bold", "italic"),
        )
        heading.place(x=50, y=10)

        bfs_btn = Button(
            self.window,
            text="BFS",
            font=("Arial", 15, "bold"),
            bg="black",
            fg="green",
            relief=RAISED,
            bd=8,
            command=self.bfs_traversing,
        )
        bfs_btn.place(x=20, y=530)

        dfs_btn = Button(
            self.window,
            text="DFS",
            font=("Arial", 15, "bold"),
            bg="black",
            fg="green",
            relief=RAISED,
            bd=8,
            command=self.dfs_traversing,
        )
        dfs_btn.place(x=400, y=530)

        self.status = Label(
            self.make_canvas,
            text="Not Visited",
            bg="deepskyblue",
            fg="firebrick1",
            font=("Arial", 20, "bold", "italic"),
        )
        self.status.place(x=50, y=450)

    def create_vertex(self):  # vertex with connection make
        for i in range(16):
            self.total_circle.append(i)

        i = 0  # node 0
        self.total_circle[i] = self.make_canvas.create_oval(240, 60, 270, 90, width=3)
        self.value = self.make_canvas.create_text(
            240 + 15, 60 + 15, text=str(i), font=("Arial", 12, "bold"), fill="white"
        )

        i += 1  # node 1
        self.total_circle[i] = self.make_canvas.create_oval(170, 130, 200, 160, width=3)
        self.value = self.make_canvas.create_text(
            170 + 15, 130 + 15, text=str(i), font=("Arial", 12, "bold"), fill="white"
        )

        i += 1  # node 2
        self.total_circle[i] = self.make_canvas.create_oval(310, 130, 340, 160, width=3)
        self.value = self.make_canvas.create_text(
            310 + 15, 130 + 15, text=str(i), font=("Arial", 12, "bold"), fill="white"
        )

        i += 1  # node 3
        self.total_circle[i] = self.make_canvas.create_oval(270, 200, 300, 230, width=3)
        self.value = self.make_canvas.create_text(
            270 + 15, 200 + 15, text=str(i), font=("Arial", 12, "bold"), fill="white"
        )

        i += 1  # node 4
        self.total_circle[i] = self.make_canvas.create_oval(370, 200, 400, 230, width=3)
        self.value = self.make_canvas.create_text(
            370 + 15, 200 + 15, text=str(i), font=("Arial", 12, "bold"), fill="white"
        )

        i += 1  # node 5
        self.total_circle[i] = self.make_canvas.create_oval(100, 200, 130, 230, width=3)
        self.value = self.make_canvas.create_text(
            100 + 15, 200 + 15, text=str(i), font=("Arial", 12, "bold"), fill="white"
        )

        i += 1  # node 6
        self.total_circle[i] = self.make_canvas.create_oval(230, 200, 260, 230, width=3)
        self.value = self.make_canvas.create_text(
            230 + 15, 200 + 15, text=str(i), font=("Arial", 12, "bold"), fill="white"
        )

        i += 1  # node 7
        self.total_circle[i] = self.make_canvas.create_oval(40, 300, 70, 330, width=3)
        self.value = self.make_canvas.create_text(
            40 + 15, 300 + 15, text=str(i), font=("Arial", 12, "bold"), fill="white"
        )

        i += 1  # node 8
        self.total_circle[i] = self.make_canvas.create_oval(90, 380, 120, 410, width=3)
        self.value = self.make_canvas.create_text(
            90 + 15, 380 + 15, text=str(i), font=("Arial", 12, "bold"), fill="white"
        )

        i += 1  # node 9
        self.total_circle[i] = self.make_canvas.create_oval(220, 300, 250, 330, width=3)
        self.value = self.make_canvas.create_text(
            220 + 15, 300 + 15, text=str(i), font=("Arial", 12, "bold"), fill="white"
        )

        i += 1  # node 10
        self.total_circle[i] = self.make_canvas.create_oval(150, 300, 180, 330, width=3)
        self.value = self.make_canvas.create_text(
            150 + 15, 300 + 15, text="10", font=("Arial", 12, "bold"), fill="white"
        )

        i += 1  # node 11
        self.total_circle[i] = self.make_canvas.create_oval(200, 380, 230, 410, width=3)
        self.value = self.make_canvas.create_text(
            200 + 15, 380 + 15, text=str(i), font=("Arial", 12, "bold"), fill="white"
        )

        i += 1  # node 12
        self.total_circle[i] = self.make_canvas.create_oval(330, 300, 360, 330, width=3)
        self.value = self.make_canvas.create_text(
            330 + 15, 300 + 15, text=str(i), font=("Arial", 12, "bold"), fill="white"
        )

        i += 1  # node 13
        self.total_circle[i] = self.make_canvas.create_oval(420, 300, 450, 330, width=3)
        self.value = self.make_canvas.create_text(
            420 + 15, 300 + 15, text=str(i), font=("Arial", 12, "bold"), fill="white"
        )

        i += 1  # node 14
        self.total_circle[i] = self.make_canvas.create_oval(380, 380, 410, 410, width=3)
        self.value = self.make_canvas.create_text(
            380 + 15, 380 + 15, text=str(i), font=("Arial", 12, "bold"), fill="white"
        )

        i += 1  # node 15
        self.total_circle[i] = self.make_canvas.create_oval(270, 380, 300, 410, width=3)
        self.value = self.make_canvas.create_text(
            270 + 15, 380 + 15, text=str(i), font=("Arial", 12, "bold"), fill="white"
        )

        self.create_connector_left(0, 1)
        self.create_connector_right(0, 2)
        self.collector_connector(0, 1, 2)

        self.create_connector_left(1, 5)
        self.create_connector_right(1, 6)
        self.collector_connector(1, 5, 6)

        self.create_connector_left(2, 3)
        self.create_connector_right(2, 4)
        self.collector_connector(2, 3, 4)

        self.create_connector_left(3, 9)
        self.create_connector_right(3, 12)
        self.collector_connector(3, 9, 12)

        self.create_connector_right(4, 13)
        self.collector_connector(4, None, 13)

        self.create_connector_left(5, 7)
        self.collector_connector(5, 7, None)

        self.create_connector_left(6, 10)
        self.collector_connector(6, 10, None)

        self.create_connector_right(7, 8)
        self.collector_connector(7, None, 8)

        self.create_connector_right(10, 11)
        self.collector_connector(10, None, 11)

        self.create_connector_left(12, 15)
        self.collector_connector(12, 15, None)

        self.create_connector_left(13, 14)
        self.collector_connector(13, 14, None)

        print(self.vertex_store)

    def create_connector_left(self, index1, index2):  # left node connection make
        first_coord = self.make_canvas.coords(
            self.total_circle[index1]
        )  # Source node coordinates
        second_coord = self.make_canvas.coords(
            self.total_circle[index2]
        )  # Destination node coordinates
        # Connector line start_x
        line_start_x = (first_coord[0] + first_coord[2]) / 2
        line_end_x = (second_coord[0] + second_coord[2]) / 2  # Connector line end_x
        # Connector line start_y
        line_start_y = (first_coord[1] + first_coord[3]) / 2
        line_end_y = (second_coord[1] + second_coord[3]) / 2  # Connector line end_y
        self.make_canvas.create_line(
            line_start_x - 10,
            line_start_y + 10,
            line_end_x + 10,
            line_end_y - 10,
            width=3,
        )

    def create_connector_right(self, index1, index2):  # right node connection make
        first_coord = self.make_canvas.coords(
            self.total_circle[index1]
        )  # Source node coordinates
        second_coord = self.make_canvas.coords(
            self.total_circle[index2]
        )  # Destination node coordinates
        # Connector line start_x
        line_start_x = (first_coord[0] + first_coord[2]) / 2
        # Connector line end_x
        line_end_x = (second_coord[0] + second_coord[2]) / 2
        # Connector line start_y
        line_start_y = (first_coord[1] + first_coord[3]) / 2
        # Connector line end_y
        line_end_y = (second_coord[1] + second_coord[3]) / 2
        self.make_canvas.create_line(
            line_start_x + 10,
            line_start_y + 10,
            line_end_x - 10,
            line_end_y - 10,
            width=3,
        )

    # all about node data collect and store
    def collector_connector(self, source, connector1, connector2):
        temp = []
        if connector1:
            temp.append(connector1)

        if connector2:
            temp.append(connector2)

        self.vertex_store.append([source, temp])

    def bfs_traversing(self):
        try:
            self.status["text"] = "Red: Visited"
            graph = self.vertex_store
            visited = set()
            self.queue_bfs = [0]  # Start from vertex 0
            result = []

            while self.queue_bfs:
                current_vertex = self.queue_bfs.pop(0)
                result.append(current_vertex)
                print(current_vertex, end=" ")
                self.make_canvas.itemconfig(
                    self.total_circle[current_vertex], fill="red"
                )
                self.window.update()
                time.sleep(0.3)

                for vertex, neighbors in graph:
                    if vertex == current_vertex:
                        for neighbor in neighbors:
                            if neighbor not in visited:
                                visited.add(neighbor)
                                self.queue_bfs.append(neighbor)

            self.status["text"] = "All nodes visited"
            # print(result)
            print()
        except:
            pass

    def dfs_traversing(self):
        try:
            self.status["text"] = "Blue: Visited"
            start_node = 0
            self.stack_dfs = [start_node]
            visited = set()
            graph = self.vertex_store

            while self.stack_dfs:
                current_node = self.stack_dfs.pop()
                self.make_canvas.itemconfig(
                    self.total_circle[current_node], fill="dodgerblue1"
                )
                self.window.update()
                time.sleep(0.3)
                if current_node not in visited:
                    print(current_node, end=" ")
                    visited.add(current_node)

                # Push unvisited neighbors onto the self.stack_dfs in reverse order
                for neighbor in reversed(graph):
                    if neighbor[0] == current_node:
                        for n in reversed(neighbor[1]):
                            if n not in visited:
                                self.stack_dfs.append(n)
            self.status["text"] = "All nodes visited"
            print()
        except:
            pass


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


if __name__ == "__main__":
    window = Tk()
    window.title("Graph Traversal Visualizer")
    center_window(window, 500, 600)
    window.maxsize(500, 600)
    window.minsize(500, 600)
    GraphTraversal(window)
    window.mainloop()
