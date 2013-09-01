%bcond_with docs

Summary: Open Graphics Transformation Languages
Name: opengtl
Version: 0.9.18
Release: 1
Source0: http://download.opengtl.org/OpenGTL-%{version}.tar.bz2
Patch0: OpenGTL-0.9.17-fix-link.patch
Patch1: OpenGTL-0.9.16-llvm-linkage.patch
Patch2: opengtl-0.9.18-llvm-3.3.patch
License: LGPLv2+
Group: System/Libraries
Url: http://www.opengtl.org/
BuildRequires: cmake
BuildRequires: zlib-devel
BuildRequires: png-devel
BuildRequires: llvm-devel >= 3.0
Requires: llvm >= 3.0
Provides: OpenGTL = %{EVRD}
%if %{with docs}
BuildRequires: texlive-latex texlive-tools texlive-graphics texlive-pdftex-def texlive-oberdiek texlive-listings
BuildRequires: imagemagick texlive-bibtex texlive-makeindex texlive-texconfig
%endif

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

%define libgtlfragment_major 0
%define libgtlfragment %mklibname gtlfragment %libgtlfragment_major

%package -n %libgtlfragment
Summary: OpenGTL fragment library
Group: System/Libraries
Conflicts: %{_lib}opengtl0.6 < 0.9.13

%description -n %libgtlfragment
OpenGTL fragment library.

%files -n %libgtlfragment
%defattr(-,root,root)
%_libdir/libGTLFragment.so.%{libgtlfragment_major}*

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
Requires: %libgtlcore = %{version}
Requires: %libopenshiva = %{version}
Requires: %libopenctl = %{version}
Requires: %libgtlimageio = %{version}
Provides: OpenGTL-devel = %{EVRD}
Provides: %{name}-devel = %{EVRD}
Provides: OpenCTL-devel = %{EVRD}
Provides: openctl-devel = %{EVRD}

%description -n %develname
This package contains header files needed if you wish to build applications
based on OpenGTL.

%files -n %develname
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%if %{with docs}
%doc %_docdir/OpenGTL/shiva/ShivaRef.pdf
%endif

#--------------------------------------------------------------------

%prep
%setup -q -n OpenGTL-%{version}
%patch0 -p0 -b .linkage~
%patch1 -p1 -b .llvmlink~
%patch2 -p1 -b .llvm33~

%build
# OVERRIDE_LLVM_ASSERT is ok because our llvm is built without
# asserts -- the detection code is off
%cmake -DOVERIDE_LLVM_ASSERT:BOOL=TRUE
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build



%changelog
* Wed Apr 18 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.9.16-1
+ Revision: 791748
- Introduce bcond for building docs
- 0.9.16
- Fix BuildRequires for docs
- Fix LLVM linkage

* Tue Apr 26 2011 Funda Wang <fwang@mandriva.org> 0.9.15.1-1
+ Revision: 659203
- requires llvm 2.9
- New version 0.9.15.1

* Sun Oct 24 2010 Funda Wang <fwang@mandriva.org> 0.9.15-2mdv2011.0
+ Revision: 589150
- correct file list
- renew tarball

* Sun Oct 24 2010 Funda Wang <fwang@mandriva.org> 0.9.15-1mdv2011.0
+ Revision: 588717
- patch to build with llvm 2.8
- new verson 0.9.15

* Wed Aug 04 2010 Funda Wang <fwang@mandriva.org> 0.9.14-3mdv2011.0
+ Revision: 565785
- renew tarball with llvm 2.7

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - rebuild for missing packages, eaten by the BS

* Tue May 18 2010 Funda Wang <fwang@mandriva.org> 0.9.14-2mdv2010.1
+ Revision: 545070
- add patch fix build with latest ldflags
- fix conflicts with

* Tue Mar 16 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.9.14-1mdv2010.1
+ Revision: 521124
- Update for koffice

* Mon Mar 15 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.9.13-2mdv2010.1
+ Revision: 519945
- Fix file list
- Fix used macros
  fix conflicts with previous lib
- New version 0.9.13

* Wed Nov 25 2009 Funda Wang <fwang@mandriva.org> 0.9.12-1mdv2010.1
+ Revision: 469908
- New versino 0.9.12

* Thu Sep 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.9.10-1mdv2010.0
+ Revision: 443967
- New version 0.9.10

* Thu Jul 30 2009 Funda Wang <fwang@mandriva.org> 0.9.9-2mdv2010.0
+ Revision: 404528
- add openctl provides

* Wed Jul 29 2009 Funda Wang <fwang@mandriva.org> 0.9.9-1mdv2010.0
+ Revision: 403874
- fix license
- import opengtl

