import pygame

class Player:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

        self.speed = 0.2

        self.size = 24
        self.color = (0, 200, 0)

    def move(self, dx: float, dy: float, tilemap):
        """
        Movimento con collisioni semplici su TileMap.
        """

        # movimento X
        new_x = self.x + dx
        if not self.collides(new_x, self.y, tilemap):
            self.x = new_x

        # movimento Y
        new_y = self.y + dy
        if not self.collides(self.x, new_y, tilemap):
            self.y = new_y

    def collides(self, x: float, y: float, tilemap) -> bool:
        """
        Collisione con tile '#'
        """

        # controlliamo i 4 angoli del player
        points = [
            (x, y),
            (x + self.size, y),
            (x, y + self.size),
            (x + self.size, y + self.size),
        ]

        for px, py in points:
            col = int(px // tilemap.TILE_SIZE)
            row = int(py // tilemap.TILE_SIZE)

            if not tilemap.is_walkable(row, col):
                return True

        return False

    def update(self, keys, tilemap):
        dx = 0
        dy = 0

        if keys[pygame.K_w]:
            dy -= self.speed
        if keys[pygame.K_s]:
            dy += self.speed
        if keys[pygame.K_a]:
            dx -= self.speed
        if keys[pygame.K_d]:
            dx += self.speed

        self.move(dx, dy, tilemap)

    def render(self, screen, camera):
        x, y = camera.apply(self.x, self.y)

        pygame.draw.rect(
            screen,
            self.color,
            (x, y, self.size, self.size)
        )
