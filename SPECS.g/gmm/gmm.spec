Name:    gmm
Summary: A generic C++ template library for sparse, dense and skyline matrices
Summary(zh_CN.UTF-8): 稀疏矩阵、稠密矩阵、斯凯莱恩矩阵的 C++ 模板库
Version: 4.0.0
Release: 5%{?dist} 
Group:   Development/Libraries
Group(zh_CN.UTF-8): 开发/库

License: LGPLv2+ 
URL:     http://home.gna.org/getfem/gmm_intro
Source:  http://download.gna.org/getfem/stable/gmm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
%{summary}

%description -l zh_CN.UTF-8
稀疏矩阵、稠密矩阵、斯凯莱恩矩阵的 C++ 模板库

%package devel
Summary:A generic C++ template library for sparse, dense and skyline matrices
Summary(zh_CN.UTF-8): %{name} 的开发包
Group:   Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Provides: %{name} = %{version}-%{release}
Provides: gmm++-devel = %{version}-%{release}
%description devel
%{summary}

%description devel -l zh_CN.UTF-8
%{name} 的开发包。

%prep
%setup -q


%build
%configure


%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot} 
magic_rpm_clean.sh

%clean 
rm -rf %{buildroot}


%files devel
%defattr(-,root,root,-)
%{_includedir}/gmm/


%changelog
* Sun Nov 08 2015 Liu Di <liudidi@gmail.com> - 4.0.0-5
- 为 Magic 3.0 重建

* Fri Oct 30 2015 Liu Di <liudidi@gmail.com> - 4.0.0-4
- 为 Magic 3.0 重建

* Thu Dec 06 2012 Liu Di <liudidi@gmail.com> - 4.0.0-3
- 为 Magic 3.0 重建

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Mar 30 2010 Steven M. Parrish <smparrish@gmail.com> - 4.0.0-1
- New upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Steven Parrish <smparrish@shallowcreek.net> 3.1-1
- New upstream release

* Wed May 28 2008 Steven Parrish <smparrish[at]shallowcreek.net> 3.0-3
- corrected license

* Wed May 28 2008 Rex Dieter <rdieter@fedoraproject.org> 3.0-2
- name gmm
- -devel: Provides: gmm++-devel = ...

* Tue May 27 2008 Steven Parrish <smparrish[at]shallowcreek.net> 3.0-1
-  Initial SPEC file

