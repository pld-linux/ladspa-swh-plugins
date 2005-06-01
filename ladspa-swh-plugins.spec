#
# Conditional build:
%bcond_with	3dnow	# enables use of 3DNow! instructions
%bcond_with	sse	# enables use of SSE instructions
#
%define		_name	swh-plugins
#
Summary:	A set of LADSPA audio plugins
Summary(pl):	Zestaw wtyczek d¼wiêkowych LADSPA
Name:		ladspa-swh-plugins
Version:	0.4.13
Release:	2
License:	GPL
Group:		Applications/Sound
Source0:	http://plugin.org.uk/releases/%{version}/%{_name}-%{version}.tar.gz
# Source0-md5:	83fc4f1ec9e6c7e0632b1b1d95717060
Patch0:		%{name}-use_our_optflags.patch
Patch1:		%{name}-shared-gsm.patch
URL:		http://plugin.org.uk/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fftw3-single-devel
BuildRequires:	gettext-devel
BuildRequires:	ladspa-devel
BuildRequires:	libgsm-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	ladspa-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%ifarch athlon
%define		with_3dnow	1
%endif

%description
A set of LADSPA audio plugins (see http://plugin.org.uk/ for more
details).

%description -l pl
Zestaw wtyczek d¼wiêkowych LADSPA (wiêcej informacji pod adresem
http://plugin.org.uk/).

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1
%patch1 -p1

sed -i -e 's:/lib/ladspa:/%{_lib}/ladspa:' Makefile.am

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	%{?with_3dnow:--enable-3dnow} \
	%{?with_sse:--enable-sse}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#%find_lang %{_name}

%clean
rm -rf $RPM_BUILD_ROOT

#%files -f %{_name}.lang
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/ladspa/*.so
%{_datadir}/ladspa/rdf/swh-*.rdf
