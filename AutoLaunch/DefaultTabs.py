#!/usr/bin/env python3.7

import asyncio
import iterm2
# This script was created with the "basic" environment which does not support adding dependencies
# with pip.

async def main(connection):
    app = await iterm2.async_get_app(connection)
    window = app.current_terminal_window

    # Save the original tab that automatically opens so that we can close it later
    original_tab = window.current_tab

    # Index of the default tab
    activated_tab_index = 2

    # Open desired tabs; For any folder you want opened, there needs to be a corresponding Iterm2 profile
    new_tabs = [
        "SICP",
        "elixir",
        None,
    ]
    coros = map(lambda arg: window.async_create_tab(index=arg[0], profile=arg[1]), enumerate(new_tabs))
    await asyncio.gather(*coros)

    # Kill the default tab
    await original_tab.async_close(force=True)

    # Set the activated tab
    initial_tab = window.tabs[activated_tab_index]
    await initial_tab.async_activate()

    # Start in fullscreen mode
    await window.async_set_fullscreen(fullscreen=True)

iterm2.run_until_complete(main)
