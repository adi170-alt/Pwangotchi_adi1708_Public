# Pwnagotchi Plugins!

This is a public version of my other private pwnagotchi repository
---------------
# Installation

1. SSH into your Pwnagotchi and create a new folder for third-party Pwnagotchi plugins. I use `/root/custom_plugins/` but it doesn't really matter: `mkdir /root/custom_plugins/`
1. Grab the `display-password.py` and `display-password.toml` file from this Github repo and put it into that custom plugins directory.
1. Edit `/etc/pwnagotchi/config.toml` and change the `main.custom_plugins` variable to point to the custom plugins directory you just created: `main.custom_plugins = "/root/custom_plugins/"`
1. In the same `/etc/pwnagotchi/config.toml` file, add the following lines to enable the plugin:
```
main.plugins.display-password.enabled = true
main.plugins.display-password.orientation = "horizontal"

main.plugins.clock.enabled = true
```
Once the above steps are completed, reboot the Pwnagotchi to ensure all changes are applied.
Credit to @cnagy becouse I copyed his instalation from readme. Sorry

----------------
# Preview:

![nh7c3hsqdlt61](https://user-images.githubusercontent.com/79835819/116106436-62635a80-a6b2-11eb-9a80-f64afd15f642.png)

----------------
# Unedited Custum Plugins:

https://github.com/c-nagy/pwnagotchi-display-password-plugin

https://github.com/LoganMD/pwnagotchi-clock

----------------
This is a public version of my other private pwnagotchi repository
Files that I imported:
* plugins
