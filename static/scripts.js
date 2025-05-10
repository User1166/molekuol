// Karanlık tema anlık beyazlığı engellemek için
(function() {
    try {
        const theme = localStorage.getItem('theme');
        if (theme === 'dark' || (!theme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            document.documentElement.classList.add('dark-theme');
        }
        document.addEventListener('DOMContentLoaded', () => {
            document.documentElement.classList.add('ready');
        });
    } catch (e) {
        console.error('Tema yüklenirken hata:', e);
    }
})();

function searchMolecule() {
    const input = document.getElementById('search-input');
    if (!input) return;
    const query = input.value.toLowerCase().trim();
    if (query) {
        window.location.href = `/tum_molekuller?search=${encodeURIComponent(query)}`;
    }
}

const searchInput = document.getElementById('search-input');
if (searchInput) {
    searchInput.addEventListener('keypress', function (event) {
        if (event.key === 'Enter') searchMolecule();
    });

    searchInput.addEventListener('input', function () {
        const query = this.value.toLowerCase().trim();
        const suggestionsBox = document.getElementById('search-suggestions');
        if (!suggestionsBox) return;
        if (query.length > 1) {
            fetch(`/api/arama_onerileri?q=${encodeURIComponent(query)}`)
                .then(r => r.json())
                .then(data => {
                    suggestionsBox.innerHTML = data.length
                        ? `<ul>${data.map(item => `<li>${item}</li>`).join('')}</ul>`
                        : '';
                });
        } else {
            suggestionsBox.innerHTML = '';
        }
    });
}

function toggleTheme() {
    document.body.classList.toggle('dark-theme');
    localStorage.setItem('theme', document.body.classList.contains('dark-theme') ? 'dark' : 'light');
}

