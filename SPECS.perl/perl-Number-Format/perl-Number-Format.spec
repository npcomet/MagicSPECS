Name:           perl-Number-Format
Version:	1.75
Release:	2%{?dist}
Summary:        Perl extension for formatting numbers
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Number-Format/
Source0:        http://search.cpan.org/CPAN/authors/id/W/WR/WRW/Number-Format-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module provides an easy means of formatting numbers in a manner
suitable for displaying to the user.

%prep
%setup -q -n Number-Format-%{version}

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
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGES README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 1.75-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.75-1
- 更新到 1.75

* Thu Jun 19 2014 Liu Di <liudidi@gmail.com> - 1.73-14
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.73-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.73-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.73-11
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.73-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.73-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.73-8
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.73-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.73-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.73-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.73-4
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.73-3
- Mass rebuild with perl-5.12.0

* Mon Jan 11 2010 Iain Arnell <iarnell@gmail.com> 1.73-2
- fix source0 location (was BADURL)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.73-2
- rebuild against perl 5.10.1

* Mon Oct 05 2009 Iain Arnell <iarnell@gmail.com> 1.73-1
- update to latest upstream

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.72a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 14 2009 Iain Arnell <iarnell@gmail.com> 1.72a-1
- update to latest upstream version

* Fri Apr 10 2009 Iain Arnell 1.70-1
- Specfile autogenerated by cpanspec 1.77.
