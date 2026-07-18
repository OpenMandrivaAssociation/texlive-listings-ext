%global tl_name listings-ext
%global tl_revision 29349
%global tl_bin_links listings-ext.sh:%{_texmfdistdir}/scripts/listings-ext/listings-ext.sh

Name:		texlive-%{tl_name}
Epoch:		1
Version:	67
Release:	%{tl_revision}.1
Summary:	Automated input of source
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/listings-ext
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listings-ext.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listings-ext.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listings-ext.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(listings-ext.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
The package provides a means of marking a source, so that samples of it
may be included in a document (by means of the listings package) in a
stable fashion, regardless of any change to the source. The markup in
the source text defines tags for blocks of source. These tags are
processed by a shell script to make a steering file that is used by the
package when LaTeX is being run.y

