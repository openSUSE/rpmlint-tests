Name:		opt2
Version:	0
Release:	0
Group:          Development/Tools/Building
Summary:	Lorem ipsum
License:	Public Domain
BuildRoot:	%_tmppath/%name-%version-build
Url:            http://www.opensuse.org/
BuildArch:      noarch
Vendor:         xxSUSE yy

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
mkdir -p %buildroot/opt/novell/
mkdir -p %buildroot/opt/suse/
echo test %buildroot/opt/suse/blah
echo test %buildroot/opt/novell/blah

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
/opt/*

%changelog
* Mon Apr 18 2011 lnussel@suse.de
- dummy
