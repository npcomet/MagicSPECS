Name:           perl-HTML-Entities-Numbered
Version:        0.04
Release:        11%{?dist}
Summary:        Conversion of numbered HTML entities
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTML-Entities-Numbered/
Source0:        http://www.cpan.org/modules/by-module/HTML/HTML-Entities-Numbered-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.32
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
HTML::Entities::Numbered is a content conversion filter for named HTML
entities (symbols, mathmetical symbols, Greek letters, Latin letters,
etc.). When an argument of name2decimal() or name2hex() contains some
nameable HTML entities, they will be replaced to numbered HTML entities.
And when an argument of name2decimal_xml() or name2hex_xml() contains
some nameable numbered HTML entities, they will be replaced to numbered
HTML entities except valid XML entities (the excepted "valid XML
entities" are the following five entities: &lt;, &gt;, &amp;, &quot;,
&apos;). By the same token, when an argument of decimal2name() or
hex2name() contains some nameable numbered HTML entities, they will be
replaced to named HTML entities.

%prep
%setup -q -n HTML-Entities-Numbered-%{version}

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


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.04-11
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.04-10
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 0.04-8
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.04-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.04-4
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.04-3
- Mass rebuild with perl-5.12.0

* Mon Feb 08 2010 Xavier Bachelot <xavier@bachelot.org> 0.04-2
- Remove unwanted Requires: perl(Test::More).

* Wed Feb 03 2010 Xavier Bachelot <xavier@bachelot.org> 0.04-1
- Specfile autogenerated by cpanspec 1.78.
- Fix License: