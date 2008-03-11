Summary:	A GUI for handling X509 certificates, RSA keys, PKCS#10 Requests
Summary(pl.UTF-8):	GUI do obsługi certyfikatów X509, kluczy RSA, żądań PKCS#10
Name:		xca
Version:	0.6.4
Release:	1
Epoch:		1
License:	BSD
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/xca/%{name}-%{version}.tar.gz
# Source0-md5:	f805a2e094436f976c7a4cda5980027e
Patch0:		%{name}-build.patch
Patch1:		%{name}-openssl.patch
Patch2:		%{name}-doc.patch
URL:		http://www.hohnstaedt.de/xca.html
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	QtGui-devel >= 4.2.7
BuildRequires:	sgml-tools
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
%patch1 -p1
%patch2 -p1

%build
# Play non-standard build system:
CFLAGS="%{rpmcxxflags}" \
CXXFLAGS="%{rpmcxxflags}" \
%{?__cc:CC="%{__cxx}"} \
%{?__cxx:CXX="%{__cxx}"} \
prefix="%{_prefix}" \
./configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/xca,%{_desktopdir},%{_mandir}/man1}

%{__make} install \
	destdir=$RPM_BUILD_ROOT

install doc/xca.1.gz $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xca
%{_desktopdir}/xca*
%{_mandir}/man1/xca.1*
