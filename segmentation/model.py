
class ImageSymbol(object):
    def __init__(self, pil_image, name="UNKNOW", 
                                  left=None, right=None, 
                                  top=None, bottom=None):
        self.pil_image = pil_image
        self.predict = None
        self.name = name
        self.left = left 
        self.right = right
        self.top = top
        self.bottom = bottom
        self.width = right - left
        self.height = bottom - top
        self.center = ((left+right)/2., (top+right)/2.)

    def __str__(self):
        position = "position: x -> %s"%self.left
        return "%s: %s | %s"%(self.name, self.predict, position)

    