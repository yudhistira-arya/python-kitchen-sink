class Contact:
    all_contacts = [] # class variable
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def print_name(self):
        print(self.name)

class Supplier(Contact):
    # default constructor will call parent constructor by default
    def order(self, order):
        # no variable shadowing
        print("send {} order to {}".format(order, self.name))

class ColorPropertyMethodStyle:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name
    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name
    def _get_name(self):
        return self._name
    # to set getter and setter
    name = property(_get_name, _set_name)

class ColorPropertyDecoratorStyle:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter
    def name(self):
        self._name = ""

if __name__ == '__main__':
    c = Contact("contact", "somebody@example.net")
    # will implicitly call parent constructor
    s = Supplier("supplier", "sup@example.net")
    c.print_name()
    s.print_name()

    c = ColorPropertyMethodStyle("#0000ff", "bright red")
    print(c.name)

    d = ColorPropertyDecoratorStyle("#0000ff", "bright red")
    print(d.name)

