%define tarball xf86-video-v4l
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

Summary:   Xorg X11 v4l video driver
Name:      xorg-x11-drv-v4l
Version:   0.2.0
Release:   3%{?dist}.3
URL:       http://www.x.org
License:   MIT
Group:     User Interface/X Hardware Support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2

ExcludeArch: s390 s390x

BuildRequires: xorg-x11-server-sdk >= 1.3.0.0-6

Requires:  xorg-x11-server-Xorg >= 1.3.0.0-6

%description 
X.Org X11 v4l video driver.

%prep
%setup -q -n %{tarball}-%{version}

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/v4l_drv.so
%{_mandir}/man4/v4l.4*

%changelog
* Thu Feb 18 2010 Dennis Gregorovic <dgregor@redhat.com> - 0.2.0-3.3
- Rebuilt for RHEL 6
- Related: rhbz#566527

* Wed Sep 02 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.2.0-3.2
- Rebuilt for RHEL 6

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 0.2.0-2.1
- ABI bump

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 20 2008 Dave Airlie <airlied@redhat.com> 0.2.0-1
- Latest upstream release

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.1.1-9
- Autorebuild for GCC 4.3

* Tue Aug 28 2007 Adam Jackson <ajax@redhat.com> 0.1.1-8
- Fix ioctl argument on LP64 machines. (#250070)

* Thu Aug 23 2007 Adam Jackson <ajax@redhat.com> - 0.1.1-7
- Rebuild for ppc toolchain bug

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 0.1.1-6
- Update Requires and BuildRequires.  Disown the module directories.

* Fri Feb 16 2007 Adam Jackson <ajax@redhat.com> 0.1.1-5
- ExclusiveArch -> ExcludeArch

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.1.1-4
- rebuild

* Tue May 23 2006 Adam Jackson <ajackson@redhat.com> 0.1.1-3
- Rebuild for 7.1 ABI fix.

* Fri May 19 2006 Mike A. Harris <mharris@redhat.com> 0.1.1-2
- Added "BuildRequires: xorg-x11-proto-devel" for (#192386)

* Sun Apr  9 2006 Adam Jackson <ajackson@redhat.com> 0.1.1-1
- Update to 0.1.1 from 7.1RC1.

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 0.0.1.5-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 0.0.1.5-1
- Updated xorg-x11-drv-v4l to version 0.0.1.5 from X11R7.0

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 0.0.1.4-1
- Updated xorg-x11-drv-v4l to version 0.0.1.4 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Fri Nov 4 2005 Mike A. Harris <mharris@redhat.com> 0.0.1.1-1
- Updated xorg-x11-drv-v4l to version 0.0.1.1 from X11R7 RC1.  For some
  unknown reason, the version went backwards from 4.0.0 to 0.0.1.1.
- Fix *.la file removal.

* Mon Oct 3 2005 Mike A. Harris <mharris@redhat.com> 4.0.0-1
- Initial spec file for v4l video driver forked from cirrus driver package.
