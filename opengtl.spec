Summary: Open Graphics Transformation Languages
Name: opengtl
Version: 0.9.15.1
Release: %mkrel 1
Source0: http://www.opengtl.org/download/OpenGTL-%{version}.tar.bz2
Patch0: OpenGTL-0.9.14-fix-link.patch
License: LGPLv2+
Group: System/Libraries
Url: http://www.opengtl.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: cmake
BuildRequires: zlib-devel
BuildRequires: png-devel
BuildRequires: llvm = 2.8
Requires: llvm = 2.8
Provides: OpenGTL = %version
Obsoletes: %{_lib}gtlfragment0 < 0.9.16

%description
Graphics Transformation Languages is a set of library for using and
integrating transformation algorithms (such as filter or color conversion)
in graphics applications

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/GTLImageIO
%{_datadir}/OpenGTL

#--------------------------------------------------------------------

%define libgtlcore_major 0
%define libgtlcore %mklibname gtlcore %libgtlcore_major

%package -n %libgtlcore
Summary: OpenGTL core library
Group: System/Libraries
Conflicts: %{_lib}opengtl0.6 < 0.9.13

%description -n %libgtlcore
OpenGTL core library.

%files -n %libgtlcore
%defattr(-,root,root)
%_libdir/libGTLCore.so.%{libgtlcore_major}*

#--------------------------------------------------------------------

%define libgtlimageio_major 0
%define libgtlimageio %mklibname gtlimageio %libgtlimageio_major

%package -n %libgtlimageio
Summary: OpenGTL core library
Group: System/Libraries
Conflicts: %{_lib}opengtl0.6 < 0.9.13

%description -n %libgtlimageio
OpenGTL core library.

%files -n %libgtlimageio
%defattr(-,root,root)
%_libdir/libGTLImageIO.so.%{libgtlimageio_major}*

#--------------------------------------------------------------------

%define libopenctl_major 0
%define libopenctl %mklibname openctl %libopenctl_major

%package -n %libopenctl
Summary: OpenGTL core library
Group: System/Libraries
Conflicts: %{_lib}opengtl0.6 < 0.9.13

%description -n %libopenctl
OpenGTL core library.

%files -n %libopenctl
%defattr(-,root,root)
%_libdir/libOpenCTL.so.%{libopenctl_major}*

#--------------------------------------------------------------------

%define libopenshiva_major 0
%define libopenshiva %mklibname openshiva %libopenshiva_major

%package -n %libopenshiva
Summary: OpenGTL core library
Group: System/Libraries
Conflicts: %{_lib}opengtl0.6 < 0.9.13

%description -n %libopenshiva
OpenGTL core library.

%files -n %libopenshiva
%defattr(-,root,root)
%_libdir/libOpenShiva.so.%{libopenshiva_major}*

#--------------------------------------------------------------------

%define develname %mklibname -d %name

%package -n %develname
Summary: OpenGTL development files
Group: Development/C++
Requires: %libgtlcore = %{version}-%{release}
Requires: %libopenshiva = %{version}-%{release}
Requires: %libopenctl = %{version}-%{release}
Requires: %libgtlimageio = %{version}-%{release}
Provides: OpenGTL-devel = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Provides: OpenCTL-devel = %{version}-%{release}
Provides: openctl-devel = %{version}-%{release}

%description -n %develname
This package contains header files needed if you wish to build applications
based on OpenGTL.

%files -n %develname
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

#--------------------------------------------------------------------

%prep
%setup -q -n OpenGTL-%{version}
%patch0 -p0

%build
%cmake
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
rm -rf %{buildroot}
