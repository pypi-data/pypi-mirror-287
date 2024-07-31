import pygame  # type: ignore

class Pygame:
    def __init__(self, WIDTH: int, HEIGHT: int, color: tuple):
        pygame.init()
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.color = color
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Application")
        self.objects = {}
        self.objcolor = {}
        self.images = {}
        self.image_pos = {}
        self.text = None
        self.file_operations = self.FileOperations()

    def screen(self):
        self.WIN.fill(self.color)
        for item in self.objects:
            pygame.draw.rect(self.WIN, self.objcolor[item + ' color'], self.objects[item])
        for item in self.images:
            self.WIN.blit(self.images[item], self.image_pos[item + ' pos'])
        if self.text:
            self.WIN.blit(self.text[0], self.text[1])
        pygame.display.update()

    def create_object(self, name: str, x: int, y: int, width: int, height: int, color: tuple):
        self.objects[name] = pygame.Rect(x, y, width, height)
        self.objcolor[name + ' color'] = color

    def key_move(self, name: str, speed: int):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.objects[name].x -= speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.objects[name].x += speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.objects[name].y -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.objects[name].y += speed

    def move(self, name: str, x: int, y: int):
        self.objects[name].x = x
        self.objects[name].y = y

    def create_image(self, name: str, image_file: str, x: int, y: int):
        self.images[name] = pygame.image.load(image_file)
        self.image_pos[name + ' pos'] = (x, y)

    def collide(self, object1: str, object2: str) -> bool:
        return pygame.Rect.colliderect(self.objects[object1], self.objects[object2])

    def position(self, object: str) -> tuple:
        return self.objects[object].x, self.objects[object].y

    def mouse_X(self) -> int:
        return pygame.mouse.get_pos()[0]

    def mouse_Y(self) -> int:
        return pygame.mouse.get_pos()[1]

    def mouse_pos(self) -> tuple:
        return pygame.mouse.get_pos()

    def image_position(self, name: str) -> tuple:
        return self.image_pos[name + ' pos']

    def click(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
        return False

    def remove_object(self, name: str):
        del self.objects[name]
        del self.objcolor[name + ' color']

    def clear_screen(self, key: str):
        if key == "YES":
            self.objects = {}
            self.objcolor = {}
            self.text = None

    def render_text(self, text: str, x: int, y: int, color: tuple):
        font_size = 30
        pygame.font.init()
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, color)
        self.text = [text_surface, (x, y)]

    def pressed_keys(self):
        return pygame.key.get_pressed()

    class FileOperations:
        def read(self, file_name: str) -> list:
            try:
                with open(file_name, 'r') as file:
                    return [line.strip() for line in file.readlines()]
            except FileNotFoundError:
                print(f"File {file_name} not found.")
                return []

        def write(self, file_name: str, text: str):
            with open(file_name, 'w') as file:
                file.write(text)

        def append(self, file_name: str, text: str):
            with open(file_name, 'a') as file:
                file.write(text)