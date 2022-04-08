"""Quiz practice."""


class Pond:
    ducks: list[str]
    slices_left: int

    def __init__(self, duck_list: list[str], bread: int):
        "Create a pond object."
        self.ducks = duck_list
        self.slices_left = bread

    def add_bread(self, slices: int) -> None:
        self.slices_left += slices

    def feeding(self) -> None:
        for duck in self.ducks:
            if self.slices_left >= 2:
                self.slices_left -= 2
            else:
                print(f"{duck} didn't get fed!")
        