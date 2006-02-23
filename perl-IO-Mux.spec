#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IO
%define		pnam	Mux
Summary:	IO::MUX - an IO stream multiplexing module
Summary(pl):	IO::MUX - moduł multiplexera dla strumieni IO
Name:		perl-IO-Mux
Version:	0.07
Release:	0.1
# "same as perl"
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	52b58db6366ff287bf2dddecad7d3ce2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(anything_fake_or_conditional)'

%description
"IO::Mux" allows you to multiplex several virtual streams over a single pipe or
socket. This is achieved by creating an "IO::Mux" object on each end of the
real stream and then creating virtual handles ("IO::Mux::Handle" objects) from
these "IO::Mux" objects.

%description -l pl
"IO::Mux" pozwala na utworzenie kilku wirtualnych strumieniu w oparciu o pojedyńczy potok
lub gniazdo. Jest to osiagane poprzez tworzenie obiektu "IO::Mux" na kazdym koncu rzeczywistego
strumienia i następnie tworzeniu wirtualnych uchwytów skojarzonych z tymi obiektami.

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
%{perl_vendorlib}/IO/Mux/*.pm
%{_mandir}/man3/*