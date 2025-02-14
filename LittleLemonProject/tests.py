from django.test import TestCase
from restaurantApp.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Bruschetta", price=12, inventory=12)
        self.assertEqual(str(item), "Bruschetta : 12")
