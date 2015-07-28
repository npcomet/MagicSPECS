Name:           perl-Catalyst-Plugin-SubRequest
Summary:        Make subrequests to actions in Catalyst
Version:        0.17
Release:        17%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/B/BO/BOBTFISH/Catalyst-Plugin-SubRequest-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/Catalyst-Plugin-SubRequest/
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

BuildRequires:  perl(Catalyst::Runtime) >= 5.80003
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request::AsCGI)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Time::HiRes)

Requires:       perl(Catalyst::Runtime) >= 5.80003

# obsolete/provide old tests subpackage
# can be removed during F19 development cycle
Obsoletes:      %{name}-tests < 0.17-3
Provides:       %{name}-tests = %{version}-%{release}

%{?perl_default_filter}

%description
Make subrequests to actions in Catalyst. Uses the Catalyst dispatcher, so
it will work like an external url call.

%prep
%setup -q -n Catalyst-Plugin-SubRequest-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check


%files
%doc Changes README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.17-17
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.17-16
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.17-15
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.17-14
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.17-13
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.17-12
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.17-11
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.17-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.17-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.17-8
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.17-7
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.17-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.17-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.17-4
- 为 Magic 3.0 重建

* Sun Jan 22 2012 Iain Arnell <iarnell@gmail.com> 0.17-3
- drop tests subpackage; move tests to main package documentation

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 02 2011 Iain Arnell <iarnell@gmail.com> 0.17-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.16-5
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.16-3
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.16-2
- Mass rebuild with perl-5.12.0

* Sun Feb 21 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.16-1
- update by Fedora::App::MaintainerTools 0.003
- PERL_INSTALL_ROOT => DESTDIR
- added a new br on perl(Catalyst::Runtime) (version 5.80003)
- dropped old BR on perl(Catalyst)
- dropped old BR on perl(Test::Pod::Coverage)
- added a new req on perl(Catalyst::Runtime) (version 5.80003)
- dropped old requires on perl(Catalyst)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.15-2
- rebuild against perl 5.10.1

* Sun Dec 06 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.15-1
- add default filtering
- auto-update to 0.15 (by cpan-spec-update 0.01)
- added a new br on perl(Catalyst::Runtime) (version 5.7012)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May 21 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.13-1
- update to 0.13

* Wed Mar 05 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.11-4
- rebuild for new perl

* Tue Jun 05 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.11-3
- bump

* Tue May 22 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.11-2
- include missing BR
- add t/ to doc

* Fri Apr 27 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.11-1
- Specfile autogenerated by cpanspec 1.71.