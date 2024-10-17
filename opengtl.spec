%bcond_with docs

%define api 0.8

Summary:	Open Graphics Transformation Languages
Name:		opengtl
Version:	0.9.18
Release:	11
License:	LGPLv2+
Group:		System/Libraries
Url:		https://www.opengtl.org/
Source0:	http://download.opengtl.org/OpenGTL-%{version}.tar.bz2
Patch0:		OpenGTL-0.9.18-fix-link.patch
Patch1:		OpenGTL-0.9.17-libpng-1.6.patch
Patch2:		opengtl-0.9.18-llvm-3.4.patch
Patch3:		opengtl-0.9.18-llvm-3.5.patch
BuildRequires:	cmake
BuildRequires:	llvm-devel >= 3.0
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(zlib)
Requires:	llvm >= 3.0
Provides:	OpenGTL = %{EVRD}
%if %{with docs}
BuildRequires:	imagemagick
BuildRequires:	texlive-bibtex
BuildRequires:	texlive-graphics
BuildRequires:	texlive-latex
BuildRequires:	texlive-listings
BuildRequires:	texlive-makeindex
BuildRequires:	texlive-oberdiek
BuildRequires:	texlive-pdftex-def
BuildRequires:	texlive-tools
BuildRequires:	texlive-texconfig
%endif

%description
Graphics Transformation Languages is a set of library for using and
integrating transformation algorithms (such as filter or color conversion)
in graphics applications

%files
%{_bindir}/*
%{_libdir}/GTLImageIO
%{_datadir}/OpenGTL

#--------------------------------------------------------------------

%define libgtlcore_major 0
%define libgtlcore %mklibname gtlcore %{api} %{libgtlcore_major}

%package -n %{libgtlcore}
Summary:	OpenGTL core library
Group:		System/Libraries
Conflicts:	%{_lib}opengtl0.6 < 0.9.13
Obsoletes:	%{_lib}gtlcore0 < 0.9.18

%description -n %{libgtlcore}
OpenGTL core library.

%files -n %{libgtlcore}
%{_libdir}/libGTLCore.so.%{libgtlcore_major}*

#--------------------------------------------------------------------

%define libgtlfragment_major 0
%define libgtlfragment %mklibname gtlfragment %{api} %{libgtlfragment_major}

%package -n %{libgtlfragment}
Summary:	OpenGTL fragment library
Group:		System/Libraries
Conflicts:	%{_lib}opengtl0.6 < 0.9.13
Obsoletes:	%{_lib}gtlfragment0 < 0.9.18

%description -n %{libgtlfragment}
OpenGTL fragment library.

%files -n %{libgtlfragment}
%{_libdir}/libGTLFragment.so.%{libgtlfragment_major}*

#--------------------------------------------------------------------

%define libgtlimageio_major 0
%define libgtlimageio %mklibname gtlimageio %{api} %{libgtlimageio_major}

%package -n %{libgtlimageio}
Summary:	OpenGTL core library
Group:		System/Libraries
Conflicts:	%{_lib}opengtl0.6 < 0.9.13
Obsoletes:	%{_lib}gtlimageio0 < 0.9.18

%description -n %{libgtlimageio}
OpenGTL core library.

%files -n %{libgtlimageio}
%{_libdir}/libGTLImageIO.so.%{libgtlimageio_major}*

#--------------------------------------------------------------------

%define libopenctl_major 0
%define libopenctl %mklibname openctl %{api} %{libopenctl_major}

%package -n %{libopenctl}
Summary:	OpenGTL core library
Group:		System/Libraries
Conflicts:	%{_lib}opengtl0.6 < 0.9.13
Obsoletes:	%{_lib}openctl0 < 0.9.18

%description -n %{libopenctl}
OpenGTL core library.

%files -n %{libopenctl}
%{_libdir}/libOpenCTL.so.%{libopenctl_major}*

#--------------------------------------------------------------------

%define libopenshiva_major 0
%define libopenshiva %mklibname openshiva %{api} %{libopenshiva_major}

%package -n %{libopenshiva}
Summary:	OpenGTL core library
Group:		System/Libraries
Conflicts:	%{_lib}opengtl0.6 < 0.9.13
Obsoletes:	%{_lib}openshiva0 < 0.9.18

%description -n %{libopenshiva}
OpenGTL core library.

%files -n %{libopenshiva}
%{_libdir}/libOpenShiva.so.%{libopenshiva_major}*

#--------------------------------------------------------------------

%define devname %mklibname -d %{name}

%package -n %{devname}
Summary:	OpenGTL development files
Group:		Development/C++
Requires:	%{libgtlcore} = %{EVRD}
Requires:	%{libopenshiva} = %{EVRD}
Requires:	%{libopenctl} = %{EVRD}
Requires:	%{libgtlimageio} = %{EVRD}
Provides:	OpenGTL-devel = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	OpenCTL-devel = %{EVRD}
Provides:	openctl-devel = %{EVRD}

%description -n %{devname}
This package contains header files needed if you wish to build applications
based on OpenGTL.

%files -n %{devname}
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%if %{with docs}
%doc %{_docdir}/OpenGTL/shiva/ShivaRef.pdf
%endif

#--------------------------------------------------------------------

%prep
%setup -q -n OpenGTL-%{version}
%patch0 -p0 -b .linkage~
%patch1 -p0 -b .png~
%patch2 -p1 -b .llvm33~
%patch3 -p1 -b .llvm35~

%build
# OVERRIDE_LLVM_ASSERT is ok because our llvm is built without
# asserts -- the detection code is off
export CXXFLAGS="$RPM_OPT_FLAGS -std=gnu++11"
%cmake -DOVERIDE_LLVM_ASSERT:BOOL=TRUE
%make

%install
%makeinstall_std -C build

