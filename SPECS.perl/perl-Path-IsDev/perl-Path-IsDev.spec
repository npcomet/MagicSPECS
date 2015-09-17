Name:           perl-Path-IsDev
Version:        1.001002
Release:        4%{?dist}
Summary:        Determine if a given Path resembles a development source tree
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Path-IsDev/
Source0:        http://www.cpan.org/authors/id/K/KE/KENTNL/Path-IsDev-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.90
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Tiny) >= 1.000
BuildRequires:  perl(Config)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Path::Tiny) >= 0.004
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Role::Tiny::With)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(utf8)
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 1.001002
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp)
Requires:       perl(File::HomeDir)
Requires:       perl(Module::Runtime)
Requires:       perl(Path::Tiny)
Requires:       perl(Scalar::Util)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Class::Tiny\\)\\s*$

%description
This module is more or less a bunch of heuristics for determining if a
given path is a development tree root of some kind.

This has many useful applications, notably ones that require behaviors for
"installed" modules to be different to those that are still "in
development"

%prep
%setup -q -n Path-IsDev-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.001002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.001002-3
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.001002-2
- Perl 5.20 rebuild

* Tue Aug 19 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.001002-1
- 1.001002 bump

* Wed Jul 16 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.001001-1
- 1.001001 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.001000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.001000-1
- 1.001000 bump

* Tue Nov 26 2013 Petr Pisar <ppisar@redhat.com> - 1.000002-1
- 1.000002 bump

* Thu Oct 24 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.000000-1
- 1.000000 bump

* Tue Oct 08 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.0-1
- 0.6.0 bump

* Mon Sep 30 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.0-1
- 0.4.0 bump

* Thu Sep 26 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.3-1
- 0.3.3 bump

* Thu Sep 19 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.2-1
- 0.3.2 bump

* Mon Sep 16 2013 Jitka Plesnikova <jplesnik@redhat.com> 0.3.0-1
- Specfile autogenerated by cpanspec 1.78.
