class Gempa:

  # Konstruktor
  def _init_(self, lokasi, skala, dampak):
    self.lokasi = lokasi
    self.skala = skala
    self.dampak = dampak

  # Method / Perilaku pada class
  def lokasi(self, lokasi):
    lokasi = self.lokasi
    print("Lokasi di = %s" %(self.lokasi))
    
  def skala(self, skala):
    skala = self.skala
    print("Terjadi Gempa Dengan Skala = %s"
          %(self.skala))
    
  def dampak(self, dampak):
    dampak = self.dampak
    print("Dampak Kerusakan = %s" %(self.dampak))
    
  def cetak(self):
    print(
        "===================",
        "\nLokasi Di\t\t:", self.lokasi,
        "\nDengan Skala\t\t:", self.skala,
        "\nDampak Kerusakan\t:", self.dampak,
        "\n==================="
    )
    
gempa1 = Gempa("Banten", 1.2, "Tidak Berasa")
gempa2 = Gempa("Palu", 6.1, "Bangunan Roboh dan Berpotensi Tsunami")
gempa3 = Gempa("Cianjur", 5.6, "Bangunan Roboh")
gempa4 = Gempa("Jayapura", 3.3, "Bangunan Retak-retak")
gempa5 = Gempa("Garut", 4.0, "Bangunan Retak-retak")

gempa1.cetak()
gempa2.cetak()
gempa3.cetak()
gempa4.cetak()
gempa5.cetak()