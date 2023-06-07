from abc import ABC, abstractmethod

class UserInterface(ABC):

    @abstractmethod
    def get_user(self, user_id: int):
        pass

    @abstractmethod
    def get_users(self):
        pass


class DeleteUserInterface(UserInterface):

        @abstractmethod
        def delete_user(self, user_id: int):
            pass