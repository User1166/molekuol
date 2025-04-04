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

// Tema durumu yerel depolamadan yüklenir
if (localStorage.getItem('theme') === 'dark') {
    document.body.classList.add('dark-theme');
}

function compareMolecules() {
    const molekul1Id = document.getElementById('molekul1').value;
    const molekul2Id = document.getElementById('molekul2').value;

    fetch('/api/karsilastir', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ molekul1_id: molekul1Id, molekul2_id: molekul2Id })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('comparison-result').innerText = data.error;
        } else {
            const result = `
                <h2>Karşılaştırma Sonuçları</h2>
                <div>
                    <h3>${data.molekul1.ad} (${data.molekul1.kimyasal_formul})</h3>
                    <ul>${data.molekul1.ozellikler.map(oz => `<li>${oz}</li>`).join('')}</ul>
                </div>
                <div>
                    <h3>${data.molekul2.ad} (${data.molekul2.kimyasal_formul})</h3>
                    <ul>${data.molekul2.ozellikler.map(oz => `<li>${oz}</li>`).join('')}</ul>
                </div>
            `;
            document.getElementById('comparison-result').innerHTML = result;
        }
    });
}
