Summary:	Frontend to Collins Dictionary
Summary(pl):	Interfejs do s³ownika Collinsa
Name:		kydpdict
Version:	0.9.0
Release:	1
License:	GPL
Group:		Applications/Dictionaries
Source0:	http://members.elysium.pl/ytm/src/%{name}-%{version}.tar.bz2
# Source0-md5:	8cc5b93c43d7d87f1051840354ef8088
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://members.elysium.pl/ytm/html/kydpdict.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	qt-devel >= 3.3.2-5
BuildRequires:	qt-linguist >= 3.3.2-5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kydpdict is a graphical (Qt) frontend for various free and commercial
dictionaries available for Windows. Contrary to its name this software
doesn't depend on KDE environment. Since version 0.9.0 it also isn't
limited to YDP dictionaries, but can use others (like SAP).

%description -l pl
Program Kydpdict jest graficzn± (Qt) nak³adk± pozwalaj±c± na ³atwe i
efektywne korzystanie w ¶rodowisku graficznym z ró¿nych darmowych i
komercyjnych s³owników dostêpnych pod Windows. Wbrew swojej nazwie nie
jest programem zale¿nym od ¶rodowiska KDE. Od wersji 0.9.0 równie¿ wbrew
swojej nazwie nie jest li tylko nak³adk± na s³ownik YDP.

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
