class Person:

    def __init__(self, name, weight):
        self.name = name;
        self.weight = weight;

    def run(self):
        self.weight -= .5

    def eat(self):
        self.weight += .5

    def __str__(self):
        return "%s的体重是%.2f " % (self.name, self.weight)


lc_person = Person("lc", 165)

lc_person.run()
lc_person.run()
lc_person.run()
lc_person.run()
lc_person.run()
lc_person.run()
lc_person.run()
lc_person.run()

print(lc_person)
