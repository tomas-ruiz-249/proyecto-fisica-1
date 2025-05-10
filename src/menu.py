import pygame as pg

class Button():
    def __init__(self, onClick: callable, text: str):
        self.onClick = onClick
        self.area = pg.Rect(0,0,0,0)
        self.text = text

    def checkForClick(self, pos: tuple[int, int]):
        if self.area.collidepoint(pos):
            self.onClick()

class Layout():
    def __init__(self, elements: list[Button]):
        self.elements = elements
    
    def set_area(self, layout_top: int, layout_width: int, layout_height:int):
        btn_width = layout_width / len(self.elements)
        count = 0
        for btn in self.elements:
            btn.area.update(count * btn_width,
                            layout_top,
                            btn_width - 1,
                            layout_height-1)
            count += 1


class Menu():
    def __init__(self, elements: list[Layout], menuHeight: int, menuWidth: int, color: pg.Color = None):
        self.elements = elements
        self.color = color if color != None else pg.Color(3, 152, 252)
        self.layout_height = menuHeight / len(elements)
        self.layout_width = menuWidth
        count = 0
        for layout in elements:
            layout.set_area(count * self.layout_height, menuWidth, self.layout_height)
            count += 1
    
    def check_for_click(self, pos: tuple[int, int]):
        for layout in self.elements:
            for button in layout.elements:
                button.checkForClick(pos)

