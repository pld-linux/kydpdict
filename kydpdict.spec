Summary:	Frontend to Collins Dictionary
Summary(pl.UTF-8):	Interfejs do słownika Collinsa
Name:		kydpdict
Version:	0.9.3
Release:	1
License:	GPL
Group:		Applications/Dictionaries
Source0:	http://members.elysium.pl/ytm/src/%{name}-%{version}.tar.bz2
# Source0-md5:	1bfb4a075bceb79527d9ca324f4b2445
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://members.elysium.pl/ytm/html/kydpdict.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	qt-devel >= 6:3.3.2-5
BuildRequires:	qt-linguist >= 3.3.2-5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kydpdict is a graphical (Qt) frontend for various free and commercial
dictionaries available for Windows. Contrary to its name this software
doesn't depend on KDE environment. Since version 0.9.0 it also isn't
limited to YDP dictionaries, but can use others (like SAP).

%description -l pl.UTF-8
Program Kydpdict jest graficzną (Qt) nakładką pozwalającą na łatwe i
efektywne korzystanie w środowisku graficznym z różnych darmowych i
komercyjnych słowników dostępnych pod Windows. Wbrew swojej nazwie nie
jest programem zależnym od środowiska KDE. Od wersji 0.9.0 również wbrew
swojej nazwie nie jest li tylko nakładką na słownik YDP.

%prep
%setup -q

%{__perl} -pi -e 's/-lqt3 -lqt2 -lqt -lqt-mt/-lqt-mt/' config/qt.m4

%build
%{__aclocal} --acdir=config
%{__autoconf}
%configure \
	--with-qt-includes=%{_includedir}/qt \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_datadir}/kydpdict
