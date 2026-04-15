from dataclasses import dataclass,field
@dataclass
class MenuItem:
    name: str
    price: float
    quantity: int
    def value(self):
        return round(self.price * self.quantity, 2)
    
@dataclass
class Restaurant:
    name: str
    menu_items: list = field(default_factory=list)
    total_revenue: float = field(init=False)
    def __post_init__(self):
        self._refresh()
    def _refresh(self):
        total = 0
        for item in self.menu_items:
            total += item.value()
        self.total_revenue = round(total ,2)
    def add_item(self, item: MenuItem):
        self.menu_items.append(item)
        self._refresh()
    def serve(self,item_name: str, qty: int) -> bool:
        for item in self.menu_items:
            if item.name == item_name:
                if item.quantity >= qty:
                    item.quantity -= qty
                    self._refresh()
                    return True
                return False
        return False
    def resupply(self,item_name: str , qty: int):
        for item in self.menu_items:
            if item.name == item_name:
                item.quantity += qty
                self._refresh()
    def report(self) -> str:
        lines = [f"{self.name} Menu:"]
        for item in self.menu_items:
            lines.append(f"  {item.name}: {item.quantity} servings @ ${item.price} each")
        lines.append(f"Total revenue: ${self.total_revenue}")
        return "\n".join(lines)
    
m1 = MenuItem("Burger", 12.99, 20)
m2 = MenuItem("Salad", 8.49, 40)
m3 = MenuItem("Pasta", 14.99, 15)

r = Restaurant("BistroHub")
r.add_item(m1)
r.add_item(m2)
r.add_item(m3)

print(r.total_revenue)
print(r.serve("Burger", 5))
print(r.serve("Burger", 25))
r.resupply("Salad", 10)
print(r.report())












     

    
