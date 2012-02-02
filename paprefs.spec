Name:           paprefs
Version:        0.9.9
Release:        10%{?dist}.R
Summary:        Management tool for PulseAudio
Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://0pointer.de/lennart/projects/paprefs
Source0:        http://0pointer.de/lennart/projects/paprefs/paprefs-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       pulseaudio-module-gconf
Requires:	gnome-packagekit
BuildRequires:  gconfmm26-devel
BuildRequires:  libglademm24-devel 
BuildRequires:  lynx
BuildRequires:  desktop-file-utils
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  intltool
BuildRequires:	dbus-glib-devel

%description
PulseAudio Preferences (paprefs) is a simple GTK based configuration dialog
for the PulseAudio sound server.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    --vendor= \
    --remove-category Application \
    $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc LICENSE doc/README
%{_bindir}/paprefs
%dir %{_datadir}/paprefs
%{_datadir}/paprefs/paprefs.glade
%{_datadir}/applications/paprefs.desktop

%changelog
* Thu Feb  2 2012 Arkady L. Shane <ashejn@russianfedora.ru> - 0.9.9-10.R
- rebuilt for EL

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 16 2011 Michel Salim <salimma@fedoraproject.org> - 0.9.9-9
- Rebuild for pulseaudio 0.9.23 (F-16) / 1.1 (F-17)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 06 2011 Lubmir Rintel <lkundrak@v3.sk> 0.9.9-7
- Rebuild for pulseaudio-0.9.22

* Tue Feb 23 2010 Rex Dieter <rdieter@fedoraproject.org> 0.9.9-6
- Requires: PackageKit-session-service (#561437)

* Mon Oct 25 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.9-5
- Rebuild to make sure we look for /usr/lib/pulse-0.9.21/modules/xxx instead of /usr/lib/pulse-0.9.19/modules/xxx
- https://bugzilla.redhat.com/show_bug.cgi?id=528557

* Wed Oct 14 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.9-4
- Fix mistag

* Wed Oct 14 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.9-3
- Rebuild to make sure we look for /usr/lib/pulse-0.9.19/modules/xxx instead of /usr/lib/pulse-0.9.16/modules/xxx

* Thu Sep 10 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.9-2
- Final 0.9.9 release

* Tue Aug 25 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.9-1.git20090825
- Add dbus-glib to deps

* Tue Aug 25 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.9-0.git20090825
- Snapshot

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.8-1
- Update to 0.9.8

* Sun Mar 15 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.9.7-5
- Try harder when looking for modules

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 9 2008 Matthias Clasen <mclasen@redhat.com> 0.9.7-3
- Handle locales properly

* Tue Sep 9 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.7-2
- Include intltool in deps

* Tue Sep 9 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.7-1
- Update to 0.9.7

* Thu Aug 28 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.6-4
- Include unowned directory /usr/share/paprefs

* Thu Mar 27 2008 Christopher Aillon <caillon@redhat.com> - 0.9.6-3
- Add compile patch for GCC 4.3

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.6-2
- Autorebuild for GCC 4.3

* Wed Nov 28 2007 Julian Sikorski <belegdol[at]gmail[dot]com> 0.9.6-1
- Update to 0.9.6

* Thu Sep 25 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.6-0.2.svn20070925
- Update SVN snapshot

* Thu Aug 16 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.6-0.1.svn20070816
- Get snapshot from SVN

* Thu Jul 2 2007 Eric Moret <eric.moret@epita.fr> 0.9.5-2
- Update license field

* Wed Jan 10 2007 Eric Moret <eric.moret@epita.fr> 0.9.5-1
- Initial package for Fedora
