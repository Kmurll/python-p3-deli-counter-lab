class DeliCounter:
    def __init__(self):
        self.line = []

    def take_a_number(self, name):
        self.line.append(name)
        position = len(self.line)
        print(f"Welcome, {name}. You are number {position} in line.")

    def now_serving(self):
        if len(self.line) == 0:
            print("There is nobody waiting to be served!")
        else:
            serving = self.line.pop(0)
            print(f"Currently serving {serving}.")

    def line(self):
        if len(self.line) == 0:
            print("The line is currently empty.")
        else:
            line_str = "The line is currently: " + ", ".join([f"{i + 1}. {name}" for i, name in enumerate(self.line)])
            print(line_str)

if __name__ == "__main__":
    katz_deli = DeliCounter()
    katz_deli.take_a_number("Ada")
    katz_deli.take_a_number("Gracie")
    katz_deli.take_a_number("Kent")
    katz_deli.line()
    katz_deli.now_serving()
