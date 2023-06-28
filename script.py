from os import system, chdir
import readline
import time
import script
#Defines
clear = lambda: system('clear')
#Warning
print("This script is gonna install Chaotic AUR, Wine dependencies and needed things for gaming. all the things that redirected from this script, is done from you")
input("Press enter to continue.")
print("Usage:")
print("If you want to save configuration with nano, press Ctrl+X for exit and save the file.")
print("You only can copy things with LShift+Ctrl+C. And then you can paste things with LShift+Ctrl+V.")
input("Press enter to continue.")
clear()

#Questions
aurhelper = input("What is your AUR helper? (only paru and yay) : ")
aurhinst = input("Is any AUR helper installed? (y/n) : ")
deskenv = input("What is your Desktop Enviroment? (only kde plasma, xfce, gnome. If you want, this is gonna be installed) : ")
deq = input("Do you want to install Desktop Enviroment? (y/n) : ")
soundtweaks = input("Do you want to install Pipewire? (this gives you lower latency) (y/n) : ")
caur = input("Do you want to install Chaotic AUR? (y/n) : ")
winedh = input("Do you want to install Wine Dependency Hell? (y/n) : ")
gpu = input("What is your GPU? (nvidia or amd) : ")
lutris = input("Do you want to install Lutris? (y/n) : ")
steamnative = input("Do you want to install Steam with Native version with other gaming tools? (y/n) : ")
winecfg = input("Do you want to improve performance with Winecfg? (y/n) :")
grubp = input("Do you want to improve performance with kernel parameters? (y/n) : ")
sysctls = input("Do you want to improve performance with sysctl.d settings? (y/n) : ")
if sysctls == "y":
    swap = input("Do you have a physical swap? (y/n) : ")
    if swap == "y":
        sorh = input("SSD or HDD? : ")
multigpu = input("Are you using multi GPU? (y/n) : ")
if multigpu == "y":
    intelnvidia = input("Are you using intel-nvidia? : ")


#Settings
clear()
print("Settings:")
print("-------------")
print("AUR Helper Installation : ", aurhinst)
print("AUR Helper : ", aurhelper)
print("Desktop Enviroment Installation : ", deq)
print("Desktop Enviroment : ", deskenv)
print("Pipewire Installation : ", soundtweaks)
print("Chaotic AUR Repository Installation : ", caur)
print("Wine Dependency Hell Installation : ", winedh)
print("Your GPU is : ", gpu)
print("Lutris Installation : ", lutris)
print("Steam Native Installation with other gaming tools : ", steamnative)
print("Winecfg Tweaks : ", winecfg)
print("Kernel Tweaks with GRUB Parameters : ", grubp)
print("Improving Performance with sysctl.d Settings : ", sysctls)
if sysctls == "y":
    print("sysctl.d settings")
    print("You are Using : ", sorh)
    print("Physical Swap Status : ", swap)
print("Multi GPU Status =", multigpu)
print(" ")
torf = input("Is That True? (y/n) :")
if torf == "n":
    print("Try Again!")
    exit()

#Making
print("Updating system!")
system("sudo pacman -Syu")
clear()
if aurhelper == "paru":
    print("Your AUR Helper is paru.")
    input("Press enter to continue.")
    if aurhinst == "y":
        print("Installing paru AUR Helper...")
        system("sudo pacman -S --needed git")
        system("cd /tmp")
        system("git clone https://aur.archlinux.org/paru.git")
        system("cd paru")
        system("makepkg -si")
        input("Press enter to continue.")
        clear()
elif aurhelper == "yay":
    print("Your AUR Helper is yay.")
    input("Press enter to continue.")
    if aurhinst == "y":
        print("Installing yay AUR Helper...")
        system("sudo pacman -S --needed git")
        system("cd /tmp")
        system("git clone https://aur.archlinux.org/yay.git")
        system("cd yay")
        system("makepkg -si")
        input("Press enter to continue.")
        clear()

if deskenv == "xfce":
    compforxfce = input("Do you want to operate compositor? (Compositor is costs %30 performance ingame) (y/n) : ")
    if compforxfce == "y":
        print("When you press enter, XFCE keyboard settings will open. You need to automate this, so you need to create a new keyboard shortcuts for disabling composition.")
        print("Copy this two:")
        print(" ")
        print("xfconf-query -c xfwm4 -p /general/use_compositing -s false")
        print("xfconf-query -c xfwm4 -p /general/use_compositing -s true")
        print('The "true" valuable, is will enable the compositor. "false" is just disables. Go to the shortcuts, and create two keyboard shortcuts. Then paste this commands, configure it whatever you want.')
        system("xfce4-keyboard-settings")
        input("Press enter to continue.")
        clear()
    if deq == "y":
        print("Warning! Minimal XFCE need to be started on tty! But its too small, so this is improving performance.")
        xfcevarriants = input("What variant do you want to install? (normal xfce/minimal xfce) : ")
        clear()
        if xfcevarriants == "normal xfce":
            system("sudo pacman -S --needed xfce4 xfce4-goodies lightdm lightdm-gtk-greeter xorg xorg-xinit")
            system("sudo systemctl enable lightdm")
            input("Press enter to continue.")
            clear()
        elif xfcevarriants == "minimal xfce":
            system("sudo pacman -S --needed xfce4 mousepad ristretto thunar-archive-plugin thunar-media-tags-plugin xfce4-battery-plugin xfce4-clipman-plugin xfce4-cpufreq-plugin xfce4-cpugraph-plugin xfce4-diskperf-plugin xfce4-fsguard-plugin xfce4-genmon-plugin xfce4-mount-plugin xfce4-mpc-plugin xfce4-netload-plugin xfce4-notifyd xfce4-pulseaudio-plugin xfce4-screenshooter xfce4-sensors-plugin xfce4-systemload-plugin xfce4-taskmanager xfce4-time-out-plugin xfce4-timer-plugin xfce4-wavelan-plugin xfce4-verve-plugin xfce4-whiskermenu-plugin xfce4-xkb-plugin")
            print("You need to start XFCE in tty. You can write startxfce4 after login.")
            input("Press enter to continue.")
            clear()
elif deskenv == "kde plasma":
    print("You can press LShift+Alt+F12 enable/disable compositor. (Compositor is costs %30 performance ingame)")
    if deq == "y":
        print("Installing KDE Plasma...")
        system("sudo pacman -S plasma dolphin konsole sddm xorg xorg-xinit")
        system("sudo systemctl enable sddm")
        input("Press enter to continue.")
        clear()
elif deskenv == "gnome":
    print("You have nothing to do for compositor. But use X11! Wayland is still bad for gaming, and unredirection is'nt working!")
    gnomevarriants = input("What variant do you want to install? (normal gnome/debloated gnome) : ")
    clear()
    if gnomevarriants == "normal gnome":
        print("Installing normal GNOME...")
        system("sudo pacman -S --needed gnome gdm xorg xorg-xinit")
        system("sudo systemctl enable gdm")
        input("Press enter to continue.")
        clear()
    elif gnomevarriants == "debloated gnome":
        print("Installing debloated GNOME...")
        system("sudo pacman -S --needed xorg xorg-xinit gdm eog evince file-roller gnome-backgrounds gnome-characters gnome-color-manager gnome-terminal gnome-control-center gnome-disk-utility gnome-menus gnome-session gnome-settings-daemon gnome-shell gnome-shell-extensions gnome-text-editor gnome-tweaks gvfs gvfs-afc gvfs-mtp nautilus xdg-user-dirs-gtk xdg-desktop-portal xdg-desktop-portal-gnome xdg-desktop-portal-gtk xdg-user-dirs xdg-utils")
        system("sudo systemctl enable gdm")
        input("Press enter to continue.")
        clear()

if soundtweaks == "y":
    print("Installing Pipewire...")
    system("sudo pacman -S pipewire-pulse pipewire-audio pipewire-jack pipewire-alsa wireplumber")
    input("Press enter to continue.")
    clear()

if caur == "y":
    print("Installing Chaotic AUR...")
    system("sudo pacman-key --recv-key 3056513887B78AEB --keyserver keyserver.ubuntu.com")
    system("sudo pacman-key --lsign-key 3056513887B78AEB")
    system("sudo pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst' 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'")
    print("When pacman.conf is opened, write go to bottom and write (You can copy): ")
    print("[chaotic-aur]")
    print("Include = /etc/pacman.d/chaotic-mirrorlist")
    input("Press enter to continue.")
    system("sudo nano /etc/pacman.conf")
    input("Press enter to continue.")
    clear()

if winedh == "y":
    print("Installing Wine dependency hell...")
    system("sudo pacman -Syu")
    system("sudo pacman -S --needed wine-staging winetricks giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo libxcomposite lib32-libxcomposite libxinerama lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader cups samba dosbox")
    input("Press enter to continue.")
    clear()

if gpu == "amd":
    print("Installing needed drivers for AMD...")
    system("sudo pacman -S --needed lib32-mesa vulkan-radeon lib32-vulkan-radeon vulkan-icd-loader lib32-vulkan-icd-loader")
    input("Press enter to continue.")
    qamd = input("Do you want to reduce input lag with AMD Xorg parameters? (This will not work on Wayland) (y/n) : ")
    if qamd == "y":
        print("Copy that things:")
        print("----------------:")
        with open('amdtweaks.txt') as f:
            amdtweak = f.read()
            print(amdtweak)
        input("Press enter to continue.")
        print("When the page is opened, copy that things and save. Your input lag will reduce with that options. (TearFree, EnablePageFlip etc.)")
        input("Press enter to continue.")
        system("sudo nano /etc/X11/xorg.conf.d/20-amdgpu.conf")
        input("Press enter to continue.")
    clear()
elif gpu == "nvidia":
    print("Installing needed drivers for NVIDIA...")
    print("https://nouveau.freedesktop.org/CodeNames.html look at this website for your GPU's serie.")
    gpuserie = input("Write down your GPU's serie (only maxwell, turing, kepler, fermi, tesla, curie, ampere, pascal, ) : ")
    if gpuserie == "maxwell":
        system("sudo pacman -S nvidia-dkms nvidia-settings nvidia-utils opencl-nvidia python-pycuda lib32-libvdpau lib32-nvidia-utils lib32-opencl-nvidia vkd3d lib32-vkd3d vulkan-icd-loader lib32-vulkan-icd-loader")
        input("Press enter to continue")
        clear()
    elif gpuserie == "pascal":
        system("sudo pacman -S nvidia-dkms nvidia-settings nvidia-utils opencl-nvidia python-pycuda lib32-libvdpau lib32-nvidia-utils lib32-opencl-nvidia vkd3d lib32-vkd3d vulkan-icd-loader lib32-vulkan-icd-loader")
        input("Press enter to continue")
        clear()
    elif gpuserie == "turing":
        system("sudo pacman -S nvidia-dkms nvidia-settings nvidia-utils opencl-nvidia python-pycuda lib32-libvdpau lib32-nvidia-utils lib32-opencl-nvidia vkd3d lib32-vkd3d vulkan-icd-loader lib32-vulkan-icd-loader")
        input("Press enter to continue")
        clear()
    elif gpuserie == "ampere":
        system("sudo pacman -S nvidia-dkms nvidia-settings nvidia-utils opencl-nvidia python-pycuda lib32-libvdpau lib32-nvidia-utils lib32-opencl-nvidia vkd3d lib32-vkd3d vulkan-icd-loader lib32-vulkan-icd-loader")
        input("Press enter to continue")
        clear()
    elif gpuserie == "kepler":
        system("sudo pacman -S nvidia-470xx-dkms nvidia-settings nvidia-utils opencl-nvidia python-pycuda lib32-libvdpau lib32-nvidia-utils lib32-opencl-nvidia vkd3d lib32-vkd3d vulkan-icd-loader lib32-vulkan-icd-loader")
        input("Press enter to continue")
    elif gpuserie == "tesla":
        system("sudo pacman -S nvidia-340xx-dkms nvidia-settings nvidia-utils opencl-nvidia python-pycuda lib32-libvdpau lib32-nvidia-utils lib32-opencl-nvidia vkd3d lib32-vkd3d vulkan-icd-loader lib32-vulkan-icd-loader")
        input("Press enter to continue")
        clear()
    elif gpuserie == "fermi":
        system("sudo pacman -S nvidia-390xx-dkms nvidia-settings nvidia-utils opencl-nvidia python-pycuda lib32-libvdpau lib32-nvidia-utils lib32-opencl-nvidia vkd3d lib32-vkd3d vulkan-icd-loader lib32-vulkan-icd-loader")
        input("Press enter to continue")
        clear()

if lutris == "y":
    print("Installing Lutris...")
    system("sudo pacman -S lutris")
    input("Press enter to continue")
    clear()

if steamnative == "y":
    print("Installing Steam-Native with other gaming tools...")
    system(f"{aurhelper} -S --needed vkd3d wine-mono lib32-vkd3d wine-staging winetricks bottles protontricks-git protonup-qt dxvk-bin lib32-libldap giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo libxcomposite lib32-libxcomposite libxinerama lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader cups samba dosbox gamemode innoextract lib32-gamemode lib32-vkd3d vkd3d")
    input("Press enter to continue")
    clear()

if winecfg == "y":
    print('When Wine Configuration is opened, go to "Libraries" and add d3d10, d3d11 and d3dcompiler_47 libraries. d3d10 and d3d11 need to be native.')
    input("Press enter to continue")
    system("winecfg")
    input("Press enter to continue")
    clear()

if grubp == "y":
    print("Warning! When you apply this settings, your system will not safe for CPU vulnerabilities. Use at your own risk! (I was using this parameters, I did'nt see any problem in my system. When you apply this your performance will be perfect but use at your own risk) Other thing, you need to be careful when doing this. If you do wrong things, the system will not open with GRUB. Use at your own risk, again! I'm not taking responsibility!")
    input("Press enter to continue")
    print("Copy this parameters:")
    print("split_lock_detect=off mitigations=off")
    print(" ")
    print("Find the GRUB_CMDLINE_LINUX_DEFAULT and write this parameters to the end of GRUB_CMDLINE_LINUX_DEFAULT, it needs to be similar like that:")
    print("GRUB_CMDLINE_LINUX_DEFAULT='nowatchdog loglevel=3 split_lock_detect=off mitigations=off")
    input("Press enter to continue")
    system("sudo nano /etc/default/grub")
    input("Press enter to continue")
    system("grub-mkconfig -o /boot/grub/grub.cfg")
    input("Press enter to continue")
    clear()

if sysctls == "y":
    print("Warning! This can break your system, pc! Be careful when you doing this! Use at your own risk! I'm not taking responsibility!")
    ram = input("How many is your RAM? (2, 4, 8, 8>) : ")
    if ram == "2":
        print("Do not use this tweak!")
    elif ram == "4":
        print("Do not use this tweak!")
    elif ram == "8":
        if swap == "y":
            if sorh == "ssd":
                print("When nano page is opened, write down this things (you can copy) : ")
                with open('ssd.txt') as f:
                    ssdset = f.read()
                    print(ssdset)
                    system("sudo nano /etc/sysctl.d/99-settings.conf")
                    input("Press enter to continue")
                    clear()
            elif sorh == "hdd":
                with open('hdd.txt') as f:
                    hddset = f.read()
                    print(hddset)
                    system("sudo nano /etc/sysctl.d/99-settings.conf")
                    input("Press enter to continue")
                    clear()
        elif swap == "n":
            with open('normal.txt') as f:
                    normalset = f.read()
                    print(normalset)
                    system("sudo nano /etc/sysctl.d/99-settings.conf")
                    input("Press enter to continue")
                    clear()

if multigpu == "y":
    if intelnvidia == "y":
        system("sudo pacman -S --needed mesa lib32-mesa libva-intel-driver lib32-libva-intel-driver primus_vk python-pycuda lib32-libvdpau lib32-nvidia-utils lib32-opencl-nvidia lib32-primus_vk python-glfw vkd3d lib32-vkd3d")
        print("Installing nvidia-prime...")
        print("You can run apps with nvidia-prime, use prime-run <program>")
        input("Press enter to continue")
        clear()
        system("sudo pacman -S nvidia-prime")
        input("Press enter to continue")
        clear()
        print("When GRUB config is opened, find GRUB_CMDLINE_LINUX_DEFAULT and write nvidia-drm.modeset=1 the start of the script")
        system("sudo nano /etc/default/grub")
        input("Press enter to continue")
        system("grub-mkconfig -o /boot/grub/grub.cfg")
        input("Press enter to continue")
        clear()
        print("https://wiki.cachyos.org/en/notebooks look at this website!")
        input("Press enter to continue")
        clear()