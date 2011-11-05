# revision 21126
# category Package
# catalog-ctan /macros/latex/contrib/codepage
# catalog-date 2011-01-18 23:40:40 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-codepage
Version:	20110118
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides a mechanism for inputting non-ASCII text.
Nowadays, the job is mostly done by the inputenc package in the
LaTeX distribution.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
