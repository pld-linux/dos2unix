Summary:	dos2unix - DOS/MAC to UNIX text file format converter
Summary(fr):	Convertisseur de format de fichier texte
Summary(pl):	dos2unix - konwerter plików tekstowych z formatów DOS/MAC na UNIX
Summary(pt_BR):	Conversor de formatos de arquivos texto
Summary(ru):	dos2unix - ËÏÎ×ÅÒÔÏÒ ÔÅËÓÔÏ×ÙÈ ÆÁÊÌÏ× DOS × ÆÏÒÍÁÔ UNIX
Summary(uk):	dos2unix - ËÏÎ×ÅÒÔÏÒ ÔÅËÓÔÏ×ÉÈ ÆÁÊÌ¦× DOS × ÆÏÒÍÁÔ UNIX
Summary(zh_CN):	×ª»»DOS»òMACÎÄ±¾ÎÄ¼þµ½UNIX¸ñÊ½
Name:		dos2unix
Version:	3.1
Release:	15
License:	Freer than LGPL
Group:		Applications/Text
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/text/%{name}-%{version}.tar.bz2
# Source0-md5:	f90026a397cf787083ec2e4892c6dcdd
Patch0:		%{name}.patch
Patch1:		%{name}-segfault.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A utility that converts plain text files in DOS/MAC format to UNIX
format.

%description -l fr
Dos2unix converti des fichier texte DOS ou MAC au format UNIX.

%description -l pl
Zestaw narzêdzi do konwersji plików tekstowych z formatów DOS/MAC na
format u¿ywany przez UNIX-a.

%description -l pt_BR
O dos2unix converte arquivos texto do DOS e MAC para o formato texto
do Unix.

%description -l ru
dos2unix - ËÏÎ×ÅÒÔÏÒ ÔÅËÓÔÏ×ÙÈ ÆÁÊÌÏ× DOS × ÆÏÒÍÁÔ UNIX.

%description -l uk
dos2unix - ËÏÎ×ÅÒÔÏÒ ÔÅËÓÔÏ×ÉÈ ÆÁÊÌ¦× DOS × ÆÏÒÍÁÔ UNIX.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__cc} %{rpmcflags} -o dos2unix dos2unix.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install dos2unix $RPM_BUILD_ROOT%{_bindir}
install dos2unix.1 $RPM_BUILD_ROOT%{_mandir}/man1

ln -sf dos2unix $RPM_BUILD_ROOT%{_bindir}/mac2unix

echo ".so dos2unix.1" > $RPM_BUILD_ROOT%{_mandir}/man1/mac2unix.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
