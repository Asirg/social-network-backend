def check_user_privacy(profile, user):
    if user.is_staff or user.id == profile.id:
        return "nobody"
    if profile.subscribers.filter(follower__id=user.id, relation='confirmed'):
        return "confirmed"
    else:
        return "all"
    
