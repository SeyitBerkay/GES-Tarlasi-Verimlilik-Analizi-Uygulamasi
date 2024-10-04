import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class GESTarlasiVerimlilikAnalizi:
    def __init__(self):
        self.veriler = None
        self.kurulu_guc = 0
        self.panel_alani = 0
        self.kayip_faktoru = 0

    def veri_yukle(self):
        # Gerçek bir uygulamada, bu fonksiyon CSV veya veritabanından veri yükleyebilir
        # Şimdilik örnek veri oluşturacağız
        tarihler = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
        uretim = np.random.normal(loc=5000, scale=1000, size=len(tarihler))  # kWh
        isinim = np.random.normal(loc=5, scale=1, size=len(tarihler))  # kWh/m²
        self.veriler = pd.DataFrame({
            'Tarih': tarihler,
            'Uretim': uretim,
            'Isinim': isinim
        })

    def parametreleri_al(self):
        print("GES Tarlası Parametrelerini Girin:")
        self.kurulu_guc = float(input("Kurulu güç (kWp): "))
        self.panel_alani = float(input("Toplam panel alanı (m²): "))
        self.kayip_faktoru = float(input("Sistem kayıp faktörü (örn. 0.14 for %14 kayıp): "))

    def verimlilik_hesapla(self):
        self.veriler['Kapasite_Faktoru'] = self.veriler['Uretim'] / (self.kurulu_guc * 24) * 100
        self.veriler['Performans_Orani'] = (self.veriler['Uretim'] / self.kurulu_guc) / self.veriler['Isinim']
        self.veriler['Verim'] = self.veriler['Uretim'] / (self.veriler['Isinim'] * self.panel_alani) * 100
        
        # Spesifik Enerji Üretimi (kWh/kWp)
        self.spesifik_uretim = self.veriler['Uretim'].sum() / self.kurulu_guc

    def sonuclari_goster(self):
        print("\n--- GES Tarlası Verimlilik Analizi Sonuçları ---")
        print(f"Analiz Dönemi: {self.veriler['Tarih'].min().date()} - {self.veriler['Tarih'].max().date()}")
        print(f"Toplam Üretim: {self.veriler['Uretim'].sum():.2f} kWh")
        print(f"Ortalama Günlük Üretim: {self.veriler['Uretim'].mean():.2f} kWh")
        print(f"Ortalama Kapasite Faktörü: {self.veriler['Kapasite_Faktoru'].mean():.2f}%")
        print(f"Ortalama Performans Oranı: {self.veriler['Performans_Orani'].mean():.2f}")
        print(f"Ortalama Verim: {self.veriler['Verim'].mean():.2f}%")
        print(f"Spesifik Enerji Üretimi: {self.spesifik_uretim:.2f} kWh/kWp")

    def grafikleri_ciz(self):
        fig, axs = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('GES Tarlası Verimlilik Analizi Grafikleri')

        # Üretim Grafiği
        axs[0, 0].plot(self.veriler['Tarih'], self.veriler['Uretim'])
        axs[0, 0].set_title('Günlük Enerji Üretimi')
        axs[0, 0].set_xlabel('Tarih')
        axs[0, 0].set_ylabel('Üretim (kWh)')

        # Kapasite Faktörü Grafiği
        axs[0, 1].plot(self.veriler['Tarih'], self.veriler['Kapasite_Faktoru'])
        axs[0, 1].set_title('Günlük Kapasite Faktörü')
        axs[0, 1].set_xlabel('Tarih')
        axs[0, 1].set_ylabel('Kapasite Faktörü (%)')

        # Performans Oranı Grafiği
        axs[1, 0].plot(self.veriler['Tarih'], self.veriler['Performans_Orani'])
        axs[1, 0].set_title('Günlük Performans Oranı')
        axs[1, 0].set_xlabel('Tarih')
        axs[1, 0].set_ylabel('Performans Oranı')

        # Verim Grafiği
        axs[1, 1].plot(self.veriler['Tarih'], self.veriler['Verim'])
        axs[1, 1].set_title('Günlük Verim')
        axs[1, 1].set_xlabel('Tarih')
        axs[1, 1].set_ylabel('Verim (%)')

        plt.tight_layout()
        plt.show()

    def calistir(self):
        self.veri_yukle()
        self.parametreleri_al()
        self.verimlilik_hesapla()
        self.sonuclari_goster()
        self.grafikleri_ciz()

if __name__ == "__main__":
    import numpy as np
    analiz = GESTarlasiVerimlilikAnalizi()
    analiz.calistir()