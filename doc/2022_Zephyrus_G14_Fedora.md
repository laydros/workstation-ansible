# 2022 Zephyrus G14 Fedora Silverblue Setup

based on https://gist.github.com/jacobranson/adc32b6247f5c19494da0d3a24026d8f

## GPU Naming

Most applications in Linux will report the names of the two GPUs as follows.

* Dimgrey Cavefish is dGPU
* Yellow Carp is iGPU

## Boot Hotkeys

* `F2`: Enter BIOS
* `LSHIFT`: Enter GRUB

## Wifi Card

The included wifi card has spotty support right now on Linux.

You may consider replacing it with an Intel AX200 or Intel AX210 instead, for plug-and-play support.

## BIOS Settings

Secure Boot must be disabled in order for kernel arguments to be respected.

## Fixing Random Crashing - HAVEN'T USED YET

There is an open issue [here](https://gitlab.freedesktop.org/drm/amd/-/issues/2068) regarding random freezes with the 6900HS / 6800HS hardware. As a workaround:

```bash
$ rpm-ostree kargs --append=initcall_blacklist=amd_pstate_init
$ reboot
```

When you boot back up, verify the changes were successful with the following command.

```bash
$ grep -q 'acpi-cpufreq' /sys/devices/system/cpu/cpu0/cpufreq/scaling_driver && echo 'success'
```

If the output says `success`, you should no longer be prone to frequent crashes.

## Adjust clock for dual booting with Windows

```bash
$ timedatectl set-local-rtc 1
```

## Asus Linux Repo

Add the Asus Linux repository for additional necessary software.

```bash
$ sudo dnf copr enable lukenukem/asus-linux
```

## asusctl

```bash
$ sudo dnf install asusctl supergfxctl asusctl-rog-gui 
$ reboot
$ systemctl enable --now supergfxd.service
$ reboot
```

This system tray icon allows switching Gnome power modes (which is already built into gnome) and enabling and disabling boost. [asusctltray](https://github.com/Baldomo/asusctltray)

## RPMFusion

RPMFusion is a third party repository with additional commonly installed packages. Install it as follows.

```bash
$ sudo dnf install \
    https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm \
    https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

After install do the following to switch codecs for Fedora 37 and later

```bash
$ sudo dnf groupupdate multimedia --setop="install_weak_deps=False" --exclude=PackageKit-gstreamer-plugin
$ sudo dnf groupupdate sound-and-video

# AMD Specific
$ sudo dnf swap mesa-va-drivers mesa-va-drivers-freeworld
$ sudo dnf swap mesa-vdpau-drivers mesa-vdpau-drivers-freeworld

# If using i686 compat libraries (for steam and alikes):
sudo dnf swap mesa-va-drivers.i686 mesa-va-drivers-freeworld.i686
sudo dnf swap mesa-vdpau-drivers.i686 mesa-vdpau-drivers-freeworld.i686
```

Tainted nonfree is dedicated to non-FLOSS packages without a clear redistribution status by the copyright holder. But is allowed as part of hardware inter-operability between operating systems in some countries :

```bash
$ sudo dnf install rpmfusion-nonfree-release-tainted
$ sudo dnf --repo=rpmfusion-nonfree-tainted install "*-firmware"
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

The default install of Firefox is not packaged as a Flatpak. There are certain issues with codecs on streaming sites that can be fixed by using the Flathub package instead. To install it:

```bash
$ rpm-ostree override remove firefox
$ flatpak install flathub \
    org.mozilla.firefox \
    org.freedesktop.Platform.ffmpeg-full
$ sudo flatpak override \
    --socket=wayland \
    --env=MOZ_ENABLE_WAYLAND=1 \
    org.mozilla.firefox
$ reboot
```
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
    org.gnome.DejaDup \
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

## Setup Homedir

```bash
$ mkdir ~/dl
$ mkdir ~/doc
$ mkdir ~/src
$ mv ~/Music ~/music
$ mkdir -p ~/media/img
$ mkdir -p ~/media/video
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

- sway/i3 like desktop switching and moving
  - `gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-1 "['<Super>1']"`
  - `gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-2 "['<Super>2']"`
  - `gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-3 "['<Super>3']"`
  - `gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-4 "['<Super>4']"`
  - `gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-5 "['<Super>5']"`
  - `gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-6 "['<Super>6']"`
  - `gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-7 "['<Super>7']"`
  - `gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-8 "['<Super>8']"`
  - `gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-9 "['<Super>9']"`
  - `gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-10 "['<Super>0']"`

  - `gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-1 "['<Shift><Super>1']"`
  - `gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-2 "['<Shift><Super>2']"`
  - `gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-3 "['<Shift><Super>3']"`
  - `gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-4 "['<Shift><Super>4']"`
  - `gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-5 "['<Shift><Super>5']"`
  - `gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-6 "['<Shift><Super>6']"`
  - `gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-7 "['<Shift><Super>7']"`
  - `gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-8 "['<Shift><Super>8']"`
  - `gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-9 "['<Shift><Super>9']"`
  - `gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-1 "['<Shift><Super>1']"`

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
    com.calbre_ebook.calibre \
    com.discordapp.Discord \
    com.github.johnfactotum.Foliate \
    com.github.marktext.marktext \
    com.github.micahflee.torbrowser-launcher \
    com.notepadqq.Notepadqq \
    com.plexamp.Plexamp \
    com.spotify.Client \
    com.vscodium.codium \
    fr.handbrake.ghb \
    im.riot.Riot \
    io.gitlab.librewolf-community \
    org.ferdium.Ferdium \
    org.musicbrainz.Picard \
    org.qutebrowser.qutebrowser \
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

## Final Fantasy XIV Setup

FFXIV is a real pain to set up now. To do so anyway, perform the following steps. The steps have been broken into parts for ease of readability.

### Part 1: Steam Play and ProtonUp

* In Steam, go to Settings, Steam Play
* Enable Steam Play for all other titles
* Run other titles with whatever the latest official Proton version is
* Restart Steam
* Install FFXIV through Steam library
* Wipe the existing game install by deleting the below directory, if it exists

```
$HOME/.steam/steam/steamapps/compatdata/39210
```

* Use ProtonUp to get Proton-6.21-GE-2 and GE-Proton7-14

### Part 2: Configuring Proton-6.21-GE-2

* Navigate to the below directory using the file manager

```
/var/home/jacob/.var/app/com.valvesoftware.Steam/.steam/steam/compatibilitytools.d/Proton-6.21-GE-2/protonfixes
```

* Open terminal in this directory.
* Run the below command.

```bash
$ ./winetricks --self-update
```

* Navigate to the `gamefixes` directory in the current directory.
* Rename `39210.py` to `39210.py.bak`
* Put [this](https://gist.github.com/Centzilius/57892e5d1aaea51b3f389e6f1d587c97#file-39210-py) file in that directory

### Part 3: Creation of compatdata with Proton 6.3-8

* In Steam, right click FFXIV, Properties
* Make sure no launch args in General tab
* Set compatibility to Proton 6.3-8
* Launch the game
* Let the launcher sit there doing nothing for 10 seconds
* Verify the below directory was created, then close the launcher

```
$HOME/.steam/steam/steamapps/compatdata/39210
```

### Part 4: Launcher preparations with Proton-6.21-GE-2

* In Steam, right click FFXIV, Properties
* Set compatibility to Proton-6.21-GE-2
* Launch ProtonTricks
* Click FFXIV in the app
* Click OK through all warnings in this entire process
* Click Install an Application
* Click OK
* Click Cancel in the new window
* Click Install a Windows DLL or Component
* Click dotnet48
* Click OK
* Run through the process until you return to the main window
* Repeat the above steps, but select vcrun2019 this time
* Run through the process until you return to the main window
* Close ProtonTricks
* In Steam, right click FFXIV, Properties
* In General tab, add the following launch arguments

```
XL_NO_SPACE_REQUIREMENTS=true XL_WINEONLINUX=true DSSENH=n %command%
```

### Part 5: Installing the game with the launcher

* Launch the game
* If any error appears, click "No" or "OK"
* The launcher should appear!
* In Steam, right click FFXIV, Manage, Browse local files
* Copy the file path of this directory and paste it into the launch directory the launcher asks for
* Be sure to select that this is a steam service account when configuring the launcher
* Sign in
* Let the launcher download the game
* Get to the title screen
* Close the game

### Part 6: Fixing the cutscenes with GE-Proton7-14

* In Steam, right click FFXIV, Properties
* Set compatibility to GE-Proton7-14
* Navigate to the below directory using the file manager

```
/var/home/jacob/.var/app/com.valvesoftware.Steam/.steam/steam/compatibilitytools.d/GE-Proton7-14/protonfixes/gamefixes
```

* Rename `39210.py` to `39210.py.bak`
* Put the same replacement file used previously into this directory
* Launch FFXIV
* Verify the cutscenes in the game work from the title screen
* Done

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

