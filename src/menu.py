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
    def __init__(self, elements: list[Button], offset: float, elem_width: float):
        self.elements = elements
        self.offset = offset
        self.elem_width = elem_width

class HLayout(Layout):
    def __init__(self, elements: list[Button], offset: float, elem_width: float):
        super().__init__(elements, offset, elem_width)  
        count = 1
        for b in elements:
            b.area.update((offset + elem_width) * count,
                          offset,
                          elem_width,
                          elem_width * 0.6)
            count += 1

class VLayout(Layout):
    def __init__(self, elements: list[Button], offset: float, elem_width: float):
        super().__init__(elements, offset, elem_width)  
        count = 0
        elem_height = elem_width * 0.5
        for b in elements:
            b.area.update(offset,
                          (elem_height + offset) * count + offset,
                          elem_width,
                          elem_height)
            count += 1

class Menu():
    def __init__(self, elements: list[Layout], color: pg.Color = None):
        self.elements = elements
        self.color = color if color != None else pg.Color(3, 152, 252)
    
    def check_for_click(self, pos: tuple[int, int]):
        for layout in self.elements:
            for button in layout.elements:
                button.checkForClick(pos)

