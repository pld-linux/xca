Summary:	A GUI for handling X509 certificates, RSA keys, PKCS#10 Requests
Summary(pl):	GUI do obs�ugi certyfikat�w X509, kluczy RSA, ��da� PKCS#10
Name:		xca
Version:	0.3.0
Release:	1
Epoch:		1
License:	BSD
Group:		Applications/Communications
Source0:	http://xca.sourceforge.net/src/%{name}-%{version}.tar.gz
Patch:		%{name}-makefile.patch
URL:		http://www.hohnstaedt.de/xca.html
BuildRequires:	db-devel
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Graphical certification authority is an interface for managing RSA
keys and certificates, and the creation and signing of PKCS#10
requests. It uses the OpenSSL library and a Berkeley DB for key and
certificate storage. It supports importing and exporting keys and PEM
DER PKCS8 certificates, signing and revoking of PEM DER PKCS12, and
the selection of x509v3 extensions. A tree view of certificates is
presented.

%description -l pl
Graficzne CA to interfejs do zarz�dzania kluczami RSA i certyfikatami,
tworzenia i podpisywania ��da� PKCS#10. U�ywa biblioteki OpenSSL i
bazy Berkeley DB do przechowywania kluczy i certyfikat�w. Obs�uguje
importowanie i eksportowanie kluczy i certyfikat�w PEM DER PKCS8,
podpisywanie i anulowanie PEM DER PKCS12 oraz wyb�r rozszerze� x509v3.
Pokazywane jest drzewo certyfikat�w.

%prep
%setup -q
%patch -p1

%build
%configure \
	CPPFLAGS="-I%{_includedir}/qt" \
	LDFLAGS="-L%{_libdir}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_datadir}/xca}

%{__make} install \
	prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xca
