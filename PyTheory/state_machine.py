import copy

class base_state:
    def __init__(self):
        pass
    def enter(self):
        pass
    def update(self, dt):
        pass
    def render(self):
        pass
    def exit(self):
        pass

class state_machine:

    def __init__(self, states=None):
        self.empty = base_state()
        if states != None:
            self.states = states
        else:
            self.states = {}
        self.current = self.empty

    def change(self, state_name, enter_args):
        if state_name in self.states == False:
            return False
        self.current.exit()
        self.current = self.states[state_name]()
        self.current.enter(enter_args)
        return True

    def update(self, dt):
        self.current.update(dt)

    def render(self):
        self.current.render()

def main():
    gameStateMachine = state_machine( {
        "base": base_state
    } )
    print(gameStateMachine)

if __name__ == "__main__":
    main()

 