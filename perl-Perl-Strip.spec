#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Perl
%define		pnam	Strip
%include	/usr/lib/rpm/macros.perl
Summary:	Perl::Strip - reduce file size by stripping whitespace, comments, pod etc.
Name:		perl-Perl-Strip
Version:	1.1
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Perl/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	23a6302ad6e09fe45ccb720b37c9875e
URL:		http://search.cpan.org/dist/Perl-Strip/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(PPI) >= 1.213
BuildRequires:	perl-common-sense >= 3.3
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module transforms Perl sources into a more compact format. It
does this by removing most whitespace, comments, pod, and by some
other means.

The resulting code looks obfuscated, but perl (and the deparser) don't
have any problems with that. Depending on the source file you can
expect about 30-60% "compression".

The main target for this module is low-diskspace environments, such as
App::Staticperl, boot floppy/CDs/flash environments and so on.

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
%doc README Changes
%attr(755,root,root) %{_bindir}/perlstrip
%{_mandir}/man1/perlstrip.1p*
%{_mandir}/man3/Perl::Strip.3pm*
%{perl_vendorlib}/Perl/Strip.pm
