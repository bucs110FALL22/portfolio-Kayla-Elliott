
class Player:
  def __init(user):
    user.entity_numb = 1
    user.lives = 3
    user.can_become_incincible = True
    user.one_hit_kill = False
    user.hit_one_damage = True
    user.move_left_n_right = True
    user.move_up_n_down = True
    user.can_be_hit = True

class Goomba:
  def __init__(mob):
    mob.entity_numb = 2
    mob.lives = 1
    mob.can_stack = False
    mob.can_become_invincible = False
    mob.one_hit_kill = False
    mob.hit_one_damage = True
    mob.move_left_n_right = True
    mob.move_up_n_down = True
    mob.can_be_hit_above = True




class MystCube:
  def __init__(cube):
    cube.entity_numb = 1
    mob.lives = 1
    mob.can_stack = False
    mob.can_become_invincible = False
    mob.one_hit_kill = False
    mob.hit_one_damage = False
    mob.move_left_n_right = False
    mob.move_up_n_down = False
    cube.can_be_hit_below = True
    
