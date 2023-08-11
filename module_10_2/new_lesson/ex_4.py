# Реализовать валидацию скобок методами ООП
# input_text = '}<div><p>{ test }}</p</div>'
# }<div><p>{ test }}</p</div>
# ^                ^^
# Unbalanced brackets: at 0, at 17, at 18

import sys


class ValidataionError(Exception):
    def __init__(self, *args, idx=None):
        self.idx = idx
        super().__init__(*args)


class StringValidation:
    def __init__(self):
        self._text = None
        self._opens = '([{<'
        self._closes = ')]}>'
        self._message = ''

    def is_balanced(self):
        stack = []
        errors = []
        for symbol_position, symbol in enumerate(self._text):
            if symbol in self._opens:
                stack.append((symbol_position, symbol))
            elif symbol in self._closes:
                position = self._closes.index(symbol)
                if stack and self._opens[position] == stack[-1][1]:
                    stack.pop()
                else:
                    errors.append(symbol_position)
        if errors or stack:
            errors.extend([s[0] for s in stack])
            self.get_message("Unbalanced brackets", sorted(errors))
            raise ValidataionError(self._message, idx=sorted(errors))

    def is_alphanumeric(self):
        pass

    def get_message(self, base, error_details):
        res = (', '.join(f"at {error}" for error in error_details))
        self._message = f"{base}: {res}"

    def mark_error(self, indexes):
        marks = ['^' if i in indexes else ' ' for i in range(len(self._text))]
        return f"{self._text}\n{''.join(marks)}"

    def validate(self, text):
        self._text = text
        try:
            self.is_balanced()
            # self.is_alphanumeric()
        except ValidataionError as err:
            print(self.mark_error(err.idx), file=sys.stderr)
            raise err
        return True


if __name__ == "__main__":
    input_text = '}<div><p>{ test }}</p</div>'
    validator = StringValidation()
    if validator.validate(text=input_text):
        print(input_text)
