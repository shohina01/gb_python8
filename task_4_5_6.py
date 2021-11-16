class Storage:
    def __init__(self):
        self.current_machines = []
        self.sent_machines = []

    def get_machines(self, machine):
        self.current_machines.append(machine)

    def send_machines(self, machine, department):
        self.current_machines.remove(machine)
        self.sent_machines.append(machine)
        department.take_equipment(machine)


class OfficeDepartment:
    def __init__(self):
        self.machines = []

    def take_equipment(self, machine):
        self.machines.append(machine)


class OfficeEquipment:

    def __init__(self, name, model, price, eq_type, amount):
        self.name = name
        self.model = model
        self.price = price
        self.type = eq_type
        self.amount = amount

    def __repr__(self):
        return f'{self.name} - {self.amount}'


class Printer(OfficeEquipment):

    def __init__(self, name, model, price, eq_type, printing_speed, quality_of_printing, amount):
        OfficeEquipment.__init__(self, name, model, price, eq_type, amount)
        self.printing_speed = printing_speed
        self.quality_of_printing = quality_of_printing


class Scanner(OfficeEquipment):

    def __init__(self, name, model, price, eq_type, scanning_speed, quality_of_scanning, amount):
        OfficeEquipment.__init__(self, name, model, price, eq_type, amount)
        self.printing_speed = scanning_speed
        self.quality_of_scanning = quality_of_scanning


class Copier(OfficeEquipment):

    def __init__(self, name, model, price, eq_type, printing_speed, quality_of_printing, amount):
        OfficeEquipment.__init__(self, name, model, price, eq_type, amount)
        self.printing_speed = printing_speed
        self.quality_of_printing = quality_of_printing


first_instant = Printer('printer', 'g-586', 58425, 'matrix', '5/sec', '1080px', 5)
second_instant = Copier('copier', 'hp894', 58425, 'matrix', '5/sec', '1080px', 6)
storage = Storage()
storage.get_machines(first_instant)
storage.get_machines(second_instant)
accountant_department = OfficeDepartment()
storage.send_machines(first_instant, accountant_department)
print(f'Now in storage are : {storage.current_machines}')
print(f'Now in department are :{accountant_department.machines}')
