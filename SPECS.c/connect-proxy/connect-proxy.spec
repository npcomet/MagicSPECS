Name:           connect-proxy
Version:        1.100
Release:        9%{?dist}
Summary:        SSH Proxy command helper
Summary(zh_CN.UTF-8): SSH 代理辅助命令

Group:          Applications/System
Group(zh_CN.UTF-8): 应用程序/系统
License:        GPLv2+
URL:            http://www.taiyo.co.jp/~gotoh/ssh/connect.html
Source0:        connect-%{version}.c
# Real source listed below, it was renamed for sanity's sake
#Source0:        http://www.taiyo.co.jp/~gotoh/ssh/connect.c
Source1:        http://www.taiyo.co.jp/~gotoh/ssh/connect.html
Patch0:         connect-proxy-make-man.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       openssh

%description
connect-proxy is the simple relaying command to make network connection via
SOCKS and https proxy. It is mainly intended to be used as proxy command
of OpenSSH. You can make SSH session beyond the firewall with this command.

Features of connect-proxy are:

    * Supports SOCKS (version 4/4a/5) and https CONNECT method.
    * Supports NO-AUTH and USERPASS authentication of SOCKS
    * Partially supports telnet proxy (experimental).
    * You can input password from tty, ssh-askpass or environment variable.
    * Simple and general program independent from OpenSSH.
    * You can also relay local socket stream instead of standard I/O.

%description -l zh_CN.UTF-8
SSH 代理辅助命令。可以支持 SOCKS4/5 和 https 代理。

%prep
#setup -q -T -c -n %{name}-%{version}
%setup -q -T -c
cp %{SOURCE0} connect.c
cp %{SOURCE1} .
%patch0 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp -p %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc connect.html
%{_mandir}/man1/*
%{_bindir}/%{name}

%changelog
* Sat Nov 07 2015 Liu Di <liudidi@gmail.com> - 1.100-9
- 为 Magic 3.0 重建

* Wed Oct 28 2015 Liu Di <liudidi@gmail.com> - 1.100-8
- 为 Magic 3.0 重建

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.100-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.100-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.100-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.100-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.100-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.100-2
- fix license tag

* Wed Feb 13 2008 Jarod Wilson <jwilson@redhat.com> 1.100-1
- Upgrade to r100.

* Tue Sep 05 2006 Jarod Wilson <jwilson@redhat.com> 1.95-5
- Rebuild for new glibc

* Wed Jul 05 2006 Jarod Wilson <jwilson@redhat.com> 1.95-4
- Minor spec cleanups
- Add copy of html doc page

* Wed Jul 05 2006 Jarod Wilson <jwilson@redhat.com> 1.95-3
- Rename source file with version for sanity's sake

* Wed Jul 05 2006 Jarod Wilson <jwilson@redhat.com> 1.95-2
- Fix BuildRoot and enable CFLAGS

* Wed Jul 05 2006 Jarod Wilson <jwilson@redhat.com> 1.95-1
- Initial build for Fedora Extras

* Wed Dec 12 2005 Jarod Wilson <jarod@wilsonet.com> 1.93-1
- Initial build
