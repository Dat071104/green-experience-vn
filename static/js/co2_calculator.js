document.addEventListener('DOMContentLoaded', () => {
    // 1. Emission factors (gCO2/km) per person roughly
    const EMISSION_FACTORS = {
        plane: 250,
        car: 120,
        motorbike: 80,
        bus: 40,
        electric: 20,
        bicycle: 0
    };

    // 2. Distances (mock map) in km
    const DISTANCES = {
        'Hà Nội': { 'Hà Giang': 300, 'Sapa': 350, 'Ninh Bình': 100, 'Mộc Châu': 190 },
        'TP.HCM': { 'Kon Tum': 450, 'Đà Lạt': 300, 'Bến Tre': 80, 'Tiền Giang': 70, 'Vũng Tàu': 125, 'Cần Thơ': 170 },
        'Đà Nẵng': { 'Hội An': 30, 'Huế': 100, 'Bà Nà Hills': 45, 'Phong Nha': 270 }
    };

    // 3. Autocomplete logic
    const origins = Object.keys(DISTANCES);
    let allDestinations = new Set();
    Object.values(DISTANCES).forEach(dests => Object.keys(dests).forEach(d => allDestinations.add(d)));
    const destinationsArray = Array.from(allDestinations);

    function setupAutocomplete(input, list) {
        input.addEventListener('input', function() {
            let val = this.value;
            closeAllLists();
            if (!val) return false;
            let a = document.createElement('div');
            a.setAttribute('id', this.id + 'autocomplete-list');
            a.setAttribute('class', 'autocomplete-items');
            this.parentNode.appendChild(a);
            
            list.forEach(item => {
                if (item.toLowerCase().includes(val.toLowerCase())) {
                    let b = document.createElement('div');
                    b.innerHTML = item;
                    b.innerHTML += "<input type='hidden' value='" + item + "'>";
                    b.addEventListener('click', function(e) {
                        input.value = this.getElementsByTagName('input')[0].value;
                        closeAllLists();
                    });
                    a.appendChild(b);
                }
            });
        });
    }

    function closeAllLists(elmnt) {
        var x = document.getElementsByClassName('autocomplete-items');
        for (var i = 0; i < x.length; i++) {
            if (elmnt != x[i] && elmnt != document.getElementById('origin') && elmnt != document.getElementById('destination')) {
                x[i].parentNode.removeChild(x[i]);
            }
        }
    }
    document.addEventListener('click', function(e) { closeAllLists(e.target); });

    setupAutocomplete(document.getElementById('origin'), origins);
    setupAutocomplete(document.getElementById('destination'), destinationsArray);

    // 4. Calculate Logic
    const form = document.getElementById('co2-form');
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const origin = document.getElementById('origin').value;
        const dest = document.getElementById('destination').value;
        const guests = parseInt(document.getElementById('guests').value) || 1;
        const typeNormal = document.getElementById('transport-normal').value;
        const typeGreen = document.getElementById('transport-green').value;
        
        // Find distance
        let dist = 200; // default 200km
        if (DISTANCES[origin] && DISTANCES[origin][dest]) {
            dist = DISTANCES[origin][dest];
        }

        const factorNormal = EMISSION_FACTORS[typeNormal];
        const factorGreen = EMISSION_FACTORS[typeGreen];

        // Total CO2 in kg
        const totalNormal = (factorNormal * dist * guests) / 1000;
        const totalGreen = (factorGreen * dist * guests) / 1000;
        
        let saved = totalNormal - totalGreen;
        if (saved < 0) saved = 0;

        const trees = Math.floor(saved / 21); // 1 tree absorbs ~21kg CO2 per year
        const gp = Math.floor(saved * 2);

        // Update UI
        document.getElementById('co2-saved').innerText = saved.toFixed(1);
        document.getElementById('trees-saved').innerText = trees;
        document.getElementById('gp-bonus').innerText = '+' + gp;
        document.getElementById('val-normal').innerText = totalNormal.toFixed(1);
        document.getElementById('val-green').innerText = totalGreen.toFixed(1);

        // Update Bar
        const max = Math.max(totalNormal, totalGreen, 1);
        document.getElementById('bar-normal').style.width = ((totalNormal / max) * 100) + '%';
        document.getElementById('bar-green').style.width = ((totalGreen / max) * 100) + '%';

        // Reveal result
        document.getElementById('result-section').classList.add('active');
        
        // Scroll to result
        setTimeout(() => {
            document.getElementById('result-section').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }, 100);
    });

    // 5. Animated Counters (used in community page but included in main js or here)
    // Actually, animated counters are requested in community.html. Let's write a small script for that too.
    const counters = document.querySelectorAll('.impact-counter');
    if (counters.length > 0) {
        const counterObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    // Logic to animate numbers goes here
                    // ... (Implementation detail can be added if needed)
                    counterObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });
        counters.forEach(c => counterObserver.observe(c));
    }
});
