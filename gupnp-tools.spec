Summary:	UPnP Tools
Name:		gupnp-tools
Version:	0.8
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.gupnp.org/sources/gupnp-tools/%{name}-%{version}.tar.gz
# Source0-md5:	e2122d273d8ae6bf1cbca94fc4659e90
Patch0:		%{name}-configure.patch
URL:		http://www.gupnp.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.18.0
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	gupnp-av-devel >= 0.5.0
BuildRequires:	gupnp-devel >= 0.13.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GUPnP Tools are free replacements of Intel UPnP tools that use GUPnP.
They provides the following client and server side tools which enable
one to easily test and debug one's UPnP devices and control points:

- Universal Control Point: a tool that enables one to discover UPnP
  devices and services, retrieve information about them, subscribe to
  events and invoke actions.

- Network Light: a virtual light bulb that allows control points to
  switch it on and off, change its dimming level and query its current
  status. It also provides a simple UI to control all the network lights
  available on the network.

- AV Control Point: a simple media player UI that enables one to
  discover and play multimedia contents available on a network.

- Upload: a simple commandline utility that uploads files to known
  MediaServers. Use Universal Control Point for discovering the
  MediaServers.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gupnp-av-cp
%attr(755,root,root) %{_bindir}/gupnp-network-light
%attr(755,root,root) %{_bindir}/gupnp-universal-cp
%attr(755,root,root) %{_bindir}/gupnp-upload
%{_datadir}/gupnp-tools
%{_desktopdir}/gupnp-av-cp.desktop
%{_desktopdir}/gupnp-network-light.desktop
%{_desktopdir}/gupnp-universal-cp.desktop
