from repositeries.user_repo import save_user as sa ,login_user as lu,existing_user as eu

def save_user(email, password_hash):
    existing_mail=eu(email)
    if existing_mail == None:
      user=sa(email,password_hash)
      return user
    return False
        