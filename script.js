// script.js
const contactForm = document.getElementById('contactForm');

// Mencegah pengiriman form bawaan dan melakukan validasi
contactForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Mencegah halaman reload

    // Mengambil nilai input dan menghapus spasi berlebih
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();

    // Validasi dasar
    if (name === "" || email === "" || message === "") {
        alert("Peringatan: Semua kolom harus diisi dengan benar!");
        return;
    }

    // Simulasi pengiriman pesan
    alert(`Terima kasih ${name}! Pesan Anda telah tervalidasi dan siap dikirim ke database.`);
    
    // Reset form setelah "terkirim"
    contactForm.reset();
});