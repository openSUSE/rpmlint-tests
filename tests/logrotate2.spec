Name:		logrotate2
Version:	0
Release:	0
Group:          Development/Tools/Building
Summary:	Lorem ipsum
License:	GPL-2.0+
BuildRoot:	%_tmppath/%name-%version-build
Url:            http://www.opensuse.org/
BuildArch:      noarch
Requires:       logrotate

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
install -d -m 755 %buildroot/var/log/foo{1,2,3,4,5,6}
install -m 644 /dev/null %buildroot/var/log/foo6/log
install -m 644 /dev/null %buildroot/var/log/foo.log

install -d -m 755 %buildroot/etc/logrotate.d
cat > %buildroot/etc/logrotate.d/logrotate2 <<EOF
/var/log/foo1/log /var/log/foo2/log {
    compress
    dateext
    maxage 365
    rotate 99
    size=+1024k
    notifempty
    missingok
    copytruncate
}

/var/log/foo3/log {
    compress
}

# good entry
/var/log/foo4/log {
    su daemon root
}

/var/log/foo5/log {
    su foo bar
}
EOF
cat > %buildroot/etc/logrotate.d/logrotate2b <<EOF
/var/log/foo5/log {
    compress
}

/var/log/foo6/log {
    compress
}

/var/log/foo.log {
    compress
}
EOF

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%config /etc/logrotate.d/*
%dir %attr(0700, daemon, root) /var/log/foo1
%dir %attr(0770, root, daemon) /var/log/foo2
%dir %attr(0555, daemon, root) /var/log/foo3
%dir %attr(0555, daemon, root) /var/log/foo4
%dir %attr(0755, root, root) /var/log/foo5
%ghost %attr(0644, root, root) /var/log/foo6/log
%ghost %attr(0644, root, root) /var/log/foo.log

%changelog
* Mon Apr 18 2011 lnussel@suse.de
- dummy
