class EmailExists(Exception):
    def __init__(self, message = "Email is already registered"):
        self.message = message
        super().__init__(self.message)