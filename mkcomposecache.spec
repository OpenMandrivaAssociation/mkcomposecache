Name: mkcomposecache
Version: 1.2
Release: %mkrel 3
Summary: Used for creating global (system-wide) Compose cache files
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
Packager: Gustavo Pichorim Boiko <boiko@mandriva.com> 
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: libx11-devel

%description
mkcomposecache is used for creating global (system-wide) Compose cache files.

Compose cache files help with application startup times and memory usage,
especially in locales with large Compose tables (e.g. all UTF-8 locales).

The tool only makes sense with libX11 1.0.2 and higher.
Included is a script mkallcomposecaches.sh that creates global cache
files for all supported locales.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x 	--x-includes=%{_includedir} \
		--x-libraries=%{_libdir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sbindir}/mkcomposecache
%{_mandir}/man8/mkcomposecache.*


