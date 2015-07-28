Name:           perl-Devel-Declare
Version:        0.006008
Release:        11%{?dist}
Summary:        Adding keywords to perl, in perl
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Devel-Declare/
Source0:        http://search.cpan.org/CPAN/authors/id/Z/ZE/ZEFRAM/Devel-Declare-%{version}.tar.gz
BuildRequires:  perl(B::Compiling)
BuildRequires:  perl(B::Hooks::EndOfScope) >= 0.05
BuildRequires:  perl(B::Hooks::OP::Check) >= 0.19
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warn)
# necessary minimum versions not automatically detected
Requires:       perl(B::Hooks::EndOfScope) >= 0.05
Requires:       perl(B::Hooks::OP::Check) >= 0.19
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Devel::Declare can install subroutines called declarators which locally
take over Perl's parser, allowing the creation of new syntax.

%prep
%setup -q -n Devel-Declare-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%doc Changes
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Devel*
%{_mandir}/man3/*

%changelog
* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.006008-11
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.006008-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.006008-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.006008-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.006008-7
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.006008-6
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.006008-5
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.006008-4
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.006008-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.006008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 06 2011 Iain Arnell <iarnell@gmail.com> 0.006008-1
- update to latest upstream version

* Fri Sep 23 2011 Iain Arnell <iarnell@gmail.com> 0.006007-1
- update to latest upstream version

* Sat Aug 27 2011 Iain Arnell <iarnell@gmail.com> 0.006006-1
- update to latest upstream

* Tue Jul 26 2011 Iain Arnell <iarnell@gmail.com> 0.006005-1
- update to latest upstream

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.006004-2
- Perl mass rebuild

* Tue May 03 2011 Iain Arnell <iarnell@gmail.com> 0.006004-1
- update to latest upstream version

* Wed Apr 20 2011 Iain Arnell <iarnell@gmail.com> 0.006003-1
- update to latest upstream version

* Sat Apr 09 2011 Iain Arnell <iarnell@gmail.com> 0.006002-1
- update to latest upstream version

* Sun Feb 27 2011 Iain Arnell <iarnell@gmail.com> 0.006001-1
- update to latest upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.006000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.006000-3
- 661697 rebuild for fixing problems with vendorach/lib

* Sat Jul 17 2010 Iain Arnell <iarnell@gmail.com> 0.006000-2
- cleanup spec for moderm rpmbuild
- BR perl(B::Compiling)

* Sat Jul 03 2010 Iain Arnell <iarnell@gmail.com> 0.006000-1
- Specfile autogenerated by cpanspec 1.78.