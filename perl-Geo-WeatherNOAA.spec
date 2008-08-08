%define module	Geo-WeatherNOAA
%define name	perl-%{module}
%define version 4.38
%define release %mkrel 3

Summary:	Perl extension for interpreting the NOAA weather data
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Requires:	perl
URL:		http://search.cpan.org/~msolomon/%{module}-%{version}
Source:		%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(LWP::Simple)
Buildroot:	%{_tmppath}/%{name}-root
BuildArch:	noarch

%description
This module is intended to interpret the NOAA zone forecasts and current 
city hourly data files. It should give a programmer an easy time to use 
the data instead of having to mine it.

Be aware that if the variable $main::opt_v is set to anything (other than 
zero or '') then Geo::WeatherNOAA will be verbose on what it's doing with 
messages sent to STDERR. Useful for debugging. 

%prep
%setup -q -n %{module}-%{version}

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

