%global         git_commit 5cff3c5
Name:           libnm-qt
Version:        0.9.8.2
Release:        1.20140422%{git_commit}%{?dist}
Epoch:          2
Summary:        Qt-only wrapper for NetworkManager DBus API

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            https://projects.kde.org/projects/extragear/libs/libnm-qt
# Source0:        http://download.kde.org/unstable/networkmanagement/%{version}/src/%{name}-%{version}.tar.xz
# # Package from git snapshots using releaseme scripts
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  cmake >= 2.6
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  libmm-qt-devel >= 1.0.0
BuildRequires:  pkgconfig(NetworkManager) >= 0.9.8
BuildRequires:  pkgconfig(ModemManager) >= 1.0.0
BuildRequires:  pkgconfig(libnm-glib) pkgconfig(libnm-util)

Requires:  NetworkManager >= 0.9.9.0

%description
Qt library for NetworkManager

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description devel
Qt libraries and header files for developing applications
that use NetworkManager

%prep
%setup -qn %{name}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}

make install/fast  DESTDIR=%{buildroot} -C %{_target_platform}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libNetworkManagerQt.so*


%files devel
%{_libdir}/pkgconfig/NetworkManagerQt.pc
%{_libdir}/libNetworkManagerQt.so
%{_includedir}/NetworkManagerQt/

%changelog
* Thu May 22 2014 Jan Grulich <jgrulich@redhat.com> - 2:0.9.8.2-1.20140422git5cff3c5
- update to git snapshot

* Tue Feb 25 2014 Jan Grulich <jgrulich@redhat.com> - 1:0.9.9.1-1.20140225gitb7f3d65
- Update to 0.9.9.1 (development version)

* Thu Nov 21 2013 Jan Grulich <jgrulich@redhat.com> - 1:0.9.8.0-1
- Update to 0.9.8.0 (stable release)

* Wed Oct 9 2013 Jan Grulich <jgrulich@redhat.com> - 1:0.9.1-1.20131009git5af966a
- Update to current git snapshot

* Tue Sep 10 2013 Jan Grulich <jgrulich@redhat.com - 1:0.9.0-1
- First stable release (0.9.0)

* Mon Aug 12 2013 Lukas Tinkl <ltinkl@redhat.com> - 0.9.8-4.20130812gitecf9fc
- Update to current git snapshot
- VPN, 3G modem and other fixes

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-3.20130613git1a1bda4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 13 2013 Jan Grulich <jgrulich@redhat.com> - 0.9.8-2.20130613git1a1bda4
- Update to the current git snapshot

* Fri May 31 2013 Jan Grulich <jgrulich@redhat.com> - 0.9.8-1.20130527git0dd3793
- Initial package
- Based on git snapshot 0dd379383ac6c1bdbdaf9044ca9a6c43c6df8d23
