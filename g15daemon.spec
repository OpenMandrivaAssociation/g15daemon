%define libname %mklibname g15daemon_client 1
%define libname_devel %mklibname g15daemon_client -d

Name:                   g15daemon
Version:                1.9.5.3
Release:                8
Summary:                Daemon to control logitech G15 keyboards
License:                GPLv2+
Group:                  System/Servers
URL:                    http://g15daemon.sourceforge.net/
Source0:                http://downloads.sourceforge.net/g15daemon/g15daemon-%{version}.tar.bz2
Source1:                g15daemon.init
Patch0:                 %{name}-1.9.5.3-fix-open-with-O_CREAT.patch
Requires(post):         rpm-helper
Requires(preun):        rpm-helper
BuildRequires:          g15-devel
BuildRequires:          g15render-devel

%description
G15daemon controls the G15 keyboard, allowing the use of 
all keys through the linux kernel uinput device driver.  
It also controls the use of the keyboard's LCD display, 
allows multiple, simultaneous client applications to connect, 
and gives the user the ability to switch between client 
apps at the press of a button.

%package -n %{libname}
Summary:        Daemon to control logitech G15 keyboards
Group:          System/Libraries
Provides:       g15daemon_client = %{EVRD}
Requires:       %{name} >= %{version}

%description -n %{libname}
G15daemon controls the G15 keyboard, allowing the use of
all keys through the linux kernel uinput device driver.
It also controls the use of the keyboard's LCD display,
allows multiple, simultaneous client applications to connect,
and gives the user the ability to switch between client
apps at the press of a button.

%package -n %{libname_devel}
Summary:        Daemon to control logitech G15 keyboards
Group:          Development/C
Provides:       g15daemon_client-devel = %{EVRD}
Requires:       g15daemon_client = %{version}

%description -n %{libname_devel}
G15daemon controls the G15 keyboard, allowing the use of
all keys through the linux kernel uinput device driver.
It also controls the use of the keyboard's LCD display,
allows multiple, simultaneous client applications to connect,
and gives the user the ability to switch between client
apps at the press of a button.

%prep
%setup -q
%patch0 -p1 -b .ocreat

%build
%configure2_5x --disable-static
%make

%install
%{makeinstall_std}
%{__rm} -r %{buildroot}%{_docdir}
%{__mkdir_p} %{buildroot}%{_initrddir}
%{__cp} -a %{SOURCE1} %{buildroot}%{_initrddir}/%{name}

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%files 
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog COPYING Documentation/README* FAQ INSTALL LICENSE NEWS README* TODO contrib lang-bindings 
%defattr(-,root,root,0755)
%{_datadir}/g15daemon
%attr(0755,root,root) %{_initrddir}/%{name}
%{_libdir}/g15daemon
%{_mandir}/man1/*
%{_sbindir}/g15daemon

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{libname_devel}
%defattr(-,root,root,0755)
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/*


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9.5.3-7mdv2011.0
+ Revision: 610782
- rebuild

* Fri Jan 08 2010 Götz Waschk <waschk@mandriva.org> 1.9.5.3-6mdv2010.1
+ Revision: 487511
- the library depends on the daemon to make the clients work

* Mon Sep 14 2009 Götz Waschk <waschk@mandriva.org> 1.9.5.3-5mdv2010.0
+ Revision: 439655
- rebuild for new libusb

* Sun May 24 2009 Jérôme Brenier <incubusss@mandriva.org> 1.9.5.3-4mdv2010.0
+ Revision: 379121
- fix build (open with O_CREAT error)
- fix license (GPLv2+)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat Feb 16 2008 David Walluck <walluck@mandriva.org> 1.9.5.3-1mdv2008.1
+ Revision: 169218
- 1.9.5.3

* Fri Feb 08 2008 David Walluck <walluck@mandriva.org> 1.9.5.2-1mdv2008.1
+ Revision: 163918
- fix URL
- fix Provides and Requires
- add Requires on rpm-helper
- add reload entry to initscript
- import g15daemon


