from app import app, db, Molekul, Ozellik, MolekulYapisi, MolekulGorunumu

with app.app_context():
    # Veritabanını temizle (Eğer gerekliyse)
    db.drop_all()
    db.create_all()

    # Moleküller ve detaylı özellikleri
    molekuller = [
        {
            "ad": "Su",
            "kimyasal_formul": "H2O",
            "aciklama": "Su, yaşamın temel taşıdır. İki hidrojen ve bir oksijen atomundan oluşur. Polar yapısı sayesinde birçok maddeyi çözer ve canlılar için hayati bir çözücüdür.",
            "tur": "kovalent",
            "yapisal_resim_url": "data:image/png;base64,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",
            "normal_resim_url": "https://img.freepik.com/free-photo/fresh-water-texture-background-transparent-liquid_53876-142911.jpg?ga=GA1.1.609453277.1743772929&semt=ais_hybrid&w=740",
            "dosya_3d": "h2o.obj",  # 3D dosya adı
            "ozellikler": ["Polar", "Çözücü", "Yüksek yüzey gerilimi", "Isı kapasitesi yüksek", "Donduğunda hacmi artar"]
        },
        {
            "ad": "Karbon Dioksit",
            "kimyasal_formul": "CO2",
            "aciklama": "Karbon dioksit, bir karbon ve iki oksijen atomundan oluşur. Fotosentezde kullanılır ve solunum sonucu açığa çıkar.",
            "tur": "kovalent",
            "yapisal_resim_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxZIqito71b6kRkUCIuEczspZg7p1_VuOvtQ&s",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/images/o2_structure.jpg",
            "normal_resim_url": "/static/images/o2.jpg",
            "dosya_3d": "co2.obj",  # 3D dosya adı
            "ozellikler": ["Diatomik", "Renksiz", "Kokusuz", "Solunum için gerekli", "Yanıcı maddeleri destekler"]
        },
        {
            "ad": "Azot",
            "kimyasal_formul": "N2",
            "aciklama": "Azot, iki azot atomundan oluşur. Atmosferin yaklaşık %78'ini oluşturur ve canlılar için önemli bir elementtir.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/images/n2_structure.jpg",
            "normal_resim_url": "/static/images/n2.jpg",
            "dosya_3d": "n2.obj",  # 3D dosya adı
            "ozellikler": ["Diatomik", "Renksiz", "Kokusuz", "Atmosferde bol bulunur", "Reaktif değildir"]
        },
        {
            "ad": "Hidrojen",
            "kimyasal_formul": "H2",
            "aciklama": "Hidrojen, evrendeki en hafif ve en bol bulunan elementtir. Enerji üretiminde ve kimyasal reaksiyonlarda kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/images/h2_structure.jpg",
            "normal_resim_url": "/static/images/h2.jpg",
            "dosya_3d": "h2.obj",  # 3D dosya adı
            "ozellikler": ["Diatomik", "Renksiz", "Kokusuz", "Yanıcı", "Enerji kaynağı"]
        },
        {
            "ad": "Metan",
            "kimyasal_formul": "CH4",
            "aciklama": "Metan, bir karbon ve dört hidrojen atomundan oluşur. Doğal gazın ana bileşenidir ve enerji kaynağı olarak kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/images/ch4_structure.jpg",
            "normal_resim_url": "/static/images/ch4.jpg",
            "dosya_3d": "ch4.obj",  # 3D dosya adı
            "ozellikler": ["Yanıcı", "Renksiz", "Kokusuz", "Sera gazı", "Doğal gazın ana bileşeni"]
        },
        {
            "ad": "Amonyak",
            "kimyasal_formul": "NH3",
            "aciklama": "Amonyak, bir nitrojen ve üç hidrojen atomundan oluşur. Gübre üretiminde, temizlik malzemelerinde ve soğutucu akışkan olarak kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/images/nh3_structure.jpg",
            "normal_resim_url": "/static/images/nh3.jpg",
            "dosya_3d": "nh3.obj",  # 3D dosya adı
            "ozellikler": ["Bazik", "Keskin kokulu", "Suda çözünür", "Gübre üretiminde kullanılır", "Temizlik malzemelerinde kullanılır"]
        },
        {
            "ad": "Etanol",
            "kimyasal_formul": "C2H5OH",
            "aciklama": "Etanol, iki karbon, altı hidrojen ve bir oksijen atomundan oluşur. Alkol olarak bilinir ve içeceklerde, yakıtlarda ve çözücü olarak kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/images/c2h5oh_structure.jpg",
            "normal_resim_url": "/static/images/c2h5oh.jpg",
            "dosya_3d": "c2h5oh.obj",  # 3D dosya adı
            "ozellikler": ["Yanıcı", "Renksiz", "Suda çözünür", "Alkol", "Çözücü"]
        },
        {
            "ad": "Asetik Asit",
            "kimyasal_formul": "CH3COOH",
            "aciklama": "Asetik asit, sirkenin ana bileşenidir. Gıda endüstrisinde ve laboratuvarlarda kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/images/ch3cooh_structure.jpg",
            "normal_resim_url": "/static/images/ch3cooh.jpg",
            "dosya_3d": "ch3cooh.obj",  # 3D dosya adı
            "ozellikler": ["Asidik", "Keskin kokulu", "Suda çözünür", "Sirkenin ana bileşeni", "Gıda endüstrisinde kullanılır"]
        },
        {
            "ad": "Etilen",
            "kimyasal_formul": "C2H4",
            "aciklama": "Etilen, iki karbon ve dört hidrojen atomundan oluşur. Plastik üretiminde kullanılır ve bitkisel hormon olarak görev yapar.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/images/c2h4_structure.jpg",
            "normal_resim_url": "/static/images/c2h4.jpg",
            "dosya_3d": "c2h4.obj",  # 3D dosya adı
            "ozellikler": ["Yanıcı", "Renksiz", "Tatlı kokulu", "Plastik üretiminde kullanılır", "Bitkisel hormon"]
        },
        {
            "ad": "Hidrojen Peroksit",
            "kimyasal_formul": "H2O2",
            "aciklama": "Hidrojen peroksit, iki hidrojen ve iki oksijen atomundan oluşur. Dezenfektan olarak ve ağartıcı olarak kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/images/h2o2_structure.jpg",
            "normal_resim_url": "/static/images/h2o2.jpg",
            "dosya_3d": "h2o2.obj",  # 3D dosya adı
            "ozellikler": ["Oksitleyici", "Renksiz", "Keskin kokulu", "Dezenfektan", "Ağartıcı"]
        },
        {
            "ad": "Metanol",
            "kimyasal_formul": "CH3OH",
            "aciklama": "Metanol, bir karbon, dört hidrojen ve bir oksijen atomundan oluşur. Çözücü ve yakıt olarak kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/images/ch3oh_structure.jpg",
            "normal_resim_url": "/static/images/ch3oh.jpg",
            "dosya_3d": "ch3oh.obj",  # 3D dosya adı
            "ozellikler": ["Yanıcı", "Renksiz", "Çözücü", "Yakıt", "Toksik"]
        },
        {
            "ad": "Formaldehit",
            "kimyasal_formul": "CH2O",
            "aciklama": "Formaldehit, bir karbon, iki hidrojen ve bir oksijen atomundan oluşur. Endüstride ve biyolojik örneklerin korunmasında kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/images/ch2o_structure.jpg",
            "normal_resim_url": "/static/images/ch2o.jpg",
            "dosya_3d": "ch2o.obj",  # 3D dosya adı
            "ozellikler": ["Keskin kokulu", "Renksiz", "Toksik", "Dezenfektan", "Endüstride kullanılır"]
        },
        {
            "ad": "Asetilen",
            "kimyasal_formul": "C2H2",
            "aciklama": "Asetilen, iki karbon ve iki hidrojen atomundan oluşur. Kaynak işlemlerinde ve kimyasal sentezlerde kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/images/c2h2_structure.jpg",
            "normal_resim_url": "/static/images/c2h2.jpg",
            "dosya_3d": "c2h2.obj",  # 3D dosya adı
            "ozellikler": ["Yanıcı", "Renksiz", "Tatlı kokulu", "Kaynak işlemlerinde kullanılır", "Kimyasal sentez"]
        },
        {
            "ad": "Propilen",
            "kimyasal_formul": "C3H6",
            "aciklama": "Propilen, üç karbon ve altı hidrojen atomundan oluşur. Polipropilen plastik üretiminde kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/images/c3h6_structure.jpg",
            "normal_resim_url": "/static/images/c3h6.jpg",
            "dosya_3d": "c3h6.obj",  # 3D dosya adı
            "ozellikler": ["Yanıcı", "Renksiz", "Hafif kokulu", "Polipropilen üretiminde kullanılır", "Petrokimya"]
        },
        {
            "ad": "Fosfin",
            "kimyasal_formul": "PH3",
            "aciklama": "Fosfin, bir fosfor ve üç hidrojen atomundan oluşur. Zehirli bir gazdır ve yarı iletken endüstrisinde kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/images/ph3_structure.jpg",
            "normal_resim_url": "/static/images/ph3.jpg",
            "dosya_3d": "ph3.obj",  # 3D dosya adı
            "ozellikler": ["Zehirli", "Renksiz", "Keskin kokulu", "Yarı iletken endüstrisinde kullanılır", "Yanıcı"]
        },
        {
            "ad": "Karbon Monoksit",
            "kimyasal_formul": "CO",
            "aciklama": "Karbon monoksit, bir karbon ve bir oksijen atomundan oluşur. Zehirli bir gazdır ve yanma süreçlerinde oluşur.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/images/co_structure.jpg",
            "normal_resim_url": "/static/images/co.jpg",
            "dosya_3d": "co.obj",  # 3D dosya adı
            "ozellikler": ["Zehirli", "Renksiz", "Kokusuz", "Yanma ürünü", "Toksik"]
        },
        {
            "ad": "Heksan",
            "kimyasal_formul": "C6H14",
            "aciklama": "Heksan, altı karbon ve on dört hidrojen atomundan oluşur. Çözücü olarak ve endüstride kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/images/c6h14_structure.jpg",
            "normal_resim_url": "/static/images/c6h14.jpg",
            "dosya_3d": "c6h14.obj",  # 3D dosya adı
            "ozellikler": ["Yanıcı", "Renksiz", "Çözücü", "Endüstride kullanılır", "Toksik"]
        },
        {
            "ad": "Karbon Disülfür",
            "kimyasal_formul": "CS2",
            "aciklama": "Karbon disülfür, bir karbon ve iki kükürt atomundan oluşur. Çözücü olarak ve kimyasal sentezlerde kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/images/cs2_structure.jpg",
            "normal_resim_url": "/static/images/cs2.jpg",
            "dosya_3d": "cs2.obj",  # 3D dosya adı
            "ozellikler": ["Yanıcı", "Renksiz", "Keskin kokulu", "Çözücü", "Kimyasal sentez"]
        },
        {
            "ad": "Fosfor Pentaklorür",
            "kimyasal_formul": "PCl5",
            "aciklama": "Fosfor pentaklorür, bir fosfor ve beş klor atomundan oluşur. Kimyasal sentezlerde kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/images/pcl5_structure.jpg",
            "normal_resim_url": "/static/images/pcl5.jpg",
            "dosya_3d": "pcl5.obj",  # 3D dosya adı
            "ozellikler": ["Renksiz", "Toksik", "Kimyasal sentez", "Reaktif", "Endüstride kullanılır"]
        },
        {
            "ad": "Diklorin Monoksit",
            "kimyasal_formul": "Cl2O",
            "aciklama": "Diklorin monoksit, iki klor ve bir oksijen atomundan oluşur. Dezenfektan olarak kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/images/cl2o_structure.jpg",
            "normal_resim_url": "/static/images/cl2o.jpg",
            "dosya_3d": "cl2o.obj",  # 3D dosya adı
            "ozellikler": ["Keskin kokulu", "Renksiz", "Dezenfektan", "Reaktif", "Kimyasal sentez"]
        },
        {
            "ad": "Azot Triyodür",
            "kimyasal_formul": "NI3",
            "aciklama": "Azot triyodür, bir azot ve üç iyot atomundan oluşur. Patlayıcı bir bileşiktir.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/images/ni3_structure.jpg",
            "normal_resim_url": "/static/images/ni3.jpg",
            "dosya_3d": "ni3.obj",  # 3D dosya adı
            "ozellikler": ["Patlayıcı", "Koyu renkli", "Reaktif", "Kimyasal sentez", "Toksik"]
        },
        {
            "ad": "Kükürt Hexaflorür",
            "kimyasal_formul": "SF6",
            "aciklama": "Kükürt hexaflorür, bir kükürt ve altı flor atomundan oluşur. Elektrik yalıtımında kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/images/sf6_structure.jpg",
            "normal_resim_url": "/static/images/sf6.jpg",
            "dosya_3d": "sf6.obj",  # 3D dosya adı
            "ozellikler": ["Renksiz", "Kokusuz", "Elektrik yalıtımı", "Sera gazı", "Kimyasal stabilite"]
        },
        {
            "ad": "Karbon Tetraklorür",
            "kimyasal_formul": "CCl4",
            "aciklama": "Karbon tetraklorür, bir karbon ve dört klor atomundan oluşur. Çözücü olarak kullanılır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/images/ccl4_structure.jpg",
            "normal_resim_url": "/static/images/ccl4.jpg",
            "dosya_3d": "ccl4.obj",  # 3D dosya adı
            "ozellikler": ["Renksiz", "Toksik", "Çözücü", "Yanıcı değil", "Endüstride kullanılır"]
        },
        {
            "ad": "Hidrojen Siyanür",
            "kimyasal_formul": "HCN",
            "aciklama": "Hidrojen siyanür, bir hidrojen, bir karbon ve bir azot atomundan oluşur. Zehirli bir gazdır.",
            "tur": "kovalent",
            "yapisal_resim_url": "/static/images/hcn_structure.jpg",
            "normal_resim_url": "/static/images/hcn.jpg",
            "dosya_3d": "hcn.obj",  # 3D dosya adı
            "ozellikler": ["Zehirli", "Renksiz", "Keskin kokulu", "Kimyasal sentez", "Endüstride kullanılır"]
        },
        {
        "ad": "Dimetil Eter",
        "kimyasal_formul": "CH3OCH3",
        "aciklama": "Dimetil eter, iki metil grubunun bir oksijen atomuyla bağlanmasıyla oluşur. Yakıt olarak ve kimyasal sentezlerde kullanılır.",
        "tur": "kovalent",
        "yapisal_resim_url": "/static/images/ch3och3_structure.jpg",
        "normal_resim_url": "/static/images/ch3och3.jpg",
        "dosya_3d": "ch3och3.obj",  # 3D dosya adı
        "ozellikler": ["Yanıcı", "Renksiz", "Tatlı kokulu", "Yakıt", "Kimyasal sentez"]
        }

    ]
    

    # Molekülleri ve özellikleri veritabanına ekle
    for molekul_data in molekuller:
        molekul = Molekul(
            ad=molekul_data["ad"],
            kimyasal_formul=molekul_data["kimyasal_formul"],
            aciklama=molekul_data["aciklama"],
            tur=molekul_data["tur"],
            dosya_3d=molekul_data["dosya_3d"]  # 3D dosya adı
        )
        db.session.add(molekul)
        db.session.commit()  # Molekülü kaydet ve ID al

        # Yapısal görünüm resmi ekle
        yapisal_gorunum = MolekulYapisi(
            resim_url=molekul_data["yapisal_resim_url"],
            molekul_id=molekul.id
        )
        db.session.add(yapisal_gorunum)

        # Normal görünüm resmi ekle
        normal_gorunum = MolekulGorunumu(
            resim_url=molekul_data["normal_resim_url"],
            molekul_id=molekul.id
        )
        db.session.add(normal_gorunum)

        # Özellikleri ekle
        for ozellik_tanim in molekul_data["ozellikler"]:
            ozellik = Ozellik(tanim=ozellik_tanim, molekul_id=molekul.id)
            db.session.add(ozellik)

    db.session.commit()
    print("Veritabanı başarıyla oluşturuldu ve veriler eklendi.")
