Summary:	Used for creating global (system-wide) Compose cache files
Name:		mkcomposecache
Version:	1.2.1
Release:	7
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xorg-macros)

%description
mkcomposecache is used for creating global (system-wide) Compose cache files.

Compose cache files help with application startup times and memory usage,
especially in locales with large Compose tables (e.g. all UTF-8 locales).

The tool only makes sense with libX11 1.0.2 and higher.
Included is a script mkallcomposecaches.sh that creates global cache
files for all supported locales.

%prep
%setup -q

%build
%configure2_5x \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}
%make

%install
%makeinstall_std

%files
%{_sbindir}/mkcomposecache
%{_mandir}/man8/mkcomposecache.*

