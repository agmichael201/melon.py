"""Classes for melon orders."""
class AbstractMelonOrder:

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
    
    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
    
        if self.species == "Christmas":
            base_price = base_price * 1.5
        
        return total
    
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0
    order_type = "government"
    def __init__(self, species, qty):
        super().__init__(species, qty, "USA")
        self.passed_inspection = False
    
    def mark_inspection(self, passed):
        self.passed_inspection = passed
    

    


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08

    def __init__(self, species, qty):
        super().__init__(species, qty, "USA")


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17


    def get_total(self):
        total = super().get_total()
        if self.qty < 10:
            total += 3
        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code



