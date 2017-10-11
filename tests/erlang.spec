Name:		erlang
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
cat <<EOF > m.erl
-module(m).
-export([fact/1]).

fact(N) when N>0 -> N * fact(N-1);
fact(0) -> 1.
EOF
erlc +no_debug_info m.erl 

%install
install -D -m 644 m.beam %buildroot/usr/lib/erlang/m.beam

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
/usr/lib/erlang/m.beam

%changelog
* Mon Apr 18 2011 lnussel@suse.de
- dummy
