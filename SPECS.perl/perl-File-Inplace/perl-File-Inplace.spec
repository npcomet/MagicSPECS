Name:           perl-File-Inplace
Version:        0.20
Release:        8%{?dist}
Summary:        Perl module for in-place editing of files
License:        (GPL+ or Artistic)
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/File-Inplace/
Source0:        http://www.cpan.org/modules/by-module/File/File-Inplace-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
File::Inplace is a perl module intended to ease the common task of editing
a file in-place. Inspired by variations of perl's -i option, this module is
intended for somewhat more structured and reusable editing than command
line perl typically allows. File::Inplace endeavors to guarantee file
integrity; that is, either all of the changes made will be saved to the
file, or none will. It also offers functionality such as backup creation,
automatic field splitting per-line, automatic chomping/unchomping, and
aborting edits partially through without affecting the original file.

%prep
%setup -q -n File-Inplace-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.20-8
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.20-7
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.20-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.20-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.20-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Rüdiger Landmann <r.landmann@redhat.com> 0.20-1
- Specfile autogenerated by cpanspec 1.78.