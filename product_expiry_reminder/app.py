import streamlit as st
import os
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="ExpireAlert", page_icon="🕛", layout="centered")
st.title("🕛 Product Expiry Reminder App")
st.write("With **🕛 Product Expiry Reminder** App, you’ll always know which product is nearing its expiration date, giving you one last chance to use it before it's too late.")

class ProductExpiryReminderApp:
    def __init__(self, products_file="products.csv", images_folder="product_images"):
        self.products_file = products_file
        self.images_folder = images_folder

        self.category_images = {
            "Dairy 🧀": [os.path.join(self.images_folder, f"dairy{i+1}.png") for i in range(12)],
            "Refreshments 🥤": [os.path.join(self.images_folder, f"bev{i+1}.png") for i in range(12)],
            "Snacks 🍪": [os.path.join(self.images_folder, f"snack{i+1}.png") for i in range(12)],
            "Vegetables 🥦": [os.path.join(self.images_folder, f"veg{i+1}.png") for i in range(12)],
            "Fruits 🍎": [os.path.join(self.images_folder, f"fruit{i+1}.png") for i in range(12)],
            "Frozen ❄️": [os.path.join(self.images_folder, f"frozen{i+1}.png") for i in range(12)],
        }

        if not os.path.exists(self.images_folder):
            os.makedirs(self.images_folder)

    def load_products(self):
        if os.path.exists(self.products_file):
            return pd.read_csv(self.products_file)
        else:
            return pd.DataFrame(columns=["image_path", "name", "expiry_date", "category"])

    def save_product(self, product):
        df = self.load_products()
        df = pd.concat([df, pd.DataFrame([product])], ignore_index=True)
        df.to_csv(self.products_file, index=False)

    def get_expiry_status(self, expiry_date):
        today = datetime.today()
        expiry_date_obj = datetime.strptime(expiry_date, "%Y-%m-%d")
        delta = (expiry_date_obj - today).days
        if delta < 0:
            return "expired"
        elif delta == 0:
            return "expired_today"
        elif delta <= 5:
            return "soon_expire"
        elif delta <= 10:
            return "soon"
        else:
            return "ok"

    def delete_product(self, index):
        df = self.load_products()
        image_path = df.loc[index, "image_path"]
        is_category_image = any(image_path in imgs for imgs in self.category_images.values())
        if os.path.exists(image_path) and not is_category_image:
            os.remove(image_path)

        df = df.drop(index)
        df.to_csv(self.products_file, index=False)

    def display_add_product_section(self):
        st.write("###### ➕ Add New Product")

        if "selected_image" not in st.session_state:
            st.session_state.selected_image = None
        if "last_category" not in st.session_state:
            st.session_state.last_category = None

        category = st.selectbox("1️⃣ Category", ["Select Category"] + list(self.category_images.keys()))

        if category != st.session_state.last_category:
            st.session_state.selected_image = None
            st.session_state.last_category = category

        if category != "Select Category":
            st.write(f"Choose an image for **{category}**:")
            image_paths = self.category_images[category]
            cols = st.columns(6)
            for i, img_path in enumerate(image_paths):
                with cols[i % 6]:
                    if os.path.exists(img_path):
                        st.image(img_path, width=90, caption=f"Image {i+1}")
                        button_label = "✅" if st.session_state.selected_image == img_path else "⬜"
                        if st.button(button_label, key=f"select_{category}_{i}"):
                            st.session_state.selected_image = img_path
                            st.rerun()
                    else:
                        st.warning(f"Image not found: {img_path}")

        selected_image = st.session_state.selected_image if category != "Select Category" else None
        product_name = st.text_input("2️⃣ Product Name")
        expiry_date = st.date_input("3️⃣ Expiry Date")

        if st.button("➕ Add Product"):
            if product_name and category != "Select Category" and expiry_date:
                image_path = selected_image
                product = {
                    "name": product_name,
                    "category": category,
                    "expiry_date": str(expiry_date),
                    "image_path": image_path
                }
                self.save_product(product)
                st.success(f"✅ '{product_name}' added successfully!")
                st.session_state.selected_image = None
                st.rerun()
            else:
                st.error("⚠️ Please fill in all the fields and select an image.")

    def display_product_list(self):
        st.subheader("📦 Product List")
        products_df = self.load_products()

        if products_df.empty:
            st.info("📜 No products added yet.")
        else:
            products_df["expiry_date"] = pd.to_datetime(products_df["expiry_date"])
            products_df = products_df.sort_values(by="expiry_date").reset_index(drop=True)

            for index, product in products_df.iterrows():
                expiry = product['expiry_date'].strftime("%Y-%m-%d")
                status = self.get_expiry_status(expiry)
                days_left = (datetime.strptime(expiry, "%Y-%m-%d") - datetime.today()).days

                if status == "expired":
                    color = "gray"
                    message = "Product is expired"
                elif status == "expired_today":
                    color = "red"
                    message = "Product is expired today"
                elif status == "soon_expire":
                    color = "red"
                    message = f"🕒 {days_left} day(s) left - Expiring soon!"
                elif status == "soon":
                    color = "orange"
                    message = f"🕒 {days_left} day(s) left"
                else:
                    color = "green"
                    message = "Product is safe"

                col1, col2 = st.columns([1, 4])
                with col1:
                    if os.path.exists(product['image_path']):
                        st.image(product['image_path'], width=100)
                    else:
                        st.warning("Image not found")
                with col2:
                    st.markdown(f"### {product['name']} ({product['category']})")
                    st.markdown(f"**Expiry:** `{expiry}` — :{color}[{message}]")
                    if st.button(f"🗑️ Delete '{product['name']}'", key=f"delete_{index}"):
                        self.delete_product(index)
                        st.success(f"'{product['name']}' deleted!")
                        st.rerun()

    def show_expiry_notifications(self):
        products_df = self.load_products()
        if products_df.empty:
            return

        products_df["expiry_date"] = pd.to_datetime(products_df["expiry_date"])
        today = datetime.today()

        for _, product in products_df.iterrows():
            days_left = (product["expiry_date"] - today).days
            if 0 <= days_left <= 5:
                st.warning(f"⚠️ '{product['name']}' is expiring in {days_left} day(s)!")
            elif days_left < 0:
                st.error(f"❌ '{product['name']}' has expired!")

if __name__ == "__main__":
    app = ProductExpiryReminderApp()
    app.show_expiry_notifications()
    app.display_add_product_section()
    app.display_product_list()