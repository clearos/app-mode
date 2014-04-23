
Name: app-mode
Epoch: 1
Version: 1.5.0
Release: 1%{dist}
Summary: Mode Manager - Core
License: LGPLv3
Group: ClearOS/Libraries
Source: app-mode-%{version}.tar.gz
Buildarch: noarch

%description
The Mode app provides a low-level driver system for master/slave mode.

%package core
Summary: Mode Manager - Core
Requires: app-base-core
Requires: app-simple-mode-core
Requires: app-events-core
Requires: csplugin-filewatch
Requires: system-mode-driver

%description core
The Mode app provides a low-level driver system for master/slave mode.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/mode
cp -r * %{buildroot}/usr/clearos/apps/mode/

install -d -m 0755 %{buildroot}/var/clearos/events/mode
install -d -m 0755 %{buildroot}/var/clearos/mode
install -D -m 0644 packaging/filewatch-mode-event.conf %{buildroot}/etc/clearsync.d/filewatch-mode-event.conf

%post core
logger -p local6.notice -t installer 'app-mode-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/mode/deploy/install ] && /usr/clearos/apps/mode/deploy/install
fi

[ -x /usr/clearos/apps/mode/deploy/upgrade ] && /usr/clearos/apps/mode/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-mode-core - uninstalling'
    [ -x /usr/clearos/apps/mode/deploy/uninstall ] && /usr/clearos/apps/mode/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/mode/packaging
%dir /usr/clearos/apps/mode
%dir /var/clearos/events/mode
%dir /var/clearos/mode
/usr/clearos/apps/mode/deploy
/usr/clearos/apps/mode/language
/usr/clearos/apps/mode/libraries
/etc/clearsync.d/filewatch-mode-event.conf
