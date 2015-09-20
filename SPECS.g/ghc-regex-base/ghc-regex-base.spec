# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name regex-base

Name:           ghc-%{pkg_name}
# part of haskell-platform
Version:        0.93.2
Release:        32%{?dist}
Summary:        Haskell regex base library

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-mtl-devel
# End cabal-rpm deps

%description
Interface API for regex-posix,pcre,parsec,tdfa,dfa.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%ghc_lib_build


%install
%ghc_lib_install


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%doc LICENSE


%files devel -f %{name}-devel.files


%changelog
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 Jens Petersen <petersen@fedoraproject.org> - 0.93.2-31
- update hackage urls

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan  2 2014 Jens Petersen <petersen@redhat.com> - 0.93.2-28
- spec file updated to cabal-rpm-0.8.7

* Wed Mar 21 2012 Jens Petersen <petersen@redhat.com> - 0.93.2-11
- rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jan  2 2012 Jens Petersen <petersen@redhat.com> - 0.93.2-9
- update to cabal2spec-0.25.2

* Mon Oct 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.93.2-8.3
- rebuild with new gmp without compat lib

* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.93.2-8.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 0.93.2-8.1
- rebuild with new gmp

* Tue Jun 21 2011 Jens Petersen <petersen@redhat.com> - 0.93.2-8
- ghc_arches replaces ghc_excluded_archs

* Mon Jun 20 2011 Jens Petersen <petersen@redhat.com> - 0.93.2-7
- BR ghc-Cabal-devel and use ghc_excluded_archs

* Fri May 27 2011 Jens Petersen <petersen@redhat.com> - 0.93.2-6
- update to cabal2spec-0.23: add ppc64

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.93.2-5
- Enable build on sparcv9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 15 2011 Jens Petersen <petersen@redhat.com> - 0.93.2-3
- update to cabal2spec-0.22.4

* Thu Nov 25 2010 Jens Petersen <petersen@redhat.com> - 0.93.2-2
- update url and drop -o obsoletes
- add hscolour

* Fri Jul 16 2010 Jens Petersen <petersen@redhat.com> - 0.93.2-1
- update to 0.93.2 for haskell-platform-2010.2.0.0
- obsolete doc subpackage (ghc-rpm-macros-0.8.0)

* Fri Jun 25 2010 Jens Petersen <petersen@redhat.com> - 0.93.1-4
- strip shared library (cabal2spec-0.21.4)

* Tue Apr 27 2010 Jens Petersen <petersen@redhat.com> - 0.93.1-3
- part of haskell-platform-2010.1.0.0
- rebuild against ghc-6.12.2
- condition ghc_lib_package

* Fri Jan 15 2010 Jens Petersen <petersen@redhat.com> - 0.93.1-2
- license is BSD
- depends on mtl

* Fri Jan 15 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 0.93.1-1
- initial packaging for Fedora automatically generated by cabal2spec-0.21.1
