Summary:	Frontend to Collins Dictionary
Summary(pl):	Interfejs do s³ownika Collinsa
Name:		kydpdict
Version:	0.5.8
Release:	2
License:	GPL
Group:		Applications/Dictionaries
Source0:	http://members.elysium.pl/ytm/src/%{name}-%{version}.tar.bz2
# Source0-md5:	8089700f3485f33991fec1ac4b7d159c
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-home_etc.patch
URL:		http://members.elysium.pl/ytm/html/kydpdict.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	qt-devel >= 3.1.0
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
%patch0 -p1

%build
%{__aclocal} --acdir=config
%{__autoconf}
%configure \
	--with-qt-includes=%{_includedir}/qt \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Scientific} \
	$RPM_BUILD_ROOT%{_datadir}/kydpdict

install src/kydpdict $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Scientific
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install src/kydpdict_pl.qm $RPM_BUILD_ROOT%{_datadir}/kydpdict
install src/tips.html $RPM_BUILD_ROOT%{_datadir}/kydpdict

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Scientific/*
%{_pixmapsdir}/*
%{_datadir}/kydpdict
