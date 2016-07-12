Name:		chroot
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
# int chroot(const char *path);
# int chdir(const char *path);

cat <<EOF > call_chroot.c
#include <unistd.h>
int main(void)
{
    return chroot("") > 0;
}
EOF

cat <<EOF > call_chroot_with_chdir.c
#include <unistd.h>
int main(void)
{
    int a = chroot("");
    int b = chdir("");
    return a + b;
}
EOF

%install
for f in chroot chroot_with_chdir; do
    gcc $RPM_OPT_FLAGS -o call_$f call_$f.c
    strip call_$f
    install -D -m 755 call_$f %buildroot/usr/bin/call_$f
done

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
/usr/bin/*

%changelog
* Fri Jul 08 2016 stefan.bruens@rwth-aachen.de
- dummy
