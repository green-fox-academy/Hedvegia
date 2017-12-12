class Garden(object):
    def __init__(self, needs=0):
        self.needs = needs

    
class Flower(Garden):
    def __init__(self, needs, flowers_name):
        super().__init__(needs)
        self.flowers_name = flowers_name

    def flower_level(self):
        if self.needs <= 5:
            print("The ", self.flowers_name, " needs water.")
        else:
            print("The ", self.flowers_name, " doesn't need water.")
    

class Trees(Garden):
    def __init__(self, needs, trees_name):
        super().__init__(needs)
        self.trees_name = trees_name

    def trees_level(self):
        if self.needs <= 10:
            print("The ", self.trees_name, " needs water.")
        else:
            print("The ", self.trees_name, " doesn't need water.")     

            

yellowFlower = Flower(3, "yellow Flower")
blueFlower = Flower(7, "blue Flower")
purpleTree = Trees(11, "purple Trees")
orangeTree = Trees(5, "orange Tree")

yellowFlower.flower_level()
blueFlower.flower_level()
purpleTree.trees_level()
orangeTree.trees_level()


