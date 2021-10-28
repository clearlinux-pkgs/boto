#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : boto
Version  : 2.49.0
Release  : 75
URL      : https://files.pythonhosted.org/packages/c8/af/54a920ff4255664f5d238b5aebd8eedf7a07c7a5e71e27afcfe840b82f51/boto-2.49.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c8/af/54a920ff4255664f5d238b5aebd8eedf7a07c7a5e71e27afcfe840b82f51/boto-2.49.0.tar.gz
Summary  : Amazon Web Services Library
Group    : Development/Tools
License  : MIT
Requires: boto-bin = %{version}-%{release}
Requires: boto-python = %{version}-%{release}
Requires: boto-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : httpretty-python
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : requests-python
BuildRequires : setuptools

%description
boto
        ####
        boto 2.49.0

%package bin
Summary: bin components for the boto package.
Group: Binaries

%description bin
bin components for the boto package.


%package python
Summary: python components for the boto package.
Group: Default
Requires: boto-python3 = %{version}-%{release}

%description python
python components for the boto package.


%package python3
Summary: python3 components for the boto package.
Group: Default
Requires: python3-core
Provides: pypi(boto)

%description python3
python3 components for the boto package.


%prep
%setup -q -n boto-2.49.0
cd %{_builddir}/boto-2.49.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1601606791
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 tests/test.py default || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/asadmin
/usr/bin/bundle_image
/usr/bin/cfadmin
/usr/bin/cq
/usr/bin/cwutil
/usr/bin/dynamodb_dump
/usr/bin/dynamodb_load
/usr/bin/elbadmin
/usr/bin/fetch_file
/usr/bin/glacier
/usr/bin/instance_events
/usr/bin/kill_instance
/usr/bin/launch_instance
/usr/bin/list_instances
/usr/bin/lss3
/usr/bin/mturk
/usr/bin/pyami_sendmail
/usr/bin/route53
/usr/bin/s3put
/usr/bin/sdbadmin
/usr/bin/taskadmin

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
