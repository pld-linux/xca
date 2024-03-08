Summary:	A GUI for handling X509 certificates, RSA keys, PKCS#10 Requests
Summary(pl.UTF-8):	GUI do obsługi certyfikatów X509, kluczy RSA, żądań PKCS#10
Name:		xca
Version:	2.6.0
Release:	1
Epoch:		1
License:	BSD
Group:		Applications/Communications
Source0:	https://github.com/chris2511/xca/releases/download/RELEASE.%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	be2ffca8a86d1ab564e5bd6f1040d383
Patch0:		cmake.patch
URL:		https://hohnstaedt.de/xca/
BuildRequires:	Qt5Sql-devel >= 5.14.0
BuildRequires:	Qt5Widgets-devel >= 5.14.0
BuildRequires:	cmake >= 3.16
BuildRequires:	libltdl-devel
BuildRequires:	openssl-devel >= 1.1.1
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= 5.14.0
BuildRequires:	qt5-linguist >= 5.14.0
BuildRequires:	python3-Sphinx
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

%package -n bash-completion-xca
Summary:	Bash completion for xca commands
Summary(pl.UTF-8):	Bashowe uzupełnianie parametrów dla poleceń xca
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0
%{?noarchpackage}

%description -n bash-completion-xca
Bash completion for xca commands.

%description -n bash-completion-xca -l pl.UTF-8
Bashowe uzupełnianie parametrów dla poleceń xca.

%prep
%setup -q
%patch0 -p1

%build

install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/xca,%{_desktopdir},%{_mandir}/man1}

%{__make} -C build install/fast \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database

%postun
%update_mime_database

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYRIGHT changelog README.md
%attr(755,root,root) %{_bindir}/xca
%{_datadir}/xca
%{_desktopdir}/xca.desktop*
%{_mandir}/man1/xca.1*
%{_docdir}/xca
%{_datadir}/metainfo/de.hohnstaedt.xca.metainfo.xml
%{_datadir}/mime/packages/xca.xml
%{_iconsdir}/hicolor/*/*/*.png
%{_pixmapsdir}/xca-32x32.xpm

%files -n bash-completion-xca
%defattr(644,root,root,755)
%{bash_compdir}/xca
