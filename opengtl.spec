Summary: Open Graphics Transformation Languages
Name: opengtl
Version: 0.9.9
Release: %mkrel 2
Source0: http://www.opengtl.org/download/OpenGTL-%{version}.tar.bz2
License: LGPLv2+
Group: System/Libraries
Url: http://www.opengtl.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: cmake
BuildRequires: zlib-devel
BuildRequires: png-devel
BuildRequires: llvm = 2.5
Provides: OpenGTL = %version

%description
Graphics Transformation Languages is a set of library for using and
integrating transformation algorithms (such as filter or color conversion)
in graphics applications

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/OpenGTL

#-------------------------------------------------------------------

%define major 0.6
%define libname %mklibname %name %major

%package -n %libname
Summary: OpenGTL library
Group: System/Libraries

%description -n %libname
OpenGTL library.

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

#-------------------------------------------------------------------
%define develname %mklibname -d %name

%package -n %develname
Summary: OpenGTL development files
Group: Development/C++
Requires: %{libname} = %{version}-%{release}
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
%cmake
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
rm -rf %{buildroot}
