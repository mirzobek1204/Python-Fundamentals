def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[ACTION] {func.__name__} executed")
        result = func(*args, **kwargs)
        return result
    return wrapper
class Employee:
    _total_employees = 0
    def __init__(self,name,emp_code):
        self.name = name
        self.emp_code = emp_code
        self._tasks = {}
        Employee._total_employees += 1
    @log_action
    def assign_task(self, task_name, score):
        upper_task_name = task_name.upper()
        self._tasks[upper_task_name] = score
        return f"{self.name} assigned {upper_task_name} with score {score}"
    def avg_score(self):
        if not self._tasks:
            return 0.0
        scores = self._tasks.values()
        average = sum(scores) / len(scores)
        return float(round(average,1))
    def top_task(self):
        if not self._tasks:
            return "No tasks"
        return max(self._tasks, key=self._tasks.get)
    @classmethod
    def from_record(cls,data):
        name, emp_code = data.split("-")
        return cls(name,emp_code)
    @staticmethod
    def is_valid_code(emp_code):
        if len(emp_code) != 7:
            return False
        for char in emp_code:
            if not "0" <= char <= "9":
                return False
        return True
    @classmethod
    def total_employees(cls):
        return cls._total_employees

e1 = Employee("Sardor", "3301001")
e1.assign_task("report", 90)
e1.assign_task("analysis", 76)
e1.assign_task("design", 84)

e2 = Employee.from_record("Kamola-3301002")
e2.assign_task("Testing", 88)
e2.assign_task("review", 95)

print(f"{e1.name}: Avg = {e1.avg_score()}, Top = {e1.top_task()}")
print(f"{e2.name}: Avg = {e2.avg_score()}, Top = {e2.top_task()}")

print(f"Valid code '3301001': {Employee.is_valid_code('3301001')}")
print(f"Valid code '33B': {Employee.is_valid_code('33B')}")
print(f"Total employees: {Employee.total_employees()}")
