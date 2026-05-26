# Aplikasi CLI - To-Do List
# Project Individu - KKA

class TodoList:
    def __init__(aplikasi, nama, user):
        aplikasi.nama = nama
        aplikasi.user = user
        aplikasi.daftar_tugas = []

    def tampil_menu(aplikasi):
        print("\n==============================")
        print(f"  {aplikasi.nama} {aplikasi.user}")
        print("==============================")
        print("1. Tambah Tugas")
        print("2. Lihat Semua Tugas")
        print("3. Tandai Tugas Selesai")
        print("4. Hapus Tugas")
        print("5. Keluar")
        print("==============================")

    def tambah_tugas(aplikasi):
        print("\n-- Tambah Tugas Baru --")

        tugas = input("Masukkan tugas: ")

        # operator comparison - cek string kosong
        if tugas == "":
            print("Tugas tidak boleh kosong!")
            return

        # buat dictionary untuk 1 tugas
        item_tugas = {
            "id": len(aplikasi.daftar_tugas) + 1,
            "nama": tugas,
            "selesai": False,
        }

        aplikasi.daftar_tugas.append(item_tugas)
        print(f"Tugas '{tugas}' berhasil ditambahkan!")

    def lihat_tugas(aplikasi):
        print("\n-- Daftar Tugas --")

        # comparison - cek list kosong
        if len(aplikasi.daftar_tugas) == 0:
            print("Belum ada tugas. Tambahkan tugas baru!")
            return

        # looping dengan for
        for tugas in aplikasi.daftar_tugas:
            status = "SELESAI" if tugas["selesai"] else "BELUM"
            print(f"{tugas['id']}. {tugas['nama']} [{status}]")

    def tandai_selesai(aplikasi):
        print("\n-- Tandai Tugas Selesai --")

        # comparison - cek list kosong
        if len(aplikasi.daftar_tugas) == 0:
            print("Tidak ada tugas untuk ditandai selesai!")
            return

        aplikasi.lihat_tugas()

        try:
            id_tugas = int(input("\nMasukkan nomor tugas: "))

            # comparison - validasi id
            if id_tugas < 1 or id_tugas > len(aplikasi.daftar_tugas):
                print("Nomor tugas tidak valid!")
                return

            # logical operator - cek if tugas sudah selesai
            if aplikasi.daftar_tugas[id_tugas - 1]["selesai"] == True:
                print("Tugas ini sudah ditandai selesai sebelumnya.")
            else:
                aplikasi.daftar_tugas[id_tugas - 1]["selesai"] = True
                print(
                    f"Tugas '{aplikasi.daftar_tugas[id_tugas - 1]['nama']}' ditandai selesai!"
                )

        except Exception:
            print("Input harus berupa angka!")

    def hapus_tugas(aplikasi):
        print("\n-- Hapus Tugas --")

        # comparison - cek list kosong
        if len(aplikasi.daftar_tugas) == 0:
            print("Tidak ada tugas untuk dihapus!")
            return

        aplikasi.lihat_tugas()

        try:
            id_tugas = int(input("\nMasukkan nomor tugas yang ingin dihapus: "))

            # comparison - validasi id
            if id_tugas < 1 or id_tugas > len(aplikasi.daftar_tugas):
                print("Nomor tugas tidak valid!")
                return

            nama_tugas = aplikasi.daftar_tugas[id_tugas - 1]["nama"]
            aplikasi.daftar_tugas.pop(id_tugas - 1)

            # update ulang id setelah dihapus
            for i in range(len(aplikasi.daftar_tugas)):
                aplikasi.daftar_tugas[i]["id"] = i + 1

            print(f"Tugas '{nama_tugas}' berhasil dihapus!")

        except Exception:
            print("Input harus berupa angka!")

    def jalankan(aplikasi):
        print("Selamat datang di To-Do List!")

        jalan = True

        while jalan:
            aplikasi.tampil_menu()
            pilihan = input("Pilih menu (1-5): ")

            # if else untuk navigasi menu
            if pilihan == "1":
                aplikasi.tambah_tugas()
            elif pilihan == "2":
                aplikasi.lihat_tugas()
            elif pilihan == "3":
                aplikasi.tandai_selesai()
            elif pilihan == "4":
                aplikasi.hapus_tugas()
            elif pilihan == "5":
                print("\nTerima kasih sudah menggunakan To-Do List. Sampai jumpa!")
                jalan = False
            else:
                print("Pilihan tidak valid, coba lagi.")


# ===================== PROGRAM UTAMA =====================

if __name__ == "__main__":
    app = TodoList("To-Do List", "sulthan")
    app.jalankan()

