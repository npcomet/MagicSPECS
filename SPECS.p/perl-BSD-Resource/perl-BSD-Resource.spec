Name:           perl-BSD-Resource
Version:	1.29.07
%define module_version %(echo %{version} | awk -F. '{print $1"."$2$3}')
Release:	1%{?dist}
Summary:        BSD process resource limit and priority functions

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/BSD-Resource/
Source0:        http://www.cpan.org/authors/id/J/JH/JHI/BSD-Resource-%{module_version}.tar.gz

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
A module providing an interface for testing and setting process limits
and priorities.

%prep
%setup -q -n BSD-Resource-%{module_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*
magic_rpm_clean.sh

%check


%files
%doc ChangeLog README
%{perl_vendorarch}/BSD/
%{perl_vendorarch}/auto/BSD/
%{_mandir}/man3/*.3*


%changelog
* Wed Apr 29 2015 Liu Di <liudidi@gmail.com> - 1.29.07-1
- 更新到 1.29.07

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.29.04-16
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 1.29.04-15
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.29.04-14
- 为 Magic 3.0 重建

* Wed Sep 19 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.29.04-13
- Add perl_default_filter to filter Resource.so from provides. 

* Thu Aug  2 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.29.04-12
- Update BR, Provides
- Clean up for modern rpmbuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29.04-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 1.29.04-10
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29.04-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jan 10 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1.29.04-8
- add filter for unneeded provides

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.29.04-6
- Perl mass rebuild & add provide

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.29.04-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Jun  8 2010 Petr Pisar <ppisar@redhat.com> - 1.29.04-1
- 1.2904 bump (bug #600626)

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.29.03-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.29.03-3
- rebuild against perl 5.10.1

* Thu Oct 29 2009 Stepan Kasal <skasal@redhat.com> - 1.29.03-2
- bump release

* Mon Jul 27 2009 Marcela Mašláňová <mmaslano@redhat.com> - 1.29.03-1
- update, remove unneeded patch

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep 21 2008 Ville Skyttä <ville.skytta at iki.fi> - 1.28-7
- Fix Patch0:/%%patch mismatch.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.28-6
- Rebuild for perl 5.10 (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.28-5
- Autorebuild for GCC 4.3

* Sat Feb  2 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.28-4
- rebuild for new perl

* Thu Aug 23 2007 Robin Norwood <rnorwood@redhat.com> 1.28-3
- Fix license tag.
- Add %%doc section

* Sat Jun 30 2007 Steven Pritchard <steve@kspei.com> 1.28-2
- Fix find option order.
- Use fixperms macro instead of our own chmod incantation.
- Remove check macro cruft.
- Remove redundant BR perl.
- BR ExtUtils::MakeMaker, Test::More, Test::Pod, and Test::Pod::Coverage.
- Patch t/setrlimit.t to fix bogus test failure.
- Set OPTIMIZE when running Makefile.PL, not make.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.28-1.fc6.1
- rebuild

* Mon Jun 05 2006 Jason Vas Dias <jvdias@redhat.com> - 1.28-1
- upgrade to upstream version 1.28

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.24-3.2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.24-3.2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 1.24-3.2
- rebuild for new perl-5.8.8

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Sat Apr  2 2005 Warren Togami <wtogami@redhat.com> - 1.24-3
- skip  #153178

* Sat Apr  2 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.24-2
- spec cleanup
- License corrected

* Thu Mar 31 2005 Warren Togami <wtogami@redhat.com> 1.24-1
- 1.24

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Chip Turner <cturner@redhat.com> 1.23-1
- update to 1.23

* Thu Jun 05 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Nov 20 2002 Chip Turner <cturner@redhat.com>
- rebuild

* Tue Aug  6 2002 Chip Turner <cturner@redhat.com>
- automated release bump and build

* Tue Jun  4 2002 Chip Turner <cturner@redhat.com>
- properly claim directories owned by package so they are removed when package is removed

* Wed Jan 30 2002 cturner@redhat.com
- Specfile autogenerated

