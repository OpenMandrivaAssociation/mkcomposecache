Summary:	Used for creating global (system-wide) Compose cache files
Name:		mkcomposecache
Version:	1.2.1
Release:	11
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
# For building mkcomposecache itself
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xorg-macros)

# For generating the caches
BuildRequires:	x11-server-xvfb
BuildRequires:	xbiff
BuildRequires:	libx11-common

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

%prep
%setup -q

%build
%configure2_5x \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}
%make

%install
%makeinstall_std

# Generate compose caches
mkdir -p %{buildroot}%{_localstatedir}/cache/libx11/compose
./mkallcomposecaches.sh prefix=%{_prefix} mkcomposecache=%{buildroot}%{_sbindir}/mkcomposecache cachedir=%{buildroot}%{_localstatedir}/cache/libx11/compose xvfbopts="'-fp '\''%{_datadir}/fonts/misc'\'" /

%files
%{_sbindir}/mkcomposecache
%{_mandir}/man8/mkcomposecache.*

%files -n x11-compose-cache
%{_localstatedir}/cache/libx11/compose
