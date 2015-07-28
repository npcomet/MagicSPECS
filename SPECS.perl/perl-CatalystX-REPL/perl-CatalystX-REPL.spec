Name:           perl-CatalystX-REPL
Version:        0.04
Release:        16%{?dist}
Summary:        Read-eval-print-loop for debugging your Catalyst application
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CatalystX-REPL/
Source0:        http://www.cpan.org/authors/id/F/FL/FLORA/CatalystX-REPL-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Carp::REPL)
BuildRequires:  perl(Catalyst) >= 5.80006
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Expect)
BuildRequires:  perl(namespace::autoclean)
Requires:       perl(Catalyst) >= 5.80006
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# Test::Expect and/or Devel::REPL is failing under mock 1.1.8 in koji
# all is fine locally with mock 1.1.14, though
%bcond_with expect_tests

%{?perl_default_filter}

%description
Using Carp::REPL with a Catalyst application is hard. That's because of all
the internal exceptions that are being thrown and caught by Catalyst during
application startup. You'd have to manually skip over all of those.

This role works around that by automatically setting up Carp::REPL after
starting your application, if the CATALYST_REPL or MYAPP_REPL environment
variables are set.

%prep
%setup -q -n CatalystX-REPL-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
# Test::Expect and/or Devel::REPL is failing under mock 1.1.8 in koji
# all is fine locally with mock 1.1.14, though
%if ! %{with expect_tests}
grep -lZ 'Test::Expect' t/*.t |xargs -0 rm -f
%endif


%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.04-16
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.04-15
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.04-14
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.04-13
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.04-12
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.04-11
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.04-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.04-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.04-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.04-7
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.04-6
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.04-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.04-4
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 13 2011 Iain Arnell <iarnell@gmail.com> 0.04-2
- Test::Expect and/or Devel::REPL fail under mock 1.1.8 in koji
  use --with expect-tests to enable locally

* Fri Sep 30 2011 Iain Arnell <iarnell@gmail.com> 0.04-1
- Specfile autogenerated by cpanspec 1.78.