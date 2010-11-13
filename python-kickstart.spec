Summary:	A Python library for manipulating kickstart files
Summary(pl.UTF-8):	Pythonowa biblioteka do obróbki plików kickstart
Name:		python-kickstart
Version:	1.50
Release:	3
License:	GPL
Group:		Libraries/Python
# https://fedorahosted.org/releases/p/y/pykickstart/ (not yet)
Source0:	pykickstart-%{version}.tar.gz
# Source0-md5:	a323c2d1242e7dd1ef4e0bb46f0eacb7
URL:		http://fedoraproject.org/wiki/Pykickstart
BuildRequires:	gettext-devel
BuildRequires:	python-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The pykickstart package is a Python library for manipulating kickstart
files.

%description -l pl.UTF-8
Pakiet pykickstart to pythonowa biblioteka do obróbki plików
kickstart.

%prep
%setup -q -n pykickstart-%{version}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/programmers-guide
%attr(755,root,root) %{_bindir}/ksflatten
%attr(755,root,root) %{_bindir}/ksvalidator
%attr(755,root,root) %{_bindir}/ksverdiff
%{py_sitescriptdir}/pykickstart-%{version}-py*.egg-info
%{py_sitescriptdir}/pykickstart
