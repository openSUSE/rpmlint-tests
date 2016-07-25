Name:		gethostbyname
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

cat <<EOF > call_gethostbyname.c
#include <netdb.h>
int main(void)
{
    return gethostbyname("") > 0;
}
EOF

cat <<EOF > call_gethostbyname2.c
#include <netdb.h>
int main(void)
{
    return gethostbyname2("", 0) > 0;
}
EOF

cat <<EOF > call_gethostbyaddr.c
#include <netdb.h>
int main(void)
{
    return gethostbyaddr(0, 0, 0) > 0;
}
EOF

cat <<EOF > call_gethostbyaddr_r.c
#include <netdb.h>
int main(void)
{
    return gethostbyaddr_r(0, 0, 0,  0, 0, 0, 0, 0) > 0;
}
EOF

cat <<EOF > call_gethostbyname_r.c
#include <netdb.h>
int main(void)
{
    return gethostbyname_r("", 0, 0, 0, 0, 0) > 0;
}
EOF

cat <<EOF > call_gethostbyname2_r.c
#include <netdb.h>
int main(void)
{
    return gethostbyname2_r("", 0, 0, 0, 0, 0, 0) > 0;
}
EOF

%install
for f in gethostbyname gethostbyname2 gethostbyaddr gethostbyaddr_r gethostbyname_r gethostbyname2_r; do
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
* Sat Mar 05 2016 stefan.bruens@rwth-aachen.de
- dummy
