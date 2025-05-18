class Counter:
    # Class variable to keep track of object count
    count = 0

    def __init__(self):
        Counter.count += 1  # Increment class variable on object creation

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

# Create objects
c1 = Counter()
c2 = Counter()
c3 = Counter()

# Display count using class method
Counter.display_count()
