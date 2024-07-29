"""
A Lisp/ML/Scala style singly linked list ("cons list")
"""

from abc import abstractmethod, ABC
from dataclasses import dataclass, field
from typing import Callable, Iterable, Tuple
from typing import TypeVar


A = TypeVar("A")

type _CList = "CList[A]"


class CList[A](ABC):

    @abstractmethod
    def append(self, other: _CList) -> _CList: ...

    @abstractmethod
    def fold_right[B](self, acc: B, f: Callable[[A, B], B]) -> B: ...

    @abstractmethod
    def fold_left[B](self, acc: B, f: Callable[[B, A], B]) -> B: ...

    @abstractmethod
    def drop(self, n: int) -> _CList: ...

    @abstractmethod
    def drop_while(self, f: Callable[[A], bool]) -> _CList: ...

    @abstractmethod
    def take(self, n: int) -> _CList: ...

    @abstractmethod
    def take_while(self, f: Callable[[A], bool]) -> _CList: ...

    @abstractmethod
    def split_at(self, i: int) -> Tuple[_CList, _CList]: ...

    def partition(self, f: Callable[[A], bool]) -> Tuple[_CList, _CList]:
        accum = lambda a, x: (a << x[0], x[1]) if f(a) else (x[0], a << x[1])
        return self.fold_right((Nil(), Nil()), accum)

    def length(self) -> int:
        return self.fold_right(0, lambda _, acc: acc + 1)

    def prepend(self, new_head: A) -> _CList:
        return Cons(new_head, self)

    def reversed(self) -> _CList:
        return self.fold_left(Nil(), lambda acc, h: Cons(h, acc))

    def map[B](self, f: Callable[[A], B]) -> "CList[B]":
        return self.fold_right(Nil(), lambda a, acc: Cons(f(a), acc))

    def filter[A](self, f: Callable[[A], bool]) -> _CList:
        return self.fold_right(Nil(), lambda a, acc: Cons(a, acc) if f(a) else acc)

    def flatten(self) -> _CList:
        return CList.flatten_(self)

    def flat_map[B](self, f: Callable[[A], "CList[B]"]) -> "CList[B]":
        return self.map(f).flatten()

    def bind[B](self, f: Callable[[A], "CList[B]"]) -> "CList[B]":
        return self.map(f).flatten()

    def sorted(self, cmp: Callable[[A, A], int]) -> _CList:
        def merge(left: _CList, right: _CList) -> _CList:
            match left, right:
                case Nil(), r:
                    return r
                case l, Nil():
                    return l
                case Cons(lh, lt), Cons(rh, rt):
                    if cmp(lh, rh) <= 0:
                        return lh << merge(lt, right)
                    return rh << merge(left, rt)
                case _:
                    return Nil()

        length = len(self)
        if length <= 1:
            return self
        left, right = self.split_at(length // 2)
        return merge(left.sorted(cmp), right.sorted(cmp))

    @staticmethod
    def flatten_(lst: "CList[CList[A]]") -> _CList:
        def concat(left, right):
            match left:
                case Nil():
                    return right
                case Cons(h, t):
                    return Cons(h, concat(t, right))

        def flatten(lst: "CList[CList[A]]") -> "CList[A]":
            match lst:
                case Nil():
                    return Nil()
                case Cons(h, t):
                    match h:
                        case Cons(_, _):
                            return concat(flatten(h), flatten(t))
                        case _:
                            return Cons(h, flatten(t))

        return flatten(lst)

    @staticmethod
    def cons(a: A) -> _CList:
        return Cons(a)

    @staticmethod
    def empty() -> _CList:
        return Nil()

    @staticmethod
    def new(*xs: A) -> _CList:
        return Cons(xs[0], CList.new(*xs[1:])) if xs else Nil()

    @staticmethod
    def from_iterable[A](iterable: Iterable[A]) -> _CList:
        return CList.new(*iterable)

    def __rlshift__(self, other) -> _CList:
        return self.prepend(other)

    def __add__(self, other) -> _CList:
        return self.append(other)

    def __len__(self) -> int:
        return self.fold_right(0, lambda _, acc: acc + 1)

    def __iter__(self):
        current = self
        while isinstance(current, Cons):
            yield current.head
            current = current.tail

    def __eq__(self, other) -> bool:
        match self, other:
            case Cons(sh, st), Cons(oh, ot):
                return sh == oh and st == ot
            case Nil(), Nil():
                return True
            case _:
                return False


class Nil(CList):

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Nil, cls).__new__(cls)
        return cls._instance

    def __repr__(self):
        return "Nil()"

    def append(self, other: _CList) -> _CList:
        return other

    def fold_right[A, B](self, acc: B, f: Callable[[A, B], B]) -> B:
        return acc

    def fold_left[A, B](self, acc: B, f: Callable[[B, A], B]) -> B:
        return acc

    def drop(self, n: int) -> _CList:
        return self

    def drop_while[A](self, f: Callable[[A], bool]) -> _CList:
        return self

    def take(self, n: int) -> _CList:
        return self

    def take_while[A](self, f: Callable[[A], bool]) -> _CList:
        return self

    def split_at(self, i: int) -> Tuple[_CList, _CList]:
        return self, self


@dataclass(frozen=True)
class Cons[A](CList[A]):
    head: A
    tail: CList[A] = field(default_factory=Nil)

    def __repr__(self):
        match self.tail:
            case Nil():
                return f"Cons({self.head})"
        return f"Cons({self.head}, {self.tail})"

    def append(self, other: _CList) -> _CList:
        return Cons(self.head, self.tail.append(other))

    def fold_right[B](self, acc: B, f: Callable[[A, B], B]) -> B:
        return f(self.head, self.tail.fold_right(acc, f))

    def fold_left[B](self, acc: B, f: Callable[[B, A], B]) -> B:
        return self.tail.fold_left(f(acc, self.head), f)

    def drop(self, n: int) -> _CList:
        return self if n <= 0 else self.tail.drop(n - 1)

    def drop_while(self, f: Callable[[A], bool]) -> _CList:
        return self if not f(self.head) else self.tail.drop_while(f)

    def take(self, n: int) -> _CList:
        return Cons(self.head) if n <= 1 else self.head << self.tail.take(n - 1)

    def take_while(self, f: Callable[[A], bool]) -> _CList:
        return self.head << self.tail.take_while(f) if f(self.head) else Nil()

    def split_at(self, i: int) -> Tuple[_CList, _CList]:
        return self.take(i), self.drop(i)
