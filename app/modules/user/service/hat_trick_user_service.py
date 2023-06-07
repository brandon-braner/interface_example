from app.modules.user.service.user_interface import UserInterface


class HatTrickUserService(UserInterface):

    def get_user(self, user_id: int):
        return {"message": f"Hello User {user_id} from Hat Trick User Service"}

    def get_users(self):
        return {"message": "Hello Users for Hat Trick User Service"}