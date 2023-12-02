from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.

class FriendList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    friends = models.ManyToManyField(User, blank=True, related_name='friends')

    def __str__(self):
        return self.user.username

    def add_friend(self, account):
        if not account in self.friends.all():
            self.friends.add(account)
            self.save()

    def remove_friend(self, account):
        if account in self.friends.all():
            self.friends.remove(account)

    def unfriend(self, removee):
        remover_friends_list = self 
        remover_friends_list.remove_friend(removee) 
        friends_list = FriendList.objects.get(user=removee)
        friends_list.remove_friend(self.user)
        
    def is_mutual_friend(self, friend):
        if friend in self.friends.all():
            return True
        return False
    

class FriendRequest(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')

    def __str__(self):
        return "From {}, to {}".format(self.from_user.username, self.to_user.username)
    
    def accept(self):
        receiver_friend_list = FriendList.objects.get(user=self.to_user)
        if receiver_friend_list:
            receiver_friend_list.add_friend(self.from_user)
            sender_friend_list = FriendList.objects.get(user=self.from_user)
            if sender_friend_list:
                sender_friend_list.add_friend(self.to_user)
                self.delete()
                
    def decline(self):
        self.delete()
        
    def cancel(self):
        self.delete()
        
        
        
  