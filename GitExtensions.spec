#
# spec file for package GitExtensions
#
# Copyright (c) 2015 Gregor Mi
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# No   Date    Author           Changelog
# --   ----    ------           ---------
#  1   2015    codeminister     init

# The 'Name' must match the openSUSE build service package name
# in order to get a properly filled download page
# (see for example https://build.opensuse.org/package/show/home:codeminister/TODO)
Name:           GitExtensions

Summary:        Standalone Git Repository Tool
Version:        2.48.03
Release:        1
License:        GPL-3.0+

# TODO
Group:          Productivity

Url:            http://sourceforge.net/projects/gitextensions/
Source0:        %{name}-%{version}-Source.zip
Source1:        %{name}.desktop
Source2:        %{name}.png

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  unzip

%description
GitExtensions is a shell extension, a Visual Studio 2008/2010/2012 plugin and a standalone Git repository tool.
It is a toolkit to make working with Git under Windows more intuitive.
The shell extension will integrate in Windows Explorer and presents a nice context menu on files.
A Mono build is provided to run it also under Linux.


%prep


%build


%install


%clean


%files


%changelog
