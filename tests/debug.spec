Name:		debug
Version:	0
Release:	0
Group:          Development/Tools/Building
Summary:	Lorem ipsum
License:	Public Domain
BuildRoot:	%_tmppath/%name-%version-build
Url:            http://www.opensuse.org/

%description
Package has an unstripped binary as well as a stripped library.
debug.env  - build with debuginfo enabled
debug1.env - build with debuginfo disabled
debug2.env - manual rpmlint run

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
