# One of the most common tasks that you'll have to perform in your programs is working with external resources.
# These resources can be files on your computer's storage or an open connection to third-party service on the internet.

# An object which controls the environment seen in a with statement by defining __enter__() and __exit__() methods.


# To write a class-based context manager in Python, you need to create an empty class with three specific methods:

# Here’s how the with statement proceeds when Python runs into it:
# Call expression to obtain a context manager.
# Store the context manager’s .__enter__() and .__exit__() methods for later use.
# Call .__enter__() on the context manager and bind its return value to target_var if provided.
# Execute the with code block.
# Call .__exit__() on the context manager when the with code block finishes.

class Database:
    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


# loading a file
with FileManager('test.txt', 'w') as f:
    f.write('Test')

print(f.closed)
