Web Sitesinin Ne İşe Yaradığı:
Yukarıda verdiğiniz kodlar, Flask framework'ü kullanılarak geliştirilmiş bir sosyal medya uygulamasını temsil ediyor. Bu uygulama, kullanıcıların aşağıdaki işlemleri yapmasına olanak tanır:

### Hesap Oluşturma ve Giriş Yapma:

- Kullanıcılar, e-posta adresleri ve şifreleriyle kayıt olabilir.

- Kayıt olduktan sonra e-posta doğrulaması yapılır.

- Şifre sıfırlama işlevi mevcuttur.

### Hikaye (Story) Paylaşma:

- Kullanıcılar metin, fotoğraf veya video içeren hikayeler paylaşabilir.

- Paylaşılan hikayeler düzenlenebilir veya silinebilir.

- Beğenme ve Yorum Yapma:

- Kullanıcılar, hikayeleri beğenebilir veya beğenmeyebilir.

- Hikayelere yorum yapabilir ve yorumları beğenebilir veya beğenmeyebilir.

### Takip Etme ve Takipçi Yönetimi:

- Kullanıcılar birbirlerini takip edebilir veya takibi bırakabilir.

- Profil sayfalarında takipçi ve takip edilen kişi listeleri görüntülenebilir.

### Profil Yönetimi:

- Kullanıcılar, kendi profillerini görüntüleyebilir ve düzenleyebilir.

- Diğer kullanıcıların profillerini ziyaret edebilir.

### Güvenlik ve Doğrulama:

- Şifreler güçlü şifre politikasına uygun olmalıdır.

- E-posta doğrulama ve şifre sıfırlama işlemleri mevcuttur.

### 
- Hangi Programlama Dilleri ve Teknolojiler Kullanıldı?
### Bu proje, aşağıdaki programlama dilleri ve teknolojiler kullanılarak geliştirilmiştir:

- Python:

- Flask: Web uygulamasının temel framework'ü.

- Flask-Login: Kullanıcı oturum yönetimi için kullanıldı.

- Flask-PyMongo: MongoDB veritabanı bağlantısı için kullanıldı.

- Flask-Bcrypt: Şifrelerin hash'lenmesi için kullanıldı.

- MongoDB: Veritabanı olarak MongoDB kullanıldı. Kullanıcı bilgileri, hikayeler, yorumlar ve beğeniler burada saklanır.

- HTML/CSS/JavaScript:

- HTML: Web sayfalarının yapısını oluşturmak için kullanıldı.

- CSS: Bootstrap kütüphanesi kullanılarak sayfaların stilini belirlemek için kullanıldı.

- JavaScript: Dinamik işlevler (beğenme, yorum yapma, hikaye düzenleme vb.) için kullanıldı.

- Jinja2:

Flask ile birlikte kullanılan bir template engine. HTML sayfalarına dinamik veri eklemek için kullanıldı.

SMTP (E-posta Gönderme):

Kullanıcı kaydı ve şifre sıfırlama işlemleri için e-posta gönderme işlevselliği eklendi. Gmail SMTP sunucusu kullanıldı.

Kodların Ne Yaptığı (Detaylı Açıklama):
1. app.py (Ana Uygulama Dosyası):
Flask uygulamasının ana yapılandırmasını içerir.

Blueprint'ler: auth (kimlik doğrulama) ve main (ana işlevler) olmak üzere iki blueprint kullanıldı.

Oturum Yönetimi: Kullanıcı oturumlarının süresi ve güvenliği ayarlandı.

MongoDB ve Bcrypt Başlatma: Veritabanı ve şifre hash'leme işlemleri için gerekli yapılandırmalar yapıldı.

2. config.py (Yapılandırma Dosyası):
Uygulamanın gizli anahtarı (SECRET_KEY) ve MongoDB bağlantı URI'si gibi yapılandırma bilgilerini içerir.

3. models.py (Veritabanı Modelleri):
User Sınıfı: Kullanıcı bilgilerini ve işlevlerini (şifre hash'leme, e-posta doğrulama, takip etme vb.) yönetir.

MongoDB İşlemleri: Kullanıcı oluşturma, güncelleme, silme ve sorgulama işlemleri burada tanımlandı.

4. auth/routes.py (Kimlik Doğrulama İşlemleri):
Kayıt Olma: Kullanıcıların kaydolmasını ve e-posta doğrulamasını yönetir.

Giriş Yapma: Kullanıcıların giriş yapmasını ve oturum açmasını sağlar.

Şifre Sıfırlama: Kullanıcıların şifrelerini sıfırlamasına olanak tanır.

E-posta Doğrulama: Kullanıcıların e-posta adreslerini doğrulamasını sağlar.

5. main/routes.py (Ana İşlevler):
Hikaye Yönetimi: Kullanıcıların hikaye eklemesini, düzenlemesini ve silmesini sağlar.

Beğenme ve Yorum Yapma: Kullanıcıların hikayeleri ve yorumları beğenmesini veya beğenmemesini sağlar.

Takip Etme: Kullanıcıların birbirlerini takip etmesini sağlar.

Profil Yönetimi: Kullanıcı profillerinin görüntülenmesini ve düzenlenmesini sağlar.

6. HTML Şablonları:
base.html: Tüm sayfalar için ortak bir temel şablon.

login.html, signup.html: Kullanıcı girişi ve kaydolma sayfaları.

story.html: Hikayelerin listelendiği ve yeni hikayelerin eklendiği sayfa.

profile.html: Kullanıcı profillerinin görüntülendiği sayfa.

edit_story.html, edit_comment.html: Hikaye ve yorum düzenleme sayfaları.

7. JavaScript İşlevleri:
Beğenme/Beğenmeme: Hikayeler ve yorumlar için beğenme/beğenmeme işlevselliği.

Bağlam Menüsü: Sağ tıklama ile hikaye ve yorum düzenleme seçenekleri.

8. Veritabanı Güncelleme Scriptleri:
update_comments.py: Yorumların benzersiz kimlikler (ID) ile güncellenmesini sağlar.

update_likes_dislikes.py: Beğenilerin ve beğenmeyenlerin sayısal değerlere dönüştürülmesini sağlar.

Genel Çalışma Mantığı:
Kullanıcı Kaydı ve Girişi:

Kullanıcı kaydolurken e-posta doğrulaması yapılır.

Giriş yaparken şifre hash'leri karşılaştırılır.

Hikaye Paylaşma ve Yönetme:

Kullanıcılar metin, fotoğraf veya video içeren hikayeler paylaşabilir.

Hikayeler düzenlenebilir veya silinebilir.

Beğenme ve Yorum Yapma:

Kullanıcılar hikayeleri ve yorumları beğenebilir veya beğenmeyebilir.

Beğeniler ve yorumlar dinamik olarak güncellenir.

Takip Etme ve Profil Yönetimi:

Kullanıcılar birbirlerini takip edebilir veya takibi bırakabilir.

Profil sayfalarında takipçi ve takip edilen kişi listeleri görüntülenebilir.

Güvenlik:

Şifreler güçlü şifre politikasına uygun olmalıdır.

E-posta doğrulama ve şifre sıfırlama işlemleri mevcuttur.

Sonuç:
Bu proje, Flask ve MongoDB kullanılarak geliştirilmiş temel bir sosyal medya uygulamasıdır. Kullanıcıların hikayeler paylaşmasına, birbirlerini takip etmesine ve etkileşimde bulunmasına
olanak tanır. Ayrıca, güvenlik ve kullanıcı deneyimi için çeşitli işlevler (e-posta doğrulama, şifre sıfırlama, beğenme/yorum yapma) eklenmişti
