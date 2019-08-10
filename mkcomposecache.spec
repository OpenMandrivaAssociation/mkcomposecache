Summary:	Used for creating global (system-wide) Compose cache files
Name:		mkcomposecache
Version:	1.2.1
Release:	19
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
# For building mkcomposecache itself
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
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_sbindir}/mkcomposecache
%{_mandir}/man8/mkcomposecache.*
