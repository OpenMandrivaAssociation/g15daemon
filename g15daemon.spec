%define libname %mklibname g15daemon_client 1
%define libname_devel %mklibname g15daemon_client -d

Name:                   g15daemon
Version:                1.9.5.3
Release:                11
Summary:                Daemon to control logitech G15 keyboards
License:                GPLv2+
Group:                  System/Servers
URL:                    http://g15daemon.sourceforge.net/
Source0:                http://downloads.sourceforge.net/g15daemon/g15daemon-%{version}.tar.bz2
Source1:                g15daemon.init
Patch0:                 %{name}-1.9.5.3-fix-open-with-O_CREAT.patch
Patch1:			g15daemon-1.9.5.3-recv-oob-answer.patch  

BuildRequires:          g15-devel
BuildRequires:          g15render-devel

Requires(post):     rpm-helper
Requires(preun):    rpm-helper

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
# just to have a happy linting..
Requires:       %{libname} = %{EVRD}

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
%patch1 -p1

%build
autoreconf -fi
%configure2_5x --disable-static
make

%install
%{makeinstall_std}
rm -r %{buildroot}%{_docdir}
mkdir -p %{buildroot}%{_initrddir}
cp -a %{SOURCE1} %{buildroot}%{_initrddir}/%{name}

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%files 
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog COPYING Documentation/README* FAQ LICENSE NEWS README* TODO contrib lang-bindings 
%defattr(-,root,root,0755)
%{_datadir}/g15daemon
%attr(0755,root,root) %{_initrddir}/%{name}
%{_libdir}/g15daemon
%{_mandir}/man1/*
%{_sbindir}/g15daemon

%files -n %{libname}
%doc AUTHORS ChangeLog COPYING Documentation/README* FAQ LICENSE NEWS README* TODO contrib lang-bindings
%{_libdir}/*.so.*

%files -n %{libname_devel}
%doc AUTHORS ChangeLog COPYING Documentation/README* FAQ LICENSE NEWS README* TODO contrib lang-bindings
%defattr(-,root,root,0755)
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/*


