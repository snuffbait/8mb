self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', e => e.waitUntil(self.clients.matchAll().then(() => self.clients.claim())));
self.addEventListener('fetch', e => {
  e.respondWith(fetch(e.request).then(r => {
    const headers = new Headers(r.headers);
    headers.set('Cross-Origin-Opener-Policy', 'same-origin');
    headers.set('Cross-Origin-Embedder-Policy', 'require-corp');
    return new Response(r.body, { status: r.status, statusText: r.statusText, headers });
  }));
});
