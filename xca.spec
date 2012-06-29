Summary:	A GUI for handling X509 certificates, RSA keys, PKCS#10 Requests
Summary(pl.UTF-8):	GUI do obsługi certyfikatów X509, kluczy RSA, żądań PKCS#10
Name:		xca
Version:	0.9.3
Release:	0.1
Epoch:		1
License:	BSD
Group:		Applications/Communications
Source0:	http://downloads.sourceforge.net/xca/%{name}-%{version}.tar.gz
# Source0-md5:	5e08cf8a93f023b1b3836c203bd0a694
Patch0:		%{name}-doc.patch
URL:		http://www.hohnstaedt.de/xca.html
BuildRequires:	QtGui-devel >= 4.3.0
BuildRequires:	libltdl-devel
BuildRequires:	openssl-devel >= 0.9.8
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= 4.3.0
BuildRequires:	qt4-linguist >= 4.3.0
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
# Play non-standard build system:
CFLAGS="%{rpmcxxflags}" \
CXXFLAGS="%{rpmcxxflags}" \
%{?__cc:CC="%{__cxx}"} \
%{?__cxx:CXX="%{__cxx}"} \
prefix="%{_prefix}" \
./configure

%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/xca,%{_desktopdir},%{_mandir}/man1}

%{__make} install \
	destdir=$RPM_BUILD_ROOT

gzip -dc doc/xca.1.gz >$RPM_BUILD_ROOT%{_mandir}/man1/xca.1
%{__rm} $RPM_BUILD_ROOT%{_prefix}/man/man1/xca.1.gz

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database

%postun
%update_mime_database

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYRIGHT changelog doc/*.html
%attr(755,root,root) %{_bindir}/xca
%{_datadir}/xca
%{_desktopdir}/xca.desktop*
%{_mandir}/man1/xca.1*
%{_datadir}/mime/packages/xca.xml
