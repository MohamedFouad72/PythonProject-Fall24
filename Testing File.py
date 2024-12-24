#Testing File
def open_menu_window(root):
    menu_win = tk.Toplevel(root)
    menu_win.title("Restaurant Menu")
    menu_win.geometry("900x700")
    menu_win.configure(bg="#161B33")

    # Load menu from file
    file_path = "menu.json"
    menu_items = load_menu_from_file(file_path)

    # Create a list attached to the menu window to keep references alive
    menu_win.image_refs = []

    create_navbar_buttonless_in_window(menu_win, root)

    # Scrollable Frame
    canvas = tk.Canvas(menu_win, bg="#161B33")
    scrollbar = tk.Scrollbar(menu_win, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#161B33")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    for category, items in menu_items.items():
        category_label = tk.Label(
            scrollable_frame,
            text=category,
            font=("Arial", 20, "bold"),
            bg="#161B33",
            fg="#FFFFFF"
        )
        category_label.pack(pady=10, anchor="w", padx=20)

        category_frame = tk.Frame(scrollable_frame, bg="#161B33")
        category_frame.pack(padx=20, pady=10, fill="x")

        for i, item in enumerate(items):
            item_frame = tk.Frame(category_frame, bg="#1F2C4D", bd=3, relief="raised")
            item_frame.grid(row=i // 2, column=i % 2, padx=10, pady=10, sticky="nsew")
            category_frame.columnconfigure(i % 2, weight=1)

            # Image Loading
            try:
                image_path = os.path.abspath(item["image"])
                if os.path.exists(image_path):
                    pil_image = Image.open(image_path).resize((150, 150))
                    tk_image = ImageTk.PhotoImage(pil_image)
                    menu_win.image_refs.append(tk_image)

                    img_label = tk.Label(item_frame, image=tk_image, bg="#1F2C4D")
                    img_label.pack(pady=5)
                else:
                    raise FileNotFoundError(f"Image not found: {image_path}")
            except Exception as e:
                print(f"Error loading image for {item['name']}: {e}")
                tk.Label(item_frame, text="[No Image]", bg="#1F2C4D", fg="white").pack(pady=5)

            # Item Name
            name_label = tk.Label(item_frame, text=item["name"], font=("Arial", 14, "bold"),
                                  bg="#1F2C4D", fg="white")
            name_label.pack(pady=2)

            # Item Price
            price_label = tk.Label(item_frame, text=f"${item['price']:.2f}", font=("Arial", 12),
                                   bg="#1F2C4D", fg="#AAAAAA")
            price_label.pack(pady=2)

            # Add to Cart Button
            buy_button = tk.Button(item_frame, text="Add to Cart",
                                   font=("Arial", 10, "bold"),
                                   bg="#4CAF50", fg="white")
            buy_button.pack(pady=5)

    # Example: Save menu when window is closed
    menu_win.protocol("WM_DELETE_WINDOW", lambda: save_menu_to_file(file_path, menu_items))
