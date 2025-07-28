// service-worker.js
const CACHE_NAME = 'mi-cache';
const urlsToCache = [
    'css/content_1.css',
    'css/font.css',
    'css/global.css',
    'css/navbar.css',
    'css/section_1.css',
    'fondos/01.avif',
    'fondos/02.avif',
    'fondos/03.avif',
    'fotos/01.avif',
    'fotos/02.avif',
    'fotos/03.avif',
    'fotos/04.avif',
    'fotos/05.avif'
    // Agrega aquí más URLs de los recursos que deseas almacenar en caché
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => cache.addAll(urlsToCache))
            .then(() => self.skipWaiting()) // Permite que el nuevo Service Worker se active de inmediato
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
            .then((response) => response || fetch(event.request))
    );
});

self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys()
            .then((cacheNames) => {
                return Promise.all(
                    cacheNames.filter((name) => name !== CACHE_NAME)
                        .map((name) => caches.delete(name))
                );
            })
            .then(() => self.clients.claim()) // Reclama el control de las páginas abiertas por el Service Worker anterior
    );
});
