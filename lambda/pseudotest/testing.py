from pseudo.runtime import RunTime
from pseudo.type.numbers import Int
from pseudo.type.string import String


class Testing(RunTime):

    def __init__(self, test_in, test_out):
        RunTime.__init__(self)
        self.test_in = test_in
        self.test_out = test_out

    def stdin(self, k, i=[]):
        try:
            v = self.test_in[0]
            del self.test_in[0]

            try:
                v = Int(v)
            except ValueError:
                v = String(v)

            self.save(k, v)

        except IndexError:
            raise AssertionError

    def stdout(self, v, i=[]):  # TODO: fix
        print(v, self.test_out[0])
        if v == self.test_out[0]:
            del self.test_out[0]
        else:
            raise AssertionError

    def run(self, instructions):
        for i in instructions:
            self.eval(i)
