from app import app, db, Molekul, Ozellik, MolekulYapisi

with app.app_context():
    # Veritabanını temizle (Eğer gerekliyse)
    db.drop_all()
    db.create_all()

    # Moleküller ve detaylı özellikleri
    molekuller = [
        {
            "ad": "Amonyak",
            "kimyasal_formul": "NH3",
            "aciklama": "Amonyak, bir nitrojen ve üç hidrojen atomundan oluşur. Gübre üretiminde, temizlik malzemelerinde ve soğutucu akışkan olarak kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Amonyak.jpeg",
            "dosya_3d": "nh3.obj",
            "ozellikler": ["Bazik", "Keskin kokulu", "Suda çözünür", "Gübre üretiminde kullanılır", "Temizlik malzemelerinde kullanılır"],
            "silinebilir": False  # Varsayılan moleküller silinemez
        },
        {
            "ad": "Asetilen",
            "kimyasal_formul": "C2H2",
            "aciklama": "Asetilen, iki karbon ve iki hidrojen atomundan oluşur. Kaynak işlemlerinde ve kimyasal sentezlerde kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Asetilen.jpeg",
            "dosya_3d": "asetilen.obj",
            "ozellikler": ["Yanıcı", "Renksiz", "Tatlı kokulu", "Kaynak işlemlerinde kullanılır", "Kimyasal sentez"],
            "silinebilir": False
        },
        {
            "ad": "Azot",
            "kimyasal_formul": "N2",
            "aciklama": "Azot, iki azot atomundan oluşur. Atmosferin yaklaşık %78'ini oluşturur ve canlılar için önemli bir elementtir.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Azot.jpeg",
            "dosya_3d": "n2.obj",
            "ozellikler": ["Diatomik", "Renksiz", "Kokusuz", "Atmosferde bol bulunur", "Reaktif değildir"],
            "silinebilir": False
        },
        {
            "ad": "Benzen",
            "kimyasal_formul": "C6H6",
            "aciklama": "Benzen, altı karbon ve altı hidrojen atomundan oluşur. Endüstride çözücü olarak kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Benzen.jpeg",
            "dosya_3d": "benzen.obj",
            "ozellikler": ["Renksiz", "Tatlı kokulu", "Çözücü", "Yanıcı", "Endüstride kullanılır"],
            "silinebilir": False
        },
        {
            "ad": "Metan",
            "kimyasal_formul": "CH4",
            "aciklama": "Metan, bir karbon ve dört hidrojen atomundan oluşur. Doğal gazın ana bileşenidir ve enerji kaynağı olarak kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/CH4.jpeg.jpg",
            "dosya_3d": "CH4.obj",
            "ozellikler": ["Yanıcı", "Renksiz", "Kokusuz", "Sera gazı", "Doğal gazın ana bileşeni"],
            "silinebilir": False
        },
        {
            "ad": "Etilen",
            "kimyasal_formul": "C2H4",
            "aciklama": "Etilen, iki karbon ve dört hidrojen atomundan oluşur. Plastik üretiminde kullanılır ve bitkisel hormon olarak görev yapar.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Etilen.jpeg",
            "dosya_3d": "etilen.obj",
            "ozellikler": ["Yanıcı", "Renksiz", "Tatlı kokulu", "Plastik üretiminde kullanılır", "Bitkisel hormon"],
            "silinebilir": False
        },
        {
            "ad": "Formaldehit",
            "kimyasal_formul": "CH2O",
            "aciklama": "Formaldehit, bir karbon, iki hidrojen ve bir oksijen atomundan oluşur. Endüstride ve biyolojik örneklerin korunmasında kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Formaldehit.jpeg",
            "dosya_3d": "formaldehit.obj",
            "ozellikler": ["Keskin kokulu", "Renksiz", "Toksik", "Dezenfektan", "Endüstride kullanılır"],
            "silinebilir": False
        },
        {
            "ad": "Fosfin",
            "kimyasal_formul": "PH3",
            "aciklama": "Fosfin, bir fosfor ve üç hidrojen atomundan oluşur. Zehirli bir gazdır ve yarı iletken endüstrisinde kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Fosfin.jpeg",
            "dosya_3d": "fosfin.obj",
            "ozellikler": ["Zehirli", "Renksiz", "Keskin kokulu", "Yarı iletken endüstrisinde kullanılır", "Yanıcı"],
            "silinebilir": False
        },
        {
            "ad": "Hidrojen",
            "kimyasal_formul": "H2",
            "aciklama": "Hidrojen, evrendeki en hafif ve en bol bulunan elementtir. Enerji üretiminde ve kimyasal reaksiyonlarda kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Hidrojen.jpeg",
            "dosya_3d": "H2.obj",
            "ozellikler": ["Diatomik", "Renksiz", "Kokusuz", "Yanıcı", "Enerji kaynağı"],
            "silinebilir": False
        },
        {
            "ad": "Karbon Dioksit",
            "kimyasal_formul": "CO2",
            "aciklama": "Karbon dioksit, bir karbon ve iki oksijen atomundan oluşur. Fotosentezde kullanılır ve solunum sonucu açığa çıkar.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Karbon dioksit.jpeg",
            "dosya_3d": "CO2.obj",
            "ozellikler": ["Diatomik", "Renksiz", "Kokusuz", "Solunum için gerekli", "Yanıcı maddeleri destekler"],
            "silinebilir": False
        },
        {
            "ad": "Karbon Disülfür",
            "kimyasal_formul": "CS2",
            "aciklama": "Karbon disülfür, bir karbon ve iki kükürt atomundan oluşur. Çözücü olarak ve kimyasal sentezlerde kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/karbon disülfür.jpeg",
            "dosya_3d": "karbon disülfür.obj",
            "ozellikler": ["Yanıcı", "Renksiz", "Keskin kokulu", "Çözücü", "Kimyasal sentez"],
            "silinebilir": False
        },
        {
            "ad": "Karbon Monoksit",
            "kimyasal_formul": "CO",
            "aciklama": "Karbon monoksit, bir karbon ve bir oksijen atomundan oluşur. Zehirli bir gazdır ve yanma süreçlerinde oluşur.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/karbon monoksit.jpeg",
            "dosya_3d": "karbon monoksit.obj",
            "ozellikler": ["Zehirli", "Renksiz", "Kokusuz", "Yanma ürünü", "Toksik"],
            "silinebilir": False
        },
        {
            "ad": "Metanol",
            "kimyasal_formul": "CH3OH",
            "aciklama": "Metanol, bir karbon, dört hidrojen ve bir oksijen atomundan oluşur. Çözücü ve yakıt olarak kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Metanol.jpeg",
            "dosya_3d": "metanol.obj",
            "ozellikler": ["Yanıcı", "Renksiz", "Çözücü", "Yakıt", "Toksik"],
            "silinebilir": False
        },
        {
            "ad": "Oksijen",
            "kimyasal_formul": "O2",
            "aciklama": "Oksijen, iki oksijen atomundan oluşur. Solunum için gereklidir ve yanmayı destekler.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Oksijen.jpeg",
            "dosya_3d": "o2.obj",
            "ozellikler": ["Diatomik", "Renksiz", "Kokusuz", "Solunum için gerekli", "Yanmayı destekler"],
            "silinebilir": False
        },
        {
            "ad": "Propilen",
            "kimyasal_formul": "C3H6",
            "aciklama": "Propilen, üç karbon ve altı hidrojen atomundan oluşur. Polipropilen plastik üretiminde kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Propilen.jpeg",
            "dosya_3d": "propilen.obj",
            "ozellikler": ["Yanıcı", "Renksiz", "Hafif kokulu", "Polipropilen üretiminde kullanılır", "Petrokimya"],
            "silinebilir": False
        },
        {
            "ad": "Su",
            "kimyasal_formul": "H2O",
            "aciklama": "Su, yaşamın temel taşıdır. İki hidrojen ve bir oksijen atomundan oluşur. Polar yapısı sayesinde birçok maddeyi çözer ve canlılar için hayati bir çözücüdür.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/2d/Su.jpeg",
            "dosya_3d": "H2O.obj",
            "ozellikler": ["Polar", "Çözücü", "Yüksek yüzey gerilimi", "Isı kapasitesi yüksek", "Donduğunda hacmi artar"],
            "silinebilir": False
        }
    ]

    # Molekülleri ve özellikleri veritabanına ekle
    for molekul_data in molekuller:
        molekul = Molekul(
            ad=molekul_data["ad"],
            kimyasal_formul=molekul_data["kimyasal_formul"],
            aciklama=molekul_data["aciklama"],
            tur=molekul_data["tur"],
            dosya_3d=molekul_data["dosya_3d"],
            silinebilir=molekul_data.get("silinebilir", False)  # Varsayılan olarak False
        )
        db.session.add(molekul)
        db.session.commit()

        # Yapısal görünüm resmi ekle
        yapisal_gorunum = MolekulYapisi(
            resim_url=molekul_data["yapisal_resim_url"],
            molekul_id=molekul.id
        )
        db.session.add(yapisal_gorunum)

        # Özellikleri ekle
        for ozellik_tanim in molekul_data["ozellikler"]:
            ozellik = Ozellik(
                tanim=ozellik_tanim, 
                molekul_id=molekul.id,
                aktif=True,
                silinebilir=False  # Varsayılan özellikler silinemez
            )
            db.session.add(ozellik)
        
        # Her moleküle 2 yeni silinebilir özellik ekle
        ekstra_ozellikler = {
            "NH3": ["Soğutma sistemlerinde kullanılır", "Endüstriyel üretimde önemlidir"],
            "C2H2": ["Metalurjide kullanılır", "Yüksek ısıda yanma özelliği"],
            "N2": ["Gıda paketlemede kullanılır", "Kriyojenik uygulamalarda kullanılır"],
            "C6H6": ["Organik sentezde kullanılır", "Petrokimya endüstrisinde önemli"],
            "CH4": ["Biyogaz üretiminde bulunur", "Atmosferde doğal olarak bulunur"],
            "C2H4": ["Meyvelerin olgunlaşmasını sağlar", "Polietilen üretiminde kullanılır"],
            "CH2O": ["Laboratuvarlarda koruyucu", "Tekstil endüstrisinde kullanılır"],
            "PH3": ["Elektronik endüstrisinde kullanılır", "Böcek ilacı olarak kullanılır"],
            "H2": ["Yakıt hücrelerinde kullanılır", "Metalurjide indirgeyici"],
            "CO2": ["İçeceklerde karbonatlayıcı", "Yangın söndürücülerde kullanılır"],
            "CS2": ["Selüloz üretiminde kullanılır", "Böcek ilacı yapımında kullanılır"],
            "CO": ["Metalurjide indirgeyici", "Kimyasal sentezlerde kullanılır"],
            "CH3OH": ["Antifriz olarak kullanılır", "Biyodizel üretiminde kullanılır"],
            "O2": ["Medikal kullanımda önemli", "Metalurjide kullanılır"],
            "C3H6": ["Sentetik fiber üretiminde kullanılır", "Organik sentezde önemli"],
            "H2O": ["Endüstriyel soğutucu", "Enerji üretiminde kullanılır"]
        }
        
        for ozellik in ekstra_ozellikler[molekul.kimyasal_formul]:
            yeni_ozellik = Ozellik(
                tanim=ozellik,
                molekul_id=molekul.id,
                aktif=True,
                silinebilir=True
            )
            db.session.add(yeni_ozellik)

    db.session.commit()
    print("Veritabanı başarıyla oluşturuldu ve veriler eklendi.")
