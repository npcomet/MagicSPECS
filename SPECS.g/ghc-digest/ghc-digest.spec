# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name digest

Name:           ghc-%{pkg_name}
Version:        0.0.1.2
Release:        6%{?dist}
Summary:        Cryptographic hashes for bytestrings

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-bytestring-devel
BuildRequires:  zlib-devel%{?_isa}
# End cabal-rpm deps

%description
This package provides efficient cryptographic hash implementations for
strict and lazy bytestrings. For now, CRC32 and Adler32 are supported;
they are implemented as FFI bindings to efficient code from zlib.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Begin cabal-rpm deps:
Requires:       zlib-devel%{?_isa}
# End cabal-rpm deps

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
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 27 2015 Jens Petersen <petersen@fedoraproject.org> - 0.0.1.2-5
- cblrpm refresh

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Jens Petersen <petersen@redhat.com> - 0.0.1.2-1
- update to 0.0.1.2
- update to new simplified Haskell Packaging Guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 17 2012 Jens Petersen <petersen@redhat.com> - 0.0.1.1-4
- update with cabal-rpm
- disable bytestring-in-base flag with patch

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Jens Petersen <petersen@redhat.com> - 0.0.1.1-2
- change prof BRs to devel

* Thu Mar 22 2012 Jens Petersen <petersen@redhat.com> - 0.0.1.1-1
- update to 0.0.1.1
- add license to ghc_files

* Fri Jan  6 2012 Jens Petersen <petersen@redhat.com> - 0.0.1.0-2
- update to cabal2spec-0.25.2

* Mon Oct 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.0.1.0-1.3
- rebuild with new gmp without compat lib

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.0.1.0-1.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 0.0.1.0-1.1
- rebuild with new gmp

* Wed Sep 28 2011 Jens Petersen <petersen@redhat.com> - 0.0.1.0-1
- update to 0.0.1.0
- use _isa for zlib-devel dependency

* Wed Jun 22 2011 Jens Petersen <petersen@redhat.com> - 0.0.0.9-2
- BR ghc-Cabal-devel and use ghc_arches (cabal2spec-0.23.2)

* Sat May 28 2011 Jens Petersen <petersen@redhat.com> - 0.0.0.9-1
- update to 0.0.9
- update to cabal2spec-0.23: add ppc64

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.0.0.8-4
- Enable build on sparcv9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 19 2011 Jens Petersen <petersen@redhat.com> - 0.0.0.8-2
- update to cabal2spec-0.22.4

* Fri Nov 12 2010 Jens Petersen <petersen@redhat.com> - 0.0.0.8-1
- BSD
- BR zlib-devel

* Fri Nov 12 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 0.0.0.8-0
- initial packaging for Fedora automatically generated by cabal2spec-0.22.2
