import random
import numpy as np
from ocatari.ram.kangaroo import Ladder


# Constants for clarity and maintainability
KANGAROO_POS_X_INDEX = 17  # RAM index for kangaroo's X position
KANGAROO_POS_Y_INDEX = 16  # RAM index for kangaroo's Y position
LEVEL_2 = 2
FLOOR = 0 

# Starting positions based on different conditions
FLOOR_1_LEVEL2_POS = (25, 10)
FLOOR_2_LEVEL2_POS = (100, 6)
FLOOR_1_START_POS = (65, 12)
FLOOR_2_START_POS = (65, 6)
ANY_FLOOR_INSTANT_WIN = (110, 0)

LVL_NUM = None


def disable_monkeys(self):
    """
    Disables the monkeys in the game
    by changing the corresponding ram positions
    """
    for x in range(4):
        self.set_ram(11 - x, 127)


def disable_coconut(self):
    """
    Disables the falling coconut in the game,
    by changing the corresponding ram positions
    """
    self.set_ram(33, 255)
    self.set_ram(35, 255)


def set_ram_kang_pos(self, pos_x, pos_y):
    """
    Set the kangaroo's position.
    Args:
    pos_x (int): The x-coordinate for the kangaroo's position.
    pos_y (int): The y-coordinate for the kangaroo's position.
    """
    if not self._already_reset:
        self.set_ram(KANGAROO_POS_X_INDEX, pos_x)
        self.set_ram(KANGAROO_POS_Y_INDEX, pos_y)
        self.set_ram(33, 255)
        self._already_reset = True

def _check_reseted(self):
    y_pos = self.get_ram()[16]
    if y_pos == 0 or y_pos == 22:
        self.set_ram(33, 255)
        self._already_reset = False

def is_at_start(pos):
    """
    checks whether the given x and y coordinates are in the starting range of the kangaroo.
    Args:
    pos_x (int): The x-coordinate.
    pos_y (int): The y-coordinate.
    """
    return 5 < pos[0] < 11 and 16 < pos[1] < 21


def check_new_level_life(self, current_lives, current_level):
    """
    Checks whether the level or amount of lives changed
    and if either or both did re-enable the changing of the starting
    position and updating the current lives and level
    """
    if current_lives != self.last_lives or current_level != self.last_level:
        self.last_lives = current_lives
        self.last_level = current_level

def unlimited_time(self):
    """
    Set the time to unlimited.
    """
    self.set_ram(59, 32)

def set_kangaroo_position(self):
    """
    Sets the kangaroo's starting position depending on the FLOOR argument.
    """
    ram = self.get_ram()
    current_level = ram[36]
    kangaroo_pos = (ram[KANGAROO_POS_X_INDEX], ram[KANGAROO_POS_Y_INDEX])    
    if is_at_start(kangaroo_pos):
        if FLOOR == 1:
            # For floor 1, position depends on whether the current level is 2
            new_pos = FLOOR_1_LEVEL2_POS if current_level == LEVEL_2 else FLOOR_1_START_POS
            set_ram_kang_pos(self, *new_pos)
        elif FLOOR == 2:
            # For floor 2, position is set to a different location
            # but also depends on the current level
            new_pos = FLOOR_2_LEVEL2_POS if current_level == LEVEL_2 else FLOOR_2_START_POS
            set_ram_kang_pos(self, *new_pos)


def random_init(self):
    """
    Randomize the floor on which the player starts.
    """
    ram = self.get_ram()
    current_level = ram[36]
    kangaroo_pos = (ram[KANGAROO_POS_X_INDEX], ram[KANGAROO_POS_Y_INDEX])
    if is_at_start(kangaroo_pos):
        random_number = random.randint(0, 2)
        if random_number == 1:
            # For floor 1, position depends on whether the current level is 2
            new_pos = FLOOR_1_LEVEL2_POS if current_level == LEVEL_2 else FLOOR_1_START_POS
            set_ram_kang_pos(self, *new_pos)
        elif random_number == 2:
            # For floor 2, position is set to a different location
            # but also depends on the current level
            new_pos = FLOOR_2_LEVEL2_POS if current_level == LEVEL_2 else FLOOR_2_START_POS
            set_ram_kang_pos(self, *new_pos)
        elif random_number == 0:
            self._already_reset = True


def change_level(self):
    """
    Changes the level according to the argument number 0-2. If not specified, selcts random level.
    """
    global LVL_NUM
    if LVL_NUM is None:
        LVL_NUM = random.randint(0, 3)
        print(f"Selcting Random Level {LVL_NUM}")
    self.set_ram(36, LVL_NUM)



def no_ladder_inpaintings():
    background_color = np.array((80, 0, 132))
    w, h = 8, 36
    patch = (np.ones((h, w, 3)) * background_color).astype(np.uint8)
    ladder_poses = [(132, 36), (132, 132), (20, 84)]
    return [(y, x, h, w, patch) for x, y in ladder_poses] # needs swapped positions

def no_ladder_step(self):
    y_pos = self.get_ram()[16]
    climbing = self.get_ram()[18]
    if climbing == 47:
        self.set_ram(18, 73)
        self.set_ram(16, y_pos+1)
    elif climbing == 39:
        self.set_ram(18, 65)
        self.set_ram(16, y_pos+1)

def remove_ladder(self):
    for obj in self.objects:
        if isinstance(obj, Ladder):
            self._objects.remove(obj)


def _modif_funcs(env, modifs):
    if "change_level" in modifs:
        modifs.remove("change_level")
        modifs.insert(0, "change_level") # Change level should be the first modif to be applied
    env.step_modifs.append(_check_reseted)
    env._already_reset = False
    for mod in modifs:
        if mod == "disable_monkeys":
            env.step_modifs.append(disable_monkeys)
        elif mod == "disable_coconut":
            env.step_modifs.append(disable_coconut)
        elif mod == "unlimited_time":
            env.step_modifs.append(unlimited_time)
        elif mod == "random_init":
            env.step_modifs.append(random_init)
            env.reset_modifs.append(random_init)
        elif "set_floor" in mod:
            if mod[-1].isdigit():
                global FLOOR
                FLOOR = int(mod[-1])
            env.reset_modifs.append(set_kangaroo_position)
            env.step_modifs.append(set_kangaroo_position)
        # elif mod == "easy_mode":
        #     env.reset_modifs.append(easy_mode)
        elif "change_level" in mod:
            if mod[-1].isdigit():
                global LVL_NUM
                LVL_NUM =  int(mod[-1])
                assert LVL_NUM < 3, "Invalid Level Number (0, 1 or 2)"
            env.step_modifs.append(change_level)
        elif mod == "no_ladder":
            env.inpaintings = no_ladder_inpaintings()
            env.step_modifs.append(no_ladder_step)
            env.place_above.extend(((223, 183, 85), (227, 151, 89))) # Player, Monkey
            env.post_detection_modifs.append(remove_ladder)    