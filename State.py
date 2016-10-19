from components.Window import Window


class State(object):
    def __init__(self, board):
        self.board = board
        self.windows = {}

    def add_window(self, name, properties):
        if name not in self.windows:
            if "position" in properties:
                position = properties["position"]
            else:
                position = (0, 0)
            if "size" in properties:
                size = properties["size"]
            else:
                size = (100, 100)
            if "name" in properties:
                name = properties["name"]
            else:
                name = "default"
            if "border_color" in properties:
                border_color = properties["border_color"]
            else:
                border_color = None
            self.windows[name] = Window(position=position, size=size, name=name, border_color=border_color)

    def draw_windows(self, screen):
        for name, window in self.windows.iteritems():
            window.draw(screen)

    def update_windows(self, key, mouse):
        for name, window in self.windows.iteritems():
            window.update(key, mouse)

    def draw(self, screen):
        self.draw_windows(screen)

    def update(self, key, mouse):
        self.update_windows(key, mouse)
