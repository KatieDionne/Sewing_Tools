# -*- coding: utf-8 -*-
"""
Created on Novemer 2025

@author: Katie Dionne

https://github.com/katiedionne
"""

'''
Calculate the minimum fabric length (in inches) required to cut all pieces,
and optionally visualize the layout.
'''


# %%

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# %%

def calculate_fabric_yardage(df: pd.DataFrame, fabric_width: float, visualize=True):
    

    def pack_pieces(piece_widths, piece_heights, fabric_width):

        # Check for pieces wider than the fabric
        if any(w > fabric_width for w in piece_widths):
            return float('nan'), []  # Return NaN length and empty layout

        """Greedy strip-packing with coordinates for visualization."""
        pieces = sorted(
            [(w, h, i) for i, (w, h) in enumerate(zip(piece_widths, piece_heights))],
            key=lambda x: x[1],
            reverse=True
        )

        total_length = 0
        remaining_width = fabric_width
        current_row_height = 0
        x_cursor = 0
        layout = []  # list of (x, y, w, h, index)

        for w, h, i in pieces:
            if w <= remaining_width:
                # place in current row
                layout.append((x_cursor, total_length, w, h, i))
                x_cursor += w
                remaining_width -= w
                current_row_height = max(current_row_height, h)
            else:
                # start new row
                total_length += current_row_height
                layout.append((0, total_length, w, h, i))
                x_cursor = w
                remaining_width = fabric_width - w
                current_row_height = h

        total_length += current_row_height
        return total_length, layout

    # --- Orientation A: vertical along yardage ---
    length_A, layout_A = pack_pieces(df["horizontal"], df["vertical"], fabric_width)
    if not pd.isna(length_A):
        print("horizontal along fabric width:", fabric_width, "wide", round(length_A/36, 2), "yards")
    

    # --- Orientation B: vertical along width ---
    length_B, layout_B = pack_pieces(df["vertical"], df["horizontal"], fabric_width)
    if not pd.isna(length_B):
        print("vertical along fabric width:", fabric_width, "wide", round(length_B/36, 2), "yards")

    if visualize and not pd.isna(length_A):
        def plot_layout(layout, total_length, orientation_label):
            fig, ax = plt.subplots(figsize=(8, max(4, total_length / 10)))
            for (x, y, w, h, i) in layout:
                rect = patches.Rectangle(
                    (x, y), w, h,
                    edgecolor='black', facecolor='lightblue', lw=1.5
                )
                ax.add_patch(rect)
                ax.text(x + w/2, y + h/2, str(i+1),
                        ha='center', va='center', fontsize=8)
            ax.set_xlim(0, fabric_width)
            ax.set_ylim(0, total_length)
            ax.set_title(f"Width: {fabric_width}\nLayout: {orientation_label}\nTotal Length = {round(total_length/36, 2)} yds")
            ax.set_xlabel("Fabric Width (inches)")
            ax.set_ylabel("Fabric Length (inches)")
            plt.gca().invert_yaxis()  # top of fabric = 0
            plt.tight_layout()
            plt.show()
        plot_layout(layout_A, length_A, "Vertical Along Yardage")

    if visualize and not pd.isna(length_B):
        def plot_layout(layout, total_length, orientation_label):
            fig, ax = plt.subplots(figsize=(8, max(4, total_length / 10)))
            for (x, y, w, h, i) in layout:
                rect = patches.Rectangle(
                    (x, y), w, h,
                    edgecolor='black', facecolor='lightblue', lw=1.5
                )
                ax.add_patch(rect)
                ax.text(x + w/2, y + h/2, str(i+1),
                        ha='center', va='center', fontsize=8)
            ax.set_xlim(0, fabric_width)
            ax.set_ylim(0, total_length)
            ax.set_title(f"Width: {fabric_width}\nLayout: {orientation_label}\nTotal Length = {round(total_length/36, 2)} yds")
            ax.set_xlabel("Fabric Width (inches)")
            ax.set_ylabel("Fabric Length (inches)")
            plt.gca().invert_yaxis()  # top of fabric = 0
            plt.tight_layout()
            plt.show()
        plot_layout(layout_B, length_B, "Vertical Along Width")


# %%

couch_sizes_1 = pd.DataFrame({
    'horizontal': [69, 90, 27, 59, 151, 36, 36, 36, 42],
    'vertical':   [36, 36, 56, 31, 15, 44, 44, 44, 49]
})

couch_sizes_2 = pd.DataFrame({
    'horizontal': [69, 90, 27, 86, 151, 36, 36, 36, 42],
    'vertical':   [36, 36, 25, 31, 15, 44, 44, 44, 49]
})

couch_sizes_3 = pd.DataFrame({
    'horizontal': [69, 90, 27, 59, 27, 26, 58, 40, 36, 36, 36, 42],
    'vertical':   [36, 36, 56, 31, 15, 15, 15, 15, 44, 44, 44, 49]
})


bikes_sizes = pd.DataFrame({
    'horizontal': [102],
    'vertical':   [138]
})

# %%
    
print("couch sizes 1")
calculate_fabric_yardage((couch_sizes_1+2), 45)
calculate_fabric_yardage((couch_sizes_1+2), 56)
calculate_fabric_yardage((couch_sizes_1+2), 60)
calculate_fabric_yardage((couch_sizes_1+2), 98)
calculate_fabric_yardage((couch_sizes_1+2), 120)

print("couch sizes 2")
calculate_fabric_yardage((couch_sizes_2+2), 45)
calculate_fabric_yardage((couch_sizes_2+2), 56)
calculate_fabric_yardage((couch_sizes_2+2), 60)
calculate_fabric_yardage((couch_sizes_2+2), 98)
calculate_fabric_yardage((couch_sizes_2+2), 120)

print("couch sizes 3")
calculate_fabric_yardage((couch_sizes_3+2), 45)
calculate_fabric_yardage((couch_sizes_3+2), 56)
calculate_fabric_yardage((couch_sizes_3+2), 60)
calculate_fabric_yardage((couch_sizes_3+2), 98)
calculate_fabric_yardage((couch_sizes_3+2), 120)

print("bike sizes")
calculate_fabric_yardage((bikes_sizes+2), 45)
calculate_fabric_yardage((bikes_sizes+2), 56)
calculate_fabric_yardage((bikes_sizes+2), 60)
calculate_fabric_yardage((bikes_sizes+2), 98)
calculate_fabric_yardage((bikes_sizes+2), 120)
