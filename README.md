# About this project
I've been around the block enough times to know that there's always a few things that I always go in and fix in every project I have, so I might as well make a copy/pastable template for it. You can use it too if you want.
## Usage
1. Copy the contents of this project when you want to start a new project, instead of using the button in the renpy sdk.
2. Open `options.rpy` and **change the `build.name` and `config.name` variables**. *This is required to prevent collisions with other projects using this file*.
3. Peruse `shock_definitions.rpy` and change your new config variables.
## Key Changes
- Sensible `.gitignore` file
- Significant menu reworks
    - Preference screen QoL tweaks
    - Navigation screen rewrite to facilitate animations
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
If you use this project and do not remove these, you need to give credit per their license terms.
- [FeniksDev controller support expansion](https://feniksdev.itch.io/controller-support-expansion-for-renpy)
- [kigyodev's improved word counter](https://kigyo.itch.io/renpy-word-counter)
- my homebrewed text bloop plugin

## Future Changes
Subject to my changing whims.
- Improved save screen
- Enhanced controller support
- Framework for better menu animations
