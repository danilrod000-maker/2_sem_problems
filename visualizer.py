# visualizer.py
import tkinter as tk
from tkinter import messagebox
from models import AVLTree


class AVLVisualizer:
    def create():
        app = AVLVisualizer()
        app.root = None
        app.window = tk.Tk()
        app.window.title("AVL Tree Visualizer")

        app.zoom = 1.0
        app.move_x = 0
        app.move_y = 0
        app.nodes_coords = []
        app.last_x = 0
        app.last_y = 0

        app.left_frame = tk.Frame(app.window, padx=15, pady=1, relief="ridge", borderwidth=5)
        app.left_frame.pack(side="left", fill="y")

        tk.Label(app.left_frame, text="ИНСТРУКЦИЯ", font=("Arial", 10, "bold")).pack(pady=(0, 5))
        instructions = (
            "• Введите число и нажмите Enter\n"
            "  чтобы добавить узел.\n"
            "• Введите число в поле удаления\n"
            "  и нажмите Enter.\n"
            "• Стрелки на клавиатуре —\n"
            "  перемещение дерева  \n"
            "• Зажмите ЛКМ и тяните мышь,\n"
            "  чтобы сдвигать холст \n"
            "• Ползунок меняет масштаб.\n"
            "• Клик по узлу —\n"
            "  свернуть/ развернуть."
        )
        tk.Label(app.left_frame, text=instructions, justify="left", fg="#333").pack(pady=(0, 15))

        tk.Label(app.left_frame, text="Добавить значение:").pack()
        app.entry = tk.Entry(app.left_frame)
        app.entry.pack(pady=(0, 10))
        app.entry.bind("<Return>", app.add_value)

        tk.Label(app.left_frame, text="Удалить значение:").pack()
        app.delete_entry = tk.Entry(app.left_frame)
        app.delete_entry.pack(pady=(0, 10))
        app.delete_entry.bind("<Return>", app.delete_value)

        tk.Button(
            app.left_frame,
            text="🗑 Очистить всё",
            command=app.clear_all,
            bg="#ff6b6b",
            fg="white",
            font=("Arial", 10, "bold")
        ).pack(pady=(5, 10))

        tk.Label(app.left_frame, text="Масштаб:").pack()
        app.scale = tk.Scale(
            app.left_frame,
            from_=0.2,
            to=3.0,
            resolution=0.1,
            orient="horizontal",
            command=app.on_scale
        )
        app.scale.set(1.0)
        app.scale.pack(pady=(0, 10))

        app.right_frame = tk.Frame(app.window)
        app.right_frame.pack(side="right", fill="both", expand=True)

        app.canvas = tk.Canvas(app.right_frame, bg="white", width=800, height=600)
        app.canvas.pack(fill="both", expand=True)

        app.canvas.bind("<Button-1>", app.handle_click)
        app.canvas.bind("<B1-Motion>", app.drag)

        app.window.bind("<Left>", lambda e: app.move(-50, 0))
        app.window.bind("<Right>", lambda e: app.move(50, 0))
        app.window.bind("<Up>", lambda e: app.move(0, -50))
        app.window.bind("<Down>", lambda e: app.move(0, 50))

        app.draw()
        return app

    def clear_all(self):
        self.root = None
        self.move_x = 0
        self.move_y = 0
        self.zoom = 1.0
        self.scale.set(1.0)
        self.nodes_coords = []
        self.draw()

    def handle_click(self, event):
        clicked_node = None
        for node, nx, ny, r in self.nodes_coords:
            if (event.x - nx) ** 2 + (event.y - ny) ** 2 <= r ** 2:
                clicked_node = node
                break

        if clicked_node:
            clicked_node.expanded = not clicked_node.expanded
            self.draw()
        else:
            self.start_drag(event)

    def move(self, dx, dy):
        self.move_x += dx
        self.move_y += dy
        self.draw()

    def start_drag(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def drag(self, event):
        dx = event.x - self.last_x
        dy = event.y - self.last_y
        self.move_x += dx
        self.move_y += dy
        self.last_x = event.x
        self.last_y = event.y
        self.draw()

    def on_scale(self, val):
        self.zoom = float(val)
        self.draw()

    def add_value(self, event=None):
        try:
            val = float(self.entry.get())
            self.root = AVLTree.insert(self.root, val)
            self.entry.delete(0, tk.END)
            self.draw()
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите число!")
            self.entry.delete(0, tk.END)

    def delete_value(self, event=None):
        try:
            val = float(self.delete_entry.get())
            self.root = AVLTree.delete(self.root, val)
            self.delete_entry.delete(0, tk.END)
            self.draw()
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите число!")
            self.delete_entry.delete(0, tk.END)

    def subtree_width(self, node):
        if not node:
            return 0
        return max(1, self.subtree_width(node.left) + self.subtree_width(node.right))

    def format_value(self, node):
        s_val = str(node.value)

        text_is_short = len(s_val) <= 4
        node_is_expanded = node.expanded

        if node_is_expanded or text_is_short:
            return s_val
        else:
            first_two_chars = s_val[:3]
            return first_two_chars + ".."

    def draw(self):
        self.canvas.delete("all")
        self.nodes_coords = []

        if self.root:
            w = self.subtree_width(self.root)
            self.draw_node(self.root, 400, 50, w * 100)

    def draw_node(self, node, x, y, width):
        if not node:
            return

        curr_x = x * self.zoom + self.move_x
        curr_y = y * self.zoom + self.move_y
        display_text = self.format_value(node)
        r = int((15 + len(display_text) * 2) * self.zoom)

        self.nodes_coords.append((node, curr_x, curr_y, r))

        dx = width / 2
        dy = 80

        if node.left:
            cx = (x - dx) * self.zoom + self.move_x
            cy = (y + dy) * self.zoom + self.move_y
            self.canvas.create_line(curr_x, curr_y, cx, cy, fill="gray")
            self.draw_node(node.left, x - dx, y + dy, dx)

        if node.right:
            cx = (x + dx) * self.zoom + self.move_x
            cy = (y + dy) * self.zoom + self.move_y
            self.canvas.create_line(curr_x, curr_y, cx, cy, fill="gray")
            self.draw_node(node.right, x + dx, y + dy, dx)

        color = "lightgreen" if node.expanded else "lightblue"
        self.canvas.create_oval(curr_x - r, curr_y - r, curr_x + r, curr_y + r, fill=color)
        self.canvas.create_text(curr_x, curr_y, text=display_text, font=("Arial", max(8, int(10 * self.zoom))))


app = AVLVisualizer.create()
app.window.mainloop()