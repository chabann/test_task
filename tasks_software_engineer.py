class CountShares:
    """
    Долевое строительство
    1. Вычислительная сложность: O(n), сложность по памяти: O(n)
    2. Ограничения на вход: 0 <= n <= 10^8 (для выполнения <= ~5 сек)
    3. Субъективная оценка: 1, время: 10 минут
    """

    def __call__(self) -> None:
        n: int = int(input())
        nums_list: list = [float(input()) for _ in range(n)]
        total_shares: int = sum(nums_list)

        for share in nums_list:
            print(round(share / total_shares, 3))


class Megatrader:
    """
    Мегатрейдер
    1. Вычислительная сложность: O(n*m*s), сложность по памяти: 
        * O(n*m*s) - мемоизация решений 
        * + O(3*n*m) - хранение входных данных  
        * + O(n*m) - стек вызовов
    2. Ограничения на вход: 0 <= n * m <= 60, 0 <= s <= 10^9 (для выполнения <= ~5 сек)
    3. Субъективная оценка: 3, время: 40 минут
    """

    def __init__(self) -> None:
        self.solutions: dict = {}
        self.stack_trace: list = []

    def __call__(self) -> None:
        params = input().split()
        num_days: int = int(params[0])
        balance: float = float(params[2])

        self.bonds: dict = self.get_input_params(num_days)

        if not len(self.bonds['price']):
            print(0)
        else:
            
            self.stack_trace.append((len(self.bonds['price']) - 1, balance))

            while self.stack_trace:
                demands = self.stack_trace[-1]
                self.knapsack(demands[0], demands[1])

            self.write_result(self.solutions.get((len(self.bonds['price']) - 1, balance), (0, [])))
            

    def write_result(self, result) -> None:
        print(result[0])

        for item in result[1]:
            print(item)

    def get_input_params(self, num_days) -> dict:
        bonds: dict = {
            'price': [],
            'profit': [],
            'name': [],
        }

        bond = input()
        while bond:
            day, _, price, count = bond.split()
            count = int(count)
            day = int(day)
            price = float(price)

            bonds['price'].append(price * count * 10)
            bonds['profit'].append(count * (1000 - 10 * price + num_days + 30 - day))
            bonds['name'].append(bond)

            bond = input()

        return bonds

    def knapsack(self, length: int, balance: float) -> None:     
        solution_key = (length, balance)

        if length < 0 or balance == 0:
            self.solutions[solution_key] = (0, [])
            self.stack_trace.pop()
    
        if solution_key not in self.solutions:
            if (self.bonds['price'][length] > balance):
                if (length-1, balance) in self.solutions:
                    self.solutions[solution_key] = self.solutions[(length-1, balance)]
                    self.stack_trace.pop()
                else:
                    self.stack_trace.append((length-1, balance))

            else:
                include_bond = None
                exclude_bond = None

                if (length - 1, balance - self.bonds['price'][length]) in self.solutions:
                    knapsack_include = self.solutions[(length - 1, balance - self.bonds['price'][length])]
                    include_bond = (knapsack_include[0] + self.bonds['profit'][length], knapsack_include[1])
                else:
                    self.stack_trace.append((length - 1, balance - self.bonds['price'][length]))

                if (length - 1, balance) in self.solutions:
                    knapsack_exclude = self.solutions[(length - 1, balance)]
                    exclude_bond = (knapsack_exclude[0], knapsack_exclude[1])
                else:
                    self.stack_trace.append((length - 1, balance))

        
                if include_bond and exclude_bond:
                    if include_bond[0] > exclude_bond[0]:
                        self.solutions[solution_key] = (include_bond[0], include_bond[1] + [self.bonds['name'][length]])
                    else:
                        self.solutions[solution_key] = (exclude_bond[0], exclude_bond[1])

                    self.stack_trace.pop()
