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
