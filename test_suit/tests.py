import random

from flaky import flaky


@flaky
class TestFlakyTest:
    def test_random1(self):
        value = random.randint(1, 5)
        assert value == 2, print("****** " + str(value))

    def test_random1(self):
        value = random.randint(1, 3)
        assert value == 2, print("****** " + str(value))

    def test_random2(self):
        value = random.randint(1, 3)
        assert value == 2, print("****** " + str(value))

    def test_random3(self):
        value = random.randint(1, 3)
        assert value == 2, print("****** " + str(value))

    def test_random4(self):
        value = random.randint(1, 3)
        assert value == 2, print("****** " + str(value))

    def test_fix1(self):
        value = 2
        assert value == 2, print("****** " + str(value))

    def test_fix2(self):
        value = 2
        assert value == 2, print("****** " + str(value))
