#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : boto
Version  : 2.48.0
Release  : 44
URL      : http://pypi.debian.net/boto/boto-2.48.0.tar.gz
Source0  : http://pypi.debian.net/boto/boto-2.48.0.tar.gz
Summary  : Amazon Web Services Library
Group    : Development/Tools
License  : MIT
Requires: boto-bin
Requires: boto-legacypython
Requires: boto-python3
Requires: boto-python
BuildRequires : chardet-python
BuildRequires : httpretty-python
BuildRequires : idna-python
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : urllib3-python

%description
boto
        ####
        boto 2.48.0

%package bin
Summary: bin components for the boto package.
Group: Binaries

%description bin
bin components for the boto package.


%package legacypython
Summary: legacypython components for the boto package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the boto package.


%package python
Summary: python components for the boto package.
Group: Default
Requires: boto-legacypython
Requires: boto-python3

%description python
python components for the boto package.


%package python3
Summary: python3 components for the boto package.
Group: Default
Requires: python3-core

%description python3
python3 components for the boto package.


%prep
%setup -q -n boto-2.48.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507149418
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 tests/test.py default || :
%install
export SOURCE_DATE_EPOCH=1507149418
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
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

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
