Name:		texlive-listings-ext
Version:	29349
Release:	2
Summary:	Automated input of source
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/listings-ext
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listings-ext.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listings-ext.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listings-ext.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-listings-ext.bin = %{EVRD}

%description
The package provides a means of marking a source, so that
samples of it may be included in a document (by means of the
listings package) in a stable fashion, regardless of any change
to the source. The markup in the source text defines tags for
blocks of source. These tags are processed by a shell script to
make a steering file that is used by the package when LaTeX is
being run.y.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/listings-ext.sh
%{_texmfdistdir}/scripts/listings-ext/listings-ext.sh
%{_texmfdistdir}/tex/latex/listings-ext/listings-ext.sty
%doc %{_texmfdistdir}/doc/latex/listings-ext/README
%doc %{_texmfdistdir}/doc/latex/listings-ext/THIS_IS_VERSION_v67
%doc %{_texmfdistdir}/doc/latex/listings-ext/getversion.tex
%doc %{_texmfdistdir}/doc/latex/listings-ext/hyperref.cfg
%doc %{_texmfdistdir}/doc/latex/listings-ext/listings-ext.bib
%doc %{_texmfdistdir}/doc/latex/listings-ext/listings-ext.el
%doc %{_texmfdistdir}/doc/latex/listings-ext/listings-ext.makemake
%doc %{_texmfdistdir}/doc/latex/listings-ext/listings-ext.mk
%doc %{_texmfdistdir}/doc/latex/listings-ext/listings-ext.pdf
%doc %{_texmfdistdir}/doc/latex/listings-ext/listings-ext_exmpl_a.java
%doc %{_texmfdistdir}/doc/latex/listings-ext/listings-ext_exmpl_b.java
%doc %{_texmfdistdir}/doc/latex/listings-ext/listings-ext_exmpl_c.java
%doc %{_texmfdistdir}/doc/latex/listings-ext/listings-ext_exmpl_d.java
%doc %{_texmfdistdir}/doc/latex/listings-ext/listings-ext_exmpl_e.java
%doc %{_texmfdistdir}/doc/latex/listings-ext/listings-ext_test_a.tex
%doc %{_texmfdistdir}/doc/latex/listings-ext/listings-ext_test_d.tex
%doc %{_texmfdistdir}/doc/latex/listings-ext/listings.cfg
#- source
%doc %{_texmfdistdir}/source/latex/listings-ext/listings-ext.dtx
%doc %{_texmfdistdir}/source/latex/listings-ext/listings-ext.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/listings-ext/listings-ext.sh listings-ext.sh
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
