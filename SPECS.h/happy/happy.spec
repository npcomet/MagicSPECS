# https://fedoraproject.org/wiki/Packaging:Haskell

%bcond_without tests
%bcond_without static

Name:           happy
# part of haskell-platform
Version:        1.19.5
Release:        3%{?dist}
Summary:        Parser Generator for Haskell

License:        BSD
Url:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-mtl-devel
%if %{with tests}
BuildRequires:  ghc-process-devel
%endif
# End cabal-rpm deps
BuildRequires:  autoconf
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  libxml2
BuildRequires:  libxslt
%if %{with static}
Requires:       %{name}-common = %{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
%endif

%description
Happy is a LALR(1) parser generator system for Haskell, similar to the tool
`yacc' for C. Like `yacc', it takes a file containing an annotated BNF
specification of a grammar and produces a Haskell module containing a
parser for the grammar.

Happy is flexible: you can have several Happy parsers in the same
program, and several entry points to a single grammar. Happy can work
in conjunction with a lexical analyser supplied by the user (either
hand-written or generated by another program).


%if %{with static}
%package common
Summary:        Common files for %{name}

%description common
This provides the common files for %{name}.


%package static
Summary:        Static Haskell build
Requires:       %{name}-common = %{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description static
This provides a build with Haskell libraries statically linked.
%endif


%prep
%setup -q


%build
%if %{with static}
%define ghc_without_dynamic 1
%ghc_bin_build
mv dist/build/%{name}/%{name}{,.static}
%undefine ghc_without_dynamic
%endif
%ghc_bin_build

cd doc
autoreconf
%configure
make html
cd ..


%install
%ghc_bin_install
%if %{with static}
mv %{buildroot}%{_bindir}/%{name}{,.dynamic}
install dist/build/%{name}/%{name}.static %{buildroot}%{_bindir}
touch %{buildroot}%{_bindir}/%{name}
rm %{buildroot}%{_pkgdocdir}/LICENSE
%endif


%check
%if %{with tests}
%cabal test
%endif


%if %{with static}
# avoid rpm ghost keeping pre-alternatives binary around
%pre
if [ $1 -gt 1 ] ; then
  if [ -f %{_bindir}/%{name} -a ! -L %{_bindir}/%{name} ]; then
      rm %{_bindir}/%{name}
  fi
fi


%post
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}.dynamic 70


%postun
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.dynamic
fi


# avoid rpm ghost keeping pre-alternatives binary around
%pre static
if [ $1 -gt 1 ] ; then
  if [ -f %{_bindir}/%{name} -a ! -L %{_bindir}/%{name} ]; then
      rm %{_bindir}/%{name}
  fi
fi


%post static
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}.static 30


%postun static
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.static
fi
%endif


%files
%if %{with static}
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.dynamic
%else
%doc ANNOUNCE CHANGES LICENSE README TODO doc/happy
%{_bindir}/%{name}
%{_datadir}/%{name}-%{version}
%endif


%if %{with static}
%files common
%doc ANNOUNCE CHANGES LICENSE README TODO doc/happy
%{_datadir}/%{name}-%{version}


%files static
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.static
%endif


%changelog
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Jens Petersen <petersen@redhat.com> - 1.19.5-2
- add static and common subpackages
- dynamic and static are handled as alternatives

* Fri Apr 03 2015 Jens Petersen <petersen@redhat.com> - 1.19.5-1
- update to 1.19.5

* Thu Aug  7 2014 Jens Petersen <petersen@redhat.com> - 1.19.4-1
- update to 1.19.4

* Tue Jul  8 2014 Jens Petersen <petersen@redhat.com> - 1.18.10-35
- update to cblrpm-0.8.11

* Fri Apr 11 2014 Jens Petersen <petersen@redhat.com> - 1.18.10-34
- split out of haskell-platform
- update to 1.18.10

* Tue Mar 20 2012 Jens Petersen <petersen@redhat.com> - 1.18.9-1
- update to 1.18.9

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.6-8.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.18.6-7.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 1.18.6-7.1
- rebuild with new gmp

* Tue Jun 21 2011 Jens Petersen <petersen@redhat.com> - 1.18.6-7
- ghc_arches replaces ghc_excluded_archs

* Mon Jun 20 2011 Jens Petersen <petersen@redhat.com> - 1.18.6-6
- BR ghc-Cabal-devel and use ghc_excluded_archs

* Wed May 25 2011 Jens Petersen <petersen@redhat.com> - 1.18.6-5
- add ppc64

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.18.6-4
- Enable build on sparcv9

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 15 2011 Jens Petersen <petersen@redhat.com> - 1.18.6-2
- update to cabal2spec-0.22.4
- BR ghc-devel

* Sun Dec  5 2010 Jens Petersen <petersen@redhat.com> - 1.18.6-1
- update to 1.18.6

* Thu Nov 25 2010 Jens Petersen <petersen@redhat.com> - 1.18.5-2
- rebuild

* Fri Jul 16 2010 Jens Petersen <petersen@redhat.com> - 1.18.5-1
- update to 1.18.5 for haskell-platform-2010.2.0.0
- use new build macros from ghc-rpm-macros-0.7.0

* Sat Jun 26 2010 Jens Petersen <petersen@redhat.com> - 1.18.4-8
- link dynamically again
- strip program (cabal2spec-0.21.4)

* Wed Jun 23 2010 Jens Petersen <petersen@redhat.com> - 1.18.4-7
- don't link dynamically since happy is needed to build ghc

* Tue Apr 27 2010 Jens Petersen <petersen@redhat.com> - 1.18.4-6
- rebuild against ghc-6.12.2

* Mon Jan 11 2010 Jens Petersen <petersen@redhat.com> - 1.18.4-5
- rebuild with ghc-6.12.1
- link dynamically
- buildrequires ghc-mtl-devel
- drop redundant buildroot and its install cleaning

* Thu Oct  1 2009 Jens Petersen <petersen@redhat.com> - 1.18.4-4
- selinux fcontext no longer needed in post script

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 17 2009 Jens Petersen <petersen@redhat.com> - 1.18.4-2
- buildrequires ghc-rpm-macros

* Sat Apr 25 2009 Jens Petersen <petersen@redhat.com> - 1.18.4-1
- 1.18.4 release

* Wed Feb 25 2009 Jens Petersen <petersen@redhat.com> - 1.18.2-3
- rebuild with %%ix86 for i586

* Mon Feb 23 2009 Jens Petersen <petersen@redhat.com> - 1.18.2-2
- cabal build replaces cabal_build

* Wed Nov 12 2008 Jens Petersen <petersen@redhat.com> - 1.18.2-1
- update to 1.18.2 release from hackage
- update to new packaging macros
- turn off debuginfo

* Tue Oct 14 2008 Jens Petersen <petersen@redhat.com> - 1.17-3
- add selinux unconfined_execmem_exec_t file context

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.17-2
- Autorebuild for GCC 4.3

* Fri Jan  4 2008 Jens Petersen <petersen@redhat.com> - 1.17-1
- update to 1.17 release

* Fri Nov 23 2007 Bryan O'Sullivan <bos@serpentine.com> - 1.16-3
- Exclude alpha and ppc64

* Thu Aug 16 2007 Jens Petersen <petersen@redhat.com>
- update License field

* Sun Mar 25 2007 Bryan O'Sullivan <bos@serpentine.com> - 1.16-2
- fix a few style issues pointed out by Jens

* Fri Jan 19 2007 Bryan O'Sullivan <bos@serpentine.com> - 1.16-1
- update to 1.16
- fix rpmlint warnings

* Fri Jan 21 2005 Jens Petersen <petersen@haskell.org> - 1.15-2
- initial packaging based on spec file from tarball
- setup libdir for x86_64
