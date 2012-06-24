Summary:	Configuration and diagnostic utils for 3Com 5x9 cards
Summary(pl):	Narz�dzia konfiguracyjne i diagnostyczne dla kart 3Com 5x9
Name:		3c5x9setup
Version:	0.05b.redhog.1
Release:	1
License:	GPL
Group:		Networking/Utilities
URL:		http://mini.dhs.org/Projects/Programming/Current/3c5x9setup/
Source0:	http://mini.dhs.org/Projects/Programming/Current/3c5x9setup/Sources/%{name}.donald.becker.%{version}.c
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EEPROM setup and diagnostic program for the 3Com 3c5x9 series
ethercards.

%description -l pl
Narz�dzie do konfiguracji EEPROM i diagnostyki kart sieciowych 3Com
serii 3c5x9.

%prep
%setup -q -T -c
cp -f %{SOURCE0} .

%build
%{__cc} %{rpmcflags} %{rpmldflags} -o 3c5x9setup 3c5x9setup*.c

%install
rm -rf $RPM_BUILD_ROOT
install -D 3c5x9setup $RPM_BUILD_ROOT%{_sbindir}/3c5x9setup

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
