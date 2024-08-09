Name:       logmein-hamachi-systemd
Version:    2.1.0.203
Release:    2
Summary:    Repack of Logmein Hamachi to use modern sd-init files
License:    Proprietary

%description
Repackage of logmein-hamachi to use systemd service files instead of sysvinit scripts

LogMeIn Hamachi is a virtual private network application developed and released in 2004 by Alex Pankratov. It is capable of establishing direct links between computers that are behind network address translation firewalls without requiring reconfiguration.

%prep
wget https://vpn.net/installers/logmein-hamachi-2.1.0.203-1.x86_64.rpm

%build
cat <<EOF > logmein-hamachi.service
[Unit]
Description=Logmein Hamachi

[Service]
ExecStart=/usr/libexec/logmein-hamachi/hamachid
Type=forking

[Install]
WantedBy=network.target
EOF
cat <<EOF > logmein-hamachi.socket
[Unit]
Description=Logmein Hamachi

[Socket]
ListenStream=/run/logmein-hamachi/ipc.sock

[Install]
WantedBy=sockets.target
EOF
rpm2cpio logmein-hamachi-2.1.0.203-1.x86_64.rpm | cpio --extract --to-stdout ./opt/logmein-hamachi/bin/hamachid > hamachid
rpm2cpio logmein-hamachi-2.1.0.203-1.x86_64.rpm | cpio --extract --to-stdout ./opt/logmein-hamachi/LICENSE > LICENSE

%install
mkdir -p %{buildroot}/usr/libexec/logmein-hamachi %{buildroot}/usr/lib/systemd/system %{buildroot}/usr/bin
install -m 755 hamachid %{buildroot}/usr/libexec/logmein-hamachi/hamachid
ln -s ../libexec/logmein-hamachi/hamachid %{buildroot}/usr/bin/hamachi
install -m 644 logmein-hamachi.service %{buildroot}/usr/lib/systemd/system/logmein-hamachi.service
install -m 644 logmein-hamachi.socket %{buildroot}/usr/lib/systemd/system/logmein-hamachi.socket

%files
/usr/bin/hamachi
/usr/lib/systemd/system/logmein-hamachi.service
/usr/lib/systemd/system/logmein-hamachi.socket
/usr/libexec/logmein-hamachi/hamachid
