from monster_class import *

class Staff(Monster):

    def __init__(self, name, staff_id):
        super().__init__(name)
        self.staff_id = staff_id
