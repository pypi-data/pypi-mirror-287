import pygame  # type: ignore
import pyautogui  # type: ignore
import random
import os
import math
import time
from moviepy.editor import ImageSequenceClip  # type: ignore

class GameWindow:
    def __init__(self, WIDTH: int, HEIGHT: int, color: tuple):
        pygame.init()
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.color = color
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Application")
        self.objects = {}
        self.objcolor = {}
        self.text = None

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


    def clear_objects(self, key: str):
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

class CellOut:
    def __init__(self, width: int, height: int, size: int, starting_pop: int, colors=None, fps=10):
        self.width = width
        self.height = height
        self.size = size
        self.colors = colors if colors else ['red', 'green']
        self.pop = starting_pop
        self.cells = []
        self.win = GameWindow(width, height, (0, 0, 0))
        self.death_conditions = False
        self.paused = False
        self.shots = 0
        self.fps = fps

    def init(self, rules=None, spawning_rules=False, death_conditions=False):
        self.init_rules(rules)
        self.init_cells()
        self.init_spawning(spawning_rules)
        self.init_text()
        self.init_death(death_conditions)

    def init_death(self, death_conditions):
        self.death_conditions = death_conditions

    def init_text(self):
        self.win.render_text(f'Population: {self.pop}', 10, 10, (255, 255, 255))

    def init_rules(self, rules):
        if rules is None:
            self.rules = [[('red', 'green'), 5, 200], [('green', 'red'), -3, 200]]
        else:
            self.rules = rules

    def init_spawning(self, spawning):
        if spawning is not False:
            self.sp = spawning

    def init_cells(self):
        for _ in range(self.pop):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            self.cells.append([random.choice(self.colors), (x, y)])
        print(self.cells)

    def run(self, exit):
        """
        exit = [population, shots, videoLength]
        else: exit = False
        """
        clock = pygame.time.Clock()
        while True:
            self.gather_screen()
            if not self.paused:
                self.exit_check(exit)
                self.execute()
                self.spawning()
                self.capture_screenshots(self.shots)
                self.shots += 1
            clock.tick(60)

    def exit_check(self, exit):
        if exit is not False:
            shots = exit[1]
            vid = exit[2]
            pop = exit[0]
            
            # Check if the number of shots is reached
            if shots is not None:  
                if self.shots >= shots:
                    pygame.quit()
                    self.create_video_from_screenshots('cellFolder', self.shots, 'output_video.mp4', self.fps)
                    quit()
            
            # Check if the video length is reached
            elif vid is not None:
                if self.shots // self.fps >= vid:
                    pygame.quit()
                    self.create_video_from_screenshots('cellFolder', self.shots, 'output_video.mp4', self.fps)
                    quit()
            
            # Check if the population condition is met
            elif pop is not None:
                if len(self.cells) >= pop:
                    pygame.quit()
                    self.create_video_from_screenshots('cellFolder', self.shots, 'output_video.mp4', self.fps)
                    quit()


    def capture_screenshots(self, number):
        screenshot = pyautogui.screenshot()
        screenshot.save(f'cellFolder/screenshot_{number}.png')

    def create_video_from_screenshots(self, image_folder, num_screenshots, output_file='output_video.mp4', fps=10):
        # Generate image filenames with zero-padding and start from 1
        image_files = [f'{image_folder}/screenshot_{i}.png' for i in range(0, num_screenshots)]

        # Create video clip from the sequence of images
        clip = ImageSequenceClip(image_files, fps=fps)
        clip.write_videofile(output_file)

        # Remove screenshots after creating the video
        print('Removing screenshots...')
        for image_file in image_files:
            if os.path.exists(image_file):  # Check if file exists before trying to remove
                os.remove(image_file)

        print('Done')

    def apply_death(self):
        Holder = []
        value = self.death_conditions[0]
        for cell in self.cells:
            if random.randint(0, value[0]) != value[1]:
                Holder.append(cell)
        self.cells = Holder

    def gather_screen(self):
        self.win.clear_objects("YES")
        self.win.render_text(f'Population: {len(self.cells)} | shots: {self.shots}, | time: {self.shots // self.fps}', 10, 10, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.create_video_from_screenshots('cellFolder', self.shots, 'output_video.mp4', self.fps)
                quit()  # Exit the loop
        keys = self.win.pressed_keys()
        if keys[pygame.K_TAB]:
            pygame.quit()
            self.create_video_from_screenshots('cellFolder', self.shots, 'output_video.mp4', self.fps)
            quit()  # Exit the loop
        if keys[pygame.K_SPACE]:
            time.sleep(2)
            self.paused = not self.paused
        for cell in self.cells:
            pos = cell[1]
            dim = self.size
            self.win.create_object(str(cell), pos[0], pos[1], dim, dim, pygame.Color(cell[0]))
        self.win.screen()

    def execute(self):
        holder = []
        for cell in self.cells:
            color = cell[0]
            pos = cell[1]
            new_pos = pos
            for rule in self.rules:
                if rule[0][0] == color:
                    Rcolors = rule[0]
                    Rvalue = rule[1]
                    Rrange = rule[2]
                    points = self.find_positions(Rcolors[1], new_pos, Rrange)
                    new_pos = self.move_to_points(points, Rvalue, new_pos, color)
            holder.append([color, new_pos])
        self.cells = holder

    def find_positions(self, color: str, position: tuple, range: int) -> list:
        points = []
        for cell in self.cells:
            if cell[0] == color:
                dist = math.sqrt((cell[1][0] - position[0]) ** 2 + (cell[1][1] - position[1]) ** 2)
                if dist <= range:
                    points.append(cell[1])
        return points

    def spawning(self):
        if not hasattr(self, 'sp') or not self.sp:
            return
        for rule in self.sp:
            colors = rule[0]
            chance = rule[1]
            mutate = rule[2]
            if random.randint(0, chance) == 1:
                if random.randint(0, mutate) == 1:
                    color = random.choice(colors)
                else:
                    color = colors[0]
                x = random.randint(0, self.width)
                y = random.randint(0, self.height)
                self.cells.append([color, (x, y)])

    def overlaping(self, colors):
        combinations = []
        for color1 in colors:
            for color2 in colors:
                combinations.append([(color1, color2), color1 == color2])
        return combinations

    def move_to_points(self, points: list, speed: int, position: tuple, current_color: str) -> tuple:
        if not points:
            return position
        total_x, total_y = 0, 0
        for x, y in points:
            total_x += x - position[0]
            total_y += y - position[1]
        magnitude = math.sqrt(total_x ** 2 + total_y ** 2)
        if magnitude == 0:
            return position
        direction_x = total_x / magnitude
        direction_y = total_y / magnitude
        new_x = position[0] + direction_x * speed
        new_y = position[1] + direction_y * speed
        if current_color == self.colors[0]:
            new_x = position[0] - direction_x * speed
            new_y = position[1] - direction_y * speed
        if 0 <= new_x <= self.width - self.size and 0 <= new_y <= self.height - self.size:
            return new_x, new_y
        else:
            return position
