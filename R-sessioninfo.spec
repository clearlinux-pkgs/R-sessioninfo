#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-sessioninfo
Version  : 1.2.2
Release  : 34
URL      : https://cran.r-project.org/src/contrib/sessioninfo_1.2.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/sessioninfo_1.2.2.tar.gz
Summary  : R Session Information
Group    : Development/Tools
License  : GPL-2.0
Requires: R-cli
BuildRequires : R-cli
BuildRequires : R-mockery
BuildRequires : buildreq-R

%description
# sessioninfo
> R Session Information
<!-- badges: start -->
[![Lifecycle: stable](https://lifecycle.r-lib.org/articles/figures/lifecycle-stable.svg)](https://lifecycle.r-lib.org/articles/stages.html)
[![R build status](https://github.com/r-lib/sessioninfo/workflows/R-CMD-check/badge.svg)](https://github.com/r-lib/sessioninfo/actions)
[![](https://www.r-pkg.org/badges/version/sessioninfo)](https://www.r-pkg.org/pkg/sessioninfo)
[![CRAN RStudio mirror downloads](https://cranlogs.r-pkg.org/badges/sessioninfo)](https://www.r-pkg.org/pkg/sessioninfo)
[![Coverage Status](https://img.shields.io/codecov/c/github/r-lib/sessioninfo/master.svg)](https://codecov.io/github/r-lib/sessioninfo?branch=master)
<!-- badges: end -->

%prep
%setup -q -c -n sessioninfo
cd %{_builddir}/sessioninfo

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641121407

%install
export SOURCE_DATE_EPOCH=1641121407
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sessioninfo
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sessioninfo
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sessioninfo
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc sessioninfo || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/sessioninfo/DESCRIPTION
/usr/lib64/R/library/sessioninfo/INDEX
/usr/lib64/R/library/sessioninfo/Meta/Rd.rds
/usr/lib64/R/library/sessioninfo/Meta/features.rds
/usr/lib64/R/library/sessioninfo/Meta/hsearch.rds
/usr/lib64/R/library/sessioninfo/Meta/links.rds
/usr/lib64/R/library/sessioninfo/Meta/nsInfo.rds
/usr/lib64/R/library/sessioninfo/Meta/package.rds
/usr/lib64/R/library/sessioninfo/NAMESPACE
/usr/lib64/R/library/sessioninfo/NEWS.md
/usr/lib64/R/library/sessioninfo/R/sessioninfo
/usr/lib64/R/library/sessioninfo/R/sessioninfo.rdb
/usr/lib64/R/library/sessioninfo/R/sessioninfo.rdx
/usr/lib64/R/library/sessioninfo/R/sysdata.rdb
/usr/lib64/R/library/sessioninfo/R/sysdata.rdx
/usr/lib64/R/library/sessioninfo/help/AnIndex
/usr/lib64/R/library/sessioninfo/help/aliases.rds
/usr/lib64/R/library/sessioninfo/help/figures/session-info2.svg
/usr/lib64/R/library/sessioninfo/help/paths.rds
/usr/lib64/R/library/sessioninfo/help/sessioninfo.rdb
/usr/lib64/R/library/sessioninfo/help/sessioninfo.rdx
/usr/lib64/R/library/sessioninfo/html/00Index.html
/usr/lib64/R/library/sessioninfo/html/R.css
/usr/lib64/R/library/sessioninfo/tests/testthat.R
/usr/lib64/R/library/sessioninfo/tests/testthat/_snaps/diff.md
/usr/lib64/R/library/sessioninfo/tests/testthat/fixtures/MD5
/usr/lib64/R/library/sessioninfo/tests/testthat/fixtures/biobase.rda
/usr/lib64/R/library/sessioninfo/tests/testthat/fixtures/descs.rda
/usr/lib64/R/library/sessioninfo/tests/testthat/fixtures/devtools-deps.rda
/usr/lib64/R/library/sessioninfo/tests/testthat/fixtures/devtools-info-unix.rda
/usr/lib64/R/library/sessioninfo/tests/testthat/fixtures/devtools-info-windows.rda
/usr/lib64/R/library/sessioninfo/tests/testthat/fixtures/devtools.rda
/usr/lib64/R/library/sessioninfo/tests/testthat/fixtures/fsdfgwetdhsdfhq4yqh_0.0.0.9000.tar.gz
/usr/lib64/R/library/sessioninfo/tests/testthat/fixtures/gh.html.gz
/usr/lib64/R/library/sessioninfo/tests/testthat/fixtures/installed.rda
/usr/lib64/R/library/sessioninfo/tests/testthat/fixtures/lines1.txt
/usr/lib64/R/library/sessioninfo/tests/testthat/fixtures/lines2.txt
/usr/lib64/R/library/sessioninfo/tests/testthat/fixtures/lines3.txt
/usr/lib64/R/library/sessioninfo/tests/testthat/fixtures/lines4.txt
/usr/lib64/R/library/sessioninfo/tests/testthat/fixtures/memoise.rda
/usr/lib64/R/library/sessioninfo/tests/testthat/fixtures/no-remote-repo.rda
/usr/lib64/R/library/sessioninfo/tests/testthat/fixtures/no-sha.rda
/usr/lib64/R/library/sessioninfo/tests/testthat/test-dependent-packages.R
/usr/lib64/R/library/sessioninfo/tests/testthat/test-diff.R
/usr/lib64/R/library/sessioninfo/tests/testthat/test-loaded-packages.R
/usr/lib64/R/library/sessioninfo/tests/testthat/test-os-name.R
/usr/lib64/R/library/sessioninfo/tests/testthat/test-package-info.R
/usr/lib64/R/library/sessioninfo/tests/testthat/test-platform-info.R
/usr/lib64/R/library/sessioninfo/tests/testthat/test-printing.R
/usr/lib64/R/library/sessioninfo/tests/testthat/test-session-info.R
/usr/lib64/R/library/sessioninfo/tests/testthat/test-utils.R
/usr/lib64/R/library/sessioninfo/tests/testthat/test-warnings.R
