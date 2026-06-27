class Camera:
    def __init__(self, width: int=900, height: int = 700):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height

    def follow(self, target) -> None:
        """
        Centra la camera sul target (player o entità con x, y).
        """
        self.x = target.x - self.width // 2
        self.y = target.y - self.height // 2

    def apply(self, x: int, y: int) -> tuple[int, int]:
        """
        Converte coordinate world → screen.
        """
        return x - self.x, y - self.y

    def apply_rect(self, rect):
        """
        Versione comoda per pygame.Rect.
        """
        return rect.move(-self.x, -self.y)
