class ConvertError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class InMemoryAutocommitError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class InMemoryBackupError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class WrongLockTypeError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class BadPathError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class WrongValueTypeError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)