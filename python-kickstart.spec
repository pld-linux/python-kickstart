Summary:	A Python library for manipulating kickstart files
Summary(pl.UTF-8):	Pythonowa biblioteka do obróbki plików kickstart
Name:		python-kickstart
Version:	1.42
Release:	1
License:	GPL
Group:		Libraries/Python
# https://fedorahosted.org/releases/p/y/pykickstart/ (not yet)
Source0:	pykickstart-%{version}.tar.gz
# Source0-md5:	3761b1e456c1dba745af1e44681829b7
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
%doc README ChangeLog docs/programmers-guide
%attr(755,root,root) %{_bindir}/ksflatten
%attr(755,root,root) %{_bindir}/ksvalidator
%{py_sitescriptdir}/pykickstart
