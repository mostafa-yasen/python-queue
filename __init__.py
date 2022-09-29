
class Queue:
  def __init__(self) -> None:
    self.items = []

  def enqueue(self, data: any) -> None:
    self.items.insert(0, data)

  def dequeue(self) -> any:
    return self.items.pop()

  def is_empty(self) -> bool:
    return len(self.items) == 0

  def print(self) -> None:
    items = self.items[:]
    end = " <== "
    while items:
      if len(items) == 1:
        end = "\n"

      print(items.pop(), end=end)


def main() -> None:
  queue = Queue()
  queue.enqueue(1)
  queue.enqueue(2)
  queue.enqueue(3)
  queue.enqueue(4)
  queue.print()

  print(queue.dequeue())
  queue.print()

  queue.enqueue(5)
  queue.print()


if __name__ == "__main__":
  main()
