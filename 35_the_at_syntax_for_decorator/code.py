import functools

user = {"username": "jose", "access_level": "admin"}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == "admin":
                return func(*args, **kwargs)
            else:
                return f"No admin privilages for {user['username']}."
        
        return secure_function
    return decorator

@make_secure("admin")
def get_admin_password():
    return "1234"

@make_secure("user")
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"

print(get_admin_password())

print(get_password("billing"))