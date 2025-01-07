class PObject:
    name = None

    def __init__(self,name):
        self.name=name
        print("哈哈哈")


if __name__ == '__main__':
    instance = PObject("1")
    print(F"show:{instance}")
    print(F"field:{instance.name}")
    instance1 = PObject("2")
    print(F"field2:{instance1.name}")
    print(F"instance:{instance.name}")
    print(F"class:{PObject.name}")