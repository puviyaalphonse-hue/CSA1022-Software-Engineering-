def login(username, password):
    # Simple lab example only; not production authentication.
    if username == 'student' and password == 'pass123':
        return 'Login successful'
    return 'Invalid username or password'

if __name__ == '__main__':
    print(login('student', 'pass123'))
