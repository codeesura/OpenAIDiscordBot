
# OpenAI

OpenAI, insanlığa yararlı ve güvenli bir şekilde yapay zeka geliştirmeyi amaçlayan bir araştırma kuruluşudur. Elon Musk ve Sam Altman gibi girişimciler, araştırmacılar ve filantroplar tarafından 2015 yılında kurulmuştur. Kuruluşun hedefi, yapay zeka alanında ilerlemektir ve makine öğrenimi, robotik ve yapay zeka güçlü teknolojileri ve uygulamalarının geliştirilmesine yönelik birçok girişimi ve projesi vardır. OpenAI, toplum için şeffaf, hesap verebilir ve yararlı olan yapay zeka geliştirmeyi hedeflemektedir ve araştırmacılar, politika yapıcılar ve diğer ilgililerle yakın işbirliği içinde çalışarak, yapay zeka'nın geliştirilmesi ve kullanımının sorumlu ve etik bir şekilde yapılmasını sağlar.

# OpenAI kütüphanesi

OpenAI, yapay zeka ve makine öğrenimi için birçok Python kütüphanesi yayınlamıştır ve bunlar OpenAI GitHub sayfasında (https://github.com/openai) mevcuttur. OpenAI tarafından yayınlanan önemli Python kütüphanelerinden bazıları şunlardır:

`gym`:  İyileştirme öğrenimi algoritmalarının geliştirilmesi ve karşılaştırılması için bir araç takımı.

`baselines`: İyileştirme öğrenimi algoritmalarının yüksek kaliteli, referans uygulamalarının bir kümesi.

`spinningup`: İyileştirme öğrenimi algoritmalarının eğitim kaynakları ve uygulamalarının bir kütüphanesi.

`openai-secret-manager`: Sürüm kontrolü ve sürekli entegrasyon ile uyumlu olarak, API anahtarları ve parolalar gibi gizli verileri güvenli bir şekilde saklamaya ve erişmeye yarayan bir Python kütüphanesi.

`openai-api-client`: Doğal dil işleme, bilgisayar görüşü ve daha fazlası gibi birçok güçlü yapay zeka modeline erişim sağlayan OpenAI API'sine erişmek için bir Python istemci kütüphanesidir.

Bu, OpenAI tarafından yayınlanan Python kütüphanelerinin sadece birkaç örneğidir ve kuruluş, Python ekosistemine yapay zeka ve makine öğrenimi için birçok diğer kütüphane, araç ve kaynak katkıda bulunmuştur.

# Kurulum

OpenAI API'si için bir API anahtarı almak için, OpenAI web sitesinde (https://beta.openai.com/signup/) bir hesap oluşturmanız gerekmektedir. Bir hesap oluşturduktan sonra, API anahtarınıza API panelinden (https://beta.openai.com/docs/api-overview/getting-started#authentication) erişebilirsiniz.

### Sanal Ortam

Python programlama bağlamında, ``Sanal ortam`` teriminin anlamı, Python programına kullanılabilir olan özel paket ve bağımlılık kümesidir. Bir ortam, kendi yüklenmiş paketleri ve bağımlılıkları olan, Python programlarını çalıştırmak için ayrı ve kendi içinde bağımsız bir ortam olarak düşünülebilir.

Python ortamlarını yönetmek için birçok araç ve yaklaşım vardır, bunlar arasında:

``virtualenv``: İzole Python ortamları oluşturmak için bir araç.

``pyenv``:  Çoklu Python sürümleri ve ortamlarını yönetmek için bir araç.

``conda``:  Python ve diğer diller için paket ve ortam yöneticisi, özellikle bilimsel hesaplamalar için yararlı.

``pipenv``: Python paketlerini ve ortamlarını yönetmek için bir araç, pip (Python paket yöneticisi) ve virtualenv'i birleştirir.

Her Python projesi veya uygulaması için ayrı bir ortam kullanmak, projenin gerektirdiği bağımlılıkların ve paketlerin diğer projelerden izole edildiğinden emin olmayı ve çakışma ve uyumluluk sorunlarını önlemeyi sağlar. Her Python projesi için ayrı bir ortam kullanmak, projenin gerekli tüm bağımlılıkları ve paketlerin yüklendiğinden emin olmak ve sistemde yüklü olabilecek diğer paketler veya bağımlılıklarla çakışmaları önlemek için iyi bir uygulamadır.

#### Sanal ortam oluşturmak (virtualenv)

``virtualenv`` kullanarak yeni bir Python sanal ortamı oluşturmak için öncelikle, Python paket yöneticisi ``pip`` kullanarak ``virtualenv`` paketini yüklemeniz gerekmektedir. Bunu aşağıdaki komutu çalıştırarak yapabilirsiniz:

```cmd
pip install virtualenv
```
``virtualenv`` yüklendikten sonra, ``virtualenv`` komutunu çalıştırarak istediğiniz ortamın adını takip ederek yeni bir sanal ortam oluşturabilirsiniz. Örneğin, ``myenv`` adlı bir sanal ortam oluşturmak için aşağıdaki komutu çalıştırırsınız:

```cmd
virtualenv myenv
```
Bu, geçerli çalışma dizininizde ``myenv`` adlı yeni bir dizin oluşturacaktır ve Python yürütülebilir dosyasının bir kopyasını ve Python paketleri ve bağımlılıkları için ayrı bir ortam oluşturmak için gereken dosyaları içerecektir.

Sanal ortamı etkinleştirmek için, virtualenv tarafından sağlanan activate betiğini çalıştırmak için ``source`` komutunu kullanmanız gerekmektedir. Linux veya macOS'ta, aşağıdaki komutu çalıştırarak bunu yapabilirsiniz:
```Linux
source myenv/bin/activate
```
Windows'ta aşağıdaki komutu kullanabilirsiniz:
```cmd
myenv\Scripts\activate.bat
```

Sanal ortam oluşturduktan sonra, kütüphaneleri indirmek gerekiyor.

OpenAI kütüphanesi :

```cmd
pip install openai
```
https://github.com/openai/openai-python
https://pypi.org/project/openai/

Discord kütüphanesi :
```cmd
pip install discord.py
```
https://github.com/Rapptz/discord.py
https://discordpy.readthedocs.io/en/stable/intro.html
https://pypi.org/project/discord.py/

```cmd
git clone https://github.com/codeesura/OpenAIDiscordBot
```



