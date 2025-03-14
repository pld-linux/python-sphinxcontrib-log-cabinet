#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx extension to organize changelogs
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do porządkowania changelogów
Name:		python-sphinxcontrib-log-cabinet
Version:	1.0.1
Release:	8
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-log-cabinet/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-log-cabinet/sphinxcontrib-log-cabinet-%{version}.tar.gz
# Source0-md5:	50e9b6e692689c605862a3f9b5c6c936
URL:		https://pypi.org/project/sphinxcontrib-log-cabinet/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sphinx extension to organize changelogs generated by versionadded,
versionchanged, deprecated directives. The log will be sorted by
newest to oldest version. For HTML docs, older versions will be
collapsed by default.

%description -l pl.UTF-8
Rozszerzenie Sphinksa do porządkowania changelogów wygenerowanych
przez dyrektywy versionadded, versionchanged i deprecated. Log jest
sortowany od najnowszej do najstarszej wersji. W przypadku
dokumentacji HTML starsze wersje są domyślnie zwijane.

%package -n python3-sphinxcontrib-log-cabinet
Summary:	Sphinx extension to organize changelogs
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do porządkowania changelogów
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-sphinxcontrib-log-cabinet
Sphinx extension to organize changelogs generated by versionadded,
versionchanged, deprecated directives. The log will be sorted by
newest to oldest version. For HTML docs, older versions will be
collapsed by default.

%description -n python3-sphinxcontrib-log-cabinet -l pl.UTF-8
Rozszerzenie Sphinksa do porządkowania changelogów wygenerowanych
przez dyrektywy versionadded, versionchanged i deprecated. Log jest
sortowany od najnowszej do najstarszej wersji. W przypadku
dokumentacji HTML starsze wersje są domyślnie zwijane.

%prep
%setup -q -n sphinxcontrib-log-cabinet-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE.rst README.rst
# XXX: shared dir
%dir %{py_sitescriptdir}/sphinxcontrib
%{py_sitescriptdir}/sphinxcontrib/log_cabinet.py[co]
%{py_sitescriptdir}/sphinxcontrib_log_cabinet-%{version}-py*.egg-info
%{py_sitescriptdir}/sphinxcontrib_log_cabinet-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-sphinxcontrib-log-cabinet
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE.rst README.rst
# XXX: shared dirs
%dir %{py3_sitescriptdir}/sphinxcontrib
%dir %{py3_sitescriptdir}/sphinxcontrib/__pycache__
%{py3_sitescriptdir}/sphinxcontrib/log_cabinet.py
%{py3_sitescriptdir}/sphinxcontrib/__pycache__/log_cabinet.cpython-*.py[co]
%{py3_sitescriptdir}/sphinxcontrib_log_cabinet-%{version}-py*.egg-info
%{py3_sitescriptdir}/sphinxcontrib_log_cabinet-%{version}-py*-nspkg.pth
%endif
