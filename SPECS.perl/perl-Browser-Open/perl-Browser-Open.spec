Name:           perl-Browser-Open
Version:	0.04
Release:	1%{?dist}
Summary:        Open a browser in a given URL
Summary(zh_CN.UTF-8): 在浏览器中打开给定的网址
License:        GPL+ or Artistic
Group:          Development/Libraries
Group(zh_CN.UTF-8): 开发/库
URL:            http://search.cpan.org/dist/Browser-Open/
Source0:        http://www.cpan.org/authors/id/C/CF/CFRANKS/Browser-Open-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::More) >= 0.92
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
The functions optionally exported by this module allows you to open URLs in
the user browser.

%description -l zh_CN.UTF-8
在浏览器中打开给定的网址。

%prep
%setup -q -n Browser-Open-%{version}

# https://rt.cpan.org/Public/Bug/Display.html?id=66166
find -type f -name '*.tmp' -exec rm -f {} \;

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*
magic_rpm_clean.sh

%check
RELEASE_TESTING=1 

%files
%defattr(-,root,root,-)
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Apr 29 2015 Liu Di <liudidi@gmail.com> - 0.04-1
- 更新到 0.04

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.03-8
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.03-7
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.03-6
- 为 Magic 3.0 重建

* Sat Jan 28 2012 Liu Di <liudidi@gmail.com> - 0.03-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.03-3
- Perl mass rebuild

* Thu Apr 07 2011 Iain Arnell <iarnell@gmail.com> 0.03-2
- update build requires

* Sat Feb 26 2011 Iain Arnell <iarnell@gmail.com> 0.03-1
- Specfile autogenerated by cpanspec 1.79.