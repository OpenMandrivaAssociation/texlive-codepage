# revision 21126
# category Package
# catalog-ctan /macros/latex/contrib/codepage
# catalog-date 2011-01-18 23:40:40 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-codepage
Version:	20180303
Release:	1
Summary:	Support for variant code pages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/codepage
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codepage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codepage.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codepage.source.tar.xz
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
%doc %{_texmfdistdir}/doc/latex/codepage/demo.zip
%doc %{_texmfdistdir}/doc/latex/codepage/frintro.pdf
#- source
%doc %{_texmfdistdir}/source/latex/codepage/codepage.drv
%doc %{_texmfdistdir}/source/latex/codepage/codepage.dtx
%doc %{_texmfdistdir}/source/latex/codepage/codepage.ins
%doc %{_texmfdistdir}/source/latex/codepage/frintro.drv

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110118-2
+ Revision: 750333
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110118-1
+ Revision: 718091
- texlive-codepage
- texlive-codepage
- texlive-codepage
- texlive-codepage
- texlive-codepage

