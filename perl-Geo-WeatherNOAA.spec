%define upstream_name	 Geo-WeatherNOAA
%define upstream_version 4.38

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl extension for interpreting the NOAA weather data
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Geo/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(LWP::Simple)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module is intended to interpret the NOAA zone forecasts and current 
city hourly data files. It should give a programmer an easy time to use 
the data instead of having to mine it.

Be aware that if the variable $main::opt_v is set to anything (other than 
zero or '') then Geo::WeatherNOAA will be verbose on what it's doing with 
messages sent to STDERR. Useful for debugging. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
make OPTIMIZE="$RPM_OPT_FLAGS" 

%install
rm -rf $RPM_BUILD_ROOT 
%makeinstall_std 

%clean
rm -rf $RPM_BUILD_ROOT 

%check
make test

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man3/*
%{perl_vendorlib}/Geo/*


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 4.380.0-1mdv2010.0
+ Revision: 403225
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 4.38-3mdv2009.0
+ Revision: 268516
- rebuild early 2009.0 package (before pixel changes)

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.38-2mdv2009.0
+ Revision: 210956
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix spacing at top of description
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 4.38-1mdv2008.0
+ Revision: 20115
- buildrequires
- 4.38


* Sat Jun 03 2006 Stew Benedict <sbenedict@mandriva.com> 4.37-3mdv2007.0
- rebuild, url

* Mon May 16 2005 Stew Benedict <sbenedict@mandriva.com> 4.37-2mdk
- rebuild

* Sun Apr 04 2004 Stew Benedict <sbenedict@mandrakesoft.com> 4.37-1mdk
- first Mandrake release

