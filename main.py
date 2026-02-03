saldo = 0
riwayat_pemasukan = []
riwayat_pengeluaran = []

def tambah_pemasukan():
    global saldo, riwayat_pemasukan
    jumlah = int(input("Masukkan jumlah pemasukan: "))
    keterangan = input("Keterangan (misal: gaji): ")
    saldo = saldo + jumlah
    riwayat_pemasukan.append({"keterangan": keterangan, "jumlah": jumlah})
    print(f"✅ Pemasukan berhasil ditambahkan! Saldo sekarang: Rp{saldo:,}")
    print()

def tambah_pengeluaran():
    global saldo, riwayat_pengeluaran
    jumlah = int(input("Masukkan jumlah pengeluaran: "))
    keterangan = input("Keterangan pengeluaran (misal: makan): ")
    if jumlah > saldo:
        print("⚠️ Peringatan: Saldo tidak cukup!")
        print(f"Saldo Anda: Rp{saldo:,}, Pengeluaran: Rp{jumlah:,}")
    else:
        saldo = saldo - jumlah
        riwayat_pengeluaran.append({"keterangan": keterangan, "jumlah": jumlah})
        print(f"✅ Pengeluaran berhasil! Saldo sekarang: Rp{saldo:,}")
    print()

def lihat_saldo():
    print("\n" + "┌" + "─"*58 + "┐")
    print("│" + " "*15 + "💰 SALDO ANDA" + " "*30 + "│")
    print("├" + "─"*58 + "┤")
    print(f"│  Rp{saldo:>53,}" + " │")
    print("└" + "─"*58 + "┘\n")

def lihat_ringkasan():
    print("\n" + "┌" + "─"*58 + "┐")
    print("│" + " "*14 + "📊 RINGKASAN KEUANGAN" + " "*22 + "│")
    print("├" + "─"*58 + "┤")
    
    # Hitung total pemasukan dan pengeluaran
    total_pemasukan = sum(p["jumlah"] for p in riwayat_pemasukan)
    total_pengeluaran = sum(p["jumlah"] for p in riwayat_pengeluaran)
    
    # Tabel ringkasan
    print(f"│ {'KETERANGAN':<27} {'JUMLAH':>27} │")
    print("├" + "─"*58 + "┤")
    print(f"│ {'💵 Total Pemasukan':<27} {'Rp' + str(total_pemasukan):>25,} │")
    print(f"│ {'💸 Total Pengeluaran':<27} {'Rp' + str(total_pengeluaran):>25,} │")
    print("├" + "─"*58 + "┤")
    print(f"│ {'💰 SALDO AKHIR':<27} {'Rp' + str(saldo):>25,} │")
    print("└" + "─"*58 + "┘\n")

def lihat_riwayat_pengeluaran():
    print("\n" + "┌" + "─"*58 + "┐")
    print("│" + " "*16 + "📊 RIWAYAT PENGELUARAN" + " "*20 + "│")
    print("├" + "─"*58 + "┤")
    
    if not riwayat_pengeluaran:
        print("│" + " "*18 + "📭 Belum ada pengeluaran" + " "*16 + "│")
    else:
        print(f"│ {'No':<3} {'Keterangan':<20} {'Jumlah':>27} │")
        print("├" + "─"*58 + "┤")
        for i, transaksi in enumerate(riwayat_pengeluaran, 1):
            emoji_map = {
                "makan": "🍔",
                "transportasi": "🚗",
                "belanja": "🛍️",
                "hiburan": "🎮",
                "lainnya": "❓"
            }
            key = "lainnya"
            for kata in emoji_map.keys():
                if kata in transaksi["keterangan"].lower():
                    key = kata
                    break
            emoji = emoji_map[key]
            desc = f"{emoji} {transaksi['keterangan']}"[:20]
            print(f"│ {i:<3} {desc:<20} {'Rp' + str(transaksi['jumlah']):>25,} │")
        print("├" + "─"*58 + "┤")
        total = sum(p["jumlah"] for p in riwayat_pengeluaran)
        print(f"│ {'TOTAL':<23} {'Rp' + str(total):>25,} │")
    
    print("└" + "─"*58 + "┘\n")

def menu():
    print("\n🏦 === APLIKASI PENGELOLA UANG SAKU ===")
    print("1. ➕ Tambah pemasukan")
    print("2. ➖ Tambah pengeluaran")
    print("3. 💰 Lihat saldo")
    print("4. 📊 Lihat ringkasan keuangan")
    print("5. 📋 Lihat riwayat pengeluaran")
    print("6. 🚪 Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "4":
        lihat_ringkasan()
    elif pilihan == "5":
        lihat_riwayat_pengeluaran()
    elif pilihan == "6":
        print("\n👋 Terima kasih! Sampai jumpa lagi!")
        break
    else:
        print("❌ Pilihan tidak valid")