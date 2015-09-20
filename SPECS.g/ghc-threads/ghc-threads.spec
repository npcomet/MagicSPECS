# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name threads

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        0.5.1.3
Release:        2%{?dist}
Summary:        Fork threads and wait for their result

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-stm-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-concurrent-extra-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
%endif
# End cabal-rpm deps

%description
This package provides functions to fork threads and wait for their result,
whether it's an exception or a normal value.

Besides waiting for the termination of a single thread this packages also
provides functions to wait for a group of threads to terminate.

This package is similar to the 'threadmanager', 'async' and 'spawn' packages.
The advantages of this package are:

* Simpler API.

* More efficient in both space and time.

* No space-leak when forking a large number of threads.

* Correct handling of asynchronous exceptions.

* GHC specific functionality like 'forkOn' and 'forkIOWithUnmask'.


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


%check
%if %{with tests}
%cabal test
%endif


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%doc LICENSE


%files devel -f %{name}-devel.files
%doc README.markdown


%changelog
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 22 2015 Jens Petersen <petersen@redhat.com> - 0.5.1.3-1
- update to 0.5.1.3

* Wed Oct 1 2014 Ricky Elrod <relrod@redhat.com> - 0.5.1.2-1
- Latest upstream release.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jan 19 2014 Ricky Elrod <codeblock@fedoraproject.org> - 0.5.1.1-1
- Latest upstream release.

* Mon Nov 18 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.5.0.3-1
- Latest upstream release.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul  8 2013 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.5.0.2-1
- spec file generated by cabal-rpm-0.8.2
