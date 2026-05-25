document.addEventListener('DOMContentLoaded', () => {
    const btnNext1 = document.getElementById('btn-next-1');
    const btnPrev2 = document.getElementById('btn-prev-2');
    
    const step1 = document.getElementById('step-1');
    const step2 = document.getElementById('step-2');
    
    const ind1 = document.getElementById('indicator-1');
    const ind2 = document.getElementById('indicator-2');
    
    if (btnNext1) {
        btnNext1.addEventListener('click', () => {
            step1.classList.remove('active');
            step2.classList.add('active');
            
            ind1.classList.add('active'); // keep it active
            ind2.classList.add('active');
            
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
    
    if (btnPrev2) {
        btnPrev2.addEventListener('click', () => {
            step2.classList.remove('active');
            step1.classList.add('active');
            
            ind2.classList.remove('active');
        });
    }
});
