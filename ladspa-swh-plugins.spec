#
# Conditional build:
# _with_3dnow		- enables use of 3DNow! instrucions
# _with_sse		- enables use of SSE instructions
#

%define		_name	swh-plugins

Summary:	A set of audio plugins for LADSPA
Summary(pl):	Zestaw wtyczek d¼wiêkowych dla LADSPA
Name:		ladspa-swh-plugins
Version:	0.4.2
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://plugin.org.uk/releases/%{version}/%{_name}-%{version}.tar.gz
# Source0-md5:	2b20f2f879ec225be78fc880787108ec
Patch0:		%{name}-use_our_optflags.patch
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
%patch0 -p1
cd gsm
mv README README.gsm

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	%{?_with_3dnow:--enable-3dnow} \
	%{?_with_sse:--enable-sse}

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
