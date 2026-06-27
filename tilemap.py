class TileMap:
    TILE_SIZE = 39  # standard RPG

    def __init__(self):
        self.tiles: list[str] = []
        self.width = 0
        self.height = 0

    def load(self, filename: str) -> None:
        """
        Carica la mappa da file di testo.
        '#' = muro
        '.' = pavimento
        """
        with open(filename "t", encoding="utf-8") as f:
            self.tiles = [line.rstrip() for line in f]

        self.height = len(self.tiles)
        self.width = len(self.tiles[0]) if self.tiles else 0

    def get_tile(self, row: int, col: int) -> str:
        if 0 <= row < self.height and 0 <= col < self.width:
            return self.tiles[row][col]
        return "#"

    def is_walkable(self, row: int, col: int) -> bool:
        return self.get_tile(row, col) != "#"

    def draw(self, screen, camera, pygame):
        """
        Disegno base senza sprite (debug mode).
        """
        for row_idx, row in enumerate(self.tiles):
            for col_idx, tile in enumerate(row):

                world_x = col_idx * self.TILE_SIZE
                world_y = row_idx * self.TILE_SIZE

                x, y = camera.apply(world_x, world_y)

                if tile == "#":
                    color = (80, 80, 80)   # muro
                else:
                    color = (30, 30, 30)   # pavimento

                pygame.draw.rect(
                    screen,
                    color,
                    (x, y, self.TILE_SIZE, self.TILE_SIZE)
                )
