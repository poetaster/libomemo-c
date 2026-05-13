#
# spec file for package libomemo-c
#
# Copyright (c) 2025 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define c_lib libomemo-c

Name:           libomemo-c
Version:        0.5.1
Release:        0
Summary:        Fork of libsignal-protocol-c adding support for OMEMO XEP-0384 0.5.0+
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/dino/libomemo-c
Source:         https://github.com/dino/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  check-devel
BuildRequires:  ninja
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl) >= 1.0
BuildRequires:  protobuf-c
BuildRequires:  protobuf-c-devel

%description
This is a fork of libsignal-protocol-c, an implementation of Signal's ratcheting
forward secrecy protocol that works in synchronous and asynchronous messaging.
The fork adds support for OMEMO as defined in XEP-0384 versions 0.3.0 and later.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream 

%build
# TODO: Please submit an issue to upstream (rhbz#2380740)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
    -GNinja \
    -DBUILD_TESTING=ON \
    -DLIB_INSTALL_DIR=%{_libdir}
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libomemo-c.so.0*

%files devel
%dir %{_includedir}/omemo
%{_includedir}/omemo/*.h
%{_libdir}/libomemo-c.so
%{_libdir}/pkgconfig/libomemo-c.pc

%changelog

