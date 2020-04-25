Summary:	A GUI for handling X509 certificates, RSA keys, PKCS#10 Requests
Summary(pl.UTF-8):	GUI do obsługi certyfikatów X509, kluczy RSA, żądań PKCS#10
Name:		xca
Version:	2.2.1
Release:	1
Epoch:		1
License:	BSD
Group:		Applications/Communications
Source0:	https://github.com/chris2511/xca/releases/download/RELEASE.%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d9564be194d4e1e0b1139670f97a73d2
Patch0:		oids.patch
URL:		https://hohnstaedt.de/xca/
BuildRequires:	Qt5Sql-devel >= 5.14.0
BuildRequires:	Qt5Widgets-devel >= 5.14.0
BuildRequires:	libltdl-devel
BuildRequires:	openssl-devel >= 1.1.1
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= 5.14.0
BuildRequires:	qt5-linguist >= 5.14.0
BuildRequires:	sgml-tools
BuildRequires:	sgml-tools-dtd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphical certification authority is an interface for managing RSA
keys and certificates, and the creation and signing of PKCS#10
requests. It uses the OpenSSL library and a Berkeley DB for key and
certificate storage. It supports importing and exporting keys and PEM
DER PKCS8 certificates, signing and revoking of PEM DER PKCS12, and
the selection of x509v3 extensions. A tree view of certificates is
presented.

%description -l pl.UTF-8
Graficzne CA to interfejs do zarządzania kluczami RSA i certyfikatami,
tworzenia i podpisywania żądań PKCS#10. Używa biblioteki OpenSSL i
bazy Berkeley DB do przechowywania kluczy i certyfikatów. Obsługuje
importowanie i eksportowanie kluczy i certyfikatów PEM DER PKCS8,
podpisywanie i anulowanie PEM DER PKCS12 oraz wybór rozszerzeń x509v3.
Pokazywane jest drzewo certyfikatów.

%prep
%setup -q
%patch0 -p1

%build

%configure \
	--disable-doc

%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/xca,%{_desktopdir},%{_mandir}/man1}

%{__make} install \
	destdir=$RPM_BUILD_ROOT

%{__make} -C doc ENABLE_DOC="" install \
	destdir=$RPM_BUILD_ROOT

gzip -dc doc/xca.1.gz >$RPM_BUILD_ROOT%{_mandir}/man1/xca.1
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/xca.1.gz

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database

%postun
%update_mime_database

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYRIGHT changelog
%attr(755,root,root) %{_bindir}/xca
%{_datadir}/xca
%{_desktopdir}/xca.desktop*
%{_mandir}/man1/xca.1*
%{_docdir}/xca
%{_datadir}/mime/packages/xca.xml
%{_pixmapsdir}/xca-32x32.xpm
