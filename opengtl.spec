Summary: Open Graphics Transformation Languages
Name: opengtl
Version: 0.9.13
Release: %mkrel 1
Source0: http://www.opengtl.org/download/OpenGTL-%{version}.tar.bz2
License: LGPLv2+
Group: System/Libraries
Url: http://www.opengtl.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: cmake
BuildRequires: zlib-devel
BuildRequires: png-devel
BuildRequires: llvm = 2.6
Requires: llvm = 2.6
Provides: OpenGTL = %version

%description
Graphics Transformation Languages is a set of library for using and
integrating transformation algorithms (such as filter or color conversion)
in graphics applications

%files
%defattr(-,root,root)
%doc %_docdir/OpenGTL/shiva/ShivaRef.pdf
%{_bindir}/*
%{_libdir}/GTLImageIO
%{_datadir}/OpenGTL

#--------------------------------------------------------------------

%define libgtlcore_major 0
%define libgtlcore %mklibname gtlcore %libgtlcore_major

%package -n %libgtlcore
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libgtlcore
Koffice 2 core library.

%files -n %libgtlcore
%defattr(-,root,root)
%_kde_libdir/libGTLCore.so.%{libgtlcore_major}*

#--------------------------------------------------------------------

%define libgtlimageio_major 0
%define libgtlimageio %mklibname gtlimageio %libgtlimageio_major

%package -n %libgtlimageio
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libgtlimageio
Koffice 2 core library.

%files -n %libgtlimageio
%defattr(-,root,root)
%_kde_libdir/libGTLImageIO.so.%{libgtlimageio_major}*

#--------------------------------------------------------------------

%define libopenctl_major 0
%define libopenctl %mklibname openctl %libopenctl_major

%package -n %libopenctl
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libopenctl
Koffice 2 core library.

%files -n %libopenctl
%defattr(-,root,root)
%_kde_libdir/libOpenCTL.so.%{libopenctl_major}*

#--------------------------------------------------------------------

%define libopenshiva_major 0
%define libopenshiva %mklibname openshiva %libopenshiva_major

%package -n %libopenshiva
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libopenshiva
Koffice 2 core library.

%files -n %libopenshiva
%defattr(-,root,root)
%_kde_libdir/libOpenShiva.so.%{libopenshiva_major}*

#--------------------------------------------------------------------

%define develname %mklibname -d %name

%package -n %develname
Summary: OpenGTL development files
Group: Development/C++
Requires: %libgtlcore = %{version}-%{release}
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
%setup -q -n OpenGTL-%version

%build
%define _disable_ld_no_undefined 1
%cmake
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
rm -rf %{buildroot}
