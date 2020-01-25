#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	IO
%define		pnam	Mux
Summary:	IO::MUX - an IO stream multiplexing module
Summary(pl.UTF-8):	IO::MUX - moduł multipleksera dla strumieni we/wy
Name:		perl-IO-Mux
Version:	0.08
Release:	0.1
# "same as perl"
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6cd0d7d9b5a4b5a3caeb610dabaaf5d8
URL:		http://search.cpan.org/dist/IO-Mux/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"IO::Mux" allows you to multiplex several virtual streams over a
single pipe or socket. This is achieved by creating an "IO::Mux"
object on each end of the real stream and then creating virtual
handles ("IO::Mux::Handle" objects) from these "IO::Mux" objects.

%description -l pl.UTF-8
"IO::Mux" pozwala na utworzenie kilku wirtualnych strumieni w oparciu
o pojedynczy potok lub gniazdo. Jest to osiągane poprzez tworzenie
obiektu "IO::Mux" na każdym końcu rzeczywistego strumienia, a
następnie tworzenie wirtualnych uchwytów skojarzonych z tymi
obiektami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/IO/Mux.pm
%dir %{perl_vendorlib}/IO/Mux
%{perl_vendorlib}/IO/Mux/*.pm
%{_mandir}/man3/*
