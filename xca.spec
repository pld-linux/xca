# TODO:
# - patch makefiles to use CXXFLAGS from %%optflags
# - add Categories to xca.desktop
Summary:	A GUI for handling X509 certificates, RSA keys, PKCS#10 Requests
Summary(pl):	GUI do obs³ugi certyfikatów X509, kluczy RSA, ¿±dañ PKCS#10
Name:		xca
Version:	0.4.5
Release:	0.1
Epoch:		1
License:	BSD
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/xca/%{name}-%{version}.tar.gz
# Source0-md5:	27a401c6e3ed1e406a602c2e7f8c3f4e
Patch:		%{name}-makefile.patch
URL:		http://www.hohnstaedt.de/xca.html
BuildRequires:	db-cxx-devel
BuildRequires:	db-devel
BuildRequires:	openssl-devel >= 0.9.7
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
#%%patch -p1

%build
%configure \
	CPPFLAGS="-I%{_includedir}/qt" \
	LDFLAGS="-L%{_libdir}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/xca}

%{__make} install \
	prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xca
%{_datadir}/applications/xca*
%{_datadir}/pixmaps/xca*
