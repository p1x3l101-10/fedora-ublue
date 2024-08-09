#!/bin/bash

set -ouex pipefail

RELEASE="$(rpm -E %fedora)"

wget --output-document='/etc/yum.repos.d/home:mkittler.repo' 'https://download.opensuse.org/repositories/home:/mkittler/Fedora_40/home:mkittler.repo'
sed -i '0,/skip_if_unavailable/{s/enabled=0/enabled=1/}' /etc/yum.repos.d/rpmfusion-nonfree-steam.repo

rpm-ostree install steam-devices syncthing syncthingctl-qt6 syncthingfileitemaction-qt6 syncthingplasmoid-qt6
rpm-ostree uninstall filelight kwalletmanager5 solaar
rpm-ostree install /tmp/files/rpms/logmein-hamachi-systemd/logmein-hamachi-systemd-2.1.0.203-1.x86_64.rpm

# Hide syncthing apps
echo "Hidden=true" >> /usr/share/syncthing-ui.desktop
echo "Hidden=true" >> /usr/share/syncthing-start.desktop
