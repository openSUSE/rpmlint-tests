Name:		rclink5
Version:	0
Release:	0
Group:          Development/Tools/Building
Summary:	Test with service and rclink
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
install -d -m 755 %buildroot/etc/init.d
install -d -m 755 %buildroot/usr/lib/systemd/system
install -d -m 755 %buildroot/usr/sbin
install -m 644 /dev/null %buildroot/usr/lib/systemd/system/blah.service
ln -s /etc/init.d/blah %buildroot/usr/sbin/rcblah

%pre
%service_add_pre blah.service

%preun
%service_del_preun blah.service

%post
%service_add_post blah.service

%postun
%service_del_postun blah.service

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
#/etc/init.d/*
/usr/lib/systemd/system/*
/usr/sbin/*

%changelog
* Mon Apr 18 2011 lnussel@suse.de
- dummy
