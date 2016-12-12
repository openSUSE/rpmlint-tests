%define soname 42
%define basename zork

Name:           zork4
Version:        1.2.3
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

%package -n libzork%{soname}
Group:          Development/Tools/Building
Summary:        Lorem ipsum
Provides:       %{name}-libs = %{version}

%description -n libzork%{soname}
Lorem ipsum dolor sit amet.

%package devel
Group:          Development/Tools/Building
Summary:        Lorem ipsum
# Does not fulfill requirement for corresponding library package ...
Requires:       libzork%{soname}-aux
Requires:       libzork%{soname}-data = %{version}
# but this one does, so package is ok
Requires:       %{name}-libs = %{version}

%description devel
Lorem ipsum dolor sit amet.

%prep
%build

%install
install -d -m 755 %buildroot/usr/lib
echo "void foobar() {}" >xx.c
gcc -O2 -shared -Wl,-soname,libzork.so.%{soname} xx.c -o %buildroot/usr/lib/libzork.so.%{soname}
strip %buildroot/usr/lib/libzork.so.%{soname}
ln -s libzork.so.%{soname} %buildroot/usr/lib/libzork.so

%clean
rm -rf %buildroot

%post -n libzork%{soname} -p /sbin/ldconfig

%postun -n libzork%{soname} -p /sbin/ldconfig

%files -n libzork%{soname}
/usr/lib/*so.*

%files devel
/usr/lib/*so

%changelog
* Mon Dec 12 2016 stefan.bruens@rwth-aachen.de
- dummy
