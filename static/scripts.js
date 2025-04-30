// Karanlık tema anlık beyazlığı engellemek için
(function() {
    try {
        const theme = localStorage.getItem('theme');
        if (theme === 'dark' || (!theme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            document.documentElement.classList.add('dark-theme');
        }
        // Sayfa yüklendikten sonra görünür yap
        document.addEventListener('DOMContentLoaded', () => {
            document.documentElement.classList.add('ready');
        });
    } catch (e) {
        console.error('Tema yüklenirken hata:', e);
    }
})();

function searchMolecule() {
    const query = document.getElementById('search-input').value.toLowerCase().trim();
    if (query) {
        // Arama sorgusunu URL parametresi olarak "Tüm Moleküller" sayfasına yönlendir
        window.location.href = `/tum_molekuller?search=${encodeURIComponent(query)}`;
    }
}

document.getElementById('search-input').addEventListener('keypress', function (event) {
    if (event.key === 'Enter') {
        searchMolecule();
    }
});

document.getElementById('search-input').addEventListener('input', function () {
    const query = this.value.toLowerCase().trim();
    if (query.length > 1) {
        fetch(`/api/arama_onerileri?q=${encodeURIComponent(query)}`)
            .then(response => response.json())
            .then(data => {
                const suggestions = data.map(item => `<li>${item}</li>`).join('');
                document.getElementById('search-suggestions').innerHTML = `<ul>${suggestions}</ul>`;
            });
    } else {
        document.getElementById('search-suggestions').innerHTML = '';
    }
});

function toggleTheme() {
    document.body.classList.toggle('dark-theme');
    localStorage.setItem('theme', document.body.classList.contains('dark-theme') ? 'dark' : 'light');
}

