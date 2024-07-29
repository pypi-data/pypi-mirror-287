import os
from qtpy import QtCore
from tkinter import ttk
import numpy as np
import tkinter as tk
import imageio.v2 as imageio
from collections import deque
from PIL import Image, ImageTk
from skimage.draw import polygon, line
from skimage.transform import resize
from scipy.ndimage import binary_fill_holes, label
from ttkthemes import ThemedTk
from pyqtgraph import GraphicsLayoutWidget, ViewBox, ImageItem, mkQApp

from .logger import log_function_call
from .gui_utils import spacrFrame, spacrButton, set_dark_style, create_menu_bar, set_default_font

class ModifyMasks:
    def __init__(self, root, folder_path, scale_factor):
        self.root = root
        self.folder_path = folder_path
        self.scale_factor = scale_factor
        self.image_filenames = sorted([f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg', '.tif', '.tiff'))])
        self.masks_folder = os.path.join(folder_path, 'masks')
        self.current_image_index = 0
        self.initialize_flags()
        self.canvas_width = 1000
        self.canvas_height = 1000
        self.root.configure(bg='black')
        self.setup_navigation_toolbar()
        self.setup_mode_toolbar()
        self.setup_function_toolbar()
        self.setup_canvas()
        self.load_first_image()

    def update_display(self):
        self.display_image()

    def update_original_mask(self, zoomed_mask, x0, x1, y0, y1):
        actual_mask_region = self.mask[y0:y1, x0:x1]
        target_shape = actual_mask_region.shape
        resized_mask = resize(zoomed_mask, target_shape, order=0, preserve_range=True).astype(np.uint8)
        if resized_mask.shape != actual_mask_region.shape:
            raise ValueError(f"Shape mismatch: resized_mask {resized_mask.shape}, actual_mask_region {actual_mask_region.shape}")
        self.mask[y0:y1, x0:x1] = np.maximum(actual_mask_region, resized_mask)
        self.mask = self.mask.copy()
        self.mask[y0:y1, x0:x1] = np.maximum(self.mask[y0:y1, x0:x1], resized_mask)
        self.mask = self.mask.copy()

    def get_scaling_factors(self, img_width, img_height, canvas_width, canvas_height):
        x_scale = img_width / canvas_width
        y_scale = img_height / canvas_height
        return x_scale, y_scale

    def canvas_to_image(self, x_canvas, y_canvas):
        x_scale, y_scale = self.get_scaling_factors(
            self.image.shape[1], self.image.shape[0],
            self.canvas_width, self.canvas_height
        )
        x_image = int(x_canvas * x_scale)
        y_image = int(y_canvas * y_scale)
        return x_image, y_image

    def normalize_image(self, image, lower_quantile, upper_quantile):
        lower_bound = np.percentile(image, lower_quantile)
        upper_bound = np.percentile(image, upper_quantile)
        normalized = np.clip(image, lower_bound, upper_bound)
        normalized = (normalized - lower_bound) / (upper_bound - lower_bound)
        max_value = np.iinfo(image.dtype).max
        normalized = (normalized * max_value).astype(image.dtype)
        return normalized

    def resize_arrays(self, img, mask):
        original_dtype = img.dtype
        scaled_height = int(img.shape[0] * self.scale_factor)
        scaled_width = int(img.shape[1] * self.scale_factor)
        scaled_img = resize(img, (scaled_height, scaled_width), anti_aliasing=True, preserve_range=True)
        scaled_mask = resize(mask, (scaled_height, scaled_width), order=0, anti_aliasing=False, preserve_range=True)
        stretched_img = resize(scaled_img, (self.canvas_height, self.canvas_width), anti_aliasing=True, preserve_range=True)
        stretched_mask = resize(scaled_mask, (self.canvas_height, self.canvas_width), order=0, anti_aliasing=False, preserve_range=True)
        return stretched_img.astype(original_dtype), stretched_mask.astype(original_dtype)

    def load_first_image(self):
        self.image, self.mask = self.load_image_and_mask(self.current_image_index)
        self.original_size = self.image.shape
        self.image, self.mask = self.resize_arrays(self.image, self.mask)
        self.display_image()

    def setup_canvas(self):
        self.app = mkQApp()
        self.win = GraphicsLayoutWidget(show=True)
        self.win.setWindowTitle('Image Canvas')

        self.view = ViewBox()
        self.view.setAspectLocked(True)
        self.win.addItem(self.view)

        self.img = ImageItem()
        self.view.addItem(self.img)

        self.view.sigMouseDragged.connect(self.mouse_dragged)
        self.view.sigMouseClicked.connect(self.mouse_clicked)
        self.view.sigMouseWheel.connect(self.mouse_wheel)

    def initialize_flags(self):
        self.drawing = False
        self.magic_wand_active = False
        self.brush_active = False
        self.dividing_line_active = False
        self.dividing_line_coords = []
        self.current_dividing_line = None
        self.lower_quantile = tk.StringVar(value="1.0")
        self.upper_quantile = tk.StringVar(value="99.9")
        self.magic_wand_tolerance = tk.StringVar(value="1000")

    def update_mouse_info(self, event):
        x, y = event.x, event.y
        intensity = "N/A"
        mask_value = "N/A"
        pixel_count = "N/A"
        if 0 <= x < self.image.shape[1] and 0 <= y < self.image.shape[0]:
            intensity = self.image[y, x]
            mask_value = self.mask[y, x]
        if mask_value != "N/A" and mask_value != 0:
            pixel_count = np.sum(self.mask == mask_value)
        self.intensity_label.config(text=f"Intensity: {intensity}")
        self.mask_value_label.config(text=f"Mask: {mask_value}, Area: {pixel_count}")
        self.mask_value_label.config(text=f"Mask: {mask_value}")
        if mask_value != "N/A" and mask_value != 0:
            self.pixel_count_label.config(text=f"Area: {pixel_count}")
        else:
            self.pixel_count_label.config(text="Area: N/A")

    def setup_navigation_toolbar(self):
        navigation_toolbar = tk.Frame(self.root, bg='black')
        navigation_toolbar.pack(side='top', fill='x')
        prev_btn = tk.Button(navigation_toolbar, text="Previous", command=self.previous_image, bg='black', fg='white')
        prev_btn.pack(side='left')
        next_btn = tk.Button(navigation_toolbar, text="Next", command=self.next_image, bg='black', fg='white')
        next_btn.pack(side='left')
        save_btn = tk.Button(navigation_toolbar, text="Save", command=self.save_mask, bg='black', fg='white')
        save_btn.pack(side='left')
        self.intensity_label = tk.Label(navigation_toolbar, text="Image: N/A", bg='black', fg='white')
        self.intensity_label.pack(side='right')
        self.mask_value_label = tk.Label(navigation_toolbar, text="Mask: N/A", bg='black', fg='white')
        self.mask_value_label.pack(side='right')
        self.pixel_count_label = tk.Label(navigation_toolbar, text="Area: N/A", bg='black', fg='white')
        self.pixel_count_label.pack(side='right')

    def setup_mode_toolbar(self):
        self.mode_toolbar = tk.Frame(self.root, bg='black')
        self.mode_toolbar.pack(side='top', fill='x')
        self.draw_btn = tk.Button(self.mode_toolbar, text="Draw", command=self.toggle_draw_mode, bg='black', fg='white')
        self.draw_btn.pack(side='left')
        self.magic_wand_btn = tk.Button(self.mode_toolbar, text="Magic Wand", command=self.toggle_magic_wand_mode, bg='black', fg='white')
        self.magic_wand_btn.pack(side='left')
        tk.Label(self.mode_toolbar, text="Tolerance:", bg='black', fg='white').pack(side='left')
        self.tolerance_entry = tk.Entry(self.mode_toolbar, textvariable=self.magic_wand_tolerance, bg='black', fg='white')
        self.tolerance_entry.pack(side='left')
        tk.Label(self.mode_toolbar, text="Max Pixels:", bg='black', fg='white').pack(side='left')
        self.max_pixels_entry = tk.Entry(self.mode_toolbar, bg='black', fg='white')
        self.max_pixels_entry.insert(0, "1000")
        self.max_pixels_entry.pack(side='left')
        self.erase_btn = tk.Button(self.mode_toolbar, text="Erase", command=self.toggle_erase_mode, bg='black', fg='white')
        self.erase_btn.pack(side='left')
        self.brush_btn = tk.Button(self.mode_toolbar, text="Brush", command=self.toggle_brush_mode, bg='black', fg='white')
        self.brush_btn.pack(side='left')
        self.brush_size_entry = tk.Entry(self.mode_toolbar, bg='black', fg='white')
        self.brush_size_entry.insert(0, "10")
        self.brush_size_entry.pack(side='left')
        tk.Label(self.mode_toolbar, text="Brush Size:", bg='black', fg='white').pack(side='left')
        self.dividing_line_btn = tk.Button(self.mode_toolbar, text="Dividing Line", command=self.toggle_dividing_line_mode, bg='black', fg='white')
        self.dividing_line_btn.pack(side='left')

    def setup_function_toolbar(self):
        self.function_toolbar = tk.Frame(self.root, bg='black')
        self.function_toolbar.pack(side='top', fill='x')
        self.fill_btn = tk.Button(self.function_toolbar, text="Fill", command=self.fill_objects, bg='black', fg='white')
        self.fill_btn.pack(side='left')
        self.relabel_btn = tk.Button(self.function_toolbar, text="Relabel", command=self.relabel_objects, bg='black', fg='white')
        self.relabel_btn.pack(side='left')
        self.clear_btn = tk.Button(self.function_toolbar, text="Clear", command=self.clear_objects, bg='black', fg='white')
        self.clear_btn.pack(side='left')
        self.invert_btn = tk.Button(self.function_toolbar, text="Invert", command=self.invert_mask, bg='black', fg='white')
        self.invert_btn.pack(side='left')
        remove_small_btn = tk.Button(self.function_toolbar, text="Remove Small", command=self.remove_small_objects, bg='black', fg='white')
        remove_small_btn.pack(side='left')
        tk.Label(self.function_toolbar, text="Min Area:", bg='black', fg='white').pack(side='left')
        self.min_area_entry = tk.Entry(self.function_toolbar, bg='black', fg='white')
        self.min_area_entry.insert(0, "100")  # Default minimum area
        self.min_area_entry.pack(side='left')

    def load_image_and_mask(self, index):
        image_path = os.path.join(self.folder_path, self.image_filenames[index])
        image = imageio.imread(image_path)
        mask_path = os.path.join(self.masks_folder, self.image_filenames[index])
        if os.path.exists(mask_path):
            print(f'loading mask:{mask_path} for image: {image_path}')
            mask = imageio.imread(mask_path)
            if mask.dtype != np.uint8:
                mask = (mask / np.max(mask) * 255).astype(np.uint8)
        else:
            mask = np.zeros(image.shape[:2], dtype=np.uint8)
            print(f'loaded new mask for image: {image_path}')
        return image, mask

    def display_image(self):
        lower_quantile = float(self.lower_quantile.get()) if self.lower_quantile.get() else 1.0
        upper_quantile = float(self.upper_quantile.get()) if self.upper_quantile.get() else 99.9
        normalized = self.normalize_image(self.image, lower_quantile, upper_quantile)
        combined = self.overlay_mask_on_image(normalized, self.mask)
        self.img.setImage(combined)

    def overlay_mask_on_image(self, image, mask, alpha=0.5):
        if len(image.shape) == 2:
            image = np.stack((image,) * 3, axis=-1)
        mask = mask.astype(np.int32)
        max_label = np.max(mask)
        np.random.seed(0)
        colors = np.random.randint(0, 255, size=(max_label + 1, 3), dtype=np.uint8)
        colors[0] = [0, 0, 0]  # background color
        colored_mask = colors[mask]
        image_8bit = (image / 256).astype(np.uint8)
        combined_image = np.where(mask[..., None] > 0,
                                  np.clip(image_8bit * (1 - alpha) + colored_mask * alpha, 0, 255),
                                  image_8bit)
        combined_image = combined_image.astype(np.uint8)
        return combined_image

    def previous_image(self):
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.initialize_flags()
            self.image, self.mask = self.load_image_and_mask(self.current_image_index)
            self.original_size = self.image.shape
            self.image, self.mask = self.resize_arrays(self.image, self.mask)
            self.display_image()

    def next_image(self):
        if self.current_image_index < len(self.image_filenames) - 1:
            self.current_image_index += 1
            self.initialize_flags()
            self.image, self.mask = self.load_image_and_mask(self.current_image_index)
            self.original_size = self.image.shape
            self.image, self.mask = self.resize_arrays(self.image, self.mask)
            self.display_image()

    def save_mask(self):
        if self.current_image_index < len(self.image_filenames):
            original_size = self.original_size
            if self.mask.shape != original_size:
                resized_mask = resize(self.mask, original_size, order=0, preserve_range=True).astype(np.uint16)
            else:
                resized_mask = self.mask
            resized_mask, _ = label(resized_mask > 0)
            save_folder = os.path.join(self.folder_path, 'masks')
            if not os.path.exists(save_folder):
                os.makedirs(save_folder)
            image_filename = os.path.splitext(self.image_filenames[self.current_image_index])[0] + '.tif'
            save_path = os.path.join(save_folder, image_filename)

            print(f"Saving mask to: {save_path}")
            imageio.imwrite(save_path, resized_mask)

    def mouse_dragged(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.view.translateBy(event.delta())
        event.accept()

    def mouse_clicked(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.view.resetTransform()
        event.accept()

    def mouse_wheel(self, event):
        delta = event.delta()
        if delta > 0:
            self.view.scaleBy((1.1, 1.1))
        else:
            self.view.scaleBy((0.9, 0.9))
        event.accept()

    def toggle_brush_mode(self):
        self.brush_active = not self.brush_active
        if self.brush_active:
            self.drawing = False
            self.magic_wand_active = False
            self.erase_active = False
            self.brush_btn.config(text="Brush ON")
            self.draw_btn.config(text="Draw")
            self.erase_btn.config(text="Erase")
            self.magic_wand_btn.config(text="Magic Wand")
            self.canvas.unbind("<Button-1>")
            self.canvas.unbind("<Button-3>")
            self.canvas.unbind("<Motion>")
            self.canvas.bind("<B1-Motion>", self.apply_brush)
            self.canvas.bind("<B3-Motion>", self.erase_brush)
            self.canvas.bind("<ButtonRelease-1>", self.apply_brush_release)
            self.canvas.bind("<ButtonRelease-3>", self.erase_brush_release)
        else:
            self.brush_active = False
            self.brush_btn.config(text="Brush")
            self.canvas.unbind("<B1-Motion>")
            self.canvas.unbind("<B3-Motion>")
            self.canvas.unbind("<ButtonRelease-1>")
            self.canvas.unbind("<ButtonRelease-3>")

    def image_to_canvas(self, x_image, y_image):
        x_scale, y_scale = self.get_scaling_factors(
            self.image.shape[1], self.image.shape[0],
            self.canvas_width, self.canvas_height
        )
        x_canvas = int(x_image / x_scale)
        y_canvas = int(y_image / y_scale)
        return x_canvas, y_canvas

    def toggle_dividing_line_mode(self):
        self.dividing_line_active = not self.dividing_line_active
        if self.dividing_line_active:
            self.drawing = False
            self.magic_wand_active = False
            self.erase_active = False
            self.brush_active = False
            self.draw_btn.config(text="Draw")
            self.erase_btn.config(text="Erase")
            self.magic_wand_btn.config(text="Magic Wand")
            self.brush_btn.config(text="Brush")
            self.dividing_line_btn.config(text="Dividing Line ON")
            self.canvas.unbind("<Button-1>")
            self.canvas.unbind("<ButtonRelease-1>")
            self.canvas.unbind("<Motion>")
            self.canvas.bind("<Button-1>", self.start_dividing_line)
            self.canvas.bind("<ButtonRelease-1>", self.finish_dividing_line)
            self.canvas.bind("<Motion>", self.update_dividing_line_preview)
        else:
            self.dividing_line_active = False
            self.dividing_line_btn.config(text="Dividing Line")
            self.canvas.unbind("<Button-1>")
            self.canvas.unbind("<ButtonRelease-1>")
            self.canvas.unbind("<Motion>")
            self.display_image()

    def start_dividing_line(self, event):
        if self.dividing_line_active:
            self.dividing_line_coords = [(event.x, event.y)]
            self.current_dividing_line = self.canvas.create_line(event.x, event.y, event.x, event.y, fill="red", width=2)

    def finish_dividing_line(self, event):
        if self.dividing_line_active:
            self.dividing_line_coords.append((event.x, event.y))
            self.apply_dividing_line()
            self.canvas.delete(self.current_dividing_line)
            self.current_dividing_line = None

    def update_dividing_line_preview(self, event):
        if self.dividing_line_active and self.dividing_line_coords:
            x, y = event.x, event.y
            self.dividing_line_coords.append((x, y))
            canvas_coords = [self.image_to_canvas(*pt) for pt in self.dividing_line_coords]
            flat_canvas_coords = [coord for pt in canvas_coords for coord in pt]
            self.canvas.coords(self.current_dividing_line, *flat_canvas_coords)

    def apply_dividing_line(self):
        if self.dividing_line_coords:
            coords = self.dividing_line_coords
            rr, cc = [], []
            for (x0, y0), (x1, y1) in zip(coords[:-1], coords[1:]):
                line_rr, line_cc = line(y0, x0, y1, x1)
                rr.extend(line_rr)
                cc.extend(line_cc)
            rr, cc = np.array(rr), np.array(cc)

            mask_copy = self.mask.copy()
            mask_copy[rr, cc] = 0
            self.mask = mask_copy

            labeled_mask, num_labels = label(self.mask > 0)
            self.mask = labeled_mask
            self.update_display()

            self.dividing_line_coords = []
            self.canvas.unbind("<Button-1>")
            self.canvas.unbind("<ButtonRelease-1>")
            self.canvas.unbind("<Motion>")
            self.dividing_line_active = False
            self.dividing_line_btn.config(text="Dividing Line")

    def toggle_draw_mode(self):
        self.drawing = not self.drawing
        if self.drawing:
            self.brush_btn.config(text="Brush")
            self.canvas.unbind("<B1-Motion>")
            self.canvas.unbind("<B3-Motion>")
            self.canvas.unbind("<ButtonRelease-1>")
            self.canvas.unbind("<ButtonRelease-3>")
            self.magic_wand_active = False
            self.erase_active = False
            self.brush_active = False
            self.draw_btn.config(text="Draw ON")
            self.magic_wand_btn.config(text="Magic Wand")
            self.erase_btn.config(text="Erase")
            self.draw_coordinates = []
            self.canvas.unbind("<Button-1>")
            self.canvas.unbind("<Motion>")
            self.canvas.bind("<B1-Motion>", self.draw)
            self.canvas.bind("<ButtonRelease-1>", self.finish_drawing)
        else:
            self.drawing = False
            self.draw_btn.config(text="Draw")
            self.canvas.unbind("<B1-Motion>")
            self.canvas.unbind("<ButtonRelease-1>")

    def toggle_magic_wand_mode(self):
        self.magic_wand_active = not self.magic_wand_active
        if self.magic_wand_active:
            self.brush_btn.config(text="Brush")
            self.canvas.unbind("<B1-Motion>")
            self.canvas.unbind("<B3-Motion>")
            self.canvas.unbind("<ButtonRelease-1>")
            self.canvas.unbind("<ButtonRelease-3>")
            self.drawing = False
            self.erase_active = False
            self.brush_active = False
            self.draw_btn.config(text="Draw")
            self.erase_btn.config(text="Erase")
            self.magic_wand_btn.config(text="Magic Wand ON")
            self.canvas.bind("<Button-1>", self.use_magic_wand)
            self.canvas.bind("<Button-3>", self.use_magic_wand)
        else:
            self.magic_wand_btn.config(text="Magic Wand")
            self.canvas.unbind("<Button-1>")
            self.canvas.unbind("<Button-3>")

    def toggle_erase_mode(self):
        self.erase_active = not self.erase_active
        if self.erase_active:
            self.brush_btn.config(text="Brush")
            self.canvas.unbind("<B1-Motion>")
            self.canvas.unbind("<B3-Motion>")
            self.canvas.unbind("<ButtonRelease-1>")
            self.canvas.unbind("<ButtonRelease-3>")
            self.erase_btn.config(text="Erase ON")
            self.canvas.bind("<Button-1>", self.erase_object)
            self.drawing = False
            self.magic_wand_active = False
            self.brush_active = False
            self.draw_btn.config(text="Draw")
            self.magic_wand_btn.config(text="Magic Wand")
        else:
            self.erase_active = False
            self.erase_btn.config(text="Erase")
            self.canvas.unbind("<Button-1>")

    def apply_brush_release(self, event):
        if hasattr(self, 'brush_path'):
            for x, y, brush_size in self.brush_path:
                img_x, img_y = (x, y)
                x0 = max(img_x - brush_size // 2, 0)
                y0 = max(img_y - brush_size // 2, 0)
                x1 = min(img_x + brush_size // 2, self.mask.shape[1])
                y1 = min(img_y + brush_size // 2, self.mask.shape[0])
                self.mask[y0:y1, x0:x1] = 255
            del self.brush_path
            self.canvas.delete("temp_line")
            self.update_display()

    def erase_brush_release(self, event):
        if hasattr(self, 'erase_path'):
            for x, y, brush_size in self.erase_path:
                img_x, img_y = (x, y)
                x0 = max(img_x - brush_size // 2, 0)
                y0 = max(img_y - brush_size // 2, 0)
                x1 = min(img_x + brush_size // 2, self.mask.shape[1])
                y1 = min(img_y + brush_size // 2, self.mask.shape[0])
                self.mask[y0:y1, x0:x1] = 0
            del self.erase_path
            self.canvas.delete("temp_line")
            self.update_display()

    def apply_brush(self, event):
        brush_size = int(self.brush_size_entry.get())
        x, y = event.x, event.y
        if not hasattr(self, 'brush_path'):
            self.brush_path = []
            self.last_brush_coord = (x, y)
        if self.last_brush_coord:
            last_x, last_y = self.last_brush_coord
            rr, cc = line(last_y, last_x, y, x)
            for ry, rx in zip(rr, cc):
                self.brush_path.append((rx, ry, brush_size))

        self.canvas.create_line(self.last_brush_coord[0], self.last_brush_coord[1], x, y, width=brush_size, fill="blue", tag="temp_line")
        self.last_brush_coord = (x, y)

    def erase_brush(self, event):
        brush_size = int(self.brush_size_entry.get())
        x, y = event.x, event.y
        if not hasattr(self, 'erase_path'):
            self.erase_path = []
            self.last_erase_coord = (x, y)
        if self.last_erase_coord:
            last_x, last_y = self.last_erase_coord
            rr, cc = line(last_y, last_x, y, x)
            for ry, rx in zip(rr, cc):
                self.erase_path.append((rx, ry, brush_size))

        self.canvas.create_line(self.last_erase_coord[0], self.last_erase_coord[1], x, y, width=brush_size, fill="white", tag="temp_line")
        self.last_erase_coord = (x, y)

    def erase_object(self, event):
        x, y = event.x, event.y
        orig_x, orig_y = x, y
        label_to_remove = self.mask[orig_y, orig_x]
        if label_to_remove > 0:
            self.mask[self.mask == label_to_remove] = 0
        self.update_display()

    def use_magic_wand(self, event):
        x, y = event.x, event.y
        tolerance = int(self.magic_wand_tolerance.get())
        maximum = int(self.max_pixels_entry.get())
        action = 'add' if event.num == 1 else 'erase'
        self.magic_wand_normal((x, y), tolerance, action)

    def apply_magic_wand(self, image, mask, seed_point, tolerance, maximum, action='add'):
        x, y = seed_point
        initial_value = image[y, x].astype(np.float32)
        visited = np.zeros_like(image, dtype=bool)
        queue = deque([(x, y)])
        added_pixels = 0

        while queue and added_pixels < maximum:
            cx, cy = queue.popleft()
            if visited[cy, cx]:
                continue
            visited[cy, cx] = True
            current_value = image[cy, cx].astype(np.float32)

            if np.linalg.norm(abs(current_value - initial_value)) <= tolerance:
                if mask[cy, cx] == 0:
                    added_pixels += 1
                mask[cy, cx] = 255 if action == 'add' else 0

                if added_pixels >= maximum:
                    break

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < image.shape[1] and 0 <= ny < image.shape[0] and not visited[ny, nx]:
                        queue.append((nx, ny))
        return mask

    def magic_wand_normal(self, seed_point, tolerance, action):
        try:
            maximum = int(self.max_pixels_entry.get())
        except ValueError:
            print("Invalid maximum value; using default of 1000")
            maximum = 1000
        self.mask = self.apply_magic_wand(self.image, self.mask, seed_point, tolerance, maximum, action)
        self.display_image()

    def draw(self, event):
        if self.drawing:
            x, y = event.x, event.y
            if self.draw_coordinates:
                last_x, last_y = self.draw_coordinates[-1]
                self.current_line = self.canvas.create_line(last_x, last_y, x, y, fill="yellow", width=3)
            self.draw_coordinates.append((x, y))

    def draw_on_zoomed_mask(self, draw_coordinates):
        canvas_height = self.canvas.winfo_height()
        canvas_width = self.canvas.winfo_width()
        zoomed_mask = np.zeros((canvas_height, canvas_width), dtype=np.uint8)
        rr, cc = polygon(np.array(draw_coordinates)[:, 1], np.array(draw_coordinates)[:, 0], shape=zoomed_mask.shape)
        zoomed_mask[rr, cc] = 255
        return zoomed_mask

    def finish_drawing(self, event):
        if len(self.draw_coordinates) > 2:
            self.draw_coordinates.append(self.draw_coordinates[0])
            rr, cc = polygon(np.array(self.draw_coordinates)[:, 1], np.array(self.draw_coordinates)[:, 0], shape=self.mask.shape)
            self.mask[rr, cc] = np.maximum(self.mask[rr, cc], 255)
            self.mask = self.mask.copy()
            self.canvas.delete(self.current_line)
            self.draw_coordinates.clear()
        self.update_display()

    def finish_drawing_if_active(self, event):
        if self.drawing and len(self.draw_coordinates) > 2:
            self.finish_drawing(event)

    def apply_normalization(self):
        self.lower_quantile.set(self.lower_entry.get())
        self.upper_quantile.set(self.upper_entry.get())
        self.update_display()

    def fill_objects(self):
        binary_mask = self.mask > 0
        filled_mask = binary_fill_holes(binary_mask)
        self.mask = filled_mask.astype(np.uint8) * 255
        labeled_mask, _ = label(filled_mask)
        self.mask = labeled_mask
        self.update_display()

    def relabel_objects(self):
        mask = self.mask
        labeled_mask, num_labels = label(mask > 0)
        self.mask = labeled_mask
        self.update_display()

    def clear_objects(self):
        self.mask = np.zeros_like(self.mask)
        self.update_display()

    def invert_mask(self):
        self.mask = np.where(self.mask > 0, 0, 1)
        self.relabel_objects()
        self.update_display()

    def remove_small_objects(self):
        try:
            min_area = int(self.min_area_entry.get())
        except ValueError:
            print("Invalid minimum area value; using default of 100")
            min_area = 100

        labeled_mask, num_labels = label(self.mask > 0)
        for i in range(1, num_labels + 1):
            if np.sum(labeled_mask == i) < min_area:
                self.mask[labeled_mask == i] = 0
        self.update_display()

def initiate_mask_app_root(width, height):
    theme = 'breeze'
    root = ThemedTk(theme=theme)
    style = ttk.Style(root)
    set_dark_style(style)
    set_default_font(root, font_name="Arial", size=8)
    root.geometry(f"{width}x{height}")
    root.title("Mask App")
    create_menu_bar(root)

    container = tk.PanedWindow(root, orient=tk.HORIZONTAL)
    container.pack(fill=tk.BOTH, expand=True)

    scrollable_frame = spacrFrame(container, bg='black')
    container.add(scrollable_frame, stretch="always")

    vars_dict = {
        'folder_path': ttk.Entry(scrollable_frame.scrollable_frame),
        'scale_factor': ttk.Entry(scrollable_frame.scrollable_frame)
    }

    row = 0
    for name, entry in vars_dict.items():
        ttk.Label(scrollable_frame.scrollable_frame, text=f"{name.replace('_', ' ').capitalize()}:").grid(row=row, column=0)
        entry.grid(row=row, column=1)
        row += 1

    def run_app():
        folder_path = vars_dict['folder_path'].get()
        scale_factor = float(vars_dict['scale_factor'].get())

        root.quit()
        root.destroy()

        new_root = ThemedTk(theme=theme)
        new_root.geometry(f"{1000}x{1000}")
        new_root.title("Mask Application")

        app_instance = ModifyMasks(new_root, folder_path, scale_factor)
        new_root.mainloop()

    create_dark_mode(root, style, console_output=None)

    run_button = spacrButton(scrollable_frame.scrollable_frame, text="Run", command=run_app)
    run_button.grid(row=row, column=0, columnspan=2, pady=10, padx=10)

    return root

def gui_make_masks():
    root = initiate_mask_app_root(330, 150)
    root.mainloop()

if __name__ == "__main__":
    gui_make_masks()
