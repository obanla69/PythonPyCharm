import unittest
from stack import MyStack

class stackTestCase(unittest.TestCase):
    def test_can_add_element(self):
        stack = MyStack()
        stack.add_to_stack("Semicolon")
        stack.add_to_stack("google.com")
        stack.add_to_stack("recuters.ng")
        stack.add_to_stack("x.com")
        self.assertEqual(len(stack.stack),4)


    def test_stack_remove_last_in_element(self):
        stack = MyStack()
        stack.add_to_stack("Semicolon")
        stack.add_to_stack("google.com")
        stack.add_to_stack("recuters.ng")
        stack.add_to_stack("x.com")
        stack.pop()
        self.assertEqual(stack.stack[-1],"recuters.ng")


def test_queue_size():
    queue1 = MyQueue()
    queue1.put(1,"oba")
    queue1.put(2,"moh")
    queue1.put(2, 120)
    print(queue1.queue)
    assert (queue1.queue_size() is 3)


if __name__ == '__main__':
    unittest.main()
