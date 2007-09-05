Summary:	dos2unix - DOS/MAC to UNIX text file format converter
Summary(fr.UTF-8):	Convertisseur de format de fichier texte
Summary(pl.UTF-8):	dos2unix - konwerter plików tekstowych z formatów DOS/MAC na UNIX
Summary(pt_BR.UTF-8):	Conversor de formatos de arquivos texto
Summary(ru.UTF-8):	dos2unix - конвертор текстовых файлов DOS в формат UNIX
Summary(uk.UTF-8):	dos2unix - конвертор текстових файлів DOS в формат UNIX
Summary(zh_CN.UTF-8):	转换DOS或MAC文本文件到UNIX格式
Name:		dos2unix
Version:	3.1
Release:	16
License:	Freer than LGPL
Group:		Applications/Text
Source0:	http://www.go.dlr.de/linux/src/%{name}-%{version}.tar.gz
# Source0-md5:	25ff56bab202de63ea6f6c211c416e96
Patch0:		%{name}.patch
Patch1:		%{name}-segfault.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A utility that converts plain text files in DOS/MAC format to UNIX
format.

%description -l fr.UTF-8
Dos2unix converti des fichier texte DOS ou MAC au format UNIX.

%description -l pl.UTF-8
Zestaw narzędzi do konwersji plików tekstowych z formatów DOS/MAC na
format używany przez UNIX-a.

%description -l pt_BR.UTF-8
O dos2unix converte arquivos texto do DOS e MAC para o formato texto
do Unix.

%description -l ru.UTF-8
dos2unix - конвертор текстовых файлов DOS в формат UNIX.

%description -l uk.UTF-8
dos2unix - конвертор текстових файлів DOS в формат UNIX.

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
