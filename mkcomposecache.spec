Summary:	Used for creating global (system-wide) Compose cache files
Name:		mkcomposecache
Version:	1.2.2
Release:	2
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
# For building mkcomposecache itself
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xorg-macros)

# For generating the caches
BuildRequires:	x11-server-xvfb
BuildRequires:	xbiff
BuildRequires:	libx11-common
# We need all glibc locales too, to generate the list of requirements after a glibc update,
# echo -ne "BuildRequires:\t"; dnf list |grep ^locales- |grep -v i686 |cut -d. -f1 |tr '\n' ' '; echo
BuildRequires:	locales-af locales-ar locales-cs locales-da locales-de locales-en locales-es locales-fr locales-he locales-hi locales-hu locales-id locales-it locales-ja locales-ko locales-nl locales-no locales-pl locales-pt locales-ro locales-ru locales-tr locales-uk locales-zh locales-aa locales-agr locales-ak locales-am locales-anp locales-as locales-ast locales-ayc locales-az locales-be locales-bem locales-ber locales-bg locales-bhb locales-bho locales-bi locales-bn locales-bo locales-br locales-bs locales-ca locales-ce locales-chr locales-crh locales-cv locales-cy locales-doi locales-dsb locales-dv locales-dz locales-el locales-eo locales-et locales-eu locales-fa locales-ff locales-fi locales-fo locales-fur locales-fy locales-ga locales-gd locales-gl locales-gu locales-gv locales-ha locales-hif locales-hne locales-hr locales-hsb locales-ht locales-hy locales-ia locales-ig locales-ik locales-is locales-iu locales-ka locales-kab locales-kk locales-kl locales-km locales-kn locales-kok locales-ks locales-ku locales-kw locales-ky locales-lb locales-lg locales-li locales-lij locales-ln locales-lo locales-lt locales-lv locales-mag locales-mai locales-mfe locales-mg locales-mhr locales-mi locales-miq locales-mjw locales-mk locales-ml locales-mn locales-mni locales-mr locales-ms locales-mt locales-my locales-nds locales-ne locales-nhn locales-niu locales-nr locales-nso locales-oc locales-or locales-os locales-pa locales-pap locales-ps locales-quz locales-raj locales-rw locales-sa locales-sah locales-sat locales-sc locales-sd locales-se locales-sgs locales-shn locales-shs locales-si locales-sk locales-sl locales-sm locales-so locales-sq locales-sr locales-ss locales-st locales-sv locales-sw locales-szl locales-ta locales-tcy locales-te locales-tg locales-th locales-the locales-tk locales-tl locales-tn locales-to locales-tpi locales-ts locales-tt locales-ug locales-unm locales-ur locales-uz locales-ve locales-vi locales-wa locales-wae locales-wo locales-xh locales-yi locales-yo locales-yue locales-yuw locales-zu

%description
mkcomposecache is used for creating global (system-wide) Compose cache files.

Compose cache files help with application startup times and memory usage,
especially in locales with large Compose tables (e.g. all UTF-8 locales).

The tool only makes sense with libX11 1.0.2 and higher.
Included is a script mkallcomposecaches.sh that creates global cache
files for all supported locales.

%package -n x11-compose-cache
Summary:	Binary cache files for libX11 Compose files
Group:		System/X11
BuildArch:	noarch

%description -n x11-compose-cache
mkcomposecache is used for creating X11 global (system-wide) Compose cache files.

%prep
%autosetup -p1

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}
%make_build

%install
%make_install

# Generate compose caches
mkdir -p %{buildroot}%{_localstatedir}/cache/libx11/compose
%if %{cross_compiling}
./mkallcomposecaches.sh prefix=%{_prefix} mkcomposecache=%{_sbindir}/mkcomposecache cachedir=%{buildroot}%{_localstatedir}/cache/libx11/compose xvfbopts="'-fp '\''%{_datadir}/fonts/misc'\'" /
%else
./mkallcomposecaches.sh prefix=%{_prefix} mkcomposecache=%{buildroot}%{_sbindir}/mkcomposecache cachedir=%{buildroot}%{_localstatedir}/cache/libx11/compose xvfbopts="'-fp '\''%{_datadir}/fonts/misc'\'" /
%endif

%files
%{_sbindir}/mkcomposecache
%doc %{_mandir}/man8/mkcomposecache.*

%files -n x11-compose-cache
%{_localstatedir}/cache/libx11/compose
