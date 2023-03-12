from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, username, password=None):  
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name=first_name,
            last_name=last_name,
            )
        
        user.set_password(password)  
        user.save()

        return user

    def create_superuser(self, email, password, first_name, last_name, username):  
        user = self.create_user(
            email = email,
            username = username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            )
        
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True 
        user.save()

        return user