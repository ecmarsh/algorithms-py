"""
@lc id=1114 lang=python3 tag=concurrency

[1114] Print in Order

Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}

The same instance of Foo will be passed to
three different threads. Thread A will call first(),
thread B will call second(), and thread C will call third().

Design a mechanism and modify the program to ensure that
second() is executed after first(), and third() is executed
after second().

Example 1:
Input: [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired
asynchronously. The input [1,2,3] means thread A calls
first(), thread B calls second(), and thread C calls third().
"firstsecondthird" is the correct output.

Example 2:
Input: [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(),
thread B calls third(), and thread C calls second().
"firstsecondthird" is the correct output.


Note:
We do not know how the threads will be scheduled in the
operating system, even though the numbers in the input seems
to imply the ordering. The input format you see is mainly to
ensure our tests' comprehensiveness.
"""


from threading import Lock


class Foo:
    def __init__(self):
        self.firstJobDone = Lock()
        self.secondJobDone = Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        # Notify thread that is waiting for first job to complete.
        self.firstJobDone.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.firstJobDone:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            # Notify thread that is waiting for second job to complete.
            self.secondJobDone.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.secondJobDone:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()

