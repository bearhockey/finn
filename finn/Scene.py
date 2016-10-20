class Scene(object):
    def __init__(self, name=None):
        self.name = name
        # components will be updated and drawn; sprites only drawn
        self.components = []
        self.sprites = []

    def always(self):
        elements = self.components + self.sprites
        for element in elements:
            always = getattr(element, "always", None)
            if callable(always):
                element.always()

    def update_components(self, key, mouse, offset=(0, 0)):
        active_component = None
        for component in self.components:
            update = getattr(component, "update", None)
            if callable(update):
                if component.update(key=key, mouse=mouse, offset=offset):
                    active_component = component
        if active_component:
            return active_component

    def update(self, key, mouse, offset=(0, 0)):
        self.update_components(key, mouse, offset)

    def draw(self, screen):
        for component in self.components:
            component.draw(screen)
        for sprite in self.sprites:
            sprite.draw(screen)

