Summary:	configuration and diagnostic utils for 3Com 5x9 cards.
Name:		3c5x9setup
Version:	0.05b.redhog.1
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narzêdzia
Group(pt_BR):	Rede/Utilitários
URL:		http://mini.dhs.org/Projects/Programming/Current/3c5x9setup/
Source0:	http://mini.dhs.org/Projects/Programming/Current/3c5x9setup/Sources/%{name}.donald.becker.%{version}.c
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EEPROM setup and diagnostic program for the 3Com 3c5x9 series ethercards

%prep
%setup -q -T -c
cp %{SOURCE0} .

%build
gcc %{rpmcflags} %{rpmldflags} -o 3c5x9setup 3c5x9setup*.c

%install
rm -rf $RPM_BUILD_ROOT
install -D 3c5x9setup $RPM_BUILD_ROOT%{_sbindir}/3c5x9setup

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
