class DataValidator:
    def __init__(self):
        self.errors = []

    def validate_email(self, email):
        if '@' not in email:
            self.errors.append(f"invalid email: {email}")
            return False
        return True

    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"invalid age: {age}")
            return False
        return True

    def get_errors(self):
        return self.errors

# Create the validator
validator = DataValidator()

# Add the arguments
validator.validate_email("jairperez")
validator.validate_age(-2)
validator.validate_email("elpepe")
validator.validate_age(420)

# print the errors
print(validator.get_errors())
