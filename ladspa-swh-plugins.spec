
%define		_name	swh-plugins

Summary:	A set of audio plugins for LADSPA
Summary(pl):	Zestaw wtyczek d¼wiêkowych dla LADSPA
Name:		ladspa-swh-plugins
Version:	0.4.2
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://plugin.org.uk/releases/%{version}/%{_name}-%{version}.tar.gz
# Source0-md5:	2b20f2f879ec225be78fc880787108ec
URL:		http://plugin.org.uk/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fftw-devel
BuildRequires:	ladspa-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%ifarch athlon
%define		_with_3dnow	1
%endif

%description
A set of audio plugins for LADSPA (see http://plugin.org.uk/ for more
details).

%description -l pl
Zestaw wtyczek d¼wiêkowych dla LADSPA (wiêcej informacji pod adresem
http://plugin.org.uk/).

%prep
%setup -q -n %{_name}-%{version}
cd gsm
mv README README.gsm

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	%{?_with_3dnow:--enable-3dnow}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{_name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO gsm/README.gsm
%attr(755,root,root) %{_libdir}/ladspa/*.so
%{_datadir}/ladspa/rdf/swh-*.rdf
