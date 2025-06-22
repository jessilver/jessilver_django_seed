import unittest
from jessilver_django_seed.seeders.BaseSeeder import BaseSeeder

class DummySeeder(BaseSeeder):
    @property
    def seeder_name(self):
        return "DummySeeder"
    def seed(self):
        self.succes("Seeded successfully!")

class TestBaseSeeder(unittest.TestCase):
    def setUp(self):
        self.seeder = DummySeeder()

    def test_seeder_name(self):
        self.assertEqual(self.seeder.seeder_name, "DummySeeder")

    def test_handle_success(self):
        # Should not raise exception
        self.seeder.handle()

    # def test_succes_and_error(self):
    #     self.seeder.succes("Success message")
    #     self.seeder.error("Error message")
