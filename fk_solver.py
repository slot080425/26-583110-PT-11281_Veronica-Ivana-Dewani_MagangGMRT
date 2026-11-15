import math
import numpy as np
import matplotlib.pyplot as plt

panjang_coxa = 5
panjang_femur = 10
panjang_tibia = 81

def fk_3d(sudut_base_rad, sudut_coxa_rad, sudut_femur_rad, sudut_tibia_rad):
    transformasi_base = np.array([
        [math.cos(sudut_base_rad), -math.sin(sudut_base_rad), 0, 0],
        [math.sin(sudut_base_rad),  math.cos(sudut_base_rad), 0, 0],
        [0,                  0,                 1, 0],
        [0,                  0,                 0, 1]
    ])
    
    transformasi_coxa = np.array([
        [math.cos(sudut_coxa_rad), -math.sin(sudut_coxa_rad), 0, panjang_coxa * math.cos(sudut_coxa_rad)],
        [0,                         1,                        0, 0],
        [math.sin(sudut_coxa_rad),  math.cos(sudut_coxa_rad), 1, panjang_coxa * math.sin(sudut_coxa_rad)],
        [0,                         0,                        0, 1]
    ])
    
    transformasi_femur = np.array([
        [math.cos(sudut_femur_rad), -math.sin(sudut_femur_rad), 0, panjang_femur * math.cos(sudut_femur_rad)],
        [0,                          1,                         0, 0],
        [math.sin(sudut_femur_rad),  math.cos(sudut_femur_rad), 1, panjang_femur * math.sin(sudut_femur_rad)],
        [0,                          0,                         0, 1]
    ])
    
    transformasi_tibia = np.array([
        [math.cos(sudut_tibia_rad), -math.sin(sudut_tibia_rad), 0, panjang_tibia * math.cos(sudut_tibia_rad)],
        [0,                          1,                         0, 0],
        [math.sin(sudut_tibia_rad),  math.cos(sudut_tibia_rad), 1, panjang_tibia * math.sin(sudut_tibia_rad)],
        [0,                          0,                         0, 1]
    ])
    
    posisi_base = transformasi_base
    posisi_coxa = np.dot(posisi_base, transformasi_coxa)
    posisi_femur = np.dot(posisi_coxa, transformasi_femur)
    posisi_tibia = np.dot(posisi_femur, transformasi_tibia)
    
    return (posisi_base, posisi_coxa, posisi_femur, posisi_tibia)

def visualisasi_gui(semua_posisi):
    posisi_base, posisi_coxa, posisi_femur, posisi_tibia = semua_posisi
    
    x_vals = [0, posisi_base[0,3], posisi_coxa[0,3], posisi_femur[0,3], posisi_tibia[0,3]]
    y_vals = [0, posisi_base[1,3], posisi_coxa[1,3], posisi_femur[1,3], posisi_tibia[1,3]]
    z_vals = [0, posisi_base[2,3], posisi_coxa[2,3], posisi_femur[2,3], posisi_tibia[2,3]]
    
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.plot(x_vals, y_vals, z_vals, marker='o', linewidth=4, markersize=8, label='Lengan Robot')
    ax.scatter(x_vals[-1], y_vals[-1], z_vals[-1], color='red', s=100, label='End-Effector', zorder=5)
    
    ax.set_xlim([-100, 100])
    ax.set_ylim([-100, 100])
    ax.set_zlim([-20, 100])
    ax.set_xlabel('Sumbu X')
    ax.set_ylabel('Sumbu Y')
    ax.set_zlabel('Sumbu Z')
    ax.set_title('Visualisasi GUI')
    ax.legend()
    
    plt.show()

def ik(target_x, target_y): 
    jarak_target = (target_x**2) + (target_y**2)
    
    if math.sqrt(jarak_target) > (panjang_femur + panjang_tibia):
        print("\ntarget tidak bisa dijangkau")
        return None, None
        
    cos_theta2 = (jarak_target - (panjang_femur**2) - (panjang_tibia**2)) / (2 * panjang_femur * panjang_tibia)
    theta2_rad = math.acos(cos_theta2) 
    
    theta1_rad = math.atan2(target_y, target_x) - math.atan2((panjang_tibia * math.sin(theta2_rad)), (panjang_femur + panjang_tibia * math.cos(theta2_rad)))
    
    theta1_deg = math.degrees(theta1_rad)
    theta2_deg = math.degrees(theta2_rad)
    
    return theta1_deg, theta2_deg

while True:
    print("\n1. fk")
    print("2. ik")
    
    pilihan = input("pilih 1/2: ")
    
    if pilihan == '1':
        try:
            sudut_base_input = input("sudut_base (dalam derajat, 0 untuk 2D): ")
            sudut_base = float(sudut_base_input)
            sudut_base_rad = math.radians(sudut_base)
            
            sudut_coxa = input("sudut_coxa (dalam derajat): ")
            sudut_coxa = float(sudut_coxa)
            sudut_coxa_rad = math.radians(sudut_coxa)

            sudut_femur = input("sudut_femur (dalam derajat): ")
            sudut_femur = float(sudut_femur)
            sudut_femur_rad = math.radians(sudut_femur)

            sudut_tibia = input("sudut_tibia (dalam derajat): ")
            sudut_tibia = float(sudut_tibia)
            sudut_tibia_rad = math.radians(sudut_tibia)

            sudut_femur_rad = sudut_coxa_rad + sudut_femur_rad
            sudut_tibia_rad = sudut_femur_rad + sudut_tibia_rad

            x = (panjang_coxa * math.cos(sudut_coxa_rad)) + (panjang_femur * math.cos(sudut_femur_rad)) + (panjang_tibia * math.cos(sudut_tibia_rad))
            y = (panjang_coxa * math.sin(sudut_coxa_rad)) + (panjang_femur * math.sin(sudut_femur_rad)) + (panjang_tibia * math.sin(sudut_tibia_rad))
            
            print(f"koordinat x: {round(x, 2)}")
            print(f"koordinat y: {round(y, 2)}")
            
            semua_posisi = fk_3d(sudut_base_rad, sudut_coxa_rad, sudut_femur_rad, sudut_tibia_rad)
            visualisasi_gui(semua_posisi)
            
        except ValueError:
            print("input angka")
            
    elif pilihan == '2':
        try:
            target_x = input("koordinat_x: ")
            target_x = float(target_x)
            
            target_y = input("koordinat_y: ")
            target_y = float(target_y)
            
            th1, th2 = ik(target_x, target_y)
            
            if th1 is not None:
                print(f"sudut femur: {round(th1, 2)} derajat")
                print(f"sudut tibia: {round(th2, 2)} derajat")
                
        except ValueError:
             print("input angka")
    else:
        print("pilih 1/2")