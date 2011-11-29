Name:		license1
Version:	0
Release:	0
Group:          Development/Tools/Building
Summary:	Lorem ipsum
License:	GPL-2.0+ or GPLv2+ and BSD-2-Clause ; BSL-1.0
BuildRoot:	%_tmppath/%name-%version-build
Url:            http://www.opensuse.org/
BuildArch:      noarch

%description
Check the license tag parser

%prep
%build

%install
install -d -m 755 %buildroot/usr/lib/dummy 

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%dir /usr/lib/dummy

%changelog
* Mon Apr 18 2011 lnussel@suse.de
- dummy
