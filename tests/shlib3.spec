Name:           shlib3
Version:        0
Release:        0
Group:          Development/Tools/Building
Summary:        Lorem ipsum
License:        GPL-2.0+
BuildRoot:      %_tmppath/%name-%version-build
Url:            http://www.opensuse.org/

%description
Lorem ipsum dolor sit amet, consectetur adipisici elit, sed
eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
aliquid ex ea commodi consequat. Quis aute iure reprehenderit in
voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui
officia deserunt mollit anim id est laborum.

%package devel
Group:          Development/Tools/Building
Summary:        Lorem ipsum
# Does not fulfill requirement for corresponding library package
Requires:       shlib3-aux = %{version}

%description devel
Lorem ipsum dolor sit amet.

%prep
%build

%install
install -d -m 755 %buildroot/usr/lib
echo "void foobar() {}" >xx.c
gcc -O2 -shared -Wl,-soname,libfoo.so.3 xx.c -o %buildroot/usr/lib/libfoo.so.3
strip %buildroot/usr/lib/libfoo.so.3
ln -s libfoo.so.3 %buildroot/usr/lib/libfoo.so

%clean
rm -rf %buildroot

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
/usr/lib/*so.*

%files devel
/usr/lib/*so

%changelog
* Mon Dec 12 2016 stefan.bruens@rwth-aachen.de
- dummy
