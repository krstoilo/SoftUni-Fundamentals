class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        list_filtered = []
        for i in self.products:
            if i[0] == first_letter:
                list_filtered.append(i)
        return list_filtered

    def __repr__(self):
        return_list = sorted(self.products)
        string_list = '\n'.join(return_list)
        return f"Items in the {self.name} catalogue:\n{string_list}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

