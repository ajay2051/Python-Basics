import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


@dataclass(frozen=False)
class Person:
    name: str
    address: str
    active: bool = True
    email_address: list[str] = field(default_factory=list)
    # id: str = field(init=False, default_factory=generate_id) Adding init=False doesnot initialize id
    id: str = field(default_factory=generate_id)
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._search_string = f"{self.name} {self.address}"


def main() -> None:
    person = Person(
        name="ajay",
        address="ktm",
    )
    print(person)
    print(person._search_string)
    print(person.__dict__["address"])


if __name__ == "__main__":
    main()
