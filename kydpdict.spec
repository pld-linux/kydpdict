Summary:	Fronted to Collins Dictionary
Summary(pl):	Interfejs do s³ownika Collinsa
Name:		kydpdict
Version:	0.5.6
Release:	4
License:	GPL
Group:		Applications/Dictionaries
Source0:	http://members.elysium.pl/ytm/src/%{name}-%{version}.tar.bz2
# Source0-md5:	8592bf17caa2128fcda38ae32ea2e66d
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-configure_in.patch
Patch1:		%{name}-info_about_commercial_component.patch
URL:		http://members.elysium.pl/ytm/html/kydpdict.html
BuildRequires:	autoconf >= 2.57
BuildRequires:	qt-devel >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6

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
%patch0 -p0
%patch1 -p0

%build
export QTDIR="%{_prefix}"
%{__aclocal}
%{__autoconf}
%configure \
	--with-qt-includes=%{_includedir}/qt
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Scientific} \
	$RPM_BUILD_ROOT%{_datadir}/kydpdict

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Scientific
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install	\
	prefix=$RPM_BUILD_ROOT%{_prefix}	\
	exec_prefix=$RPM_BUILD_ROOT%{_exec_prefix}	\
	bindir=$RPM_BUILD_ROOT%{_bindir}	\
	datadir=$RPM_BUILD_ROOT%{_datadir}
rm -fr $RPM_BUILD_ROOT%{_datadir}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Scientific/*
%{_pixmapsdir}/*
%{_datadir}/kydpdict
