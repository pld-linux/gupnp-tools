Summary:	GUPnP Tools
Summary(pl.UTF-8):	Narzędzia GUPnP
Name:		gupnp-tools
Version:	0.8.3
Release:	1
License:	GPL v2+
Group:		X11/Applications
#Source0Download: http://gupnp.org/download
Source0:	http://gupnp.org/sites/all/files/sources/%{name}-%{version}.tar.gz
# Source0-md5:	9d0c554629211d38252057d827355317
Patch0:		%{name}-configure.patch
Patch1:		%{name}-desktop.patch
URL:		http://gupnp.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.18.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gupnp-av-devel >= 0.5.5
BuildRequires:	gupnp-devel >= 0.13
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.18.0
Requires:	gnome-icon-theme >= 2.20
Requires:	gtk+3 >= 3.0.0
Requires:	gupnp-av >= 0.5.5
Requires:	gupnp >= 0.13
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
  status. It also provides a simple UI to control all the network
  lights available on the network.

- AV Control Point: a simple media player UI that enables one to
  discover and play multimedia contents available on a network.

- Upload: a simple commandline utility that uploads files to known
  MediaServers. Use Universal Control Point for discovering the
  MediaServers.

%description -l pl.UTF-8
Narzędzia GUPnP to wolnodostępne zamienniki narzędzi UPnP Intela
wykorzystujące GUPnP. Udostępniają następujące narzędzia klienckie i
serwerowe, pozwalające łatwo diagnozować urządzenia i punkty kontrolne
UPnP:

- Universal Control Point (uniwersalny punkt kontrolny) - narzędzie
  pozwalające wykrywać urządzenia i usługi UPnP, odczytywać informacje
  o nich, pobierać zdarzenia i wywoływać akcje.

- Network Light (światło sieciowe) - wirtualna żarówka pozwalająca
  punktom kontrolnym na włączanie i wyłączanie, zmianę poziomu
  oświetlenia oraz sprawdzanie aktualnego stanu. Udostępnia także
  prosty interfejs użytkownika do sterowania światłami sieciowymi
  dostępnymi w sieci.

- AV Control Point (punkt kontrolny AV) - prosty interfejs użytkownika
  odtwarzacza multimedialnego pozwalający wykrywać i odtwarzać treści
  multimedialne dostępne w sieci.

- Upload - proste narzędzie działające z linii poleceń przesyłające
  pliki na znane serwery multimediów (MediaServers). Serwery można
  zlokalizować przy użyciu uniwersalnego punktu kontrolnego.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
