
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('js/service_worker.js')
        .then((registration) => {
            console.log('Service Worker registrado con éxito:', registration);
        })
        .catch((error) => {
            console.error('Error al registrar el Service Worker:', error);
        });
}