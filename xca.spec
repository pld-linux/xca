# TODO:
# - add Categories to xca.desktop
Summary:	A GUI for handling X509 certificates, RSA keys, PKCS#10 Requests
Summary(pl):	GUI do obs³ugi certyfikatów X509, kluczy RSA, ¿±dañ PKCS#10
Name:		xca
Version:	0.4.6
Release:	0.1
Epoch:		1
License:	BSD
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/xca/%{name}-%{version}.tar.gz
# Source0-md5:	3defe69788b9e0eb738f374143be6e12
Patch0:		%{name}-misc.patch
URL:		http://www.hohnstaedt.de/xca.html
BuildRequires:	db-cxx-devel
BuildRequires:	openssl-devel >= 0.9.7c
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphical certification authority is an interface for managing RSA
keys and certificates, and the creation and signing of PKCS#10
requests. It uses the OpenSSL library and a Berkeley DB for key and
certificate storage. It supports importing and exporting keys and PEM
DER PKCS8 certificates, signing and revoking of PEM DER PKCS12, and
the selection of x509v3 extensions. A tree view of certificates is
presented.

%description -l pl
Graficzne CA to interfejs do zarz±dzania kluczami RSA i certyfikatami,
tworzenia i podpisywania ¿±dañ PKCS#10. U¿ywa biblioteki OpenSSL i
bazy Berkeley DB do przechowywania kluczy i certyfikatów. Obs³uguje
importowanie i eksportowanie kluczy i certyfikatów PEM DER PKCS8,
podpisywanie i anulowanie PEM DER PKCS12 oraz wybór rozszerzeñ x509v3.
Pokazywane jest drzewo certyfikatów.

%prep
%setup -q
%%patch0 -p1

%build

LDFLAGS="%{rpmldflags}" \
CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcflags}" \
FFLAGS="%{rpmcflags}" \
%{?__cc:CC="%{__cc}"} \
%{?__cxx:CXX="%{__cxx}"} \
prefix="%{_prefix}" \
./configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/xca,%{_desktopdir}}

%{__make} install \
	destdir=$RPM_BUILD_ROOT
	
#mv $RPM_BUILD_ROOT%{_datadir}/applications/* $RPM_BUILD_ROOT%{_desktopdir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xca
%{_desktopdir}/xca*
%{_pixmapsdir}/xca*
