# ================= Base Class: Character =================
class Character:
    book_title = "No Longer at Ease"
    author = "Chinua Achebe"

    def __init__(self, name, role, traits):
        self.name = name        # character's name
        self.role = role        # role in the story
        self.traits = traits    # personality traits (list)

    # Display character info including book and author
    def info(self):
        print(f"{self.name} is the {self.role} in '{self.book_title}' by {self.author}, with traits: {', '.join(self.traits)}.")

    # Character performs an action
    def act(self, action):
        print(f"{self.name} {action}.")


# ================= Subclass: Student =================
class Student(Character):
    def __init__(self, name, role, traits, university, field_of_study):
        super().__init__(name, role, traits)  # inherit attributes
        self.university = university          # university attended
        self.field_of_study = field_of_study  # field of study

    # Override info method (polymorphism)
    def info(self):
        print(f"{self.name}, a student of {self.field_of_study} at {self.university}, in '{self.book_title}' by {self.author}, has traits: {', '.join(self.traits)}.")

    # New method specific to students
    def study(self):
        print(f"{self.name} is studying {self.field_of_study} at {self.university}.")


# ================= Create Objects =================

# Protagonist: Obi Okonkwo
obi = Student(
    name="Obi Okonkwo",
    role="protagonist",
    traits=["intelligent", "idealistic", "ambitious"],
    university="University College, London",
    field_of_study="Accounting"
)

# Supporting character: Mr. Green
mr_green = Character(
    name="Mr. Green",
    role="government official",
    traits=["authoritative", "strict"]
)

# ================= Interactions =================
obi.info()
obi.study()
obi.act("reflects on his return to Nigeria")

print()  # blank line for separation

mr_green.info()
mr_green.act("questions Obi about his plans")
