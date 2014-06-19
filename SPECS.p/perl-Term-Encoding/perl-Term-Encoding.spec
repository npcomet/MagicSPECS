Name:           perl-Term-Encoding
Version:        0.02
Release:        2%{?dist}
Summary:        Detect encoding of the current terminal
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Term-Encoding/
Source0:        http://www.cpan.org/authors/id/M/MI/MIYAGAWA/Term-Encoding-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(inc::Module::Install)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Win32::Console not used
# Optional run-time:
BuildRequires:  perl(I18N::Langinfo)
# Tests:
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(warnings)

%description
Term::Encoding is a simple Perl module to detect an encoding the current
terminal expects, in various ways.

%prep
%setup -q -n Term-Encoding-%{version}
# Remove bundled modules
rm -r ./inc/*
sed -i -e '/^inc\//d' MANIFEST

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
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 05 2014 Petr Pisar <ppisar@redhat.com> 0.02-1
- Specfile autogenerated by cpanspec 1.78.
