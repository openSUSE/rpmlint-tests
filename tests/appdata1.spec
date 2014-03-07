Name:		appdata1
Version:	0
Release:	0
Group:          Development/Tools/Building
Summary:	Check validation of appdata.xml
License:	GPL-2.0+
BuildRoot:	%_tmppath/%name-%version-build
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

%install
install -d -m 755 %buildroot/usr/share/appdata

cat > %buildroot/usr/share/appdata/gnome-power-statistics.appdata.xml <<'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2013 First Lastname <your@email.com> -->
<application>
 <id type="desktop">gnome-power-statistics.desktop</id>
 <licence>CC0</licence>
 <name>Power Statistics</name>
 <summary>Observe power management</summary>
 <description>
  <p>
   Power Statistics is a program used to view historical and current battery
   information and will show programs running on your computer using power.

   &error
  </p>
  <p>Example list:</p>
  <ul>
   <li>First item</li>
   <li>Second item</li>
  </ul>
  <p>
  You probably only need to install this application if you are having problems
  with your laptop battery, or are trying to work out what programs are using
  significant amounts of power.
  </p>
 </description>
 <screenshots>
  <screenshot type="default" width="800" height="600">http://www.hughsie.com/en_US/main.png</screenshot>
  <screenshot width="800" height="600">http://www.hughsie.com/en_US/preferences.png</screenshot>
 </screenshots>
 <url type="homepage">http://www.gnome.org/projects/en_US/gnome-power-manager</url>
 <updatecontact>gnome-power-manager-list@gnome.org</updatecontact>
 <project_group>GNOME</project_group>
</application>
EOF

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
/usr/share/appdata

%changelog
* Mon Apr 18 2011 lnussel@suse.de
- dummy
