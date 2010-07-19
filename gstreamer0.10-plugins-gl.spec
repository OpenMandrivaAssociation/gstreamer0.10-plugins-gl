%define bname gstreamer0.10
%define name %bname-plugins-gl
%define version 0.10.1
%define oname gst-plugins-gl
%define majorminor 0.10
%define release %mkrel 2
%define major 0
%define libname %mklibname gstgl %majorminor %major
%define develname %mklibname -d gstgl %majorminor

Summary: GStreamer OpenGL Plug-ins
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://gstreamer.freedesktop.org/src/%oname/%{oname}-%{version}.tar.bz2
License: LGPLv2+
Group: Sound
Url: http://gstreamer.freedesktop.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgstreamer0.10-plugins-base-devel >= 0.10.15.1
BuildRequires: liboil-devel >= 0.3.8
BuildREquires: glew-devel
BuildREquires: libpng-devel
BuildREquires: gtk+2-devel
#gw it needs clutter 0.8
BuildREquires: clutter-devel
BuildRequires: gtk-doc


%description
This module contains integration libraries and plug-ins for using OpenGL
within GStreamer pipelines. This module contains elements for, among others:

* output: glimagesink
* adapters: glupload, gldownload
* video processing: gldeinterlace, glcolorscale
* GL effects: glfiltersobel, glfilterblur, gleffects, others
* sources: gltestsrc


%package -n %libname
Summary: Libraries for GStreamer streaming-media framework
Group: System/Libraries

%description -n %libname
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

This package contains the libraries.

%package -n %develname
Summary: Libraries and include files for GStreamer streaming-media framework
Group: Development/C
Requires: %{libname} = %{version}
Provides: libgstgl-devel = %version-%release

%description -n %develname
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
%configure2_5x --disable-dependency-tracking \
  --with-package-name='Mandriva %name package' \
  --with-package-origin='http://www.mandriva.com/'

%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %oname-%majorminor
# Clean out files that should not be part of the rpm. 
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%check
cd tests/check
make check

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %oname-%majorminor.lang
%defattr(-, root, root)
%doc RE* NEWS
%_libdir/gstreamer-%majorminor/libgstopengl.so

%files -n %libname
%defattr(-, root, root)
%_libdir/libgstgl-%majorminor.so.%{major}*

%files -n %develname
%defattr(-, root, root)
%doc ChangeLog
%_libdir/libgstgl-%majorminor.so
%_includedir/gstreamer-%majorminor/gst/gl/
%_libdir/pkgconfig/gstreamer-gl-%majorminor.pc
%_datadir/gtk-doc/html/gst-plugins-gl-libs-%majorminor
%_datadir/gtk-doc/html/gst-plugins-gl-plugins-%majorminor

