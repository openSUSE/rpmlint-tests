Name:		permissions2
Version:	0
Release:	0
Group:          Development/Tools/Building
Summary:	Lorem ipsum
License:	GPL-2.0+
BuildRoot:	%_tmppath/%name-%version-build
Url:            http://www.opensuse.org/
PreReq:         permissions

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
install -d -m 755 %buildroot/bin
cp /bin/su %buildroot/bin

%clean
rm -rf %buildroot

%verifyscript
%verify_permissions -e /bin/su

%post
%set_permissions /bin/su

%files
%defattr(-,root,root)
%attr(4755,root,root) /bin/su

%changelog
* Mon Apr 18 2011 lnussel@suse.de
- dummy
