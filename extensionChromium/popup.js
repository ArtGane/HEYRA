document.addEventListener('DOMContentLoaded', function() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        const url = tabs[0].url;
        const urlObject = new URL(url);
        
        // Récupérer le nom de domaine
        const domainName = urlObject.hostname;

        // Afficher le nom de domaine
        document.getElementById('url').textContent = `Nom de domaine : ${domainName}`;
        
        // Événement pour copier le nom de domaine
        document.getElementById('copy').addEventListener('click', function() {
            navigator.clipboard.writeText(domainName)
                .then(() => {
                    console.log('Nom de domaine copié dans le presse-papiers');
                })
                .catch(err => {
                    console.error('Erreur lors de la copie :', err);
                });
        });
    });
});
