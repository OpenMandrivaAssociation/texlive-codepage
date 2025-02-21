Name:		texlive-codepage
Version:	51502
Release:	2
Summary:	Support for variant code pages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/codepage
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codepage.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codepage.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codepage.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a mechanism for inputting non-ASCII text.
Nowadays, the job is mostly done by the inputenc package in the
LaTeX distribution.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/codepage/code437.tex
%{_texmfdistdir}/tex/latex/codepage/code850.tex
%{_texmfdistdir}/tex/latex/codepage/codeiso1.tex
%{_texmfdistdir}/tex/latex/codepage/codemac.tex
%{_texmfdistdir}/tex/latex/codepage/codepage.sty
%{_texmfdistdir}/tex/latex/codepage/initcar.tex
%{_texmfdistdir}/tex/latex/codepage/shapecm.tex
%{_texmfdistdir}/tex/latex/codepage/shapedc.tex
%doc %{_texmfdistdir}/doc/latex/codepage/LISEZMOI
%doc %{_texmfdistdir}/doc/latex/codepage/README
%doc %{_texmfdistdir}/doc/latex/codepage/codepage.pdf
%doc %{_texmfdistdir}/doc/latex/codepage/frintro.pdf
%doc %{_texmfdistdir}/doc/latex/codepage/voyel850.tex
%doc %{_texmfdistdir}/doc/latex/codepage/voyeliso.tex
#- source
%doc %{_texmfdistdir}/source/latex/codepage/codepage.drv
%doc %{_texmfdistdir}/source/latex/codepage/codepage.dtx
%doc %{_texmfdistdir}/source/latex/codepage/codepage.ins
%doc %{_texmfdistdir}/source/latex/codepage/frintro.drv

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
