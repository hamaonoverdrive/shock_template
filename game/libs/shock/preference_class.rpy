init offset = -200

init python:
    class PreferencesStorage:
        def __init__(self, defaults = None):
            self.defaults = defaults

        def get(self, attr):
            if hasattr(self, attr):
                return getattr(self, attr)
            else:
                match self.defaults:
                    case "animation":
                        return null_transform
                    case _:
                        return None

    shock = PreferencesStorage()
    shock.audio = PreferencesStorage()
    shock.anims = PreferencesStorage("animation")
    shock.nvl = PreferencesStorage()
    shock.menu = PreferencesStorage()

transform null_transform(arg0=None, arg1=None, arg2=None):
    # this is STUPID but renpy won't let me use *args
    on idle:
        matrixcolor IdentityMatrix()
