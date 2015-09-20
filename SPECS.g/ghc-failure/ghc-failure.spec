# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name failure

Name:           ghc-%{pkg_name}
Version:        0.2.0.3
Release:        2%{?dist}
Summary:        A simple type class for success/failure computations

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-transformers-devel
# End cabal-rpm deps

%description
This library is deprecated upstream by the exceptions package.


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


# no license file included!
%files -f %{name}.files


%files devel -f %{name}-devel.files


%changelog
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Jens Petersen <petersen@redhat.com> - 0.2.0.3-1
- update to 0.2.0.3

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Jens Petersen <petersen@redhat.com> - 0.2.0.1-3
- update to new simplified Haskell Packaging Guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 07 2012 Jens Petersen <petersen@redhat.com> - 0.2.0.1-1
- update to 0.2.0.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 18 2012 Jens Petersen <petersen@redhat.com> - 0.1.0.1-10
- update to cabal2spec-0.25

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0.1-9.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.1.0.1-8.3
- rebuild with new gmp without compat lib

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.1.0.1-8.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 0.1.0.1-8.1
- rebuild with new gmp

* Sat Jul 09 2011 Ben Boeckel <mathstuf@gmail.com> - 0.1.0.1-8
- Update to cabal2spec-0.24

* Tue Jun 21 2011 Jens Petersen <petersen@redhat.com> - 0.1.0.1-7
- ghc_arches replaces ghc_excluded_archs

* Mon Jun 20 2011 Jens Petersen <petersen@redhat.com> - 0.1.0.1-6
- BR ghc-Cabal-devel and use ghc_excluded_archs

* Wed May 11 2011 Ben Boeckel <mathstuf@gmail.com> - 0.1.0.1-5
- Update to cabal2spec-0.22.7

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.1.0.1-4
- Enable build on sparcv9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 15 2011 Ben Boeckel <mathstuf@gmail.com> - 0.1.0.1-2
- Update to cabal2spec-0.22.4
- Rebuild

* Tue Nov 23 2010 Ben Boeckel <mathstuf@gmail.com> - 0.1.0.1-1
- Update to 0.1.0.1

* Sat Sep 04 2010 Ben Boeckel <mathstuf@gmail.com> - 0.1.0-1
- Initial package

* Sat Sep  4 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 0.1.0-0
.- initial packaging for Fedora automatically generated by cabal2spec-0.22.2
