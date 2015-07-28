Name:           perl-Perl-Critic-Compatibility
Version:        1.001
Release:        12%{?dist}
Summary:        Perl::Critic policies for compatibility with Perl versions
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Perl-Critic-Compatibility/
Source0:        http://www.cpan.org/authors/id/E/EL/ELLIOTJS/Perl-Critic-Compatibility-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Module::Build)
# Perl::Critic 1.083_001 rounded to 3 decimal digits
BuildRequires:  perl(Perl::Critic) >= 1.084
BuildRequires:  perl(Readonly)
BuildRequires:  perl(version)
# Tests only:
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# Perl::Critic 1.083_001 rounded to 3 decimal digits
Requires:       perl(Perl::Critic) >= 1.084

%description
Some Perl::Critic policies that will help you keep your code compatible with
other versions of Perl, regardless of the version that you're developing with.
This includes both backward and forward compatibility.

%prep
%setup -q -n Perl-Critic-Compatibility-%{version}

%build
%{__perl} Build.PL installdirs=core
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_privlib}/*
%{_mandir}/man3/*

%changelog
* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 1.001-12
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.001-11
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.001-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.001-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.001-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.001-7
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.001-6
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 1.001-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.001-2
- Perl mass rebuild

* Wed Jan 26 2011 Petr Pisar <ppisar@redhat.com> 1.001-1
- Specfile autogenerated by cpanspec 1.78.
- Summary shortened
- Description text taken from POD Synopsis
- Remove BuildRoot stuff
- Install into perl core directory