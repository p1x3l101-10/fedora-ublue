#!/bin/bash

set -ouex pipefail

RELEASE="$(rpm -E %fedora)"

wget --output-document='/etc/yum.repos.d/home:mkittler.repo' 'https://download.opensuse.org/repositories/home:/mkittler/Fedora_40/home:mkittler.repo'
sed -i '0,/skip_if_unavailable/{s/enabled=0/enabled=1/}' /etc/yum.repos.d/rpmfusion-nonfree-steam.repo

rpm-ostree install steam-devices syncthing syncthingctl-qt6 syncthingfileitemaction-qt6 syncthingplasmoid-qt6
rpm-ostree uninstall filelight kwalletmanager5
