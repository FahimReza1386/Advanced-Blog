from accounts.models.profile import Profile

class ProfileService:
    
    @staticmethod
    def create_for_user(user):
        return Profile.objects.create(user=user)