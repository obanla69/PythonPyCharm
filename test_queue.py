from queue import MyQueue


def test_queue_size():
    queue1 = MyQueue()
    queue1.put(1,"oba")
    queue1.put(2,"moh")
    queue1.put(2, 120)
    print(queue1.queue)
    assert (queue1.queue_size() is 3)

def test_is_empty():
   queue1 = MyQueue()
   queue1.put("item")

   assert (queue1.is_empty() is True)




def test_add():
    assert False


def test_remove():
    assert False


def test_put():
    assert False


def test_delete_by_index():
    assert False


def test_add():
    assert False


