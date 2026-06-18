import tkinter as tk




class Node:
    def create(value):
        node = Node()
        node.value = value
        node.left = None
        node.right = None
        node.height = 1
        node.expanded = False
        return node

class AVLTree:
    def height(n):
        return n.height if n else 0

    def update_height(n):
        n.height = max(AVLTree.height(n.left), AVLTree.height(n.right)) + 1

    def balance_factor(n):
        return AVLTree.height(n.left) - AVLTree.height(n.right)



    def rotate_right(y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        AVLTree.update_height(y)
        AVLTree.update_height(x)
        return x

    def rotate_left(x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        AVLTree.update_height(x)
        AVLTree.update_height(y)
        return y


    def insert(node, value):
        if not node:
            return Node.create(value)

        if value < node.value:
            node.left = AVLTree.insert(node.left, value)
        else:
            node.right = AVLTree.insert(node.right, value)

        AVLTree.update_height(node)
        balance = AVLTree.balance_factor(node)

        if balance > 1 and value < node.left.value:
            return AVLTree.rotate_right(node)
        if balance < -1 and value > node.right.value:
            return AVLTree.rotate_left(node)
        if balance > 1 and value > node.left.value:
            node.left = AVLTree.rotate_left(node.left)
            return AVLTree.rotate_right(node)
        if balance < -1 and value < node.right.value:
            node.right = AVLTree.rotate_right(node.right)
            return AVLTree.rotate_left(node)

        return node

    def get_min(node):
        while node.left:
            node = node.left
        return node

    def delete(node, value):
        if not node:
            return node

        if value < node.value:
            node.left = AVLTree.delete(node.left, value)
        elif value > node.value:
            node.right = AVLTree.delete(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = AVLTree.get_min(node.right)
            node.value = temp.value
            node.right = AVLTree.delete(node.right, temp.value)

        AVLTree.update_height(node)
        balance = AVLTree.balance_factor(node)

        if balance > 1 and AVLTree.balance_factor(node.left) >= 0:
            return AVLTree.rotate_right(node)
        if balance > 1 and AVLTree.balance_factor(node.left) < 0:
            node.left = AVLTree.rotate_left(node.left)
            return AVLTree.rotate_right(node)
        if balance < -1 and AVLTree.balance_factor(node.right) <= 0:
            return AVLTree.rotate_left(node)
        if balance < -1 and AVLTree.balance_factor(node.right) > 0:
            node.right = AVLTree.rotate_right(node.right)
            return AVLTree.rotate_left(node)

        return node

class SplayTree:

    def rotate_right(x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def rotate_left(x):
        y = x.right
        x.right = y.left
        y.left = x
        return y
    def splay(root, value):
        if not root or root.value == value:
            return root
        if value < root.value:
            if not root.left:
                return root
            if value < root.left.value:
                root.left.left = SplayTree.splay(root.left.left, value)
                root = SplayTree.rotate_right(root)
            elif value > root.left.value:
                root.left.right = SplayTree.splay(root.left.right, value)
                if root.left.right:
                    root.left = SplayTree.rotate_left(root.left)
            return root if not root.left else SplayTree.rotate_right(root)
        else:
            if not root.right:
                return root
            if value > root.right.value:
                root.right.right = SplayTree.splay(root.right.right, value)
                root = SplayTree.rotate_left(root)
            elif value < root.right.value:
                root.right.left = SplayTree.splay(root.right.left, value)
                if root.right.left:
                    root.right = SplayTree.rotate_right(root.right)
            return root if not root.right else SplayTree.rotate_left(root)
    def insert(root, value):
        if not root:
            return Node.create(value)
        root = SplayTree.splay(root, value)
        if root.value == value:
            return root
        new_node = Node.create(value)
        if value < root.value:
            new_node.right = root
            new_node.left = root.left
            root.left = None
        else:
            new_node.left = root
            new_node.right = root.right
            root.right = None
        return new_node


    def delete(root, value):
        if not root:
            return None
        root = SplayTree.splay(root, value)
        if root.value != value:
            return root
        if not root.left:
            return root.right
        new_root = SplayTree.splay(root.left, value)
        new_root.right = root.right
        return new_root
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

        app.mode = "AVL"
        btn_frame = tk.Frame(app.left_frame)
        btn_frame.pack(pady=10)

        def set_avl():
            app.mode = "AVL"

        def set_splay():
            app.mode = "SPLAY"

        tk.Button(btn_frame, text="AVL", command=set_avl).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Splay", command=set_splay).pack(side="left", padx=5)

        tk.Label(app.left_frame, text="ИНСТРУКЦИЯ", font=("Arial", 10, "bold")).pack(pady=(0, 5))
        instructions = (
            "• Введите число и нажмите Enter\n"
            "  чтобы добавить узел.\n"
            "• Введите число в поле удаления\n"
            "  и нажмите Enter.\n"
            "• Стрелки на клавиатуре —\n"
            "  перемещение дерева.\n"
            "• Зажмите ЛКМ и тяните мышь,\n"
            "  чтобы сдвигать холст.\n"
            "• Ползунок меняет масштаб.\n"
            "• Клик по узлу —\n"
            "  свернуть / развернуть."
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
            if self.mode == "AVL":
                self.root = AVLTree.insert(self.root, val)
            else:
                self.root = SplayTree.insert(self.root, val)
            self.entry.delete(0, tk.END)
            self.draw()
        except ValueError:
            pass

    def delete_value(self, event=None):
        try:
            val = float(self.delete_entry.get())
            if self.mode == "AVL":
                self.root = AVLTree.delete(self.root, val)
            else:
                self.root = SplayTree.delete(self.root, val)
            self.delete_entry.delete(0, tk.END)
            self.draw()
        except ValueError:
            pass

    def subtree_width(self, node):
        if not node:
            return 0
        return max(1, self.subtree_width(node.left) + self.subtree_width(node.right))

    def format_value(self, node):
        s_val = str(node.value)
        return s_val if (node.expanded or len(s_val) <= 4) else s_val[:2] + ".."

    def draw(self):
        self.canvas.delete("all")
        self.nodes_coords = []

        if self.root:
            w = self.subtree_width(self.root)
            self.draw_node(self.root, 400, 50, w * 50)

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