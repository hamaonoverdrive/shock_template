init offset = -200

init python:
    class PreferencesStorage:
        def __init__(self, animation = False):
            self.animation = True

        def get(self, attr):
            if hasattr(self, attr):
                return getattr(self, attr)
            else:
                if not self.animation:
                    return None
                else:
                    return null_transform

    shock = PreferencesStorage()
    shock.audio = PreferencesStorage()
    shock.anims = PreferencesStorage(True)
    shock.nvl = PreferencesStorage()

transform null_transform(arg0=None, arg1=None, arg2=None):
    # this is STUPID but renpy won't let me use *args
    on idle:
        matrixcolor IdentityMatrix()
