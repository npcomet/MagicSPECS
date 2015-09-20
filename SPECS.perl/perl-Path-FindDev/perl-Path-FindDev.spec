Name:           perl-Path-FindDev
Version:        0.5.2
Release:        5%{?dist}
Summary:        Find a development path somewhere in an upper hierarchy
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Path-FindDev/
Source0:        http://www.cpan.org/authors/id/K/KE/KENTNL/Path-FindDev-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Tiny) >= 0.010
BuildRequires:  perl(Path::IsDev) >= 0.2.2
BuildRequires:  perl(Path::IsDev::Object)
BuildRequires:  perl(Path::Tiny) >= 0.054
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(utf8)
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More) >= 1.001002
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp)
Requires:       perl(File::Spec)
Requires:       perl(Path::IsDev) >= 0.2.2
Requires:       perl(Path::IsDev::Object)
Requires:       perl(Path::Tiny)
Requires:       perl(Scalar::Util)

%description
This package is mostly a glue layer around Path::IsDev with a few directory
walking tricks.

%prep
%setup -q -n Path-FindDev-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Sep 17 2015 Liu Di <liudidi@gmail.com> - 0.5.2-5
- 为 Magic 3.0 重建

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.5.2-3
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.5.2-2
- Perl 5.20 rebuild

* Tue Aug 19 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.5.2-1
- 0.5.2 bump

* Wed Jul 16 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.5.1-1
- 0.5.1 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 05 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.5.0-1
- 0.5.0 bump

* Mon Nov 25 2013 Petr Pisar <ppisar@redhat.com> - 0.4.2-1
- 0.4.2 bump

* Thu Oct 24 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.1-1
- 0.4.1 bump

* Wed Oct 02 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.0-1
- 0.4.0 bump

* Thu Sep 26 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.2-1
- 0.3.2 bump

* Fri Sep 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.1-1
- 0.3.1 bump

* Mon Sep 16 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.0-1
- Specfile autogenerated by cpanspec 1.78.