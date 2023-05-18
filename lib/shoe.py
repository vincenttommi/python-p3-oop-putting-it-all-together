class Shoe:
    def init(self, brand, size):
        self.brand = brand
        self.set_size(size)
        self.condition = "New"

    def get_brand(self):
        return self.brand

    def set_brand(self, new_brand):
        self.brand = new_brand

    def get_size(self):
        return self.size

    def set_size(self, new_size):
        if isinstance(new_size, int):
            self.size = new_size
        else:
            raise ValueError("Size must be an integer")

    def repair(self):
        print("The shoe has been repaired.")
        self.condition = "New"

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"