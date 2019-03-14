# Created by pyp2rpm-2.0.0
%global pypi_name pep8
%global with_python2 1
%define version 1.7.1

Name:           python-%{pypi_name}
Version:        %{version}
Release:        1
Group:          Development/Python
Summary:        pep8 is a tool to check your Python code against some of the style conventions in PEP 8.

License:        MIT
URL:            https://pep8.readthedocs.io/en/release-1.7.x/
Source0:        https://files.pythonhosted.org/packages/01/a0/64ba19519db49e4094d82599412a9660dee8c26a7addbbb1bf17927ceefe/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
 
%if %{with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif # if with_python2


%description
pep8 is a tool to check your Python code against some of the style conventions in PEP 8.
It provides a plugin architecture so adding new checks is easy.
It offers parseable output which allows you to Jump to error location in your editor.

%if %{with_python2}
%package -n     python2-%{pypi_name}
Summary:        pep8 is a tool to check your Python code against some of the style conventions in PEP 8.

%description -n python2-%{pypi_name}
pep8 is a tool to check your Python code against some of the style conventions in PEP 8.
It provides a plugin architecture so adding new checks is easy.
It offers parseable output which allows you to Jump to error location in your editor.
%endif # with_python2


%prep
%setup -q -n %{pypi_name}-%{version}

%if %{with_python2}
rm -rf %{py2dir}
cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'
%endif # with_python2


%build
%{__python} setup.py build

%if %{with_python2}
pushd %{py2dir}
%{__python2} setup.py build
popd
%endif # with_python2


%install

%if %{with_python2}
pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python2

%{__python} setup.py install --skip-build --root %{buildroot}


%files
%doc  CONTRIBUTING.rst README.rst CHANGES.txt
%{_bindir}/pep8
%{python_sitelib}/*/*
%{python_sitelib}/pep8.py


%if %{with_python2}
%files -n python2-%{pypi_name}
%doc  CONTRIBUTING.rst README.rst CHANGES.txt
%{python2_sitelib}/*/*
%{python2_sitelib}/pep8.*
%endif # with_python2

