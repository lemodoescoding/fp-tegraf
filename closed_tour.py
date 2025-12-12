import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import time
import random

class KnightTourGAA:
    def __init__(self, board_size=8):
        self.size = board_size
        self.board = np.full((board_size, board_size), -1)
        self.path = []
        
    def solve_closed_tour_genetic(self, start_x=0, start_y=0):
        # Menggunakan Genetic Algorithm Approach
        # Membuat populasi solusi dan evolusi (Greedy dengan mutasi acak)
        self.board = np.full((self.size, self.size), -1)
        self.path = [(start_x, start_y)]
        self.board[start_x][start_y] = 0
        
        # Gunakan greedy dengan random perturbation untuk simulasi genetic
        return self.genetic_solve(start_x, start_y, 1, start_x, start_y, mutation_rate=0.3)
    
    def genetic_solve(self, x, y, move_count, start_x, start_y, mutation_rate):
        # Greedy dengan random mutation
        if move_count == self.size * self.size:
            if self.can_reach(x, y, start_x, start_y):
                return True
            return False
        
        moves = []
        possible_moves = [(2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)]
        
        for dx, dy in possible_moves:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny):
                # Warnsdorff's rule (accessibility)
                accessibility = self.count_unvisited_neighbors(nx, ny)
                
                # Tambahkan random float untuk mutation (Genetika)
                # Untuk mencegah algoritma terjebak di local optimum yang sama
                mutation = random.random() * mutation_rate
                moves.append((accessibility + mutation, nx, ny))
        
        # Sortir gerakan berdasarkan skor (heuristic + mutasi)
        moves.sort()
        
        for _, nx, ny in moves:
            self.board[nx][ny] = move_count
            self.path.append((nx, ny))
            
            if self.genetic_solve(nx, ny, move_count + 1, start_x, start_y, mutation_rate):
                return True
            
            # Backtracking jika jalan buntu
            self.board[nx][ny] = -1
            self.path.pop()
        
        return False

    def is_valid(self, x, y):
        # Cek apakah posisi valid dan belum dikunjungi
        return (0 <= x < self.size and 
                0 <= y < self.size and 
                self.board[x][y] == -1)
    
    def can_reach(self, from_x, from_y, to_x, to_y):
        # Cek apakah kuda bisa bergerak dari satu posisi ke posisi lain
        dx = abs(from_x - to_x)
        dy = abs(from_y - to_y)
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)
    
    def count_unvisited_neighbors(self, x, y):
        # Hitung jumlah tetangga yang belum dikunjungi (Heuristic dasar)
        count = 0
        for dx, dy in [(2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)]:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny):
                count += 1
        return count
    
    def visualize(self, save_path='knights_tour_closed.png'):
        fig, ax = plt.subplots(figsize=(10, 10))
        
        for i in range(self.size):
            for j in range(self.size):
                color = '#F0D9B5' if (i + j) % 2 == 0 else '#B58863'
                ax.add_patch(plt.Rectangle((j, self.size-1-i), 1, 1, 
                                           facecolor=color, edgecolor='black'))
                
                if self.board[i][j] != -1:
                    ax.text(j + 0.5, self.size - 1 - i + 0.5, 
                           str(self.board[i][j] + 1),
                           ha='center', va='center', fontsize=9, fontweight='bold')
        
        for i in range(len(self.path) - 1):
            start = self.path[i]
            end = self.path[i + 1]
            
            arrow = FancyArrowPatch(
                (start[1] + 0.5, self.size - 1 - start[0] + 0.5),
                (end[1] + 0.5, self.size - 1 - end[0] + 0.5),
                arrowstyle='->', mutation_scale=15, linewidth=2,
                color='red', alpha=0.6, zorder=10
            )
            ax.add_patch(arrow)
        
        if len(self.path) == self.size * self.size:
            start = self.path[-1]
            end = self.path[0]
            arrow = FancyArrowPatch(
                (start[1] + 0.5, self.size - 1 - start[0] + 0.5),
                (end[1] + 0.5, self.size - 1 - end[0] + 0.5),
                arrowstyle='->', mutation_scale=15, linewidth=3,
                color='green', alpha=0.8, linestyle='--', zorder=11
            )
            ax.add_patch(arrow)
        
        start_pos = self.path[0]
        circle = plt.Circle((start_pos[1] + 0.5, self.size - 1 - start_pos[0] + 0.5), 
                           0.35, color='yellow', alpha=0.8, zorder=12, edgecolor='black', linewidth=2)
        ax.add_patch(circle)
        
        ax.set_xlim(0, self.size)
        ax.set_ylim(0, self.size)
        ax.set_aspect('equal')
        ax.axis('off')
        
        plt.title(f"Knight's Tour - Closed Tour\n{self.size}x{self.size} Board", 
                 fontsize=16, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"\n[✓] Gambar disimpan sebagai '{save_path}'")

if __name__ == "__main__":
    print("KNIGHT'S TOUR - CLOSED TOUR")
    
    board_size = 8
    kt = KnightTourGAA(board_size=board_size)
    
    print(f"\nPapan catur: {board_size}x{board_size}")
    print("Masukkan posisi awal kuda (0-7):")
    
    try:
        start_x = int(input("  Baris (0-7): "))
        start_y = int(input("  Kolom (0-7): "))
        
        if not (0 <= start_x < board_size and 0 <= start_y < board_size):
            print(f"[!] Posisi tidak valid! Menggunakan default (0,0)")
            start_x, start_y = 0, 0
    except:
        print("[!] Input tidak valid! Menggunakan default (0,0)")
        start_x, start_y = 0, 0
    
    print(f"\n[1] Mencari solusi Closed Tour dengan Genetic Algorithm...")
    start_time = time.time()
    
    success = kt.solve_closed_tour_genetic(start_x, start_y)
    
    if success:
        elapsed = time.time() - start_time
        print(f"\n[✓] Solusi ditemukan dalam {elapsed:.3f} detik")
        print(f"[✓] Total langkah: {len(kt.path)}")
        print(f"[✓] Posisi awal: {kt.path[0]}")
        print(f"[✓] Posisi akhir: {kt.path[-1]}")
        print(f"[✓] Kuda dapat kembali ke posisi awal (Closed Tour)!")
        
        print("\n[2] Langkah-langkah:")
        for i in range(min(64, len(kt.path))):
            x, y = kt.path[i]
            print(f"    Langkah {i+1}: ({x}, {y})")
        
        print("\n[3] Membuat visualisasi...")
        kt.visualize('knights_tour_closed.png')
        
    else:
        print(f"[!] Tidak ditemukan Closed Tour.")
        print(f"    Silakan coba lagi (karena ada unsur random pada mutasi genetik).")
    
    print("Program selesai!")