class Fibonacci:
    def __init__(self, steps) -> None:
        self.steps = steps
        self.prev_numbers = [0, 1]
        self._step = 0

    def __next__(self):
        if self._step < self.steps:
            number = self.prev_numbers[0]
            new_number = sum(self.prev_numbers)
            self.prev_numbers[0] = self.prev_numbers[1]
            self.prev_numbers[1] = new_number;

            self._step += 1

            return number   
        else:
            raise StopIteration
    

fib = Fibonacci(100)

for i in range(0, 101):
    print(next(fib), fib._step)
