# About this project
I've been around the block enough times to know that there's always a few things that I always go in and fix in every project I have, so I might as well make a copy/pastable template for it. You can use it too if you want.
## Usage
1. Copy the contents of this project when you want to start a new game and save it to the your launcher's working directory.
2. Boot up the SDK.
3. Click "create new project" and, when prompted, select "shock_template"
4. Peruse `shock_definitions.rpy` and change your new config variables.
## Key Changes
- Sensible `.gitignore` file
    - Note: if you use the "template" feature, you will need to copy this over manually
- Significant menu reworks
    - Preference screen QoL tweaks
    - Navigation screen rewrite to facilitate animations
    - Improved save screen
    - Added option to use history screen not attached to game_menu
    - Integrated feniksdev's controller support *without* using the EasyGUI template
- Modified default nvl behavior to length, height = None
    - Also corrected the history and small screen variant
    - nvl mode scrolls on overflow, optional scrollbar to go back up
- Various new preference parameters
    - Added hooks for menu sounds
    - Added transform `hover_nav` to all buttons in `navigation()`
- Most importantly: prevented accidental activation of `hover_sound` when clicking navigation_menu items and changing screens.
    - *Note: this is no longer the most important thing in this project, but it was what got me to start it in the first place*

### Added to `/game/libs`
If you use this project, you need to give attribution per their license terms.
- [FeniksDev controller support expansion](https://feniksdev.itch.io/controller-support-expansion-for-renpy)
- [kigyodev's improved word counter](https://kigyo.itch.io/renpy-word-counter)
- [brunoais' gui inspect](https://brunoais.itch.io/renpy-guiinspect)
- my homebrewed text bloop plugin

## TODO
- [X] fix focus on saves screen
- [x] fix focus when changing button styles
- [ ] clean up styles on saves screen
- [x] change default esc screen when null menu is false
- [ ] ~~change shock prefs to "init python in shock"~~ not what I want
- [x] figure out how to add single transform to all button prompts
- [ ] add default sounds to menus + buttons
- [ ] new radio and check images
- [ ] add text pause lib
    - [ ] option to enable in shock.
    - [ ] options on pref screen + change slider ranges
    - [ ] example with eileen
    - [ ] add "silence" tag
    - [ ] fix regex to not trigger on decimals in tags
- [ ] flag all new entries in `gui.rpy`
- [ ] verify mobile layout
- [ ] update license terms in this doc, include in "about" page by default.

## Future Changes
Subject to my changing whims.
