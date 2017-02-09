
class PasscodeAssembler:
    _passcode = []
    _derivations = []

    def __init__(self, debug=False):
        self._debug = debug

    def add_derivation(self, input_derivation):
        self._derivations.append(input_derivation)
        for derivation in self._derivations:
            for index, number in enumerate(derivation):
                if number not in self._passcode:
                    self._passcode.append(number)
                else:
                    for reiterated_number in derivation:
                        if number != reiterated_number and reiterated_number in self._passcode:
                            if not PasscodeAssembler.appears_before(reiterated_number, number, self._passcode) and\
                                    PasscodeAssembler.appears_before(reiterated_number, number, derivation):
                                self.prepend_to(reiterated_number, number)
        if self._debug:
            print(str(input_derivation) + ' : ' + str(self._passcode))

    def prepend_to(self, a, b):
        try:
            index_a, index_b = self._passcode.index(a), self._passcode.index(b)
            self._passcode.insert(index_a, self._passcode.pop(index_b))
        except ValueError:
            pass

    def append_to(self, a, b):
        try:
            index_a, index_b = self._passcode.index(a), self._passcode.index(b)
            self._passcode.insert(index_a+1, self._passcode.pop(index_b))
        except ValueError:
            pass

    @staticmethod
    def appears_before(arg1, arg2, list_arg):
        return list_arg.index(arg1) < list_arg.index(arg2)

    @staticmethod
    def elements_appear_in(list1, list2):
        for element in list1:
            if element in list2:
                return True
        return False

    def get_passcode(self):
        result = "Passcode: "
        for number in self._passcode:
            result += str(number)
        return result


if __name__ == '__main__':
    f = open('problem_79_derivations.txt', 'r')
    derivations = f.read().split()
    assembler = PasscodeAssembler()
    for derivation in derivations:
        assembler.add_derivation(list(derivation))
    print(assembler.get_passcode())
