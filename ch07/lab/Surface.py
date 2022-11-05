from Rectangle import Rectangle

class Surface:
    def __init__(surf, filename, x, y, h, w):
        surf.rect = Rectangle(x, y, h, w)
        surf.image = filename  #file name??
    def getRect(surf):
        return surf.rect


    

