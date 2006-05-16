Summary:	A python library for manipulating kickstart files
Name:		python-kickstart
Version:	0.23
Release:	1
Source0:	pykickstart-%{version}.tar.gz
# Source0-md5:	aa52b2e3ad0bb422095f14029d527503
License:	GPL
Group:		Libraries
BuildRequires:	python-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The pykickstart package is a python library for manipulating kickstart
files.

%prep
%setup -q -n pykickstart-%{version}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog COPYING docs/programmers-guide
%{py_sitescriptdir}/pykickstart
%attr(755,root,root) %{_bindir}/ksvalidator
