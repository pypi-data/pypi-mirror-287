from dataclasses import dataclass


@dataclass
class Nil2_: ...


Nil2 = Nil2_()


@dataclass
class Cons2[A]:
    head: A
    tail: "Cons2[A]"

    def __repr__(self):
        return f"Cons({self.head}, {self.tail})"
