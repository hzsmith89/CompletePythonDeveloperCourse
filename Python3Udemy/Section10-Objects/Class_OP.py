class Operations:

    def sum(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2


class MultiOperations(Operations):

    def mult(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        return n1 / n2

    # Override Method
    def sum(self, n1, n2):
        return (n1 + n2) * 2
