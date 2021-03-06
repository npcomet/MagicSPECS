Name:           perl-Gnome2-GConf
Version:        1.044
Release:        24%{?dist}
Summary:        Perl wrappers for the GConf configuration engine
License:        LGPLv2+
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Gnome2-GConf/
Source0:        http://www.cpan.org/modules/by-module/Gnome2/Gnome2-GConf-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

## core
BuildRequires:  perl(Test::More)
## non-core
BuildRequires:  perl(Glib) >= 1.120, perl(Glib::MakeHelper), GConf2
BuildRequires:  perl(ExtUtils::Depends) >= 0.2
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.03

BuildRequires:  GConf2-devel

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))


%description
This module allows you to use the GConf configuration system in order to
store/retrieve the configuration of an application. The GConf system is a
powerful configuration manager based on a user daemon that handles a set of
key and value pairs, and notifies any changes of the value to every program
that monitors those keys. GConf is used by GNOME 2.x.


%prep
%setup -q -n Gnome2-GConf-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

cp xs/* .

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*


%check
%{?_with_network_tests:  }


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHOR ChangeLog doctypes gconf.typemap maps NEWS README examples/ t/
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Gnome2*
%{_mandir}/man3/*


%changelog
* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 1.044-24
- 为 Magic 3.0 重建

* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 1.044-23
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.044-22
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.044-21
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.044-20
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.044-19
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.044-18
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.044-17
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.044-16
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.044-15
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.044-14
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.044-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.044-12
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.044-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.044-10
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.044-9
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.044-8
- rebuild against perl 5.10.1

* Thu Jul 30 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.044-7
- Fix mass rebuild breakdown: Add BR: perl(Glib::MakeHelper).

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.044-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.044-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jul 13 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.044-4
- skip network tests when building in the buildsys

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.044-3
Rebuild for new perl

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.044-2
- Autorebuild for GCC 4.3

* Tue Oct 23 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.044-1
- update to 1.044
- add t/ to doc

* Tue Aug 21 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.043-2
- bump

* Sun Oct 15 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.043-1
- update to 1.043

* Mon Sep 04 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.040-1
- update to 1.040

* Thu Aug 31 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.032-4
- bump for mass rebuild

* Tue Aug 22 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.032-3
- bump for build & release

* Fri Aug 18 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.032-2
- added missing BR
- tweaked %build to help -debuginfo generation

* Sun Aug 13 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.032-1
- Specfile autogenerated by cpanspec 1.68.
- Initial spec file for F-E
