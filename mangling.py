class A:
    __count = 0  # Becomes _A__count

    def get_count(self):
        return self.__count
    
    def set_count(self, count):
        self.__count = count



class Widget:
    __count = 0

    def __init__(self) -> None:
        super().__init__()
        self.__count = Widget.__count
        Widget.__count += 1

    @property
    def widget_id(self):
        return self.__count
    

    @staticmethod
    def total_widgets_created(self):
        return Widget.__count

   
class Button(Widget):
    def __init__(self) -> None:
        super().__init__()
        self.__count = 0

    def click(self):
        self.__count += 1

    def total_clicks(self):
        return self.__count
    
