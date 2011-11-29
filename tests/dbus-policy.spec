Name:		dbus-policy
Version:	0
Release:	0
Group:          Development/Tools/Building
Summary:	Lorem ipsum
License:	GPL-2.0+
BuildRoot:	%_tmppath/%name-%version-build
Url:            http://www.opensuse.org/
BuildArch:      noarch

%description
Lorem ipsum dolor sit amet, consectetur adipisici elit, sed
eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
aliquid ex ea commodi consequat. Quis aute iure reprehenderit in
voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui
officia deserunt mollit anim id est laborum.

%prep
%build

%install
install -d -m 755 %buildroot/usr/share/dbus-1/system-services/
install -d -m 755 %buildroot/etc/dbus-1/system.d/
echo test > %buildroot/usr/share/dbus-1/system-services/org.opensuse.rpmlintfail.service
cat <<EOF > %buildroot/etc/dbus-1/system.d/org.opensuse.rpmlintfail.conf
<buspolicy>
<policy user="root">
<allow send_destination="org.opensuse.rpmlintfail"/>
</policy>
</buspolicy>
EOF

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%config /etc/dbus-1/system.d/*
/usr/share/dbus-1/system-services/*

%changelog
* Mon Apr 18 2011 lnussel@suse.de
- dummy
