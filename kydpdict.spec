Summary:	Frontend to Collins Dictionary
Summary(pl):	Interfejs do s³ownika Collinsa
Name:		kydpdict
Version:	0.6.6
Release:	1
License:	GPL
Group:		Applications/Dictionaries
Source0:	http://members.elysium.pl/ytm/src/%{name}-%{version}.tar.bz2
# Source0-md5:	081361ebfb36475e126ec7c481047ab1
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://members.elysium.pl/ytm/html/kydpdict.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	qt-devel >= 3.3.2-5
BuildRequires:	qt-linguist >= 3.3.2-5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kydpdict is a Qt frontend for Collins dictionaries released by Young
Digital Poland. There are English-Polish, Polish-English,
German-Polish and Polish-German dictionaries available.

%description -l pl
Kydpdict to interface do s³owników Collinsa wydanych przez Young
Digital Poland. Dostêpne s± s³owniki: angielsko-polski,
polsko-angielski, niemiecko-polski i polsko-niemiecki.

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
