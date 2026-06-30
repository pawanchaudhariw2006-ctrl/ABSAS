import shelve
import bcrypt

DB_FILE = "app_vault_shelf"

def init_vault():
    """Initializes the persistent dictionary storage system."""
    # Shelve creates files dynamically upon item assignment
    pass

def add_user(username, password):
    """Hashes the password and saves the profile registry."""
    hashed_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    with shelve.open(DB_FILE) as db:
        if username in db:
            return False  # Profile registry signature already claimed
        
        db[username] = hashed_pass
        return True

def check_user(username, password):
    """Verifies credentials securely against stored password arrays."""
    with shelve.open(DB_FILE) as db:
        if username in db:
            stored_hash = db[username]
            return bcrypt.checkpw(password.encode('utf-8'), stored_hash)
    return False

# Initialize system structure dependencies immediately
init_vault()