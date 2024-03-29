%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Name:		quadrapassel
Version:	40.2
Release:	5
Summary:	GNOME Quadrapassel game
License:	GPLv2+ and CC-BY-SA
Group:		Games/Arcade
URL:		https://wiki.gnome.org/Quadrapassel
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(clutter-1.0) >= 1.0.0
BuildRequires:	pkgconfig(clutter-gtk-1.0) >= 1.0.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:	pkgconfig(libcanberra-gtk3) >= 0.26
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:  librsvg-vala-devel
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(manette-0.2)
BuildRequires:  cmake
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:  meson
BuildRequires:  vala
Obsoletes: gnome-games-quadrapassel < 1:3.7.92
# For help
Requires:	yelp

%description
The Russian game of falling geometric shapes.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Quadrapassel.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Quadrapassel.gschema.xml
%{_iconsdir}/*/*/apps/org.gnome.Quadrapassel*.*
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/metainfo/org.gnome.Quadrapassel.appdata.xml

