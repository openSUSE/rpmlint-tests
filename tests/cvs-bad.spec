Name:		cvs-bad
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

%install
mkdir -p %buildroot/usr/lib/foo/{CVS,RCS}
echo dummy > %buildroot/usr/lib/foo/.cvsignore
echo dummy > %buildroot/usr/lib/foo/CVS/foo
echo dummy > %buildroot/usr/lib/foo/bla,v
echo dummy > %buildroot/usr/lib/foo/RCS/asd

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
/usr/lib/*

%changelog
* Mon Apr 18 2011 lnussel@suse.de
- dummy
