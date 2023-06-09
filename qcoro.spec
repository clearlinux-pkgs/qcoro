#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
Name     : qcoro
Version  : 0.8.0
Release  : 1
URL      : https://github.com/danvratil/qcoro/archive/refs/tags/v0.8.0.tar.gz
Source0  : https://github.com/danvratil/qcoro/archive/refs/tags/v0.8.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.3 MIT
Requires: qcoro-lib = %{version}-%{release}
Requires: qcoro-license = %{version}-%{release}
BuildRequires : Vulkan-Headers
BuildRequires : Vulkan-Tools
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : glibc-dev
BuildRequires : libxkbcommon-dev
BuildRequires : libxkbfile-dev
BuildRequires : mesa-dev
BuildRequires : openssl-dev
BuildRequires : qt6base-dev
BuildRequires : qtbase-dev
BuildRequires : qttools
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![Linux CI](https://github.com/danvratil/qcoro/actions/workflows/build-linux.yml/badge.svg)](https://github.com/danvratil/qcoro/actions/workflows/build-linux.yml)
[![Windows CI](https://github.com/danvratil/qcoro/actions/workflows/build-windows.yml/badge.svg)](https://github.com/danvratil/qcoro/actions/workflows/build-windows.yml)
[![MacOS CI](https://github.com/danvratil/qcoro/actions/workflows/build-macos.yml/badge.svg)](https://github.com/danvratil/qcoro/actions/workflows/build-macos.yml)
[![Docs build](https://github.com/danvratil/qcoro/actions/workflows/update-docs.yml/badge.svg?branch=main)](https://github.com/danvratil/qcoro/actions/workflows/update-docs.yml)
[![Latest release](https://img.shields.io/github/v/release/danvratil/qcoro?label=%F0%9F%93%A6%20Release)](https://github.com/danvratil/qcoro/releases)
![License: MIT](https://img.shields.io/badge/%E2%9A%96%EF%B8%8F%20License-MIT-brightgreen)
![C++20](https://img.shields.io/badge/C%2B%2B-20-%2300599C?logo=cplusplus)
![Supported Compilers](https://img.shields.io/badge/%E2%9A%99%EF%B8%8F%20Compilers-GCC%2C%20clang%2C%20MSVC-informational)

%package dev
Summary: dev components for the qcoro package.
Group: Development
Requires: qcoro-lib = %{version}-%{release}
Provides: qcoro-devel = %{version}-%{release}
Requires: qcoro = %{version}-%{release}

%description dev
dev components for the qcoro package.


%package lib
Summary: lib components for the qcoro package.
Group: Libraries
Requires: qcoro-license = %{version}-%{release}

%description lib
lib components for the qcoro package.


%package license
Summary: license components for the qcoro package.
Group: Default

%description license
license components for the qcoro package.


%prep
%setup -q -n qcoro-0.8.0
cd %{_builddir}/qcoro-0.8.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1682115087
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake .. -DUSE_QT_VERSION=5
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1682115087
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qcoro
cp %{_builddir}/qcoro-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/qcoro/7e78f78b7c473b6e330b02213c0a45f3d85a1d98 || :
cp %{_builddir}/qcoro-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qcoro/3630f1ffcec0e075bf446b88c7b507b1287b571d || :
cp %{_builddir}/qcoro-%{version}/LICENSES/GFDL-1.3-or-later.txt %{buildroot}/usr/share/package-licenses/qcoro/9f4b4e87b606c795e2ff126522fec25546fb335f || :
cp %{_builddir}/qcoro-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/qcoro/347ce7df3437ef947fc76d294e461f2d7af1ad2a || :
cp %{_builddir}/qcoro-%{version}/docs/about/license.md %{buildroot}/usr/share/package-licenses/qcoro/c225c3c4debd821182d34d51796e174cf3ea54fd || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qcoro5/QCoro/QCoro
/usr/include/qcoro5/QCoro/QCoroAbstractSocket
/usr/include/qcoro5/QCoro/QCoroAsyncGenerator
/usr/include/qcoro5/QCoro/QCoroCore
/usr/include/qcoro5/QCoro/QCoroDBus
/usr/include/qcoro5/QCoro/QCoroDBusPendingCall
/usr/include/qcoro5/QCoro/QCoroDBusPendingReply
/usr/include/qcoro5/QCoro/QCoroFuture
/usr/include/qcoro5/QCoro/QCoroFwd
/usr/include/qcoro5/QCoro/QCoroGenerator
/usr/include/qcoro5/QCoro/QCoroIODevice
/usr/include/qcoro5/QCoro/QCoroImageProvider
/usr/include/qcoro5/QCoro/QCoroLocalSocket
/usr/include/qcoro5/QCoro/QCoroNetwork
/usr/include/qcoro5/QCoro/QCoroNetworkReply
/usr/include/qcoro5/QCoro/QCoroProcess
/usr/include/qcoro5/QCoro/QCoroQml
/usr/include/qcoro5/QCoro/QCoroQmlTask
/usr/include/qcoro5/QCoro/QCoroSignal
/usr/include/qcoro5/QCoro/QCoroTask
/usr/include/qcoro5/QCoro/QCoroTcpServer
/usr/include/qcoro5/QCoro/QCoroThread
/usr/include/qcoro5/QCoro/QCoroTimer
/usr/include/qcoro5/QCoro/QCoroWebSocket
/usr/include/qcoro5/QCoro/QCoroWebSocketServer
/usr/include/qcoro5/QCoro/QCoroWebSockets
/usr/include/qcoro5/QCoro/Task
/usr/include/qcoro5/qcoro/concepts_p.h
/usr/include/qcoro5/qcoro/config.h
/usr/include/qcoro5/qcoro/coroutine.h
/usr/include/qcoro5/qcoro/macros_p.h
/usr/include/qcoro5/qcoro/qcoro.h
/usr/include/qcoro5/qcoro/qcoroabstractsocket.h
/usr/include/qcoro5/qcoro/qcoroasyncgenerator.h
/usr/include/qcoro5/qcoro/qcorocore.h
/usr/include/qcoro5/qcoro/qcorocore_export.h
/usr/include/qcoro5/qcoro/qcorodbus.h
/usr/include/qcoro5/qcoro/qcorodbus_export.h
/usr/include/qcoro5/qcoro/qcorodbuspendingcall.h
/usr/include/qcoro5/qcoro/qcorodbuspendingreply.h
/usr/include/qcoro5/qcoro/qcorofuture.h
/usr/include/qcoro5/qcoro/qcorofwd.h
/usr/include/qcoro5/qcoro/qcorogenerator.h
/usr/include/qcoro5/qcoro/qcoroimageprovider.h
/usr/include/qcoro5/qcoro/qcoroiodevice.h
/usr/include/qcoro5/qcoro/qcorolocalsocket.h
/usr/include/qcoro5/qcoro/qcoronetwork.h
/usr/include/qcoro5/qcoro/qcoronetwork_export.h
/usr/include/qcoro5/qcoro/qcoronetworkreply.h
/usr/include/qcoro5/qcoro/qcoroprocess.h
/usr/include/qcoro5/qcoro/qcoroqml.h
/usr/include/qcoro5/qcoro/qcoroqml_export.h
/usr/include/qcoro5/qcoro/qcoroqmltask.h
/usr/include/qcoro5/qcoro/qcoroquick_export.h
/usr/include/qcoro5/qcoro/qcorosignal.h
/usr/include/qcoro5/qcoro/qcorotask.h
/usr/include/qcoro5/qcoro/qcorotcpserver.h
/usr/include/qcoro5/qcoro/qcorothread.h
/usr/include/qcoro5/qcoro/qcorotimer.h
/usr/include/qcoro5/qcoro/qcorowebsocket.h
/usr/include/qcoro5/qcoro/qcorowebsockets.h
/usr/include/qcoro5/qcoro/qcorowebsockets_export.h
/usr/include/qcoro5/qcoro/qcorowebsocketserver.h
/usr/include/qcoro5/qcoro/task.h
/usr/include/qcoro5/qcoro/waitoperationbase_p.h
/usr/lib64/cmake/QCoro5/QCoro5Config.cmake
/usr/lib64/cmake/QCoro5/QCoro5ConfigVersion.cmake
/usr/lib64/cmake/QCoro5Core/QCoro5CoreConfig.cmake
/usr/lib64/cmake/QCoro5Core/QCoro5CoreConfigVersion.cmake
/usr/lib64/cmake/QCoro5Core/QCoro5CoreTargets-relwithdebinfo.cmake
/usr/lib64/cmake/QCoro5Core/QCoro5CoreTargets.cmake
/usr/lib64/cmake/QCoro5Coro/QCoro5CoroConfig.cmake
/usr/lib64/cmake/QCoro5Coro/QCoro5CoroConfigVersion.cmake
/usr/lib64/cmake/QCoro5Coro/QCoro5CoroTargets.cmake
/usr/lib64/cmake/QCoro5Coro/QCoroMacros.cmake
/usr/lib64/cmake/QCoro5DBus/QCoro5DBusConfig.cmake
/usr/lib64/cmake/QCoro5DBus/QCoro5DBusConfigVersion.cmake
/usr/lib64/cmake/QCoro5DBus/QCoro5DBusTargets-relwithdebinfo.cmake
/usr/lib64/cmake/QCoro5DBus/QCoro5DBusTargets.cmake
/usr/lib64/cmake/QCoro5Network/QCoro5NetworkConfig.cmake
/usr/lib64/cmake/QCoro5Network/QCoro5NetworkConfigVersion.cmake
/usr/lib64/cmake/QCoro5Network/QCoro5NetworkTargets-relwithdebinfo.cmake
/usr/lib64/cmake/QCoro5Network/QCoro5NetworkTargets.cmake
/usr/lib64/cmake/QCoro5Qml/QCoro5QmlConfig.cmake
/usr/lib64/cmake/QCoro5Qml/QCoro5QmlConfigVersion.cmake
/usr/lib64/cmake/QCoro5Qml/QCoro5QmlTargets-relwithdebinfo.cmake
/usr/lib64/cmake/QCoro5Qml/QCoro5QmlTargets.cmake
/usr/lib64/cmake/QCoro5Quick/QCoro5QuickConfig.cmake
/usr/lib64/cmake/QCoro5Quick/QCoro5QuickConfigVersion.cmake
/usr/lib64/cmake/QCoro5Quick/QCoro5QuickTargets-relwithdebinfo.cmake
/usr/lib64/cmake/QCoro5Quick/QCoro5QuickTargets.cmake
/usr/lib64/cmake/QCoro5WebSockets/QCoro5WebSocketsConfig.cmake
/usr/lib64/cmake/QCoro5WebSockets/QCoro5WebSocketsConfigVersion.cmake
/usr/lib64/cmake/QCoro5WebSockets/QCoro5WebSocketsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/QCoro5WebSockets/QCoro5WebSocketsTargets.cmake
/usr/lib64/libQCoro5Core.so
/usr/lib64/libQCoro5DBus.so
/usr/lib64/libQCoro5Network.so
/usr/lib64/libQCoro5Qml.so
/usr/lib64/libQCoro5Quick.so
/usr/lib64/libQCoro5WebSockets.so
/usr/lib64/qt5/mkspecs/modules/qt_QCoroCore.pri
/usr/lib64/qt5/mkspecs/modules/qt_QCoroCoro.pri
/usr/lib64/qt5/mkspecs/modules/qt_QCoroDBus.pri
/usr/lib64/qt5/mkspecs/modules/qt_QCoroNetwork.pri
/usr/lib64/qt5/mkspecs/modules/qt_QCoroQml.pri
/usr/lib64/qt5/mkspecs/modules/qt_QCoroQuick.pri
/usr/lib64/qt5/mkspecs/modules/qt_QCoroWebSockets.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQCoro5Core.so.0
/usr/lib64/libQCoro5Core.so.0.8.0
/usr/lib64/libQCoro5DBus.so.0
/usr/lib64/libQCoro5DBus.so.0.8.0
/usr/lib64/libQCoro5Network.so.0
/usr/lib64/libQCoro5Network.so.0.8.0
/usr/lib64/libQCoro5Qml.so.0
/usr/lib64/libQCoro5Qml.so.0.8.0
/usr/lib64/libQCoro5Quick.so.0
/usr/lib64/libQCoro5Quick.so.0.8.0
/usr/lib64/libQCoro5WebSockets.so.0
/usr/lib64/libQCoro5WebSockets.so.0.8.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qcoro/347ce7df3437ef947fc76d294e461f2d7af1ad2a
/usr/share/package-licenses/qcoro/3630f1ffcec0e075bf446b88c7b507b1287b571d
/usr/share/package-licenses/qcoro/7e78f78b7c473b6e330b02213c0a45f3d85a1d98
/usr/share/package-licenses/qcoro/9f4b4e87b606c795e2ff126522fec25546fb335f
/usr/share/package-licenses/qcoro/c225c3c4debd821182d34d51796e174cf3ea54fd
