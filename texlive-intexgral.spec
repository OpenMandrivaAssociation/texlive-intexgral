%global tl_name intexgral
%global tl_revision 79814

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.1.0
Release:	%{tl_revision}.1
Summary:	A LaTeX package for typesetting integrals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/intexgral
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/intexgral.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/intexgral.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/intexgral.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Typesetting integrals, although common in LaTeX, is not particularly
practical. The way in which the different parts are managed often
generates unreadable source code, making modifications laborious. The
package therefore follows a simple philosophy: focus on the essential
element of an integral, the integrand. Everything else (limits,
differentials, symbols) can be modified using keys. These keys are
designed to allow you to easily and quickly change the style of an
integral. Additionally, the package provides various auxiliary macros to
support some keys which can have lengthy inputs.

