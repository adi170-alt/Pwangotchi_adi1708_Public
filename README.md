# Pwnagotchi Plugins!
# WARNING: This only works with waveshare v2 or comletly without a screen, It maybe works on other ones but idk

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
After that U want to edit the gps config and the memtemp config
You can find the plugins in here:
```
/usr/local/lib/python3.7/dist-packages/pwnagotchi/plugins/default/
```
You can just simply replace those files, but just make sure that u have pwanotchi version v1.5.5

---------------
Once the above steps are completed, reboot the Pwnagotchi to ensure all changes are applied.

----------------
# Preview:

![nh7c3hsqdlt61](https://user-images.githubusercontent.com/79835819/116106436-62635a80-a6b2-11eb-9a80-f64afd15f642.png)

----------------
# Unedited Custum Plugins:

Wpa sec Pasword viewer plugin: https://github.com/c-nagy/pwnagotchi-display-password-plugin

Clock plugin: https://github.com/LoganMD/pwnagotchi-clock

Christmas plugin: https://github.com/LoganMD/pwnagotchi-christmas-countdown

----------------
I can add the Brithday plugin that I made, but It is not the best

----------------
This is a public version of my other private pwnagotchi repository
Files that I imported:
* plugins
----------------
# credits:
Credit to [@cnagy](https://github.com/c-nagy) becouse I copyed his instalation from readme. Sorry
Credit to [@highrup](https://www.reddit.com/user/highrup/) becouse it was his idea
And also credit for the peaple who made those plugins links are in the preview tab
