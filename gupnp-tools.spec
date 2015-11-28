Summary:	GUPnP Tools
Summary(pl.UTF-8):	Narzędzia GUPnP
Name:		gupnp-tools
Version:	0.8.11
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gupnp-tools/0.8/%{name}-%{version}.tar.xz
# Source0-md5:	d265a1728163e23072a98a18a00eb1a6
Patch0:		%{name}-desktop.patch
URL:		http://gupnp.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.24
BuildRequires:	gssdp-devel >= 0.14
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	gtksourceview3-devel >= 3.2.0
BuildRequires:	gupnp-av-devel >= 0.5.5
BuildRequires:	gupnp-devel >= 0.20.14
BuildRequires:	intltool >= 0.40.6
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	adwaita-icon-theme
Requires:	glib2 >= 1:2.24
Requires:	gssdp >= 0.14
Requires:	gtk+3 >= 3.10.0
Requires:	gtksourceview3 >= 3.2.0
Requires:	gupnp-av >= 0.5.5
Requires:	gupnp >= 0.20.14
Requires:	libsoup >= 2.4
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

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gssdp-discover
%attr(755,root,root) %{_bindir}/gupnp-av-cp
%attr(755,root,root) %{_bindir}/gupnp-network-light
%attr(755,root,root) %{_bindir}/gupnp-universal-cp
%attr(755,root,root) %{_bindir}/gupnp-upload
%{_datadir}/gupnp-tools
%{_desktopdir}/gupnp-av-cp.desktop
%{_desktopdir}/gupnp-network-light.desktop
%{_desktopdir}/gupnp-universal-cp.desktop
