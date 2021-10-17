class LinkedList:
    def __init__(self, collection=None):
        self.head = None
        # [1, 2, 3] ->: [3] -> [2] -> [1] -> None
        if collection:
            for item in reversed(collection):
                self.insert(item)

    # [Vader, Sideous, Revan] ->: [Revan] -> [Sideous] -> [Vader] -> None

    def __iter__(self):
        def value_generator():

            current = self.head
            while current:
                yield current.value
                current = current.next

        return value_generator()

    def __len__(self):
        return len(list(iter(self)))

    def __str__(self):
        out = ""
        for value in self:
            out += f"[ { value } ] -> "
        out += "None"
        return out

    def __eq__(self, other):
        return list(self) == list(other)

    def __getitem__(self, index):
        if index < 0:
            raise IndexError
        for i, item in enumerate(self):
            if i == index:
                return item
        raise IndexError

    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

    if __name__ == "__main__":

        # def gen():
        #     for i in range(10):
        #         yield i

        # num_gen = gen()
        # try:
        #     print(next(num_gen))
        #     print(next(num_gen))
        #     print(next(num_gen))
        #     print(next(num_gen))
        #     print(next(num_gen))
        #     print(next(num_gen))
        #     print(next(num_gen))
        #     print(next(num_gen))
        #     print(next(num_gen))
        #     print(next(num_gen))
        # except StopIteration:
        #     print('All Done!')

        # def gen2():
        #     i = 0
        #     while True:
        #         yield i
        #         i += 1

        # num_gen = gen2()
        # for i in range(1000000):
        #     print(next(num_gen))

        list1 = list("abc")  # - > ['a', 'b'. 'c']
        print(list1)
        list2 = list("abc def")
        print(list2)
