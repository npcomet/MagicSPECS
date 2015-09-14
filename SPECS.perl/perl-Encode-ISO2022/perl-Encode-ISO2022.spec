Name:           perl-Encode-ISO2022
Version:        0.04
Release:        1%{?dist}
Summary:        ISO/IEC 2022 character encoding scheme
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Encode-ISO2022/
Source0:        http://www.cpan.org/authors/id/N/NE/NEZUMI/Encode-ISO2022-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl(Config)
# 2.10 from Encode requirement in META.json
BuildRequires:  perl-Encode-devel >= 2.10
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode::CN)
BuildRequires:  perl(Encode::Encoding)
BuildRequires:  perl(Encode::JP)
BuildRequires:  perl(Encode::KR)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This module provides a character encoding scheme (CES) switching a set of
multiple coded character sets (CCS).

%prep
%setup -q -n Encode-ISO2022-%{version}

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
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Encode
%{_mandir}/man3/*

%changelog
* Fri Jun 26 2015 Petr Pisar <ppisar@redhat.com> 0.04-1
- Specfile autogenerated by cpanspec 1.78.
