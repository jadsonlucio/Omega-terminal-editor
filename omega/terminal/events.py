EVENTS_CODES = {
    30 : "key_pressed",
    31 : "cursor_move",
    40 : "exit",
}

class Event():
    def __init__(self, event_type, global_event = False, **kwargs):
        self.type = event_type
        self.global_event = global_event

        for key,value in kwargs.items():
            self.__setattr__(key, value)

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, event_type):
        if isinstance(event_type, str):
            for code,name in EVENTS_CODES.items():
                if name == event_type:
                    self._type = code
                    break
            else:
                raise Exception(f"Event of name {event_type} not found")
        else:
            if event_type in EVENTS_CODES:
                self._type = event_type
            else:
                raise Exception(f"Event of code {event_type} not found")

class Events:
 
    def __init__(self):
        pass

    def key_pressed(self, event):
        pass

    def cursor_move(self, event):
        pass

    def exit(self, event):
        pass

    def event_call(self, event):
        if event.type in EVENTS_CODES:
            self.__getattribute__(EVENTS_CODES[event.type])(event)
