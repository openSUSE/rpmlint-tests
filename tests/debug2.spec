Name:		debug2
Version:	0
Release:	0
Group:          Development/Tools/Building
Summary:	Lorem ipsum
License:	Public Domain
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
cat <<EOF > t.c
int main(void)
{
	return 0;
}
EOF
gcc -g $RPM_OPT_FLAGS -o t.o -c t.c
gcc -g $RPM_OPT_FLAGS -o t t.o
ar rs t.a t.o
cp -a t.a t2.a
strip --strip-debug t.a
strip t2.a

%install
install -D -m 755 t %buildroot/usr/bin/t
install -D -m 644 t.a %buildroot/usr/lib/foo/t.a
install -D -m 644 t2.a %buildroot/usr/lib/foo/t2.a

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
/usr/bin/t
/usr/lib/foo/*

%changelog
* Mon Apr 18 2011 lnussel@suse.de
- dummy
