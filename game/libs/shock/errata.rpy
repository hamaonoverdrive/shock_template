default no_hover = False
define click_time = 0.1
screen hover_cooldown(time):
    timer time action SetVariable("no_hover", False)
    timer time + 0.01 action Hide("hover_cooldown")

init python:
    # registring channels
    renpy.music.register_channel(name='adv', mixer='sfx')

    def fix_focus(f):
        from functools import wraps
        @wraps(f)
        def wrapper(*args, **kwargs):
            global no_hover
            if no_hover:
                args = (args[0], True)
            return f(*args, **kwargs)
        return wrapper

    def fix_click():
        global click_time, no_hover
        no_hover = True
        renpy.show_screen("hover_cooldown", time=click_time)

    renpy.display.displayable.Displayable.focus = fix_focus(renpy.display.displayable.Displayable.focus)

    def play_advance_sound():
        renpy.music.play(shock.audio.get("say_click"), channel='adv', loop=False)
        return True

    def get_non_linear_volume(mixer):
        import math

        value = Preference(mixer).get_volume()
        if value > 0:
            if config.quadratic_volumes:
                value = math.sqrt(value)
            else:
                value = math.log10(value) * 20 + config.volume_db_range
        else:
            value = 0

        return value * 100/40

    # used for navigation screen
    class MenuItem:
        def __init__(self, name, action=ShowMenu, args=[], kwargs={}, valid="True"):
            self.name = name
            self.action = action
            self.args = args
            self.kwargs = kwargs
            self.valid = valid

define config.say_allow_dismiss = play_advance_sound
