%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Name:		quadrapassel
Version:	3.18.0
Release:	1
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
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
Obsoletes: gnome-games-quadrapassel < 1:3.7.92
# For help
Requires:	yelp

%description
The Russian game of falling geometric shapes.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml
%{_iconsdir}/*/*/apps/%{name}*.*
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/appdata/%{name}.appdata.xml


%changelog
* Tue Feb 17 2015 wally <wally> 3.14.0-3.mga5
+ Revision: 815345
- require yelp for showing help

* Wed Oct 15 2014 umeabot <umeabot> 3.14.0-2.mga5
+ Revision: 749627
- Second Mageia 5 Mass Rebuild

* Mon Sep 22 2014 ovitters <ovitters> 3.14.0-1.mga5
+ Revision: 719241
- new version 3.14.0

* Tue Sep 16 2014 umeabot <umeabot> 3.13.92-2.mga5
+ Revision: 688572
- Mageia 5 Mass Rebuild

* Tue Sep 16 2014 ovitters <ovitters> 3.13.92-1.mga5
+ Revision: 676936
- new version 3.13.92

* Mon Sep 01 2014 ovitters <ovitters> 3.13.91-1.mga5
+ Revision: 670764
- new version 3.13.91

* Tue Aug 19 2014 ovitters <ovitters> 3.13.90-1.mga5
+ Revision: 665310
- new version 3.13.90

* Mon Jul 21 2014 ovitters <ovitters> 3.13.4-1.mga5
+ Revision: 655294
- new version 3.13.4

* Thu May 29 2014 ovitters <ovitters> 3.13.1-1.mga5
+ Revision: 627589
- new version 3.13.1

* Mon May 12 2014 ovitters <ovitters> 3.12.2-1.mga5
+ Revision: 622281
- new version 3.12.2

* Mon Apr 14 2014 ovitters <ovitters> 3.12.1-1.mga5
+ Revision: 614228
- new version 3.12.1

* Sun Mar 23 2014 ovitters <ovitters> 3.12.0-1.mga5
+ Revision: 606977
- new version 3.12.0

* Tue Mar 18 2014 ovitters <ovitters> 3.11.92-1.mga5
+ Revision: 604653
- new version 3.11.92

* Mon Mar 03 2014 ovitters <ovitters> 3.11.91-1.mga5
+ Revision: 599037
- new version 3.11.91

* Mon Feb 17 2014 ovitters <ovitters> 3.11.90-1.mga5
+ Revision: 593859
- new version 3.11.90

* Wed Feb 05 2014 dams <dams> 3.11.5-1.mga5
+ Revision: 583040
- new version 3.11.5

* Wed Feb 05 2014 dams <dams> 3.11.4-1.mga5
+ Revision: 582962
- new version 3.11.4

* Mon Nov 11 2013 ovitters <ovitters> 3.10.2-1.mga4
+ Revision: 550452
- new version 3.10.2

* Sat Nov 09 2013 ovitters <ovitters> 3.10.0-3.mga4
+ Revision: 550198
- fix url

* Sat Oct 19 2013 umeabot <umeabot> 3.10.0-2.mga4
+ Revision: 536049
- Mageia 4 Mass Rebuild

* Sat Sep 21 2013 ovitters <ovitters> 3.10.0-1.mga4
+ Revision: 483089
- new version 3.10.0

* Tue Sep 17 2013 ovitters <ovitters> 3.9.92-1.mga4
+ Revision: 480479
- new version 3.9.92

* Sun Sep 01 2013 ovitters <ovitters> 3.9.91-1.mga4
+ Revision: 474123
- new version 3.9.91

* Sun Aug 18 2013 ovitters <ovitters> 3.9.90-1.mga4
+ Revision: 467521
- new version 3.9.90

* Tue Jul 30 2013 dams <dams> 3.9.5-1.mga4
+ Revision: 460791
- new version 3.9.5

* Sun Jul 28 2013 ovitters <ovitters> 3.8.2-1.mga4
+ Revision: 459754
- new version 3.8.2

  + fwang <fwang>
    - cleanup spec

* Sun Jun 09 2013 dams <dams> 3.8.1-1.mga4
+ Revision: 440928
- imported package quadrapassel

