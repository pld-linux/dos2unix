Summary:	dos2unix - DOS/MAC to UNIX text file format converter
Summary(fr):	Convertisseur de format de fichier texte
Summary(pl):	dos2unix - konwerter plikСw tekstowych z formatu DOS/MAC na UNIX
Summary(pt_BR):	Conversor de formatos de arquivos texto
Summary(ru):	dos2unix - конвертор текстовых файлов DOS в формат UNIX
Summary(uk):	dos2unix - конвертор текстових файл╕в DOS в формат UNIX
Summary(zh_CN):	в╙╩╩DOS╩РMACнд╠╬нд╪Ч╣╫UNIX╦Яй╫
Name:		dos2unix
Version:	3.1
Release:	13
License:	Freer than LGPL
Group:		Applications/Text
Source0:	ftp://sunsite.unc.edu//pub/Linux/utils/text/%{name}-%{version}.tar.bz2
Patch0:		%{name}.patch
Patch1:		%{name}-segfault.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A utility that converts plain text files in DOS/MAC format to UNIX
format and back.

%description -l fr
Dos2unix converti des fichier texte DOS ou MAC au format UNIX.

%description -l pl
Zestaw narzЙdzi do konwersji pliki tekstowych w formacie DOS/MAC na
u©ywany poprzez UNIXa oraz odwrotnie.

%description -l pt_BR
O dos2unix converte arquivos texto do DOS e MAC para o formato texto
do Unix.

%description -l ru
dos2unix - конвертор текстовых файлов DOS в формат UNIX.

%description -l uk
dos2unix - конвертор текстових файл╕в DOS в формат UNIX.

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
