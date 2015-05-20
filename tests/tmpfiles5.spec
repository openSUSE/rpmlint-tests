Name:		tmpfiles4
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
install -d -m 755 %buildroot/usr/lib/tmpfiles.d
install -d -m 755 %buildroot/var/log
> %buildroot/var/log/foo
cat > %buildroot/usr/lib/tmpfiles.d/foo.conf << EOF
d /var/log/foo  0755  root  root  10d
EOF

%clean
rm -rf %buildroot

%post
%tmpfiles_create /usr/lib/tmpfiles.d/foo.conf

%files
%defattr(-,root,root)
/usr/lib/tmpfiles.d
%ghost /var/log/foo

%changelog
* Mon Apr 18 2011 lnussel@suse.de
- dummy
