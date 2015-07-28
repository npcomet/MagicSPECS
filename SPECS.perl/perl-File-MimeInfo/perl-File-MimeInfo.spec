Name:           perl-File-MimeInfo
Version:        0.16
Release:        10%{?dist}
Summary:        Determine file type and open application
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/File-MimeInfo/
Source0:        http://www.cpan.org/authors/id/P/PA/PARDUS/File-MimeInfo/File-MimeInfo-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Module::Build) perl(Test::More) perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(File::BaseDir) perl(File::DesktopEntry)
# needed for some tests otherwise there are warnings
BuildRequires:  shared-mime-info 
# there is also a mimeinfo.cache file created by desktop-file-utils
# needed. It won't be there if building in a chroot, even if 
# desktop-file-utils is installed if desktop-file-utils was never run.
Requires:       shared-mime-info
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module can be used to determine the mime type of a file. It tries to
implement the freedesktop specification for a shared MIME database.

%prep
%setup -q -n File-MimeInfo-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%doc Changes README
%{_bindir}/mimeopen
%{_bindir}/mimetype
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.16-10
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.16-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.16-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.16-7
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.16-6
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.16-5
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.16-4
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.16-3
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.16-2
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Marcela Mašláňová <mmaslano@redhat.com> - 0.16-1
- bump to 0.16
- remove patch, which is included in new release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.15-9
- Perl mass rebuild & apply test fix from cpan RT#66841 & clean spec

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.15-7
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.15-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.15-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.15-2
- rebuild for new perl

* Thu Feb 14 2008 Patrice Dumas <pertusus@free.fr> 0.15-1
- update to 0.15, remove upstreamed no-ask patch

* Wed Aug  8 2007 Patrice Dumas <pertusus@free.fr> 0.14-1
- update to 0.14

* Thu Nov 16 2006 Patrice Dumas <pertusus@free.fr> 0.13-3
- add a Requires on shared-mime-info (Bug #215972)

* Wed Oct 11 2006 Patrice Dumas <pertusus@free.fr> 0.13-2
- add an option to launch mimeopen non interactively

* Wed Oct 11 2006 Patrice Dumas <pertusus@free.fr> 0.13-1
- Specfile autogenerated by cpanspec 1.69.