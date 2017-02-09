class PasscodeAssembler:
    _passcode = []
    _derivations = []

    def __init__(self, debug=False, derivation_list=None):
        self._debug = debug
        self._derivations = derivation_list

    def compute_passcode(self):
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
                print(str(derivation) + ' : ' + str(self._passcode))

    def prepend_to(self, a, b):
        try:
            index_a, index_b = self._passcode.index(a), self._passcode.index(b)
            self._passcode.insert(index_a, self._passcode.pop(index_b))
        except ValueError:
            pass

    @staticmethod
    def appears_before(arg1, arg2, list_arg):
        return list_arg.index(arg1) < list_arg.index(arg2)

    def get_passcode(self):
        self.compute_passcode()
        result = "Passcode: "
        for number in self._passcode:
            result += str(number)
        return result


if __name__ == '__main__':
    f = open('problem_79_derivations.txt', 'r')
    derivation_lists = [list(item) for item in f.read().split()]
    assembler = PasscodeAssembler(derivation_list=derivation_lists)
    print(assembler.get_passcode())
