%define bname gstreamer0.10
%define name %bname-plugins-gl
%define version 0.10.2
%define oname gst-plugins-gl
%define majorminor 0.10
%define release 4
%define major 1
%define libname %mklibname gstgl %majorminor %major
%define develname %mklibname -d gstgl %majorminor

Summary:	GStreamer OpenGL Plug-ins
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://gstreamer.freedesktop.org/src/%oname/%{oname}-%{version}.tar.bz2
License:	LGPLv2+
Group:		Sound
Url:		http://gstreamer.freedesktop.org/
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	pkgconfig(liboil-0.3)
BuildRequires:	glew-devel
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig(gtk+-2.0)
#gw it needs clutter 0.8
BuildRequires:	clutter-devel
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(glu)


%description
This module contains integration libraries and plug-ins for using OpenGL
within GStreamer pipelines. This module contains elements for, among others:

* output: glimagesink
* adapters: glupload, gldownload
* video processing: gldeinterlace, glcolorscale
* GL effects: glfiltersobel, glfilterblur, gleffects, others
* sources: gltestsrc


%package -n %{libname}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libname}
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

This package contains the libraries.

%package -n %{develname}
Summary:	Libraries and include files for GStreamer streaming-media framework
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	libgstgl-devel = %{version}-%{release}

%description -n %{develname}
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new   
plugins.

This package contains the libraries and includes files necessary to develop
applications and plugins for GStreamer.



%prep
%setup -q -n %oname-%version

%build
%configure2_5x \
		--disable-dependency-tracking \
		--with-package-name='%{distribution} %{name} package' \
		--with-package-origin='%{disturl}'

%make

%install
%makeinstall_std
%find_lang %oname-%majorminor
# Clean out files that should not be part of the rpm. 
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la


%files -f %oname-%majorminor.lang
%doc RE* NEWS
%_libdir/gstreamer-%majorminor/libgstopengl.so

%files -n %libname
%_libdir/libgstgl-%majorminor.so.%{major}*

%files -n %develname
%doc ChangeLog
%_libdir/libgstgl-%majorminor.so
%_includedir/gstreamer-%majorminor/gst/gl/
%_libdir/pkgconfig/gstreamer-gl-%majorminor.pc
%_datadir/gtk-doc/html/gst-plugins-gl-libs-%majorminor
%_datadir/gtk-doc/html/gst-plugins-gl-plugins-%majorminor



%changelog
* Sat Nov 05 2011 Götz Waschk <waschk@mandriva.org> 0.10.2-3mdv2012.0
+ Revision: 718904
- rebuild

* Fri Nov 05 2010 Funda Wang <fwang@mandriva.org> 0.10.2-2mdv2011.0
+ Revision: 593570
- rebuild for gstreamer provides

* Sat Sep 04 2010 Götz Waschk <waschk@mandriva.org> 0.10.2-1mdv2011.0
+ Revision: 575867
- new version
- new major

* Mon Jul 19 2010 Götz Waschk <waschk@mandriva.org> 0.10.1-2mdv2011.0
+ Revision: 554909
- build without clutter support

* Mon Jul 13 2009 Götz Waschk <waschk@mandriva.org> 0.10.1-1mdv2010.0
+ Revision: 395470
- import gstreamer0.10-plugins-gl


