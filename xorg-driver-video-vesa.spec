Summary:	X.org video driver for generic VESA video cards
Name:		xorg-driver-video-vesa
Version:	2.3.2
Release:	3
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vesa-%{version}.tar.bz2
# Source0-md5:	3eddd393fba79550e012d717499d58ad
Patch0:		%{name}-remove-mibstore.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-proto
BuildRequires:	xorg-util-macros
BuildRequires:	xorg-xserver-server-devel
Requires:	xorg-xserver-server
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for generic VESA video cards.

%prep
%setup -qn xf86-video-vesa-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/vesa_drv.so
%{_mandir}/man4/vesa.4*

