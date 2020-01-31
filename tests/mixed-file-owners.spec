#
# spec file for package mixed-file-owners
#
# Copyright (c) 2019 SUSE LLC.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           mixed-file-owners
Version:        1
Release:        0
Summary:        Test package with a file hierarchy with mixed users
License:        GPL-2.0+
Url:            https://www.opensuse.org/

%description
description of the package that is longer than the summary so it has some filler text

%install
mkdir -p ${RPM_BUILD_ROOT}/%_datadir/foo/{bar,baz}

%files
%dir %attr(-,bin,root) %_datadir/foo
# bad: user 'foo' has control over root-owned file
%dir %attr(-,root,root) %_datadir/foo/bar
# good: file owner matches dir owner
%dir %attr(-,bin,root) %_datadir/foo/baz

%changelog
* Fri Jan 17 2020 malte.kraus@suse.com
 - change history of the spec
