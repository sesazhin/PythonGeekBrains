class Toy:
    def __init__(self,name,type,color,goods):
        self._name = name
        self._type = type
        self._color = color
        self._goods = goods

    def gettype(self):
        return self._type

    def getname(self):
        return self._name

    def getcolor(self):
        return self._color

    def getgoods(self):
        return self._goods

    def setcolor(self, color):
        self._color = color

class Wolf(Toy):
    def __init__(self,name,color):
        if Toy.__init__(self,name,"wolf",color,1):
            print("ERROR: Wolf:__init__>> Object with type wolf hasn't been created!")

class Bear(Toy):
    def __init__(self,name,color):
        if Toy.__init__(self,name,"bear",color,2):
            print("ERROR: Wolf:__init__>> Object with type bear hasn't been created!")

class Bunny(Toy):
    def __init__(self,name,color):
        if Toy.__init__(self,name,"bunny",color,3):
            print("ERROR: Wolf:__init__>> Object with type bear hasn't been created!")

class Fabric:
    _list_of_names = {"wolf": ["Akela"], "bear": ["Baloo"], "bunny": ["Bugs Bunny"]}
    _list_of_types = {"wolf": 1, "bear": 2, "bunny": 3}  # 1,2,3 - how many resources required for each type of toy

    def __init__(self,goods_amount):
        self._goods_amount = goods_amount #unused for now...

    def getnames():
        return Fabric._list_of_names

    def Bying_goods(self,type_of_toy): #do we really need 'self' here?
        if type_of_toy in Fabric._list_of_types.keys():
            print("\nFabric:Bying_goods>>Bought {} materials for toy of type {}".format(Fabric._list_of_types.get(type_of_toy), type_of_toy))

        else:
            print("\nERROR: Fabric:Bying_goods>> Can't produce toy of type '{}' (this type is not supported)".format(type_of_toy))

    def Tailoring(self,name,type_of_toy):

        if name in Fabric._list_of_names.get(type_of_toy): #if toy with this name and specified type exists - try to create it (check whether Fabric has enough resources first)
            if self._goods_amount < Fabric._list_of_types.get(type_of_toy):  # if not enough existing resources to tailor a toy - then buy them
                self.Bying_goods(type_of_toy)

            # if resources were enough or if we bought them - create instance of a toy:

            if type_of_toy == "wolf":
                toy = Wolf(name, None)

            if type_of_toy == "bear":
                toy = Bear(name, None)

            if type_of_toy == "bunny":
                toy = Bunny(name, None)

            return toy

        else:
            print("\nERROR: Fabric:Tailoring>> Can't produce toy of name: '{}' and type: {} (this is not supported)".format(name,type_of_toy))

    def Coloring(self,ToyObj,toy_color):

        toy = ToyObj

        try:
            toy.setcolor(toy_color)
            print("Fabric:Coloring>> Finished to create a toy: '{}' with name: '{}' and color: '{}'".format(toy.gettype(),toy.getname(),toy.getcolor()))

        except AttributeError:
            print("ERROR: Fabric:Tailoring>> Object with type <ToyObj> hasn't been created!")

fabric1 = Fabric(0)
toy = fabric1.Tailoring("Akela","wolf")
fabric1.Coloring(toy,"red")

toy2 = fabric1.Tailoring("Bugs Bunny","bunny")
fabric1.Coloring(toy2,"blue")

toy3 = fabric1.Tailoring("Baloo","bear")
fabric1.Coloring(toy3,"yellow")

toy4 = fabric1.Tailoring("Bugs Bunny","wolf")
fabric1.Coloring(toy4,"red")