%define c_lib libomemo-c0
Name:           libomemo-c
Version:        0.5.1
Release:        0
Summary:        Fork of libsignal-protocol-c adding support for OMEMO XEP-0384 0.5.0+
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/dino/libomemo-c
Source:         https://github.com/dino/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  check-devel
BuildRequires:  cmake >= 2.8.4
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl) >= 1.0
BuildRequires:  protobuf-c
BuildRequires:  protobuf-c-devel

%description
This is a fork of libsignal-protocol-c, an implementation of Signal's ratcheting forward secrecy protocol that works in synchronous and asynchronous messaging. The fork adds support for OMEMO as defined in XEP-0384 versions 0.3.0 and later.

%package -n libomemo-c-devel
Summary:        Development files for libomemo-c
Group:          Development/Libraries/C and C++
Requires:       %{c_lib} = %{version}
Requires:       protobuf-c-devel

%description -n libomemo-c-devel
Development files and headers for libomemo-c

%package -n %{c_lib}
Summary:        Omemo C Library
Group:          System/Libraries

%description -n %{c_lib}
The libomemo-c library is a forward secrecy protocol library written in C.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake \
    -DBUILD_TESTING=ON

%cmake_build

%install
%cmake_install

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest

%post -n %{c_lib} -p /sbin/ldconfig
%postun -n %{c_lib} -p /sbin/ldconfig

%files -n %{c_lib}
%license LICENSE
%doc README.md
%{_libdir}/libomemo-c.so.*

%files devel
%dir %{_includedir}/omemo
%{_includedir}/omemo/*.h
%{_libdir}/libomemo-c.so
%{_libdir}/pkgconfig/libomemo-c.pc

%changelog
