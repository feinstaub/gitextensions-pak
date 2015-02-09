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
# (see for example https://build.opensuse.org/package/show/home:codeminister/GitExtensions)
Name:          GitExtensions

Summary:       Standalone Git Repository Tool
Version:       2.48.03
Release:       1
License:       GPL-3.0+
Group:         Development/Tools/Version Control
Url:           http://sourceforge.net/projects/gitextensions/
Source0:       %{name}-%{version}-Mono.zip
Source1:       gitext
Source2:       %{name}.desktop
Source3:       %{name}.png
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
BuildArch:     noarch
# note that mono is not (yet) required for build because we use the prebuilt zip file
BuildRequires: mono-core mono-devel unzip
BuildRequires: update-desktop-files
# disable auto dep scanning:
AutoReqProv:   no
Requires:      mono-core mono-extras mono-winforms

%description
Git Extensions is a toolkit to make working with Git more intuitive.
It is implemented in .NET/WinForms and designed to also run on Linux using mono.
The commandline executable is called gitext.
The noarch part currently installs to /opt which should be fixed according to RPMLINT.


%prep
# see http://www.rpm.org/max-rpm/s1-rpm-inside-macros.html
# %%setup: unpack the original sources
# -q unknown option: leave it away
# -n <name> - Set Name of Build Directory
%setup -n %{name}


%build
# Nothing to build


%install
# install to /opt/GitExtensions
install -d %{buildroot}/opt/%{name}
cp -v -R * %{buildroot}/opt/%{name}
rm %{buildroot}/opt/%{name}/gitext.sh

# taken from https://build.opensuse.org/package/view_file/home:Warhammer40k:stuff/GitExtensions/GitExtensions.spec
# copy gitext executable, note the trailing slash
install -d %{buildroot}/%{_bindir}/
# todo: what do all the parameters say?
install -p -D -m 0755 %{SOURCE1} %{buildroot}/%{_bindir}/

# taken from https://build.opensuse.org/package/view_file/network/FreeFileSync/FreeFileSync.spec (does not work)
# copy .desktop
install -d %{buildroot}/%{_datadir}/applications/
install -p %{SOURCE2} %{buildroot}/%{_datadir}/applications/

# copy .png file
install -d %{buildroot}/%{_datadir}/pixmaps/
install -p %{SOURCE3} %{buildroot}/%{_datadir}/pixmaps/

# todo: what does the -i mean?
# Obsoleted?? http://lists.opensuse.org/opensuse-packaging/2011-12/msg00177.html
%suse_update_desktop_file -i %name


%clean
%__rm -rf "%{buildroot}"


%files
%defattr(-,root,root,-)
%{_bindir}/gitext
%dir /opt/%{name}
/opt/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Feb 9 2015 Gregor Mi <codestruct@posteo.org> - 2.48.03
- package created based on https://build.opensuse.org/package/view_file/home:Warhammer40k:stuff/GitExtensions/GitExtensions.spec
  and https://build.opensuse.org/package/view_file/network/FreeFileSync/FreeFileSync.spec
  There are some RPMLINT issues.
