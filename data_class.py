# from functools import total_ordering


# @total_ordering
# class MaualComment:
#     def __init__(self, id: int, text: str):
#         self.__id: int = id
#         self.__text: str = text

#     @property
#     def id(self):
#         return self.__id

#     @property
#     def text(self):
#         return self.__text

#     def __repr__(self):
#         return "{}(id={}, text={})".format(
#             self.__class__.__name__, self.__id, self.__text
#         )

#     def __eq__(self, other):
#         if other.__class__ is self.__class__:
#             return (self.__id, self.__text) == (other.__id, other.__text)
#         else:
#             return NotImplemented

#     def __ne__(self, other):
#         result = self.__eq__(other)
#         if result is NotImplemented:
#             return NotImplemented
#         else:
#             return not result

#     def __hash__(self) -> int:
#         return hash(self.__class__, self.__id, self.__text)

#     def __lt__(self, other):
#         if other.__class__ is self.__class__:
#             return (self.__id, self.__text) < (other.__id, other.__text)
#         else:
#             return NotImplemented

#     def __le__(self, other):
#         if other.__class__ is self.__class__:
#             return (self.__id, self.__text) <= (other.__id, other.__text)
#         else:
#             return NotImplemented

#     def __gt__(self, other):
#         if other.__class__ is self.__class__:
#             return (self.__id, self.__text) > (other.__id, other.__text)
#         else:
#             return NotImplemented

#     def __ge__(self, other):
#         if other.__class__ is self.__class__:
#             return (self.__id, self.__text) >= (other.__id, other.__text)
#         else:
#             return NotImplemented


import dataclasses
import inspect
from dataclasses import dataclass, field
from pprint import pprint
from typing import List


@dataclass(
    frozen=True, order=True
)  # frozen=True adds hash function which makes data immutable
# attr.s(frozen=True, order=True, slots=True)
class Comment:
    id: int = field()
    # id: int = attr.ib(validator=attr.validators.instance_of(int))
    text: str = field(default=" ")  # Default value
    # text: str = attr.ib(default = "", converter=str)
    replies = List[int] = field(
        default_factory=List, compare=False, hash=False, repr=False
    )
    #  replies : List[int] = attr.ib(factory=List, compare=False, hash=False, repr=False)


def main():
    comment = Comment(1, "This is first comment")

    print(dataclasses.replace(comment, id=3))  # Change id = 3
    print(comment)
    # print(astuple(comment))
    # print(asdict(comment))
    pprint(inspect.getmembers(Comment, inspect.isfunction))


if __name__ == "__main__":
    main()
