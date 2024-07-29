import pygame

from folumo.betterGUI.constants import MOUSEMOTION
from folumo.betterGUI.screen import Element, Canvas


class Sprite(Element):
    def __init__(self, xy, image_path):
        super().__init__(xy)
        self.image = pygame.image.load(image_path)

    def render(self) -> Canvas:
        canvas = Canvas(self.image.get_size())
        canvas.surf.blit(self.image, (0, 0))
        return canvas


class AnimatedSprite(Element):
    def __init__(self, xy, image_paths, frame_rate=10):
        super().__init__(xy)
        self.images = [pygame.image.load(path) for path in image_paths]
        self.frame_rate = frame_rate
        self.current_frame = 0
        self.frame_count = 0

    def update(self):
        self.frame_count += 1
        if self.frame_count >= self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.images)
            self.frame_count = 0

    def render(self) -> Canvas:
        self.update()
        canvas = Canvas(self.images[self.current_frame].get_size())
        canvas.surf.blit(self.images[self.current_frame], (0, 0))
        return canvas


class HealthBar(Element):
    def __init__(self, xy, size, max_health, current_health, bar_color, bg_color):
        super().__init__(xy)
        self.size = size
        self.max_health = max_health
        self.current_health = current_health
        self.bar_color = bar_color
        self.bg_color = bg_color

    def set_health(self, health):
        self.current_health = max(0, min(self.max_health, health))

    def render(self) -> Canvas:
        canvas = Canvas(self.size)
        pygame.draw.rect(canvas.surf, self.bg_color, (0, 0, *self.size))
        health_width = int(self.size[0] * (self.current_health / self.max_health))
        pygame.draw.rect(canvas.surf, self.bar_color, (0, 0, health_width, self.size[1]))
        return canvas


class Inventory(Element):
    def __init__(self, xy, size, slot_size, slot_color, bg_color):
        super().__init__(xy)
        self.size = size
        self.slot_size = slot_size
        self.slot_color = slot_color
        self.bg_color = bg_color
        self.items = [[None for _ in range(size[0])] for _ in range(size[1])]

    def add_item(self, item, position):
        x, y = position
        if 0 <= x < self.size[0] and 0 <= y < self.size[1]:
            self.items[y][x] = item

    def render(self) -> Canvas:
        canvas = Canvas((self.size[0] * self.slot_size, self.size[1] * self.slot_size))
        canvas.surf.fill(self.bg_color)
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                pygame.draw.rect(canvas.surf, self.slot_color,
                                 (x * self.slot_size, y * self.slot_size, self.slot_size, self.slot_size), 1)
                item = self.items[y][x]
                if item:
                    item_canvas = item.render()
                    canvas.surf.blit(item_canvas.surf, (x * self.slot_size, y * self.slot_size))
        return canvas


class HUD(Element):
    def __init__(self, xy, elements):
        super().__init__(xy)
        self.elements: list[Element] = elements

    def render(self) -> Canvas:
        canvas = Canvas((1920, 1080))
        for element in self.elements:
            element_canvas = element.render()
            canvas.surf.blit(element_canvas.surf, element.xy)
        return canvas


class DialogueBox(Element):
    def __init__(self, xy, size, text, font_size=24, text_color=(0, 0, 0), bg_color=(255, 255, 255)):
        super().__init__(xy)
        self.size = size
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.text_color = text_color
        self.bg_color = bg_color

    def render(self) -> Canvas:
        canvas = Canvas(self.size)
        canvas.surf.fill(self.bg_color)
        lines = self.text.split('\n')
        y = 0
        for line in lines:
            text_surface = self.font.render(line, True, self.text_color)
            canvas.surf.blit(text_surface, (5, y))
            y += text_surface.get_height() + 5
        return canvas


class Timer(Element):
    def __init__(self, xy, size, font_size=24, text_color=(255, 255, 255), bg_color=(0, 0, 0)):
        super().__init__(xy)
        self.size = size
        self.font = pygame.font.Font(None, font_size)
        self.text_color = text_color
        self.bg_color = bg_color
        self.time_left = 0
        self.running = False

    def start(self, time):
        self.time_left = time
        self.running = True

    def stop(self):
        self.running = False

    def update(self):
        if self.running and self.time_left > 0:
            self.time_left -= 1 / 60  # Assuming 60 FPS
            if self.time_left <= 0:
                self.time_left = 0
                self.running = False

    def render(self) -> Canvas:
        self.update()
        canvas = Canvas(self.size)
        canvas.surf.fill(self.bg_color)
        minutes = int(self.time_left // 60)
        seconds = int(self.time_left % 60)
        time_str = f"{minutes:02}:{seconds:02}"
        text_surface = self.font.render(time_str, True, self.text_color)
        canvas.surf.blit(text_surface, (self.size[0] / 2 - text_surface.get_width() / 2, self.size[1] / 2 - text_surface.get_height() / 2))
        return canvas


class Tooltip(Element):
    def __init__(self, element, text, font_size=24, text_color=(0, 0, 0), bg_color=(255, 255, 255)):
        super().__init__(element.xy)
        self.element = element
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.text_color = text_color
        self.bg_color = bg_color
        self.visible = False

    def is_hovering(self, pos):
        x, y = self.xy
        width, height = self.element.lastRender.surf.get_size()
        return x <= pos[0] <= x + width and y <= pos[1] <= y + height

    def handle_event(self, event):
        if event.type == MOUSEMOTION:
            hovering = self.is_hovering(event.pos)
            self.visible = hovering

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False

    def render(self) -> Canvas:
        if not self.visible:
            return Canvas((0, 0))

        text_surface = self.font.render(self.text, True, self.text_color)
        canvas = Canvas((text_surface.get_width() + 10, text_surface.get_height() + 10), False, self.bg_color)
        canvas.surf.blit(text_surface, (5, 5))
        return canvas


class Slider(Element):
    def __init__(self, xy, size: tuple[int, int], min_value: int, max_value: int, initial_value: int, bar_color: tuple[int, int, int], knob_color: tuple[int, int, int]):
        super().__init__(xy)
        self.size = size
        self.min_value = min_value
        self.max_value = max_value
        self.value = initial_value
        self.bar_color = bar_color
        self.knob_color = knob_color
        self.knob_position = (initial_value - min_value) / (max_value - min_value) * size[0]
        self.dragging = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovering(event.pos):
                self.dragging = True
                self.update_knob(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.update_knob(event.pos)

    def update_knob(self, pos):
        x = pos[0] - self.xy[0]
        x = max(0, min(x, self.size[0]))
        self.knob_position = x
        self.value = self.min_value + (self.max_value - self.min_value) * (x / self.size[0])

    def is_hovering(self, pos):
        x, y = self.xy
        width, height = self.size
        return x <= pos[0] <= x + width and y <= pos[1] <= y + height

    def render(self) -> Canvas:
        canvas = Canvas(self.size)
        pygame.draw.rect(canvas.surf, self.bar_color, (0, self.size[1] // 2 - 5, self.size[0], 10))
        pygame.draw.circle(canvas.surf, self.knob_color, (int(self.knob_position), self.size[1] // 2), 10)
        return canvas
