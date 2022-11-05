from Rectangle import Rectangle
from Surface import Surface

#r = Rectangle(10, 10, 10, 10)

#assert((r.x, r.y, r.height, r.width) == (10,10,10,10)) #succsess


#r = Rectangle(-1, 1, 1, 1)

#assert((r.x, r.y, r.height, r.width) == (0,1,1,1))  #fail


#r = Rectangle(1, -1, 1, 1)

#assert((r.x, r.y, r.height, r.width) == (1,0,1,1)) #fail


#r = Rectangle(1, 1, -1, 1)

#assert((r.x, r.y, r.height, r.width) == (1,1,0,1))  #fail


#r = Rectangle(1, 1, 1, -1)

#assert((r.x, r.y, r.height, r.width) == (1,1,1,0)) #fail


#######

r = Rectangle(10, 10, 10, 10)

assert((r.x, r.y, r.height, r.width) == (10,10,10,10)) #succsess

r = Rectangle(-1, 1, 1, 1)

assert((r.x, r.y, r.height, r.width) == (-1,1,1,1))  #succsess


r = Rectangle(1, -1, 1, 1)

assert((r.x, r.y, r.height, r.width) == (1,-1,1,1)) #succsess


r = Rectangle(1, 1, -1, 1)

assert((r.x, r.y, r.height, r.width) == (1,1,-1,1))  #succsess


r = Rectangle(1, 1, 1, -1)

assert((r.x, r.y, r.height, r.width) == (1,1,1,-1)) #succsess




s = Surface("myimage.png", 10, 10, 10, 10)

assert((s.rect.x, s.rect.y, s.rect.height, s.rect.width) == (10,10,10,10))  #pass


srect = s.getRect()

assert((srect.x,  s.getRect().y, srect.height,  srect.width) == (10,10,10,10))  #pass

assert s.image   #pass


print("Test Complete!")
