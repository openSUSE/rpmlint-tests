Name:		permissions1
Version:	0
Release:	0
Group:          Development/Tools/Building
Summary:	Lorem ipsum
License:	GPL-2.0+
BuildRoot:	%_tmppath/%name-%version-build
Url:            http://www.opensuse.org/

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
install -d -m 755 %buildroot/etc/permissions.d
install -d -m 755 %buildroot/usr/share/permissions/permissions.d
install -d -m 755 %buildroot/bin
install -d -m 755 %buildroot/usr/bin
echo "/bin/foo root:root 4755" > %buildroot/etc/permissions.d/test
echo "/bin/foo root:root 4755" > %buildroot/usr/share/permissions/permissions.d/test

echo "int main() {}" > xx.c
gcc -fno-PIE -O2 xx.c -o %buildroot/bin/ls
strip %buildroot/bin/ls
cp %buildroot/bin/ls %buildroot/usr/bin/su

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%config /etc/permissions.d/test
%attr(0644,root,root) /usr/share/permissions/permissions.d/test
%attr(4755,root,root) /bin/ls
%attr(0755,root,bin) /usr/bin/su

%changelog
* Mon Apr 18 2011 lnussel@suse.de
- dummy
