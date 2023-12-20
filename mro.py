# class Root:
#     def f(self):
#         print("Root.f", self)

# class A(Root):
#     pass

# class B(A):
#     def f(self):
#         print("B.f", self)
#         super().f()

# b = B()
# b.f()


# class Root:
#     def f(self):
#         print('Root.f')


# class A(Root):
#     def f(self):
#         print("A.f", )


# class B(A):
#     def f(self):
#         print("B.f", )
#         super().f()

# b = B()
# b.f()


class Root:
    def f(self):
        print("root")


class A(Root):
    def f(self):
        print('A')
        super().f()


class B(Root):
    def f(self):
        print("B")


class C(A, B):
    def f(self):
        print("A, B")
        super().f()


c = C()
c.f()


class Root:
    def f(self):
        print("root")


class A(Root):
    def f(self):
        print('A')
        super().f()


class B(Root):
    def f(self):
        print("B")
        super().f()  # Super means next in line not the parent class


class C(A, B):
    def f(self):
        print("A, B")
        super().f()


c = C()
c.f()


class Root:
    f = "root"


class A(Root):
    fx = "A"


class B(Root):
    fx = 'B'


class C(A, B):
    fx = "C"


print(C.__mro__)
print([c.__name__ for c in C.__mro__])


class Root:
    def f(self):
        print("root")


class A(Root):
    def f(self):
        pass


class B(Root):
    def f(self):
        print("B")


class C(A, B):
    def f(self):
        print("A, B")
        super().f()


c = C()
c.f()


class Root:
    def f(self):
        print("root")


class A(Root):
    def f(self):
        print('A')
        super().f()


class B(Root):
    def f(self):
        pass


class C(A, B):
    def f(self):
        print("A, B")
        super().f()


c = C()
c.f()
