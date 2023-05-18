class Book:
    def init(self, title, page_count):
        self.title = title
        self.set_page_count(page_count)

    def get_title(self):
        return self.title

    def set_title(self, new_title):
        self.title = new_title

    def get_page_count(self):
        return self.page_count

    def set_page_count(self, new_page_count):
        if isinstance(new_page_count, int):
            self.page_count = new_page_count
        else:
            print("Page count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")