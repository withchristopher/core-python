""" Model for aircraft flights."""


class Flight:

    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError (f"Invalid route number '{number}'")

        self._number = number


    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]


class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registrstion = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registrstion

    def model(self):
        return self._registrstion

    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                "ABCDEFGHIJK"[:self._num_seats_per_row])

