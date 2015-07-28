Name:           perl-DateTime-Locale
Version:        0.45
Release:        13%{?dist}
Summary:        Localization support for DateTime.pm
# package itself is 'same terms as Perl'
# modules under DateTime/Locale/ are generated from data provided by the CLDR project
# tools/t/test-data contains CLDR data files under MIT license
License:        (GPL+ or Artistic) and MIT
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DateTime-Locale/
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/DateTime-Locale-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl >= 0:5.006
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Params::Validate) >= 0.91
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Output)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# perl-DateTime-Locale used to be bundled with perl-DateTime
# ideally, this would be resolved with
# Requires:     perl-DateTime >= 2:0.70-1
# but DateTime::Locale doesn't strictly require DateTime
# and this would introduce circular build dependencies
Conflicts:	perl-DateTime <= 1:0.7000-3.fc16

%{?perl_default_filter}

%description
DateTime::Locale is primarily a factory for the various locale sub-classes.
It also provides some functions for getting information on all the
available locales.

%prep
%setup -q -n DateTime-Locale-%{version}

iconv -f iso-8859-1 -t utf-8 Changes >Changes.iconv \
&& touch -r Changes Changes.iconv \
&& mv -f Changes.iconv Changes

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes LICENSE LICENSE.cldr README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.45-13
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.45-12
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.45-11
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.45-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.45-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.45-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.45-7
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.45-6
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.45-5
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 0.45-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 15 2011 Iain Arnell <iarnell@gmail.com> 0.45-1
- Specfile autogenerated by cpanspec 1.78.