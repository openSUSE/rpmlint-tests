Name:		systemd-good
Version:	0
Release:	0
Group:          Development/Tools/Building
Summary:	Lorem ipsum
License:	GPL-2.0+
Url:            http://www.opensuse.org/
BuildArch:      noarch

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
cat > foobar.service <<EOF
[Unit]
Description=Foobar Daemon

[Service]
ExecStart=/usr/sbin/foobar

[Install]
WantedBy=multi-user.target
EOF

%install
mkdir -p %buildroot%{_sbindir}
ln -s service %buildroot%{_sbindir}/rcfoobar
install -D -m 644 foobar.service %buildroot/usr/lib/systemd/system/foobar.service

%pre
%service_add_pre foobar.service

%preun
%service_del_preun foobar.service

%post
%service_add_post foobar.service

%postun
%service_del_postun foobar.service

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{_sbindir}/rcfoobar
/usr/lib/systemd/system/foobar.service

%changelog
* Mon Apr 18 2011 lnussel@suse.de
- dummy
