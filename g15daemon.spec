%define libname %mklibname g15daemon_client 1
%define libname_devel %mklibname g15daemon_client -d
%define libname_static_devel %mklibname g15daemon_client -d -s

Name:                   g15daemon
Version:                1.9.5.2
Release:                %mkrel 1
Summary:                Daemon to control logitech G15 keyboards
License:                GPL
Group:                  System/Servers
URL:                    http://g15daemon.sourceforge.net/
Source0:                http://downloads.sourceforge.net/g15daemon-%{version}.tar.bz2
Source1:                g15daemon.init
Requires(post):         rpm-helper
Requires(preun):        rpm-helper
BuildRequires:          g15-devel
BuildRequires:          g15render-devel
BuildRoot:              %{_tmppath}/%{name}-%{version}-%{release}-root

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
Provides:       g15daemon_client = %{version}-%{release}

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
Provides:       g15daemon_client-devel = %{version}-%{release}
Requires:       g15daemon_client = %{version}-%{release}

%description -n %{libname_devel}
G15daemon controls the G15 keyboard, allowing the use of
all keys through the linux kernel uinput device driver.
It also controls the use of the keyboard's LCD display,
allows multiple, simultaneous client applications to connect,
and gives the user the ability to switch between client
apps at the press of a button.

%package -n %{libname_static_devel}
Summary:        Daemon to control logitech G15 keyboards
Group:          Development/C
Provides:       g15daemon_client-static-devel = %{version}-%{release}
Requires:       g15daemon_client-devel = %{version}-%{release}

%description -n %{libname_static_devel}
G15daemon controls the G15 keyboard, allowing the use of
all keys through the linux kernel uinput device driver.
It also controls the use of the keyboard's LCD display,
allows multiple, simultaneous client applications to connect,
and gives the user the ability to switch between client
apps at the press of a button.

%prep
%setup -q

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{__rm} -r %{buildroot}%{_docdir}
%{__rm} %{buildroot}%{_libdir}/g15daemon/%{version}/plugins/*.a %{buildroot}%{_libdir}/g15daemon/%{version}/plugins/*.la

%{__mkdir_p} %{buildroot}%{_initrddir}
%{__cp} -a %{SOURCE1} %{buildroot}%{_initrddir}/%{name}

%clean
%{__rm} -rf %{buildroot}

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

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
%{_libdir}/*.la
%{_libdir}/*.so
%{_mandir}/man3/*

%files -n %{libname_static_devel}
%defattr(-,root,root,0755)
%{_libdir}/*.a
