class random:
    def __init__(self, name, height, salary=0):
        self.height = height
        self.name = name
        self.salary = salary





if __name__ == '__main__':
    first_emp = random("Logan", 5)
    second_emp = random("Haley", 6, 56000)

    print(first_emp.height)
    print(second_emp.salary)
