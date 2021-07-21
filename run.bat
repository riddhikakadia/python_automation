SET PATH="C:\Python36"

cd /d "%~dp0"

cd ..

py.test --junit-xml="./reports/report.xml"