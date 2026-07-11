%global tl_name codepage
%global tl_revision 51502

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Support for variant code pages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/codepage
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/codepage.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/codepage.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/codepage.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a mechanism for inputting non-ASCII text. Nowadays,
the job is mostly done by the inputenc package in the LaTeX
distribution.

