init -10 python:
    shock.audio.ui_hover = None
    shock.audio.ui_click = None
    shock.audio.say_click = None # sound when advancing dialogue

    shock.anims.nav_hover = null_transform # applied to all navigation_menu items at all times
    shock.anims.nav_frame_show = ex_nav_popout # used when showing the navigation_menu
    shock.anims.nav_item_show = ex_nav_item_popout # used for all elements in the navigation menu
    # must take 1 argument, which is the index of the item in the currently valid menu items

    # aside: the background for the navigation menu stored alongside main_menu_background
    #        and game_menu_background in gui.rpy

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
    shock.menu.use_split_main_menu = False
    # split main menu: does not use navigation() screen
    shock.menu.show_quick_key_hints = True
    # quick key hints: symbols showing keyboard shortcuts/controller inputs
    #                  for the textbuttons on quick_menu


init offset = -99
transform ex_nav_popout():
    ## The `on show` event occurs when the screen is first shown.
    on show:
        ## Align it off-screen at the left. Note that no y information is
        ## given, as that is handled on the popup screen.
        xpos 0.0 xanchor 1.0
        ## Ease it on-screen
        parallel:
            easein 0.2 xpos 0.0 xanchor 0.0
        parallel:
            easein 0.15 xzoom 1.15
            easeout 0.05 xzoom 1.0
    ## The `on hide` event occurs when the screen is hidden.
    on hide:
        ## Ease it off-screen again.
        easeout_back 0.25 xpos 0.0 xanchor 1.0

transform ex_nav_item_popout(index):
    xpos -0.5 xanchor 1.0
    0.05 * index + 0.1
    easein 0.1 xpos 0.0 xanchor 0.0
