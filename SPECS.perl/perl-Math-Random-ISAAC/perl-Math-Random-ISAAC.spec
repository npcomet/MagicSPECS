Name:           perl-Math-Random-ISAAC
Version:        1.004
Release:        9%{?dist}
Summary:        Perl interface to the ISAAC PRNG algorithm
License:        MIT or GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Math-Random-ISAAC/
Source0:        http://www.cpan.org/authors/id/J/JA/JAWNSY/Math-Random-ISAAC-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
As with other Pseudo-Random Number Generator (PRNG) algorithms like the
Mersenne Twister (see Math::Random::MT), this algorithm is designed to take
some seed information and produce seemingly random results as output.

%prep
%setup -q -n Math-Random-ISAAC-%{version}
sed -i 's/\r//' examples/*.pl


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%defattr(-,root,root,-)
%doc Changes examples LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.004-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.004-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.004-7
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.004-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.004-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.004-3
- Perl mass rebuild

* Fri Feb 25 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 1.004-2
- Bump the release number.

* Sun Feb 19 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 1.004-1
- Specfile autogenerated by cpanspec 1.78.