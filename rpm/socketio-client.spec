%global commit0 %{COMMIT_ID}
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           socketio-client-cpp
Version:        1.6.0
Release:	%{shortcommit0}%{dist}
Summary:	Socket.IO C++ client
Group:		Development/Libraries
License:	MIT
URL:      https://github.com/socketio/socket.io-client-cpp
Source0:	socket.io-client-cpp-%{COMMIT_ID}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}%{dist}-XXXXXX)
BuildRequires:	boost-date-time, boost-random, boost-system, cmake, make, openssl-devel, rpm-build
Requires:	boost-date-time, boost-random, boost-system, cmake, make, openssl-devel

%description
Socket.IO C++ client package.
Originally maintained here: https://github.com/socketio/socket.io-client-cpp
For details, please refer to the site.
For the packaging of shared library version is by https://github.com/dkmoon/socket.io-client-cpp


#%define debug_package %{nil}


%prep
%setup -q -n socket.io-client-cpp


%build
mkdir rpm_build_result
pushd rpm_build_result
cmake  -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS=ON -DBoost_USE_STATIC_LIBS=OFF ..
make
popd


%install
rm -rf %{buildroot}
pushd rpm_build_result
DESTDIR=%{buildroot} make install
popd


%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,root,0755)
/usr/lib/libsioclient.so*
/usr/lib/libsioclient_tls.so*


%post
/sbin/ldconfig


%postun
/sbin/ldconfig



%package devel
Summary:	Socket.IO C++ client
Group:		Development/Libraries
Requires:       socketio-client-cpp = %{version}-%{release}


%description devel
Socket.IO C++ client header package.
Originally maintained here: https://github.com/socketio/socket.io-client-cpp
For details, please refer to the site.
For the packaging of shared library version is by https://github.com/dkmoon/socket.io-client-cpp


%files devel
%defattr(0644,root,root,0755)
/usr/include/sio_client.h
/usr/include/sio_message.h
/usr/include/sio_socket.h


#%changelog
