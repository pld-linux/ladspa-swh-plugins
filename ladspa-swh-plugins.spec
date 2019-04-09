#
# Conditional build:
%bcond_with	3dnow	# enables use of 3DNow! instructions
%bcond_with	sse	# enables use of SSE instructions
#
Summary:	A set of LADSPA audio plugins
Summary(pl.UTF-8):	Zestaw wtyczek dźwiękowych LADSPA
Name:		ladspa-swh-plugins
Version:	0.4.17
Release:	1
License:	GPL
Group:		Applications/Sound
#Source0Download: https://github.com/swh/ladspa/releases
Source0:	https://github.com/swh/ladspa/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8c036a21c13215841ad53199b4a92b1a
Patch0:		%{name}-use_our_optflags.patch
Patch1:		%{name}-shared-gsm.patch
URL:		http://plugin.org.uk/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	fftw3-single-devel >= 3.0
BuildRequires:	gettext-tools >= 0.19.3
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

%description -l pl.UTF-8
Zestaw wtyczek dźwiękowych LADSPA (więcej informacji pod adresem
http://plugin.org.uk/).

%prep
%setup -q -n ladspa-%{version}
%patch0 -p1
%patch1 -p1

%{__sed} -i -e 's:/lib/ladspa:/%{_lib}/ladspa:' Makefile.am
%{__sed} -i -e '/^po\/Makefile.in$/d' configure.ac

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_3dnow:--enable-3dnow} \
	%{?with_sse:--enable-sse}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# only empty en_GB locale exists
#%find_lang swh-plugins

%clean
rm -rf $RPM_BUILD_ROOT

#%files -f swh-plugins.lang
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/ladspa/alias_1407.so
%attr(755,root,root) %{_libdir}/ladspa/allpass_1895.so
%attr(755,root,root) %{_libdir}/ladspa/am_pitchshift_1433.so
%attr(755,root,root) %{_libdir}/ladspa/amp_1181.so
%attr(755,root,root) %{_libdir}/ladspa/analogue_osc_1416.so
%attr(755,root,root) %{_libdir}/ladspa/bandpass_a_iir_1893.so
%attr(755,root,root) %{_libdir}/ladspa/bandpass_iir_1892.so
%attr(755,root,root) %{_libdir}/ladspa/bode_shifter_1431.so
%attr(755,root,root) %{_libdir}/ladspa/bode_shifter_cv_1432.so
%attr(755,root,root) %{_libdir}/ladspa/butterworth_1902.so
%attr(755,root,root) %{_libdir}/ladspa/chebstortion_1430.so
%attr(755,root,root) %{_libdir}/ladspa/comb_1190.so
%attr(755,root,root) %{_libdir}/ladspa/comb_1887.so
%attr(755,root,root) %{_libdir}/ladspa/comb_splitter_1411.so
%attr(755,root,root) %{_libdir}/ladspa/const_1909.so
%attr(755,root,root) %{_libdir}/ladspa/crossover_dist_1404.so
%attr(755,root,root) %{_libdir}/ladspa/dc_remove_1207.so
%attr(755,root,root) %{_libdir}/ladspa/decay_1886.so
%attr(755,root,root) %{_libdir}/ladspa/decimator_1202.so
%attr(755,root,root) %{_libdir}/ladspa/declip_1195.so
%attr(755,root,root) %{_libdir}/ladspa/delay_1898.so
%attr(755,root,root) %{_libdir}/ladspa/delayorama_1402.so
%attr(755,root,root) %{_libdir}/ladspa/diode_1185.so
%attr(755,root,root) %{_libdir}/ladspa/divider_1186.so
%attr(755,root,root) %{_libdir}/ladspa/dj_eq_1901.so
%attr(755,root,root) %{_libdir}/ladspa/dj_flanger_1438.so
%attr(755,root,root) %{_libdir}/ladspa/dyson_compress_1403.so
%attr(755,root,root) %{_libdir}/ladspa/fad_delay_1192.so
%attr(755,root,root) %{_libdir}/ladspa/fast_lookahead_limiter_1913.so
%attr(755,root,root) %{_libdir}/ladspa/flanger_1191.so
%attr(755,root,root) %{_libdir}/ladspa/fm_osc_1415.so
%attr(755,root,root) %{_libdir}/ladspa/foldover_1213.so
%attr(755,root,root) %{_libdir}/ladspa/foverdrive_1196.so
%attr(755,root,root) %{_libdir}/ladspa/freq_tracker_1418.so
%attr(755,root,root) %{_libdir}/ladspa/gate_1410.so
%attr(755,root,root) %{_libdir}/ladspa/giant_flange_1437.so
%attr(755,root,root) %{_libdir}/ladspa/gong_1424.so
%attr(755,root,root) %{_libdir}/ladspa/gong_beater_1439.so
%attr(755,root,root) %{_libdir}/ladspa/gsm_1215.so
%attr(755,root,root) %{_libdir}/ladspa/gverb_1216.so
%attr(755,root,root) %{_libdir}/ladspa/hard_limiter_1413.so
%attr(755,root,root) %{_libdir}/ladspa/harmonic_gen_1220.so
%attr(755,root,root) %{_libdir}/ladspa/hermes_filter_1200.so
%attr(755,root,root) %{_libdir}/ladspa/highpass_iir_1890.so
%attr(755,root,root) %{_libdir}/ladspa/hilbert_1440.so
%attr(755,root,root) %{_libdir}/ladspa/imp_1199.so
%attr(755,root,root) %{_libdir}/ladspa/impulse_1885.so
%attr(755,root,root) %{_libdir}/ladspa/inv_1429.so
%attr(755,root,root) %{_libdir}/ladspa/karaoke_1409.so
%attr(755,root,root) %{_libdir}/ladspa/latency_1914.so
%attr(755,root,root) %{_libdir}/ladspa/lcr_delay_1436.so
%attr(755,root,root) %{_libdir}/ladspa/lowpass_iir_1891.so
%attr(755,root,root) %{_libdir}/ladspa/ls_filter_1908.so
%attr(755,root,root) %{_libdir}/ladspa/matrix_ms_st_1421.so
%attr(755,root,root) %{_libdir}/ladspa/matrix_spatialiser_1422.so
%attr(755,root,root) %{_libdir}/ladspa/matrix_st_ms_1420.so
%attr(755,root,root) %{_libdir}/ladspa/mbeq_1197.so
%attr(755,root,root) %{_libdir}/ladspa/mod_delay_1419.so
%attr(755,root,root) %{_libdir}/ladspa/multivoice_chorus_1201.so
%attr(755,root,root) %{_libdir}/ladspa/notch_iir_1894.so
%attr(755,root,root) %{_libdir}/ladspa/phasers_1217.so
%attr(755,root,root) %{_libdir}/ladspa/pitch_scale_1193.so
%attr(755,root,root) %{_libdir}/ladspa/pitch_scale_1194.so
%attr(755,root,root) %{_libdir}/ladspa/plate_1423.so
%attr(755,root,root) %{_libdir}/ladspa/pointer_cast_1910.so
%attr(755,root,root) %{_libdir}/ladspa/rate_shifter_1417.so
%attr(755,root,root) %{_libdir}/ladspa/retro_flange_1208.so
%attr(755,root,root) %{_libdir}/ladspa/revdelay_1605.so
%attr(755,root,root) %{_libdir}/ladspa/ringmod_1188.so
%attr(755,root,root) %{_libdir}/ladspa/satan_maximiser_1408.so
%attr(755,root,root) %{_libdir}/ladspa/sc1_1425.so
%attr(755,root,root) %{_libdir}/ladspa/sc2_1426.so
%attr(755,root,root) %{_libdir}/ladspa/sc3_1427.so
%attr(755,root,root) %{_libdir}/ladspa/sc4_1882.so
%attr(755,root,root) %{_libdir}/ladspa/sc4m_1916.so
%attr(755,root,root) %{_libdir}/ladspa/se4_1883.so
%attr(755,root,root) %{_libdir}/ladspa/shaper_1187.so
%attr(755,root,root) %{_libdir}/ladspa/sifter_1210.so
%attr(755,root,root) %{_libdir}/ladspa/sin_cos_1881.so
%attr(755,root,root) %{_libdir}/ladspa/single_para_1203.so
%attr(755,root,root) %{_libdir}/ladspa/sinus_wavewrapper_1198.so
%attr(755,root,root) %{_libdir}/ladspa/smooth_decimate_1414.so
%attr(755,root,root) %{_libdir}/ladspa/split_1406.so
%attr(755,root,root) %{_libdir}/ladspa/step_muxer_1212.so
%attr(755,root,root) %{_libdir}/ladspa/surround_encoder_1401.so
%attr(755,root,root) %{_libdir}/ladspa/svf_1214.so
%attr(755,root,root) %{_libdir}/ladspa/tape_delay_1211.so
%attr(755,root,root) %{_libdir}/ladspa/transient_1206.so
%attr(755,root,root) %{_libdir}/ladspa/triple_para_1204.so
%attr(755,root,root) %{_libdir}/ladspa/valve_1209.so
%attr(755,root,root) %{_libdir}/ladspa/valve_rect_1405.so
%attr(755,root,root) %{_libdir}/ladspa/vocoder_1337.so
%attr(755,root,root) %{_libdir}/ladspa/vynil_1905.so
%attr(755,root,root) %{_libdir}/ladspa/wave_terrain_1412.so
%attr(755,root,root) %{_libdir}/ladspa/xfade_1915.so
%attr(755,root,root) %{_libdir}/ladspa/zm1_1428.so
%{_datadir}/ladspa/rdf/swh-*.rdf
