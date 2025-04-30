from flask import Flask, render_template, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///molekul.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Molekül Modeli
class Molekul(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ad = db.Column(db.String(100), nullable=False)
    kimyasal_formul = db.Column(db.String(20), unique=True, nullable=False)
    aciklama = db.Column(db.Text, nullable=False)
    tur = db.Column(db.String(50), nullable=True)  # "iyonik", "kovalent" veya "metalik"
    resim_url = db.Column(db.String(200), nullable=True)  # Molekül resmi için URL
    dosya_3d = db.Column(db.String(200), nullable=True)  # 3D dosya adı
    silinebilir = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Molekul {self.ad}>'

# Özellik Modeli
class Ozellik(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tanim = db.Column(db.String(100), nullable=False)
    molekul_id = db.Column(db.Integer, db.ForeignKey('molekul.id'), nullable=False)
    molekul = db.relationship('Molekul', backref=db.backref('ozellikler', lazy=True))
    aktif = db.Column(db.Boolean, default=True)
    silinebilir = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Ozellik {self.tanim}>'

# Molekül Yapısal Görünüm Tablosu
class MolekulYapisi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resim_url = db.Column(db.String(200), nullable=False)  # Yapısal görünüm resmi için URL
    molekul_id = db.Column(db.Integer, db.ForeignKey('molekul.id'), nullable=False)
    molekul = db.relationship('Molekul', backref=db.backref('yapisal_gorunum', lazy=True))

    def __repr__(self):
        return f'<MolekulYapisi {self.resim_url}>'

# Molekül Normal Görünüm Tablosu
class MolekulGorunumu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resim_url = db.Column(db.String(200), nullable=False)  # Normal görünüm resmi için URL
    molekul_id = db.Column(db.Integer, db.ForeignKey('molekul.id'), nullable=False)
    molekul = db.relationship('Molekul', backref=db.backref('normal_gorunum', lazy=True))

    def __repr__(self):
        return f'<MolekulGorunumu {self.resim_url}>'

# Anasayfa
@app.route('/')
def index():
    tum_molekuller = Molekul.query.all()
    return render_template('index.html', tum_molekuller=tum_molekuller)

# Tüm Moleküller Sayfası
@app.route('/tum_molekuller')
def tum_molekuller():
    search_query = request.args.get('search', '').lower()
    tum_molekuller = Molekul.query.all()

    if search_query:
        tum_molekuller = [
            molekul for molekul in tum_molekuller
            if search_query in molekul.ad.lower() or
               search_query in molekul.kimyasal_formul.lower() or
               search_query in molekul.aciklama.lower()
        ]

    return render_template('tum_molekuller.html', tum_molekuller=tum_molekuller, search_query=search_query)

# Molekül Detay Sayfası
@app.route('/molekul/<kimyasal_formul>')
def molekul_detay(kimyasal_formul):
    molekul = Molekul.query.filter_by(kimyasal_formul=kimyasal_formul).first()
    if molekul:
        ozellikler = molekul.ozellikler  # Molekülün özelliklerini al
        return render_template('molekul.html', molekul=molekul, ozellikler=ozellikler)
    else:
        return "Molekül bulunamadı!"

# Molekül 3D Görselleştirme API
@app.route('/api/3d/<kimyasal_formul>')
def api_3d_molekul(kimyasal_formul):
    molekul = Molekul.query.filter_by(kimyasal_formul=kimyasal_formul).first()
    if molekul and molekul.dosya_3d:
        return jsonify({'dosya_3d': url_for('static', filename=f'3d/{molekul.dosya_3d}', _external=True)})
    return jsonify({'error': '3D dosyası bulunamadı!'}), 404

# Tüm Moleküller API
@app.route('/api/molekuller')
def api_molekuller():
    molekuller = Molekul.query.all()
    molekul_listesi = []
    for molekul in molekuller:
        molekul_listesi.append({
            'ad': molekul.ad,
            'kimyasal_formul': molekul.kimyasal_formul,
            'aciklama': molekul.aciklama,
            'tur': molekul.tur
        })
    return jsonify(molekul_listesi)

# Molekül Karşılaştırma Sayfası
@app.route('/karsilastir')
def karsilastir():
    molekuller = Molekul.query.all()
    return render_template('karsilastir.html', molekuller=molekuller)

# Molekül Karşılaştırma API
@app.route('/api/karsilastir', methods=['POST'])
def api_karsilastir():
    data = request.json
    molekul1 = Molekul.query.filter_by(id=data.get('molekul1_id')).first()
    molekul2 = Molekul.query.filter_by(id=data.get('molekul2_id')).first()
    if molekul1 and molekul2:
        return jsonify({
            'molekul1': {
                'ad': molekul1.ad,
                'kimyasal_formul': molekul1.kimyasal_formul,
                'ozellikler': [oz.tanim for oz in molekul1.ozellikler]
            },
            'molekul2': {
                'ad': molekul2.ad,
                'kimyasal_formul': molekul2.kimyasal_formul,
                'ozellikler': [oz.tanim for oz in molekul2.ozellikler]
            }
        })
    return jsonify({'error': 'Molekül bulunamadı!'}), 404

# Molekül 3D Görselleştirme Sayfası
@app.route('/3d/<kimyasal_formul>')
def goruntule_3d(kimyasal_formul):
    molekul = Molekul.query.filter_by(kimyasal_formul=kimyasal_formul).first()
    if molekul:
        return render_template('3d.html', molekul=molekul)
    return "Molekül bulunamadı!", 404

# Arama Önerileri API
@app.route('/api/arama_onerileri')
def arama_onerileri():
    query = request.args.get('q', '').lower()
    if query:
        molekuller = Molekul.query.filter(Molekul.ad.ilike(f'%{query}%')).all()
        return jsonify([molekul.ad for molekul in molekuller])
    return jsonify([])

# Özellik Ekleme API
@app.route('/api/ozellik/ekle', methods=['POST'])
def ozellik_ekle():
    data = request.json
    molekul_id = data.get('molekul_id')
    tanim = data.get('tanim')
    
    if not all([molekul_id, tanim]):
        return jsonify({'error': 'Eksik bilgi'}), 400
        
    yeni_ozellik = Ozellik(
        tanim=tanim,
        molekul_id=molekul_id,
        aktif=True,
        silinebilir=True
    )
    db.session.add(yeni_ozellik)
    db.session.commit()
    
    return jsonify({
        'id': yeni_ozellik.id,
        'tanim': yeni_ozellik.tanim,
        'silinebilir': yeni_ozellik.silinebilir
    })

# Özellik Gizleme API
@app.route('/api/ozellik/gizle/<int:ozellik_id>', methods=['POST'])
def ozellik_gizle(ozellik_id):
    ozellik = Ozellik.query.get_or_404(ozellik_id)
    
    if not ozellik.silinebilir:
        return jsonify({'error': 'Bu özellik silinemez'}), 403
        
    ozellik.aktif = False
    db.session.commit()
    
    return jsonify({'success': True})

# Özellikleri Sıfırlama API
@app.route('/api/ozellik/sifirla/<int:molekul_id>', methods=['POST'])
def ozellik_sifirla(molekul_id):
    molekul = Molekul.query.get_or_404(molekul_id)
    
    # Tüm özellikleri getir
    ozellikler = Ozellik.query.filter_by(molekul_id=molekul_id).all()
    
    for ozellik in ozellikler:
        if ozellik.silinebilir:
            # Silinebilir özellikleri sil
            db.session.delete(ozellik)
        else:
            # Varsayılan özellikleri aktifleştir
            ozellik.aktif = True
    
    db.session.commit()
    return jsonify({'success': True})

# Hakkında Sayfası
@app.route('/hakkinda')
def hakkinda():
    return render_template('hakkinda.html')

# İletişim Sayfası
@app.route('/iletisim')
def iletisim():
    return render_template('iletisim.html')

# Navigasyon linkleri
nav_links = [
    {'url': '/', 'text': 'Ana Sayfa'},
    {'url': '/tum_molekuller', 'text': 'Tüm Moleküller'},
]

# Template context processor
@app.context_processor
def inject_nav_links():
    return dict(nav_links=nav_links)

if __name__ == '__main__':
    app.run(debug=True)
