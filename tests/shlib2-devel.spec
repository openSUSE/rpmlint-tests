Name:		shlib2-devel
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
install -d -m 755 %buildroot%_libdir
echo "void foobar() {}" >xx.c
gcc -O2 -shared -Wl,-soname,libfoo.so.1 xx.c -o %buildroot%_libdir/libfoo.so.1
strip %buildroot%_libdir/libfoo.so.1
ln -s libfoo.so.1 %buildroot%_libdir/libfoo.so
gcc -O2 -shared -Wl,-soname,libfoo-2.so xx.c -o %buildroot%_libdir/libfoo-2.so
# should cause no error
cp /etc/motd %buildroot%_libdir/libfoo-2.so.foo

%clean
rm -rf %buildroot

%files
%_libdir/*

%changelog
* Mon Apr 18 2011 lnussel@suse.de
- dummy
