# Linux things common across installs

based on https://gist.github.com/jacobranson/adc32b6247f5c19494da0d3a24026d8f

## Set user-dirs

```bash
$ mkdir -p ~/doc/desktop
$ mkdir ~/dl
$ mkdir ~/src
$ mv ~/Music ~/music
$ mkdir -p ~/media/img
$ mkdir -p ~/media/video
```

```bash
$ xdg-user-dirs-update --set DESKTOP $HOME/doc/desktop
$ xdg-user-dirs-update --set DOWNLOAD $HOME/dl
$ xdg-user-dirs-update --set TEMPLATES $HOME/doc/desktop
$ xdg-user-dirs-update --set PUBLICSHARE $HOME/doc/desktop
$ xdg-user-dirs-update --set DOCUMENTS $HOME/doc
$ xdg-user-dirs-update --set MUSIC $HOME/music
$ xdg-user-dirs-update --set PICTURES $HOME/media/img
$ xdg-user-dirs-update --set VIDEOS $HOME/media/video
```


## Standard software

Install basic tools:

```bash
$ sudo dnf install \
    bat \
    curl \
    exa \
    git \
    htop \
    ncdu \
    neovim \
    ripgrep \
    tmux \
    tree \
    tmux \
    zsh
```

Install more stuff for desktop and development:

```bash
$ sudo dnf install \
    alacritty \
    ansible \
    ansible-lint \
    aria2 \
    btop \
    cmake \
    detox \
    duf \
    ffmpeg \
    freetype-devel \
    fontconfig-devel \
    libxcb-devel \
    libxkbcommon-devel \
    foot \
    g++ \
    gcc \
    gcc-c++ \
    git-delta \
    gitk \
    httpie \
    irssi \
    kernel-devel \
    neofetch \
    make \
    mpv \
    mupdf \
    oksh \
    pkg-config \
    syncthing \
    tealdeer \
    yt-dlp 
```

Use [this link](https://yadm.io/docs/install) for instructions to install yadm

## Flathub

To get a wider variety of software, and more up to date packages, replace the Fedora Flatpak repository with Flathub.

```bash
$ flatpak remove --all
$ flatpak remote-delete fedora
$ flatpak remote-add --if-not-exists flathub \
    https://flathub.org/repo/flathub.flatpakrepo
$ flatpak update
$ reboot
```

## Firefox

Be sure to add the following to `about:config` in Firefox to enable hardware decoding and disable Pocket integration.

```
media.ffmpeg.vaapi.enabled = true
media.ffvpx.enabled = false
media.navigator.mediadatadecoder_vpx_enabled = true
media.rdd-vpx.enabled = false
extensions.pocket.enabled = false
```

## GNOME Applications

To install a starter set of GNOME & GNOME-related applications:

```bash
$ flatpak install flathub \
    com.github.tchx84.Flatseal \
    com.mattjakeman.ExtensionManager \
    com.transmissionbt.Transmission \
    com.usebottles.bottles \
    io.github.celluloid_player.Celluloid \
    org.gnome.Boxes \
    org.gnome.baobab \
    org.gnome.Calendar \
    org.gnome.Cheese \
    org.gnome.EasyTAG
    org.gnome.Evince \
    org.gnome.eog \
    org.gnome.Firmware \
    org.gnome.Geary \
    org.gnome.Lollypop \
    org.gnome.meld \
    org.gnome.SoundRecorder \
    org.gnome.TextEditor 
    
```

## GNOME Extensions

GNOME extensions can be installed from [extensions.gnome.org](https://extensions.gnome.org).
They can be configured using the Extension Manager application.

Some popular ones include the following.

* [AppIndicator and KStatusNotifierItem Support](https://extensions.gnome.org/extension/615/appindicator-support/)
* [Just Perfection](https://extensions.gnome.org/extension/3843/just-perfection/)
* [Burn My Windows](https://extensions.gnome.org/extension/4679/burn-my-windows/)
* [Power Profiles Indicator](https://extensions.gnome.org/extension/5335/power-profile-indicator/)
* [supergfxctl-gex](https://extensions.gnome.org/extension/5344/supergfxctl-gex/)

## Pop Shell

Pop Shell is a tiling window manager extension for GNOME. To install:

```bash
$ sudo dnf install gnome-shell-extension-pop-shell
$ reboot
```

## NFS Shares

To add support to the File Manager to access NFS shares:

```bash
$ rpm-ostree install gvfs-nfs
$ reboot
```

## GNOME Preferences

## get gsettings

`gsettings list-recursively`

## gnome application switcher scope

You can change the scope of the window switcher (Alt-Tab) from current workspace only to all workspaces with the command:

```
gsettings set org.gnome.shell.window-switcher current-workspace-only false
```

You can change the scope of the application switcher (Alt-backtick) from all workspaces to current workspace only with the command:

```
gsettings set org.gnome.shell.app-switcher current-workspace-only true
```

Use the same commands, replacing set with reset and leaving out the argument (e.g. false) to reset the setting to default. You can also use the graphical tool dconf-editor (not installed by default) to change these settings.

- Keyboard & Mouse
  
  - turn on Emacs Input (maybe quit this?)
    `gsettings set org.gnome.desktop.interface gtk-key-theme Emacs`
  - Mouse Click Emulation - set to fingers
    `gsettings set org.gnome.desktop.peripherals.touchpad click-method 'fingers'`

- Topbar
  
  - turn on Activities Overview Hot Corner
    `gsettings set org.gnome.desktop.interface enable-hot-corners true`
  
  - turn on Battery Percentage
    `gsettings set org.gnome.desktop.interface show-battery-percentage true`

- Windows
  
  - show minimize button 
    `gsettings set org.gnome.desktop.wm.preferences button-layout ':minimize,maximize,close'`
  - use Alt as resize button
    `gsettings set org.gnome.desktop.wm.preferences mouse-button-modifier '<Alt>'`
  - turn on Resize with Secondary-Click
    `gsettings set org.gnome.desktop.wm.preferences resize-with-right-button true`

- dash to dock
  
  - icon size
    `gsettings set org.gnome.shell.extensions.dash-to-dock dash-max-icon-size 36`
  - dock on left
    `org.gnome.shell.extensions.dash-to-dock dock-position 'LEFT'`

## screenshot directory

`gsettings set org.gnome.gnome-screenshot auto-save-directory '$HOME/img/scrot'`


## Rebind Keys

- desktop switching
  `gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-left "['<Primary><Super>Left']"`
  `gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-right "['<Primary><Super>Right']"`
  `gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-left "['<Primary><Shift><Super>Left']"`
  `gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-right "['<Primary><Shift><Super>Right']"`

- allow ctrl-tab switching tabs in gnome-terminal
  - `gsettings set org.gnome.Terminal.Legacy.Keybindings:/org/gnome/terminal/legacy/keybindings/ next-tab '<Primary>Tab'`
  - `gsettings set org.gnome.Terminal.Legacy.Keybindings:/org/gnome/terminal/legacy/keybindings/ prev-tab '<Primary><Shift>Tab'`

Modifications can be made to the default keyboard layout using `gsettings`. For example, the below command binds the Caps Lock key to Control, and toggles Caps Lock if both Shift keys are pressed simultaneously.

```bash
$ gsettings set org.gnome.desktop.input-sources xkb-options "['caps:ctrl_modifier', 'shift:both_capslock']"
```

To see a list of all options for keyboard layout modifications:

```bash
$ localectl list-x11-keymap-options | cat | less
```

To see full descriptions of the layouts and options available:

```bash
$ man 7 xkeyboard-config
```

## Other Applications

Install any other software you like, as well. For example:

```bash
$ flatpak install flathub \
    ch.protonmail.protonmail-bridge \
    com.bitwarden.desktop \
    com.discordapp.Discord \
    com.github.marktext.marktext \
    com.github.micahflee.torbrowser-launcher \
    com.plexamp.Plexamp \
    com.spotify.Client \
    com.vscodium.codium \
    fr.handbrake.ghb \
    im.riot.Riot \
    io.gitlab.librewolf-community \
    org.ferdium.Ferdium \
    org.musicbrainz.Picard \
    org.remmina.Remmina \
    org.signal.Signal
```

## Steam, Proton, Lutris, Gamemode, & MangoHud

* Use Steam to buy & play Linux-native games.
* Use Proton to play Windows-only games on Linux via Steam.
* Use Lutris to play Windows-only games not on Steam.
* Use Gamemode to see increased performance in games.
* Use MangoHud to see system stats in games.

```bash
$ flatpak install flathub \
    net.lutris.Lutris \
    org.freedesktop.Platform.VulkanLayer.MangoHud \
    com.valvesoftware.Steam \
    com.valvesoftware.Steam.Utility.gamescope \
    net.davidotek.pupgui2 \
    com.github.Matoking.protontricks
$ rpm-ostree install gnome-shell-extension-gamemode
$ reboot
```

## Controllers in Steam Games Fix

This section requires that the `rpmfusion-nonfree` repository has been installed on your system.

The Steam Flatpak has issues detecting controllers by default. To fix this:

```bash
$ rpm-ostree install steam-devices
$ reboot
```

Next, perform the following steps.

1. Launch Steam
2. Lauch Big Picture Mode
3. Go to Settings
4. Go to Base configurations in the Controller section
5. Select Desktop configuration
6. Select Browse Configs
7. Select templates
8. Select Show other controller types
9. Select Gamepad (the variant for your specific controller, ex. PlayStation 5 controller)

## Setup MangoHud

MangoHud can be used to show system stats in games. To create a MangoHud config file:

```bash
$ mkdir ~/.var/app/com.valvesoftware.Steam/config/MangoHud
$ touch ~/.var/app/com.valvesoftware.Steam/config/MangoHud/MangoHud.conf
```

You can edit the config as follows:

```bash
$ nano ~/.var/app/com.valvesoftware.Steam/config/MangoHud/MangoHud.conf
```

Documentation [here](https://github.com/flightlessmango/MangoHud#mangohud_config-and-mangohud_configfile-environment-variables) on the config file.

If you just want to see everything available, add `full` to the file and save.

### Default Keybinds

* `Shift_L+F2`: Toggle Logging
* `Shift_L+F4`: Reload Config
* `Shift_R+F12`: Toggle Hud

## Enabling Gamemode & MangoHud in a Steam Game

1. Right click on the game
2. Click Properties
3. In the General tab, put the following in launch options

```
gamemoderun mangohud %command%
```

If you have other things set in there, make sure `gamemoderun mangohud` comes first.

## PolyMC

To play Minecraft, install PolyMC.

```bash
$ flatpak install flathub org.polymc.PolyMC
```

By default, PolyMC will launch on iGPU. To change this:

```bash
$ cp /var/lib/flatpak/exports/share/applications/org.polymc.PolyMC.desktop ~/.local/share/applications/
$ echo "PrefersNonDefaultGPU=true" >> ~/.local/share/applications/org.polymc.PolyMC.desktop
```

You can verify the change worked by right clicking PolyMC in the GNOME app grid. If an option "Launch using Integrated Graphics Card" appears in the list, it worked.

You can verify the game is running on dGPU by opening the F3 menu in-game. GPU should say "Dimgrey Cavefish".

## Setup Emulation

Execute the following commands to install emulators for many popular game consoles.

```bash
$ flatpak install flathub \
    dev.ares.ares \
    io.github.m64p.m64p \
    org.DolphinEmu.dolphin-emu \
    org.yuzu_emu.yuzu \
    io.mgba.mGBA \
    org.desmume.DeSmuME \
    org.citra_emu.citra \
    org.duckstation.DuckStation \
    net.pcsx2.PCSX2 \
    net.rpcs3.RPCS3 \
    org.ppsspp.PPSSPP
```

## Setup Melee

* Download [Slippi](https://slippi.gg/downloads)
* Download [m-overlay](https://github.com/bkacjios/m-overlay/wiki/Linux)
  * Download `love-11.3-x86_64.AppImage` linked on the above page
  * Download `m-overlay-x64.love` from the Releases page
  * Run the following commands:

```bash
$ cd ~/Downloads
$ chmod +x ./Slippi-Launcher-2.1.15-x86_64.AppImage
$ chmod +x ./love-11.3-x86_64.AppImage
$ sudo setcap cap_sys_ptrace=eip ./love-11.3-x86_64.AppImage
$ rpm-ostree install libcap-devel
$ reboot
```

