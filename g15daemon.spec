%define _disable_lto 1
%define _disable_ld_no_undefined 1

%define libname %mklibname g15daemon_client 1
%define libname_devel %mklibname g15daemon_client -d

Name:                   g15daemon
Version:                1.9.5.3
Release:                12
Summary:                Daemon to control logitech G15 keyboards
License:                GPLv2+
Group:                  System/Servers
URL:                    http://g15daemon.sourceforge.net/
Source0:                http://downloads.sourceforge.net/g15daemon/g15daemon-%{version}.tar.bz2
Source1:                g15daemon.service
Patch0:                 %{name}-1.9.5.3-fix-open-with-O_CREAT.patch
Requires(post):         rpm-helper
Requires(preun):        rpm-helper
BuildRequires:          g15-devel
BuildRequires:          g15render-devel
Requires(post): 	systemd-units
Requires(preun): 	systemd-units
Requires(postun): 	systemd-units

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
%configure --disable-static
%make_build

%install
%make_install
rm -r %{buildroot}%{_docdir}

install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/g15daemon.service

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files 
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog COPYING Documentation/README* FAQ INSTALL LICENSE NEWS README* TODO contrib lang-bindings 
%defattr(-,root,root,0755)
%{_datadir}/g15daemon
%{_unitdir}/g15daemon.service
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
