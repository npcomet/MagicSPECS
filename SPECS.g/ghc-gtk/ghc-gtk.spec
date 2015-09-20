# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name gtk

Name:           ghc-%{pkg_name}
Version:        0.13.9
Release:        1%{?dist}
Summary:        Binding to the Gtk+ graphical user interface library

License:        LGPLv2+
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cairo-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-gio-devel
BuildRequires:  ghc-glib-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-pango-devel
BuildRequires:  ghc-text-devel
BuildRequires:  gtk2hs-buildtools
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
# End cabal-rpm deps
# linking libHSgtk.so needs cc1plus
BuildRequires:  gcc-c++

%description
This is the core library of the Gtk2Hs suite of libraries for Haskell based on
Gtk+. Gtk+ is an extensive and mature multi-platform toolkit for creating
graphical user interfaces.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Begin cabal-rpm deps:
Requires:       pkgconfig(gthread-2.0)
Requires:       pkgconfig(gtk+-2.0)
# End cabal-rpm deps
Obsoletes: ghc-gtkglext-devel < 0.11, ghc-soegtk-devel < 0.11, ghc-vte-devel < 0.11
Obsoletes: ghc-gtkglext-prof < 0.11, ghc-soegtk-prof < 0.11, ghc-vte-prof < 0.11


%description devel
This package provides the Haskell %{pkg_name} library development files.


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%ghc_lib_build


%install
%ghc_lib_install

rm %{buildroot}%{ghc_pkgdocdir}/COPYING

# move demos
rm -r %{buildroot}%{_datadir}/%{pkg_name}-%{version}


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license COPYING


%files devel -f %{name}-devel.files
%doc demo


%changelog
* Wed Jul 22 2015 Jens Petersen <petersen@redhat.com> - 0.13.9-1
- update to 0.13.9

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Jens Petersen <petersen@redhat.com> - 0.13.4-1
- update to 0.13.4

* Fri Dec 12 2014 Jens Petersen <petersen@redhat.com> - 0.13.3-1
- update to 0.13.3

* Tue Sep 16 2014 Jens Petersen <petersen@redhat.com> - 0.13.0.0-1
- update to 0.13.0.0
- refresh to cblrpm-0.8.11

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 21 2013 Jens Petersen <petersen@redhat.com> - 0.12.5.0-1
- update to 0.12.5.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Jens Petersen <petersen@redhat.com> - 0.12.4-4
- update to new simplified Haskell Packaging Guidelines

* Sat Feb 23 2013 Kevin Fenzi <kevin@scrye.com> - 0.12.4-3
- Rebuild for broken deps in rawhide

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 19 2012 Jens Petersen <petersen@redhat.com> - 0.12.4-1
- update to 0.12.4

* Sat Nov 17 2012 Jens Petersen <petersen@redhat.com> - 0.12.3.1-4
- update with cabal-rpm

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Jens Petersen <petersen@redhat.com> - 0.12.3.1-2
- change prof BRs to devel

* Thu Jun 21 2012 Jens Petersen <petersen@redhat.com> - 0.12.3.1-1
- update to 0.12.3.1
- no longer need gtk-gthread.h-include.patch

* Fri Jun 15 2012 Jens Petersen <petersen@redhat.com> - 0.12.3-2
- rebuild

* Tue Mar 20 2012 Jens Petersen <petersen@redhat.com> - 0.12.3-1
- update to 0.12.3

* Fri Jan  6 2012 Jens Petersen <petersen@redhat.com> - 0.12.2-1
- update to 0.12.2 and cabal2spec-0.25.2
- workaround gthread.h error "Only <glib.h> can be included directly."

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.12.1-1.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 0.12.1-1.1
- rebuild with new gmp

* Tue Sep 20 2011 Jens Petersen <petersen@redhat.com> - 0.12.1-1
- update to 0.12.1
- add _isa suffix to gtk2-devel depends (see #723558)

* Tue Jun 21 2011 Jens Petersen <petersen@redhat.com> - 0.12.0-5
- BR ghc-Cabal-devel instead of ghc-prof and use ghc_arches (cabal2spec-0.23.2)

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.12.0-4
- Enable build on sparcv9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 Jens Petersen <petersen@redhat.com> - 0.12.0-2
- update to cabal2spec-0.22.4

* Tue Nov 30 2010 Jens Petersen <petersen@redhat.com> - 0.12.0-1
- update to 0.12.0

* Thu Nov 25 2010 Jens Petersen <petersen@redhat.com> - 0.11.2-6
- fix Cabal-1.10 build with ghc7-Gtk2HsSetup-Cabal-1.10.patch
- drop devhelp since no longer supported by haddock-2.8.0

* Thu Oct 28 2010 Jens Petersen <petersen@redhat.com> - 0.11.2-5
- glade and gtksourceview2 packages are now in fedora
- add explicit dep on mtl

* Thu Sep 30 2010 Jens Petersen <petersen@redhat.com> - 0.11.2-4
- obsolete gtk2hs glade, gtkglext, gtksourceview2, soegtk, vte until packaged

* Mon Sep 13 2010 Jens Petersen <petersen@redhat.com> - 0.11.2-3
- depend on gio too

* Mon Sep 13 2010 Jens Petersen <petersen@redhat.com> - 0.11.2-2
- include demos in devel doc

* Wed Sep  1 2010 Jens Petersen <petersen@redhat.com> - 0.11.2-1
- update to 0.11.2

* Fri Jul 16 2010 Jens Petersen <petersen@redhat.com> - 0.11.0-1
- BR ghc-glib, ghc-pango, ghc-cairo
- ghc-rpm-macros-0.8.1
- support hscolour and devhelp
- build with LANG=en_US.UTF-8 as a workaround for LANG=C issue

* Fri Jul 16 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 0.11.0-0
- initial packaging for Fedora automatically generated by cabal2spec-0.22.1