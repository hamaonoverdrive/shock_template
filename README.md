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
    - Integrated feniksdev's controller support *without* using the EasyGUI template
- Various new preference parameter
    - Added default style to all buttons that gives them `activate_sound` and `hover_sound` parameters
    - Added `ui_adv` for text advance
    - Added transform `hover_nav` to all buttons in `navigation()`
- Modified default nvl behavior to length, height = None
    - Also corrected the history and small screen variant
    - nvl mode scrolls on overflow, optional scrollbar to go back up
- Most importantly: prevented accidental activation of `hover_sound` when clicking navigation_menu items and changing screens.
    - *Note: this is no longer the most important thing, but it was what got me to start this project in the first place*

### Added to `/game/libs`
If you use this project and do not remove these files, you need to give attribution per their license terms.
- [FeniksDev controller support expansion](https://feniksdev.itch.io/controller-support-expansion-for-renpy)
- [kigyodev's improved word counter](https://kigyo.itch.io/renpy-word-counter)
- [brunoais' gui inspect](https://brunoais.itch.io/renpy-guiinspect)
- my homebrewed text bloop plugin

## Future Changes
Subject to my changing whims.
- Improved save screen
- Enhanced controller support
- Framework for better menu animations
- OPTIONS for split history screen and main menu screen
- MY solution to speech pauses + options to enable
