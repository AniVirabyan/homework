
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

class Bullet:
    def __init__(self, x, y, direction=pygame.Vector2(0, -1), owner="player"):
        self.pos = pygame.Vector2(x, y)
        self.speed = 300
        self.direction = direction
        self.owner = owner  # Указываем, кто является владельцем пули ("player" или "enemy")

    def move(self, dt):
        self.pos += self.direction * self.speed * dt

    def draw(self):
        pygame.draw.circle(screen, "Blue", self.pos, 5)

    def collision_barrier(self, barrier_x_start, barrier_x_end, barrier_y):
        # Проверка столкновения с барьером
        if self.pos.y <= barrier_y and barrier_x_start <= self.pos.x <= barrier_x_end:
            self.direction.y *= -1  # Отражаем пулю вниз
            self.pos.y = barrier_y + 1  # Чуть сдвинуть, чтобы не застряла
            return True
        return False

    def collision_player(self, player_pos, player_width, player_height):
        # Проверка на попадание пули в игрока
        if self.owner != "player":  # Игрок не умирает от своих пуль
            if self.pos.x >= player_pos.x - player_width and self.pos.x <= player_pos.x + player_width and self.pos.y >= player_pos.y - player_height and self.pos.y <= player_pos.y + player_height:
                return True
        return False

class Enemy:
    def __init__(self, x, y, width, height, speed):
        self.pos = pygame.Vector2(x, y)
        self.width = width
        self.height = height
        self.speed = speed
        self.bullets = []
        self.target_x = x  # Начальная позиция для движения врага по X
        self.alive = True  # Переменная для отслеживания состояния врага (жив/мертв)

    def move(self, dt):
        if self.alive:  # Если враг жив, он может двигаться
            # Плавное движение врага по оси X
            direction = self.target_x - self.pos.x  # Вычисляем направление движения
            if direction > 0:
                self.pos.x += min(self.speed * dt, direction)  # Плавно двигаемся вправо
            elif direction < 0:
                self.pos.x += max(-self.speed * dt, direction)  # Плавно двигаемся влево

            # Ограничиваем движение врага в пределах экрана по X
            if self.pos.x < 0:
                self.pos.x = 0
            if self.pos.x + self.width > screen.get_width():
                self.pos.x = screen.get_width() - self.width

    def shoot(self):
        # Враг стреляет вниз с вероятностью 1%
        if random.random() < 0.01:  # 1% шанс выстрела
            bullet = Bullet(self.pos.x + self.width // 2, self.pos.y + self.height)  # Пуля появляется из центра врага
            bullet.direction = pygame.Vector2(0, 1)  # Стреляем вниз
            bullet.owner = "enemy"  # Указываем, что пуля принадлежит врагу
            self.bullets.append(bullet)

    def update(self, dt):
        if self.alive:  # Обновляем только если враг жив
            self.move(dt)
            self.shoot()
            # Обновляем пули врага
            for bullet in self.bullets[:]:
                bullet.move(dt)
                bullet.draw()

    def draw(self):
        if self.alive:  # Рисуем врага только если он жив
            pygame.draw.rect(screen, "Green", (self.pos.x, self.pos.y, self.width, self.height))

# Параметры барьера
barrier_x_start = 200  # Начальная позиция барьера по X
barrier_x_end = 500  # Конечная позиция барьера по X
barrier_y = 400  # Позиция барьера по Y
barrier_speed_x = 100  # Скорость движения барьера по оси X

# Игровые объекты
bullets = []
enemy = Enemy(500, 100, 50, 50, 100)  # Враг на экране

# Двигаем игрока, чтобы он не выходил за пределы экрана
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    # 🔹 Двигаем барьер горизонтально
    barrier_x_start += barrier_speed_x * dt
    barrier_x_end += barrier_speed_x * dt

    # 🔹 Проверяем, чтобы барьер не выходил за пределы экрана
    if barrier_x_start <= 0 or barrier_x_end >= screen.get_width():
        barrier_speed_x *= -1  # Меняем направление

    # 🔹 Рисуем игрока
    pygame.draw.circle(screen, "red", player_pos, 40)

    # 🔹 Рисуем горизонтальный барьер
    pygame.draw.line(screen, "white", (barrier_x_start, barrier_y), (barrier_x_end, barrier_y), 5)

    # 🔹 Движение игрока, чтобы он не выходил за границы
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and player_pos.y - 40 > 0:  # Верхняя граница экрана
        player_pos.y -= 300 * dt
    if keys[pygame.K_s] and player_pos.y + 40 < screen.get_height():  # Нижняя граница экрана
        player_pos.y += 300 * dt
    if keys[pygame.K_a] and player_pos.x - 40 > 0:  # Левый край экрана
        player_pos.x -= 300 * dt
    if keys[pygame.K_d] and player_pos.x + 40 < screen.get_width():  # Правый край экрана
        player_pos.x += 300 * dt

    # 🔹 Стрельба
    if keys[pygame.K_SPACE]:
        bullets.append(Bullet(player_pos.x, player_pos.y - 40, direction=pygame.Vector2(0, -1)))  # Стреляем вверх

    # 🔹 Обновляем и рисуем пули игрока
    for bullet in bullets[:]:
        bullet.move(dt)
        bullet.draw()
        if bullet.collision_barrier(barrier_x_start, barrier_x_end, barrier_y):
            continue  # Пуля столкнулась с барьером и изменила направление
        
        # Проверка на столкновение пули с врагом
        if bullet.owner == "player":  # Игрок стреляет только в врага
            # Если пуля попала в врага
            if enemy.pos.x <= bullet.pos.x <= enemy.pos.x + enemy.width and enemy.pos.y <= bullet.pos.y <= enemy.pos.y + enemy.height:
                print("Enemy hit!")
                enemy.width -= 10  # Уменьшаем размер врага при попадании
                if enemy.width <= 0:
                    print("Enemy destroyed!")
                    enemy.alive = False  # Враг уничтожен
                    print("You Win!")  # Игрок победил

    # 🔹 Обновление и рисование пуль врага
    enemy.update(dt)

    # 🔹 Рисуем врага
    enemy.draw()

    # Проверка на попадание пули врага в игрока
    for enemy_bullet in enemy.bullets[:]:
        if enemy_bullet.collision_player(player_pos, 40, 40):
            print("Game Over!")
            running = False

    pygame.display.flip()
    dt = clock.tick(60) / 1000  # Дельта времени

pygame.quit()
