# SOC W2 D3 - Classes
class Student():
        # constructor?
    def __init__(self, ask_id, food):
        self.id_name = ask_id
        self.food = food

    def my_print(self):
        print(self.id_name + ' ' + self.food)


s1 = Student("Slay Queen", "potatoes")
s2 = Student("NerdSlash", "pupusas")
s3 = Student("DogeLovah", "tacos")

print(s1.id_name)  # dot notation
print(s2.food)
s3.my_print()
