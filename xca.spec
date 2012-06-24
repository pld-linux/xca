Summary:	A GUI for handling X509 certificates, RSA keys, PKCS#10 Requests
Name:		xca
Version:	0.2.7
Release:	1
Epoch:		1
License:	BSD
Group:		Applications/Communications
Source0:	http://xca.sourceforge.net/src/%{name}-%{version}.tar.gz
URL:		http://www.hohnstaedt.de/xca.html
BuildRequires:	openssl-devel
BuildRequires:	db3-devel
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_mandir		%{_prefix}/man

%description
Graphical certification authority is an interface for managing RSA
keys and certificates, and the creation and signing of PKCS#10
requests. It uses the OpenSSL library and a Berkeley DB for key and
certificate storage. It supports importing and exporting keys and PEM
DER PKCS8 certificates, signing and revoking of PEM DER PKCS12, and
the selection of x509v3 extensions. A tree view of certificates is
presented.

%prep
%setup -q

%build
%configure \
	CPPFLAGS="-I%{_includedir}/qt" \
	LDFLAGS="-L%{_libdir}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xca
