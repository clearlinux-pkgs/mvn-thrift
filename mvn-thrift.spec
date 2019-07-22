#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-thrift
Version  : 0.9.3
Release  : 2
URL      : https://repo1.maven.org/maven2/org/apache/thrift/libthrift/0.9.3/libthrift-0.9.3.jar
Source0  : https://repo1.maven.org/maven2/org/apache/thrift/libthrift/0.9.3/libthrift-0.9.3.jar
Source1  : https://repo.maven.apache.org/maven2/org/apache/thrift/libfb303/0.9.3/libfb303-0.9.3.jar
Source2  : https://repo.maven.apache.org/maven2/org/apache/thrift/libfb303/0.9.3/libfb303-0.9.3.pom
Source3  : https://repo1.maven.org/maven2/org/apache/thrift/libthrift/0.9.3/libthrift-0.9.3.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-thrift-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-thrift package.
Group: Data

%description data
data components for the mvn-thrift package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/thrift/libthrift/0.9.3
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/thrift/libthrift/0.9.3/libthrift-0.9.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/thrift/libfb303/0.9.3
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/thrift/libfb303/0.9.3/libfb303-0.9.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/thrift/libfb303/0.9.3
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/thrift/libfb303/0.9.3/libfb303-0.9.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/thrift/libthrift/0.9.3
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/thrift/libthrift/0.9.3/libthrift-0.9.3.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/thrift/libfb303/0.9.3/libfb303-0.9.3.jar
/usr/share/java/.m2/repository/org/apache/thrift/libfb303/0.9.3/libfb303-0.9.3.pom
/usr/share/java/.m2/repository/org/apache/thrift/libthrift/0.9.3/libthrift-0.9.3.jar
/usr/share/java/.m2/repository/org/apache/thrift/libthrift/0.9.3/libthrift-0.9.3.pom
