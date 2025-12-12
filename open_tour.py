import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import time

class KnightTourOpen:
    def __init__(self, board_size=8):
        self.size = board_size
        self.board = np.full((board_size, board_size), -1)
        self.moves_x = [2, 1, -1, -2, -2, -1, 1, 2]
        self.moves_y = [1, 2, 2, 1, -1, -2, -2, -1]
        
    def is_valid(self, x, y):
        # Cek apakah posisi valid dan belum dikunjungi
        return (0 <= x < self.size and 
                0 <= y < self.size and 
                self.board[x][y] == -1)
    
    def get_degree(self, x, y):
        # Hitung jumlah posisi valid yang bisa dikunjungi dari (x, y)
        count = 0
        for i in range(8):
            nx = x + self.moves_x[i]
            ny = y + self.moves_y[i]
            if self.is_valid(nx, ny):
                count += 1
        return count
    
    def solve_open_tour(self, start_x=0, start_y=0):
        self.board = np.full((self.size, self.size), -1)
        self.board[start_x][start_y] = 0
        self.path = [(start_x, start_y)]
        
        if self.solve_recursive(start_x, start_y, 1):
            return True
        return False
    
    def solve_recursive(self, x, y, move_count):
        # Backtracking dengan Warnsdorff's heuristic
        # Jika semua kotak sudah dikunjungi
        if move_count == self.size * self.size:
            return True
        
        # Generate semua kemungkinan gerakan
        moves = []
        for i in range(8):
            nx = x + self.moves_x[i]
            ny = y + self.moves_y[i]
            if self.is_valid(nx, ny):
                degree = self.get_degree(nx, ny)
                moves.append((degree, nx, ny))
        
        # Warnsdorff's heuristic, pilih kotak dengan aksesibilitas terendah
        moves.sort()
        
        # Coba setiap gerakan
        for _, nx, ny in moves:
            self.board[nx][ny] = move_count
            self.path.append((nx, ny))
            
            if self.solve_recursive(nx, ny, move_count + 1):
                return True
            
            # Backtrack
            self.board[nx][ny] = -1
            self.path.pop()
        
        return False
    
    def visualize(self, save_path='knights_tour_open.png'):
        fig, ax = plt.subplots(figsize=(10, 10))
        
        for i in range(self.size):
            for j in range(self.size):
                color = '#F0D9B5' if (i + j) % 2 == 0 else '#B58863'
                ax.add_patch(plt.Rectangle((j, self.size-1-i), 1, 1, 
                                          facecolor=color, edgecolor='black'))
                
                if self.board[i][j] != -1:
                    ax.text(j + 0.5, self.size - 1 - i + 0.5, 
                           str(self.board[i][j] + 1),
                           ha='center', va='center', fontsize=10, fontweight='bold')
        
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
        
        start_pos = self.path[0]
        end_pos = self.path[-1]
        
        circle_start = plt.Circle((start_pos[1] + 0.5, self.size - 1 - start_pos[0] + 0.5), 
                                 0.3, color='green', alpha=0.7, zorder=11)
        circle_end = plt.Circle((end_pos[1] + 0.5, self.size - 1 - end_pos[0] + 0.5), 
                               0.3, color='blue', alpha=0.7, zorder=11)
        ax.add_patch(circle_start)
        ax.add_patch(circle_end)
        
        ax.set_xlim(0, self.size)
        ax.set_ylim(0, self.size)
        ax.set_aspect('equal')
        ax.axis('off')
        
        plt.title(f"Knight's Tour - Open Tour\n{self.size}x{self.size} Board", 
                 fontsize=16, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"\n✓ Gambar disimpan sebagai '{save_path}'")

if __name__ == "__main__":
    print("KNIGHT'S TOUR - OPEN TOUR")
    print("\nOpen Tour: Kuda mengunjungi semua kotak sekali (Tidak harus kembali ke posisi awal)")
    
    board_size = 8
    kt = KnightTourOpen(board_size=board_size)
    
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
    
    print(f"\n[1] Mencari solusi Open Tour dari posisi ({start_x}, {start_y})...")
    start_time = time.time()
    
    if kt.solve_open_tour(start_x=start_x, start_y=start_y):
        elapsed = time.time() - start_time
        print(f"✓ Solusi ditemukan dalam {elapsed:.3f} detik")
        print(f"✓ Total langkah: {len(kt.path)}")
        print(f"✓ Posisi awal: {kt.path[0]}")
        print(f"✓ Posisi akhir: {kt.path[-1]}")
        
        print("\n[2] Langkah-langkah:")
        for i in range(min(64, len(kt.path))):
            x, y = kt.path[i]
            print(f"    Langkah {i+1}: ({x}, {y})")
        
        print("\n[3] Membuat visualisasi...")
        kt.visualize('knights_tour_open.png')
        
    else:
        print(f"[!] Tidak ditemukan solusi dari posisi tersebut")
        print(f"    Coba posisi awal yang berbeda!")
    
    print("Program selesai!")