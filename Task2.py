def instances_counter(cls):
    class Counter:
        counter = 0

        def __init__(self):
            Counter.counter += 1

    @classmethod
    def get_created_instances(cls):
        print(Counter.counter)

    @classmethod
    def reset_instances_counter(cls):
        Counter.counter = 0
        print("Counter is 0")

    return Counter


@instances_counter
class User:
    pass


if __name__ == '__main__':
    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3

