Name: mkcomposecache
Version: 1.2.1
Release: %mkrel 4
Summary: Used for creating global (system-wide) Compose cache files
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
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



%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-3mdv2011.0
+ Revision: 666432
- mass rebuild

* Thu Dec 02 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.2.1-2mdv2011.0
+ Revision: 604944
- Remove Packager tag
- Rebuild

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.2.1-1mdv2010.1
+ Revision: 464637
- New version: 1.2.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.2-6mdv2010.0
+ Revision: 426147
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.2-5mdv2009.0
+ Revision: 223290
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.2-4mdv2008.1
+ Revision: 170983
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.2-3mdv2008.1
+ Revision: 166394
- Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Tue Jan 22 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2mdv2008.1
+ Revision: 156497
- Updated BuildRequires and resubmit package.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.2-1mdv2008.1
+ Revision: 130019
- kill re-definition of %%buildroot on Pixel's request
- fix man pages


* Mon Feb 05 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.2-1mdv2007.0
+ Revision: 116282
- new version: 1.2

* Sat Jul 08 2006 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.1-2mdv2007.0
+ Revision: 38450
- added missing build dependency on libx11-devel

* Tue Jul 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.1-1mdv2007.0
+ Revision: 38303
- new upstream release(1.1):
  * Set default cache path to /var/cache/libx11/compose (see libX11 1.0.3).
  * Invocation parameters changed.
  * Improved customizability a lot.
  * More tests & verification.
  * Being more verbose now.
  * Works for root now.
  *General cleanup.
  * Should work out-of-the-box on 64bit machines now

* Sat Jul 01 2006 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0-1mdv2007.0
+ Revision: 38214
- Adding mkcomposecache to the repository.

