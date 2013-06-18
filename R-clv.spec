%global packname  clv
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.3_2
Release:          2
Summary:          Cluster Validation Techniques
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-2.tar.gz
Requires:         R-cluster
Requires:         R-class 
BuildRequires:    R-devel
BuildRequires:    Rmath-devel
BuildRequires:    texlive-collection-latex
BuildRequires:    R-cluster
BuildRequires:    R-class
BuildRequires:    pkgconfig(lapack)

%description
Package contains most of the popular internal and external cluster
validation methods ready to use for the most of the outputs produced by
functions coming from package "cluster". Package contains also functions
and examples of usage for cluster stability approach that might be applied
to algorithms implemented in "cluster" package as well as user defined
clustering algorithms.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Mon Feb 20 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3_2-1
+ Revision: 777613
- Import R-clv
- Import R-clv

