from abc import ABC, abstractmethod

class BaseSeeder(ABC):

    @property
    @abstractmethod
    def seeder_name(self):
        pass

    help = f'Seed database with {seeder_name} data'

    @abstractmethod
    def seed(self):
        pass

    def handle(self):
        print(f'\033[93mExecuting {self.seeder_name}...\033[0m')
        try:
            self.seed()
            print(f'\033[93mExecuting finished for {self.seeder_name}\033[0m')
        except Exception as e:
            print(f'\033[91mError executing {self.seeder_name}: {e}\033[0m')
    
    def success(self, message):
        print(f'\033[92m- {message}\033[0m')

    def error(self, message):
        print(f'\033[91m- {message}\033[0m')

    def info(self, message):
        print(f'\033[94m- {message}\033[0m')

    def warning(self, message):
        print(f'\033[93m- {message}\033[0m')

    def debug(self, message):
        print(f'\033[95m- {message}\033[0m')

    def __name__(self):
        return self.seeder_name
    
