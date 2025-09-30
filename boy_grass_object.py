from pico2d import *
import random


# Game object class here
#1 객체를 도출 - 추상화
#2 속성을 도출 - 추상화
#3 행위를 도출
#4 클레스를 제작

class Boy:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100 , self.x, 90)
        pass

class Small_ball:
    def __init__(self):
        self.x, self.y = random.randint(50, 750), 599
        self.speed = random.randint(5, 10)
        self.image = load_image('ball21x21.png')

    def update(self):
        if self.y - self.speed > 60:
            self.y -= self.speed
        else:
            self.y = 60
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        pass

class Big_ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.speed = random.randint(5, 10)
        self.image = load_image('ball41x41.png')

    def update(self):
        if self.y - self.speed > 70:
            self.y -= self.speed
        else:
            self.y = 70
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        pass

class Zombie:
    def __init__(self):
        self.x, self.y = 100, 170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5
        pass

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0, frame_width, frame_height, self.x, self.y, frame_width // 2, frame_height // 2)
        pass

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def update(self): # 객체의 상호 작용, 행위
        pass

    def draw(self):
        self.image.draw(400, 30)
        pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()


def reset_world():
    global running
    running = True

    global world # 모든 게임 객체를 담을 수 있는 리스트
    world = [] # 아무것도 없는 빈 세상

    # 객체들을 생성
    grass = Grass()
    world.append(grass)

    team = [Boy() for _ in range(11)]
    world += team #리스트 끼리 더하기

    zombie = Zombie()
    world.append(zombie)

    small_ball = Small_ball()
    big_ball = Big_ball()

    for _ in range(20):
        if random.randint(0, 1) == 0:
            world.append(Small_ball())
        else:
            world.append(Big_ball())

reset_world()


def update_world():
    for game_object in world:
        game_object.update()


def render_world():
    clear_canvas()
    for game_object in world:
        game_object.draw()
    update_canvas()


while running:
    handle_events() # 사용자 입력 처리
    update_world() # 객체들의 상호작용을 시뮬레이션, 계산
    render_world() # 객체들의 모습을 그린다.
    delay(0.05)

close_canvas()
