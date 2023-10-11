# DCL-162: Advanced Python Programming

These projects are created as part of the following training: DCL-162 "Advanced Python Programming"

Please follow the link for the complete training catalog: https://www.deepcloudlabs.com/resources

# Modules and Packages

Python'da bir paket oluşturmak için bir dizin yaratmanız yeterli olacaktır:

![Installation folder](module10-figure01.png?raw=true "package directory content")

Bu dizin yapısı içinde **`__init__.py`** dosyası modül yüklenirken bir kere çalıştırılır ve modülle ilgili başlangıç işlemleri gerçekleştirilir:

```python
print("deepcloudlabs module is loaded!")
# all initialization code goes here

from deepcloudlabs.dictionary import lines

with open("deepcloudlabs/dictionary-tur.txt", "r") as the_file:
    for line in the_file.readlines():
        lines.append(line.strip())
```

Böylelikle modül içindeki **dictionary.py** dosyası içinde tekrar tekrar dosyanın yüklenmesine gerek olmaz:


```python
lines = []

def get_word(index):
    return lines[index]
```

Burada **lines** listesi her zaman modül yüklenirken sözlük dosyası okunarak doldurulur. Modülün kullanımına ilişkin aşağıdaki örneklere göz atalım:

```python
from deepcloudlabs.utils import lost_numbers as nums, is_even as cift_mi

print(nums)
print(cift_mi(42))

import deepcloudlabs.hr

print(dir(deepcloudlabs))
example = {
    "identity": "9876543210",
    "fullname": "kate austen"
}
jack = deepcloudlabs.hr.Employee("12345678910", "jack bauer")

kate = deepcloudlabs.hr.Employee(**example)

print(jack.identity, jack.fullname)
print(kate.identity, kate.fullname)

from deepcloudlabs.dictionary import get_word

print(get_word(42))
```

**deepcloudlabs** altındaki **utils.py** paketini yüklemek için aşağıdaki python satırını yazmanız yeterli olacaktır:

```python
from deepcloudlabs.utils import lost_numbers as nums, is_even as cift_mi
```

**deepcloudlabs** altındaki **hr.py** paketini yüklemek için aşağıdaki python satırını yazmanız yeterli olacaktır:

```python
import deepcloudlabs.hr
```

Bu şekilde **Employee** sınıfından nesne yaratabilirsiniz:

```python
example = {
    "identity": "9876543210",
    "fullname": "kate austen"
}
jack = deepcloudlabs.hr.Employee("12345678910", "jack bauer")

kate = deepcloudlabs.hr.Employee(**example)

print(jack.identity, jack.fullname)
print(kate.identity, kate.fullname)
```
Sözlükteki 42. sıradaki kelimeye erişmek için ise aşağıdaki kodu yazıyoruz:

```python
from deepcloudlabs.dictionary import get_word

print(get_word(42))
```

# Python'da PIP Paketi Oluşturmak

Python'da **pip paketi** oluşturmak için aşağıdaki adımları izleyebilirsiniz:

![paket dizin yapısı](pip-module-fig01.png?raw=true "package directory content")

![paket dizin yapısı](pip-module-fig03.png?raw=true "package directory content")

![paket dizin yapısı](pip-module-fig02.png?raw=true "package directory content")

**setup.py** dosyası içinde dağıtım dosyalarını oluşturacak Python betiği yer alıyor:

```python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='dcllottery',  
     version='0.1',
     scripts=['dcl-lottery'] ,
     author="Binnur Kurt",
     author_email="info@deepcloudlabs.com",
     description="Lottery utility package",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/deepcloudlabs/lottery",
     packages=setuptools.find_packages(where="src"),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
    package_dir={"": "src"},
    python_requires=">=3.6",
 )
 ```
**setup.py** betiğini çalıştırabilmek için iki paketin kurulu olması gerekiyor: **setuptools** ve **wheel**. Eğer kurulu değil iseler aşağıdaki verildiği şekilde bu iki paketi kurabilirsiniz:

```bash
$ pip install setuptools wheel
Collecting setuptools
  Using cached setuptools-57.4.0-py3-none-any.whl (819 kB)
Collecting wheel
  Using cached wheel-0.36.2-py2.py3-none-any.whl (35 kB)
Installing collected packages: wheel, setuptools
Successfully installed setuptools-57.4.0 wheel-0.36.2
```

**setup.py** dosyasını çalıştırarak dağıtım dosylarını oluşturabilirsiniz:

```bash 
$ python setup.py bdist_wheel
running bdist_wheel
running build
running build_py
creating build
creating build\lib
creating build\lib\dcllottery
copying src\dcllottery\utils.py -> build\lib\dcllottery
copying src\dcllottery\__init__.py -> build\lib\dcllottery
running build_scripts
creating build\scripts-3.9
copying dcl-lottery -> build\scripts-3.9
installing to build\bdist.win-amd64\wheel
running install
running install_lib
creating build\bdist.win-amd64
creating build\bdist.win-amd64\wheel
creating build\bdist.win-amd64\wheel\dcllottery
copying build\lib\dcllottery\utils.py -> build\bdist.win-amd64\wheel\.\dcllottery
copying build\lib\dcllottery\__init__.py -> build\bdist.win-amd64\wheel\.\dcllottery
running install_egg_info
running egg_info
creating src\dcllottery.egg-info
writing src\dcllottery.egg-info\PKG-INFO
writing dependency_links to src\dcllottery.egg-info\dependency_links.txt
writing top-level names to src\dcllottery.egg-info\top_level.txt
writing manifest file 'src\dcllottery.egg-info\SOURCES.txt'
reading manifest file 'src\dcllottery.egg-info\SOURCES.txt'
adding license file 'LICENSE'
writing manifest file 'src\dcllottery.egg-info\SOURCES.txt'
Copying src\dcllottery.egg-info to build\bdist.win-amd64\wheel\.\dcllottery-0.1-py3.9.egg-info
running install_scripts
creating build\bdist.win-amd64\wheel\dcllottery-0.1.data
creating build\bdist.win-amd64\wheel\dcllottery-0.1.data\scripts
copying build\scripts-3.9\dcl-lottery -> build\bdist.win-amd64\wheel\dcllottery-0.1.data\scripts
adding license file "LICENSE" (matched pattern "LICEN[CS]E*")
creating build\bdist.win-amd64\wheel\dcllottery-0.1.dist-info\WHEEL
creating 'dist\dcllottery-0.1-py3-none-any.whl' and adding 'build\bdist.win-amd64\wheel' to it
adding 'dcllottery/__init__.py'
adding 'dcllottery/utils.py'
adding 'dcllottery-0.1.data/scripts/dcl-lottery'
adding 'dcllottery-0.1.dist-info/LICENSE'
adding 'dcllottery-0.1.dist-info/METADATA'
adding 'dcllottery-0.1.dist-info/WHEEL'
adding 'dcllottery-0.1.dist-info/top_level.txt'
adding 'dcllottery-0.1.dist-info/RECORD'
removing build\bdist.win-amd64\wheel
```

Artık dağıtım dosyalarını https://pypi.org sitesine taşıyabiliriz:

```bash 
$ python -m twine upload  dist/*
Uploading distributions to https://upload.pypi.org/legacy/
Enter your password: *your password*
Uploading dcllottery-0.1-py3-none-any.whl
100%|████████████████████████████████████████████████████████████████████| 6.06k/6.06k [00:02<00:00, 2.25kB/s]

View at:
https://pypi.org/project/dcllottery/0.1/
```

Artık herhangi bir proje içinden bu pakete ulaşabilirsiniz:

```bash
$ pip install dcllottery
Collecting dcllottery
  Using cached dcllottery-0.1-py3-none-any.whl (3.0 kB)
Installing collected packages: dcllottery
Successfully installed dcllottery-0.1
```

Örnek bir kullanım için aşağıdaki kodu kullanabilirsiniz:

```python
import dcllottery.utils as dcl

numbers = dcl.get_lottery_numbers(1,60,6)
print(numbers)
```
