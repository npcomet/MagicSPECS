# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name equivalence

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        0.2.5
Release:        3%{?dist}
Summary:        Maintaining an equivalence relation implemented as union-find using STT

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-STMonadTrans-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-mtl-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-quickcheck2-devel
%endif
# End cabal-rpm deps

%description
This is an implementation of Tarjan's Union-Find algorithm (Robert E.
Tarjan. "Efficiency of a Good But Not Linear Set Union Algorithm", JACM 22(2),
1975) in order to maintain an equivalence relation. This implementation is a
port of the /union-find/ package using the ST monad transformer (instead of the
IO monad).


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
%{_docdir}/%{name}-%{version}/LICENSE


%files devel -f %{name}-devel.files


%changelog
* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 0.2.5-3
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb  9 2015 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.2.5-1
- spec file generated by cabal-rpm-0.9.3
