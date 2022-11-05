
class Rectangle:
  #def x_coor(default, x):
   # default = 0
   # x = int(input("Enter an x cordinent of 0 or greater:"))
   # if x < default:
   #x = default
      
  #def y_coor(default, y):
    #default = 0
   # y = int(input("Enter an y cordinent of 0 or greater:"))
   # if y < default:
     # y = default
      
  #def h_coor(default, h):
   # default = 0
   # h = int(input("Enter an h cordinent of 0 or greater:"))
    #if h < default:
    #  h = default
      
  #def w_coor(default, w):
  #  default = 0
   # w = int(input("Enter an w cordinent of 0 or greater:"))
   # if w < default:
    #  w = default
      
  def __init__(rect, x, y, h, w):
    rect.x = x #x_coor(x)
    rect.y = y #y_coor(y)
    rect.height = h #h_coor(h)
    rect.width = w #w_coor(w)
    default = 0
    if x < 0:
      x = default

    if y < 0:
      y = default

    if h < 0:
      h = default

    if w < 0:
      w = default

  def __str__(rect):
    return "Makrect(x : ' + str(rect.x) + ' , y : ' + str(rect.y) + ')(h : ' + str(rect.height) + ' , w : ' + str(rect.width) + ')"
   





