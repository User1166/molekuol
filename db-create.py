from app import app, db, Molekul, Ozellik, MolekulYapisi

with app.app_context():
    # Veritabanını temizle (Eğer gerekliyse)
    db.drop_all()
    db.create_all()

    # Tüm özellikleri doğrudan tanımla
    ozellikler_txt = {
        "NH3": {
            "Yapı": "Her amonyak molekülü üç hidrojen atomu ve bir azot atomu içerir. Formülü (NH3) olan amonyak molekülü piramidal bir yapıya sahiptir.",
            "Fiziksel Özellikler": "Renk: Renksiz, Koku: Keskin ve rahatsız edici bir kokuya sahiptir. Kaynama Noktası: -33.34 °C (sıvı amonyak), Erime Noktası: -77.73 °C, Yoğunluk: Oda sıcaklığında gaz halinde hafif bir gazdır (hava yoğunluğunun yaklaşık %60'ı).",
            "Kimyasal Özellikler": "Amonyak, bazik özellikler gösterir. Su ile tepkimeye girdiğinde amonyum iyonu (NH₄⁺) oluşturur. Amonyak, asitlerle tepkimeye girerek tuzlar oluşturur. Amonyak, nitrat ve nitrit gibi bileşiklerin oluşumunda önemli bir rol oynar. Polar bir molekül olup, su gibi polar çözücülerde iyi çözünür.",
            "Kimyasal Reaksiyonlar": "Asit-Baz Tepkimeleri: Amonyak, asitlerle tepkimeye girerek amonyum tuzları oluşturur. Oksidasyon: Amonyak, yüksek sıcaklıklarda oksijenle tepkimeye girerek azot oksitleri (NO, NO₂) oluşturabilir. Haber Süreci: Amonyak, endüstriyel olarak azot ve hidrojen gazlarının tepkimesiyle üretilir.",
            "Toksik Etkiler": "Amonyak, yüksek konsantrasyonlarda toksik olabilir. Solunduğunda solunum yollarını tahriş edebilir ve gözlerde yanma hissine yol açabilir. Amonyak buharları, ciltle temas ettiğinde de tahriş edicidir.",
            "Kullanım Alanları": "İlaç sentezi (Aminler, amin türevleri), Boyar madde üretimi (Azot bileşikleri), Plastik üretimi (Poliamidler, örneğin naylon), Zirai ilaçlar (Amonyak türevi pestisitler)."
        },
        "H2": {
            "Yapı": "Diatomik molekül olup, iki hidrojen atomunun kovalent bağ ile birleşmesiyle oluşur. Bağ uzunluğu: 74 pm. Bağ açısı: 180° (doğrusal yapı).",
            "Fiziksel Özellikler": "Molekül Ağırlığı: 2.016 g/mol. Gaz halinde (oda sıcaklığında). Renksiz, kokusuz. Kaynama Noktası: –252.87 °C. Erime Noktası: –259.16 °C. Yoğunluk: 0.0899 g/L. Suda çözünürlük düşük.",
            "Kimyasal Özellikler": "Oldukça reaktif bir elementtir ve birçok bileşik oluşturabilir. Oksijenle birleşerek su (H₂O) oluşturur. İndirgen ajan olarak çalışır. Elektron verebilir. Asidik özellikler göstermez, daha çok bazik özellikler gösterir.",
            "Kimyasal Reaksiyonlar": "Hidrojenin oksijenle reaksiyonu (yanma), Hidrojenin metallerle reaksiyonu (hidrojenasyon), Hidrojenin halojenlerle reaksiyonu, Hidrojenin azotla reaksiyonu, Hidrojenin karbonla reaksiyonu.",
            "Toksik Etkiler": "Yanıcı ve patlayıcıdır (havada %4–75 konsantrasyon). Yüksek konsantrasyonlarda boğulma riski. Yanıklar: Yüksek sıcaklıklarda ciddi yanıklar.",
            "Kullanım Alanları": "Kimya sanayi (Amonyak üretimi, hidrojenasyon), Enerji üretimi (yakıt hücreleri), Petrol sanayi, Metal işleme, Gıda endüstrisi, Elektrik üretimi, Laboratuvarlar, Uzay sanayi (roket yakıtı)."
        },
        "O2": {
            "Yapı": "Oksijen, diatomik bir molekül olup, iki oksijen atomu arasında kovalent bağ ile birleşir. Molekül doğrusal yapıdadır ve bağ uzunluğu 121 pm'dir. Oksijenin, diatomik molekülünün bağ açısı 180°'dir.",
            "Fiziksel Özellikler": "Molekül Ağırlığı: 32.00 g/mol, Fiziksel Hali: Gaz (oda sıcaklığında), Renk ve Koku: Renksiz, kokusuz, Kaynama Noktası: –183.0°C, Erime Noktası: –218.79°C, Yoğunluk: 1.429 g/L, Suda Çözünürlük: 3.0 cm³ / 100 cm³",
            "Kimyasal Özellikler": "Oksijen, güçlü bir oksitleyici (elektron alıcı) maddedir. Elektron alabilir, birçok bileşiği oksitler. Özellikle metaller ve organik bileşiklerle reaksiyona girerek oksitler oluşturur. Bir Lewis bazıdır.",
            "Kimyasal Reaksiyonlar": "Yanma Reaksiyonları, Metallerin Oksitlenmesi, Ozonun Oluşumu, Asitlerle Reaksiyonlar, Hidrojen Peroksit Üretimi.",
            "Toksik Etkiler": "Normal atmosfer koşullarında toksik değildir. Yüksek oksijen seviyeleri oksijen zehirlenmesine yol açabilir. 1-2 atmosfer basınçta zehirlenme belirtileri: baş ağrısı, bulantı, baş dönmesi ve solunum güçlükleri.",
            "Kullanım Alanları": "Tıp (solunum desteği), Sanayi (metal üretimi), Kimya sanayi (metanol, asetik asit üretimi), Enerji üretimi, Havacılık, Su arıtma, Ozon tabakası oluşumu."
        },
        "C2H2": {
            "Yapı": "Kimyasal formülü C₂H₂ olan Asetilen, iki karbon atomu arasında üçlü bağ bulunan en basit alkin bileşiğidir. Her bir karbon atomu, bir hidrojen atomuna bağlıdır.",
            "Fiziksel Özellikler": "Ağır gaz: Oda sıcaklığında gaz halindedir. Kokusuz: Kendine özgü bir kokusu yoktur, ancak yanma sırasında farklı kokular oluşabilir. Su ile az çözünür, organik çözücülerde iyi çözünür.",
            "Kimyasal Özellikler": "Yanıcı bir gazdır ve yanma reaksiyonları sırasında yüksek sıcaklıklar oluşturur. Hidrojenasyon, halojenasyon ve polimerizasyon gibi reaksiyonlar gösterebilir. Zayıf asit olarak kabul edilir ve alkali metallerle reaksiyona girerek asetilid tuzları oluşturabilir.",
            "Kimyasal Reaksiyonlar": "Yanma tepkimesi, Hidrojenasyon tepkimesi, Halojenasyon tepkimesi, Hidrasyon tepkimesi, Polimerizasyon tepkimesi.",
            "Toksik Etkiler": "Yüksek konsantrasyonlarda solunduğunda boğulma riski. Merkezi sinir sistemi üzerinde baskılayıcı etki. Baş ağrısı, baş dönmesi ve bilinç kaybı.",
            "Kullanım Alanları": "Kaynak gazı olarak kullanılır. Metal kesme ve kaynak işlemlerinde yaygın olarak tercih edilir. Organik sentezlerde başlangıç maddesi. Aydınlatma sistemlerinde (tarihi kullanım)."
        },
        "CO2": {
            "Yapı": "Doğrusal O=C=O, İki çift bağ (C=O) içerir, Kutuplanmamış (apolar) bir moleküldür.",
            "Fiziksel Özellikler": "Renk ve Koku: Renksiz ve kokusuz bir gazdır. Erime ve Kaynama Noktası: CO₂, gaz halinde oda sıcaklığında bulunur, ancak -78.5°C'de katı (süblimleşir) hale geçer ve -56.6°C'de sıvı hale gelir. Yoğunluk: Karbondioksit, havadan daha yoğun bir gazdır. Çözünürlük: CO₂, su içinde çözünür.",
            "Kimyasal Özellikler": "Asidik Özellik: CO₂, su ile birleştiğinde karbonik asit (H₂CO₃) oluşturur. Elektron Çekici yapısı Karbondioksit moleküler yapısında karbon atomu yüksek elektronegatifliğe sahiptir.",
            "Kimyasal Reaksiyonlar": "Karbonil Grubu, Karboksilasyon Reaksiyonları (Grignard, Aldol Yoğunlaşması ve Diğer Polimerizasyon Reaksiyonları), Fotosentez reaksiyonları.",
            "Toksik Etkiler": "CO₂, konsantrasyonu arttığında solunum için tehlikeli olabilir. Yüksek konsantrasyonlarda (yaklaşık %5 ve üzerinde) boğulma riski doğurabilir.",
            "Kullanım Alanları": "Kimyasal Sentezler, Organik Sentez Reaksiyonları, Karboksilat İyonları ve Esterler üretimi, Süperkritik CO₂ uygulamaları."
        },
        "N2": {
            "Yapı": "İki azot atomu arasında üçlü kovalent bağ bulunan diatomik bir molekül. Bağ uzunluğu 1.0976 Å. Doğada genellikle iki atomlu molekül halinde (N₂) bulunur. N₂ molekülü üçlü kovalent bağ içerir ve bu bağ çok güçlüdür.",
            "Fiziksel Özellikler": "Fiziksel hali: Gaz (oda sıcaklığında), Renk, koku, tat: Renksiz, kokusuz, tatsız, Erime noktası: -210°C, Kaynama noktası: -196°C, Yoğunluk (0°C, 1 atm'de): ~1.25 g/L, Suda az çözünür, Elektrik iletmez.",
            "Kimyasal Özellikler": "Kararlılık: N₂ molekülü çok kararlı ve inerttir (üçlü bağdan dolayı), Reaktivite: Normal koşullarda az reaktif, yüksek sıcaklık veya katalizörle reaktif hale gelir, Elektronegatiflik: 3.04 (yüksek), Oksitlenme basamakları: -3 (amonyak), +1, +2, +3, +4, +5 (nitrik asit gibi).",
            "Kimyasal Reaksiyonlar": "Haber Süreci (Amonyak sentezi), Yanma (oksijenle reaksiyon), Asit oluşumu, Metal azotürlerin oluşumu.",
            "Toksik Etkiler": "N₂ gazı: Zehirli değil fakat oksijenin yerini alırsa boğulmaya neden olabilir, Yüksek konsantrasyonda: Bilinç kaybı, baş dönmesi, boğulma riski, Azot oksitleri (NO, NO₂): Solunum yollarını tahriş eder, toksiktir, Sıvı azot: Ciltle temas halinde donmaya neden olabilir (soğuk yanığı).",
            "Kullanım Alanları": "Endüstride, Laboratuvarlarda, Elektronik sanayisinde, Gıda sanayisinde, Tıpta kullanım alanları mevcuttur."
        },
        "C6H6": {
            "Yapı": "Aromatik halka yapısı (6 karbon atomu), Düzlemsel geometri, Rezonans yapısı mevcut, Her karbon atomu bir hidrojen atomuna bağlı.",
            "Fiziksel Özellikler": "Erime noktası: 5.5°C, Kaynama noktası: 80.1°C, Renksiz sıvı, Tatlımsı aromatik koku, Suda az çözünür, Organik çözücülerde iyi çözünür.",
            "Kimyasal Özellikler": "Kararlı yapı (rezonans), Aromatik özellik, SEAr reaksiyonları verir, Katılma reaksiyonlarına dirençli, Yanıcı (dumanlı alev).",
            "Kimyasal Reaksiyonlar": "Elektrofilik aromatik sübstitüsyon, Friedel-Crafts alkilleme/açilleme, Nitrasyon, Sülfonasyon, Halojenasyon.",
            "Toksik Etkiler": "Kanserojen etki (lösemi riski), Merkezi sinir sistemi üzerinde toksik, Uzun süreli maruziyette kan hastalıkları, Solunduğunda baş dönmesi ve bilinç kaybı.",
            "Kullanım Alanları": "Endüstriyel çözücü, Plastik üretimi, Reçine üretimi, Sentetik kauçuk üretimi, Boya ve ilaç endüstrisi hammaddesi."
        },
        "CO": {
            "Yapı": "Doğrusal bir yapıya sahiptir. Karbon (C) ve oksijen (O) atomları arasında bir üçlü bağ bulunur.",
            "Fiziksel Özellikler": "Molekül Ağırlığı: 28.01 g/mol. Gaz halinde, renksiz, kokusuz. Kaynama Noktası: –191.5°C, Erime Noktası: –205°C. Yoğunluk: 0.967 (hava=1). Suda çözünürlük düşük.",
            "Kimyasal Özellikler": "Zayıf indirgen madde, elektron verebilir. Metallerle kompleks bileşikler oluşturur. Lewis asidi olarak davranır.",
            "Kimyasal Reaksiyonlar": "Yanma (oksidasyon), metallerin indirgenmesi, fosfor bileşikleri üretimi, organik bileşiklerin sentezi.",
            "Toksik Etkiler": "Hemoglobinle bağlanır, dokulara oksijen taşınmasını engeller. Düşük dozda: baş ağrısı, baş dönmesi. Yüksek dozda: solunum yetmezliği, beyin hasarı, ölüm.",
            "Kullanım Alanları": "Kimya sanayi (asetik asit üretimi), metalürji, enerji üretimi, laboratuvarlar, otomotiv sektörü."
        },
        "CH2O": {
            "Yapı": "Moleküler formül: CH₂O, Yapısı: H-C(=O)-H (bir karbonil grubu ve iki hidrojen bağlı), Karbonil grubu: Aldehit fonksiyonel grubudur (-CHO).",
            "Fiziksel Özellikler": "Oda sıcaklığında gaz hâlindedir (kaynama noktası ≈ -19°C), Suda çok iyi çözünür → %37'lik sulu çözeltisine formalin denir, Keskin, tahriş edici kokuludur.",
            "Kimyasal Özellikler": "Formaldehit karbonil grubu sayesinde reaktif bir bileşiktir, Aldehit özellikleri gösterir, Nükleofillerle reaksiyona girer, Polimerleşmeye yatkındır, İndirgenebilir, İndirgeme testlerine pozitif yanıt verir.",
            "Toksik Etkiler": "Zehirli ve kanserojendir, Solunduğunda, yutulduğunda veya cilde temas ettiğinde tehlikelidir, Kanserojen olarak sınıflandırılmıştır.",
            "Kullanım Alanları": "Reçine üretimi (ürea-formaldehit, fenol-formaldehit), Tekstil ve kağıt sanayiinde sertleştirici, Dezenfektan (formalin formunda), Organik sentezlerde ara madde.",
            "Kimyasal Reaksiyonlar": """a) İndirgenme:
            b) Oksidasyon:
            c) Asetal Oluşumu (Alkollerle):
            d) Polimerleşme (Kondensasyon):
            e) Aminlerle reaksiyon (Schiff bazı oluşumu):"""
        },
        "CS2": {
            "Yapı": "Doğrusal molekül: S=C=S, S=C çift bağları içerir (rezonans yapısı), CO₂'ye benzer yapı.",
            "Fiziksel Özellikler": "Molekül Ağırlığı: 76.14 g/mol, Sıvı (oda sıcaklığında), Renksiz, hoş olmayan keskin koku, Erime Noktası: -111.6°C, Kaynama Noktası: 46.3°C, Yoğunluk: 1.26 g/cm³.",
            "Kimyasal Özellikler": "Yanıcı, elektrofilik, çift bağlara sahip, polimerleşmeye yatkın değil, bazı metallerle kompleks yapabilir.",
            "Toksik Etkiler": "Soluma: Baş dönmesi, baş ağrısı, bilinç kaybı. Uzun süreli maruziyet: Sinir sistemi bozuklukları. Yüksek dozda: Ölüm riski.",
            "Kullanım Alanları": "Viskon üretimi, Lastik sanayi, Pestisit üretimi, Organik çözücü, Kimya araştırmaları.",
            "Kimyasal Reaksiyonlar": "Yanma:---Hidrojen sülfür ile tepkime (tiyokarbamidler oluşabilir)-------:Alkollerle ve aminlerle tepkimeleri:Tiyokarbonatlar ve ditiyokarbamatlar elde edilir.---Metallerle kompleksleşme:Özellikle bazik metallerle koordinasyon bileşikleri oluşturur."
        },
"CH3OH": {
    "Yapı": "Moleküler formülü: CH₄O ya da CH₃OH, Hidroksil grubu (-OH) içerir.",
    "Fiziksel Özellikler": "Berrak, renksiz, uçucu sıvı, Kaynama noktası: ~64.7°C, Erime noktası: -97.6°C, Su ile tamamen karışabilir.",
    "Kimyasal Özellikler": "Reaktif alkol, Zayıf asit ve baz özellikleri gösterir, Alkoller sınıfına ait.",
    "Toksik Etkiler": "Gözlerde yanma ve görme kaybı, Sinir sistemi hasarı, Metabolik asidoz, Karaciğer ve böbrek hasarı, Ölüm riski.",
    "Kullanım Alanları": "Çözücü, Yakıt, Kimyasal sentez, Metilasyon ajanı, Formaldehit ve plastik üretimi.",
    "Kimyasal Reaksiyonlar": "Yanma Tepkimesi: Metanol, oksijenle tepkimeye girerek karbondioksit ve su oluşturur. Bu tepkime enerji açığa çıkar. Aldehit Oluşumu: Metanol, oksidasyon tepkimeleri ile formaldehit (metanal) oluşturabilir. Estere Dönüşüm: Metanol, asitlerle tepkimeye girerek esterler oluşturabilir."
        },
        "C3H6": {
            "Yapı": "Kimyasal formülü: C₃H₆, üç karbonlu ve bir çift bağ içeren doymamış hidrokarbon, CH₂=CH-CH₃ yapısı.",
            "Fiziksel Özellikler": "Gaz halinde, Renksiz, Kaynama noktası: -47.6°C, Erime noktası: -185.2°C, Suda az çözünür.",
            "Kimyasal Özellikler": "Reaktif çift bağ, Polimerleşme yatkınlığı, Hidratasyon ve halojenleme reaksiyonları verir.",
            "Toksik Etkiler": "Solunum sistemi irritasyonu, Merkezi sinir sistemi etkileri, Göz ve cilt tahrişi.",
            "Kullanım Alanları": "Polipropilen üretimi, Propilen oksit üretimi, Yakıt katkısı, Sentetik fiber üretimi.",
            "Kimyasal Reaksiyonlar": "Hidrojenasyon (çift bağın indirgenmesi)---Halojenleme:Hidrohalojenleme---Polimerleşme: en önemli endüstriyel reaksiyon)---Oksidasyon Tepkimeleri:Yanma Tepkimesi:"
        
        },
        "C2H4": {
            "Yapı": "İki karbon atomu arasında bir çift bağ (C=C) bulunur. Her karbon atomu ayrıca iki hidrojen atomuna bağlanır. Düzlemsel geometriye sahiptir.",
            "Fiziksel Özellikler": "Gaz halinde (oda sıcaklığında). Renksiz, hafif tatlımsı kokusu vardır. Erime noktası: –169 °C, Kaynama noktası: –104 °C. Suda az çözünür, organik çözücülerde iyi çözünür.",
            "Kimyasal Özellikler": "Reaktif çift bağ içerir. Hidrojenasyon, polimerizasyon ve halojenasyon reaksiyonlarına girer. Alkenlerin karakteristik özelliklerini gösterir.",
            "Kimyasal Reaksiyonlar": "Hidratasyon: su ile tepkimeye girerek alkol (etanol) oluşturur. Oksidasyon: oksijenle tepkimeye girerek etilen oksit oluşturur. Polimerizasyon: polietilen oluşturur.",
            "Toksik Etkiler": "Yüksek konsantrasyonlarda solunum yolu irritasyonuna ve baş dönmesine neden olur. Merkezi sinir sistemi depresyonu. Uzun süreli maruziyette nörolojik etkiler.",
            "Kullanım Alanları": "Polietilen üretimi, Etilen glikol üretimi, Bitkisel hormon olarak kullanım, Meyvelerin olgunlaşmasını hızlandırma."
        },
        "H2O": {
            "Yapı": "Eğik (bent) geometri, Bağ açısı: 104.5°, Oksijen atomu 2 bağ yapar ve 2 yalnız elektron çifti içerir, Molekül polar yapıdadır.",
            "Fiziksel Özellikler": "Sıvı (oda sıcaklığında), Renksiz ve kokusuz, Erime Noktası: 0°C, Kaynama Noktası: 100°C, Yoğunluk: 1.00 g/cm³ (4°C'de), Yüksek yüzey gerilimi (~72 mN/m).",
            "Kimyasal Özellikler": "Amfoter madde (asit ve baz gibi davranabilir), Kovalent bağlı polar molekül, Zayıf şekilde kendi kendine iyonlaşabilir, Hidrojen bağı yapabilir.",
            "Kimyasal Reaksiyonlar": "Asit-baz reaksiyonları, Hidroliz reaksiyonları, Redoks tepkimeleri, Hidrat oluşumu, Suyun iyonlaşması.",
            "Toksik Etkiler": "Aşırı alımda hiponatremi (kan sodyum seviyesinin düşmesi), Yetersizlikte dehidrasyon, İnhalasyonda boğulma riski.",
            "Kullanım Alanları": "Yaşamsal önemi, Endüstriyel prosesler, Çözücü olarak, Enerji üretimi, Tarım, Temizlik ve hijyen."
        },
        "PH3": {
            "Yapı": "Piramidal geometri, Fosfor üç tek bağ yapar ve bir yalnız elektron çifti içerir, Bağ açısı ~93.5°, Polar molekül.",
            "Fiziksel Özellikler": "Gaz halinde (oda sıcaklığında), Renksiz, çürük balık kokusu, Kaynama noktası: -87.7°C, Erime noktası: -133.5°C, Suda az çözünür.",
            "Kimyasal Özellikler": "Zayıf bazik özellik gösterir, Redüksiyon özellik gösterir, Metal kompleksleri oluşturur.",
            "Kimyasal Reaksiyonlar": "Fosforun su ile tepkimesi, Fosfinin oksijenle reaksiyonu, Halojenlerle reaksiyon, Metallerle kompleks oluşumu.",
            "Toksik Etkiler": "Yüksek toksisiteli, Solunum yetmezliği riski, Sinir sistemi hasarı, Karaciğer ve böbrek hasarı.",
            "Kullanım Alanları": "Böcek öldürücü (fumigasyon), Fosfor bileşikleri üretimi, Metal işleme, Kimyasal sentezler."
        },
        "CH4": {
            "Yapı": "Moleküler formülü: CH₄, Tetrahedral yapı (4 bağ açısı 109,5°), Karbon ile dört hidrojen arasında tekli kovalent bağlar.",
            "Fiziksel Özellikler": "Gaz halinde (oda sıcaklığında), Renksiz ve kokusuz, Yoğunluğu havadan düşük, Erime noktası: -182.5°C, Kaynama noktası: -161.5°C.",
            "Kimyasal Özellikler": "Oldukça kararlı bir bileşik (C–H bağları güçlü), Yanıcı, oksijenle tepkimeye girerek CO₂ ve H₂O oluşturur, Halojenlerle reaksiyona girer.",
            "Kimyasal Reaksiyonlar": "Yanma tepkimesi, Radikal halojenleme (Cl₂ ve Br₂ ile), Isı ve ışıkla ayrışma (piroliz veya kraking).",
            "Toksik Etkiler": "Doğrudan toksik değil ancak yüksek konsantrasyonlarda boğulma riski, Sera gazı etkisi CO₂'den 25 kat daha güçlü.",
            "Kullanım Alanları": "Doğal gazın ana bileşeni (%85-90), Yakıt olarak kullanım (ısı ve enerji üretimi), Kimyasal sentezlerde başlangıç maddesi (metanol, formaldehit üretimi)."
        }
    }

    molekuller = [
        {
            "ad": "Amonyak",
            "kimyasal_formul": "NH3",
            "aciklama": "Amonyak, bir nitrojen ve üç hidrojen atomundan oluşur. Gübre üretiminde, temizlik malzemelerinde ve soğutucu akışkan olarak kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Amonyak.jpeg",
            "dosya_3d": "nh3.obj",
            "silinebilir": False,
            "ozellikler": ozellikler_txt.get("NH3", {})
        },
        {
            "ad": "Hidrojen",
            "kimyasal_formul": "H2",
            "aciklama": "Hidrojen, evrendeki en hafif ve en bol bulunan elementtir. Enerji üretiminde ve kimyasal reaksiyonlarda kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Hidrojen.jpeg",
            "dosya_3d": "H2.obj",
            "silinebilir": False,
            "ozellikler": ozellikler_txt.get("H2", {})
        },
        {
            "ad": "Oksijen",
            "kimyasal_formul": "O2",
            "aciklama": "Oksijen, iki oksijen atomundan oluşur. Solunum için gereklidir ve yanmayı destekler.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Oksijen.jpeg",
            "dosya_3d": "o2.obj",
            "silinebilir": False,
            "ozellikler": ozellikler_txt.get("O2", {})
        },
        {
            "ad": "Asetilen",
            "kimyasal_formul": "C2H2",
            "aciklama": "Asetilen, iki karbon atomu arasında üçlü bağ bulunan en basit alkin bileşiğidir. Metal kesme ve kaynak işlemlerinde yaygın olarak kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Asetilen.jpeg",
            "dosya_3d": "asetilen.obj",
            "silinebilir": False,
            "ozellikler": ozellikler_txt.get("C2H2", {})
        },
        {
            "ad": "Karbondioksit",
            "kimyasal_formul": "CO2",
            "aciklama": "Karbon dioksit, atmosferde bulunan ve fotosentezde kullanılan önemli bir gazdır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Karbondioksit.jpeg",
            "dosya_3d": "CO2.obj",
            "silinebilir": False,
            "ozellikler": ozellikler_txt.get("CO2", {})
        },
        {
            "ad": "Azot",
            "kimyasal_formul": "N2",
            "aciklama": "Azot, iki azot atomundan oluşur. Atmosferin yaklaşık %78'ini oluşturur ve canlılar için önemli bir elementtir.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Azot.jpeg",
            "dosya_3d": "n2.obj",
            "silinebilir": False,
            "ozellikler": ozellikler_txt.get("N2", {})
        },
        {
            "ad": "Karbon Monoksit",
            "kimyasal_formul": "CO",
            "aciklama": "Karbon monoksit, karbon ve oksijen atomları arasında üçlü bağ içeren doğrusal bir moleküldür.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/karbonmonoksit.jpeg",
            "dosya_3d": "karbon monoksit.obj",
            "silinebilir": False,
            "ozellikler": ozellikler_txt.get("CO", {})
        },
        {
            "ad": "Formaldehit",
            "kimyasal_formul": "CH2O",
            "aciklama": "Formaldehit, bir karbon, iki hidrojen ve bir oksijen atomundan oluşan aldehittir.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Formaldehit.jpeg",
            "dosya_3d": "formaldehit.obj",
            "silinebilir": False,
            "ozellikler": ozellikler_txt.get("CH2O", {})
        },
        {
            "ad": "Karbon Disülfür",
            "kimyasal_formul": "CS2",
            "aciklama": "Karbon disülfür, karbon ve kükürt atomları arasında çift bağ içeren doğrusal bir moleküldür.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/karbondisülfür.jpeg",
            "dosya_3d": "karbon disülfür.obj",
            "silinebilir": False,
            "ozellikler": ozellikler_txt.get("CS2", {})
        },
        {
            "ad": "Metanol",
            "kimyasal_formul": "CH3OH",
            "aciklama": "Metanol, bir karbon, üç hidrojen ve bir hidroksil grubu içeren basit bir alkoldür.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Metanol.jpeg",
            "dosya_3d": "metanol.obj",
            "silinebilir": False,
            "ozellikler": ozellikler_txt.get("CH3OH", {})
        },
        {
            "ad": "Propilen",
            "kimyasal_formul": "C3H6",
            "aciklama": "Propilen, üç karbonlu ve bir çift bağ içeren doymamış bir hidrokarbondur.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Propilen.jpeg",
            "dosya_3d": "propilen.obj",
            "silinebilir": False,
            "ozellikler": ozellikler_txt.get("C3H6", {})
        },
        {
            "ad": "Etilen",
            "kimyasal_formul": "C2H4",
            "aciklama": "Etilen, iki karbon atomu arasında bir çift bağ içeren basit bir alken bileşiğidir.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Etilen.jpeg",
            "dosya_3d": "etilen.obj",
            "silinebilir": False,
            "ozellikler": ozellikler_txt.get("C2H4", {})
        },
        {
            "ad": "Su",
            "kimyasal_formul": "H2O",
            "aciklama": "Su, bir oksijen ve iki hidrojen atomundan oluşan yaşam için temel bir moleküldür.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Su.jpeg",
            "dosya_3d": "H2O.obj",
            "silinebilir": False,
            "ozellikler": ozellikler_txt.get("H2O", {})
        },
        {
            "ad": "Fosfin",
            "kimyasal_formul": "PH3",
            "aciklama": "Fosfin, bir fosfor ve üç hidrojen atomundan oluşan toksik bir gazdır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Fosfin.jpeg",
            "dosya_3d": "fosfin.obj",
            "silinebilir": False,
            "ozellikler": ozellikler_txt.get("PH3", {})
        },
        {
            "ad": "Metan",
            "kimyasal_formul": "CH4",
            "aciklama": "Metan, bir karbon ve dört hidrojen atomundan oluşan en basit alkan bileşiğidir. Doğal gazın ana bileşenidir.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/CH4.jpeg.jpg",
            "dosya_3d": "CH4.obj",
            "silinebilir": False,
            "ozellikler": ozellikler_txt.get("CH4", {})
        },
        {
            "ad": "Benzen",
            "kimyasal_formul": "C6H6",
            "aciklama": "Benzen, altı karbon atomunun halka şeklinde dizildiği ve her karbona bir hidrojen bağlandığı aromatik bir hidrokarbondur.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Benzen.jpeg",
            "dosya_3d": "benzen.obj",
            "silinebilir": False,
            "ozellikler": ozellikler_txt.get("C6H6", {})
        }
    ]

    for molekul_data in molekuller:
        molekul = Molekul(
            ad=molekul_data["ad"],
            kimyasal_formul=molekul_data["kimyasal_formul"],
            aciklama=molekul_data["aciklama"],
            tur=molekul_data["tur"],
            dosya_3d=molekul_data["dosya_3d"],
            silinebilir=molekul_data.get("silinebilir", False)
        )
        db.session.add(molekul)
        db.session.commit()

        yapisal_gorunum = MolekulYapisi(
            resim_url=molekul_data["yapisal_resim_url"],
            molekul_id=molekul.id
        )
        db.session.add(yapisal_gorunum)

        # Varsayılan özellikleri ekle
        for baslik, deger in molekul_data.get("ozellikler", {}).items():
            ozellik = Ozellik(
                tanim=f"{baslik}: {deger}",
                molekul_id=molekul.id,
                aktif=True,
                silinebilir=False
            )
            db.session.add(ozellik)

        # Her molekül için 3 yeni silinebilir özellik ekle
        ek_ozellikler = {
            "NH3": [
                "Endüstriyel Üretim: Haber-Bosch prosesi ile yüksek basınç ve sıcaklıkta azot ve hidrojenden üretilir.",
                "Depolama: Sıvılaştırılmış formda basınçlı tanklarda saklanır.",
                "Çevresel Etki: Atmosfere salındığında asit yağmurlarına katkıda bulunabilir."
            ],
            "H2": [
                "Depolama Yöntemleri: Sıvı hidrojen, metal hidritler veya basınçlı tanklarda depolanır.",
                "İzotoplar: Döteryum (D₂) ve Trityum (T₂) gibi izotopları nükleer uygulamalarda kullanılır.",
                "Enerji Yoğunluğu: Birim kütle başına en yüksek enerji içeriğine sahip yakıttır."
            ],
            "O2": [
                "Sıvı Oksijen: Roket yakıtı olarak kullanılır ve kriojenik uygulamalarda önemlidir.",
                "Atmosferik Önemi: Ozon tabakasının oluşumunda ve stratosferik kimyada rol oynar.",
                "Biyolojik Rol: ATP üretiminde elektron alıcı olarak görev yapar."
            ],
            "C2H2": [
                "Endüstriyel Üretim: Kalsiyum karbürün su ile reaksiyonundan elde edilir.",
                "Güvenlik: Patlamaya karşı özel güvenlik önlemleri gerektirir.",
                "Alternatif İsimler: Etin olarak da bilinir ve alkin serisinin ilk üyesidir."
            ],
            "CO2": [
                "Süperkritik Özellikler: 31°C üzerinde süperkritik akışkan olarak davranır.",
                "Jeolojik Depolama: Yeraltı formasyonlarında karbon yakalama ve depolama için kullanılır.",
                "pH Etkisi: Suda çözündüğünde pH'ı düşürür ve asidik özellik gösterir."
            ],
            "N2": [
                "Kriyojenik Uygulamalar: Sıvı azot -196°C'de soğutucu olarak kullanılır.",
                "Biyolojik Döngü: Azot döngüsünün temel bileşenidir.",
                "Endüstriyel Saflaştırma: Hava ayırma ünitelerinde üretilir."
            ],
            "CO": [
                "Sensör Teknolojisi: CO dedektörleri güvenlik sistemlerinde yaygın kullanılır.",
                "Endüstriyel Sentez: Metanol ve asetik asit üretiminde temel hammaddedir.",
                "Uzay Kimyası: Yıldızlararası ortamda yaygın bulunur."
            ],
            "CH2O": [
                "Sterilizasyon: Tıbbi aletlerin sterilizasyonunda kullanılır.",
                "Doğal Oluşum: Volkanik gazlarda ve orman yangınlarında oluşur.",
                "Metabolizma: Vücutta bir karbon kaynağı olarak metabolize edilir."
            ],
            "CS2": [
                "Ekstraksiyon: Yağ ekstraksiyonunda çözücü olarak kullanılır.",
                "Optik Özellikler: Yüksek kırılma indisine sahiptir.",
                "Endüstriyel Kullanım: Selüloz üretiminde önemli rol oynar."
            ],
            "CH3OH": [
                "Biyoyakıt: Yenilenebilir enerji kaynağı olarak kullanılır.",
                "Antifriz Özelliği: Düşük donma noktası nedeniyle soğutucu sistemlerde kullanılır.",
                "Alternatif Yakıt: Direkt metanol yakıt hücrelerinde kullanılır."
            ],
            "C3H6": [
                "Kopolimer Üretimi: Etilen ile kopolimer oluşturabilir.",
                "Ekonomik Değer: Petrokimya endüstrisinin önemli ara ürünüdür.",
                "İzomerizasyon: Siklopropan ile izomerdir."
            ],
            "C2H4": [
                "Meyve Olgunlaşması: Doğal bitki hormonu olarak işlev görür.",
                "Polimerizasyon Kinetiği: Ziegler-Natta katalizörleri ile polimerleşir.",
                "Endüstriyel Üretim: Steam cracking ile üretilir."
            ],
            "H2O": [
                "Anomali: 4°C'de maksimum yoğunluğa ulaşır.",
                "İzotop Kompozisyonu: D₂O (ağır su) nükleer reaktörlerde kullanılır.",
                "Süperkritik Su: 374°C ve 218 atm üzerinde süperkritik akışkan olur."
            ],
            "PH3": [
                "Yarı İletken Üretimi: Elektronik endüstrisinde katkılama maddesi olarak kullanılır.",
                "Biyolojik Oluşum: Anaerobik bakteriler tarafından üretilebilir.",
                "Uzay Kimyası: Venüs atmosferinde tespit edilmiştir."
            ],
            "CH4": [
                "Hidrat Oluşumu: Doğal gaz hidratları deniz tabanında bulunur.",
                "Atmosferik Kimya: Hidroksil radikalleri ile reaksiyona girer.",
                "Biyogaz Üretimi: Anaerobik fermantasyon ile üretilir."
            ],
            "C6H6": [
                "Moleküler Orbital: Hückel kuralına uyar ve 6 π elektronu içerir.",
                "Tarihsel Önemi: Kekulé'nin rüyasında yapısını keşfettiği rivayet edilir.",
                "Endüstriyel Dönüşüm: Alkilbenzen üretiminde temel hammaddedir."
            ]
        }

        # Yeni özellikleri ekle
        for yeni_ozellik in ek_ozellikler.get(molekul_data["kimyasal_formul"], []):
            ozellik = Ozellik(
                tanim=f"{yeni_ozellik}",
                molekul_id=molekul.id,
                aktif=True,
                silinebilir=True  # Bu özellikler silinebilir
            )
            db.session.add(ozellik)

    db.session.commit()
    print("Veritabanı başarıyla oluşturuldu ve veriler eklendi.")
