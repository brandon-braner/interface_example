from app.modules.user.service.user_interface import UserInterface


class TQAUserService(UserInterface):
    def get_user(self, user_id: int):
        return {"message": f"Hello User {user_id} from TQA User Service"}

    def get_users(self):
        return {"message": "Hello All Users from TQA User Service"}
