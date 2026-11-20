init -99 python:
    shock.audio.ui_hover = None
    shock.audio.ui_click = None
    shock.audio.say_click = None # sound when advancing dialogue

    shock.anims.nav_hover = null_transform # replace with name of transform

    shock.nvl.scrolling = True
    shock.nvl.scrollbars = "vertical" # None to remove scrollbar
    shock.nvl.scrollbars_mousewheel = True

    shock.menu.use_null_menu = True
    # null menu: opened when hitting escape
    #            reccomend enabled for controller support
    #            defaults to "save" screen if unset/False
    shock.menu.use_split_history = True
    # split history: fullscreen history window
    #                notably, doesn't show in navigation menu
    #                defaults to renpy default history screen if unset/False
    shock.menu.use_split_main_menu = True
    # split main menu: does not use navigation() screen
