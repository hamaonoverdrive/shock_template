################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language
    
style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")
    activate_sound shock.audio.get("ui_click")
    hover_sound shock.audio.get("ui_hover")

style image_button:
    activate_sound shock.audio.get("ui_click")
    hover_sound shock.audio.get("ui_hover")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            style "quick_menu"

            if pad_config.is_using_mouse() or not shock.menu.get("show_quick_key_hints"):
                textbutton _("Back") action Rollback()
                textbutton _("History") action ShowMenu('history')
                textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _("Auto") action Preference("auto-forward", "toggle")
                #textbutton _("Save") action ShowMenu('save')
                # ^ seems redundant with menu button imo
                #textbutton _("Q.Save") action QuickSave()
                #textbutton _("Q.Load") action QuickLoad()
                # ^ no one uses these
                textbutton _("Menu") action ShowMenu()
            else:
                icon_button pad_event "rollback" caption _("Back"):
                    action Rollback() suffix "small" mkb_icon "key_pgup"
                icon_button pad_event "history" key_event ["L", "l"] caption _("History"):
                    action ShowMenu('history') suffix "small" mkb_icon "key_l"
                icon_button pad_event "toggle_skip" caption _("Skip"):
                    action Skip() suffix "small" mkb_icon "key_tab"
                icon_button pad_event "toggle_afm" caption _("Auto"):
                    action Preference("auto-forward", "toggle") suffix "small" mkb_icon "key_a"
                    selected preferences.afm_enable
                #icon_button pad_event "game_save" caption _("Save"):
                #    action ShowMenu("save") suffix "small" mkb_icon "key_z"
                icon_button pad_event "game_menu" caption _("Menu"):
                    action ShowMenu() suffix "small" mkb_icon "key_escape"

        key "a" action Preference("auto-forward", "toggle")
        key "z" action ShowMenu("saves")
        key "l" action ShowMenu("history")

        ## Ensures this screen is updated for input type changes
        add game_menu_listener


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is button
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")

style quick_icon_button is quick_button
style quick_icon_button_text is quick_button_text

################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation(can_focus=True, show_return=True, show_item_anim=True):

    default menu_items = [
        MenuItem("Start", Start,
                 valid="main_menu"),
        MenuItem("History", args=["history"], 
                 valid="not main_menu and not shock.menu.get('use_split_history')"),
        MenuItem("Saves", args=["saves"]),
        MenuItem("Preferences", args=["preferences"]),
        MenuItem("End Replay", EndReplay, kwargs={"confirm":True}, 
                 valid="_in_replay"),
        MenuItem("Main Menu", MainMenu,
                 valid="not _in_replay and not main_menu"),
        MenuItem("About", args=["about"]),
        MenuItem("Controls", args=["help"],
                 valid='renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile"))'),
        MenuItem("Quit", Quit, kwargs={"confirm":True},
                 valid="renpy.variant('pc')")
    ]

    frame:
        background gui.navigation_menu_background
        yfill True
        at shock.anims.get("nav_frame_show")
        vbox:
            style_prefix "navigation"

            xpos gui.navigation_xpos
            yalign 0.5

            spacing gui.navigation_spacing

            $ offset = 0
            for i in range(len(menu_items)):
                $ item = menu_items[i]
                if eval(item.valid):
                    textbutton _(item.name):
                        action [item.action(*item.args, **item.kwargs), Function(fix_click)]
                        default_focus i + offset == 0 and can_focus
                        keyboard_focus can_focus or not shock.menu.get("use_null_menu")
                        sensitive can_focus or pad_config.is_using_mouse() or not shock.menu.get("use_null_menu")
                        id item.name
                        if show_item_anim:
                            at shock.anims.get("nav_hover"), shock.anims.get("nav_item_show")(i + offset)
                        else:
                            at shock.anims.get("nav_hover")
                else:
                   $  offset -= 1

        if show_return:
            textbutton _("Return"):
                style "return_button"
                yalign 1.0
                keyboard_focus can_focus or not shock.menu.get("use_null_menu")
                sensitive can_focus or pad_config.is_using_mouse() or not shock.menu.get("use_null_menu")

                action Return()
                if show_item_anim:
                    at shock.anims.get("nav_hover"), shock.anims.get("nav_item_show")(len(menu_items) + offset)
                else:
                    at shock.anims.get("nav_hover")



style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    if shock.menu.get("use_split_main_menu"):
        ## This empty frame darkens the main menu.
        frame:
            style "main_menu_frame"

        vbox:
            yalign 0.5
            textbutton _("Start") action Start() id "start" at shock.anims.get("nav_hover")
            textbutton _("Preferences") action ShowMenu("preferences") id "prefs" at shock.anims.get("nav_hover")
            textbutton _("About") action ShowMenu("about") id "about" at shock.anims.get("nav_hover")
            textbutton _("Controls") action ShowMenu("help") id "controls" at shock.anims.get("nav_hover")
            if renpy.variant("pc"):
                textbutton _("Quit") action Quit(confirm=False) id "pc" at shock.anims.get("nav_hover")
    else:
        use navigation(show_return=False, show_item_anim=False)

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0, can_focus=True, show_footer=True):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    side 'c r':
                        controller_viewport:
                            id "game_menu_vp"
                            vscroll_style "center"
                            draggable renpy.variant("touch")
                            yinitial yinitial
                            scrollbars "vertical"
                            mousewheel True
                            pagekeys True
                            arrowkeys "not sticks"

                            spacing spacing

                            transclude
                        vbar value YScrollValue("game_menu_vp"):
                            keyboard_focus False
                            unscrollable "hide"

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation(can_focus=False, show_item_anim=False)

    #label title
    truncate_text title:
        style "game_menu_label"
        reset_size_on_overflow True
        xsize gui.navigation_width - gui.navigation_xpos * 2 - 10
        shrink_to_fit gui.text_size # smallest allowed font size

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

    ## Show the footer button icons
    if show_footer:
        use key_footer():
            use game_menu_footer_buttons

    ## Ensures this screen is updated for input type changes
    add game_menu_listener

screen game_menu_footer_buttons():
    if shock.menu.get("use_null_menu") and not pad_config.is_using_mouse():
        $ return_action = ShowMenu("null_menu", show_item_anim=False)
    else:
        $ return_action = Return()
    icon_button kind icn.menu_return suffix "small" action return_action
    icon_button kind icn.select suffix "small"

screen null_menu(show_item_anim=True):

    tag menu

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background

    use navigation(show_item_anim=show_item_anim)

    key "game_menu" action Return()


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_navigation_frame:
    xsize gui.navigation_width
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos gui.navigation_xpos
    ysize 180

style game_menu_label_text:
    size 75
    color gui.accent_color
    yalign 0.5

style return_button:
    xoffset gui.navigation_xpos
    yalign 1.0
    yoffset -45
default focus_level = 0
screen tabbed_menu(my_pages, page_expression, use_cursor=False, arrowkeys=None):
    default pages = [page for page in my_pages.keys()]
    default titles = [title for title in my_pages.values()]

    default f1 = FocusDisplayable(gui.preferences_selector_frame,
        hide_on_mouse=True, padding=gui.preferences_selector_frame_padding,
        active_area=(350, 200, config.screen_width-350, config.screen_height-200))

    default yadjustor = ui.adjustment()

    fixed:
        style_prefix 'tabbed_common'
        hbox:
            ## The icon shortcut to change pages
            icon_button caption _("Previous Page") kind icn.page_left:
                action [IncrementVariable("focus_level", 15), CycleScreenVariable("page", pages, reverse=True), Function(yadjustor.change, 0)]
                icon_only True
            ## Buttons to change pages; can be clicked with the mouse, but
            ## not focused with arrow keys
            for page_id, title in my_pages.items():
                textbutton title keyboard_focus False:
                    action [IncrementVariable("focus_level", 15), SetScreenVariable("page", page_id), Function(yadjustor.change, 0)]

            ## The icon shortcut to change pages
            icon_button caption _("Next Page") kind icn.page_right:
                action [IncrementVariable("focus_level", 15), CycleScreenVariable("page", pages), Function(yadjustor.change, 0)]
                icon_only True

    ## A container for all preference screens reusing this one
    frame:
        right_margin 70 bottom_margin 200
        xsize config.screen_width-350-70
        ysize config.screen_height-220 padding (20, 20)
        style_prefix 'tabbed_common' align (1.0, 1.0)
        has fixed
        xsize None ysize None
        yfill False

        side 'c r':
            style_prefix 'tabbed'
            ## This uses the controller viewport to be navigable via keyboard
            ## or controller.
            controller_viewport:
                id 'tab_vp'
                ## needed to force this back to the top when we change tabs
                yadjustment yadjustor
                ## The scroll style tries to keep the focused item in the center
                ## It also takes the focus_displayable earlier to better animate
                ## it while the viewport is scrolling.
                vscroll_style "center" 
                if use_cursor:
                    focus_displayables f1
                ## How long to animate the scroll movement (horizontally, vertically)
                scroll_delay (0.1, 0.1)
                ## This ensures the penalty for items that are up and left/right
                ## from the currently selected item aren't penalized too harshly
                ## for it, since we generally want to select the row above/below
                ## the current one.
                penalty 24
                ## If the viewport can be dragged, it tends to grab focus when
                ## using the arrow keys or controller to navigate, which
                ## is undesirable unless the user has a touch device.
                mousewheel True draggable renpy.variant("touch")
                if arrowkeys is not None:
                    arrowkeys arrowkeys
                has vbox

                use expression page_expression

            ## A scrollbar for mouse or touch users; keyboard_focus is False
            ## so it can't be navigated to with the arrow keys or controller.
            vbar value YScrollValue("tab_vp"):
                unscrollable "hide"
                keyboard_focus False
                default_focus False

    $ tooltip = GetTooltip()
    if tooltip:
        fixed:
            xsize config.screen_width-350-70 xalign 1.0 style 'default'
            ycenter 0.88
            text tooltip style 'tabbed_tooltip'

        hbox:
            style_prefix "slider"
            box_wrap True

    if use_cursor:
        add f1

style tabbed_label is pref_label
style tabbed_label_text is pref_label_text
style tabbed_side is pref_side
style tabbed_label is pref_label
style tabbed_label_text is pref_label_text
style tabbed_hbox is pref_hbox
style tabbed_vbox is pref_vbox
style tabbed_bar is pref_bar
style tabbed_text is pref_text

style tabbed_common_window:
    xsize config.screen_width-(gui.navigation_width + gui.navigation_xpos)

style tabbed_common_fixed:
    xsize config.screen_width-(gui.navigation_width + gui.navigation_xpos)
    yfill True
    align (1.0, 1.0)

style tabbed_common_hbox:
    spacing 65
    xalign 0.5
    xoffset -gui.navigation_xpos
    ypos 0.05

style tabbed_common_button:
    size_group 'pref_tabs' yalign 0.5

style tabbed_common_button_text:
    text_align 0.5 xalign 0.5 yalign 0.5

style tabbed_tooltip:
    xalign 0.5 yalign 0.5
    text_align 0.5 xmaximum 1200
    outlines [(2, "#000")] color "#FFF"
    layout "subtitle"

## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen saves():
    tag menu

    default f1 = FocusDisplayable(gui.preferences_selector_frame,
        hide_on_mouse=True, padding=gui.preferences_selector_frame_padding,
        active_area=(350, 200, config.screen_width-350, config.screen_height-200))

    use game_menu(_("Saves"), show_footer=False):

        style_prefix "save"
        default max_pages = 6 # feel free to increase just readjust space accordingly

        fixed:
            style_prefix 'tabbed_common'
            vbox:
                xfill True
                hbox:
                    # navbar for pages, stealing some formatting from tabbed_menu
                    icon_button caption _("Previous Page") kind icn.page_left:
                        action FilePagePrevious(wrap=True, max=max_pages)
                        icon_only True

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto") keyboard_focus False

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick") keyboard_focus False

                    ## range(1, 10) gives the numbers from 1 to max_pages.
                    for page in range(1, max_pages+1):
                        textbutton "[page]" action FilePage(page) keyboard_focus False

                    icon_button caption _("Next Page") kind icn.page_right:
                        action FilePageNext(wrap=True, max=max_pages)
                        icon_only True
                null height 20
                # the actual save slots
                hbox:
                    yalign 0.5
                    $ columns = 3
                    $ rows = 2

                    # Display a grid of file slots.

                    grid columns rows:
                        transpose False
                        style_group "file_picker"
                        spacing 5

                        # Display ten file slots, numbered 1 - 10.
                        for i in range(1, columns * rows + 1):

                            # Each file slot is a button.
                            button: #note that if you put ANY IMAGE in the following, it will add and stretch the bg. Trust me, I tried lol
                                keyboard_focus False
                                action FileLoad(i)
                                has vbox
                                null width 5
                                use file_butt
                            # OKAY THIS IS REALLY SILLY IN HOW THIS WORKS:
                            # So the background for the file slots is actually a button! The reason why it's a button is because the FileSave, FileLoad, and FileAction functions have a feature to show which save file is the newest. The button will be marked as *selected* if it is the newest, so the images used for ‘selected_background’ and ‘selected_hover_background’ are used to denote that it’s the newest file. I didnt assign a ‘selected_’ function to the save and load buttons specifically because it looks weird and doesn't clearly signal to the player that it's the newest save.
                            # Because of this though, that means the background of the save file is hoverable and clickable. I have it set so that it loads because I figured a locked file would still be able to load, just not delete or save over.

    add f1

    use key_footer():
        hbox:
            icon_button:
                kind icn.reset
                caption _("Sync")
                action Show("choices",
                            config.enter_yesno_transition, # transition
                            "Select Sync Mode",
                            {
                                "Upload": UploadSync(),
                                "Download": DownloadSync()
                            })
                suffix "small"
            use game_menu_footer_buttons

#This screen has all the info of the save/load
screen file_butt:
    frame:

        has vbox
        style_group "saveload"

        xfit True
        yfit True

        #adds the screenshot
        add FileScreenshot(i) xalign .5

        #adds the time whe the player saves their file
        $ file_time = FileTime(i, format=u'%b %d %Y, %I:%M %p', empty=_("Empty Slot"))

        text "[file_time]" xalign .5 style "file_picker_text"

        null height 2

        #This adds the name of the file, which is a number
        $ file_name = FileSlotName(i, columns * rows)

        # use the player-renameable save if this isn't auto/quick
        if str(file_name)[0].isdigit():
            default page_name_value = FilePageNameInputValue(pattern=_("Save {}"),  page=file_name)
            ## The page name, which can be edited by clicking on a button.
            button:

                key_events True
                keyboard_focus False
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    value page_name_value
                    pixel_width config.thumbnail_width
        else:
            # otherwise, just a text field
            button:
                text file_name.replace("a", "Auto ").replace("q", "Quick ")

        null height 10
        hbox:
            xsize config.thumbnail_width
            #SAVE BUTTON#
            textbutton _("Save") action FileSave(i, confirm=True, page=None) xalign .5:
                default_focus 3 * (6 - (i-1)%6)

            #LOAD BUTTON#
            #Not much to do here. Load is always showing and intereactable even if the save is locked.
            textbutton _("Load") action FileLoad(i, confirm=True, page=None) xalign .5:
                default_focus 2 * (6 - (i-1)%6)

            #DELETE BUTTON#
            #same as before in save~
            textbutton _("Delete") action FileDelete(i, confirm=True, page=None) xalign .5:
                default_focus (6 - (i-1)%5)

style file_picker_button is frame:
    selected_background gui.preferences_selector_frame

style file_picker_frame:
    background None

style file_picker_text:
    size 25

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")

style saveload_button is page_label
style saveload_input is page_label_text
style saveload_text is page_label_text


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences


screen preferences():

    default page = "pref_display"

    tag menu

    use game_menu(_("Preferences"), scroll="viewport")

    use tabbed_menu({
        "pref_display": _("Display\n& Gameplay"),
        "pref_audio": _("Audio"),
        "pref_controls": _("Controls"),
        "pref_accessibility": _("Accessibility")
    }, page, use_cursor=True)

    ## This is a special screen element like `key` which only triggers the
    ## provided action if the player is focused on the button with the provided
    ## ID. So, if the player is focused on the pick_icons button and hits
    ## focus_right, it will cycle to the next controller layout.
    focused_on "pick_icons" key "focus_left" action [Notify("left"), CycleControllerLayout(reverse=True)]
    focused_on "pick_icons" key "focus_right" action CycleControllerLayout(reverse=False)



screen pref_display():
    if renpy.variant("pc") or renpy.variant("web"):
        # Only need fullscreen/windowed on desktop and web builds
        hbox:
            style_prefix "radio"
            label _("Display")
            textbutton _("Window"):
                # Ensures this button is selected when
                # not in fullscreen.
                selected not preferences.fullscreen
                default_focus 10 + focus_level
                action Preference("display", "window")
                tooltip _("Display the game in a window")
            null width 50
            textbutton _("Fullscreen"):
                action Preference("display", "fullscreen")
                tooltip _("Display the game in fullscreen")

    hbox:
        style_prefix "radio"
        label _("Skip Unseen Text")
        textbutton _("ON"):
            default_focus 5 + focus_level
            action Preference("skip", "all")
            tooltip _("Skip all text, regardless of whether it's been seen before")
        null width 50
        textbutton _("OFF"):
            action Preference("skip", "seen")
            tooltip _("Only skip text that has been seen before")

    hbox:
        style_prefix "radio"
        label _("Skip After Choices")
        textbutton _("ON"):
            action Preference("after choices", "skip")
            tooltip _("Keep skipping after making a choice")
        null width 50
        textbutton _("OFF"):
            action Preference("after choices", "stop")
            tooltip _("Stop skipping upon reaching a choice")

    hbox:
        vbox:
            spacing 0
            label _("Text Speed")
            if preferences.text_cps != 0:
                if preferences.text_cps != 1:
                    text "[int(preferences.text_cps)] " + _("characters/second") xalign 1.0
                else:
                    text "[int(preferences.text_cps)] " + _("character/second") xalign 1.0
            else:
                text _("Instant") xalign 1.0
        text _("MIN")
        ## Controller bars will be automatically selected as soon
        ## as it's focused, unlike default bars which must be
        ## "clicked into"/out of.
        controller_bar value Preference("text speed") default_focus 2 + focus_level:
            tooltip _("Adjust the speed at which text is displayed")
        text _("MAX")

    hbox:
        label _("Auto-Forward Delay")
        text _("MIN")
        controller_bar value Preference("auto-forward time"):
            tooltip _("Adjust how long of a delay there is before text auto-advances")
        text _("MAX")

    hbox:
        style_prefix "radio"
        label _("Transitions")
        textbutton _("ON"):
            action Preference("transitions", "all")
            tooltip _("Transitions will play")
        null width 50
        textbutton _("OFF"):
            action Preference("transitions", "none")
            tooltip _("Transitions will not play")

screen pref_audio():
    if config.has_music or config.has_sound or config.has_voice:
        hbox:
            style_prefix "radio"
            label _("Mute All")
            textbutton _("MUTED") action Preference("all mute", "enable"):
                default_focus 10 + focus_level
                tooltip _("Mute all audio channels")
            null width 50
            textbutton _("NOT MUTED") action Preference("all mute", "disable"):
                tooltip _("Unmute all audio channels")

        hbox:
            vbox:
                spacing 0
                label _("Main Volume")
                text "[int(get_non_linear_volume('main volume'))]%" xalign 1.0
            text _("MIN")
            controller_bar value Preference("main volume"):
                tooltip _("Adjust the overall volume of the game")
            text _("MAX")

    if config.has_music:
        hbox:
            vbox:
                spacing 0
                label _("Music Volume")
                text "[int(get_non_linear_volume('music volume'))]%" xalign 1.0
            text _("MIN")
            controller_bar value Preference("music volume") default_focus 8 + focus_level:
                tooltip _("Adjust the volume of the music")
            text _("MAX")

    if config.has_sound:
        hbox:
            vbox:
                spacing 0
                label _("Sound Volume")
                text "[int(get_non_linear_volume('sound volume'))]%" xalign 1.0
            text _("MIN")
            controller_bar value Preference("sound volume") default_focus 6 + focus_level:
                tooltip _("Adjust the volume of sound effects")
            text _("MAX")
            if config.sample_sound:
                textbutton _("Test") action Play("sound", config.sample_sound)


    if config.has_voice:
        hbox:
            vbox:
                spacing 0
                label _("Voice Volume")
                text "[int(get_non_linear_volume('voice volume'))]%" xalign 1.0
            text _("MIN")
            controller_bar value Preference("voice volume") default_focus 4 + focus_level:
                tooltip _("Adjust the volume of voiceover")
            text _("MAX")
            if config.sample_voice:
                textbutton _("Test") action Play("voice", config.sample_voice)


screen pref_controls():
    hbox:
        style_prefix "radio" spacing 25
        label _("Icon Set")
        textbutton "←":
            ## These buttons aren't focusable, because a special
            ## action is set up below to make it so focusing
            ## the icon set and hitting left/right cycles the
            ## available options.
            style 'pref_arrow' keyboard_focus False
            action CycleControllerLayout(reverse=True)
        button:
            style 'default'
            id 'pick_icons'
            alt _("Choose a button icon set {}".format(pad_config.get_alt_text(["a", "b", "l1", "l2"], is_event=False, alt_tag=False)))
            tooltip _("Choose a button icon set")
            action NullAction() default_focus 15 + focus_level
            has hbox
            spacing 15 first_spacing 15
            add "pad_a"
            add "pad_b"
            add "pad_l1"
            add "pad_l2"
        textbutton "→":
            style 'pref_arrow' keyboard_focus False
            action CycleControllerLayout(reverse=False)


    hbox:
        style_prefix "radio"
        label _("Hold to Skip")
        textbutton _("ON") default_focus 10 + focus_level:
            action [SetField(persistent, "hold_to_skip", True),
                Function(pad_remap.update_keymap)]
            tooltip _("Hold down the skip button to skip text")
        null width 50
        textbutton _("OFF"):
            action [SetField(persistent, "hold_to_skip", False),
                Function(pad_remap.update_keymap)]
            tooltip _("Press the skip button to toggle skipping on and off again")

    ## If you have drag and drop functionality, you may
    ## want these options
    # hbox:
    #     style_prefix "radio"
    #     label _("Hold to Drag")
    #     textbutton _("ON"):
    #         action [SetField(persistent, "hold_to_drag", True),
    #             Function(pad_remap.update_keymap)]
    #         tooltip _("Hold down the drag button to drag around items")
    #     null width 50
    #     textbutton _("OFF"):
    #         action [SetField(persistent, "hold_to_drag", False),
    #             Function(pad_remap.update_keymap)]
    #         tooltip _("Press the drag button to toggle picking up and releasing a draggable item")

    hbox:
        style_prefix "radio"
        label _("Left stick x-axis")
        textbutton _("NORMAL"):
            ## SetStickInversion, StickDeadzoneAdjustment, and
            ## StickSensitivityAdjustment are all custom
            ## made actions and bar values.
            action SetStickInversion("left", "x", False)
        null width 50
        textbutton _("INVERTED"):
            action SetStickInversion("left", "x", True)

    hbox:
        style_prefix "radio"
        label _("Left stick y-axis")
        textbutton _("NORMAL"):
            action SetStickInversion("left", "y", False)
        null width 50
        textbutton _("INVERTED"):
            action SetStickInversion("left", "y", True)

    hbox:
        label _("Left stick dead zone")
        text _("MIN")
        controller_bar value StickDeadzoneAdjustment("left")
        text _("MAX")

    hbox:
        label _("Left stick sensitivity")
        text _("LOW")
        controller_bar value StickSensitivityAdjustment("left")
        text _("HIGH")

    hbox:
        style_prefix "radio"
        label _("Right stick x-axis")
        textbutton _("NORMAL"):
            action SetStickInversion("right", "x", False)
        null width 50
        textbutton _("INVERTED"):
            action SetStickInversion("right", "x", True)

    hbox:
        style_prefix "radio"
        label _("Right stick y-axis")
        textbutton _("NORMAL"):
            action SetStickInversion("right", "y", False)
        null width 50
        textbutton _("INVERTED"):
            action SetStickInversion("right", "y", True)

    hbox:
        label _("Right stick dead zone")
        text _("MIN")
        controller_bar value StickDeadzoneAdjustment("right")
        text _("MAX")

    hbox:
        label _("Right stick sensitivity")
        text _("LOW")
        controller_bar value StickSensitivityAdjustment("right")
        text _("HIGH")

style pref_arrow:
    is default
style pref_arrow_text:
    size 70 outlines [(2, "#000")] color "#FFF"
    xalign 0.5 yalign 0.5 prefer_emoji False
    hover_color gui.hover_color

screen pref_accessibility():
    hbox:
        style_prefix "radio"
        label _("Font Override")
        textbutton _("Default") default_focus 10 + focus_level:
            action Preference("font transform", None)
            tooltip _("Use the default font")
        null width 50
        textbutton _("DejaVu Sans"):
            action Preference("font transform", "dejavusans")
            tooltip _("Use the DejaVu Sans font")
    hbox:
        style_prefix 'radio'
        label ""
        textbutton _("Opendyslexic"):
            action Preference("font transform", "opendyslexic")
            tooltip _("Use the OpenDyslexic font")

    hbox:
        label _("Text Size Scaling")
        text _("MIN")
        controller_bar value Preference("font size"):
            tooltip _("Adjust the size of the text")
        text _("MAX")

    hbox:
        label _("Line Space Scaling")
        text _("MIN")
        controller_bar value Preference("font line spacing"):
            tooltip _("Adjust the space between lines of text")
        text _("MAX")

    hbox:
        style_prefix 'radio'
        label _("High Contrast Text")
        textbutton _("ON"):
            action Preference("high contrast text", "enable")
            tooltip _("Use high contrast text")
        null width 200
        textbutton _("OFF"):
            action Preference("high contrast text", "disable")
            tooltip _("Turn high contrast text off")

    hbox:
        style_prefix 'radio'
        label _("Self-Voicing")
        textbutton _("Text-to-speech"):
            action Preference("self voicing", "enable")
            tooltip _("Enable text-to-speech")
        null width 30
        textbutton _("Clipboard"):
            action Preference("clipboard voicing", "enable")
            tooltip _("Copy readable text to the clipboard, for use with external screen reader software")
    hbox:
        style_prefix 'radio'
        label ""
        textbutton _("Debug"):
            action Preference("debug voicing", "enable")
            tooltip _("Display a debug message with the text self-voicing would use")
        null width 200
        textbutton _("OFF"):
            action Preference("self voicing", "disable")
            tooltip _("Turn self-voicing off")

    hbox:
        label _("Voice Volume")
        text _("MIN")
        controller_bar value Preference("voice volume"):
            tooltip _("Adjust the volume of voiceover")
        text _("MAX")

    hbox:
        label _("Self-Voicing Volume Drop")
        text _("MIN")
        controller_bar value Preference("self voicing volume drop"):
            tooltip _("Adjust how much to drop the volume of other channels while self-voicing is enabled")
        text _("MAX")

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox
style radio_hbox is pref_hbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox
style check_hbox is pref_hbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_side:
    xfill True
    yfill True
    align (1.0, 0.5)
    spacing gui.pref_spacing

style pref_label:
    top_margin 15
    bottom_margin 15
    xsize 450

style pref_label_text:
    xalign 1.0 text_align 1.0
    yalign 1.0

style pref_hbox:
    first_spacing 40
    spacing 25
    xmaximum 1350
    box_wrap True
    box_wrap_spacing 25

style pref_vbox:
    spacing gui.pref_spacing

style radio_button:
    foreground "gui/button/radio_[prefix_]foreground.png"
    padding (35, 6, 6, 6)
    yalign 0.5

style check_button:
    foreground "gui/button/check_[prefix_]foreground.png"
    padding (35, 6, 6, 6)
    yalign 0.5

style pref_bar:
    is slider
    yalign 0.5
    xsize 640

style pref_text:
    yalign 0.5
    size 26
    min_width 70
    text_align 0.5 xalign 0.5

## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False
    
    if shock.menu.get("use_split_history"):
        # SPLIT HISTORY

        ## This just has a background to darken the screen
        add "#000b"

        side "c r":
            style_prefix "history"
            ## Use a controller viewport for scrolling
            controller_viewport:
                mousewheel True draggable True pagekeys True
                ## It uses the "fast jump" shortcuts to get to the beginning/end
                ## of the viewport. The d-pad and arrowkeys can be used to scroll.
                shortcuts True arrowkeys 'not sticks'
                yinitial 1.0 id "history_vp" which_stick "both"

                has vbox

                for h in _history_list:

                    frame:
                        has hbox
                        if h.who:
                            label h.who style 'history_name':
                                substitute False
                                ## Take the color of the who text
                                ## from the Character, if set
                                if "color" in h.who_args:
                                    text_color h.who_args["color"]
                                xsize gui.history_name_width
                        else:
                            null width gui.history_name_width

                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text what:
                            substitute False

                    if h != _history_list[-1]:
                        null height gui.history_spacing

                if not _history_list:
                    label _("The dialogue history is empty.")

            side "t c b":
                ## Include shortcut icons if the player is using a controller
                if pad_config.is_using_controller():
                    hbox:
                        spacing 0
                        for icn in pad_config.get_icons("scroll_shortcut", "small"):
                            add icn
                        add "pad_up_small"
                else:
                    null
                vbar value YScrollValue("history_vp") keyboard_focus False
                if pad_config.is_using_controller():
                    hbox:
                        spacing 0
                        for icn in pad_config.get_icons("scroll_shortcut", "small"):
                            add icn
                        add "pad_down_small"
                else:
                    null

        ## And a footer to return to the game
        use key_footer():
            icon_button kind icn.back suffix "small"

    else:
        # INTEGRATED HISTORY
        # (renpy default)
        use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing, show_footer=False):

            style_prefix "history"

            for h in _history_list:

                window:
                    has hbox
                    ## This lays things out properly if history_height is None.
                    #has fixed:
                    #    yfit True

                    if h.who:

                        label h.who:
                            style "history_name"
                            substitute False

                            ## Take the color of the who text from the Character, if
                            ## set.
                            if "color" in h.who_args:
                                text_color h.who_args["color"]
                    else:
                        null width gui.history_name_width

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        substitute False

            if not _history_list:
                label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xalign gui.history_name_xalign
    yalign gui.history_name_yalign
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

style history_frame:
    xsize gui.history_text_width + gui.history_name_width + 20
    ysize None
    background None
    padding (0,0,0,0)

style history_label:
    xfill True

style history_side:
    xysize (gui.history_text_width + gui.history_name_width + 20, 850)
    align (0.5, 0.5)
    spacing 10

style history_hbox:
    spacing 20


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    ## Starting device is the last input type
    default page = "keyboard_help" if pad_config.is_using_keyboard() else "mouse_help" if pad_config.is_using_mouse() else "gamepad_help"
    default tabs = ["keyboard_help", "mouse_help", "gamepad_help"]

    ## Absorb focusing actions since nothing on this screen is keyboard-focusable
    ## This shouldn't really be necessary but Ren'Py sometimes highlights a
    ## button when it shouldn't.
    key ['focus_left', 'focus_up', 'focus_right', 'focus_down'] action NullAction()

    use game_menu(_("Help"), can_focus=False, show_footer=page != "gamepad_help")

    use tabbed_menu({
        "keyboard_help": _("Keyboard"),
        "mouse_help": _("Mouse"),
        "gamepad_help": _("Gamepad")
    }, page, arrowkeys="not sticks")

    if page == "gamepad_help":
        use key_footer():
            if GamepadExists():
                icon_button kind icn.reset suffix "small":
                    caption _("Remap Controls")
                    action ShowMenu("controller_remap")
            use game_menu_footer_buttons

screen keyboard_help():
    style_prefix 'help'
    hbox:
        frame:
            add "key_enter" alt _("Enter") xalign 1.0
        text _("Advances dialogue and activates the interface.")

    hbox:
        frame:
            add "key_space" alt _("Space") xalign 1.0
        text _("Advances dialogue without selecting choices.")

    hbox:
        frame:
            has hbox
            spacing 5
            add "key_left" alt _("Arrow Keys")
            add "key_up"
            add "key_right"
            add "key_down"
        text _("Navigate the interface.")

    ############################################################
    ## These are custom to this template
    hbox:
        frame:
            has hbox
            spacing 5
            add "key_q" alt "Q"
            add "key_e" alt "E"
        text _("Switch pages in the interface.")
    ############################################################

    hbox:
        frame:
            add "key_pgup" alt _("Page Up") xalign 1.0
        text _("Rolls back to earlier dialogue.")

    hbox:
        frame:
            add "key_pgdn" alt _("Page Down") xalign 1.0
        text _("Rolls forward to later dialogue.")

    hbox:
        frame:
            add "key_l" alt _("L") xalign 1.0
        text _("Open history screen.")

    hbox:
        frame:
            add "key_ctrl" alt _("Ctrl") xalign 1.0
        text _("Skips dialogue while held down.")

    hbox:
        frame:
            add "key_tab" alt _("Tab") xalign 1.0
        text _("Toggles dialogue skipping.")

    hbox:
        frame:
            add "key_a" alt _("A") xalign 1.0
        text _("Toggles auto-forward.")

    hbox:
        frame:
            add "key_escape" alt _("Escape") xalign 1.0
        text _("Accesses the game menu.")

    hbox:
        frame:
            add "key_h" alt "H" xalign 1.0
        text _("Hides the user interface.")

    hbox:
        frame:
            add "key_s" alt "S" xalign 1.0
        text _("Takes a screenshot.")

    hbox:
        frame:
            add "key_v" alt "V" xalign 1.0
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        frame:
            has hbox
            spacing 5
            add "key_shift" alt "Shift+A"
            text "+" style 'default' yalign 0.5
            add "key_a"
        text _("Opens the accessibility menu.")


screen mouse_help():
    style_prefix 'help'
    hbox:
        frame:
            add "mouse_left" alt _("Left Click") xalign 1.0
        text _("Advances dialogue and activates the interface.")

    hbox:
        frame:
            add "mouse_middle" alt _("Middle Click") xalign 1.0
        text _("Hides the user interface.")

    hbox:
        frame:
            add "mouse_right" alt _("Right Click") xalign 1.0
        text _("Accesses the game menu.")

    hbox:
        frame:
            add "mouse_down" alt _("Mouse Wheel Down") xalign 1.0
        text _("Rolls back to earlier dialogue.")

    hbox:
        frame:
            add "mouse_up" alt _("Mouse Wheel Up") xalign 1.0
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    style_prefix 'help'
    hbox:
        frame:
            has hbox
            spacing 5
            for ic, al in pad_config.get_icons("dismiss", "", True):
                add ic alt al
        text _("Advances dialogue.")

    hbox:
        frame:
            has hbox
            spacing 5
            for ic, al in pad_config.get_icons("button_select", "", True):
                add ic alt al
        text _("Activates the interface.")

    hbox:
        frame:
            has hbox
            spacing 5
            for ic, al in pad_config.get_icons("rollback", "", True):
                add ic alt al
        text _("Rolls back to earlier dialogue.")

    hbox:
        frame:
            has hbox
            spacing 5
            for ic, al in pad_config.get_icons("rollforward", "", True):
                add ic alt al
        text _("Rolls forward to later dialogue.")


    hbox:
        frame:
            has hbox
            spacing 5
            for ic, al in pad_config.get_icons("focus_left", "", True):
                add ic alt al
        text _("Navigates the interface.")

    ############################################################
    ## These are custom to this template
    hbox:
        frame:
            has hbox
            spacing 5
            for ic, al in pad_config.get_icons("page_left", "", True):
                add ic alt al
            for ic, al in pad_config.get_icons("page_right", "", True):
                add ic alt al
        text _("Switches pages in the interface.")
    ############################################################

    hbox:
        frame:
            has hbox
            spacing 5
            for ic, al in pad_config.get_icons("game_menu", "", True):
                add ic alt al
        text _("Accesses the game menu.")

    hbox:
        frame:
            has hbox
            spacing 5
            for ic, al in pad_config.get_icons("hide_windows", "", True):
                add ic alt al
        text _("Hides the user interface.")

    hbox:
        frame:
            has hbox
            spacing 5
            for ic, al in pad_config.get_icons("toggle_afm", "", True):
                add ic alt al
        text _("Toggles auto-advance.")

    hbox:
        frame:
            has hbox
            spacing 5
            for ic, al in pad_config.get_icons("toggle_skip", "", True):
                add ic alt al
        text _("Toggles dialogue skipping.")

    hbox:
        frame:
            has hbox
            spacing 5
            for ic, al in pad_config.get_icons("screenshot", "", True):
                add ic alt al
        text _("Takes a screenshot.")

    hbox:
        frame:
            has hbox
            spacing 5
            for ic, al in pad_config.get_icons("self_voicing", "", True):
                add ic alt al
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        frame:
            has hbox
            spacing 5
            for ic, al in pad_config.get_icons("accessibility", "", True):
                add ic alt al
        text _("Opens the accessibility menu.")


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_frame:
    xsize 350
    background None

style help_hbox:
    xalign 1.0
    spacing 50
    yalign 0.5

style help_button:
    xmargin 12

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0

style help_text:
    min_width 800
    xmaximum 800
    yalign 0.5


################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action, yes_text=_("Confirm"), no_text=_("Cancel")):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                ## Updated, for controller. These are special buttons which
                ## automatically handle controller and keyboard events, and show
                ## an appropriate icon next to a text caption.
                icon_button caption yes_text:
                    ## The kind property is used to inherit properties from
                    ## previously declared IconButton objects. You can find common
                    ## ones declared in controller_icons.rpy
                    kind icn.select
                    ## The suffix means the "_small" icon version is shown
                    suffix "small"
                    ## The button action is as it usually would be
                    action yes_action
                    ## You can set up styles as though it were a usual textbutton
                    text_style "confirm_button_text" style "confirm_button"
                    ## It will also take an hbox_style if you want to adjust the hbox

                    yalign 0.5
                    text_insensitive_color gui.idle_color
                if no_action is not None:
                    icon_button caption no_text:
                        yalign 0.5
                        kind icn.back suffix "small" action no_action
                        ## Note that due to style_prefix "confirm", the icon_buttons
                        ## automatically get the styles "confirm_icon_button",
                        ## "confirm_icon_button_text", and "confirm_icon_button_hbox"

    ## Right-click and escape answer "no".
    key "game_menu" action no_action

screen choices(message, choices):
    # choices is dict with key: text, value: action
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                default kinds = [icn.delete, icn.sync, icn.reset, icn.select]
                # keys that get popped in reverse order
                for text, action in choices.items():

                    icon_button caption text:
                        kind kinds.pop()
                        suffix "small"
                        action action
                        yalign 0.5
                        text_insensitive_color gui.idle_color

    ## Right-click and escape answer "no".
    key "game_menu" action Hide("choices")



style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        side "c r":
            controller_viewport:
                id "nvl_vp"
                if shock.nvl.get("scrolling"):
                    yinitial 1.0
                    scrollbars shock.nvl.get("scrollbars")
                    mousewheel shock.nvl.get("scrollbars_mousewheel")
                arrowkeys "not sticks"

                ysize 1080 - (gui.nvl_borders.padding[1] + gui.nvl_borders.padding[3]) - 20

                vbox:
                    spacing gui.nvl_spacing

                    ## Displays dialogue in either a vpgrid or the vbox.
                    if gui.nvl_height:

                        vpgrid:
                            cols 1
                            yinitial 1.0

                            use nvl_dialogue(dialogue)

                    else:

                        use nvl_dialogue(dialogue)

                    ## Displays the menu, if given. The menu may be displayed incorrectly if
                    ## config.narrator_menu is set to True.
                    for i in items:

                        textbutton i.caption:
                            action i.action
                            style "nvl_button"

            vbar value YScrollValue("nvl_vp"):
                unscrollable "hide"
                keyboard_focus False
                default_focus False

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
