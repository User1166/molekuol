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
            "yapisal_resim_url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxAQEhUPEBAWFhUVFxUWGBAVGBcVFRUQFxcWFxYaFRgYHSggGBolGxUYIjEhJSkrLy4uFx8zODMtNygtLisBCgoKDg0OGxAQGy0lHyYtLy0wLy0rLS0tLy0rLS0tLy0vLS0tLS0wLy8tLS0tLS8tLS0vLy0tLS0tLS0tLS0vLf/AABEIALUBFgMBEQACEQEDEQH/xAAcAAEAAgIDAQAAAAAAAAAAAAAABgcEBQECAwj/xABDEAABAwICBgcFBAgFBQAAAAABAAIDBBEFIQYSMUFRYQcTIjJxgZEUQlKhwSNykrEVU2KCotHh8DNDc7LSJDVUY9P/xAAaAQEAAwEBAQAAAAAAAAAAAAAAAwQFAgEG/8QANREBAAIBAgMECAUEAwEAAAAAAAECAwQREiExBUFR8BMyYXGBobHRFCKRweEjM0JSNLLxFf/aAAwDAQACEQMRAD8AvFAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBBhYhitPTi80rWcie0fBozPkF3THa/qwjvlpT1p2aCp0/o2mzGyv5taAP43A/JWK6PJPXaFW3aGKOm8+faxx0iwb4Jf4P8AkuvwVvGHH/0af6z8vuzqPTmik7znx/6jfqwuA9VHbSZI9qWmuxW68vf5lIKaqjlbrxva9vxNIcPkq9qzWdpWq2i0b1nd7Lx0ICAgICAgICAgICAgICAgICAgICAgICAgICAg8qioZG0yPcGtaLlxyAHNexEzO0PLWisbz0V/jmmk0xMVGCxv623bcOIvkwfPwWhi0taxvdlZtba88OPlHj3/AMNBHhtzrSvLnHM53JPNxzKs8fdCrGPfnaXZ7qdmWqCeQ1j6lIi8kzSrxfXM3Qjzt/JdejnxcTkjweD52HbEB4Ej6L3hmO9zNonucU1W+F3WQSPY7iD+e5w5EJakWja0blbzSd6TsnmjWm7ZSIaqzHnISjJjjwcPdPyPLYs7NpJrzp0aun10W/LflPimiptAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQcPcACSbAZknYAgqzSTG318vVxm0DDkPit77voPqtXDhjFXeerE1Gec9uGPV883gAyFvAfNxXfO0uOVIaypq3Py2D4R9eKnrSIQWvMvCyk2cFk2ebuLLzZ64IXmw4IXOwnmgmkxJFHO652RSHabe4478th8uCz9Vg2/PX4tXRamZ/p3+H2TxUGmICAgICAgICAgICAgICAgICAgICAgICAghvSNixjjbSsPalzdbaIhlb945eAKuaPHvbinuZ+vzcNeCO/6IrTRCJmfi48/7yVyZ4pUaxww1VROZHXPkOAVitdoV7W4pc0tO+V7Y42lznGwaN5/vNd2mKxxT0c1rNpitesprFotR0jBJXy3J9wEtbfg0N7Tz/dlnzqsuW22GPP0acaTDirxZp8/WXH6UwXZ7Nl8XV/1uvfQ6v/b5vPTaP/X5O8mjFDVsMlDLquHu3c5tzue13aZ/eRXP4nNittljz9Hv4TDmrvhnz8ecITV0z4nuikbquabFp4/Uc1oVtFo4o6M21ZpM1t1Y5C8l44BIIINiCCCNoIzBHO65mN3sTtzXFovi3tdOyY97uvHCRuR9cj4OCxM2PgvMPocGX0lIs2yjTCAgICAgICAgICAgICAgICAgICAgICAgqjHaj2ivkdtDDqDkI+zb8dz5rWxV4cUe392Hmtx55nw/b+WDi02xg8T9P78FNijvQ5bdzACsQgT3QejZBTyV8o2h1jvETNtuZcPkFm6y83yRir5mWroaRjxzmt5iEQxTEJKmV00hzOwbmt3NHIf1WlixVx1itWZly2y24rMSyl2RszCMRfTStmZfLvN+JnvNP97bKLNijJSaylw5rYrxaG503rqWodHLA/WeAWvGq5t27WntAbDceap6PHkxxNbxyW9bkxZJi1J5osVblRdCuJepl0XVlpZqcnJwEgHNp1XHzDmeiztbXlFmp2ffnNfj5+SxlQaggICAgICAgICAgICAgICAgICAgICAgIKbw460krjtJJ83OJK2bcqxD5+nO0ywql+s9x5n0GQ/JT0jaIQ3neZdFLCOViY83qsKYwb2QNJ82uPrY+qy9P8Am1cz72xqI4NHFfd+yvwtmGK5sunjgriXTqVzL11K4l66FcS9bzo/favZzbIPLVv+bQqWr/tyvaH+7HuW2sttCAgICAgICAgICAgICAgICAgICAgICAgpyibqTSxnaHOHm15C2Z51iXz9eV7R56tZdWIV3YKSHixcZvNhLHtzIZC4j7paH+mf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",
            "normal_resim_url": "data:image/jpeg;base64,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",
            "dosya_3d": "co2.obj",  # 3D dosya adı
            "ozellikler": ["Diatomik", "Renksiz", "Kokusuz", "Solunum için gerekli", "Yanıcı maddeleri destekler"]
        },
        {
            "ad": "Azot",
            "kimyasal_formul": "N2",
            "aciklama": "Azot, iki azot atomundan oluşur. Atmosferin yaklaşık %78'ini oluşturur ve canlılar için önemli bir elementtir.",
            "tur": "kovalent",
            "yapisal_resim_url": "data:image/jpeg;base64,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",
            "normal_resim_url": "data:image/jpeg;base64,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",
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
